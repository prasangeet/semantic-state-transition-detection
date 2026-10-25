
#!/usr/bin/env bash
set -Eeuo pipefail

# CLEVRER dataset downloader
# Works from any directory inside the repository.
#
# Download all resources:
#   bash scripts/download_clevrer.sh
#
# Download and extract archives:
#   bash scripts/download_clevrer.sh --extract

ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
DATA_DIR="$ROOT_DIR/data/raw/clevrer"
DOWNLOAD_DIR="$DATA_DIR/downloads"
QUESTIONS_DIR="$DATA_DIR/questions"

VIDEO_BASE="http://data.csail.mit.edu/clevrer/videos"
ANNOTATION_BASE="http://data.csail.mit.edu/clevrer/annotations"
QUESTION_BASE="http://data.csail.mit.edu/clevrer/questions"
DERENDER_URL="http://data.csail.mit.edu/clevrer/derender_proposals.zip"

mkdir -p "$DOWNLOAD_DIR" "$QUESTIONS_DIR"

for cmd in wget unzip; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Error: '$cmd' is required."
        echo "Install it and run this script again."
        exit 1
    fi
done

download_zip() {
    local url="$1"
    local filename="$2"
    local destination="$DOWNLOAD_DIR/$filename"

    if [[ -f "$destination" ]] &&
       unzip -tq "$destination" >/dev/null 2>&1; then
        echo "[OK] Archive already verified: $filename"
        return
    fi

    echo
    echo "[DOWNLOAD] $filename"
    wget -c --show-progress "$url" -O "$destination"

    if ! unzip -tq "$destination" >/dev/null 2>&1; then
        echo "[ERROR] ZIP verification failed: $filename"
        echo "Run the script again to retry/resume."
        return 1
    fi

    echo "[OK] Verified: $filename"
}

download_json() {
    local url="$1"
    local filename="$2"
    local destination="$QUESTIONS_DIR/$filename"

    if [[ -s "$destination" ]] &&
       python3 -m json.tool "$destination" >/dev/null 2>&1; then
        echo "[OK] JSON already verified: $filename"
        return
    fi

    echo
    echo "[DOWNLOAD] $filename"
    wget -c "$url" -O "$destination"

    if ! python3 -m json.tool "$destination" >/dev/null 2>&1; then
        echo "[ERROR] JSON validation failed: $filename"
        return 1
    fi

    echo "[OK] Verified JSON: $filename"
}

echo "======================================"
echo " CLEVRER Dataset Setup"
echo "======================================"
echo "Destination: $DATA_DIR"

# Video splits
download_zip "$VIDEO_BASE/train/video_train.zip" \
    "video_train.zip"
download_zip "$VIDEO_BASE/validation/video_validation.zip" \
    "video_validation.zip"
download_zip "$VIDEO_BASE/test/video_test.zip" \
    "video_test.zip"

# Object/event annotations
download_zip "$ANNOTATION_BASE/train/annotation_train.zip" \
    "annotation_train.zip"
download_zip "$ANNOTATION_BASE/validation/annotation_validation.zip" \
    "annotation_validation.zip"

# Question and answer JSON resources
download_json "$QUESTION_BASE/train.json" "train.json"
download_json "$QUESTION_BASE/validation.json" "validation.json"
download_json "$QUESTION_BASE/test.json" "test.json"

# Derender proposals
download_zip "$DERENDER_URL" "derender_proposals.zip"

echo
echo "======================================"
echo " All CLEVRER resources downloaded!"
echo "======================================"
du -sh "$DOWNLOAD_DIR" "$QUESTIONS_DIR"

if [[ "${1:-}" == "--extract" ]]; then
    echo
    echo "Extracting video and annotation archives..."

    for split in train validation test; do
        case "$split" in
            train)
                archive="video_train.zip"
                ;;
            validation)
                archive="video_validation.zip"
                ;;
            test)
                archive="video_test.zip"
                ;;
        esac

        mkdir -p "$DATA_DIR/$split"
        unzip -q -n "$DOWNLOAD_DIR/$archive" -d "$DATA_DIR/$split"
    done

    for split in train validation; do
        archive="annotation_${split}.zip"
        mkdir -p "$DATA_DIR/annotations/$split"
        unzip -q -n "$DOWNLOAD_DIR/$archive" \
            -d "$DATA_DIR/annotations/$split"
    done

    mkdir -p "$DATA_DIR/derender_proposals"
    unzip -q -n "$DOWNLOAD_DIR/derender_proposals.zip" \
        -d "$DATA_DIR/derender_proposals"

    echo "Extraction complete."
fi

echo
echo "CLEVRER setup finished."
