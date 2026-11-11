# OSCaR-Lite Evaluation Report

- Generated: 2026-11-10T15:43:03.941363+00:00
- Samples evaluated: 500

## Temporal Stage Metrics

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic Similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.3401 | 0.1626 | 0.0765 | 0.0373 | 0.2151 | 0.5576 |
| During | 0.3540 | 0.1768 | 0.0861 | 0.0433 | 0.2313 | 0.5543 |
| After | 0.3486 | 0.1683 | 0.0753 | 0.0321 | 0.2228 | 0.5332 |
| Transition | 0.3213 | 0.1728 | 0.0919 | 0.0531 | 0.2523 | 0.6095 |

## Temporal Alignment

- Overall temporal score: 0.5636

| Stage | Semantic Alignment |
|---|---:|
| Before | 0.5576 |
| During | 0.5543 |
| After | 0.5332 |
| Transition | 0.6095 |

## Qualitative Error Analysis

- Similarity threshold: 0.5000
- Low-similarity cases: 684

| Stage | Low-Similarity Cases | Rate | Mean Similarity |
|---|---:|---:|---:|
| Before | 181 | 0.3620 | 0.5576 |
| During | 180 | 0.3600 | 0.5543 |
| After | 208 | 0.4160 | 0.5332 |
| Transition | 115 | 0.2300 | 0.6095 |

### Cases for Manual Inspection

#### Sample 5 — Before

- Similarity: 0.4471
- Prediction: The countertop is cluttered with a variety of items, including a white ceramic bowl, a wooden spoon, and a small bowl. The counter is positioned in a position that is reminiscent of a kitchen counter, with contrasting surfaces and contrasting patterns. The countertop appears to be a modern kitchen, with its counters and counter tops positioned strategically on the counter. The surrounding area is a neutral, unadorned, white surface, with the counters stacked against the counter, indicating a recent or recent activity. The kitchen counter is in pristine condition, with no visible marks or markings, and the counter top is stacked in contrasting hues, suggesting a previous or recent action. The surface is bare,
- Reference: The floor is comprised of square, mustard-yellow tiles with slightly darker grout lines that create a grid-like pattern across the surface. In this scene, a few small, dark specks and light smudges are scattered across the tiles, indicating either bits of dirt or minor stains. The floor's glossy finish reflects some of the overhead lighting, which highlights the imperfections and the wear of the tiles, such as faint scratches and slight discoloration in places, suggesting this is a well-used area.

#### Sample 8 — Before

- Similarity: 0.4819
- Prediction: The coffee maker is positioned on a counter, with its lid open, indicating that it is in the process of being plugged in. The lid is a white, patterned plastic, with a metal handle, suggesting that it may be a microwave. The machine's interior is cluttered with unused items, including a pot, a bowl, and a small dish. The coffeemaker's lid is open, suggesting it may have been plugged into a power outlet. The surrounding area is bare, with no visible evidence of any activity.
- Reference: The toaster, with a reflective stainless steel surface, sits idly on a countertop, surrounded by ambient light. Its two slots are vacant, and there’s no visible sign of any toasted bread within. The toaster's temperature dial is at its midpoint, suggesting a medium toast setting, while the lever is in its uppermost position, indicating it hasn’t been pressed down. The power indicator light, located on the side, is not illuminated, suggesting that the toaster is currently off.

#### Sample 9 — Before

- Similarity: 0.4730
- Prediction: The tomato appears to be in the middle of a tomato, positioned in a position that is preparing to be sliced. The tomato is sliced in slicing motion, indicating that it has been sliced and is ready to be cut. The knife is positioned on the side of the tomato, suggesting that the knife is in the process of cutting the tomato. The tomatoes are positioned against the white background, suggesting the tomato has been cut into the desired shape. The camera's focus is on the tomato itself, which is a bright orange color, implying that it is being cut.
- Reference: The pepper, vibrant red in color, lies intact on the cutting board. Its skin is glossy, reflecting the light from the surrounding environment. The stem protrudes upward, indicating the top side of the vegetable, and the overall shape of the pepper appears robust and fresh, untouched by any cutting or slicing.

#### Sample 15 — Before

- Similarity: 0.3693
- Prediction: The jar is a solid, jumbo-sized, spherical, shaped, and topped with a large, rounded, curved edge. Its lid is positioned in a position that indicates it is in the process of being poured, indicating that the contents of the jar are still being drained. The rim of the container is firmly pressed against the edge of the lid, suggesting that the sloughing action is underway. The lid is slightly tilted, suggesting a slight movement, suggesting the blending process is underway, implying that the liquid has been poured into the jug. The liquid is filtered through the nozzle, suggesting it is still a
- Reference: In this scene, the stock appears to be at an early stage of preparation. The liquid's surface is slightly rippled, perhaps due to recent stirring, and a light sheen can be seen, hinting at the presence of oils or fats. The coloration of the stock is a pale yellow, suggesting it might be a chicken or vegetable broth. The glass containing the stock shows that the mixture is almost full, and there are no visible solid particles or ingredients, indicating a clear and potentially strained mixture.

#### Sample 20 — Before

- Similarity: 0.3009
- Prediction: The paper is positioned in a kitchen, with a white plate, a tin foil wrapped around it, and a hand holding it, indicating it is in the process of being sliced. The paper appears to be a thin, unbreakable piece of paper, with the edges of the paper revealing a slightly curved edge. The person holding the paper is likely preparing to slice it, with their fingers pointing at the paper, suggesting that they are preparing for a slice. The hand is likely holding the roll, which is likely to be the first slice to be cut, and the paper appears poised to be in the middle of the unfolding process. The hands are likely attempting to slice the paper in slic
- Reference: The yogurt in this frame appears to be in a state of being intentionally arranged. One can observe that a hand is positioning a yogurt container, which is upright and has a lid depicting some form of fruit, likely indicating the flavor. The placement is precise and seems to be part of an organized pattern, with two other yogurt containers already placed in proximity: one upright and another on its side, possibly to showcase the brand or variety. The environment suggests that the action is taking place in a kitchen, given the presence of a microwave, stove, and various kitchen items in the background.

#### Sample 21 — Before

- Similarity: 0.3837
- Prediction: The halibut is positioned in a kitchen sink, with a thin layer of steamed broccoli florets pointing to the kitchen sink. The slicked edges are reminiscent of a slender, overlapping leaf, with the stems extending outwards. The water is a little damp, but the halved portion of the slop appears to be soaking wet. The leaves are a bit damp, with some wilted leaves indicating they're being prepared for cooking. The leafs are positioned on a plate, with their stems visible, indicating that they've been boiled. The hands are pointing at the sliced hale,
- Reference: The pak choi leaf appears fresh and vibrant, with a distinct green hue. It is mostly submerged in a stainless steel bowl filled with water, with droplets of water cascading over its surface from the tap. The leaf's broad, flat structure showcases its venation pattern, and it seems to be in the initial stages of being rinsed, given its position under the tap.

#### Sample 22 — Before

- Similarity: 0.3116
- Prediction: The chicken is in a state of being sliced, with the skin firmly pressed against the skin, suggesting a gradual process. The skin is a dark brown, with a thin layer of skin on the inside, suggesting that the meat has been partially cooked. The flesh is ripe, with its fleshy appearance indicating that the skin has been soaked in saline. The knife's edge is positioned slightly above the skin to indicate that the knife is preparing to slice the meat. The hand's fingers are positioned on the side of the skin suggesting that they are preparing the meat to be sliced.
- Reference: The garlic press appears to be in the initial stages of use, with a clove of garlic placed within its chamber. The device is oriented horizontally, held firmly in the user’s hands over a pan containing uncooked spaghetti. The handles of the garlic press are slightly apart, suggesting that the squeezing action has just begun. The press itself is constructed of metal, likely stainless steel, with a grid of small holes at its head through which the garlic will be extruded. The user's grip is confident, indicating the commencement of the pressing process.

#### Sample 23 — Before

- Similarity: 0.4359
- Prediction: The wok is placed in a kitchen sink, with a handle pointing downwards, indicating that it is in the process of being cleaned. The wow's surface is cluttered with crumbs, resulting from the presence of a clinging or scrubbing device, implying that the wok has been soiled. The surface is covered with mud, suggesting that the water has been running, a sign that the kitchen is in resurgence. The water's slick surface is visible, suggesting the wow is a recent one.
- Reference: The pan appears to be under a stream of clear, flowing water from the tap. It's being held at an angle, allowing the water to flow directly into it. Around the pan, there's a residual presence of water droplets, indicative of a recent rinse. The pan's inner surface has a reflective sheen from the water, and it seems to be devoid of any significant food particles or residue. The overall impression is of an initial rinsing phase, as the person prepares to scrub or clean it more thoroughly.

#### Sample 24 — Before

- Similarity: 0.3252
- Prediction: The sandwich is positioned in a kitchen, with a white plate, a plastic bag, and a spherical shape. The sandwich has a rectangular shape, with the top portion of the sandwich positioned on top of the other side, indicating a previous meal. The bread is sliced, with its edges slightly exposed, suggesting a recent meal.
- Reference: A pair of scissors is opened and inserted into a notch of a blue plastic clip, which is mounted on the edge of a packet labeled "Funghi Porcini". The scissors' handles are blue, and the blades silver, with one blade partially inserted into the clip's opening. The person holding the scissors appears to be right-handed, as inferred by the thumb and fingers' positioning. The clip is halfway along the length of the packet, suggesting the intention to either open or reseal it. Surrounding the scene are various kitchen items, including dishes in an orange drying rack, a roll of paper towels, and a white napkin.

#### Sample 26 — Before

- Similarity: 0.4939
- Prediction: The paper is a white, opaque, opaque material with a dark hue, indicating it has been pressed into the paper. The paper's surface is bare, with no visible markings or markings, suggesting it is being handled. The person's hand is positioned in a position to grasp the paper, which is likely a hand holding the paper in resembling a spoon. The material appears to be a thin, unbreakable, paper-like material, with traces of a crease or a fold, suggesting the paper is being pressed against the paper'
- Reference: The cling film appears tightly wound around a yellow cylindrical cardboard tube, its roll relatively untouched and pristine. It's gripped firmly in a person’s hands, one thumb positioned near the film’s end, suggesting preparation for unrolling. The film itself shows no signs of stretching or distortion, and the plastic’s translucent sheen is consistent, reflecting the light evenly, indicating it has not yet been pulled or manipulated.

#### Sample 28 — Before

- Similarity: 0.4737
- Prediction: The white plate appears to be a white plate with a yellowish hue, indicating it is in the process of being cleaned. The surface is a dark brown, with hints of a smoky or muddy color. The plate is positioned in a position that indicates it is being cleaned, with the plate positioned on top of it, presumably to prevent any spills. The person holding the plate is likely a professional or a beginner, and the plate appears likely to be in the middle of preparing to clean it. The table is surrounded by a series of white objects, including a kitchen towel, a dish towel, and a bowl. The object appears to have been thrown at the plate,
- Reference: The sheet of paper is grasped firmly in the person's right hand, held vertically, with the bottom edge parallel to the drawer's edge and the top edge oriented upwards. The hand appears to be in the initial phase of tearing, with the fingers positioned in a way that suggests force is about to be applied. The paper itself looks pristine, uncreased, and undamaged, with its white surface catching the light, indicating a smooth, possibly new sheet. There is no visible wear or prior folding, and the edges are crisp and straight.

#### Sample 30 — Before

- Similarity: 0.3724
- Prediction: The chicken is placed in a pot of boiling water, indicating it is still in the cooking process. The water is dripping from the bottom of the pan, resulting in clumps of food particles forming a cloudy, hazy mess. The chicken's surface is covered with a thin layer of water, suggesting it is soaking for a while. The surface of the chicken is covered in mud, suggesting that it is being boiled. The surrounding area is cluttered with mud and debris, suggesting a recent cooking process is underway.
- Reference: The colander is positioned above the left sink basin, securely held by a hand enveloped in a yellow rubber glove. It appears to be filled to the brim with freshly rinsed rice grains that are clumped together, suggesting that the rice has just been washed and is possibly still absorbing water. The colander itself is metallic, with a pattern of round perforations throughout, ideal for draining water while retaining the small grains. Light reflects off the wet surfaces of the colander and the rice, indicating the presence of moisture.

#### Sample 31 — Before

- Similarity: 0.4580
- Prediction: The countertop is a white, glossy surface with a light brown hue, indicating a recent cleaning. A hand is demonstrating a hand-held device, pointing at the counter, a slat or a small piece of paper, presumably a paper towel. The counter appears to be a clean, uncluttered one, with traces of food and other items scattered around. The surface is cluttered with crumbs, crumbs and other debris, implying a cleaning process is underway. The countertop appears to have been cleaned, with the residue indicating that it has been wiped down. The hand is seen attempting to clean the countertop, highlighting the presence of crumbs or other debris. The object in the frame is
- Reference: The glass, appearing to be a standard pint-size, is situated upside down on the tabletop, its opening facing down. The translucent material suggests it's made of a typical glass composition, possibly indicating recent usage as there are no visible residues on its inner surface. The base of the glass, now at the top, reflects a smidgen of light, hinting at a relatively clean and glossy finish. The glass is positioned slightly off-center to the left in the viewer's perspective, with ample space around it, undisturbed and static in its placement.

#### Sample 36 — Before

- Similarity: 0.2742
- Prediction: The sandwich is positioned in a kitchen, with a knife in its middle, a slicing knife in the middle, and a hand in its right hand, pointing to the knife's edge. The knife'd edge is a sharp edge, suggesting a slight movement, indicating the bread has been sliced. The sandwich's surface is cluttered, with the edges of the sandwich revealing a thin, uncooked portion. The bread is stacked against a wall, with its edges overlapping, suggesting the bread is being prepared. The hand's fingers are positioned on the edge of the bread, suggesting that the bread may be a light or medium-sized portion, implying a medium-size portion
- Reference: The butter is encased in a rectangular plastic tub with a bright blue lid, prominently featuring the brand "FLORA" and a sunflower image indicating a light, sunflower-based spread. The lid is securely attached, showing no signs of having been opened. The spread inside is unseen, implying a fresh, untouched state. The tub rests on a kitchen counter, held firmly by a left hand, with the right hand holding a butter knife poised to lift the lid, indicating an imminent action of usage.

#### Sample 41 — Before

- Similarity: 0.2662
- Prediction: The microwave door is positioned in a kitchen, with a door open, suggesting a person's hand is attempting to open it. The door is partially closed, suggesting that the microwave is not fully open. The kitchen is cluttered with cluttered items, including a dish, a pot, and a microwave basket. The cabinet's interior is a dark, cluttered space, with its interior cluttered and cluttered. The surrounding area is occupied by a variety of objects, including the kitchen counter, displaying a cluttered kitchen counter and displaying various items, such as a glass dish, and the kitchen sink.
- Reference: The milk bottle, with a classic white and yellow design suggesting a standard pasteurized variety, rests on its side near the kitchen sink's edge. Its cap, a vibrant red that contrasts starkly with the bottle's muted tones, is partially obscured from view, suggesting it may not be fully secured. Shadows cast across the bottle indicate ambient lighting from above, and a slight reflection hints at the bottle's glossy surface, likely plastic. The positioning of the bottle, coupled with nearby kitchen items, gives the impression of a hurried or cluttered setting.

#### Sample 43 — Before

- Similarity: 0.4707
- Prediction: The coffee is in a glass bowl, with a lid positioned at the center of the bowl, indicating that it has been placed in ice water. The cup is surrounded by a thin layer of ice, suggesting that it is still in the liquid phase, suggesting a gradual process. The coffee's texture is reminiscent of a coffee filter, with the frothy consistency of whipped cream, suggesting the coffee is still a bit soft. The glass bowl is positioned in icy water, suggesting it is a medium-sized coffee filter. The spoon is pointing at the coffee, suggesting its presence is likely to be a small amount, suggesting an initial stirring. The hand is indicating a steady motion, suggesting there
- Reference: The sugar jar appears closed and placed to the left of a hand mixer and a box of tea, just in front of a power strip crowded with various plugs. It's a clear jar with a visible fill line of sugar, indicating it is nearly full. The lid is white with a flip-top mechanism that is currently in a closed position, securing the contents within. The jar sits on a kitchen countertop made of speckled grey material, and there is an assortment of kitchenware and other items in the immediate vicinity.

#### Sample 51 — Before

- Similarity: 0.4143
- Prediction: The bin appears to be in a position of a sorting device, indicating that it is in agitation, suggesting that the bin is in motion. The bin's lid is positioned in oblique motion, suggesting a motion-induced movement. The lid is partially open, suggesting the bin has been placed in pause mode. The surrounding environment is a blurry, hazy environment, suggesting an activity or activity. The nearby bin is presumably a kitchen item, suggesting it may be a food container.
- Reference: The image captures a cylindrical filter component, partially obscured by the person's hand as they are in the midst of removing or inspecting it. The filter's exterior is predominantly white, with some areas of discoloration, suggesting it may have accumulated dust or other particulate matter. The top portion of the filter appears to be a semi-transparent material, possibly a fine mesh designed to trap contaminants. The texture of the surface suggests a fibrous material, commonly used in filters to enhance their trapping capability. There is visible debris collected on the filter's surface, indicating it has been in use and is performing its function of purifying the air or water it is designed for.

#### Sample 57 — Before

- Similarity: 0.3626
- Prediction: The pot is positioned in a kitchen sink, with a lid positioned at the top, indicating that it is in the process of being filled. The lid is a white, patterned one, with an orange or green color, suggesting that the pot is in re-filling mode. The pot's interior is cluttered with utensils, including a pot holder, a bowl, and a sink. The sink is surrounded by a series of utmostly stacked pots, presumably aimed at a single pot. The kitchen sink is in an area with slats, which indicate that the water has been boiled. The water level is moderate, suggesting a low level
- Reference: The coffee filter is depicted being held at a slight angle above the coffee maker. It appears to be a used filter, given the dark, wet coffee grounds that fill it to near capacity, suggesting a recently completed brewing cycle. The filter's structure, a basket shape with radial ribs, indicates that it is designed to fit snugly within the coffee maker's compartment. A few coffee grounds have spilled onto the machine's surface, and the filter's rim is stained, showing signs of frequent use.

#### Sample 60 — Before

- Similarity: 0.4027
- Prediction: The scrubbing pad is positioned in a position that is agitated by the water, indicating that it is in the process of being washed. The surface of the slat is a dark, reflective, hazy, smoky, and abrasive, suggesting that the water has been dripping from the tap. The nozzle is angled downwards, suggesting a sprinkling of water, which indicates that the nozzle has been placed in resevoir. The water is drained from the faucet, suggesting the water is still running. The faucet is swung downwards to indicate that the tap is still wet, suggesting an ongoing process.
- Reference: The coffee pot appears to be positioned on a metal drainage area adjacent to the sink, with water droplets and residual soap suds on its surface. The pot's lid is not in its fully closed position, potentially suggesting that it was recently opened or cleaned. The pot's handle seems to be held, implying active engagement with it, perhaps in the process of rinsing or cleaning.

#### Sample 62 — Before

- Similarity: 0.3028
- Prediction: The flour appears to be a light brown, clump of a mixture of flour and a granulated sugar, suggesting that it is still a bit sticky. The texture of the dough appears to have been a little rough, suggesting it may be preparing for a quick meal. The consistency of the flour appears slightly sticky, suggesting a slight clubbing or a sticky texture. The flour's texture is reminiscent of sand, suggesting the flour may be slightly clumped or clunky. The dough appears slightly moist, suggesting some movement, possibly a hand or kneading, indicating the dough may be ready for use.
- Reference: A bottle of olive oil is introduced into the scene, appearing on the right side of the image, held by a hand with fingers wrapped around its neck. The bottle cap is still on, indicating the oil has not yet been used. The label is facing away from the camera, obscuring the brand and specific type of olive oil. The bottle is tilted at a slight angle, suggesting the person is about to pour the oil into a bowl containing a mixture, likely in preparation for adding the oil to the ingredients. The surrounding area is cluttered with various cooking utensils and containers, but the focus is on the imminent action of pouring.

#### Sample 63 — Before

- Similarity: 0.3757
- Prediction: The tomato appears to be a light green, with a slightly smoky hue, suggesting it has been sliced. It is a thin, uncooked piece of tomato, with no visible seeds or traces of any kind, suggesting that it may have been slicked. The tomato is positioned in a position that indicates it is being prepared, suggesting a fresh, ripe tomato. The texture of the tomato appears slightly greasy, suggesting the tomato may have a slight sponginess, suggesting its texture may have changed slightly. The tomatoes are positioned on a plate, indicating that they are being prepared. The kitchen staff is preparing the tomato, which is presumably a large, rectangular piece of lettuce, with
- Reference: A bowl sits on a countertop cluttered with various kitchen appliances and items, holding a mixture that appears to be in the initial stages of preparation. In the bowl, there is a raw egg, its yolk intact and sunny, surrounded by a clear viscous albumen, with flecks of black pepper scattered throughout, providing a stark contrast to the pale yellow and translucent whites. The egg has been cracked open recently, as suggested by the lack of disturbance in the albumen and the yolk's domed shape, indicating minimal interaction with the fork lying beside it.

#### Sample 69 — Before

- Similarity: 0.4845
- Prediction: The onion appears to be sliced in half, with the skin positioned on top of the onion, indicating that it is in the process of being cut. The knife's edge is a sharp edge, suggesting that the onion has been cut in half. The onion is sliced, revealing a smooth, smoky texture, suggesting a ripe or charred portion. The skin is reminiscent of a freshly cut onion, with a thin layer of flesh surrounding the edges, suggesting the onion may be a medium-sized piece of onion. The image is framed by a white, reflective surface, suggesting an uncooked onion.
- Reference: A yellow bell pepper rests on a cutting board, partially sliced by a person whose hands are visible in the frame. The pepper's top has been removed, and it is lying on its side, oriented diagonally across the board. The blade of a knife is in contact with the pepper, positioned mid-cut through a segment, suggesting the motion of chopping. There are multiple slices of the pepper already cut, fanned out slightly on the board, indicating that the chopping process is underway.

#### Sample 71 — Before

- Similarity: 0.2898
- Prediction: The fabric is a dark, smoky color, with a light-colored hue that is reminiscent of a sandpaper. The fabric appears to be a mixture of squishy and abrasive, with the fabric indicating a gradual process. The brush is positioned in a position that is likely to be used to clean the fabric, indicating that the fabric has been thoroughly washed. The cloth is slouchy, with its surface revealing a smooth, textured surface. The surrounding fabric is in pristine condition, with no visible marks or imperfections. The surface of the fabric is slightly damp, with some areas showing signs of stains or adsorption. The area is
- Reference: The degreaser in question appears to be in a state of rest, positioned on a clean, off-white tabletop. The bottle is upright, with its nozzle directed upwards, and no visible spray is being emitted. Its label is facing away from the viewer, obscuring any brand or usage instructions that may be present. The cap seems to be firmly attached, and the trigger is in a neutral position, suggesting it hasn't been recently pressed. The surrounding area is free of any visible residue or signs of degreaser application, indicating that the cleaning action has yet to commence.

#### Sample 73 — Before

- Similarity: 0.3597
- Prediction: The gas burner is positioned on a stovetop, with a handle pointing downwards, indicating it has been agitated. The burner is covered in a thin layer of liquid, resulting in clumps of scalding particles. The flame appears to be a mixture of hot and cold, with the liquid eroding the surface of the burner. The person's hand is demonstrating a gentle motion, pointing to the burner, which is likely a part of the cooking process. The blades are positioned in varying positions, forming a curved, circular shape, implying a gradual movement. The surface of this burner appears to have been soiled, revealing a visible
- Reference: The grid is held at a diagonal angle, with the top right corner slightly elevated compared to the bottom left, creating a visible slant across the image. The fingers of the right hand are wrapped around the top edge, securing it with a firm grip, while the thumb extends towards the center to stabilize the position. The grid's metal rods gleam with moisture, indicating recent cleaning or contact with water, and droplets are scattered across the surrounding sink area, reflecting the grid's recent movement.

#### Sample 74 — Before

- Similarity: 0.4606
- Prediction: The white substance is a white, spongy, clumpy, and slightly sticky, suggesting it has been sprayed with a light coating. The surface is cluttered with crumbs, which are likely to be a mixture of flour and a few other ingredients, suggesting that the substance may be preparing for cooking. The object is positioned on a plate, indicating that it is preparing to serve, implying that the person is attempting to serve. The white material is reminiscent of a sandpaper, which is likely to have been thrown onto the surface, suggesting a slight smudge or a small amount of flour. The surrounding area is occupied with slender, overlapping
- Reference: The scale is a compact, digital model with a clear glass platform, resting on a black granite countertop. It is positioned to the right side of the bowl filled with a white powdery substance, presumed to be flour. The scale appears to be turned off, as no digital numbers or lights are visible on its display. It is situated next to an open notebook, with its top edge aligned with the spiral binding, suggesting that it might be used for recording measurements. Surrounding the scale are scattered ingredients and kitchen tools, indicating an ongoing cooking or baking process.

#### Sample 77 — Before

- Similarity: 0.2602
- Prediction: The button appears to be in a position where it is positioned in solitary motion, indicating that it is in re-entry. The button's surface is a dark, reflective, hazy, white, and opaque, suggesting that it has been pressed, pressed or pressed. The fingernail is pointing at the button, suggesting it is still in the position of a hand, implying that it's pressed against the button. The hand is firmly pressed on the button'
- Reference: The milk container is initially captured with the lid firmly secured on top. The smooth, white surface of the container suggests that it's made of plastic, and it appears to be a standard size, suggesting it may contain a liter or so of milk. The container is grasped by a hand, presumably in preparation for opening.

#### Sample 84 — Before

- Similarity: 0.4795
- Prediction: The microwave is positioned on a kitchen counter, with a white plate in the middle, a glass plate in front of it, and a small bowl in the center. The microwave has a metal handle, which indicates it is a microwave oven, and the lid is firmly attached to the microwave. The kitchen counter is cluttered with utensils, including a dish towel, mug, and other items. The countertop is adorned with patterned ceramic tiles, which are reminiscent of a tiled kitchen counter. The surrounding area is occupied by a person's hand, which is likely a hand holding the microwave, and there is hardly any visible movement in the kitchen. The counter is in a dark, dark
- Reference: A hand is reaching towards the toaster's power plug, which is connected to a white double socket mounted on a tiled wall above a gray countertop. The toaster itself is a four-slice model with a metallic finish, reflecting the ambient light of the room. It sits idle with its control knobs turned to a neutral position, and the bread slots appear empty. To the right of the toaster, there's a clear plastic container and a colorful cutting board with the words "SLICE," "CHOP," and "PEEL" in a playful typography, hinting at food preparation activities.

#### Sample 86 — Before

- Similarity: 0.4165
- Prediction: The bag appears to be a plastic bag, with a white label on the side, suggesting it is a bag with slender or rectangular shape. The bag's interior is cluttered, with the contents of the bag being visible, including a handful of food and a few items. The person's hand is likely a beginner, with her hands pointing at the bag, suggesting a quick grasp. The camera's focus is on the bag'
- Reference: The leek, freshly uprooted from its packaging, appears in the process of being transferred, likely from a shopping bag onto a household surface, possibly in preparation for storage or cooking. It's held at one end, with the root tip facing downwards, suspended mid-air, showcasing its full length and firm, layered structure. The white base transitions into a deep green, with the tightly wrapped, flat leaves that are characteristic of leeks. The plastic wrap encasing it is slightly puckered, indicating the initial grip that preceded the motion captured.

#### Sample 89 — Before

- Similarity: 0.1780
- Prediction: The door appears to be open, with a gaping gap in the middle of the frame, suggesting a gradual movement. The door is positioned in a position that is not visible in the first frame, indicating that the door is open. The surrounding area is cluttered, with no visible objects or objects in the background. The light source is visible, suggesting that the light is coming from the outside, implying that the room is not fully lit. The lighting is dim, suggesting the room may be a dark room, suggesting there may be some lighting in the room. The room is framed by a wall, which is a focal point, suggesting it is anchored to the wall. The adjacent door is not seen, suggesting an opening or a
- Reference: The squash container, predominantly white with touches of blue, rests atop a gray counter. It stands upright, showcasing its slender and elongated design. The label, although not entirely discernible, carries hints of blue and green graphics, likely illustrating the flavor or variety of the squash. Adjacently, a white cap lies on the counter, suggesting it's been recently removed or will be placed back on the container.

#### Sample 90 — Before

- Similarity: 0.4229
- Prediction: The avocado appears to be ripe, with a thin, slightly slender, fleshy appearance. Its skin is a vibrant orange, with the flesh apricot-shaped, indicating it has been sliced. The avocado is positioned in a slicing position, with its flesh positioned against the side of the avocado, implying a pre-cooking process. The knife's edge is firmly held, with an open edge indicating the knife is preparing to slice. The fruit appears to have been steamed, with some smoky spots and a light coating of juice on the outside. The flesh appears to resemble a freshly squeezed lime, with visible veins of
- Reference: The pepper is positioned on a wooden cutting board, cut-side down with its stem end facing left, indicating that an initial slice has been made to separate it into two halves. Its vibrant yellow skin is smooth and shiny, reflecting the light, with a slight variance in hue, suggesting natural rippling or indentations. The interior is not visible in this frame, but the intact silhouette suggests the seeds and inner membranes are likely still present.

#### Sample 91 — Before

- Similarity: 0.4486
- Prediction: The holder of the coffee pot appears to be in a position where it is positioned in swivel motion, with a hand grip pointing downwards. The handle is angled downwards, indicating that the water has been drained. The water's surface is a reflective, hazy color, suggesting that the coffee is being boiled. The nozzle of the holder is pointing upwards, suggesting a brewing process. The faucet is aimed downwards and the water'
- Reference: The burner cap is situated in the left basin of a stainless steel double sink, surrounded by several other stove components that are likely soaking in water. The cap appears heavily coated with residues, indicative of consistent use without recent cleaning. Water droplets scattered around the cap suggest a recent rinse, yet the cap's surface remains dulled by accumulated grime. The wear is evident, with the matte finish on the cap's surface contrasting sharply with the metallic sheen of the sink and the gloss of the wet stove parts.

#### Sample 92 — Before

- Similarity: 0.4801
- Prediction: The sink is positioned in a position that is cluttered with a variety of items, including a dish towel, a bowl, and a sink utensil. The sink's surface is a dark brown, with traces of rust, suggesting that it may be a clogged sink. The faucet is surrounded by a series of items that are positioned near the sink, including dishes, utilities, and other items. The water level is moderate, suggesting a moderate amount of water. The surrounding area is reminiscent of a kitchen, with the sink'
- Reference: A porcelain plate rests precariously on a white plastic dish drainer, tilting towards the edge, as if caught mid-movement. Its surface is glossy, reflecting the light overhead, indicating either a clean sheen or the presence of water. The plate’s rim is designed with a delicate curve, suggesting a subtle elegance. Its bottom is partially visible, and the brand mark is faintly discernible, implying a bottom-heavy tilt that could cause it to slip off the rack. The dish drainer's slats cast linear shadows on the plate's surface, adding to the sense of it being in a transient state.

#### Sample 96 — Before

- Similarity: 0.3738
- Prediction: The saran wrapper is positioned in a kitchen, with the lid firmly attached to the top of the container, indicating that it is in the process of being opened. The person's hand is pointing at the samurai-style portion of the taser, which is a curved, curved shape with a slight bend in the middle. The tasser is shaped like a small sash, with curved edges and a slightly curved edge, suggesting that the holder is preparing to open. The lid is firmly pressed against the rim of the bag, suggesting the person is attempting to open the utensil. The contents of the pouch are
- Reference: The packaging appears to be a vacuum-sealed plastic container with a prominent orange hue indicating the presence of salmon. The seal is intact, suggesting that the packaging has not yet been opened. The clear plastic molds closely around the contours of the fish, highlighting its size and shape. This type of packaging is often used to preserve the freshness of seafood. The person is holding the package with both hands, preparing to open it.

#### Sample 100 — Before

- Similarity: 0.3871
- Prediction: The door appears to be open, with a gaping gap in the middle of the frame, suggesting a possible opening. The door is positioned in a position that is likely to be a part of the kitchen, indicating that the door is open. The surrounding area is cluttered, suggesting that the room is not fully occupied. The interior of the door appears cluttered and unadorned, suggesting the door may be open.
- Reference: The image captures an illuminated environment where light diffuses softly across various surfaces, indicating an active light source within the room. The light reflects off the tiled flooring, creating a pattern of highlights and shadows that suggest a glossy finish on the tiles. The countertop to the right also catches the light, indicating its polished surface, and various kitchenware items reflect the light differently, from the metallic sheen of pots and pans to the more subdued reflection of ceramic dishes. The light appears to be emanating from a point above the scene, casting a consistent glow across the room.

#### Sample 101 — Before

- Similarity: 0.4833
- Prediction: The jar appears to be in a kitchen, with a bowl of ice cream in the middle, a glass container with ice in the center, and a spoon in the centre. The ice appears to have been poured into the bowl, indicating that it is ready to be poured. The spoon's surface is a dark brown, revealing a smooth, frosted surface, suggesting that the ice has been dipped in ice water. The container is positioned in icy, icy conditions, suggesting a cold or hot liquid, implying a hot or cold liquid. The bowl appears to contain ice, suggesting it may be a chilled or hot beverage, presumably a liquid-based
- Reference: The milk in the container appears to be in an initial stage of stirring, with the surface showing a mild disturbance. There is a visible swirl starting to form, indicating the motion of a spoon or a stirrer recently having passed through it. The consistency of the milk seems uniform and no significant mixing of any added ingredient is apparent yet. The color is a uniform creamy white, and the viscosity appears to be typical of milk, without any signs of thickening or curdling.

#### Sample 107 — Before

- Similarity: 0.4884
- Prediction: The dough appears to be in a relatively early stage, with a light coating of flour and a thin layer of granules forming a dense, sticky paste. The texture is reminiscent of a dough, with the dough clumping together, indicating that it is still a bit sticky. The dough is a little sticky, with some lumps indicating a more seasoned texture. The consistency is slightly sticky, suggesting that the dough may be a softer dough than it should be.
- Reference: The biscuit appears to be in its initial stage of being pressed, with its texture still visible, suggesting that it has just begun to be mixed or crushed. It's surrounded by an assortment of kitchen appliances and utensils, indicating that preparation is underway. The area looks cluttered, with a glass of something powdery next to the bowl, possibly an ingredient yet to be added. The biscuits retain their integrity to some extent, as the pressing has seemingly just commenced.

#### Sample 109 — Before

- Similarity: 0.3484
- Prediction: The kitchen counter appears to be positioned in a position that is positioned at a slight angle, indicating that the counter is currently being worked on. The counter is stacked against a wall, with a white surface, suggesting that the countertop is currently in resemblance to the counter. The countertop is a dark brown, with an orange hue, suggesting a light or dark color. The kitchen sink is anchored to the wall, suggesting the countertop has been wiped down. The table is surrounded by a series of wooden furniture, including a wooden table, a chair, and a tablecloth. The surface of the counter appears cluttered, suggesting there is hardly any room for the counter to be placed. The lighting is
- Reference: A rubber glove, seemingly of a durable material and a vivid yellow hue, is placed on the edge of a wooden cutting board that is resting on a kitchen countertop. The glove's fingers are splayed outwards, revealing its inner surface and suggesting it has recently been removed. Adjacent to the glove is a blue cutting board, which bears marks of use, a testament to recent culinary activity. A spoon and a knife lay on the blue board, indicating a pause in meal preparation or the aftermath of cooking.

#### Sample 110 — Before

- Similarity: 0.3387
- Prediction: The kitchen counter appears to be in a position to be positioned in, suggesting that it is in resemblance to a kitchen counter. The counter's surface is cluttered, with a white surface, indicating a clean counter surface. The countertop is positioned on a counter, presumably a countertop or countertop, suggesting a place to place the counter. A hand is seen pointing at the counter, suggesting it is a hand with utensils or a spoon. The kitchen is surrounded by a series of white objects, including a wooden spoon, a jar, and a small kitchen towel.
- Reference: The chair appears in a position where it is partially tucked under a table. The tablecloth is colorful with a pattern, resting on a table with a light-colored surface. The chair itself has a cushioned seat with a light fabric, and the backrest is not visible in this angle. The floor is tiled, reflecting the chair's shadow and some light. The chair is angled such that one leg is closer to the camera, suggesting it may have been in motion or is about to be moved.

#### Sample 112 — Before

- Similarity: 0.4838
- Prediction: The box appears to be a plastic bag, with a lid that is partially open, suggesting that the contents are being thrown out. The lid is positioned in a position that indicates that the bag is being emptied, indicating that the person is attempting to open the bag. The bag's interior is cluttered, suggesting a gradual movement, and the contents of the bag are likely to be in the hands of the person attempting the action.
- Reference: The image captures a blur of movement, likely due to the camera's swift motion. Amidst this swirl of colors and shapes, the focus is on a partially visible bag of coffee. The bag is not clearly discernible, but the slight crinkling texture suggests it may have been recently handled or is in the process of being moved. The surrounding environment is a jumble of kitchenware and appliances, all blending into the scene's dynamic and hasty vibe.

#### Sample 116 — Before

- Similarity: 0.3873
- Prediction: The bowl appears to be a white, slender one, with a slightly curved edge, suggesting a sprinkling of a small amount of flour or other flour. The bowl is positioned in a position that indicates a slight movement, with the bowl positioned slightly above the bowl, suggesting that the bowl is still in the middle of the bowl. The kitchen staff is presumably preparing to serve the bowl to the camera, indicating that the person is preparing the bowl and is unsure of what the bowl's contents are.
- Reference: The ingredients appear to be in the early stages of preparation. A variety of food items are visible, most notably diced sweet potatoes that are collected inside a white bowl. On the countertop, there's evidence of fresh preparation with discarded peels and cut-offs from what seems like vegetables and fruits. To the side, there's a knife resting on a chopping board, indicating recent use. Some other ingredients, like canned goods and possibly some spices or seasonings, are also present nearby.

#### Sample 118 — Before

- Similarity: 0.3771
- Prediction: The vegetables are positioned in a pan, indicating that they are in the process of being sliced. They are stacked on a table, displaying a variety of vegetables, including broccoli, cauliflower, and cauliflower, all sliced in varying sizes, ranging from medium to large. The vegetables appear to be ripe, with a slight hint of a slicing, suggesting that they may be ready to be cooked. The pan is cluttered with steamed vegetables, implying that they have been boiled, resulting in clumps of vegetables that appear to have been cooked, forming a tight, overlapping mass. The ingredients are arranged in contrasting hues, suggesting they may have been freshly
- Reference: The hob presents a white stove with four gas burners of varying sizes, organized in a traditional layout with two rows and two columns. The burners are capped with black grates, suitable for holding cookware securely. In this scene, a wok is placed on the front right burner, filled with a mix of vegetables that appear to be in the early stages of cooking, indicated by their vibrant colors and rigid textures. The knobs for gas control are aligned on the front panel, each corresponding to one of the burners. The control knob for the wok's burner is turned on, suggesting an active flame heating the pan. A spoon rest lies empty next to the hob, and the wooden countertop that surrounds the stove is clear of any other kitchen utensils or ingredients.

#### Sample 119 — Before

- Similarity: 0.4366
- Prediction: The sanitized spoon appears to be in a water bath, with a sprinkling of soapy water on the surface. The spoon is positioned in resembling a bowl, with the handle pointing downwards, indicating that it is in the process of being washed. The water is dripping from the spoon, resulting in scalding and a slight smudge on the bottom. The resulting liquid is likely to be a detergent, a solution that is likely being rinsed.
- Reference: The V60 coffee dripper appears fully immersed in sudsy dishwater, with a hand grasping it firmly from above. The orientation of the V60 is such that the opening is facing downwards into the water, suggesting the initial phase of cleaning. Bubbles cling to its exterior, and the interior is not visible, indicating that it may have been recently plunged into the soapy solution. The surrounding environment includes a sponge and other washing implements, further setting the scene of an ongoing dishwashing task.

#### Sample 122 — Before

- Similarity: 0.4634
- Prediction: The box appears to be a plastic container, with a lid that is partially open, suggesting a person is attempting to open the contents. The lid is positioned in a position that indicates the person is holding the container, indicating that the contents are being thrown out. The person's hand is pointing at the container's contents, suggesting that the container is being opened. The container'
- Reference: The bag of coffee is perched on top of a washing machine, positioned upright with its top section pinched between two fingers. The closure appears to be a strip that sticks out, indicating that the bag has a resealable seal which has been peeled apart. There’s a visible crease along the edge of the seal, suggesting that this might not be the first time the bag has been opened. The other hand hovers nearby, likely to assist in fully opening the bag or to prevent it from tipping over. The environment around the coffee bag is domestic and utilitarian, with a bottle of laundry detergent standing nearby, reinforcing the casual setting of the action.

#### Sample 124 — Before

- Similarity: 0.2830
- Prediction: The salad appears to be a mixture of greens, with a light green hue, indicating it has been tossed in a bowl. The leaves are a vibrant orange, with the stems pointing towards the kitchen, suggesting they are being tossed. The bowl is cluttered with slender leaves, suggesting that the salad is being thrown in if it's not yet ready. The salad is a bright green, with an orange-red hue, suggesting it'll be ready for a meal.
- Reference: The wooden spoon in view exhibits a clean and unused appearance with a smooth, glossy finish indicative of minimal prior usage. The utensil is grasped firmly in the person’s right hand, its bowl facing downwards towards the plate below. The positioning of the spoon, coupled with the direction of the individual's grip, suggests an impending action, likely to involve contact with the plate's contents. The spoon's handle extends towards the edge of the frame, slightly tilted, enhancing the sense of anticipated movement.

#### Sample 127 — Before

- Similarity: 0.3244
- Prediction: The cloth appears to be a slender, curved object with a wide, rounded edge, indicating it has been soaked. The cloth is a dark brown, with hints of a liquid or liquid content, suggesting it is being washed. The person's hand is positioned in a position that indicates it is soaking, implying it is in the process of drying. The fabric appears to have been soaking for a long time, presumably to prevent the fabric from drying out. The hand is still agitated, suggesting the fabric may be damp or abrasive, suggesting that the cloth is being soaked or washered. The material appears to contain a lot of water, suggesting
- Reference: The tap is positioned centrally above the sink, with water flowing at a moderate rate, indicated by the slight splash and ripple around the stream. The faucet handle is angled upward, suggesting it is in an open position, and the stream of water casts a soft shadow on the stainless steel basin. The water droplets are visible on the metallic surface around the faucet's base, reflecting the room's light and hinting at recent or ongoing use.

#### Sample 131 — Before

- Similarity: 0.4350
- Prediction: The cloth appears to be a wicker, with a handle pointing downwards, indicating it is in the process of being cleaned. The cloth is positioned in a position that indicates it is being washed, with the handle positioned slightly downwards. The fabric appears to have been washered, with its surface indicating that it has been was washeered. The person's hand is presumably a beginner, with her fingers pointing upwards, suggesting that the cloth has been soaked. The material appears to contain a mixture of flour and water, which may indicate that the fabric has been thoroughly washeded. The hand is likely a novice, with fingers indicating a thorough cleaning process. The area is
- Reference: The grid appears to be a lightweight, flexible plastic object, predominantly yellow in color with a matrix of uniform square cut-outs. It is being held by a person's hand, which is visible in the image, suggesting the grid is being moved or manipulated in some way. The orientation of the grid is such that the longer side is vertical, and the shorter side is horizontal, indicating that it may be in the process of being turned or flipped. The surrounding context, a kitchen sink area with various cleaning items, suggests that the grid may be a dish rack component or a similar utensil used in kitchen organization.

#### Sample 132 — Before

- Similarity: 0.4740
- Prediction: The pot appears to be in a pot, with a lid positioned on top of it, suggesting that the lid is being removed. The lid is positioned in slats, suggesting the pot is being stacked, indicating that the pot has been placed in re-sealable state. The pot is surrounded by a thin layer of a thick layer of water, suggesting a simmering or cooking process. The water level is moderate, suggesting there is a slight amount of water in the pot, suggesting it may be a medium temperature. The kitchen is cluttered with utensils, including a kitchen towel, a dish towel, and a small kitchen sink. The stove is occupied, suggesting an
- Reference: The frame presents a close-up perspective of a kitchen gas stove burner, with the surrounding area featuring some kitchen utensils and ingredients. The burner's flame, however, is not distinctly visible in this particular image. Given the scene's setting, it suggests that the burner might be turned on at a low flame or perhaps not ignited at all. The overall ambiance of the kitchen suggests an immediate cooking action, with the stove's proximity to cooking pots and other accessories.

#### Sample 133 — Before

- Similarity: 0.4575
- Prediction: The jar is positioned in a kitchen, with a lid positioned on top of it, indicating that the contents of the container are being poured into the container. The lid is firmly attached to the jar, suggesting that the container is being emptied. The container is surrounded by a series of jars, each containing a different type of food or beverage. The contents of each jar are labelled with their respective names, suggesting the contents are being prepared. The rim of the jug is a clear, hazy container, suggesting a fresh, unfiltered liquid. The liquid is filtered through a funnel, suggesting it is preparing to be poured. The bottle's interior is
- Reference: The can appears to be in an initial state of being opened, held firmly in one hand while the other hand uses a manual can opener to puncture the lid. The lid has been partially cut open, creating a crescent of exposed interior, revealing what looks to be a rich red sauce inside. The can opener's arms are positioned at an angle indicative of the cutting process having just begun, with a visible gap where the cutting wheel has punctured the metal lid.

#### Sample 140 — Before

- Similarity: 0.3743
- Prediction: The paper is positioned on a table, with its edges positioned in a horizontal position, indicating a position where the paper is being placed. The paper appears to be a white, patterned fabric, with a light green hue, suggesting a smoky surface. The surface is a dark brown, with the edges of the paper indicating the surface is being prepared for use. The person's hand is presumably holding the paper, pointing to the paper and its contents, suggesting that the paper has been placed in resegregation. The hand is likely a beginner, with her fingers pointing at the paper. The cloth is slouchy, with some of the fabric indicating that it is being
- Reference: In this frame, the glass is grasped firmly by a hand, with fingers encircling its circumference. The glass appears to be partially filled with a clear liquid, as evident by the meniscus visible just below the rim. The base of the glass is securely placed on a wooden table with distinct grain patterns, while the surroundings exhibit a homey atmosphere with a wooden flooring and a portion of a chair visible.

#### Sample 142 — Before

- Similarity: 0.4708
- Prediction: The lid of the saucepan appears to be a white, spherical, shaped container, with a rounded edge, suggesting a cooking process. The lid is positioned in a position that indicates the lid is in the process of being placed, indicating that the lid has been placed. The saucepan is surrounded by a thin layer of white, suggesting that the liquid is a liquid. The surrounding area is cluttered with utensils, including a kitchen towel, a dish towel, and a small kitchen towel. The kitchen towel is anchored to the lid, suggesting the liquid may be boiled or cooled. The person's hand is pointing at the lid of this saucepan, suggesting it is preparing to
- Reference: In this frame, the sausage is not immediately visible, suggesting it may be obscured or hidden beneath other objects on the countertop. Various items, including a bottle, a knife, and a plate, are scattered around the area, which could be potentially concealing the sausage. The dominant visual elements are a person's hands, which appear to be in the midst of handling or interacting with an item, possibly the plate, implying that the sausage might be under it or being prepared for covering.

#### Sample 145 — Before

- Similarity: 0.2695
- Prediction: The sliced avocado appears to be in a fresh state, indicating that it is in the process of being sliced. The avocado is positioned in slender, ripe portions, with a thin, slightly curved edge, a tangy texture, and a smooth, smoky texture. The fruit is a white, tangier avocado, with an orange-colored exterior, suggesting that it may be a fruit with ripened flesh. The rind is slicing, with its flesh separating from the avocado, suggesting a gradual process of squeezing the flesh.
- Reference: The piece of pitta bread is placed atop a round wooden cutting board. One can observe that the pitta is neither completely flat nor too puffed up, suggesting it has been lightly handled or possibly folded. From this angle, it appears slightly uneven in texture, indicative of its natural and rustic quality. The bread's surface appears soft and somewhat porous, likely making it ideal for dipping or holding fillings.

#### Sample 147 — Before

- Similarity: 0.4094
- Prediction: The gas stove is positioned on a counter, with a lid containing a pot of water, a frying pan, and a microwave. The burner is surrounded by a white ceramic plate, indicating that it is in the process of cooking. The flame is bright, with the light coming from the burner's hood, implying that the burner is still on. The stove's interior is cluttered with utensils, including a kitchen towel, jar, and other items. The kitchen is occupied with dozens of dishes, including the one serving a meal, and the kitchen sink is anchored to the counter. The countertop is adorned with patterned ceramic tiles, reminiscent of a stovetop
- Reference: The mixer is prominently positioned on a kitchen countertop, close to the stovetop area. It appears to be a modern blender with a transparent container, a white base, and a lid. The blender's power cord extends towards an electrical socket, indicating it's ready for use. A hand, presumably the user's, is seen reaching out and grasping the blender's base, suggesting an imminent action or movement.

#### Sample 153 — Before

- Similarity: 0.3157
- Prediction: The countertop appears to be a white, patterned one, with a light blue hue, suggesting a recent cleaning. A hand is positioned on the counter, pointing to a sink, which appears to have been cleaned. The counter's surface is a dark brown, with the counter'd surface indicating a previous cleaning. The countertop is surrounded by a series of white towels, indicating that the cleaning process is ongoing. The towel's fabric is presumably soaked, suggesting that the cloth is still wet. The sink appears to contain a small amount of soap, suggesting it may be soaked in soap. The surface is slightly damp, with some visible soap residue. The cloth's material is reminiscent of a sponge
- Reference: The pepper mill appears to be in motion, falling towards the ground. The motion blur present in the image suggests rapid movement, and the position of the pepper mill, tilted at an angle, indicates it has just been knocked or is slipping from its standing position. The proximity of the hand and the cloth suggest an attempt to catch or stabilize the falling object. There's a dynamic interaction between the hand, the cloth, and the pepper mill, captured in the midst of an unexpected shift from stability to motion.

#### Sample 157 — Before

- Similarity: 0.4670
- Prediction: The cloth appears to be a slender, abrasive, and a bit sticky, with a slight smudge on the surface. The cloth is a dark brown, with an orange hue, indicating it has been soaked. The fabric is positioned in a position that indicates it is in the process of being washed, with the cloth positioned at the center of the cloth, implying it is being was washered. The person's hand is visible, with her fingers pointing at the cloth. The hand appears to have been soaking the cloth in the water, suggesting it has a mild soapy residue. The water is slick, with its surface indicating a waterlogged state
- Reference: The sink appears moderately used with visible water droplets around the basin and a few soap suds clinging to the surface, indicating recent activity. A standard silver faucet with a single handle is situated over the sink, slightly askew to the right, suggesting it has been handled recently. The stainless-steel basin has a dull sheen, with some areas reflecting light more than others due to the uneven distribution of moisture. A yellow sponge is resting at the corner, and a bottle of dish soap is within reach, signifying a dishwashing task either just commenced or paused momentarily.

#### Sample 158 — Before

- Similarity: 0.3203
- Prediction: The white towel appears to be a white towel, with a slender, slightly curved handle, suggesting a hand or hand towel. It is positioned on a table, with its sides facing outwards, indicating a position for the towel. The towel's surface is a dark brown, with the edges of the towel indicating the towel'
- Reference: The orange rests on a smooth, matte surface, likely a wooden table. Its glossy skin reflects a muted light, emphasizing the deep, sun-kissed hue typical of ripe oranges. There are slight imperfections visible on its skin, perhaps a small scar or two, and minute, pitted details, reminding the viewer of its organic nature.

#### Sample 160 — Before

- Similarity: 0.4657
- Prediction: The cloth appears to be a slatted, curved object, with a thin, rounded edge, suggesting it is being held in a hand. The cloth is positioned in contrasting hues, suggesting that it is a white cloth, indicating it has been washed. The fabric is slanted, suggesting the cloth is being washered. The person's movements are reminiscent of a person holding a cloth, suggesting they are preparing to take a shower. The material is presumably a damp cloth, with the cloth positioned over the cloth, which indicates it is likely to be wet. The water level is low, suggesting a waterlogged surface, implying the cloth may be we
- Reference: The kitchen sink area is cluttered with various dishes and utensils. A person's arms are visible, with their hands engaged in adjusting the faucet, perhaps in preparation for dishwashing. The water is running, and there's a visible stream flowing from the tap, indicating that cleaning activities are in progress. The left sink basin is filled with water, while the right one contains several submerged items, possibly soaking. On the counter, a white dish rack is loaded with a stack of clean white plates, along with other kitchen tools and utensils that seem freshly washed and are left to dry.

#### Sample 161 — Before

- Similarity: 0.4967
- Prediction: The bag appears to be a plastic bag, with a spherical shape, indicating a bag with rounded edges. The bag is positioned in a position that is likely to be in the hands of a person, implying a hand or handbag. The person's hand is visible, suggesting a grasping motion, and the bag appears a bit loose, suggesting that the person is attempting to open it. The object is a white plastic bag with an orange-colored interior, suggesting the bag is likely a small plastic bag. The camera's focus is on the bag itself, which appears to have been partially opened, presumably to be empty. The bags are positioned on a flat surface, suggesting
- Reference: The image reveals the interior of a cylindrical bin, which appears to be a washing machine drum, with a textured white exterior and a dark, shadowy interior. The rim of the drum is partially illuminated by a striking pink and white light source, creating a stark contrast with the darkness inside. A pair of hands, protected by bright yellow rubber gloves, reaches into the drum, suggesting the commencement of a task. The reflection on the drum's surface indicates a nearby metallic object, possibly a utility that is within the vicinity of the bin.

#### Sample 163 — Before

- Similarity: 0.2235
- Prediction: The hand is positioned in a position to the right of the person's left, with the palm facing outward, indicating a person'
- Reference: The tablecloth is captured mid-motion, suggesting that it's in the process of being unfolded or placed. Its edges can be seen fluttering, with one corner appearing closer to the viewer's perspective. The cloth's texture and pattern are not fully discernible due to the action's swift nature and the image's blur. The majority of the tablecloth remains bunched up or folded, indicating that the unfolding has just begun.

#### Sample 170 — Before

- Similarity: 0.4208
- Prediction: The slicer is positioned in a kitchen, with a knife in the middle, pointing to a slit in the center of the blade, indicating a moment of action. The blade is angled downwards, revealing a sharp edge, suggesting a cutting motion. The knife's surface is cluttered with crumbs, suggesting that the blade is still active. The kitchen is surrounded by a series of kitchen items, including a pot, sink, and counter, which are all placed on the counter, implying a busy or busy workspace. The stainless steel blade is visible, with its blade pointing downwards. The surrounding area is a dark, reflective, and reflective, highlighting the kitchen's
- Reference: A hand is captured in the midst of a dynamic action, positioned above a plate of freshly sliced tomatoes, holding a dual-sectioned spice shaker with a clear body, revealing two separate compartments containing white and darker granules, presumably salt and pepper. The motion is frozen in time, with a small mound of the darker spice poised on the edge of the shaker, suggesting that some of the contents have already been dispensed onto the tomatoes. The scene is indicative of seasoning in progress, with the intent to enhance the flavor of the tomatoes.

#### Sample 171 — Before

- Similarity: 0.4812
- Prediction: The pan appears to be in a simmering state, with a sprinkling of water, indicating that the pan is still hot. The pan is positioned in icy conditions, with the water evaporating from the pan's surface, implying that the water has been boiled. The surface of the pan appears slightly damp, suggesting that the liquid has cooled sufficiently to allow the pan to simmer. The water is a light brown color, suggesting a medium-low temperature, and the pan has been placed in ice water, suggesting the pan may be a bit hot.
- Reference: The oat appears to be somewhat settled in the pan, suggesting that it may have been recently poured in or has been resting for a while. The texture and spread of the oat across the surface indicate that it might be uniformly distributed, with very minimal clumping or clustering. There are subtle variations in the color and density of the oats, indicating that they are likely raw and uncooked. No overt signs of movement or agitation can be discerned from this particular frame.

#### Sample 174 — Before

- Similarity: 0.3712
- Prediction: The vegetables are in a state of adolent, with a slight smoky hue, suggesting they're in the early stages of cooking. They are a bright green color, with the leaves indicating they've been boiled or soaked in water. The texture of the vegetables is slightly charred, suggesting that they'll be a little soft. The color of the leaves suggests that they may be soaking in water, suggesting it's still a bit damp.
- Reference: The colander is held at an angle, allowing viewers to peer inside and see its contents. Inside the colander, a mix of beans in various colors - ranging from yellow and white to deep red and brown - is prominently displayed. Droplets of water can be inferred, suggesting that the beans have been recently rinsed or washed. Surrounding the colander are various kitchen items and ingredients, creating a lively culinary scene. The person's hand grips the colander's handle firmly, suggesting an intention to shake or move it.

#### Sample 180 — Before

- Similarity: 0.4173
- Prediction: The pizza is a light brown, with a thin layer of cheese, indicating it has been seasoned. The crust is topped with shredded cheese, which is reminiscent of a pizza crust, with the cheese tanging and a hint of salt. The pizza's surface is bare, with no visible toppings, suggesting it has not yet been toasted. The toppings are a mixture of shredded mozzarella cheese, olive oil, and melted cheese, suggesting that they may have been sprayed with melted butter. The surface of the pizza is slightly uneven, suggesting a slight sloppy or uneven surface. The texture of the toppings is distinctly textured, suggesting the pizza may have a slightly spongy
- Reference: The tomato is depicted in a relatively unaltered state, with a spoon resting against a round flatbread that has a smattering of tomato sauce in the center. The sauce appears freshly spread, with a vivid red hue and discernible chunks, indicating the sauce may be homemade or chunky in style. The spoon, with a hint of sauce on its surface, suggests the action of spreading has just occurred. The sauce is not evenly distributed, with a heavier concentration towards the center and mere smears and dollops radiating outward, implying a hurried or imprecise application.

#### Sample 182 — Before

- Similarity: 0.2364
- Prediction: The surface of the oven is a dark, reflective object, with a light-colored hue that is likely a reflection of the stove. The surface is cluttered with crumbs and other debris, indicating a deliberate attempt to remove it. The light is reflected off the surface, implying a gradual process, resulting in a smoky surface. The object is positioned in obscurity, presumably a kitchen counter or counter, a place where the oven's surface is visible, highlighting the absence of a stove or counter.
- Reference: A clear glass container, possibly a laundry detergent dispenser, is upturned, with its contents seemingly in the process of being poured out, although the liquid is not visible. The container is held aloft by a person whose arms and lower body are visible, but the upper body and head are out of the frame. Below, to the right of the washing machine, lies a blue box of detergent, resting on its side. The washing machine door is open, revealing a glimpse of colorful clothes inside, but the focus is not on the clothes at this moment.

#### Sample 185 — Before

- Similarity: 0.4605
- Prediction: The microwave is positioned on a kitchen counter, with a white plate and a bowl of food in the middle. The lid is a dark brown, with the lid indicating that it is in the kitchen. The interior of the microwave is dark, with its interior cluttered with food, including a few dishes and utensils. The microwave has a black handle, suggesting that it may be a microwave oven, but the lid is not visible. The kitchen is surrounded by a series of kitchen items, including the oven's lid, which are positioned in a horizontal position, indicating the oven is in occupied. The surrounding area is cluttered, with dishes, including one of the most recent ones, a dish with
- Reference: The oven’s digital display is highlighted in bright red, showing a temperature setting of 180 degrees, likely in Celsius given the context. This specific reading indicates a moderate baking temperature, commonly used for a wide range of dishes, from baked goods to casseroles. The reflective glass surface of the oven door mirrors the interior racks and elements, hinting at a clean and possibly recently unutilized state. The user's hand, adorned with a fitness tracker, suggests an attention to detail and precision, pressing a button on the control panel likely to adjust the temperature, as indicated by the finger's position.

#### Sample 187 — Before

- Similarity: 0.2698
- Prediction: The jar appears to be in a kitchen, with a lid positioned on top of a bowl, suggesting that the contents are being thrown out. The lid is positioned in slender, overlapping sections, suggesting a gradual movement, indicating that the container is being slid open. The rim of the jar is a curved, rounded shape, suggesting the contents may be thrown away. The container is surrounded by a series of jars, which are stacked in overlapping rows, suggesting they may be in the process of being tossed. The contents of the container are positioned against the rim, suggesting it may be being discarded. The surrounding area is cluttered, suggesting there may be
- Reference: The chicken appears to be in the initial stages of preparation, with a few pieces lying irregularly on a wooden chopping board. The pieces are uneven in size and shape, suggesting they have been roughly chopped, and the texture looks somewhat ragged, indicating a less than smooth cut, possibly due to the use of a non-professional or slightly blunt kitchen knife. The board itself has a few stray chicken pieces scattered about, and there is no sign of any seasoning or marinade on the meat, implying the chicken is plain and possibly recently removed from its packaging.

#### Sample 189 — Before

- Similarity: 0.4058
- Prediction: The pizza is sliced in a circular motion, with the edges of the pizza being slightly exposed, indicating that it has been sliced. The pizza has a thin, slender, and a smooth texture, implying a medium-sized slice of pizza. The crust is a light brown, with a slight crust, suggesting a softer crust. The knife is positioned in angular motion, presumably to prevent the pizza from sticking to the surface, a sign of a quick cutting. The blade is angled slightly, suggesting that the pizza is being cut. The surface of the slice is bare, suggesting the pizza has been cut in curved or a flattened shape, highlighting the pizza's
- Reference: The cake appears to be a crumbly-textured delight, perhaps a streusel or a crumble-topped cake, with a golden-brown surface. A small segment of the cake has been sliced away, revealing a moist, darker interior which contrasts with the crumbly topping. The slice's cut edges are jagged, indicating the cake's dense and rich composition. The cake is placed on a vibrant purple circular plate, and roughly three-fourths of the cake remains intact.

#### Sample 193 — Before

- Similarity: 0.4144
- Prediction: The sliced meat appears to be in a state of deterioration, with the meat slicing down to a crisp, charred state. The meat is a medium-rare, medium-sized piece of meat, with a slightly charring appearance. The knife is positioned in angling motion, indicating the meat has been cut into pieces. The flesh is sliced in slender slices, implying the meat is being cooked. The slices are stacked on a table, presumably in the kitchen, with their edges exposed, suggesting the meat may be preparing for cooking.
- Reference: A wooden cutting board is positioned over the edge of a stovetop, featuring several freshly cut, irregularly shaped pieces of tofu, each exhibiting a spongy texture and a pale cream color, indicative of firm tofu that has not yet been cooked or seasoned. The tofu appears moist, likely from being recently pressed or cut, with small beads of water visible on its surface. The board shows remnants of moisture and small bits of tofu residue, suggesting it has been used to cut the tofu into these sizable chunks.

#### Sample 196 — Before

- Similarity: 0.4162
- Prediction: The paper is positioned in a kitchen, with a white surface, a patterned design, and a reflective surface, suggesting it is being prepared for use. The paper's surface is a dark brown, with the edges of the paper indicating a light or liquid content. The person's hand is presumably holding the paper, indicating it is preparing to open. The material is reminiscent of a paper towel, with its edges indicating the surface is being prepped for use, with some of the material being discarded. The hand is likely a beginner, demonstrating a willingness to open the paper and attempting to open it. The surface of the tray is indicating that it is ready to be used, with an apparent
- Reference: The bag appears to be in a semi-folded state, with the top part being held by a hand, suggesting an ongoing action. The bag's label and some of its contents are visible, suggesting it might not be fully closed or sealed. The texture and wrinkles on the bag's surface indicate that it's not in a pristine or straightened condition, and there's some degree of manipulation that has already occurred.

#### Sample 197 — Before

- Similarity: 0.4867
- Prediction: The paper is positioned on a table, with a white surface, indicating a person's hand. The paper has a light brown hue, suggesting a smoky or a slightly soiled surface. The surface is a dark brown, with the edges of the paper indicating the presence of a food or other liquid. The person'
- Reference: A pot with a steamy lid sits atop a gas stove, indicating something is being cooked. The stovetop is stainless steel and reflects the surrounding items, including another pot and a grater. The kitchen counter appears messy with a spill near the stovetop, and various kitchen tools are strewn about, including a grater, a pair of tongs, and a bottle, possibly of oil or vinegar. A person's arm is in motion, wiping the counter with a white paper towel, suggesting an attempt to tidy up. The blurred motion of the hand implies swift movement, likely in the midst of cleaning.

#### Sample 203 — Before

- Similarity: 0.3121
- Prediction: The bottle is positioned in a kitchen, with a lid positioned at the top, indicating that it is in the process of being opened. The bottle's contents are a clear liquid, with no visible residue or traces of food or other debris, suggesting that the bottle is in pristine condition. The lid is a dark brown, with an orange-colored cap, suggesting a discarded bottle. The container is surrounded by a thin layer of water, suggesting the bottle may be a liquid, suggesting it may be in the middle of a cooking process. The liquid is filtered through a small opening, suggesting there is no visible liquid or residue, suggesting its contents are still present. The glass is framed by overlapping s
- Reference: The squash is being held in the left hand of the person, with the focus on its bottom part, which is nestled securely in the palm. The squash appears to be a common variety, with a smooth, bright outer skin, suggesting it's ripe and ready for consumption or cooking. The hand gripping it is slightly tilted, indicating either the beginning or the end of a movement. The person’s thumb and fingers are not applying much pressure, implying a gentle touch, possibly to check its firmness or to move it without causing any bruising.

#### Sample 204 — Before

- Similarity: 0.4409
- Prediction: The light is dim, with a light source indicating a low-light setting. The light source is visible, with the light coming from the outside of the oven, indicating that the oven is not yet fully lit. The surface of the stove is a dark brown, with no visible light, suggesting that the light is coming from a nearby source. The lighting is dim and the light source appears to be a source of light, implying that the stove has been turned on. The kitchen counter is positioned in a position that is not visible, suggesting a lighting source is not present. The counter's surface is cluttered, with only a few small items visible, highlighting the light's intensity. The floor is bare, with
- Reference: The light appears to be brightly illuminating the space, casting a strong and focused glow on the wall. The intensity of the light creates contrasting shadows, especially in the corners where the walls meet. The presence of the light seems to emphasize the texture of the wall, revealing any minor imperfections or blemishes present.

#### Sample 208 — Before

- Similarity: 0.4576
- Prediction: The sanitized sponge appears to be in a position to be agitated, with a smoky surface, indicating it is in the process of being cleaned. The surface is a dark, hazy, white, and abrasive, suggesting it has been soiled. The sponge appears agitating, suggesting that it is preparing to be washed, implying that it has just been washered. The grit appears to have been soaked, suggesting the sponge may be a medium-sized sponge, a type of sponge that is likely to be used for washing dishes. The sink appears to contain a small amount of soap, suggesting a soapy or diluted solution is
- Reference: The wooden spoon appears partially submerged in a sink full of sudsy water, with its handle pointing upwards and angled slightly to the right. The spoon's bowl is visible above the waterline, reflecting light and revealing its smooth, curved interior. The handle, stained darker towards the end, suggests frequent use, indicating that this utensil has been part of many cooking processes. Surrounding the spoon are a plethora of dishes and utensils, suggesting an active kitchen environment.

#### Sample 212 — Before

- Similarity: 0.3634
- Prediction: The kitchen sink appears to be in a position to be positioned in obscurity, indicating that the sink is in occupied. The sink's surface is a dark brown, atypically white, with a light-colored surface, suggesting that the kitchen sink is not yet fully occupied, suggesting a gradual movement. The kitchen's lighting is dim, suggesting the kitchen is not fully lit, suggesting it is not being fully utilised. The surrounding area is cluttered, suggesting there is hardly any room for the sink to be placed, suggesting an imminent movement.
- Reference: The image shows a digital oven timer with the display clearly visible against a stainless steel backdrop. The timer is set at a specific time, though the exact digits are not clearly discernible due to the angle and distance. The display is illuminated in a cool blue light, indicating that the oven is active or in the process of being set. The digits appear to be stable, with no visible blinking that would suggest the time is being adjusted at this moment. The user's hand is poised near the controls, suggesting that they have just interacted with the timer or are about to.

#### Sample 218 — Before

- Similarity: 0.4190
- Prediction: The sliced tomato appears to be a ripe, uncooked piece of cheese, with a thin, slightly smoky texture. It is a white, slightly chewy, tangy, and slightly mushy, suggesting it is being prepared for cooking. The texture is reminiscent of a bread, with its texture contrasting against the surrounding area, suggesting a fresh, ripened tomato. The tomato appears a little dry, with the texture of spongy cheese indicating it is not yet ready for use. The knife's edge is visible, suggesting the person is attempting to slice the tomato, which is likely to be in the process of being sliced.
- Reference: The piece of pitta bread appears intact, resting on a circular wire mesh which sits atop a wooden cutting board. The bread has a golden-brown surface, suggestive of a light toasting, and exhibits a slightly puffed texture, indicating its freshness and softness. One hand, with a smartwatch on the left wrist, hovers above the bread, fingers gently curved as if they have just placed it down or are preparing to pick it up. Surrounding the bread, the kitchen counter is cluttered with various utensils and items, including a sponge and a scouring pad in the sink, which suggest an active cooking environment.

#### Sample 220 — Before

- Similarity: 0.2805
- Prediction: The slicer is placed in a water bath, with the handle positioned in the middle of the water. The water flows downwards, indicating that the sprig is dripping, resulting in sludge. The nozzle is positioned at the center of the holder, pointing to the water's surface, implying a slurry or liquid stream. The surface of the sink is cluttered with scrubbing soap, which is likely a source of soap residue. The sink's lighting is dim, suggesting a low-light setting.
- Reference: The cucumber appears to be partially washed, with beads of water dotting its surface, reflecting the overhead light. It's held firmly in one hand while the other hand grips a kitchen knife, poised as if in the midst of slicing. The cucumber's dark green skin shows slight variations in hue and a fresh, firm texture. The hand holding the cucumber has visible knuckles and fingers, suggesting a gentle but steady grip, indicative of a task performed with care.

#### Sample 222 — Before

- Similarity: 0.4145
- Prediction: The cloth appears to be a bare, soiled fabric, with a thin layer of fabric forming a loose, clumpy texture. The fabric is a solid, textured fabric, indicating it has been soaked or washed. The cloth is positioned in a position that indicates it is in the process of being soaked, with the cloth indicating that it is still wet. The texture of the cloth is slightly damp, with some areas showing signs of abrasion or adsorption. The material is largely a light-colored fabric, suggesting it is being washered or was washes, with most of the fabric indicating a dry or wet state. The person's movements
- Reference: The sponge appears heavily saturated with water, indicated by its swollen size and the darkened coloration, a common sign of absorption. It's being compressed by a firm grip, causing a clear stream of water to be forcefully expelled, evidenced by the droplets in motion around the sponge. This action also reveals the sponge's porous texture as the pressure pushes the water out through its many cavities, conforming to the shape of the hand that is squeezing it.

#### Sample 223 — Before

- Similarity: 0.4851
- Prediction: The plastic container is positioned in a kitchen, with the lid open, indicating that the contents are being poured into the container. The lid is firmly attached to the container, revealing a clear, unadorned surface. The contents are a variety of foods, including fruits, vegetables, and dairy products, and the lid is partially closed, suggesting that the container is being opened. The container is partially open, suggesting a closed portion, and there is no visible liquid or solid content in the container's interior.
- Reference: The tuna can appears to be sealed, indicating that it has not yet been opened. The individual's fingers grip the can's edges, while the other hand seems poised to interact with it, possibly preparing to use an implement or just beginning the process of opening. The aluminum lid of the can reflects the ambient light, showing no signs of puncture or any openings.

#### Sample 231 — Before

- Similarity: 0.4495
- Prediction: The onion is positioned in a kitchen sink, with its lid open, revealing a slender, slightly curved shape. The inside of the onion is slightly slanted, suggesting that it is a fresh, uncooked piece of food. The outer portion of the vegetable appears to be a green, ripe, and slightly charred, suggesting it may be preparing for cooking. The interior of the container is cluttered, with the lid open and the inside of its packaging indicating that the food has been prepared.
- Reference: The plastic bag appears to be tightly sealed with its contents under slight pressure, as evidenced by the bulging nature and rounded edges at the top. The fingers of the hands pulling at the bag suggest the beginning of an opening action, with the plastic demonstrating a degree of tension and resistance. This tension is visible in the slight creases and stretched appearance around the areas where the fingers make contact. The bag is translucent, revealing a glimpse of the round, light-colored objects inside, likely potatoes, packed closely together.

#### Sample 232 — Before

- Similarity: 0.4861
- Prediction: The blender is positioned in a kitchen, with a hand on the handle, pointing at the blender's lid, suggesting that it is in the process of blending. The blender'd lid is a slender, curved metal handle, suggesting a slight movement, and the blade is angled slightly to the right, suggesting the blender is in agitation. The lid is slightly tilted, suggesting it is blending, and there is no indication of the blender itself being in motion. The kitchen's lighting is dim, with the kitchen lighting dimly lit, suggesting an ambient light source. The palette is dark, with white and black objects scattered around the kitchen, including a bowl of ice cream, a glass bowl,
- Reference: The ingredient in the bowl appears to be a thick, vividly yellow mixture, indicative of a batter infused with either a generous amount of egg yolk or another yellow coloring component such as turmeric or saffron. It's glossy and smooth on the surface, suggesting that it has been well mixed to incorporate air, which is often a desired quality in batters for leavening purposes. The consistency is uniform without any visible lumps, implying that the dry and wet ingredients have been thoroughly combined.

#### Sample 236 — Before

- Similarity: 0.4580
- Prediction: The cheese appears to be a thin, uncooked piece of cheese, with a slightly smoky texture. It is sliced in a circular motion, indicating it is being prepared for a meal. The knife is positioned in angular motion, suggesting it is a medium-sized slice of cheese. The cheese is shaped like a rectangular piece of bread, with the edges pointing towards the surface of the cheese.
- Reference: The butter appears to be in a cold, solid state, likely taken straight from the refrigerator, as indicated by its firm texture and the way it retains the square impressions from the packaging. It is light yellow, suggesting a typical composition without added colorants, and is resting on a slice of multi-grain bread. The butter's surface is uneven with ridges and valleys where the knife has begun to skim across, but the spreading has not fully commenced, which suggests the butter’s temperature is still quite low, not yet softening enough for easy spreading.

#### Sample 238 — Before

- Similarity: 0.3474
- Prediction: The bottle is positioned in a kitchen, with a lid positioned on top of the bottle, indicating that it is in the process of being opened. The bottle's packaging is a clear plastic container, with no visible markings or markings, suggesting that the contents are not yet sealed. The lid is firmly attached to the bottle'
- Reference: A glass jar, nearly full of white flour, is being tilted over a large mixing bowl, allowing a gentle cascade of flour to fall into the bowl. The flour appears fine and powdery, suggesting a soft, sifted texture. It forms a small mound within the bowl, and there's a visible dusting of flour escaping into the air, reflecting the light and creating a soft haze around the jar's opening. The flow from the jar is steady but controlled, indicating a careful pouring motion by the person handling the ingredients.

#### Sample 241 — Before

- Similarity: 0.4279
- Prediction: The jar appears to be in a position to be positioned in resembling a kitchen sink, with a handle pointing downwards, suggesting a hand is preparing to move. The rim of the jar is positioned slightly downwards and the handle is pointing upwards, indicating a recent movement. The lid is a dark brown, a light green color, suggesting that it may be a microwave-safe container. The surrounding area is cluttered with jars, dishes, and other items, suggesting the emergence of a busy kitchen.
- Reference: A red soup ladle with a long handle is resting inside a deep, circular white bowl. The bowl is placed on a white paper plate that shows remnants of food particles, suggesting a meal was recently consumed. Adjacent to the bowl is a clear glass, about a quarter full with a yellowish liquid, possibly a beverage. The table setting includes a folded yellow napkin under the bowl and a portion of a white paper plate visible in the foreground, suggesting the presence of another dining space opposite the viewer.

#### Sample 245 — Before

- Similarity: 0.4625
- Prediction: The white substance appears to be a mixture of ice cream, whipped cream, and whipped toppings, indicating that it has been poured into a bowl. The whipped mixture is a light brown color, suggesting that it may be whipped or whipped, suggesting a smooth texture. The texture of the whipped confectioners' sugar is reminiscent of a powdery confectioner's sugar, suggesting it may have been whipped. The white object appears to have been placed in a hot, icy pan, possibly a microwave, implying that the melted whipped sugar has been placed on top of the white substance. The object appears a little damp, suggesting the icing may have melted, suggesting there may
- Reference: The egg in this frame is intact and appears freshly cracked into the white bowl, with both yolks whole and centrally located, untouched by the fork lying next to the bowl. The translucent albumen encases the deep orange yolks, which are uniform and undisturbed, suggesting that the egg has not been manipulated since being opened. The stark contrast between the bright yellow yolks and the white bowl accentuates the egg's freshness and the stillness of this initial stage of preparation.

#### Sample 247 — Before

- Similarity: 0.4496
- Prediction: The sanitized sponge appears to be in a water bath, with a sprinkling of soapy water on the surface. The sponge is positioned in sweeping motions, indicating it is in the process of being washed. The water is dripping from the sink, resulting in scalding and a visible smudge on the sponge's surface.
- Reference: The blender is positioned upside-down with its opening facing downwards, allowing any residual liquid or contents to drain away. The lid is placed on the counter, revealing the blender's interior which appears to have a frothy residue possibly from a recently blended concoction. The surrounding area is wet, suggesting that the rinsing process has begun. Slight droplets on the blender's surface reflect the ambient light, indicating its recent contact with water.

#### Sample 248 — Before

- Similarity: 0.4007
- Prediction: The door is positioned in a position that is not yet fully open, indicating that the door is open. The door's surface is a dark, hazy, dark grey, with a slight hint of a glare. The interior of the door appears to be a room with contrasting walls and furniture, suggesting that the room is not fully open.
- Reference: The light switch appears to be in an inactive state, with the toggle buttons in a neutral position, not pressed down. The ambient lighting in the room remains dim, indicating that the electrical circuit connected to the light source is incomplete. The shadow cast on the wall by the hand and the switch assembly suggests a faint light source elsewhere in the room, not from the intended fixture, and the overall atmosphere is one of low illumination.

#### Sample 251 — Before

- Similarity: 0.3919
- Prediction: The milk appears to be a liquid, indicating it is still in the liquid phase, suggesting that it is not yet fully incorporated. The milk's texture is reminiscent of a milky consistency, suggesting a smooth texture, implying a creamy texture. The liquid appears to have been poured into the milk, suggesting it is a medium-sized amount, suggesting the milk is still a little frothy. The Milky Milky liquid appears slightly frothing, suggesting there is no liquid present, suggesting its presence is likely to be concentrated. The water's surface is hazy, suggesting an icy or lukewarm state, suggesting some liquid may be present. The lint is indicating a
- Reference: The water in this frame is contained within a transparent, cylindrical vessel, possibly a pitcher or a blender jug. The surface of the water appears calm and undisturbed, indicating it has been sitting still. It captures the ambient light, highlighting the vessel's round edges and its contents. There is no sign of active pouring or disturbance in the water, which suggests that it has been recently filled or is awaiting use. The water level reaches approximately midway up the vessel, providing ample space for more water or other ingredients to be added.

#### Sample 252 — Before

- Similarity: 0.3612
- Prediction: The butter appears to be a white, spongy, brittle piece of bread, with a slightly sloppy texture. The knife is positioned in a position to grasp the bread, which is a bare portion, with the edge of the bread indicating a slight movement. The bread is sliced in overlapping sections, with its edges positioned slightly apart, suggesting a gradual process. The butter is slender, with an overall appearance of a crisp, ripe, and a light brownish color. The surface of the butter appears slightly damp, with some areas of the surface showing signs of scrubbing or slicing. The texture of the sandwich appears to indicate a relatively recent process,
- Reference: The cake presents as an almost complete ring, set against a decorative lace doily. It appears to be a dense, golden-brown bundt cake with a moist-looking crumb, suggesting a rich and buttery composition. A single slice has been neatly removed, placed back in its original position, slightly askew to indicate it has been cut. Crumbs dot the doily around the cake's base, and the inner circle of the bundt shape is clear, revealing the doily's intricate pattern.

#### Sample 253 — Before

- Similarity: 0.2658
- Prediction: The frying pan is in a position to be seen, with its surface positioned in sandpaper, indicating that it has been frying for a long time. The pan is positioned on a counter, with the blades pointing downwards, implying that the pan is currently in the process of cooking. The blades are positioned at a slight angle, suggesting that the frying process is still underway. The surface of the pan appears to be a medium-sized, atypically a frying medium, with a thin layer of grease visible, presumably from the cooking process. The resulting liquid appears to have been poured onto the pan, resulting in clumps of grease forming on the
- Reference: The rag, mostly blurred due to motion, is clutched by a hand and seems to be in the process of wiping or cleaning. The fabric appears to be somewhat damp, reflecting light in certain areas, indicating moisture. There's a sense of dynamic movement in the rag's position, with the fabric bunching up slightly under the pressure of the hand.

#### Sample 255 — Before

- Similarity: 0.3358
- Prediction: The microwave is positioned in a kitchen, with a white countertop, a chrome-plated door, and a black handle. The interior of the microwave is dark, with its interior cluttered with clutter. The door is a rectangular shape, with the handle pointing towards the microwave, suggesting a possible opening. The microwave's interior is cluttered, with an unadorned surface, including a counter top, cluttered counter top and cluttered drawers. The kitchen is surrounded by a series of white ceramic counterware, including the microwave'
- Reference: The image captures a hand reaching out towards an area, presumably where the switch is located. The fingers are extended, suggesting intent to interact with something, possibly to activate or deactivate it. The background reveals a kitchen setting with various appliances, but the main focal point appears to be the action of the hand. The exact state of the switch itself is not immediately clear from this angle, but the intentionality of the hand movement suggests that it is about to engage with it.

#### Sample 258 — Before

- Similarity: 0.4260
- Prediction: The slicer is placed in a kitchen sink, with a handle pointing downwards, indicating it is in the process of being rinsed. The blade is positioned in overlapping motions, suggesting that the water has been drained. The water is a hazy, cloudy liquid, implying that the scrubbing process is complete. The person's hand is firmly grasping the grater, pointing upwards, and the blade is still pointing toward the sink. The rinsing motions suggest that the blade has been rinsed, resulting in sloughing.
- Reference: The rectangular dish, positioned in the lower left quadrant, displays a well-used appearance with burnt-on residues covering its inner surface. A smattering of droplets surrounds the pan, suggesting recent attempts at cleaning or soaking. The wear and stains indicate that the dish has likely been through a cooking process that involved high heat, such as roasting or baking, which has resulted in the caramelization of food remnants adhering persistently to the metal.

#### Sample 260 — Before

- Similarity: 0.3914
- Prediction: The kitchen counter is positioned in a position that is cluttered with a variety of items, including a white plate, a bowl, and a dish. The counter is placed in contrasting hues, indicating a recent change in the kitchen setting. The countertop is a dark brown, with hints of a kitchen sink or microwave. The kitchen sink is anchored to a wooden base, suggesting a clean surface. The table is surrounded by a series of items and cluttered by stains, suggesting that the kitchen counter may be a place to store a meal or other food items. The lighting is dim, with the ambient light indicating an active kitchen setting, implying a busy kitchen. The surrounding area is
- Reference: The frame captures a moment within a kitchen environment, where it seems that a recent spill has occurred. There's a visible wetness on the countertop, possibly indicating the initial application or spillage of the detergent. The image doesn't show a direct spray action, but there's an implication of a recent spray given the freshly wet appearance. Adjacent to the spill, there's a hand that appears to be preparing to wipe or clean up the liquid.

#### Sample 267 — Before

- Similarity: 0.3212
- Prediction: The avocado appears to be in the hands of a person, positioned in a kitchen, with its skin exposed, revealing a smoky hue. The avocado is a bright green, ripe avocado, with a slightly charred exterior, suggesting it may be a fruit. The skin is bare, suggesting the avocado may be in riper stages. The hand is positioned on the side of the avocado, indicating the avocado is in the process of being sliced. The blades are positioned slightly away from the avocado and the skin is still visible, suggesting that the avocado has been sliced in resemblance to the avocado.
- Reference: The sweetcorn is sealed within a can, the top of which is intact and unopened. It sits on a white cutting board, surrounded by the remnants of previously chopped red onions. The can's label faces upwards, displaying its contents to the viewer, and no tools are present to suggest the beginning of an opening process. The environment suggests the preparation of a meal, likely involving the sweetcorn as a topping, indicated by the presence of two pizzas in the background awaiting further ingredients.

#### Sample 272 — Before

- Similarity: 0.4666
- Prediction: The crockpot is placed in a water bath, with a stream of water indicating a current of water. The water flows through the cringe, indicating that the water has been drained. The rim of the spout is visible, suggesting that the nozzle is a nozzle that has been placed in the water. A hand is guiding the hose, pointing to the rim, and a hand is holding the utensil, implying that the tap is in the process of swiping water.
- Reference: The ladle appears to be partially submerged in water, with its bowl facing downwards, allowing the stream of tap water to flow directly into it. The handle of the ladle is gripped firmly in the person's right hand, with fingers wrapped around it, suggesting that it is either being positioned for washing or is in the initial stages of rinsing. The surrounding area of the sink is cluttered, with various kitchen utensils and cleaning supplies in proximity, indicating an ongoing cleaning task. Bubbles or suds are not visible on the ladle at this stage, which could imply that it has not yet been soaped or is in the process of a preliminary rinse.

#### Sample 273 — Before

- Similarity: 0.3874
- Prediction: The sink appears to be in a state of flux, with a sprinkling of soapy water, suggesting that the water has been drained. The sink is positioned in sweeping motions, with the water edging toward the sink, suggesting a recent change in the water cycle. The soapy liquid is a light, suggesting it may be a solution, suggesting the water is still a little soiled. The water is slick, suggesting there may be some water in the sink. The kitchen sink is in pristine condition, with no visible debris, suggesting an ongoing cleaning process. The counter is cluttered with dishes, including a large one, indicating a kitchen sink may be in the process of being cleaned
- Reference: The top appears to be a flat surface, likely made of a dark material, perhaps a type of stone or synthetic countertop material. The image captures a moment where a hand is holding a white mug with a pinkish glowing base, and the contents inside the mug resemble some type of food, possibly dumplings or a similar dish. The surrounding area of the top shows a stove or cooktop with at least two burners, one of which has a dark pan placed on it.

#### Sample 275 — Before

- Similarity: 0.4066
- Prediction: The coffee pot is positioned in a kitchen sink, with a lid positioned at the top, indicating it is in the process of being filled. The lid is a white ceramic, with an opaque surface, suggesting it is awaiting a refill. The coffee maker's handle is angled slightly, suggesting that it is not yet fully filled. There are no visible objects, including a coffee mug, a mug or a cup, and a hand-held device, which indicates it is still in the brewing process. The pot is in pristine condition, with no visible marks or markings, and the lid is in its original position, suggesting the coffee pot has been boiled.
- Reference: The cap burner in this frame is positioned amidst other objects within the vicinity. It seems to be resting securely on the burner base. The reflection and shadow patterns on its surface suggest ambient lighting from above. The cap's edges are distinct, and the inner section shows slight color variations, possibly from usage or lighting effects. The immediate surroundings have other kitchen items, but the cap burner is the focal point.

#### Sample 278 — Before

- Similarity: 0.2440
- Prediction: The dough appears to be a thin, uncooked dough, with a light brownish color, indicating it has been rolled. The dough is a solid, asymmetrical shape, with the edges of the dough forming a smooth, rounded shape. The texture of the texture is reminiscent of a dough, implying that it is being rolled, resulting in a uniform texture. The surface of the flour appears to have been kneaded, suggesting that the dough is still a bit sticky, owing to the presence of traces of flour in the dough. The flour appears slightly sticky, suggesting a more gradual process of rolling, forming an even, uniform texture, contrasting with the dough's texture
- Reference: The film cling is held within its cardboard package, with only a portion of it being visibly pulled out. The transparent film, as it exits the box, displays some wrinkles and irregularities in its structure, likely due to the extraction process. The edge of the cling film is still connected to the box's serrated cutting edge, suggesting it has yet to be torn off for use.

#### Sample 279 — Before

- Similarity: 0.3393
- Prediction: The microwave appears to be in a position to be positioned in obscurity, with its lid positioned slightly below the microwave's edge, suggesting that it is positioned at a slight angle, indicating that the microwave is not yet fully positioned. The microwave'
- Reference: The cabinet appears partially open, with its door ajar, revealing contents that include a variety of items such as food containers and perhaps small kitchen appliances. The interior shelves are not fully visible, but from what can be seen, they appear to be moderately filled. The cabinet's exterior is white, matching the general color scheme of the kitchen, and it has a handle that is not clearly visible due to the angle of the shot. The blur in the image suggests motion, indicating the cabinet door is in the process of being moved.

#### Sample 281 — Before

- Similarity: 0.4244
- Prediction: The table is positioned on a white surface, with a reflective surface that is reminiscent of a kitchen counter, with the surface of the table indicating a recent cleaning. The table's surface is a dark brown, with an orange hue, suggesting a cleaning process. The surface is slightly damp, with some areas of the surface showing signs of scrubbing or abrasion. The surrounding area is cluttered, with several items indicating that the table is still in its place. The hand is pointing at the table, indicating the presence of crumbs or other debris, and the table'
- Reference: A hand is pressing the nozzle of a spray bottle, emitting a fine mist of detergent onto a white surface. The detergent disperses in small, glistening droplets, creating a slightly irregular pattern due to the angle and pressure of the spray. The light reflects off the droplets, highlighting their presence against the matte finish of the surface. The shadow of the person holding the bottle is cast over the area, suggesting an indoor setting with a light source above.

#### Sample 285 — Before

- Similarity: 0.3539
- Prediction: The sanitized spoon appears to be in a water bath, with a sprinkling of soapy water on the surface. The spoon is positioned in resembling a bowl, with the handle pointing downwards, indicating that it is in the process of being washed. The water is dripping from the spoon, resulting in scalding and a slight smudge on the spoon surface.
- Reference: The lemon squeezer piece is held in a vertical orientation with its lower section submerged in soapy water. It's grasped firmly at its upper end by a hand adorned with a black wrist accessory, suggesting the initiation of the cleaning process. The squeezer's metallic surface is partially visible, reflecting the overhead lighting, and hints of water droplets or residues cling to its curved contours. It's not yet clear how soiled the squeezer is, as the view is obstructed by the water and the hand's position.

#### Sample 287 — Before

- Similarity: 0.4449
- Prediction: The slices of bread are sliced in a pan, indicating that they are in the process of being sliced. The slices are positioned on a flat surface, implying they are being slicked, forming a smooth, overlapping pattern. The edges of the slices are slightly uneven, suggesting that they may be sliced at a medium pace, resulting in sloppy edges. The bread slices are still a little firm, suggesting they may have been sliced too quickly.
- Reference: The potatoes appear to be freshly placed in the pan, thinly sliced into semi-circular shapes. Each slice is generously coated with some type of seasoning or marinade, evident from the visible golden and shiny glaze. The pieces overlap each other, with many resting at the top, suggesting they haven't been stirred or cooked for long. The overall appearance indicates they're in the early stage of cooking, waiting to be evenly spread out and cooked to perfection.

#### Sample 293 — Before

- Similarity: 0.3263
- Prediction: The scrubbing brush is positioned in a position that is agitated by the water, indicating it is in the process of being rinsed. The brush is placed in resealable plastic wrap, anchored by a thin layer of water, and the water's sludge is visible. The nozzle is angled downwards, pointing to the water-filled portion of the spout, implying it is a medium-sized amount. The water'
- Reference: The colander appears prominently in the upper part of the frame, held by a person's hands. It is angled such that the bottom faces slightly away from the viewer, suggesting that it may have just been picked up or is in the process of being moved. The colander's interior is not fully visible due to its position, but it seems to be empty and clean, without any food particles or residue clinging to the holes. The lighting casts a soft glow on the white surface of the colander, highlighting its perforated pattern and the water droplets clinging to its surface, indicating recent rinsing.

#### Sample 294 — Before

- Similarity: 0.3693
- Prediction: The stove appears to be in a state of flux, with a visible portion of the burner visible, suggesting that the burner is still in use. The burner is positioned in slats, indicating that it is still being used, and the burner's surface is a dark brown color, suggesting a recent cleaning process. The stove's interior is cluttered with stains, and there are no visible signs of cooking. The kitchen counter is adorned with patterned paper towels, a sign of a kitchen sink, and a clogged sink.
- Reference: The towel appears to be a crumpled mass of white fabric, lightly soiled with what could be remnants of food or grease, suggesting recent use in wiping or cleaning. It's held loosely in the hand, with fingers slightly curled around it, indicating a casual or in-between action moment. The texture of the towel seems soft and pliable, showing no signs of stiffness, and the stains are not overly pronounced, indicating that the towel might still be in a usable condition for further cleaning tasks.

#### Sample 295 — Before

- Similarity: 0.4996
- Prediction: The sanitized bowl appears to be in a position to be positioned in resembling a kitchen sink, with a handle pointing downwards. The bowl is positioned on a counter, with the handle positioned at the center of the bowl, indicating that it is in the process of being cleaned. The rim of the slanted bowl is visible, suggesting that the bowl is being cleaned, and the bowl's surface is being wiped down with lint, suggesting a recent cleaning process. The sink is surrounded by a series of white towels, which are positioned near the bowl. The surrounding area is cluttered with soiled dishes, including one that is a little damp, and
- Reference: The strainer is held firmly in one hand, positioned under a running tap with water cascading through its numerous vertical slits. Its white plastic surface is dotted with remnants of food particles, particularly concentrated at the base where they seem to resist the rinse. The wear on the strainer's surface suggests frequent use, highlighted by the contrast of clean water flowing over less pristine areas. The strainer's grid-like interior is clearly visible, acting as a barrier to the larger debris while allowing water to pass through.

#### Sample 297 — Before

- Similarity: 0.3295
- Prediction: The chicken is positioned in a kitchen, with its skin exposed, revealing a smoky texture. The meat is sliced in angular slices, indicating it is in the process of being cooked. The skin is a dark brown, contrasting color, suggesting it may be a rare or uncooked chicken. The chicken's skin is covered in slender, spongy pieces, suggesting the meat is being prepared. The knife's edge is angled, suggesting a slight movement, implying the meat has been sliced. The kitchen's lighting is dim, suggesting that the kitchen is preparing the chicken.
- Reference: The cutting board is held at an angle, with the edge slightly elevated over a pan filled with other ingredients. A single garlic clove rests on the board, and it appears partially crushed, with its papery skin still attached but flayed open, indicating that it has been prepared for mincing or crushing. The garlic’s yellowish hue suggests it's fresh, and there's a visible moistness on the clove, possibly from the garlic juice being released due to the pressure applied. The person's hand is positioned as if they have just finished or are about to continue the crushing process.

#### Sample 298 — Before

- Similarity: 0.2828
- Prediction: The saucepan appears to be in a position to be positioned in spluttering motion, with a slender, curved edge indicating a medium-sized amount of water. The surface of the saucepan is cluttered with smoky residue, suggesting that the saucepan has been boiled. The saucepan's surface is a dark brown color, suggesting a light or liquid presence. The pan's interior is reminiscent of a kitchen counter, with its rims and handles pointing toward the stove. The kitchen sink is positioned near the stove, indicating that the stove is still running. The stove's lighting is dim, suggesting the stove has been turned on. The sink's light is dimly lit,
- Reference: The gloves appear to be durable rubber kitchen gloves, commonly used for washing dishes or cleaning to protect the hands from water and detergents. They are bright yellow, a standard color which suggests their use in household chores. The gloves extend to the mid-forearm, providing ample coverage. In this frame, the glove on the left hand is gripping a white bowl near the sink, fingers curved around the edge, indicating a firm grip. The texture of the gloves seems slightly wrinkled, a characteristic that often occurs when the material is flexed.

#### Sample 302 — Before

- Similarity: 0.4763
- Prediction: The box appears to be a plastic bag, with a lid, a handle, and a top that is positioned on top of the box. The lid is a rectangular shape, with the top of it being a white, indicating a spherical shape. The box's interior is cluttered, with its contents scattered around the box, implying a gradual process. The person's hand is likely preparing to open the box and removing the lid, which is likely to be in the process of opening. The bag appears to have been opened, with some of the contents visible, including the lid's cap, which appears to indicate a slight opening.
- Reference: The carton of milk is being grasped firmly by a right hand, with the cap in a slightly rotated position, indicating it has been unscrewed or is in the process of being closed. The green cap contrasts with the predominantly white color of the milk carton, which bears a label with distinct green accents and a circular logo. The carton appears nearly full, with no evident signs of crumpling or squeezing, suggesting that it has been recently opened or is well-preserved. The person is standing in a domestic setting with neutral-colored flooring and a black sandal visible on their left foot, contributing to a casual, everyday atmosphere.

#### Sample 303 — Before

- Similarity: 0.3927
- Prediction: The bottle is positioned in a kitchen, with a lid positioned on top of the bottle, indicating that it is in the process of being opened. The lid is firmly attached to the bottle's handle, suggesting that the bottle is in resealable condition. The bottle'
- Reference: The aluminum beverage can is captured in a near-upright position on a wooden table. A person's hand, adorned with a metallic watch, is gently grasping the can from its side, with fingers wrapped around its circumference. There is another circular object on the table, possibly a glass coaster or the can's lid. The table surface has a rich wood grain, with visible streaks and knots, and there's a black mat adjacent to the can.

#### Sample 304 — Before

- Similarity: 0.3590
- Prediction: The jar appears to be in a position to be positioned in resembling a kitchen sink, with a handle pointing downwards, suggesting a recent movement. The rim of the jar is cluttered with slender items, including a tupperware container, a plastic bag, and a bowl of ice. The lid is positioned on top of the container, suggesting that it is in the process of being placed. The surrounding area is a well-lit kitchen, with the kitchen sink and the kitchen counter positioned near the holder. The kitchen counter is anchored to the rim, with its contents positioned at the center of the frame.
- Reference: The tin presents as a well-used baking dish with signs of extensive wear, indicating a history of repeated culinary ventures. Its surface is mottled with baked-on residues and staining that speak to a rich tapestry of past meals, perhaps sweet or savory dishes that have left their indelible mark over time. The corners and edges of the tin exhibit darker discoloration, particularly pronounced in areas where heat would have been most intense, further testifying to its service in many a heated oven.

#### Sample 305 — Before

- Similarity: 0.3534
- Prediction: The vegetable appears to be in a state of flux, with a thin layer of a thick layer of vegetables positioned in the middle of the frame, indicating that the vegetable has been boiled. The vegetables are positioned on a plate, presumably a medium-sized portion, with the lid pointing towards the pan, suggesting that the vegetables are still a little bit hot. The pan is positioned near the edge of the vegetable, with its lid positioned slightly above the vegetable. The vegetable is a bright green color, with an orange hue to it, suggesting a light or medium-colored vegetable.
- Reference: The countertop is partially visible, composed of a light-colored, solid surface with few distinct features. To the left, there's a stainless steel double sink with one basin empty and the other holding a plastic dish rack filled with kitchen utensils and plates. A solitary, well-used sponge rests on the divider between the sinks. The countertop adjacent to the sink appears wet, possibly from recent cleaning or dishwashing activities, with water droplets scattered across the surface. Visible in the lower right corner is an individual's forearm, lending a sense of scale and human presence to the scene.

#### Sample 308 — Before

- Similarity: 0.4235
- Prediction: The crockpot is placed in a water-filled bucket, with a stream of water dripping from the bottom. The water is drained from the top of the cringe, indicating that it is being washed. The rim of the bowl is positioned in sandpaper, pointing to the water's eroding surface. The bowl is covered in mud, with water accumulating on the sides, implying a recent watering. The surface of the sink is cluttered with water, resulting in clumps of soapy water. The faucet is affixed to the rim, suggesting a gentle watering process.
- Reference: The baking tray in the image is a large, rectangular, dark-colored vessel, possibly made of metal with a non-stick surface, placed under running water from a white tap. The tray appears quite dirty, with patches of grime and food residue clinging to its interior surfaces, indicating recent use. It’s being held by a person with a silver bracelet on their left wrist, suggesting that they are in the midst of cleaning it. The contrast between the dark tray and the bright yellow tiles of the kitchen adds to the visibility of the soiling.

#### Sample 309 — Before

- Similarity: 0.2880
- Prediction: The chicken is placed in a kitchen sink, with the lid open, indicating it is in the process of being rinsed. The skin is bare, with a thin layer of white flesh on the inside, a sign of the chicken's recent processing. The chicken'
- Reference: In this frame, the metallic tap over the kitchen sink is positioned in a downward angle. The faucet appears to be turned off, as there is no visible flow of water emanating from it. The surface of the tap is reflective, and a chain-like apparatus is attached near its base, possibly serving as a plug mechanism for the sink.

#### Sample 312 — Before

- Similarity: 0.3041
- Prediction: The onion is sliced in half, with the ends facing downwards, indicating that it has been trimmed. The skin is a dark brown, atypically white, with a few small bumps and a slight smoky hue. The onion's flesh is reminiscent of a slicked potato, with its flesh a little spongy and slender, suggesting that it may be a vegetable. The person holding the onion is likely preparing to peel it, implying that they are preparing the onion for the next step.
- Reference: The green beans are captured in the midst of preparation, with some already trimmed and neatly collected inside a white colander with numerous draining holes. The colander is designed in a unique apple shape, adding a playful aesthetic to the task. The beans appear freshly cut, indicated by the moist ends where the stems were removed. The individual holding the beans is in the process of trimming, as evidenced by the green bean in hand, with one end already cut and the other poised for trimming. Small cut pieces of the stem can be seen discarded on the black countertop, and the container of untrimmed beans sits nearby, waiting to be processed.

#### Sample 320 — Before

- Similarity: 0.3966
- Prediction: The chicken is positioned in a kitchen, with its skin exposed, revealing a thin layer of meat. The meat is sliced in slicing motion, indicating the meat has been cooked. The skin is a dark brown, contrasting color, suggesting the meat is being prepared. The chicken's skin is covered in crumbs, suggesting it has been boiled. The knife is pointing at the meat, suggesting that the meat may be preparing for cooking. The hand is demonstrating the process of removing the meat from the skin, implying the meat was cooked.
- Reference: The sweet potato skin appears freshly sliced, revealing a bright orange interior, indicative of a recent cut. The peel segments are irregular in shape and size, scattered haphazardly on the wooden cutting board, some still attached to chunks of the sweet potato flesh. The edges of the skin are slightly curled up, a natural response to being separated from the dense, moist flesh. One can observe the contrast between the rough, textured outer surface of the peel and the smooth, moist inner surface that was against the sweet potato flesh.

#### Sample 324 — Before

- Similarity: 0.4648
- Prediction: The fish is sliced in half, with the meat sliced into bite-sized pieces, indicating the first time the person has cut the meat. The flesh is a dark brown, charred, and slightly smoky, with a light brown color to the meat, suggesting a slight cooking process. The skin is slender, with its flesh akin to a skewer, suggesting the person is preparing the meat for cooking. The knife is positioned in the middle of the fish, implying the person's initial handling of the meat to ensure the meat is cooked to the desired consistency.
- Reference: A small portion of sweet potato is visible on a white cutting board. The sweet potato chunk appears freshly cut, with a bright orange interior that stands in contrast to its brown, slightly rough skin. The knife, which likely was used for the cutting, rests next to the potato piece, and it glistens subtly, hinting at its recent use. The way the potato sits on the board suggests it's been placed there momentarily, perhaps after being cut, and there's a certain rawness to its appearance, characteristic of fresh produce.

#### Sample 328 — Before

- Similarity: 0.4329
- Prediction: The bag appears to be a plastic container, with a lid that is partially open, suggesting that the contents are being thrown out. The lid is positioned in a position that indicates that the bag is being opened, indicating that the person is preparing to open the bag. The bag's contents are positioned on a counter, suggesting a gradual opening of the bag, implying that the individual is attempting to open it. The person's hand is pointing at the bag'
- Reference: The slice of bread is being held by a person's hand, captured mid-motion as it's moved towards a toaster. The bread appears to be a piece of wholegrain or multigrain toast, with visible seeds and grains throughout its surface, suggesting a health-conscious choice. The hand gripping it seems to be in the midst of an action, likely having just retrieved it from the bread bag resting on the counter. The bread itself is in focus, with the background slightly blurred due to the movement, emphasizing the slice as the central element of the frame.

#### Sample 329 — Before

- Similarity: 0.4861
- Prediction: The bottle is positioned in a kitchen, with a lid positioned on top of it, indicating that it is in the process of being opened. The lid is a dark brown, slender, and a jar-shaped container, suggesting that it may be a food container. The bottle's interior is cluttered, with its contents positioned neatly on the top of the bottle, suggesting a gradual opening. The container's surface is bare, suggesting it may have been a container for a liquid or other liquid, implying that it was a solid container.
- Reference: The bag appears to be partially opened, exposing a small section of its contents which look like bread. The bag is of a transparent nature with an orange label, suggesting it could be store-bought bread. The surrounding area includes other household items, but the main focus is the bag with a person's hand reaching towards it, hinting at the intention to open it further or take out its contents.

#### Sample 332 — Before

- Similarity: 0.4152
- Prediction: The oven door is partially open, with a hand in the middle of the door, suggesting a person is preparing to open the door. The door is positioned in a position that is likely to be open during the moment, indicating that the oven is about to close. The oven's interior is cluttered with utensils, including a dish towel, a plate, and a tray. The kitchen is surrounded by a kitchen counter, which is anchored to the oven'
- Reference: The freezer drawer is captured in mid-motion, slightly ajar with a gap visible between the drawer and the freezer frame, indicating that it has just begun to close. The edges of the drawer exhibit a matte finish, perhaps due to the cold temperature within, while the contents remain obscured by the blurred motion. The slight angle and position of the drawer suggest a quick, perhaps forceful movement, with the potential for items inside to shift due to the speed of closure.

#### Sample 333 — Before

- Similarity: 0.3766
- Prediction: The jar appears to be in a kitchen, with a lid positioned on top of the container, indicating that the contents are being poured into the container. The lid is positioned in slender, overlapping sections, suggesting that the container is being emptied. The container is surrounded by a thin layer of plastic, suggesting a gradual process of soaking the jar in water. The spherical shape of the sprigs suggests that the jug is a jumbo-sized portion of a large, oversized jar, implying that the lid is being placed in resealable storage.
- Reference: The bread appears to be partially enveloped in a translucent plastic bag, with the opening twisted and held by the person's left hand, which suggests that the bread is being secured or possibly about to be unwrapped. The visible portion of the bread seems slightly compressed by the grip, hinting at its soft, yielding texture. There are specks of what might be crumbs or seeds on the countertop, indicating recent activity, possibly related to the bread being handled.

#### Sample 334 — Before

- Similarity: 0.4514
- Prediction: The paper is positioned in a kitchen, with a white plate and a blue-green paper towel on the side. The paper has a slender, slightly curved edge, indicating it is being prepared for use. The hand is pointing at the paper, which appears to be a plastic bag, with its edges rounded, suggesting it is a food item. The person's hand is likely preparing to open the paper and removing the paper towel, which is likely to be in the process of being opened. The tray is stacked against a wall, with the paper towels positioned on the sides of the tray, implying the person is attempting to open it. The table is surrounded by a set of
- Reference: A slice of bread is being held in a hand, slightly angled to the side, displaying its golden-brown exterior with slight toasting around the edges. The bread's porous texture is evident, with small air pockets and a gentle crust. The hand is midway through spreading a thick, white, creamy substance, likely mayonnaise or a similar condiment, across the surface of the bread. The spreading is uneven, with more of the substance near the knife edge and less toward the far side, indicating the action is not yet complete. The substance's peaky texture suggests it has a stiff consistency.

#### Sample 335 — Before

- Similarity: 0.3581
- Prediction: The table is positioned in a position that is reminiscent of a kitchen counter, with a white surface and a dark brown hue. The table's surface is cluttered with crumbs, indicating that it is not yet ready for use. The surface is slightly damp, suggesting that the table is still damp. The hand is presumably preparing to place the table, pointing to the table'
- Reference: The degreaser appears as a white mist, consisting of fine droplets in mid-air, captured as they disperse across the surface in the upper right quadrant of the frame. The motion of the degreaser is dynamic, indicating that it has just been sprayed from the bottle, which is held in the right hand of the individual. The droplets are densest nearest the nozzle, indicating the recent activation of the spray mechanism. Below the area of the spray, the countertop remains visibly dry, reflecting the light from above, suggesting that the degreaser has not yet had time to settle or spread across the surface.

#### Sample 336 — Before

- Similarity: 0.4008
- Prediction: The coffee pot is placed in a water-filled pot, with a faucet positioned near the bottom. The water flows downwards, indicating that the water has been drained. The pot is surrounded by a stream of water, suggesting that the pot is being dripped. The faucet is positioned in alternating between the two, allowing the water to flow downwards and the pot to remain dripping. The coffeepot is a white, slender object, pointing at a coffee pot, a mug, or a cup, containing a small amount of coffee. The cup's interior is cluttered with smoky residue, suggesting a recent cleaning process. The surrounding water is
- Reference: A hand is gripping a piece of cutlery, a fork, under a stream of water flowing from a silver-colored faucet with a slight curvature. The tines of the fork are positioned downwards, perpendicular to the stream, suggesting the initial action of rinsing. Soap bubbles cling to the base of the tines and handle, indicating recent scrubbing activity. The surrounding area is cluttered, with other kitchen items and a purple sponge visible, and a bottle of liquid soap prominently in the background, contributing to the domestic cleaning context.

#### Sample 338 — Before

- Similarity: 0.3711
- Prediction: The pan appears to be in a medium-sized pot, with a thin layer of oil on the bottom, indicating that it is in the process of cooking. The oil is a light brown color, implying that it has been frying for a long time. The pan is positioned in sprinkling a layer of olive oil on top, a sign that the oil is still hot. The surface of the pan is slightly exposed, suggesting that the cooking process is still a bit slow. The edges of the skillet are slightly exposed and the pan appears a little sloppy, suggesting the cooking is still going on. The skillet appears to have been preparing the oil for frying, presumably to ensure that the pan has not
- Reference: The extractor fan situated above the stove is in a visibly used state, with a distinct pattern of grease and vapor deposits concentrated in the center, spreading outwards to the edges. The coloration of these deposits varies from dark brown at the center to a lighter, amber-like hue towards the periphery, indicating a combination of both recent use and an accumulation over time. The fan's surface has a matte finish, which suggests it is not currently in operation, as an active fan would likely reflect some of the ambient light from the surrounding area.

#### Sample 341 — Before

- Similarity: 0.2801
- Prediction: The cutting board appears to be in a position where it is being held by a person's hand, with the blade pointing downwards. The blade is positioned in overlapping motions, indicating that the cutting board is in restraining motions. A hand is attempting to remove the blade from the board, pointing to the blade's surface, which is likely to be a chopping block. The board appears agitated, suggesting that the blade is being slammed against the board. The surface appears to have been soiled, suggesting a recent cleaning process.
- Reference: The tablecloth appears predominantly white with a large, vivid green apple design in the center, suggesting a fresh, crisp theme. It is stretched out across the surface, occupying a significant portion of the frame, with an emphasis on the apple's detailed depiction that includes a spectrum of green shades and visible brush strokes, adding a textured, artistic touch. The tablecloth's edges are not visible, indicating it is fully spread out, and the surface wrinkles suggest it has been used rather than freshly laundered or ironed.

#### Sample 342 — Before

- Similarity: 0.4572
- Prediction: The sanitizer is placed in a sink, with a faucet in the middle, indicating that it is in the process of being rinsed. The nozzle is positioned in overlapping motions, pointing to the kitchen sink, implying that the water has been drained. The water is dripping from the sink, suggesting that the sans have been soaked. The sink is surrounded by a stream of water, suggesting a waterlogged environment. The faucet is swung open, suggesting the water is still running.
- Reference: The teaspoon appears to be in the initial stages of cleaning, held securely in someone's hands over a beige kitchen sink. The sink is partially filled with soapy water, and a purple sponge is being used to scrub the spoon's surface. The teaspoon itself is shiny, suggesting it is made of stainless steel, and it reflects the overhead lighting, hinting at its still unclean status with potential residue or water spots visible on its surface. A bottle of dish soap stands nearby, indicating the cleaning process is actively underway.

#### Sample 349 — Before

- Similarity: 0.4641
- Prediction: The microwave is positioned on a counter, with a white plate and a black plate, suggesting a kitchen setting. The plate is a rectangular shape, with an oval-shaped design, suggesting it is shaped like a microwave oven. The counter's surface is cluttered, with the plate and plate stacked in a single row, suggesting that the microwave is not fully occupied. The countertop is surrounded by a series of white plates, indicating that the oven is not yet fully stocked. The kitchen counter is anchored to a wall, with white plates and trays, suggesting the microwave has been plugged in. The microwave's interior is reminiscent of a modern kitchen, with its white counter top, white counter,
- Reference: The image depicts a wall-mounted electrical socket with two switches, each connected to a plug. The left switch is in the off position, as indicated by the visible red band on the switch, typically a universal sign for 'off' on many UK appliances. The right switch is in the on position, without a visible red band, and is powering a white kettle. The person's hand is in motion towards the left switch, with their index finger extended, poised to flick the switch. The surrounding area is cluttered with various kitchen items, including a toaster to the left and a microwave oven to the right, which suggests the setting is a home kitchen.

#### Sample 351 — Before

- Similarity: 0.4093
- Prediction: The bag appears to be a plastic bag, with a white label on the side, indicating that it is in the process of being opened. The bag is positioned in a position that indicates that it has been opened, presumably to store food or other items. The person's hand is likely preparing to open the bag, which is likely to be in the middle of a kitchen or kitchen counter. The packaging is a clear, unadorned bag, containing a variety of items, including a jar, a small plastic container, and a lid. The contents of the bag are positioned on the inside, with the lid positioned at the top of the pouch, implying that it was opened.
- Reference: The olive oil bottle appears to be a standard size, with a metallic cap that is placed adjacent to the bottle on a black, glossy stovetop surface, reflecting the ambient light. The bottle itself is not in view, suggesting it may be upright and out of the frame or placed elsewhere. The cap is positioned with its open end facing upwards, indicating it has just been removed and set aside temporarily. Nearby, there are scattered items on the stovetop, including a paper bag and what appears to be a packet of food, contributing to a sense of ongoing kitchen activity.

#### Sample 353 — Before

- Similarity: 0.3595
- Prediction: The coffee pot is positioned on a counter, with a lid containing a removable lid, suggesting that it is in the process of being placed. The lid is a white, spherical shape, with an oval-shaped shape, suggesting a brewing process. The pot's interior is cluttered with slender, patterned ceramic pots, indicating that the pot is in a pre-determined state. The coffee maker's lid is lined with piping, suggesting it is awaiting a refill. The surrounding area is bare, with no visible evidence of any food or other items.
- Reference: The button appears to be in a neutral state, unpressed and intact, showing no signs of deformation or displacement. It is situated among a cluster of other buttons, all of which seem to be similarly at rest. The surface of the button reflects a certain amount of ambient light, indicating a smooth, possibly plastic material. Its color blends with the surrounding buttons, suggesting a user interface designed for uniformity. The finger is positioned above the button, casting a slight shadow, but not yet exerting any pressure that would indicate activation.

#### Sample 354 — Before

- Similarity: 0.3554
- Prediction: The sink appears to be in a state of flux, with a spout of water dripping from the bottom, suggesting that the water is still circulating. The sink's surface is cluttered with slats, which suggest that the sink is still in the process of removing the water. The water is a dark color, suggesting a watery environment. The faucet is positioned in recessed position, suggesting the water has been drained. The kitchen sink is surrounded by a series of sinks, suggesting there may be a slight movement in the sink. The surrounding area is reminiscent of a kitchen sink, with its rounded edges and rounded corners, suggesting it may be in the middle of preparing
- Reference: A ladle with a bright yellow handle and a reflective, stainless steel scoop is held mid-air, seemingly captured in the midst of an action. Its position is off-center towards the lower part of the frame, pointing diagonally upwards, suggesting an upward or forward motion. The ladle's handle appears sturdy and ergonomic, with a slight curvature that fits comfortably in a grip, as indicated by the fingers wrapped securely around it. The scene is domestic, with a kitchen countertop visible, and various items such as a wooden spoon resting in a white spoon rest, a clear glass with a green motif, and a plastic water bottle in motion, caught mid-roll towards the edge of the counter.

#### Sample 355 — Before

- Similarity: 0.3699
- Prediction: The boiled sage appears to be in the middle of its preparation, with the stems pointing downwards, suggesting that the stem is being prepared for cooking. The leaves are positioned in a position that indicates that they are being prepared to be cooked, with a slight tilt to the surface of the steamed sachet. The sprigs are arranged in overlapping rows, indicating that the boiled portion is being sliced. The leafs are lined with slicing tips, suggesting a gradual process of scrubbing the sliced sages.
- Reference: The pak choi leaf rests partially on a wooden cutting board and partially in a person's hand. The green leafy top is vibrant and contrasts with the paler, more fibrous white stem. It appears fresh, with no visible wilting or discoloration, indicating recent harvest or proper storage. The leaf's structure is mostly intact, with only the base of the stem showing signs of an initial cut, suggesting the slicing process has just begun.

#### Sample 356 — Before

- Similarity: 0.3742
- Prediction: The kitchen sink appears to be in a state of flux, suggesting that it is not yet fully stocked. The sink's surface is cluttered with a variety of items, including a pot, a bowl, and a dish. The kitchen's lighting is dim, suggesting a low-light setting, and the sink'
- Reference: The mixture in the pan appears to be in the initial stages of cooking, with a moderate amount of clear liquid pooling around the ingredients. Scattered throughout the liquid are green components, which resemble sliced green parts of spring onions or possibly green bell peppers, not yet softened by the heat. Their shapes are irregular, and they float separately in the liquid without clumping together. There is a visible sheen on the surface, indicating the presence of oil or another cooking fat, aiding in the sautéing process. The edges of the mixture are not sticking to the pan, suggesting that it is being stirred frequently or that the heat is appropriately moderated.

#### Sample 359 — Before

- Similarity: 0.2798
- Prediction: The cloth appears to be soaked in a liquid, indicating it is in the process of being washed. The cloth is a dark brown, with a light yellow hue, a sign of the presence of soap or detergent. The water is scalding, suggesting it is soaking for a long time. The hand is positioned in the middle of the cloth, presumably a beginner's hand, with the hand pointing towards the cloth. The fabric is soaked, suggesting the cloth is still wet, and the water is likely to be running.
- Reference: The bin is situated in the lower right corner of the image, just beside a white dish rack that houses various kitchen utensils. It appears slightly overfilled, with its contents reaching above the rim, indicating a pressing need for emptying. A clear plastic bag lines the bin, and items within seem to be a mix of food waste and other household refuse, suggesting recent kitchen activity. The positioning of the bin, tucked away under the counter, implies an efficient use of space in a kitchen where activities are underway.

#### Sample 361 — Before

- Similarity: 0.4594
- Prediction: The sliced meat is positioned on a plate, with its edges exposed, indicating the meat is being prepared. The meat is covered in a thin layer of fat, suggesting that it is being cooked. The skin is a dark brown, revealing a smoky texture, suggesting the meat has been boiled. The knife's edge is firmly held, suggesting a slight movement, implying the meat may be ready to be sliced. The blade is angled slightly, suggesting it is preparing to slice. The slicing motion is indicative of the meat's preparation process, suggesting its preparation is pending.
- Reference: The pepper is fully encapsulated in a clear plastic wrap, presenting a vivid contrast against the yellow cutting board. It's nestled between a green and a yellow pepper, suggesting they are part of a multi-colored pack. The untouched plastic suggests the initial stage of the culinary preparation process. The individual's hand is positioned over the green pepper, implying an imminent action, perhaps to commence the unwrapping or cutting. The surrounding area is littered with onion skins and garlic cloves, indicating ongoing cooking activity.

#### Sample 362 — Before

- Similarity: 0.3179
- Prediction: The cloth appears to be a bare, slick, rippling fabric, with a thin, wavy texture. Its surface is a dark brown, indicating it has been soaked in water. The cloth is positioned in a position that indicates it is in the process of being washed, with the cloth firmly pressed against the cloth, resulting in slouching. The fabric appears to have been soaking for a long time, exhibiting a smooth, supple texture, a characteristic of the fabric. The texture of the cloth is slightly damp, suggesting that the fabric may be wet or damp. The material appears to appear to be wetting, with its surface indicating that the
- Reference: The water tap, constructed of a material with a metallic sheen, is captured at the moment it is releasing water. The flow is moderate, creating a cascade that impacts the sink's basin and generates a spray of water droplets visible against the basin's surface. The tap's handle is positioned at an angle that suggests it is in the 'on' position, allowing water to flow freely. Surrounding the faucet, various kitchen items can be discerned, contributing to a scene of domesticity.

#### Sample 364 — Before

- Similarity: 0.2959
- Prediction: The jar appears to be in a kitchen setting, with a white handle and a black handle, suggesting a hand-held device. The lid is positioned in slats, indicating that it is not yet fully inserted. The rim of the jar is a dark brown, contrasting color, suggesting that it may be a plastic container. The hand is pointing at the holder, suggesting it is seated in resemblance to a wooden spoon, suggesting the jug is not fully positioned. The handle is angled slightly, suggesting its position is not immediately apparent. The surrounding area is cluttered with jars, including a small kitchen sink, a microwave, and uten
- Reference: The sweet potato in this frame exudes a fresh and robust appearance. Its skin, mostly smooth with a few natural blemishes, holds a rich orange-brown hue, hinting at its natural earthy origins. The oblong shape of the tuber is accentuated by subtle curves and a slightly tapered end. There's a faint glisten on its surface, perhaps from being freshly washed or due to ambient light. One can almost sense its starchy texture and sweet aroma just by looking at it.

#### Sample 365 — Before

- Similarity: 0.4040
- Prediction: The stove appears to be in a state of flux, with a visible portion of the burner visible, suggesting that the burner is still plugged in. The burner is positioned on the stovetop, with the burners positioned in contrasting positions, suggesting a recent change in the burner settings. The stovetop is surrounded by a series of white ceramic plates, indicating that the oven has been re-gassed. The counters are positioned near the stove, with one of the white plates pointing to the stove. The other plate is a white ceramic plate, suggesting the oven is still running. The countertop is cluttered with stains, suggesting there may be a slight smudge on the surface, implying a cleaning
- Reference: The hob surface in this frame appears to have a somewhat creamy-textured substance spread across it. The consistency of the substance gives the impression of a sauce or liquid that has been spilled or is in the process of being cleaned. There's an evident sheen on the surface, indicating the presence of moisture. On the right side of the hob, we can see some containers and kitchen items, and on the left, there appears to be a hand with a blue cloth, presumably in the act of cleaning.

#### Sample 367 — Before

- Similarity: 0.3449
- Prediction: The jar appears to be in a kitchen, with a lid positioned at the top, indicating that the contents of the jar are being poured into the jug. The lid is positioned in slender, curved position, suggesting that the slurry is being dipped in ice water, implying that the liquid has been boiled. The jumbo-sized jar is surrounded by a thin layer of ice, suggesting a gradual process of blending the ice and allowing the whipped cream to settle. The liquid appears to have been poured onto the jicama, suggesting the blending process is underway. The glass is a dark, reflective, opaque, and
- Reference: The cap appears to be in a dimly lit setting, making the details slightly obscured. From the visible portion, it seems to be situated amidst various household items. The angle at which the cap is positioned does not offer a full view, providing only a partial glimpse of it. The surrounding environment has a chaotic appearance with multiple objects scattered around, drawing attention away from the cap itself.

#### Sample 368 — Before

- Similarity: 0.3645
- Prediction: The bag appears to be a plastic bag, with a spherical shape, indicating it is in the process of being opened. The person's hand is positioned in the middle of the bag, presumably preparing to open the contents. The bag is a white, opaque, opaque plastic bag with contrasting markings, suggesting it is awaiting its contents.
- Reference: The tomatoes appear freshly opened from a sealed, rectangular plastic can, with the lid being peeled back by a pair of hands. The contents are vibrant red chopped tomatoes, steeped in their own juice, with a noticeable gleam that suggests a high moisture content. Small bits of tomato pulp and seeds are visible, indicating a coarse chop. The can's label, facing downwards, is not fully visible, but the color and texture are unmistakably those of canned chopped tomatoes.

#### Sample 369 — Before

- Similarity: 0.3263
- Prediction: The slat appears to be a bare, soiled piece of paper, with a thin layer of paper on the surface. The paper is positioned in a hand-held device, with the handle pointing downwards, indicating a recent process. The crease is asymmetrical, with its edges angled slightly downwards. The surface of the paper appears to have been soaked, with water dripping from the surface, resulting in slickness. The water is drenched, suggesting a gradual process.
- Reference: The filter appears to be a metal kitchen strainer with multiple perforations, primarily used for draining food items. Its surface glistens with moisture, suggesting it has recently come into contact with water or some liquid. Settled at the bottom of the filter is a small amount of residual water, reflecting the ambient light. The metal has a worn look, showing signs of use with visible mineral deposits or staining. Next to the filter, one can observe a green liquid detergent container, further indicating the kitchen context.

#### Sample 371 — Before

- Similarity: 0.3761
- Prediction: The courgette appears to be in a medium-sized bowl, indicating it has been boiled. It is a light brown color, implying it has just been cooked. The leaves are a little smoky, suggesting they may be a bit charred, suggesting that they may have been steamed. The green leaves are slightly charring, suggesting the courgettes may have cooled slightly, suggesting a slight cooking process.
- Reference: The spatula is held at a slightly angled position, hovering over a pan that contains diced vegetables, presumably being sautéed. The hand grasping it appears to be mid-stir, suggesting a gentle but firm motion. The utensil itself looks to be made of a dark material, possibly non-stick plastic or silicone, suited to the task of cooking without scratching the pan's surface. Its flat edge and slotted design indicate that it's meant for flipping or turning food items while allowing excess oil or liquid to drain through the openings.

#### Sample 372 — Before

- Similarity: 0.3801
- Prediction: The bin appears to be in a position to be positioned in obscurity, with the lid positioned slightly below the bin's hinges, suggesting that the bin is in limb or limb motion. The bin'
- Reference: The basket appears in a dynamic state, captured in a blurred motion suggesting swift movement. The contents within the basket are indistinguishable due to the high speed of the action, with colors melding into streaks across the frame. The basket's form is elongated horizontally, indicating rapid horizontal displacement, possibly due to it being dropped or thrown. The surrounding environment is also captured in a blur, with the flooring providing the only stable visual anchor, its orange hue casting a warm tone on the scene.

#### Sample 376 — Before

- Similarity: 0.3584
- Prediction: The cactus is positioned in a kitchen sink, with a water-filled bowl containing a handful of vegetables, including broccoli, lettuce, and tomatoes. The bowl is cluttered with cacti, indicating that the vegetables are being prepared. The water-soaked bowl is filled with water, implying that the ingredients are being boiled. The kitchen sink is surrounded by a stream of water, suggesting that the water has been boiled, a sign of the process of cooking. The dish is a coiled, shaped like a carrot, with its stems pointing towards the camera. The camera's focus is on the vegetables, which are positioned near the water's surface, pointing to the
- Reference: The cucumber appears to be relatively dry and untouched by water. The person's hands are not yet interacting with the cucumber directly. The cucumber's skin looks smooth with a shiny green hue, indicative of its freshness. There are no apparent blemishes or imperfections on the visible part of the cucumber, and it rests against the side of the sink, yet to be cleaned.

#### Sample 378 — Before

- Similarity: 0.4855
- Prediction: The vegetables are stacked on a white plate, indicating they are in the process of being chopped. They are positioned in a circular motion, implying they are being sliced. The surface of the plate is cluttered with a variety of vegetables, including broccoli, cauliflower, and cauliflower. The vegetables appear to be ripe, suggesting they may be a little stale. The pan is surrounded by a series of green leaves, suggesting that they are ripening, suggesting the vegetables are still in the middle of their preparation. The leaves are arranged in overlapping, suggesting a gradual process of slicing. The vegetable appears to be in the early stages of cooking, suggesting it has been preparing for a long
- Reference: A gas hob displays a single black pan centered on the front right burner, which is alight, suggesting cooking is in progress. The pan contains diced vegetables, primarily zucchini and carrots, being sautéed, as evidenced by the glossy sheen, possibly from oil. Cooking utensils — a spatula and a spoon — rest on the counter, within easy reach. To the left, a plate with remnants of food and a white spatula suggest a meal is being prepared or has recently been consumed. The hob appears to be clean, and the knobs on the hob front are in an undisturbed position, indicating a single burner in use.

#### Sample 379 — Before

- Similarity: 0.3546
- Prediction: The saucepan appears to be in a position to be positioned in obscurity, with its lid positioned on the side of the stove, suggesting that it is in resemblance to a kitchen sink. The saucepan's surface is cluttered with a variety of items, including a pot, a bowl, and a dish. The lid is positioned slightly above the stove's edge, suggesting a slight movement, indicating that the saucepan is in the position of a stove burner. The kitchen sink appears to have been placed in hazy conditions, suggesting the saucepan may be in the middle of preparing to serve. The surrounding area is a cluttered kitchen, with cluttered counters, counters and other items indicating
- Reference: The tray is situated on the scales, appearing relatively stationary. The tray itself has a clean and shiny surface with an almost reflective quality. It sits flush against the scale's surface, suggesting that it's resting firmly and has not yet been disturbed.

#### Sample 381 — Before

- Similarity: 0.2820
- Prediction: The meat is sliced in a circular motion, indicating it is in the process of being cooked. The meat has a smooth, charred appearance, implying it has been grilled. The skin is a dark brown, revealing a thin layer of meat, a sign of the cooking process. The knife is positioned in squat position, pointing at the meat, suggesting it is preparing to be grilled, presumably to be cooked.
- Reference: The spice jar appears to be in its early stages of application. The jar's cap, equipped with perforated holes for even distribution, is slightly tilted, hinting at the intent to pour. Yet, only a minute amount of spice seems to have been dispersed from the jar, likely just the beginning of the seasoning process. The surrounding area on the dish contains sporadic and minimal specks of the spice, indicating that the seasoning process has just started.

#### Sample 384 — Before

- Similarity: 0.4573
- Prediction: The refrigerator is positioned in a room with a door open, revealing a kitchen area with cluttered shelves, a sink, and a fridge. The door is partially open, suggesting a possible door, indicating a closed position. The refrigerator's interior is cluttered with unused items, including a refrigerator basket, cluttered kitchenware, and the refrigerator'
- Reference: The milk container, a common plastic jug with a handle and a screw-top lid, appears to be in a state of rest, possibly just after being placed down or before being picked up. It stands on the middle shelf of the open refrigerator, surrounded by various other items such as a box of what appears to be cereal, another beverage container, and assorted refrigerated goods. Its location and upright position suggest it was not in immediate use, and there is no sign of disturbance to its contents, which are not visible but presumably are settled due to the lack of motion.

#### Sample 387 — Before

- Similarity: 0.4521
- Prediction: The fabric is a light-colored, smoky fabric with a hazy texture. Its surface is cluttered with stains, indicating that the fabric has been washed. The fabric appears to be a mixture of sand and water, suggesting that the detergent has been soaked. The cloth is positioned in a position that indicates that the liquid has been removed from the fabric, implying that the product has been thoroughly washered. The area is reminiscent of a kitchen, with soiled surfaces and a clean kitchen counter, a sink, and utensils. The surrounding area is also cluttered, suggesting a deliberate use of the detergent.
- Reference: The frame captures a hand-held bottle of degreaser positioned at an angle indicative of it being in the midst of a spraying action. The white trigger is compressed, and a fine mist can be inferred to be emitting from the nozzle, although the actual spray is not visible. The bottle, mostly obscured by the hand, seems to be about half-full, showing that it has been utilized before. The label is partly visible, though the specific branding and instructions are not clear. The bottle is being aimed at an off-white table, presumably targeting an unseen stain or area for cleaning.

#### Sample 392 — Before

- Similarity: 0.4128
- Prediction: The cabinet appears to be in a state of transition, with the door open, revealing a white surface with a dark interior. The interior is cluttered with cluttered items, including a kitchen sink, a microwave, and a small refrigerator. The cabinet's interior is partially uncovered, with bare walls and furniture, suggesting a gradual movement. The door is open, suggesting the person is attempting to open the door. The person's hand is likely a familiar one, with her fingers pointing at the door, suggesting that she is preparing to open it. The surrounding area is a well-lit room, with bright lights and contrasting objects, suggesting an activity. The object's position is reminiscent of a person
- Reference: A tea towel is partially draped over the edge of an open drawer. The towel exhibits a vibrant stripe pattern with bold colors—yellow, pink, blue, green, and white—creating a lively contrast against the wooden tones of the drawer. It appears to be a linen material, given its texture and slight wrinkles, indicative of recent use or hasty storage. The tea towel is positioned such that it could easily slip off the drawer's edge, suggesting that it wasn't placed with long-term storage in mind.

#### Sample 397 — Before

- Similarity: 0.3254
- Prediction: The knife appears to be in a position to be positioned on a counter, indicating that it is in resemblance to a kitchen knife. The blade is positioned in strait-edged position, suggesting that it has been positioned at a certain angle, implying that the knife is in the position of a knife. Its surface is slightly tilted, suggesting a slight movement, and the blade is likely positioned near the edge of the kitchen counter, suggesting the knife may be in the process of being placed. The knife's surface appears to have been slammed against the counter, possibly to the right of the blade, suggesting it may be a slicing tool. The kitchen counter
- Reference: The salt appears to be contained within a typical cylindrical container with a white cap, likely designed with a flip-top for easy pouring or shaking. The container rests among an array of other kitchen items, and the immediate surroundings give no clear indication of any recent interaction or disturbance involving the salt. The placement and orientation of the salt container suggest that it has been set down after use or it's awaiting its turn for inclusion in the culinary process.

#### Sample 401 — Before

- Similarity: 0.4730
- Prediction: The cloth appears to be a white fabric, with a light brown hue, suggesting a person is holding the cloth. The cloth is a dark brown, with an orange or yellowish hue, indicating a hand or hand towel. The fabric is positioned in a position that indicates a slight movement, implying a quick movement. The person's movements are reminiscent of a seated person, with the cloth positioned at the center of the cloth, presumably a part of the person'
- Reference: The floor appears to be a hardwood surface, exhibiting a rich, warm brown hue with a polished finish that reflects a bit of the surrounding light. The planks are arranged in a traditional staggered pattern, which creates a flow across the floor, adding to the sense of space within the room. There are some small debris and dust particles scattered sparsely across the surface, indicating a need for cleaning. The floor's condition is overall tidy, but the presence of these small particles suggests recent foot traffic or activity.

#### Sample 403 — Before

- Similarity: 0.3847
- Prediction: The bread is a white, slender piece of bread, with a thin, slightly curved edge, indicating it is in the process of being prepared. The bread has a smooth, textured surface, with the edges of the bread revealing a sprinkling of cheese, which is indicative of a recent meal. The loaf is positioned in a position that is reminiscent of sliced bread, a type of bread that is typically toasted, and the bread is likely to be a light, moist bread. The parchment paper is bare, with no visible markings or markings, suggesting that the bread has been sliced. The paper is slightly creased, suggesting a slight crease in the bread
- Reference: The onion appears to be in the initial stages of preparation. It is sliced into semi-circular or crescent-shaped pieces, with the pieces neatly arranged on a plate. The thickness of each slice is relatively consistent, suggesting that the onion has been methodically and carefully prepared. Around the plate, other ingredients, such as olives, are visible, implying that the onion might be an integral part of a broader recipe. The vibrant, off-white to pale yellow coloration of the onion slices indicates freshness.

#### Sample 406 — Before

- Similarity: 0.3345
- Prediction: The bin appears to be in a position of a discarded garbage can, indicating that it is in limb or hand motion. The lid is positioned in slats, suggesting that the contents are being thrown away. The bin's interior is cluttered, suggesting a deliberate movement, and the bin'
- Reference: The strainer appears to be held at an angle, capturing the viewer's immediate attention. It contains a vivid, possibly viscous, orange-yellow liquid that seems to be either being poured into or is about to be drained from the strainer. The liquid's bright hue contrasts with the white of the strainer, and there are several distinct streams and drops evident, suggesting a dynamic moment of motion or transition.

#### Sample 410 — Before

- Similarity: 0.2875
- Prediction: The jar is positioned in a kitchen, with a lid positioned at the top, indicating the person is preparing to open the container. The lid is a dark brown, a translucent, opaque container with contrasting markings, suggesting a fresh, unopened jar. The rim is adorned with overlapping, overlapping jar lids, implying the person has opened the jar, allowing the container to be viewed. The container is surrounded by a thin layer of jar material, suggesting the person's intent to open it. The bottle is stacked against the wall, revealing a jar with rounded edges, suggesting that the holder is attempting to open. The person'
- Reference: A partially completed pizza with a base of dough prominently displays a smattering of sweetcorn kernels. These golden nuggets of corn are scattered across the pizza in a casual, seemingly haphazard fashion, dotting the surface with their sunny hues. The sweetcorn appears to have been freshly sprinkled, with some kernels resting atop streaks of tomato sauce, while others find themselves nestled between the creamy white of the dough. There’s a sense of motion, perhaps captured mid-action, as if the sweetcorn has just tumbled from the can and landed in a random array on the pizza.

#### Sample 412 — Before

- Similarity: 0.3142
- Prediction: The chopping board appears to be in a position where it is positioned in sandpaper, with a sprinkling of water on the surface. The water is a clear liquid, indicating that the blade is being soiled. The board is surrounded by a stream of water, suggesting that the water has been drained. The surface of the board is slightly damp, suggesting a gradual process. The hand is pointing at the board, pointing to the water's surface, suggesting it is in pristine condition.
- Reference: The spring onion appears freshly introduced into a kitchen sink area, its roots still intact, suggesting recent procurement, possibly from a garden or market. The onion's white bulbous end displays a healthy sheen, indicative of moisture retention, while the green stalks exhibit a vibrant color, with no visible wilting, indicating freshness. The onion is held at a slight angle, with fingers gripping firmly around the lower green stalks, preparing for a rinse or a cut.

#### Sample 427 — Before

- Similarity: 0.4797
- Prediction: The jar appears to be a plastic container with a lid, indicating that it is in a position to be placed in if it is to be opened. The lid is positioned in oblique position, suggesting that the container is a container of food or other items. The container is partially open, suggesting a possible opening, implying that the contents are in resealable packaging. The rim of the container appears to have been partially opened, suggesting the contents may be in pristine condition. The contents of the jar are positioned on a shelf, suggesting they are in the process of being placed in the container. The surrounding area is cluttered, suggesting there may be lingering debris or debris in the vicinity
- Reference: The refrigerator's top shelf is partially visible, housing a carton of eggs with several eggs missing, suggesting recent use. The middle shelf is empty, indicating either a recent clearing or pending restocking. The lower section, less discernible due to the angle, appears to contain some indistinct items, potentially vegetables. The door is ajar, and the interior light is off, implying that the door has been open for a while or the automatic light function is not active. To the right of the refrigerator, there is a countertop with a coffee machine and a stainless steel pot, indicating the proximity of the kitchen's cooking area.

#### Sample 430 — Before

- Similarity: 0.2554
- Prediction: The slicked meat is positioned in a kitchen, with the meat sliced in contrasting hues, suggesting a smoky texture. The meat is covered in slender, ripe flesh, suggesting it is a meat product. The flesh is charred, suggesting the meat is not fully cooked. The person's hand is presumably preparing to eat, indicating that they are preparing for a meal. The sliced meat is likely a vegetable, implying it is not yet ready for cooking.
- Reference: The plastic bag in question appears to be partially crumpled and compact, resting on the kitchen counter. It is not fully open, suggesting that its contents have not yet been fully removed. The bag's mouth is not stretched wide, indicating that the opening action has either just begun or is about to commence. It has a translucency that allows the inside or the lack of contents to be partially visible, and its thin material has some creases and folds from its previously stored state.

#### Sample 433 — Before

- Similarity: 0.3535
- Prediction: The door appears to be in a position that is partially open, suggesting a gradual movement, suggesting that the door is closed. The door's surface is a dark brown, suggesting it is positioned in descending order, suggesting the door may be closed. It is surrounded by a series of white objects, including a white plate, a glass plate, and a wooden box. The object appears to have been placed in resemblance to the door, suggesting its position is ambiguous. The surrounding area is cluttered, suggesting there is no room for the door to be open.
- Reference: The cloth appears to be partially scrunched in the person's hand, showing signs of having been twisted or wrung out. Its texture looks damp and heavy, suggesting it has absorbed a significant amount of water or another liquid. The cloth's color is not fully discernible due to the motion blur and lighting, but it seems to have a light tone, possibly white or cream. The person's grip on the cloth is firm, as indicated by the tautness on the visible portion, indicating that the squeezing action has just been performed or is about to be initiated.

#### Sample 436 — Before

- Similarity: 0.2449
- Prediction: The kitchen sink appears to be in a state of flux, with a sprinkling of a small amount of soap on the bottom, suggesting that the sink is in resealable condition. The sink's surface is cluttered with sludge, suggesting a recent cleaning process. The kitchen counter is positioned in pristine condition, with the sink'
- Reference: The peeler appears to be in a resting position, nestled comfortably in the grip of a person's hand. The metallic blade, designed to strip away the outer layers of vegetables, reflects the ambient light, hinting at its sharpness and readiness for use. Surrounding the peeler are the evidences of its recent work: small, thin pieces of peel that have been expertly removed from the partially visible eggplant, suggesting a meticulous and careful peeling process. The hand holding the peeler shows a relaxed yet purposeful hold, indicating a brief pause in the action, perhaps as the person assesses their next move.

#### Sample 437 — Before

- Similarity: 0.2608
- Prediction: The sink appears to be in a state of flux, with a sprinkling of water on the surface, suggesting that it is a medium-sized sink. The water is filtered through a funnel, suggesting a gradual process, with the water evaporating from the sink. Its surface is cluttered with sludge, suggesting it may be a liquid or a solid. The sink's surface appears to have been swept away, suggesting the water has been drained. The surrounding area is reminiscent of a kitchen, with kitchen appliances and a sink, suggesting there may be some movement.
- Reference: The pieces of pepper are strewn about on a wooden chopping board. Their fresh, vibrant yellow hue contrasts starkly with the brown backdrop of the board. They appear to be freshly chopped, with a few seeds evident among the pieces, and the wetness of the freshly cut vegetable glistening in the ambient light.

#### Sample 439 — Before

- Similarity: 0.3559
- Prediction: The scrubbing pad appears to be in a position where it is positioned in sweeping motions, indicating that it is currently being washed. The surface of the slat is cluttered with a variety of debris, including a discarded paper towel, a folded towel, and a towel. The holder is a white, reflective object with contrasting hues, suggesting that it has been soiled. The hand is pointing at the holder, pointing to the curved side of the pad, implying that it was sprayed with water. The cloth is soaked with water, suggesting it is still wet. The water is dripping from the nozzle, suggesting the hose is
- Reference: The towel appears to be a standard kitchen towel with a predominantly yellow hue, featuring a red pattern, which suggests a possible decorative or functional design. It is being held by a person whose hand and forearm are visible in the image. The towel is partially crumpled and in motion, which blurs the details of its design and exact shape, as the person seems to be in the process of either picking it up or beginning to use it. The background reveals a typical kitchen countertop with various items scattered around, indicating that cleaning or cooking activities may be taking place.

#### Sample 440 — Before

- Similarity: 0.4947
- Prediction: The butter appears to be a mixture of melted butter and cream, with a thin layer of cream on top, indicating that it has been boiled. The butter is a light brown color, with the edges of the butter indicating a medium-sized amount of butter. The knife's edge is visible, suggesting that the butter has been heated, implying that it is still a bit hot. The blade is positioned slightly downwards, suggesting a slight movement, a sign that the knife is preparing to cut. The texture of the knife'
- Reference: The cheese appears as a solid mass with a creamy white color and is speckled with herbs, indicative of a seasoned spreadable cheese. It retains its shape within the confines of the plastic container, suggesting a firm texture at rest. There is a noticeable sheen on the surface, hinting at a moist consistency. The cheese shows signs of previous scooping, with an uneven surface and stray pieces on the sides of the container. The spoon, positioned to scoop, has yet to disturb the cheese in this frame.

#### Sample 448 — Before

- Similarity: 0.4010
- Prediction: The washing machine is positioned in a dark room, with a white door, a black handle, and a chrome-plated door handle. The door is a rectangular shape, with an oval shape, suggesting a door or window. The machine's interior is cluttered, with its door and counter, and its interior cluttered with items. The surrounding area is occupied by a kitchen, with the kitchen and bathroom being visible. The washing machines are positioned on a flat surface, with no visible objects, and the surrounding area appears to be a single-use laundry room.
- Reference: The coffee machine sits on a kitchen counter, displaying a standby mode, indicated by the lack of illuminated buttons or indicators. Its carafe is absent from the heating plate, suggesting that it has either been removed for cleaning or to serve coffee. A cluster of wires is visible near the machine, with a possible power cord extending towards an electrical outlet. The surrounding area is cluttered with various items, but the machine itself appears clean and in good condition, waiting for interaction to commence its brewing cycle.

#### Sample 456 — Before

- Similarity: 0.4837
- Prediction: The coffee pot is placed in a sink, with a faucet in the middle, a hand-held device indicating the presence of a water source. The water source is positioned in the center of the pot, indicating that the water has been running through the pot. The faucet is aimed downwards, pointing to the water source, implying that the pot is being boiled. The coffeepot is surrounded by a stream of water, suggesting that the tap is a source of water. The person holding the coffee pot, who is presumably a novice, is demonstrating the use of rinsing the pot to remove excess water.
- Reference: The coffee machine is adorned with vibrant blue and gold patterns, presenting an ornate and decorative appearance. Its main body has a curved design, with the base being somewhat cylindrical, leading to an open top. The spout of the machine is not visible, suggesting it's either turned away or the machine doesn't have one. There's a prominently featured label or marking on the front, but the exact details or brand are not discernible.

#### Sample 458 — Before

- Similarity: 0.4890
- Prediction: The pan is positioned in a kitchen sink, with a handle pointing downwards, indicating that it is in the process of being cleaned. The pan's surface is cluttered with scrubbing soap, which is likely a sign of a recent cleaning process. The surface is covered with mud and debris, suggesting that the pan has been soiled. The water level is low, suggesting a gradual movement, implying that the water has been running. The sink's interior is awash with soapy water, suggesting the pan is in resurgence. The kitchen sink is surrounded by a series of white towels, which are positioned on the counter, highlighting the pan'
- Reference: The tap is in an off position, with the lever aligned parallel to the countertop, indicating no water flow. Its metallic surface reflects the ambient light, and no water droplets are visible on or around the spout, further confirming it hasn't been used immediately prior. The tap's position, far from the basin edge, suggests it is designed to accommodate a variety of dish sizes for washing.

#### Sample 459 — Before

- Similarity: 0.3785
- Prediction: The knife appears to be in a position to be positioned in squat position, with its handle positioned slightly outwards, indicating it is in resemblance to a kitchen knife. The blade is angled slightly downwards, suggesting it is positioned at a slight angle, suggesting that it is not yet fully positioned. The knife's surface is cluttered with a variety of other items, including a slat, a bowl, and a plate. The kitchen knife is pinned against the edge of the knife, suggesting a gradual movement, implying a quick movement. The angle of the blade is slightly blurred, suggesting the knife is still in pause mode. The hand is
- Reference: The image reveals a standard-sized, cylindrical can positioned near the edge of a countertop, partially opened with a lid attached. The pull-tab of the can has been engaged and is bent at an angle, indicating the lid has been partially peeled back. The metallic interior surface of the can reflects the ambient light, highlighting the exposed content which appears to be a type of food, possibly a canned fruit or vegetable, showing a glimpse of small, rounded items consistent with peas or corn.

#### Sample 460 — Before

- Similarity: 0.2506
- Prediction: The chicken is placed on a plate, positioned in a kitchen sink, with a small amount of food on the bottom, indicating it has been preparing. The surface is covered with crumbs, a sign of a recent cooking session, and the chicken is positioned on the counter, implying a busy kitchen. The chicken appears to be in resemblance to a chicken breast, with the meat weighing less than a few pounds, suggesting that the cooking process is still underway. The kitchen sink is cluttered with food, with no visible signs of cooking.
- Reference: The image captures a motion-blurred scene where the water tap appears to be at a critical transition point. The blurred state of the hand and the tap suggest a dynamic interaction, with the tap likely in the process of being turned off. The water flow is not clearly visible, indicating either a rapid movement that the camera could not freeze or a very thin stream of water that blends into the surrounding blur. Drops of water can be inferred to be present, possibly splashing or just ceasing to fall, reflecting the hurried action taking place.

#### Sample 463 — Before

- Similarity: 0.4599
- Prediction: The pot appears to be in a position to be positioned in southwestern Asia, with a curved edge, suggesting a gradual movement. The lid is positioned on the stove, indicating that it is in re-entry, suggesting that the pot is still in the process of being placed. The pot's surface is a dark brown, suggesting it may be a pot or pan, suggesting the pot may be in the middle of a cooking session. The surrounding area is cluttered with chopping debris, suggesting there may be some activity taking place. The kitchen appears to have been preparing for the cooking session, suggesting an activity is underway.
- Reference: The switch is not distinctly visible in this particular frame, making it difficult to definitively state its condition. The blurring and motion in the frame suggest that there may have been some rapid movement. The surroundings predominantly feature a kitchen stovetop, a pot, and a hand, which might be reaching towards or away from a possible switch, but the specifics about the switch's position, appearance, or state are obscured.

#### Sample 464 — Before

- Similarity: 0.4603
- Prediction: The sliced kale is a vibrant green, with a bright green hue, indicating it has been steamed. The leaves are arranged in a slender, overlapping pattern, suggesting they are being prepared for cooking. The leafs are positioned in contrasting colors, suggesting that they are preparing for a meal. The knife is angled slightly, suggesting a slight movement, implying the knife is still a bit loose. The blade is positioned slightly downwards, suggesting the knife has been used to prepare the kalasses.
- Reference: The lettuce in this frame appears freshly cut, with pieces ranging in size from larger chunks to finer bits. The varied sizes suggest that the cutting has just started, and the user hasn't yet achieved a consistent chop size. The bright green color of the lettuce indicates its freshness, and some of the edges of the lettuce pieces appear slightly jagged, showing the initial cuts.

#### Sample 468 — Before

- Similarity: 0.4734
- Prediction: The slicer is placed in a water bath, with the water running from the faucet, indicating that it is in the process of being rinsed. The nozzle is positioned in overlapping motions, pointing to the water's direction, implying that the water has been drained. The water is filtered through a small opening in the spout, highlighting the resulting liquid content. The surface of the scourer is a dark, reflective, hazy, revealing a hazey of water, a reflective surface, and a light source. The surrounding water is visible, suggesting that the rinsing process is underway.
- Reference: The bell pepper appears freshly introduced to the stream of water, its vibrant red skin displaying a matte finish with several droplets starting to form on the surface. The droplet pattern is sparse, indicating that the rinsing process has just begun. The pepper is held from the bottom by a hand, with fingers slightly curled around its curves, ensuring a secure grip. The light reflects differently on the dry and wet parts of the pepper, highlighting its plump and firm condition.

#### Sample 470 — Before

- Similarity: 0.4254
- Prediction: The bottle is positioned in a kitchen sink, with its lid positioned on the counter, indicating that it is in the process of being opened. The bottle's interior is cluttered, with a cluttered surface, including a sink, counter, and a counter top. The lid is a white, contrasting color, suggesting that it has been opened.
- Reference: The plug appears to be partially inserted into a power outlet, which is located close to a cluttered area, possibly a kitchen counter, given the presence of various kitchen items and food packages. The outlet itself is standard, likely designed for two-pronged plugs, and the plug is white, contrasting with the cream-colored wall. The person's hands are gloved in yellow, suggesting the maintenance of hygiene or protection from dirt. The plug is captured in the midst of an action, with the person's hands positioned as if they are in the process of gently pulling or manipulating the plug.

#### Sample 473 — Before

- Similarity: 0.4873
- Prediction: The jar appears to be in a kitchen sink, with a handle pointing downwards, indicating it is in the process of being thrown away. The lid is positioned in contrasting hues, suggesting it is being soiled. The rim is a dark brown, with the edge of the jar indicating a recent cleaning. The hand is pointing upwards, with its fingers pointing towards the container, suggesting a thorough cleaning.
- Reference: The bottle appears to be a sturdy plastic container, primarily blue in color with a textured design enhancing grip. Its cap, also blue but of a slightly different shade, is secured tightly to the bottle, which seems to be in the process of being opened by a pair of hands. These hands exhibit a firm grip on the bottle, with the cap still in place, indicating the initial stage of opening. The contents of the bottle are not visible, suggesting it might be opaque, and there's a noticeable absence of any liquid spillage, implying that the bottle is likely full or unopened.

#### Sample 476 — Before

- Similarity: 0.3477
- Prediction: The pizza is a thin, uncooked piece of dough with a light brown color, indicating it has been sprayed with melted butter. The dough is positioned in a circular shape, forming a smooth, textured layer, reminiscent of a pizza crust. The surface of the pizza is slightly uneven, suggesting that the dough may be a bit dry. The pizza's surface is bare, suggesting it may be partially cooled. The blades are positioned on the edge of the dough, suggesting a slight movement, implying the dough is still moist. The texture of the crust is reminiscent a dough that has been baked, resulting in crumbs that appear to be melted and melted. The crust
- Reference: The salt shaker is inverted, with its opening directed towards a mound of shredded cheese on a round flatbread. It's being held by a hand mid-motion, implying that the action of shaking has just begun or is about to begin. The shaker's lid is white, suggesting a contrast with the surrounding ingredients and the warm tones of the kitchen. There's no visible salt coming out yet, indicating this is the initial stage of seasoning. The hand looks to be giving a slight shake, with salt potentially starting to disperse.

#### Sample 477 — Before

- Similarity: 0.2983
- Prediction: The soup appears to be in a simmering state, with a light coating of sauce, indicating that it is still being stirred. The sauce appears to have been boiled, with the liquid clumping around the edges, suggesting that it may be a little too hot. The soup is a medium-sized portion, with an average consistency, suggesting it may have been cooked in saline or a liquid-based state. The surface of the soup appears slightly damp, suggesting the presence of a few grains or lumps. The texture of the sauce appears slightly spongy, suggesting a slight cooking process.
- Reference: The light in this frame emanates a magenta hue, suggesting the early stages of ignition. The intensity is moderate, indicative of the gas burner beginning to engage, with the flame just starting to find its full strength. The light casts a gentle but defined glow on the surrounding area, illuminating the edges of the pot and creating a soft reflection on the cooktop. It is contained primarily under the pot, providing a focused source of heat with minimal diffusion into the surrounding environment.

#### Sample 480 — Before

- Similarity: 0.4630
- Prediction: The spout is positioned in a position that is agitated, with the lid firmly pressed against the surface. The nozzle is angled downwards, indicating a squeezing motion, resulting in slouching. The surface appears to be awash with water, suggesting a waterlogged state. The water is a clear liquid, suggesting that the slurry is dripping from the nozzle. The object is presumably a plastic container, with a handle that is likely to be used to remove the hose or other tools.
- Reference: The liquid washing up is yet to be dispensed from its container, which is being held in a poised position over a sponge. The sponge, appearing dry and ready to absorb, waits to receive the liquid. There is an anticipation in the scene as the liquid remains enclosed in its container, suggesting that the act of dispensing is imminent.

#### Sample 482 — Before

- Similarity: 0.4303
- Prediction: The foil is a thin, opaque piece of paper that is positioned on a plate, indicating it is in the process of being sliced. The foil's surface is bare, with no visible markings or markings, suggesting it is being prepared for cooking. The person's hand is unsure of the contents of the foil, suggesting that it may be a food item. The paper is ripe, with a light brown hue, suggesting the foil is being discarded. The packaging is cluttered with crumbs, which are likely to be discarded, implying the foil may be in the middle of cooking.
- Reference: The packaging, in this frame, is intact with no apparent tampering or alterations. A package of red meat rests on the countertop, untouched and in its original state. Adjacently, there's a package of chicken or some lighter meat. The package has a label attached to it, displaying some information, potentially related to its weight and price, but the exact details cannot be discerned. The plastic seal around both these meat packages is undisturbed, signaling that the items have not been accessed yet.

#### Sample 486 — Before

- Similarity: 0.4224
- Prediction: The glove appears to be a slender, curved, or curved object, with a slight crease in the middle, suggesting it is a medium-sized glove. Its surface is slightly curved and angled, suggesting that it is not a particularly delicate item. The glove's surface appears to have been soaked or soaked, suggesting a gradual process. The gloves are positioned in a position that indicates they are a bit damp, suggesting they are not soaked. The cloth is positioned slightly downwards, suggesting the glove is soaking or soaking, suggesting its texture may be softer than usual. The fabric is pinned to the edge of the glove, suggesting there may be some movement involved. The hand appears
- Reference: The hand in this frame appears to be in motion, with a slightly open palm showing. Some fingers appear slightly bent, hinting at a gentle gripping or holding action. There's a glimpse of a shadowy reflection on the floor, suggesting that the hand might be near an object or surface which is causing this shadow. The overall state of the hand conveys a sense of action or movement, perhaps as part of a larger gesture or task.

#### Sample 489 — Before

- Similarity: 0.4711
- Prediction: The oven is in a dark, dark room, with a white surface, a black handle, and a metal handle. The oven's interior is cluttered, with the door open, indicating a door or window. The door is open, with its handle positioned in oblique motion, suggesting a hand or hand-held device. The interior of the oven is a light brown, with an orange hue, suggesting the oven has been preparing for a meal. The kitchen is occupied, with several items on the counter, including a microwave, oven, and oven.
- Reference: The digital timer is partially obscured by a hand reaching towards it, with fingers extended, indicating an imminent action, such as pressing a button. The display of the timer is not fully visible due to the angle and the position of the hand. However, it's clear that the timer is active as some green lit segments can be discerned, suggesting that the time is being displayed and is likely counting down. The surrounding area is a kitchen setting with a visible oven beneath the timer and household items around.

#### Sample 490 — Before

- Similarity: 0.4528
- Prediction: The packaging is a white, opaque, opaque plastic wrapper with a thin layer of paper on top. The packaging has a sleeve, indicating that it is being prepared to be opened. The person's hand is positioned in the middle of the packaging, presumably preparing to open the wrapper. The package is surrounded by a series of translucent, translucent strips, implying that the contents are being rolled out. The foil is stacked against the packaging's edges, suggesting that the packaging is being opened.
- Reference: The tortilla appears freshly lifted from the stack, held by a hand wearing a checkered shirt, indicating the beginning of an action. It exhibits slight flexing at the edges, a common characteristic of a pliable, room-temperature tortilla. The smooth, pale surface of the tortilla contrasts with the more textured and vibrant packaging from which it was taken, and the surrounding kitchen paraphernalia—like the bag of chips and container of sugar in the background—provides a casual, domestic setting.

#### Sample 491 — Before

- Similarity: 0.3347
- Prediction: The pak choi is positioned in a kitchen, with a thin layer of sliced pak leaves indicating the first step in the process. The leaves are trimmed and trimmed, with the stems pointing towards the camera, suggesting that the pak is being prepared. The leafs are arranged in overlapping rows, indicating that the leaves are being prepared for the next step. The bok choy is a bright green color, with its leaves contrasting with the rest of the sliced greens. The knife is angled slightly, suggesting a curved motion, implying that the knife is being used to cut the bok
- Reference: The coriander appears freshly placed on a wooden cutting board. The stems and leaves are still mostly intact, exhibiting a rich green hue. Some of the leaves are slightly overlapped, and a few of the stems extend outward, hinting that they haven't been worked with yet. The coriander's overall appearance suggests it's in its natural, untouched state on the board, ready to be processed.

#### Sample 494 — Before

- Similarity: 0.3813
- Prediction: The microwave appears to be in a position to be positioned in obscurity, with its lid positioned slightly out of the way, suggesting that it is not yet fully occupied. The interior of the microwave appears slightly cluttered, with a few items visible, including a small dish, a pot, and a microwave-safe bowl. The kitchen is cluttered with cluttered items, including dishes, dishes, and other items, suggesting a recent or recent change in the kitchen. The microwave's interior is a dark, reflective object, suggesting it may be a stove-type appliance, indicating a kitchen setting. The surrounding area is reminiscent of a home, with the kitchen lighting indicating that the microwave is not fully positioned
- Reference: In this frame, the door is almost entirely closed. The door's handle, located on the right side, appears to be in its resting position, suggesting that it hasn't been fully engaged yet. Shadows cast from the door onto the adjacent surfaces indicate that ambient light is coming from the left side of the frame. The door seamlessly blends into the cabinetry, making it difficult to discern any clear boundaries at first glance.

#### Sample 495 — Before

- Similarity: 0.3750
- Prediction: The kitchen towel is positioned on a table, with its handle positioned slightly outwards, indicating it is in the kitchen. The towel's surface is a dark brown, contrasting color, suggesting it is unused. The fabric is patterned, suggesting a light or damp cloth, and the towel'
- Reference: The electrical plug, white in color with two prongs, is securely inserted into a wall socket. The plug's cord extends towards the bottom right corner of the image, indicating that it is under some tension, possibly from the device it is connected to or from the act of being pulled. The wall socket is situated close to the corner of two walls meeting, and the plug itself is partially obscured by a wooden chair leg, hinting at a domestic setting. The flooring is tiled in a warm yellow hue, and the skirting is white, matching the plug and socket.

#### Sample 498 — Before

- Similarity: 0.3317
- Prediction: The microwave is in a dark, cluttered state, with a white surface, indicating it is not yet fully operational. The microwave's interior is cluttered, with its lid positioned in oblique position, suggesting that the microwave is not fully operational, suggesting a possible attempt to open the microwave. The kitchen is occupied with utensils, including a kitchen sink, a microwave oven, and a dish. The surrounding area is a room with cluttered furniture, including the kitchen counter, displaying a variety of kitchen items, including dishes, dishes, and kitchenware. The lighting is dim, with the ambient light indicating a low-light setting.
- Reference: The milk bottle is a transparent, plastic jug with a white handle and cap, indicative of a standard milk container one might find in a supermarket. It's placed on its side, with the handle facing upwards, suggesting it has been casually laid down rather than carefully positioned. The cap appears to be securely fastened, and there's no visible distortion of the bottle's shape, indicating that the bottle has not been squeezed or otherwise manipulated. It rests near the edge of the countertop, surrounded by various kitchen appliances and items, including a toaster, a kettle, and an empty mug, hinting at a domestic setting perhaps in the midst of preparing a meal or a drink.

#### Sample 5 — During

- Similarity: 0.3927
- Prediction: In this frame, the kitchen counter is now more visible, with a more cluttered appearance. The counter's surface is now a bit more bare, with the counter'd space revealing a slightly darker hue. The kitchen counter'remarks are still visible, but the counter is still a little more noticeable. The countertop's color is now slightly more vibrant, with white highlights and a slight contrast to the counter. The white counter top is now visible, indicating a cluttered kitchen counter.
- Reference: The floor appears to remain consistently colored with the same mustard-yellow tiles, but the angle of the shot reveals more of the tile area. Additional small debris and smudges are present, and a damp streak is now visible, likely from the wiping motion. The streak has a darker shade than the rest of the floor, indicating that the floor may have been somewhat dirty before being wiped, and the wetness is bringing out the contrast in the tile's coloration.

#### Sample 7 — During

- Similarity: 0.4762
- Prediction: In this frame, the bin's lid is now more visible, with a slightly raised hand, suggesting a more gradual movement. The lid's position remains unchanged, with the lid still firmly attached to the bin, indicating that the action is ongoing. The bin'd lid remains in the same position, with its lid still slightly lowered, suggesting that the lid is still in the position of its original position. The surrounding environment is more cluttered, with less clutter and a less noticeable presence of the bin.
- Reference: The jar is now in motion, caught mid-air with its label oriented towards the camera. Its trajectory appears to be downwards, indicating it has been dropped. The lid remains firmly affixed, and no contents are visible escaping from the jar. The blurred background due to the motion suggests a rapid descent. The person’s foot and the striped sock are prominent in the frame, possibly the inadvertent catalysts for the jar’s sudden journey towards the floor.

#### Sample 8 — During

- Similarity: 0.4241
- Prediction: In this frame, the hand is positioned on the top of the machine, a position that is likely to be a part of the process of preparing the food. The hand's grip is slightly more firm, suggesting that the hand has been adjusting the settings on the machine. The surrounding area is still a little blurry, with the surrounding area indicating that the machine is still in its initial stages of preparation. The person's hand is still holding the button, which is a key component of the device's function.
- Reference: The same toaster now displays subtle differences. The lever has been slightly pushed downwards, but not entirely, hinting at the beginning of the toasting process. The slots still appear vacant, and there isn't any visible toasted bread. However, there's a soft glow starting to emanate from the slots, suggesting that the heating elements are beginning to activate. The power indicator light has a dim glow, further affirming the initial stages of the toasting process.

#### Sample 9 — During

- Similarity: 0.4954
- Prediction: In this scene, the tomato has been sliced into smaller pieces, revealing a more slicked appearance. The knife's edge is now positioned in the center of the tomato, indicating the cutting action, implying the knife'd action. The tomato's flesh is now more rounded, demonstrating the ripeness of the skin. The skin is now slightly spongy, suggesting a sprinkling of the flesh. The hand's motion is indicating a slight movement, a sign of the cutting process.
- Reference: The pepper has been partially sliced open. A portion of the pepper's insides, including its seeds and white pith, are now exposed. The cut appears clean, with the knife currently positioned at the top, near the stem, ready to continue the slicing. The red skin of the pepper contrasts starkly with the pale insides, and the once whole vegetable now has an opened flap, revealing its inner contents.

#### Sample 12 — During

- Similarity: 0.4027
- Prediction: In this frame, the bin's lid is now slightly more open, suggesting that the lid is partially closed. The lid's position remains unchanged, suggesting a gradual movement, indicating that the bin is still in its current position. The bin'd lid remains in its original position, presumably a discarded item, but the lid remains firmly attached to the bin.
- Reference: The basket's opening seems slightly wider in this frame as compared to the previous, hinting at some movement. The basket's content remains elusive, and its surroundings look similar to the previous frame with the patterned textile or rug in proximity. Parts of the person's legs and feet are visible, clad in flip-flops. The floor tiles continue to suggest an indoor environment.

#### Sample 15 — During

- Similarity: 0.4512
- Prediction: In this frame, the pot is now positioned in a more streamlined position, with the lid still firmly attached to the pot. The hand is now holding the pot, indicating that the lid is being pressed. The lid is now slightly tilted, revealing a slight movement in the process of removing the lid. The pot's surface is now more exposed, implying that the pot has been pushed back into the pot'rs container. The jar's contents are now more visible, demonstrating the presence of the lid and the jar itself.
- Reference: The stock, now in a different container, displays a more disturbed surface, likely from recent agitation. Condensation is evident on the inside surface of the pot's lid, suggesting that the stock has been heated for some time and has reached a simmering or boiling state. Some small particles or residues can be observed near the center of the pot, possibly remnants of the ingredients used to flavor the broth. The overall color of the stock remains consistent, maintaining its pale yellow hue.

#### Sample 20 — During

- Similarity: 0.4728
- Prediction: In this frame, the paper is now more firmly held, with the hands positioned in a more slender position. The paper's surface is more exposed, with a creased edge indicating a deeper layer of paper. The hand's movements are more deliberate, indicating that the paper has been pressed into the paper.
- Reference: In this frame, the action has progressed, with the hand now holding a yogurt container mid-air, suggesting movement. The container appears to have been recently moved, as indicated by its orientation and the slight blur conveying motion. The backdrop remains consistent with the kitchen setting, and the previously mentioned items remain static, reinforcing that the yogurt's movement is the focal point of the activity. The hand's grip is firm, suggesting purpose in the movement of the yogurt container.

#### Sample 21 — During

- Similarity: 0.3297
- Prediction: In this frame, the rinsing action is more streamlined, with the water flowing more smoothly. The water's movement is more consistent, with a more gentle hand being held over the liander, indicating that the sand has been thoroughly rinsed. The leaves are now more firmly held, with more of the water circulating around the florets. The hands are more engaged in the process, demonstrating the resemblance of a hand washing the weeds.
- Reference: The leaf is now being held up, allowing for a clearer view of its size and shape. It exhibits a shiny appearance, indicative of the moisture it has just been subjected to. The leaf's stem or base, which is slightly paler than the rest of the leaf, appears firm and unblemished. The main vein running through the middle of the leaf is prominently visible, leading to the numerous smaller veins branching out.

#### Sample 22 — During

- Similarity: 0.3945
- Prediction: In this scene, the meat is now being sliced into smaller pieces, indicating that the meat has been partially removed from the skin. The skin is now more exposed to the knife's action, implying that the knife has been a bit more firmly held. The knife'd edge is now slightly angled, suggesting that the skin has been removed from its surface. The meat is still firmly attached to the skin, demonstrating the slight movement of the knife.
- Reference: In this moment, the garlic press is engaged more fully. The hands of the user have brought the handles closer together compared to the previous frame, applying pressure to crush the garlic clove inside. There is visible strain in the hand muscles, evidenced by the tighter grip on the handles. The chamber where the garlic resides is obscured from view, but the action implies that the garlic is being pressed through the holes, though no garlic is yet emerging. The positioning of the press over the pan remains unchanged, signaling readiness to deposit the garlic directly into the waiting dish.

#### Sample 28 — During

- Similarity: 0.3474
- Prediction: In this frame, the hand is more firmly held, indicating that the hand has been agitated. The hand is now more agitating, implying that the person is holding the tray. The surface of the tray is now slightly more exposed, revealing a more rounded appearance. The person's hand is still positioned in the middle of the table, presumably a hand holding the plate. The table's surface is now a bit more exposed and a little more exposed. The hands are now more engaged, demonstrating a heightened focus on the plate's contents.
- Reference: In this moment, the paper is captured mid-tear, exhibiting a jagged, uneven line running down from the top edge where the tear has begun. The person's right hand continues to secure the top portion of the paper, while the left hand has begun to pull away the bottom segment, creating a clear division. The tear is not straight, indicating that the force applied by the hands is uneven or that the paper's resistance is causing a non-linear rip. The brightness of the light on the paper accentuates the texture of the torn edge.

#### Sample 29 — During

- Similarity: 0.4792
- Prediction: In this frame, the scrubbing brush is now held in the hand, indicating that the water has been sprayed on the surface of the nozzle. The hand's movements are more controlled, allowing the hose to be more focused on the rim of the brush, which is likely a reflection of the water's action. The spout's surface appears to be soiled, suggesting that the rinsing action is underway. The water'd particles are a little more concentrated, suggesting a more thorough cleaning of the surface.
- Reference: The plate now appears to be held level under the tap, with the flow of water striking it more directly from above as opposed to an angle. The pattern on the plate is more clearly visible, confirming that it is indeed decorative and not just a trick of the light. Fewer soap bubbles are present on the plate, suggesting that the rinsing action of the water is effectively removing the soapy residue. The positioning of the plate under the tap allows for a more even distribution of water across its surface, potentially signaling a final rinse to ensure all soap has been cleared away.

#### Sample 30 — During

- Similarity: 0.4697
- Prediction: In this frame, the steamed broccoli is now in a more streamlined state, with the bowl now being held in the hand, indicating that the water has been drained. The water's surface is now more soiled, with a sprinkling of white and yellow particles forming a layer of scalding debris. The person's hand is now positioned in the center of the rinsing basket, presumably a source of fresh air. The swisher's grip is now slightly more firm, allowing the boiled broccoli to remain more firmly held. The broccoli's color is more vibrant, with yellow and green hues contrasting with the surrounding water.
- Reference: The colander is now tilted slightly to the side, causing some of the rice grains to shift towards the edge closest to the sink. This change in angle suggests that the person is beginning to shake or tap the colander to encourage excess water to drain from the rice. The hand gripping the colander has adjusted to accommodate the tilt, and the rice appears less clumped, with individual grains becoming more discernible as they spread out due to the movement.

#### Sample 31 — During

- Similarity: 0.3693
- Prediction: In this frame, the cleaning solution is now more visible, with a more pronounced streak of white residue. The person's hand is now positioned in the center of the cleaning cloth, indicating that the cleaning agent has been wiped away. The surface of the cloth is now slightly more cluttered, with the crumbs and other debris lingering on the surface. The hand's position is more hazy, with more of the grit indicating a scrubbing action. The cloth's surface is now less visible, revealing a slightly more reflective appearance.
- Reference: In this instance, the glass maintains its upside-down orientation, but there is a noticeable shift in its position on the tabletop. The person's hand is in motion, with fingers and thumb appropriately placed to apply force to the glass's base. The movement suggests a slide across the wooden surface, as evidenced by the change in the light reflection pattern on the glass's base, which now has a slightly blurred appearance due to the motion.

#### Sample 32 — During

- Similarity: 0.3708
- Prediction: In this frame, the lid is now positioned in a more streamlined position, with the lid's shape indicating the movement of the hand. The hand's movements are more pronounced, suggesting that the hand is holding the lid, rather than removing it. The lid'd shape is more rounded, suggesting a gradual movement, and the lid remains in place. The person's hand is more likely to be holding the container, which is likely to contain a large amount of food or other items.
- Reference: The lettuce is in the process of being unveiled; the plastic wrap has been partially removed, revealing the top of the lettuce head. The leaves at the crown appear slightly more relaxed than before, likely due to the removal of the constraining wrap. The green hue of the leaves is consistent, displaying no signs of wilting or discoloration, which emphasizes the freshness of the produce. The person handling the lettuce has initiated the unwrapping from the top, peeling the plastic down and away from the lettuce, indicating a preparation to use the lettuce imminently.

#### Sample 33 — During

- Similarity: 0.4545
- Prediction: In this frame, the sink is now in a more natural state, with the lid still slightly tilted, suggesting a gradual movement. The kitchen's lighting is now more dim, with a focus on the kitchen counter and the kitchen sink, which is now positioned in contrasting shades. The sink's surface is now slightly blurred, suggesting that the sink has been agitated, indicating that the water has been removed from the sink. The surrounding area is now less visible, with only a few items visible, such as the sink'r handles and the sink sink're still visible.
- Reference: The cabinet door is now open wider than in the previous frame, revealing more of its contents. The lower shelf still displays the orderly arrangement of cans, and now, the upper shelf's contents become partially visible, featuring what appears to be a row of upright standing bottles or jars. The arrangement suggests a systematic approach to organizing the items by size or type. The cabinet's interior is bathed in the ambient light of the room, which casts soft shadows and gives a homely atmosphere to the kitchen storage space.

#### Sample 36 — During

- Similarity: 0.4098
- Prediction: In this frame, the olives are now positioned in a more pristine state, with the skin still firmly attached to the surface. The hand is now pointing at the olive, indicating that the knife has been inserted into the olive. The olive's surface is now slightly creased, suggesting that the blade is positioned slightly more close to the edge of the olive and allowing the knife to move more easily. The knife's edge is now visible, revealing a slight crease in the olive'straight portion. The palm of the hand is still pointing towards the olive; the knife'scoring is now evident. The blade's position is now more apparent, implying that the olive has been placed in res
- Reference: The scene is largely unchanged with the same blue-lidded butter tub in view. However, there's a subtle shift in the positioning of the hands and the butter knife. The right hand still grips the knife, now slightly repositioned, suggesting movement. The butter tub remains closed, and there is no additional evidence of the contents being disturbed. The anticipation of the spread's use is still present, reflected in the slight adjustment of the hands, preparing for the opening of the tub.

#### Sample 41 — During

- Similarity: 0.3428
- Prediction: In this frame, the microwave door is now positioned in a more streamlined position, with the lid still firmly closed. The hand is now more pronounced, indicating that the door is open, a sign of progress. The kitchen's interior remains unchanged, with a kitchen counter and counter top reminiscent of the previous frame. The door's position remains unchanged and the surrounding area is still visible, implying that the microwave has been opened. The surrounding area remains unchanged as well, with only the door and counter area visible.
- Reference: Here, the milk bottle appears more prominently in the foreground, its label more visible, confirming its identity as a household dairy product. The red cap now seems more defined and appears to be partially twisted open, indicating recent or imminent use. The angle of the bottle suggests that it has been nudged or moved, possibly by the person whose hands are in view. The surrounding area remains cluttered, with kitchen utensils and containers in close proximity to the bottle, further emphasizing the dynamic nature of this domestic scene.

#### Sample 43 — During

- Similarity: 0.3897
- Prediction: In this frame, the coffee grounds are now more agitated, with the water sprinkling onto the surface of the coffee. The cup's surface is now more exposed, with a more rounded shape, indicating that the water has been drained. The coffee grounds have been agitating, with some of the liquid still forming a smooth, frothy texture. The hand's motion is more pronounced, implying that the coffee has been stirred. The mug's contents are now less agitative, with less water displacing the coffee's slurry.
- Reference: In this scene, the sugar jar has been grasped by a hand, suggesting an intent to use it. The lid remains closed, but the jar has been relocated slightly to the right, closer to the center of the counter, and it now sits directly beside a plate that holds a teabag. The hand that holds the jar is partially obscuring it, with the thumb positioned near the flip-top lid, possibly poised to open it. The surrounding items remain unchanged, maintaining the casual disarray of a lived-in space.

#### Sample 46 — During

- Similarity: 0.4741
- Prediction: In this frame, the utensil is now in a more streamlined position, with the handle positioned slightly more vertically, indicating a deeper cleaning. The hand is now more firmly held, allowing the scrubbing to continue, ensuring that the rinsing action is more effective. The utilities are still visible, with a sprinkling of soapy water on the surface of the urn, a sign of the ongoing process.
- Reference: Here, the scissors are seen in a more active state of being cleaned. One blade is covered with white, foamy suds, indicating the presence of soap or detergent. The other blade remains visible and gleams even more prominently, possibly due to the cleaning. The hands grip the scissors in a manner suggesting that they are being scrubbed or brushed, and there's a clear intention to thoroughly clean the instrument.

#### Sample 51 — During

- Similarity: 0.3678
- Prediction: In this frame, the bin is now in a more upright position, with the lid still slightly tilted, suggesting a slight movement. The lid's position is more apparent, suggesting that the bin has been partially opened. The bin's contents are still visible, with a few items still visible. The surrounding environment is more cluttered, with no visible objects or clutter. The object's surroundings are more streamlined, with only a handful of items visible.
- Reference: In this frame, the filter is now fully exposed, held aloft between the person's hands. The debris that was hinted at in the previous frame is now clearly visible, showing a collection of dust, lint, and possibly pet hair clumped together along the folds of the filter's mesh. This accumulation signifies that the filter has been actively filtering out these particles from the environment. The color contrast between the collected dirt and the original white of the filter accentuates the filter's need for cleaning or replacement. The fingers of the person handling the filter are splayed, indicating a gentle yet firm grip, likely to avoid damaging the filter or spilling the trapped debris.

#### Sample 57 — During

- Similarity: 0.3908
- Prediction: In this frame, the pot is now in a more natural state, with the lid still firmly closed. The person's hand is now more likely to be holding the pot, indicating that the water has been boiled. The pot's surface remains slightly damp, with a slight smudge of water on the bottom of the pot. The lid remains open, with no visible movement, and the pot'rsel's edge is still visible. The kitchen counter is now positioned in contrasting contrast with the sink, revealing a cluttered kitchen area. The sink's counter-top is now slightly elevated, implying that the pot has been placed in recirculation mode. The hand's movements are more pronounced
- Reference: In this view, the filter is captured mid-removal, slightly lifted from the coffee maker's well. The moist coffee grounds cling together, exhibiting the filter's effectiveness in maintaining the grounds' mass without spillage. The filter shows a slight deformation, likely from the weight of the wet grounds, and the hand's grip has tightened, causing the filter edges to crinkle. The positioning of the hand suggests the intention to dispose of the contents, as it is held away from the body to prevent spillage on clothing.

#### Sample 60 — During

- Similarity: 0.4142
- Prediction: In this frame, the scrubbing brush is now held in a more controlled position, indicating that the water has been drained. The hand is now holding the rinsing spoon, presumably a holder, to ensure that the wring remains clean. The water's surface is now more agitated, allowing the nozzle to move more quickly, resulting in fewer bubbles. The risins are now more concentrated, forming a tighter, more rounded shape.
- Reference: In this scene, the coffee pot is again within the sink, but now, the user is directly interacting with the lid mechanism. The hand grips the lid, which is angled slightly open, likely to rinse or wash its interior components. Water, along with some frothy soap suds, remains on the exterior surface of the pot. The pot's spout is directed downward, indicating that any residual liquid inside might be draining out.

#### Sample 61 — During

- Similarity: 0.4280
- Prediction: In this frame, the table is now more firmly held, with the hand motion indicating that the table has been moved. The hand motion is more evident, indicating the hand is moving, a gesture that indicates the table's position. The table'd surface is now slightly more exposed, with a more rounded appearance. The surface of the table appears to be a bit more ragged, suggesting that the hand action is more deliberate. The creases and folds are more prominent, suggesting a slight movement in the direction of the hand movement.
- Reference: The crumb has undergone a subtle but noticeable shift; it now appears slightly displaced from its original position, indicating the initial stages of being swept by the vacuum cleaner's suction. The change in lighting around it suggests movement, with a slight blur to its edges caused by the motion of the tablecloth or the disturbance in the air from the vacuum. There's a sense of dynamic transition, as the crumb is caught in the moment between stillness and being vacuumed away.

#### Sample 62 — During

- Similarity: 0.3537
- Prediction: In this frame, the flour has been agitated, with the consistency of the dough becoming more uniform. The hand's motion is more pronounced, indicating that the flour is being stirred. The dough is now more dense, with a more uniform texture. The consistency of its texture is more consistent, with some of the flour still being incorporated into the dough.
- Reference: The olive oil bottle is now in a more pronounced tilted position, and the cap has been removed, revealing the dark opening at the top ready for dispensing the oil. The hand's grip on the bottle appears firm, suggesting a deliberate action is about to take place. However, there's no visible stream of oil yet, indicating the pouring has not started. The anticipation of the oil being added to the contents of the bowl builds as the hand positions the bottle directly above the bowl's rim, preparing to combine the liquid with the other ingredients.

#### Sample 63 — During

- Similarity: 0.2916
- Prediction: In this frame, the tomato has been sprayed with a light coating of olive oil, indicating that it has been thoroughly soaked. The tomato's surface is slightly damp, suggesting that the oil has been added to the tomato'd surface. The hand motion is more pronounced, implying that the tomato is being sprinkled onto the plate. The palm of the hand is now positioned in the center of the tomato, presumably a squeezing motion.
- Reference: The contents of the bowl show signs of being mixed, as the egg's yolk now presents a disrupted surface, with strands of the albumen beginning to blend into the yolk. The pepper specks are more widely distributed, some sinking into the depths of the egg mixture, while others cling to the emerging strands of egg white. The fork's position has changed, implying it has been used to stir the ingredients together, but the mixture remains only partially combined with clear distinctions between the yolk and the whites still visible.

#### Sample 74 — During

- Similarity: 0.3672
- Prediction: In this frame, the spoon is now more firmly held, indicating that the hand is moving. The spoon's surface is now slightly more rounded, suggesting that the spoon has been a bit more agitated. The hand's movements are more pronounced, suggesting a more gradual movement, implying that the knife has been more engaged. The surface of the spoon appears to be more sloppy, suggesting the spoon may have been agitating the spoon, resulting in a clump of food particles.
- Reference: The scale has been moved closer to the center of the countertop, and it is now directly adjacent to the bowl containing the flour. It is still turned off, with no numerical display visible, which implies that it has not yet been used for weighing. Its position relative to the bowl suggests preparation for measuring ingredients, as it is now in a more convenient location for the person to transfer contents into the bowl. The surrounding kitchenware and ingredients remain unchanged, maintaining the scene of an active kitchen environment.

#### Sample 77 — During

- Similarity: 0.4335
- Prediction: In this frame, the button has been pushed downwards, indicating that it is being pressed. The hand is now positioned in the center of the button, a position that is more apparent in the context of the action. The button's surface is slightly curved, suggesting that the hand is pressed downwards. The fingernail's position is slightly altered, suggesting a slight movement. The surrounding environment is still reminiscent of a slick coffee machine, with the surrounding environment indicating a steady hand movement.
- Reference: The milk container's lid has been slightly loosened in this frame. The hand's grip on the container has tightened, indicating a deliberate action to open it. There's a slight tilt to the container, suggesting the user might be trying to pour or check the contents inside. However, the lid is not entirely off, and no milk has been dispensed yet.

#### Sample 83 — During

- Similarity: 0.3719
- Prediction: In this frame, the lid has been removed from the container, indicating that the contents have been removed. The lid is now positioned in a more streamlined position, implying that the lid is being removed. It is now more visible, with the lid firmly pressed against the side of the container. The contents of the lid are now visible, a sign of the presence of the contents.
- Reference: In this snapshot, the jar of pesto has been opened, and its rich, verdant contents are more exposed to the viewer. The cap has been removed, revealing a full jar with pesto filled almost to the brim. The texture appears thick and consistent, with specks of ingredients like basil, garlic, and pine nuts scattered uniformly throughout. A spoon or some instrument has been inserted into the pesto, possibly taking out or stirring the contents.

#### Sample 84 — During

- Similarity: 0.4338
- Prediction: In this frame, the microwave oven is now more visible, with a slightly raised hand pointing at the microwave. The person's hand is more firmly grasping the microwave, indicating that the microwave has been placed in a position where it is likely to be inserted. The kitchen's lighting is still dim, with the kitchen'd lighting still visible. The microwave's interior remains unchanged, with its interior cluttered with clutter and clutter. The hand's motion is more apparent, suggesting that the person is attempting to open the microwave door.
- Reference: The hand has withdrawn from the socket area, suggesting that the toaster has been activated. There are no visible changes to the toaster's external appearance, as the mechanical action of starting the toasting process is internal. The kitchen counter remains unchanged, and the toaster maintains its polished metallic sheen. The cable runs from the back of the toaster and is plugged into the same double socket as before, indicating continuity in the scene.

#### Sample 86 — During

- Similarity: 0.3977
- Prediction: In this frame, the bag is now in a more streamlined state, with the handle still slightly angled, suggesting a hand's movement. The bag's contents are now more visible, with a rounded edge and a slight crease in the middle of the bag, indicating a tight grip. The hand'd motion is more evident, implying a grasping motion, a shift in the direction of the hand'reaction.
- Reference: In this snapshot, the leek is in the midst of a dynamic, albeit unintended, journey as it descends towards the floor. The white end, previously pointing downwards, now inclines towards the camera, hinting at a flipping motion. The plastic wrap has loosened in places, a testament to the forces at play, and the leek's green tops appear more splayed, no longer neatly aligned due to the movement. The blurring of its edges suggests a swift motion, further highlighting the unexpected descent.

#### Sample 89 — During

- Similarity: 0.3037
- Prediction: In this frame, the light source is now more visible, indicating that the door has been opened. The light source's position remains unchanged, suggesting that the light is still visible. The door's angle is slightly different from the previous frame, suggesting a gradual change in the lighting angle. The lighting is now reflected in the light, implying that the lighting is more intense. The shadows are more noticeable, suggesting the light has been absorbed into the light. The surrounding area is now less visible, suggesting an underlying light source.
- Reference: The container appears to be at a slightly different angle, giving an impression of being either moved or possibly tilted. It continues to reveal its label, with the blue and green graphics more prominent in this frame. The white cap remains off, placed close to the base of the container. Nearby objects and the counter’s surface indicate that the location remains consistent with the previous frame.

#### Sample 90 — During

- Similarity: 0.4704
- Prediction: In this frame, the sliced avocado is now in a more slicked position, indicating that the knife has been inserted into the avocado. The avocado's skin is now more exposed, revealing a smoky appearance. The hand's motion is more deliberate, implying that the avocado has been cut in half. The knife's grip is more firm, demonstrating the sprightly motion of the hand. The rind remains intact, displaying a smooth, ripe appearance.
- Reference: Here, the pepper appears more prominently in the foreground, having been repositioned and partially sliced into segments. It rests with the interior facing upwards, revealing a pale inner flesh, ridged with white membranes that cradle a cluster of seeds at the stem end. The slices are clean and the pepper's structure remains intact, though it is now open and exposed, with the previously concealed interior now in view.

#### Sample 91 — During

- Similarity: 0.3677
- Prediction: In this frame, the scrubbing brush is now held in a more streamlined position, with the handle positioned slightly more vertically. The water's movement is more pronounced, with a slight shift in the direction of the stroke, indicating that the brush is being rinsed. The squeezing motion is more consistent, with more water dripping onto the surface of the brush, resulting in fewer streaks. The brush's surface appears to be a bit damper, with less water sprinkling on the surface. The hand's grip is more relaxed, with its angle slightly angled, allowing the brush to move more easily. The bristles of the ricotta are
- Reference: The burner cap is now being held securely in the grasp of a person's hands under a running faucet, positioned in the right side of the sink. Water flows directly onto the cap, cascading over its curves and edges. The person's fingers are manipulating the cap, likely applying pressure to dislodge stubborn residue. The proximity to the faucet suggests a more targeted and forceful cleaning approach, aiming to restore the cap's condition with a thorough rinse.

#### Sample 92 — During

- Similarity: 0.4700
- Prediction: In this frame, the sink is now more visible, with a more streamlined appearance. The hand is now positioned in a slightly more slender position, indicating that the water has been drained. The water level is now slightly higher, suggesting that the sink has been cleaned. The sink's surface is now less noticeable, suggesting a gradual movement. The surrounding area is still cluttered, with the sink'r surface indicating a clean surface.
- Reference: The plate now appears in a different orientation, held by a hand wearing a silver watch, suggesting a right-handed individual. It is captured at an angle that exposes its circular form and the slightly upturned edge. The plate’s underside is more visible, revealing a manufacturer's stamp and a ring of unglazed porcelain where the plate would sit during firing. Droplets of water are scattered across the surface, hinting at a recent wash. The fingers are curled around the edge, gripping it securely, and there’s a dynamic tension as if the plate is being moved purposefully.

#### Sample 96 — During

- Similarity: 0.4722
- Prediction: In this frame, the person is attempting to remove the lid from the pan, a process that has been completed. The person's hand is now more firmly grasping the lid, indicating that the knife has been inserted into the pan. The lid is now slightly positioned, implying that the person has been holding the lid. The hand's grip is still firmly gripped, presumably to prevent the knife from slipping. The container's contents are now more readily visible, demonstrating the presence of the knife's handle.
- Reference: In this moment, the person has partially peeled back the top layer of the plastic seal, starting the process of opening. The opening is at the initial stage, with just the corner of the packaging being lifted. The seal's detachment is most noticeable at the top left corner where the individual's fingers are pulling the material away, revealing a glimpse of the salmon's surface beneath. The packaging still retains its original shape, but the airtight seal has been compromised.

#### Sample 97 — During

- Similarity: 0.3450
- Prediction: In this frame, the box is now in a more streamlined state, with the hands positioned in varying directions. The person's hand is more pronounced, indicating that the box has been opened. The box's contents are more visible, with a rounded edge and a slight movement. The packaging is still in its original state, but the contents are still visible. The hand's movements are more reliant on the action, implying that the person is holding the box.
- Reference: In this moment, the cereal is in the process of being poured. A stream of small, flaky, tan-colored cereal pieces cascades from the bag into a bowl held below with the same hand that was holding the bag open in the previous frame. The flow of the cereal is steady, indicating that the bag has been tilted sufficiently to allow the contents to exit freely. The flakes catch the light as they fall, suggesting a light, crispy texture, and they accumulate in the bowl, already containing a modest amount of cereal.

#### Sample 99 — During

- Similarity: 0.4252
- Prediction: In this frame, the hand is more firmly engaged, indicating that the cleaning solution has been sprayed. The surface of the cloth is now more cluttered, revealing a more pronounced pattern of crumbs and crumbs. The hand's position is more apparent, implying that the person is attempting to clean the cloth. The cloth's surface is now a bit more ragged, suggesting that the cloth has been washed away. The person's hand is now less visible, presumably a hand with a clean hand, pointing to the cloth's surface.
- Reference: In this frame, the wooden table's grain is still visible, albeit slightly blurred due to movement. The same objects from the previous frame remain, but they are viewed from a slightly different angle. The hand of a person can be seen, grasping a blue cloth or piece of paper. The shadows and reflections on the table change slightly, consistent with the movement that's happening in the scene.

#### Sample 100 — During

- Similarity: 0.4693
- Prediction: In this frame, the door is a bit more open, suggesting a more gradual movement, with the door still partially closed. The door's position is more pronounced, suggesting that the door has been opened. The kitchen's lighting is more dim, suggesting the kitchen is preparing for a meal or other activity. The surrounding environment is more neutral, with a light source and a brighter, more reflective surface. The interior of the cabinet is more open and spacious, indicating a greater focus on the kitchen.
- Reference: In this image, the environment has transitioned into a state of semi-darkness, with the light source significantly reduced. The glow that previously brightened the entire room is now subdued, with shadows beginning to dominate the space. The reflective surfaces that once gleamed under the light now present muted reflections, and the overall visibility in the room has decreased. It appears as though the light source is in the process of being extinguished, capturing the room in an intermediate stage between light and dark.

#### Sample 105 — During

- Similarity: 0.4719
- Prediction: In this frame, the spout is now more agitated, with the water dripping from the faucet eroding the surface of the bowl. The hand's movements are more deliberate, indicating that the water has been drained, resulting in a more concentrated stream of water. The water's consistency is more uniform, suggesting that the rinsing action is more sporacious. The spongy surface of its surface is more visible, implying that the bowl is being dragged or soiled. The person's gesture is more deliberate and reflects the presence of the wringing spoon, which is positioned in the center of the basin.
- Reference: The saucepan is now being held by a person's hand, with the handle gripped firmly. It's tilted over the sink, allowing the excess liquid to drain away. A small amount of steam can be observed rising from the pan, suggesting that the contents are still hot. The pasta within looks compacted due to the angle of the pan, and it's clear that it's being held in this position to let the water escape through a colander or lid that's being used to retain the pasta.

#### Sample 109 — During

- Similarity: 0.4710
- Prediction: In this frame, the hand is now more firmly held, indicating that the hand has been agitated. The hand is more agitating, implying that the hands are agitation or a squeezing motion. The hands are now more engaged, demonstrating a more deliberate motion, a gesture that may have been a part of the action. The person's posture is more relaxed, suggesting that the action is more deliberate. The kitchen counter is now positioned in a slightly different position, presumably a place to place the food or other items. The counter's surface is now slightly more exposed, suggesting a different angle of movement. The table's lighting is now dim, suggesting the presence of a light
- Reference: The yellow rubber glove has now been donned by a hand, partially visible in the frame. This active position suggests an ongoing or imminent cleaning task. The fingers are spread apart, with the thumb extended away from the fingers, indicating a grip or movement. The glove is positioned over a bowl submerged in the sink, surrounded by suds, which implies a dishwashing process. The change from being placed on the cutting board to being worn signals a transition from preparation to action in kitchen chores.

#### Sample 110 — During

- Similarity: 0.3915
- Prediction: In this frame, the hand is more firmly held, indicating that the hand has been positioned. The hand is now more affixed to the surface, implying that the person is holding the hand. The hands are still in the same position, presumably a hand or hand towel, and the hand appears to be pointing at the hand or the hand itself. The person's posture is more relaxed, suggesting that the hands are more engaged. The palm of the hand remains stationary, a position that is likely a reflection of the hands or hand.
- Reference: The chair is now seen at a different angle and slightly further away from its original position under the table. The cushion is still visible, and the chair's wooden frame has come into clearer view, indicating that it has been pulled back or to the side. The tablecloth and table surface are no longer in the immediate vicinity of the chair, emphasizing its movement. The lighting conditions remain consistent with the first frame, and the shadow cast by the chair has shifted accordingly.

#### Sample 113 — During

- Similarity: 0.4040
- Prediction: In this frame, the sink has been drained, with the water sprinkling off of the surface. The person's hand is now more likely to be holding the sink, indicating that the water has been removed. The water's sludge remains in the sink's reservoir, presumably a source of moisture. The sink'ed surface is now slightly more exposed, with a more pronounced scrubbing action. The squeezing motion is more noticeable, with more water being poured onto the sink.
- Reference: In this frame, the burner cap still shows signs of soiling, but there's a noticeable change in its appearance. The central area and the edges look slightly cleaner, revealing the metal's original color and sheen beneath the once-uniform layer of grime. It's clear that some of the residue has been scrubbed off, as evidenced by the lighter patches and streaks on the cap's surface. Water continues to bead on the cap, and the person's hands show more purposeful movement, indicating a more thorough cleaning action is taking place.

#### Sample 114 — During

- Similarity: 0.4653
- Prediction: In this frame, the garlic clove is now more firmly held, with the skin separating from the skin. The skin is now a little more exposed, with a more pronounced layer of skin on the surface. The hand is now holding the clove, indicating that the garlic has been slicked. The clove's skin is more exposed to the knife, demonstrating the sensitivity of the knife's grip. The knife'd edge is now slightly more exposed and the skin is a bit more exposed.
- Reference: The hands are more actively engaged with the onion, with the fingers grasping it firmly. The skin of the onion in this frame shows signs of being manipulated, with a noticeable separation between the dry outer skin and the moist inner layers. The purplish-red outer skin seems to be peeling away, revealing the shinier and slightly translucent layers underneath. The action suggests that the person is in the process of removing or has started to remove the skin.

#### Sample 119 — During

- Similarity: 0.4634
- Prediction: In this frame, the scrubbing brush is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The hand's grip is more firmly held, allowing the brush to move more quickly, resulting in fewer streaks. The water's surface is more reflective, suggesting that the brush is being rubbed with soapy water. The brush's bristles are more rounded, suggesting a deeper cleaning process. The person's hand is more likely to be holding the rinsing brush in the hand, demonstrating the presence of soap and water.
- Reference: The V60 is now captured at a different angle, partially lifted out of the water, allowing a clearer view of its condition. It's being held by the rim, fingers gripping the upper edge, revealing a glimpse of the inner filter area that still contains some residual coffee grounds or staining. The motion of the water around it suggests that it is being actively cleaned, likely involving a swirling or shaking action to dislodge any remaining coffee debris.

#### Sample 124 — During

- Similarity: 0.4759
- Prediction: In this frame, the salad is now more asymmetrical, with the leaves separating from the bowl. The hands are now more involved in the action, indicating that the salad has been agitated. The salad's surface is now slightly overlapping, suggesting that the ingredients have been incorporated into the salad. The leaves are now a little more rounded, suggesting a more gradual movement, and the bowl is now positioned in a slightly more sloping position.
- Reference: In this instance, the spoon's orientation has shifted; it now rests within the confines of the plate, cradling a small portion of the meal's remnants. The bowl of the spoon is partially obscured by food particles, indicating it has been actively used. The utensil's handle reflects a secure hold within the individual's grasp, and the angle of the spoon suggests a motion of scooping or scraping the plate. The wooden texture remains visible, though slightly less pronounced due to the overlay of food.

#### Sample 127 — During

- Similarity: 0.4890
- Prediction: In this frame, the hand is now more firmly held, indicating that the water has been drained. The water's surface is now slightly damper, a sign of the water'ns ability to absorb moisture. The hand's grip is more firm, suggesting that the hand has been exerting more pressure on the water. The hands' grip is now less firm, implying that the hands are exerting less pressure on it. The squeezing motion is more noticeable, demonstrating the hand'responsible action.
- Reference: The faucet is now in a different state with the handle lowered towards the sink, reducing the water flow to a mere trickle. The diminished water stream produces less disturbance in the sink basin, resulting in a calmer surface with only a few ripples emanating from the point where the water meets the stainless steel. The handle's position closer to the sink indicates the tap is in the process of being turned off.

#### Sample 131 — During

- Similarity: 0.4868
- Prediction: In this frame, the sink is now more firmly held, with the hands positioned in a more squat position. The person's hand is more pressed against the edge of the sink, indicating that the water has been drained. The water's surface is now slightly damper, revealing a slicker surface, a smoother surface and a less soiled surface. The sink's water level is now less hazy, implying that the sink has been cleaned. The hand's grip is still slightly firm, allowing the water to drain freely. The surface of the water is now a bit more soaked, suggesting that the surface is still damp.
- Reference: In this scene, the grid is being held at a slightly different angle, with the person's hand gripping it firmly. The fingers are wrapped around one edge, implying a secure hold, likely in the midst of turning or positioning the grid. The grid remains yellow and retains its pattern of square openings, but the perspective has changed slightly, offering a view that emphasizes the grid's thickness and the shadows cast by the overhead lighting. This perspective also gives a clearer view of the sink and the countertop, reinforcing the domestic setting.

#### Sample 133 — During

- Similarity: 0.4562
- Prediction: In this frame, the lid of the jar has been removed from the container, indicating that the contents have been removed. The lid is now firmly held, implying that the lid is being removed. It is now more likely that the person is holding the lid, a gesture that may indicate that the container is being reopened. The hand is now slightly more relaxed, demonstrating the presence of the lid. The container's contents are now in the hands of the person who is holding it, presumably to ensure that the liquid remains in the container.
- Reference: In this stage, the can's lid shows more progress in the opening process. The cutting has advanced around the circumference, and the lid now has a larger exposed area, almost half of it separated from the rim. The hand grips the can opener at a different angle, suggesting the action of turning the tool has continued from the initial puncture. The manual can opener's cutting wheel has moved along the lid, leaving a jagged metal edge in its wake.

#### Sample 142 — During

- Similarity: 0.4772
- Prediction: In this frame, the lid is now positioned in a more streamlined position, with the handle positioned slightly more vertically, indicating a hand's movement. The hand'd motion is more pronounced, implying a slight movement, akin to a chopping motion. The lid remains in the same position, presumably a part of the kitchen, but the hand'remains still in the position of the handle. The kitchen's lighting is now more dim, revealing a darker, more reflective surface, reminiscent of a kitchen setting.
- Reference: The frame offers a clearer view of the kitchen setting, but the sausage remains elusive. While the person's hands dominate the frame, drawing attention to the plate they're holding, the sausage is not directly visible. It's plausible that the sausage is now beneath the plate, given the positioning and movement of the hands, indicating an action related to covering or unveiling.

#### Sample 145 — During

- Similarity: 0.4082
- Prediction: In this frame, the fruit has been sliced into smaller pieces, revealing a more rounded shape. The knife's edge is now slightly curved, indicating a slight movement, implying a hand's hand is removing the fruit from the cutting board. The fruit's skin is now more exposed, suggesting that the knife'd action is a deliberate move. The rind remains intact, with the skin firmly anchored in the fruit.
- Reference: In the second image, the piece of pitta is being interacted with; the person's fingers are grasping one edge of it. This handling causes a slight curvature in the bread, making the middle portion elevate a tad, readying it for the dipping process. The fingers appear to be holding the pitta gently, ensuring it doesn't break or crumble, maintaining its structural integrity. The subtle shadows cast by the fingers on the bread accentuate its textured surface.

#### Sample 153 — During

- Similarity: 0.4222
- Prediction: In this frame, the person's hand is more focused on the kitchen counter, indicating that the kitchen is still clean. The counter's surface is now more cluttered, with a more pronounced focus on the counter'd surface. The person'es hand appears to be focusing on the countertop, presumably a hand with fewer fingers, a resembling a kitchen sink. The countertop's surfaces are more streamlined, with the counter and counter area cluttered with crumbs and other debris. The hand's position is more hazy, implying that the person is focusing more on the surface.
- Reference: In this instance, the pepper mill is grasped firmly in the hand, suggesting that the previous state of falling has been arrested. The hand's grip is tight around the pepper mill's middle section, which is often designed to be ergonomically suitable for such a hold. The other hand remains in contact with the cloth, possibly stabilizing the situation or preparing to resume cleaning. The orientation of the pepper mill is now more vertical, indicating control has been re-established over its movement.

#### Sample 158 — During

- Similarity: 0.4401
- Prediction: In this frame, the bowl is now in a more streamlined position, with the handle still slightly angled, suggesting a slight movement. The bowl's surface is now more cluttered, with a rounded edge and a wider, more rounded center. The hand's motion is more pronounced, suggesting that the bowl has been moved, indicating that it is still in its current position. The white and blue background of the bowl'd surface is more apparent, implying that the object is still there, and the white and red contrast with the white background suggests that the cup is still present.
- Reference: Now, the orange has begun to move, evident from a slight blurring on one side, indicating the direction of the push. The previously highlighted scars and details are somewhat distorted due to the motion. The area of the table now occupied by the orange is darker, suggesting that the light source is constant, and the orange's position has indeed changed.

#### Sample 160 — During

- Similarity: 0.4103
- Prediction: In this frame, the rag is now more firmly held, indicating that the water has been drained. The hand is now holding the ring, which is now a spherical shape, with a slightly different shape than the previous frame. The ring's surface is now slightly more exposed, revealing a more rounded appearance. The water's tangerine hue is more vibrant, suggesting that the rinsing action is a reflection of the water'ns evaporation.
- Reference: The perspective has shifted to provide an overview of the dish drying area. The white dish rack now occupies the central portion of the frame, holding the same white plates and an assortment of utensils and kitchenware, suggesting that no additional items have been added since the last frame. A blue bucket is positioned to the left of the rack, and various cleaning products are visible, hinting at a well-utilized kitchen space. The sink is out of view, but the presence of the dish rack and cleaning items suggests ongoing dishwashing or kitchen cleaning activities.

#### Sample 163 — During

- Similarity: 0.3045
- Prediction: In this frame, the hand is more firmly held, indicating that the hand has been agitated. The hand is now more agitating, implying that the person is holding the hand, a gesture that is likely to be a sign of a more serious action. The hands are now more engaged, demonstrating a greater willingness to hold the hand. The person's posture is more relaxed, revealing a heightened sense of balance and balance. The overall posture is still asymmetrical, evoking a relaxed posture.
- Reference: In this frame, the tablecloth appears to have been further unfurled, covering more surface area of the floor and furniture around it. There's a hint of its material and perhaps a design or pattern, although it's not entirely clear due to the dynamic nature of the scene. There's still a sense of movement, suggesting that the action of setting or straightening the tablecloth is ongoing.

#### Sample 170 — During

- Similarity: 0.4648
- Prediction: In this frame, the chicken is now in a more streamlined position, with the fingers pointing downwards, indicating that the chicken has been agitated. The hand is now more reliant on the knife, presumably to remove the excess moisture from the chicken's surface. The chicken'd surface is now a bit more cluttered, with a smoky appearance, reminiscent of a kitchen sink or counter. The hands are now more focused on the chicken, implying that the hand is attempting to remove any remaining moisture. The kitchen counter is now slightly tilted, suggesting that the hands are preparing the chicken for cooking.
- Reference: The hand appears to have completed the action of seasoning, as evidenced by the change in the positioning of the spice shaker, now held with a more relaxed grip. The distribution of the spices on the tomatoes is more apparent, with individual grains of the darker spice visible against the vibrant red of the sliced tomatoes. The tomatoes exhibit a glistening surface, likely due to the freshly applied seasoning interacting with the tomato juices, enhancing the visual appeal and suggesting a readiness for the next step in preparation or consumption.

#### Sample 171 — During

- Similarity: 0.3986
- Prediction: In this frame, the pan is now more streamlined, with the sides of the pot positioned slightly apart, indicating that the water has been drained. The pan's surface is now slightly more exposed, revealing a more pronounced layer of water. The spoon's movements are more controlled, demonstrating a deeper immersion in the water, allowing the water to drain more quickly. The water's consistency is more uniform, suggesting that the pan has been heated more quickly, resulting in a smoother surface.
- Reference: In this frame, the oat seems to exhibit signs of subtle movement. There's a hint of displacement, as the oat's edges show slight shifting from their original position. The overall spread remains relatively uniform, but there are indications of mild disturbances within the surface, suggesting that some agitation or mixing might have taken place. The oats still retain their raw appearance, with no evident signs of cooking or moisture absorption.

#### Sample 174 — During

- Similarity: 0.4623
- Prediction: In this frame, the vegetables are now more firmly seated, indicating that they are being stirred. The hands are now positioned in a more sprightly position, demonstrating the presence of the ingredients. The color of the vegetables appears to be a bit darker, suggesting that the ingredients are being added to the pan. The ingredients are now in varying amounts, ranging from a light brown to a dark brown, and the texture of the veggies appears to have changed.
- Reference: The colander, still held by the person's hand, now appears to be in a slightly different position, closer to a stainless steel sink. The mix of beans remains inside, glistening with moisture, indicating that they are still wet from rinsing. A few beans seem to be closer to the edge, perhaps ready to fall out if the colander is shaken more vigorously. Adjacent to the colander are kitchenware items such as cups and bowls, and nearby are opened cans, giving context to a meal preparation.

#### Sample 181 — During

- Similarity: 0.4894
- Prediction: In this frame, the utensil is now in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The hand is now more firmly held, allowing the water to drain more quickly, resulting in fewer spills. The water level is now less hazy, implying that the urn is still agitating, a sign of the presence of a rinsing action. The uden's surface is now a bit more exposed, suggesting that the surface is being rubbed with soapy water. The hands are now more engaged, demonstrating the presence and cleanliness of the risina.
- Reference: In this scene, the dish is tilted at an angle, revealing its bottom to the viewer while still being grasped by the person's hand. Water droplets are visible on the surface, possibly indicating that it has just been rinsed or is in the process of being washed. The angle of the dish in relation to the camera provides a view of the curved edge, which seems to be thin and possibly has a slight lip. The surrounding items in the sink are cast in shadow, drawing the focus to the highlighted edge of the dish.

#### Sample 182 — During

- Similarity: 0.1968
- Prediction: In this frame, the hand is more pronounced, indicating that the hand has been a bit more engaged in the action. The hand is now more firmly engaged in its motion, implying that the person is attempting to move the hand. The object's position is more apparent, suggesting that the hands are moving in a more asymmetrical direction. The hands are now more likely to be a little more agitated, suggesting a slight movement. The focus is now on the hand, which is more likely a hand-held device, and the hand's motion is more evident.
- Reference: The scene is centered around the base of the washing machine, where a single black sock with a green toe and heel accent lies on the yellowish floor, indicating it might have been dropped inadvertently. The blue detergent box from the previous scene is still present, now more prominently in view. The washing machine's door remains open, but the clothes inside are not the main focus of this frame either, suggesting a pause in the laundry process.

#### Sample 185 — During

- Similarity: 0.3895
- Prediction: In this frame, the microwave oven is now in a more natural position, with the lid still firmly attached to the door, indicating that the person is holding the oven. The hand's motion is more pronounced, suggesting that the hand is holding it, implying that the microwave has been placed in pause mode. The kitchen's interior remains unchanged, with a kitchen counter and counter top indicating the oven's position. The door's surface is still visible, with its occupants still seated, presumably preparing to open the door.
- Reference: In this scene, the temperature display reads a much higher value of 556, an unusual and likely erroneous display since conventional ovens typically don’t reach such extreme temperatures. This could indicate that the user is in the process of setting or adjusting the temperature and has possibly overshot the desired temperature setting. The user’s action of turning a knob, usually associated with increasing or decreasing the oven's temperature, supports this. The digits are bright and unambiguous against the dark background of the oven’s control panel.

#### Sample 187 — During

- Similarity: 0.4255
- Prediction: In this frame, the hand is positioned in a more natural position, presumably a hand holding the pot. The pot's surface is slightly different from the previous frame, suggesting that the pot is now a bit more cluttered. The kitchen counter is now more visible, with the lid indicating that the lid is still in place. The hand's movements are more pronounced, suggesting a movement in the direction of the pot, indicating a slight movement. The lighting is more dim, suggesting the pot'd position is more streamlined.
- Reference: In this scene, the individual is engaged in the process of washing their hands over the sink, which suggests an intermediate step between handling the chicken. The chicken is not visible in this frame, but the action indicates a pause in the preparation process, likely for hygiene purposes after having manipulated the raw chicken. The running water and the posture of the hands being rubbed together are clear indications of thorough cleaning, which is a critical step in preventing cross-contamination in the kitchen.

#### Sample 189 — During

- Similarity: 0.3650
- Prediction: In this frame, the cheese has been sliced in half, with the knife pointing downwards. The knife's edge is now slightly curved, indicating a slight movement, implying a hand's movement. The cheese is now firmly pressed against the cutting board, revealing a smooth, rounded surface. The blade's motion is evident, demonstrating the knife'd motion. The sliced cheese remains intact, with a tangy texture and a crisp appearance.
- Reference: The cake, still maintaining its crumbly texture on the surface, has now been further reduced in size. An additional portion has been sliced away, and this new slice showcases the cake's uniform interior, which is noticeably darker than its topping. The golden topping creates a stark contrast against the darker, moist center. Now, more than half of the cake remains on the plate, with its exposed interior providing a glimpse into its delectable consistency.

#### Sample 194 — During

- Similarity: 0.4285
- Prediction: In this frame, the bowl is now held in a more streamlined position, with the handle still firmly held. The water's movement is more apparent, with a sprinkling of water on the surface of the bowl, indicating that the water has been drained. The hand's grip is more firm, allowing the bowl to move more quickly, resulting in fewer bubbles. The bowl's surface appears more cluttered, with more water dripping from the faucet, a sign of a deeper watering.
- Reference: The saucepan now sits more squarely in the sink, and it is filled with soapy water, creating a bubbly mixture that obscures the bottom and sides. The water is less turbulent, suggesting that the initial vigorous rinsing has ceased. There appears to be a slight reduction in the food residue as the cleaning agent has had some time to work on the leftover contents. The individual's hand is on the handle, stabilizing the pan as the cleaning continues.

#### Sample 203 — During

- Similarity: 0.4672
- Prediction: In this frame, the bottle is now in a more natural state of motion, with the lid still firmly attached to the bottle. The hand's movements are more pronounced, suggesting that the bottle has been agitated, indicating that the contents of the bottle are being poured into the bottle, rather than poured directly into the container. The bottle's contents are now more readily visible, implying that the liquid has been added to the container, thereby ensuring that the container remains intact. The lid remains in place, presumably a protective layer, and the bottle'd contents are still visible.
- Reference: In this instance, the squash is shown at a different angle, slightly more elevated than before, allowing a view of its side. The grip on the squash has changed; the fingers seem to be more spread out, adjusting the balance and grip as the squash is being manipulated. The skin of the squash still appears undamaged and firm, reflecting its freshness. The motion blur around the fingers suggests a swift, yet controlled movement.

#### Sample 209 — During

- Similarity: 0.4884
- Prediction: In this frame, the pan is now more streamlined, with the edges of the pan revealing a more rounded appearance. The pan's surface is now slightly more exposed, indicating that the pan has been heated. The surface is still a bit sloppy, with a slight crease in the center of the surface, implying that the heat has been absorbed. The frying pan'd surface is more pronounced, with more of a curved surface, suggesting that the cooking process has been more intensive. The spoon's motion is more consistent, demonstrating that the skillet has been cooking longer.
- Reference: In this frame, the omelette looks further along in the cooking process. Most of its surface now exhibits a matte finish, suggesting that the egg mixture has solidified more uniformly. There are fewer evident runny or liquid portions, implying a consistent heat distribution and continuous cooking. The edges of the omelette seem slightly curled up, hinting at a potential readiness for flipping or folding.

#### Sample 211 — During

- Similarity: 0.2887
- Prediction: In this frame, the cloth is now more firmly held, with the fingers pointing downwards. The cloth's surface appears to be a bit damper, with a slight crease in the fabric's texture. The hand's movements are more pronounced, with their hands pointing upwards.
- Reference: The sink now displays evidence of cleaning activity. There are streaks of moisture across the basin, particularly around the drain, indicative of a wiping action. To the right of the sink, cleaning implements including a sponge and a metallic scrubber can be seen, along with a spray bottle, likely containing a cleaning agent. A black-handled frying pan and other kitchen utensils are drying in a white dish rack. The individual's hands are still present, with the right hand grasping a carrot peel, possibly preparing to discard it, while the left hand rests on the counter, not actively engaged in the cleaning process.

#### Sample 212 — During

- Similarity: 0.4443
- Prediction: In this frame, the hand is more firmly grasped, indicating that the hand has been pressed against the door, a position that is likely to be a step forward. The hand's motion is more evident, suggesting that the person is attempting to open the door or close the door. The door remains open, presumably a sign of progress, but the hand still maintains the same grip, suggesting a slight movement. The kitchen remains cluttered, with the kitchen's lighting and furniture still visible.
- Reference: This frame captures the oven timer in an out-of-focus state, with the camera motion suggesting a swift movement either of the camera or the user's hand. Due to the blurriness, the exact time on the timer cannot be determined. However, the blue illumination of the timer's display persists, which continues to indicate active use. The surrounding environment is also blurred, emphasizing the motion and rendering details indistinct.

#### Sample 214 — During

- Similarity: 0.3802
- Prediction: In this frame, the rinsing spoon is now held in a more streamlined position, with the handle positioned slightly more vertically. The water flows more smoothly, resulting in fewer bubbles, which are likely caused by the presence of the soapy water. The hand's grip is more relaxed, suggesting that the water is raffinating the spoon, allowing the water to flow more smoothly. The ricotta-colored surface of the spoon appears more hazy, indicating that the scrubbing action is more intensive. The hands' posture is more pronounced, suggesting a gentler rinse.
- Reference: The blue cup is now more directly underneath the faucet, and water is actively being poured into it. The stream of water is seen falling from the faucet spout directly into the cup. The inner surface of the cup displays water droplets and some frothy bubbles, suggesting that the filling process is ongoing.

#### Sample 216 — During

- Similarity: 0.3878
- Prediction: In this frame, the hand is positioned on the counter, a position that is more apparent in the kitchen. The hand is now positioned in the center of the kitchen, indicating that the kitchen is ready for cooking. The kitchen's lighting is still visible, with the kitchen lighting still visible. The counter's surface is still occupied, with a white countertop and a counter top, presumably a reflection of the counter'd surface. The countertop's surrounding area is still evident, with its surrounding furniture, including the counter top and counter, and the countertop's counter top.
- Reference: Here, the coffee remains untouched and static, maintaining its dark coloration that suggests it is still hot and freshly made. There is no visible motion or disturbance to the surface, and the coffee's consistency appears smooth, without any signs of separation or layering that sometimes occur as an espresso settles. The positioning of the cup is unchanged from the prior frame, reinforcing the lack of interaction since the espresso was poured. The coffee's stillness hints at a brief interlude between brewing and consumption.

#### Sample 217 — During

- Similarity: 0.3740
- Prediction: In this frame, the water is now in a more streamlined state, with the lid still firmly closed. The hand is now more firmly held, indicating that the water has been drained. The water's consistency is more consistent, suggesting that the liquid has been added to the water. The lid remains in place, presumably a re-filling device, and the water'n's contents are still present.
- Reference: In this blurred frame, the action is captured mid-motion, reflecting a swift movement. The basket, now moving, is at the center, creating a whirl of colors around it. The person's hand is a blur, indicating the rapid movement of opening or possibly detaching the basket from the appliance. The background is indecipherable due to the motion blur, but splashes of orange and white suggest the continuation of the kitchen counter's cluttered state. The focus is solely on the action and the basket, with details obscured by the speed of the movement.

#### Sample 218 — During

- Similarity: 0.4253
- Prediction: In this frame, the pita is now firmly grasped by a hand, revealing a sprinkling of the pito on the surface. The hand's grip is slightly more firm, indicating that the pit has been pressed into place. The pito's surface is now slightly exposed, demonstrating the presence of a small portion of the squishy pito. The squirt of the olive oil on the pittop is now visible, implying that the olive has been placed in the pit.
- Reference: The same piece of pitta bread now exhibits a noticeable change; it is torn with a portion of it missing, indicating that a piece has been broken off. The hand, still with the smartwatch visible, is in the process of pulling away a fragment of the bread, with fingers pinched together holding the small torn piece. The texture of the bread's interior is visible, revealing a soft, fluffy crumb that contrasts with the darker, crispier edges. This action is fluid and seems to be done with ease, suggesting the bread's delicate texture.

#### Sample 220 — During

- Similarity: 0.4010
- Prediction: In this frame, the rinsing spoon is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's surface appears to be a bit damp, suggesting that the spout may be clogged or soiled. The hand's grip is more firmly held, implying that the spoon is being dragged or rubbed. The ricotta-like texture of the spoon's rind is more apparent, suggesting a deeper immersion in the water.
- Reference: Here, the cucumber is positioned under a running tap, with a stream of water cascading over its curved surface, which suggests the washing process is ongoing. The hand gripping the cucumber adjusts its hold, now supporting it from underneath to allow the water to run along its entire length. The pressure of the water causes slight ripples along the skin of the cucumber, and droplets bounce off, creating a dynamic scene where the focus is on ensuring the vegetable is thoroughly cleansed.

#### Sample 222 — During

- Similarity: 0.4279
- Prediction: In this frame, the rag is now more firmly held, with the fingers pointing downwards. The hands are now more engaged in the process of removing the soaked cloth, indicating that the scrubbing has been completed. The rag's surface is now slightly more exposed, with a more pronounced crease and a slight crease in the center. The cloth's texture is more consistent, with more of a wavy appearance, a contrast to the previous state of the wringing.
- Reference: In this frame, the sponge still looks damp but less engorged compared to the previous state, suggesting that a significant amount of water has already been wrung out. The grip on the sponge has been relaxed, allowing it to expand slightly, but it maintains a compressed shape due to the residual pressure from the fingers. The water is no longer being ejected with the same intensity, implying that the action of squeezing has been partially released.

#### Sample 225 — During

- Similarity: 0.2366
- Prediction: In this frame, the blender's lid is now positioned in a more streamlined position, indicating that the user has placed the lid on the blender. The hand's motion is more pronounced, suggesting that the blender is now in the position of its attachment, a position that would be appropriate for a quick and easy meal. The lid remains in place, implying that the lid is still attached, and the blender has been pressed against the lid. The surrounding environment is still cluttered, with the kitchen setting still visible, including the counter, counter, and kitchen counter.
- Reference: There is a notable reduction in the streaking of the mixture, indicating a progression toward uniformity. The color is now more consistent throughout, without the distinct white areas seen previously, implying a better combination of ingredients. The texture is creamier, and the previous soft peaks have started to settle into a more cohesive batter. The beaters are well-coated, and the mixture exhibits a sheen, suggesting the development of a silky structure, characteristic of a well-emulsified blend.

#### Sample 226 — During

- Similarity: 0.4679
- Prediction: In this frame, the bread is now in a more streamlined state, with the hands positioned more horizontally, indicating that the bread has been sliced. The hands are now more engaged in the process of removing the bread, implying that the loaf has been partially removed. The bread remains in its original state, presumably untouched, and the bread's texture is still uniform. The hand's movements are more deliberate, demonstrating that the action is a deliberate attempt to remove the bread from the bread. The loaf's shape is more consistent with the bread itself, a characteristic of bread that is characterized by a smooth, rounded appearance.
- Reference: Here, the scissors have made contact with the wrap, capturing the moment where the blades begin to slice through the material. The wrap's tension appears uneven, with a slight ruffling near the point of contact with the scissors. The person's grip on the wrap and scissors is steady and firm, providing control over the cutting action. The surrounding kitchen items remain unchanged, maintaining the focus on the task at hand. The wrap itself has a slight wrinkle near the cutting area, a common trait when handling such materials.

#### Sample 231 — During

- Similarity: 0.3878
- Prediction: In this frame, the onion is now in a more streamlined state, with the fingers pointing downwards. The person's hand is more pronounced, suggesting that the onion has been pushed into the container. The onion's surface is slightly curved, suggesting a gradual movement, indicating that the action is a deliberate one. The tang of the onion's flavor remains consistent with the onion, which is reminiscent of a tangy, tang-like texture.
- Reference: In this frame, the opening of the plastic bag has progressed. The fingers have pried apart the top edges, creating a visible opening through which the contents could be accessed. The plastic is now less tense, and the opening is wider, suggesting the bag’s seal has been broken. The opening's edges curl outward slightly, indicating the flexibility and reduced pressure on the plastic. The contents remain mostly obscured, but the act of opening has caused slight shifts in the position of the potatoes inside.

#### Sample 232 — During

- Similarity: 0.4202
- Prediction: In this frame, the blender's lid is now more visible, with a slightly raised edge indicating that the blender has been agitated. The lid's surface is slightly curved, suggesting that the blade is still firmly attached to the blender, indicating a gradual movement. The blender'd lid remains in place, presumably a temporary fix, and the blender is now positioned in a position to maintain its blending motion.
- Reference: In this scene, the ingredient maintains its rich yellow hue and glossy texture, but there is a slight change in the surface consistency. A depression is visible where the hand mixer's blades have just passed through, indicating the mixture’s thickness and ability to hold shape momentarily before settling. This texture suggests that the batter is not too runny, maintaining a certain body that could be suitable for a recipe requiring structural integrity, like a cake or bread.

#### Sample 233 — During

- Similarity: 0.4936
- Prediction: In this frame, the hand is now more firmly held, indicating that the hand has been positioned in a more pronounced position. The hand is more centered, implying that the person is holding the towel, which is likely a part of the fabric, and the hand's movements are more deliberate. The hands are now more engaged, demonstrating a shift in the direction of the hand, a reversing of the previous position.
- Reference: In this frame, the plate is in motion, captured while being moved swiftly to the left by the person's right hand. Due to the quick movement, the plate and the hand appear slightly blurred. The plate itself is still nearly empty, and the same design details are visible along the rim. The geometric pattern on the tablecloth is more distorted due to the perspective shift, and the shadow of the person’s hand is now cast on the tablecloth, indicating the plate is being moved closer to the table's surface.

#### Sample 234 — During

- Similarity: 0.4294
- Prediction: In this frame, the hand is more firmly held, indicating that the hand has been positioned in a more pronounced position. The hand is now more angled, suggesting that the person is holding the hand, implying that the hands are moving. The hands are still positioned, suggesting a slight movement, and the hand's motion is more consistent with the hand. The object's position is more blurred, suggesting the hand may be a bit more hesitant, a gesture that could indicate a shift in the hand position.
- Reference: Motion dominates the scene as the mat, now at a different angle, exposes a crease forming diagonally, a testament to its pliable nature. The once flat surface has yielded to the fold, its color appearing somewhat muted due to the angle and lighting. This frame captures the mat in transition, its form altered by the unseen hands guiding its shape. Surrounding kitchen elements blur into abstract shapes and colors, their details sacrificed to the swift action centered on the mat.

#### Sample 238 — During

- Similarity: 0.3440
- Prediction: In this frame, the bottle is now in a more upright position, with the cap still firmly attached to the side of the bottle. The hand's grip is slightly more firm, suggesting that the bottle has been pushed into the bottle's opening. The bottle'd cap is now positioned in the middle of the container, indicating that the cap is still in the bottle, allowing the bottle to be accessed. The cap's shape is more pronounced, suggesting a gradual movement, with a slight shift in the angle of the cap'ing action.
- Reference: The jar of flour is now inverted completely, positioned directly above the bowl to maximize the flow of flour. The powdery substance seems to be pouring out more quickly, as evidenced by a thicker stream forming a more substantial pile on top of the previously deposited flour. The white mound in the bowl has grown noticeably, and a cloud of flour dust is more pronounced around the rim of the jar, signifying a brisk pouring action.

#### Sample 241 — During

- Similarity: 0.4038
- Prediction: In this frame, the kitchen sink is now in a more streamlined position, with the handle positioned slightly more prominently, indicating a slight movement. The kitchen's surface is now more cluttered, with a cluttered appearance and a less noticeable hand. The hand is now positioned in sweeping motion, implying a gradual movement, a shift in the direction of the kitchen. The sink's position remains unchanged, with its rim and edge pointing downwards. The countertop's contrasting hues are more vibrant, suggesting a deeper focus on the kitchen counter or counter.
- Reference: The ladle appears to have been lifted from the bowl and is now hovering above the plate, with its bowl-end pointing downwards, poised to be placed down. The liquid in the glass remains at the same level, and the surrounding items on the table, such as the remote control, the blue bowl with green beans, and the yellow-lidded container, remain unmoved. The table's surface is visible, showing more of the texture and the edge of the white paper plate in the foreground.

#### Sample 244 — During

- Similarity: 0.4937
- Prediction: In this frame, the scrubbing brush is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been sucked out of the nozzle. The water's movement is more pronounced, with a broader range of movements, including the hand's movements, which are more sporacious and agitating. The hand'dive's grip is more relaxed, allowing the brush to move more quickly and effectively. The squeezing motion is more focused on the rinsing surface, demonstrating the presence of a larger, more concentrated stream of water.
- Reference: In this instant, the peeler appears to be more engulfed by the sudsy froth, with the sponge compressing even further into its form, pressing the cleansing agents deep into the peeler's joints and blade. The water's flow from the faucet continues uninterrupted, washing away some of the soapy mixture, revealing a bit more of the peeler's handle and the swivel mechanism that allows the blade to adjust to the contours of a potato.

#### Sample 245 — During

- Similarity: 0.4409
- Prediction: In this frame, the spoon is now positioned in a more streamlined position, indicating that the spoon has been agitated. The spoon's surface is now slightly curved, suggesting that the hand is attempting to grasp the spoon, a motion that may indicate a slight movement. The hand's motion is more pronounced, suggesting a smoother motion. The object's shape is more apparent, implying that the object is a spoon or a utensil, and the spoon'd motion is less noticeable.
- Reference: In this frame, the egg's transformation has commenced. The fork, now held by a hand, has been introduced into the bowl, and the yolks have been breached. The yolks and albumen are beginning to blend, creating streaks of yellow amid the clear whites as the fork’s tines drag through the mixture. The action is gentle, indicated by the soft waves and the lack of splatter, revealing that the whisking process is in its initial phase, with the ingredients being combined with care to avoid spilling.

#### Sample 247 — During

- Similarity: 0.2661
- Prediction: In this frame, the scrubbing brush is now more visible, with the handle positioned slightly more vertically, indicating that the water has been drained. The hand's movements are more pronounced, with a more rounded angle, implying that the brush is being dragged along the surface of the rinsing pan. The water's movement is more sporacious, allowing the brush to move more quickly, resulting in a cleaner, more concentrated stream of water. The brush's surface is now a bit more soiled, suggesting that the lint is still present.
- Reference: In this scene, the blender is still inverted, but now water is actively flowing from the faucet into the blender's interior. The stream of water is causing a bubbly reaction, likely mixing with the remaining residue inside the blender, creating more froth that is visible through the transparent plastic. The lid remains off to the side, and the water's force seems to be targeting the bottom, now the highest point, of the blender's interior.

#### Sample 248 — During

- Similarity: 0.4812
- Prediction: In this frame, the light is now more visible, with a more pronounced focus on the door and the door itself. The light is more visible in the middle of the room, with the door still open, suggesting a gradual movement. The lighting is now a bit more dim, with less lighting and a less noticeable difference in the lighting. The door's position remains unchanged, with its occupants still positioned in the same position.
- Reference: In this instance, the hand is actively engaging one of the buttons on the light switch, applying pressure downwards. This action typically closes the electrical circuit, allowing current to flow to the light fixture. While the button is being pressed, there is no immediate change in the room's lighting observable in the frame, possibly due to a momentary delay between the button being pressed and the light being activated, or the frame being captured in the split second before the light responds.

#### Sample 251 — During

- Similarity: 0.4483
- Prediction: In this frame, the milk is now a little more agitated, indicating that the hand is attempting to stir the milk. The hand's motion is more pronounced, implying that the milk has been stirred, resulting in a more concentrated liquid. The milk's texture is more uniform, exhibiting a smoother texture, a less dense texture, and a slightly more rounded consistency. The sprinkling of the milk on the surface of the spoon is more evident, demonstrating the presence of the hand'd motion.
- Reference: In this scene, the water has been transferred into a kitchen appliance, most likely an open sandwich toaster or grill. The water is dispersed unevenly, with some areas appearing more concentrated, indicating a recent pour. The appliance's surface is shiny and reflective, with the water magnifying its sheen. Droplets and small rivulets of water are visible, with some coalescing into larger pools, reflecting a state of recent activity and the dynamic nature of the liquid as it interacts with the hot surface.

#### Sample 252 — During

- Similarity: 0.3633
- Prediction: In this frame, the knife is now positioned in the hand, a slicing motion indicating the knife has been inserted into the knife's blade. The knife'd edge is now slightly curved, indicating a slight movement, implying a sharpening action. The blade's surface is now more rounded, suggesting a more gradual movement. The hand's grip is still firm, suggesting that the knife was pressed against the knife, revealing a smoother surface. The butter's texture is more consistent, suggesting the knife may have been pressed into the butter'ns' surface.
- Reference: In this frame, the cake remains largely the same, still maintaining its ringed bundt form. The slice that was previously cut and replaced askew is now absent, removed from the frame entirely. This subtraction leaves a clear demarcation where the slice once was, disrupting the cake's continuity. The doily beneath remains visible, and there are no additional crumbs or changes in the cake's texture or coloration.

#### Sample 253 — During

- Similarity: 0.4289
- Prediction: In this frame, the sponge has been agitated, indicating that it has been placed in a hot, dry place. The hand is now more likely to be holding the sponge, which is likely to have been sprayed with water. The surface of the sponge appears to be slightly damp, suggesting that the water has been applied to the sponge. The sponge's surface appears to have cooled, suggesting the sponge is still soaking wet. The creases on the sponge'd surface are more noticeable, suggesting a more gradual process.
- Reference: In this frame, the rag is more distinctly visible, showing its textured surface more clearly. It's still being held firmly, emphasizing its utilitarian function in cleaning. The wetness of the rag is evident, with certain portions appearing more saturated than others. Its edges are splayed out a bit, showcasing its length and breadth.

#### Sample 255 — During

- Similarity: 0.4883
- Prediction: In this frame, the microwave oven is now in a more visible position, with the lid still slightly open. The hand is now positioned in the middle of the microwave, indicating that the microwave has been opened. The microwave's interior remains unchanged, with its door still open, and the surrounding area, including the kitchen, remains unchanged. The kitchen's counters, counter top, and door remain unchanged, implying that the oven is still open.
- Reference: In this frame, the hand is more pronouncedly positioned over a switch or control panel. The fingers are closer together, signifying that the hand has either just pressed or is about to press a button or switch. The surrounding area has a toaster, containers, and other kitchen items. Based on the proximity of the fingers to the device, it's indicative that an action on the switch has been made or is imminent.

#### Sample 256 — During

- Similarity: 0.4609
- Prediction: In this frame, the stove is still in motion, with the person's hand pointing at the counter. The kitchen counter is now more visible, with a white towel indicating a hand or hand with utensils. The counter's surface is now cluttered with crumbs, crumbs and other debris, indicating that the stove has been occupied. The countertop's position remains unchanged, with no visible movement, implying that the person is preparing food or cooking. The stove's lighting is still visible, presumably from the kitchen counter, but the counter'rsquo;s lighting indicates that the counter is still active.
- Reference: In this snapshot, the hand is in closer proximity to the grill, specifically targeting the grate over one of the burners. The thumb appears to be tucked underneath the grate, indicating that the person is preparing to lift or remove it. The condition of the grill remains unchanged from the previous frame, retaining its clean and maintained appearance. The hand's shadow is cast over the cooktop, altering the reflection and metallic sheen of the surface. No other objects or materials are in direct contact with the grill, maintaining a focus on the imminent action of the hand.

#### Sample 258 — During

- Similarity: 0.3887
- Prediction: In this frame, the hose is now in a more streamlined position, with the handle positioned slightly more vertically, indicating a deeper cleaning action. The water's movement is more pronounced, with a broader range of movements, ranging from a gentle rinsing to a vigorous rinse. The hose's surface is now more cluttered, with more water being drained from the nozzle, resulting in fewer spots of debris. The person's hand is more relaxed, demonstrating a less pronounced movement. The hand's posture is more casual, implying a steady hand'responsible to the water'n's motion.
- Reference: The dish now appears closer to the center of the frame, reflecting a slight shift in focus during the cleaning process. Water droplets and suds cling to its surface, evidencing the use of soap or detergent for cleansing. The presence of a blue scrubbing brush in the sink basin implies that a manual scrubbing action has been or will be applied to the dish. There is less visible residue on the pan's surface compared to the previous state, suggesting that some cleaning has already taken place.

#### Sample 264 — During

- Similarity: 0.4733
- Prediction: In this frame, the chicken is more seasoned, with a more pronounced aroma of a slurry of water. The water's consistency has been progressively lowered, indicating that the water has been added to the pan. The color of the chicken's surface has remained consistent, suggesting that the cooking process has been more intensive. The steamed chicken is now more acrid, exhibiting a slightly darker hue, a hint of smokyness.
- Reference: In this moment, the stirring motion has introduced movement into the mixture, causing some ingredients to become more visible. The yellow pieces, likely vegetables, are more prominent against the lighter color of the curry, which is a creamy, beige hue indicative of a gravy enriched with either dairy or coconut milk. The stirring seems to be gently folding the ingredients, allowing even distribution of heat and flavors throughout the curry. The steam rising off the surface suggests that the temperature is well-maintained for cooking.

#### Sample 267 — During

- Similarity: 0.4569
- Prediction: In this frame, the onion has been partially sliced, with the skin still exposed. The hand is now positioned in the position of the knife, indicating that the knife has been inserted into the onion. The knife's grip is now more firm, suggesting that the onion is now being carefully cut. The onion's skin remains intact, with its skin revealing a smoky appearance. The skin is now slightly slanted, suggesting a gradual movement, implying that the cutting is now complete. The blade is now in the same position as the knife'd hand, presumably aimed at removing the onion from the skin.
- Reference: In this scene, the can of sweetcorn is undergoing the initial stages of being opened. A can opener has been affixed to the top, its handles gripped firmly in the user's hands. The blade has punctured the lid, as evidenced by the slight separation visible along the can's edge where the opener has begun its work. The opening process appears to be at the very start, with only a small portion of the lid cut, and the sweetcorn remains concealed inside, its state still mostly a mystery beyond the label's promise.

#### Sample 269 — During

- Similarity: 0.4526
- Prediction: In this frame, the steamed broccoli is now more firmly sliced, indicating that the knife has been slicked. The knife's blade is now slightly angled, implying that the sliced broccoli is being sliced in a circular motion. The sprinkling of the boiled broccoli leaves appears to be a gradual process, demonstrating the emergence of a sprig of broccoli. The leaves are now more uniformly arranged, forming a single layer of spongy, clumpy pieces. The blade is still pointing at the coiled broccoli, a sign of the progress of the cutting process.
- Reference: The cutting process seems to be more advanced in this frame. There are now more pieces of choi pak arranged on the wooden cutting board. The slices appear to be more uniform in size, suggesting a methodical chopping approach. The green leaves and white stems are more distinguishable now, as the choi pak is being broken down further. The bowl, which previously contained choi pak, is now fuller, indicating that more of the vegetable has been prepped.

#### Sample 271 — During

- Similarity: 0.4369
- Prediction: In this frame, the sink is now in a more natural state, with the lid still slightly tilted, suggesting a gradual movement. The hand is now more firmly grasping the sink, indicating that the sink has been agitated. The sink's surface is now slightly more exposed, suggesting that the water has been removed from the sink. The kitchen counters are now more visible, with a cluttered display of kitchen items and a kitchen counter. The counters and counters remain in place, with no visible movement.
- Reference: In this moment, the bottle of washing up liquid is actively being squeezed, indicated by the blurred motion of the hand and the bottle's deformation. The stream is dynamic; a splash is just beginning as the liquid hits the accumulated pool in the bowl, causing slight ripples to emerge. Droplets may be starting to scatter due to the force of impact, and the stream itself is likely becoming erratic as the pressure changes with the squeezing action.

#### Sample 272 — During

- Similarity: 0.4094
- Prediction: In this frame, the rinsing spoon is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's surface appears to be drier, with a broader range of movement, resulting in fewer bubbles. The hand's grip is more firmly held, allowing the spoon to move more quickly, thereby removing any remaining debris. The ricotta-colored water is now more concentrated, forming a tighter, more sprinkling effect.
- Reference: In this scene, the ladle is now being held at a slightly different angle, with the person's hand turned so that the bowl of the ladle faces upwards. The fingers are visible at the base of the ladle's handle, applying pressure and adjusting the grip as needed for the cleaning process. The faucet continues to run, with water cascading over the inner surface of the ladle, which now shows evidence of soap suds, indicating that it has been soaped and is undergoing washing. The environment is consistent with that of the previous frame, with kitchen items still scattered around the sink.

#### Sample 278 — During

- Similarity: 0.4154
- Prediction: In this frame, the dough is now more firmly held, with the edges of the dough still slightly exposed. The hand's motion is more deliberate, indicating that the dough has been kneaded. The dough's surface is more asymmetrical, implying that the hand is attempting to press the dough into the dough, forming a smooth, even layer. The creases are more defined, suggesting that the knicker is a bit more firm, and the dough' texture is more uniform.
- Reference: The cling film has been further pulled out from its package, stretching across the length of the scene in front of the person. The film appears to have more noticeable creases and overlaps, and the extended portion is held aloft by the individual's hands. The packaging is in a nearly vertical position, indicating the force exerted to extract the film.

#### Sample 279 — During

- Similarity: 0.4719
- Prediction: In this frame, the microwave oven is now more visible, with a slightly different shape and a more noticeable difference in its position. The kitchen's lighting is now dim, suggesting a gradual movement, indicating that the oven is still in its current position.
- Reference: In this frame, the cabinet door is still ajar but appears to be more closed than in the previous frame, suggesting a continued motion towards closing. The items inside the cabinet remain the same, and there is no significant change in the organization or arrangement of the contents. The blur is still present, reinforcing the idea of movement. The angle of the door compared to the previous frame suggests it has been moved slightly but is not yet fully closed.

#### Sample 280 — During

- Similarity: 0.3726
- Prediction: In this frame, the table is in a more streamlined position, with a slightly more cluttered appearance. The surface of the table appears to be a bit damp, suggesting a soiled surface. The table's surface is more exposed, suggesting that the table has been wiped down. The counter's lighting is dim, suggesting the table'd lighting is reflected in the light. The countertop's color is more vibrant, suggesting it may be scuffed or smashed. The kitchen counter'envelops the table, suggesting an upscale kitchen setting. The white tile floor is a contrast to the surrounding furniture, suggesting its placement in contrasting with the rest of the room. The blue and white tile is reminiscent of
- Reference: In this snapshot, the toaster is again partially visible, caught mid-motion. A hand is grasping a drawer handle, possibly searching for an item or in the process of storing something. The motion blur permeates the scene, creating an effect that implies swift, perhaps frantic, activity. The cabinet's wood grain and the handle's details are smeared across the image due to the motion, suggesting that the focus of the action has quickly shifted from the toaster to the drawer.

#### Sample 284 — During

- Similarity: 0.4199
- Prediction: In this frame, the pan is now more cluttered, with the ingredients a little more visible. The pan's surface is now slightly more exposed, with a more uniform appearance of the ingredients. The cooking process has been a bit more fluid, with some of the vegetables still being adrift, indicating that they are still preparing. The kitchen is now a step closer to the beginning of the cooking process, with more of the veggies forming a clump of florets.
- Reference: The pasta now shows a more even distribution of the pesto sauce. The rotini retains its distinct spiral shape but is now uniformly coated with the sauce, resulting in a harmonious blend of color and texture. It's evident that the stirring process has progressed, as there's an overall creamy consistency to the dish. The wooden spoon continues its mixing, moving the pasta and ensuring even coverage of the sauce.

#### Sample 294 — During

- Similarity: 0.4314
- Prediction: In this frame, the pan is now more streamlined, with the handle pointing downwards, indicating a more gradual movement. The pan's surface appears to be a bit more ragged, with a slight change in the color of the pan'd surface. The person's hand is more likely to be holding the pan, implying a gentle motion. The surface of the blade is now slightly more exposed, revealing a broader range of surfaces. The blade's position is more pronounced, demonstrating a gradual movement, a shift in the direction of the action.
- Reference: In this instance, the towel is not immediately visible; instead, the focus is on the hands, one of which is holding a clear glass object while the other is manipulating a smaller, bluish-white object that could be a cap or a lid. This suggests that the towel may have been set aside or is being held in a manner that is not captured by the frame. The absence of the towel from direct view implies a shift in the cleaning process or a transition to a different cleaning task.

#### Sample 295 — During

- Similarity: 0.4791
- Prediction: In this frame, the scrubbing brush is now more visible, with the handle positioned slightly more vertically, indicating that the water has been drained. The hand is now positioned in a more horizontal position, presumably a sprinkling of soapy water, a sign of the presence of soap in the water. The squeezing motion is more noticeable, with a small amount of soap smeared onto the surface of the brush. The brush's surface appears to be a bit damp, suggesting that the brush is still agitating. The water level is now less visible, and the brush'ns' surface is more exposed. The person's hand is still holding the rin
- Reference: The strainer now cradles a vibrant blue sponge, its rough texture indicating its abrasive capabilities for cleaning. Water no longer flows through it; instead, the focus has shifted to the manual scrubbing action, which is suggested by the positioning of the hands and the sponge. Small bubbles from detergent residues cling to the inner walls of the strainer, and the previously visible food particles appear diminished, a result of the ongoing cleaning effort.

#### Sample 297 — During

- Similarity: 0.4019
- Prediction: In this frame, the chicken is now in a more streamlined state, with the skin still firmly attached to the meat. The hand is now positioned in the middle of the kitchen, indicating that the chicken has been sliced. The knife's edge is now slightly angled, suggesting that the knife is now being pressed against the meat, implying that the meat has been cut into the desired shape. The meat is now more rounded, revealing a softer texture, and the skin is now less sloppy.
- Reference: In this moment, the person's hands show motion, with the fingers of one hand holding the board steady and the other using the flat side of a knife blade to scrape the garlic off the board. The garlic is no longer in a solid clove form but is now a smeared, pasty consistency, spread thinly across the board. This indicates that the garlic has been crushed to a degree that it's almost paste-like, ready to be added to the pan for cooking. The action of scraping suggests that the person is transferring the garlic into the pan, as the garlic paste is gathered towards the edge of the board.

#### Sample 298 — During

- Similarity: 0.2767
- Prediction: In this frame, the sink has been re-opened, with the handle still firmly held, indicating that the water has been removed from the sink. The hand is now more likely to be holding the sink, implying that the sink is still in the position of its predecessor, the sanitized basin. The water's surface is now slightly damper, suggesting that the lint has been lifted from the basin.
- Reference: Here, the gloves are again in focus, with the left hand visibly holding onto a pot's edge and the right hand slightly raised, suggesting a moment of transition or the performance of a task requiring a two-handed approach. The bright yellow rubber material of the gloves continues to be prominent, and they maintain a sheen that could either be from the material's natural finish or a slight dampness, possibly from exposure to water.

#### Sample 303 — During

- Similarity: 0.4519
- Prediction: In this frame, the bottle is now in a more upright position, with the lid still firmly attached to the bottle. The hand's grip is slightly more firm, suggesting that the bottle has been pushed into the bottle's opening. The bottle'd cap remains in place, with its contents still visible. The lid remains in the same position, indicating that the cap is still in the bottle, and the bottle itself is now firmly held.
- Reference: In this snapshot, the same aluminum beverage can is now slightly tilted. The person's hand, identifiable from the same metallic wrist accessory, appears to be pouring liquid from the can into a transparent glass that already has some fluid. The glass exhibits a hint of condensation, indicating the chilliness of its content. The table retains its wooden aesthetic, and the black mat and a fork are visible nearby.

#### Sample 304 — During

- Similarity: 0.3836
- Prediction: In this frame, the utensil is now in a more streamlined position, with the handle positioned slightly more vertically, indicating a hand's movement. The hand'd motion is more pronounced, implying a movement in the direction of the urn, a gesture that may indicate a shift in the position of the hand. The utmost portion of the handle is now visible, with a rounded edge indicating the hand'es movements. The brush's surface is now more cluttered, revealing a less cluttered appearance.
- Reference: In this moment, the tin is captured mid-transition, the focus of a simple yet crucial kitchen task. Water is being poured into the tin, producing a dynamic interplay of fluidity against the rigid, stained background of the tin's interior. The stream of water appears forceful, suggesting a vigorous pour, and its impact on the tin’s surface creates a scattering of water droplets and rivulets that momentarily disturb the residual patterns of baked-on remnants.

#### Sample 305 — During

- Similarity: 0.4961
- Prediction: In this frame, the vegetables are positioned in a more streamlined position, with the ingredients separating more evenly. The hands are more engaged, indicating that they are preparing to serve, rather than merely removing the vegetables. The kitchen is now more cluttered, with a variety of items ranging from vegetables to a handful of dried fruit to steamed rice. The pan is now positioned on the counter, presumably a counter for the food to be consumed.
- Reference: The perspective shifts to show more of the countertop's expanse, revealing a clean, clutter-free surface that extends towards a cooking area. An array of beer bottles of various sizes and labels stands in an irregular formation near the edge, alongside a pair of clear glasses, one upright and the other tipped over. A wooden spoon lies on a white spoon rest, next to a skillet on the stove filled with a sautéed mixture, indicating a meal preparation in progress. The person's hands are now in view, one holding a sponge, suggesting active cleaning.

#### Sample 308 — During

- Similarity: 0.4773
- Prediction: In this frame, the rinsing spoon is now held in a more streamlined position, with the handle positioned slightly more vertically. The water's movement is more pronounced, with a broader angle indicating that the water has been drained. The hand's grip is more relaxed, with more movement, indicating the presence of the water. The ricotta-colored waterdrops are more visible, with their rounded shape indicating a deeper rinse. The person's hand is more likely to be holding the spoon, allowing the water to drain more quickly.
- Reference: In this scene, the baking tray has been tilted to allow the stream of water to rinse its surface. The person's hands are visible, with one hand adjusting the tap and the other supporting the tray. There are visible pieces of debris and food particles being washed away, leaving cleaner surfaces in their wake. The tray’s non-stick coating is more evident now as the water flows over it, reflecting the light more on the washed areas, while the particles suggest that the tray was likely used for roasting or baking.

#### Sample 310 — During

- Similarity: 0.2048
- Prediction: In this frame, the knife's surface is more pronounced, with a more rounded edge and a sharper edge. The hand's motion is more deliberate, indicating that the knife has been pressed against the surface, resulting in a smoother surface. The knife'd edge is more noticeable, revealing a slight crease in the surface.
- Reference: In this scene, the tray is shown in a similar state to the first, maintaining its worn appearance with streaks and spots of oil glistening lightly across its surface. The placement of the three dough balls remains unchanged; however, the perspective is slightly different, indicating a shift in the camera angle or the tray's position. The dough balls appear untouched and consistent in their shape and size with the previous frame, reinforcing the notion that they are in a static state of rest.

#### Sample 312 — During

- Similarity: 0.3571
- Prediction: In this frame, the onion is now a little more exposed, with the skin revealing a more rounded appearance. The person's hand is more pronounced, indicating that the onion has been sliced, exposing the skin. The onion's skin is more exposed to the light, implying that the knife has been used to cut the onion. The knife's blade is now more angled, revealing the onion'd skin.
- Reference: The scene continues with the preparation of the green beans. Here, the person's hands are seen holding a bean between the thumb and forefinger, suggesting the act of snapping or trimming the ends. The discarded pieces of trimmed ends are more prominent on the countertop, creating a scattered array of green against the dark surface. The white colander still cradles the trimmed beans, which maintain their bright green color, a sign of their freshness. The lighting casts shadows on the beans and the person's hands, enhancing the texture and depth of the image.

#### Sample 320 — During

- Similarity: 0.3798
- Prediction: In this scene, the chicken is now in a more streamlined position, with the skin revealing a darker hue. The hand is now positioned in the middle of the pan, indicating that the meat has been sliced. The meat is now more seasoned, with a lighter hue to the meat. The skin is now slightly smoky, with no visible signs of cooking. The chicken's surface is still a bit damp, with some of the meat still charred.
- Reference: In this scene, the skin remains in focus, but the act of peeling seems to have progressed. The sweet potato skin now appears more detached from the flesh, with a larger portion of the vegetable being exposed. The peelings on the cutting board have increased in quantity, indicating the continuation of the peeling process. The hand position suggests an ongoing action, with the knife being used to carefully separate the skin from the flesh, minimizing waste. The skin pieces exhibit varying degrees of curvature, reflecting the natural shape of the sweet potato.

#### Sample 321 — During

- Similarity: 0.4562
- Prediction: In this frame, the spout is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's movement is more pronounced, with a broader range of movements, including the hand, which is more likely to be abrasive, allowing the rinsing action to take place. The hand's grip is more relaxed, revealing a wider range of motions, including a movement that may be more sporacious. The ribbing of the utensil appears more agitated, demonstrating the presence of a larger amount of water.
- Reference: In this snapshot, the pan remains in the sink but appears to be in a slightly altered position, suggesting it has been moved or adjusted. The dark liquid inside the pan seems less prominent, which could mean that some of it has been discarded or the angle simply doesn't capture it as prominently. The hand previously seen with a green sponge is now holding the pan's handle, possibly preparing to rinse or scrub it. The surrounding environment remains relatively unchanged, with the nearby dishes and utensils still awaiting their turn to be cleaned.

#### Sample 324 — During

- Similarity: 0.4814
- Prediction: In this frame, the meat is now a more seasoned and tender, with the skin a little more exposed. The knife's grip is now more firm, indicating that the meat has been sliced. The meat is still a bit firmer, with a slight change in the shape of the knife'd edge. The skin is now slightly more supple, suggesting that the knife has been cut into the meat. The flesh is now less brittle, suggesting a gradual process of cooking.
- Reference: The piece of sweet potato remains on the cutting board, with its vibrant orange hue still prominent. It appears untouched since the last observation, but there is now a fork introduced into the scene. The fork is positioned near the potato, angled as if it's about to pierce or pick up the vegetable piece. The knife, previously placed beside the potato, now sits at a slight angle to it, possibly indicating some minor movement or adjustment in preparation for the next action.

#### Sample 325 — During

- Similarity: 0.4588
- Prediction: In this frame, the slicing knife is now more firmly held, indicating that the knife has been sloughed away. The knife's blade is now positioned in the center of the cutting board, a position that is more likely to be used to slice the vegetables. The hand's fingers are now more precise, implying that the blade is slashed away from the cutting surface. The blade's surface is now slightly curved, suggesting that the cutting tool has been used to cut the vegetables into smaller pieces. The sprigs of the knife are now firmly pinned to the cutting boards, demonstrating the utmost care for the delicately sliced vegetables.
- Reference: In this scene, the kiwi has been further dissected, with more of the skin peeled away. The exposed inner flesh appears juicy and glistening under the ambient light, indicating the freshness of the fruit. The individual's fingers are pinching a section of the peel, stabilizing the fruit while the other hand maneuvers a spoon to gently separate the skin from the flesh. The contrast between the remaining skin and the bright green fruit is striking, underscoring the ongoing peeling process.

#### Sample 327 — During

- Similarity: 0.4163
- Prediction: In this frame, the sink is now more visible, with a more streamlined appearance. The hand is now positioned in the middle of the sink, indicating that the sink has been agitated. The sink's surface is now slightly more exposed, suggesting that the water has been removed from the sink. The water level is now less visible, suggesting a gradual movement, and the sink'd surface is still a bit damp. The surrounding environment is still blurred, implying a cluttered kitchen or bathroom.
- Reference: The image captures a motion blur, indicating rapid movement, with the lunch box becoming an elongated smear across the visual field. Due to the swift motion, the box's details are indiscernible, and the once discernible shapes are now streaks of white and gray, blending with the blurred background. The perspective has shifted dramatically, signaling that the lunch box is in the midst of being tipped over, though its contents and final position remain uncertain in this snapshot of action.

#### Sample 328 — During

- Similarity: 0.2935
- Prediction: In this frame, the bag is now in a more streamlined state, with the lid still firmly attached to the bag. The hand's movements are more pronounced, suggesting that the bag has been pushed open. The bag's contents are more visible, with a rounded edge and a slight movement in the direction of the hand. The contents of the bag are more readily visible, indicating that the person is attempting to open the bag or removing it.
- Reference: Here, the slice of bread is partially inside the toaster, with only a small portion protruding above the slot. It sits within a gray toaster that seems to be of a modern design, with the red light on the control panel indicating that the toaster is on and actively toasting. The bread has begun its transformation from a soft, pliable state to one that will become crispy and golden-brown, the anticipation of that textural change implicit in the image.

#### Sample 329 — During

- Similarity: 0.4320
- Prediction: In this frame, the hand is positioned on the top of the bottle, a position that is more apparent in the context of the scene. The lid is now slightly tilted, suggesting that the lid is being pushed. The hand's motion is more evident, suggesting a movement in the direction of the action. The bottle's contents are still visible, with the lid's shape and shape indicating that the liquid has been poured into it. The surrounding environment is more reminiscent of a kitchen setting, with a light source and a clear view of the kitchen.
- Reference: The bag now seems more exposed as compared to the previous frame. The hand appears to be actively engaging with the bag, either adjusting or opening it. The bread inside is more clearly visible, showing its texture and confirming that it is indeed a bread bag. The orange label on the bag is also clearer, and the overall placement of the bag has slightly shifted, implying some interaction has taken place.

#### Sample 332 — During

- Similarity: 0.3583
- Prediction: In this frame, the oven door is now in a more streamlined position, with the handle positioned slightly more horizontally. The person's hand is now more firmly grasping the door, indicating that the oven has been opened. The interior of the oven is now cluttered with a variety of items, including the oven's interior, which is a contrasting contrast to the kitchen's white counter top. The kitchen'd interior is now slightly more open, with fewer items and less clutter. The door's position is now less visible, with only the door'side of the kitchen visible.
- Reference: In this instance, the freezer drawer is almost entirely closed, with only a slender sliver of space visible, signifying the near completion of the closing action. The swift movement is evident from the blur of the drawer's edges, and there is a discernible decrease in the gap from the previous state. The contents are still not in clear view, but the drawer appears to be secure, indicating that items inside are less likely to be disturbed.

#### Sample 334 — During

- Similarity: 0.4341
- Prediction: In this frame, the paperclip is now positioned in a more streamlined position, with the fingers pointing downwards. The hand's movements are more deliberate, indicating that the paper has been pressed against the edge of the paper. The paperclip's surface is slightly curved, suggesting that the hand is attempting to grasp the paper, a process that may have been initiated by the person who is holding it. The hands' posture is more relaxed, suggesting a slight movement in the direction of the action. The creases on the paper are more prominent, suggesting the paper is now being pressed into the paper's edge.
- Reference: The same hand now holds the knife at a different angle, pointing more towards the bottom corner of the frame, which suggests that the spreading motion has continued. The creamy substance appears more evenly distributed across the bread's surface, though there are still areas of varying thickness. The hand's grip on the knife has shifted slightly, now more in control, and the knife itself has less of the white substance on its blade, indicating that most of it has been transferred to the bread. The bread slice remains angled, and the crust is more prominently in view.

#### Sample 335 — During

- Similarity: 0.3314
- Prediction: In this frame, the hand is now more firmly engaged in the action of removing the table mat. The hand is more asymmetrical, indicating that the mat has been placed in a more pronounced position. The mat's surface is now slightly more exposed, suggesting that the hand has been removing it from the table. The table's shape is now a bit more streamlined, implying that the table is now being rearranged. The creases and wrinkles are more prominent, suggesting a gradual movement.
- Reference: The degreaser now shows a different stage of application. The mist has settled slightly, with fewer droplets suspended in mid-air, and more visible accumulation on the surface, forming irregular patterns where the liquid has begun to settle. The hand holding the bottle has moved marginally to the right, indicating the continuation of the spraying action. The countertop reflects less light where the degreaser has settled, indicating the surface is now moistened by the liquid. The spread of the degreaser is more widespread, covering a larger area than in the previous frame.

#### Sample 338 — During

- Similarity: 0.1823
- Prediction: In this frame, the pan is now more streamlined, with the edges of the pan revealing a more uniform appearance. The pan's surface is now slightly more exposed, indicating that the pan has been agitated. The creases on the sides of the skillet are more noticeable, implying that the cooking process has been completed. The cooking process is still a little slow, but the pan'd surface remains a bit firmer, resulting in a less dense and brittle pan.
- Reference: Upon closer inspection, the extractor fan presents a consistent appearance of wear, with no discernible changes in the distribution or intensity of the grease marks compared to the previous state. The uniformity of the discoloration suggests that the fan has been subjected to a steady amount of heat and airborne particles over a considerable duration. There is no evidence of any cleaning attempts, as the patterns of grease remain uninterrupted and widespread across the entire surface of the fan.

#### Sample 341 — During

- Similarity: 0.3615
- Prediction: In this frame, the scrubbing brush is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been sucked out of the nozzle. The water's movement is more pronounced, with a broader angle indicating the presence of a larger amount of water. The hand's grip is more relaxed, allowing the brush to move more quickly, resulting in fewer streaks. The squeezing motion is more consistent, demonstrating the presence and movement of the brush.
- Reference: In this perspective, the tablecloth is viewed from above, providing a clear and centered view of the green apple illustration. The cloth now shows signs of interaction, with water visibly running across its surface, causing the fabric to cling and contour around the sink's edge, creating a dynamic interplay of light and shadow. This frame gives the impression of the tablecloth undergoing a cleaning process, with the water altering its flat appearance to one that is more textured and three-dimensional.

#### Sample 348 — During

- Similarity: 0.4407
- Prediction: In this frame, the refrigerator door is now open, with a hand in the middle of the door, revealing a more streamlined view of the contents. The door's interior is more spacious, with the contents of the fridge positioned in a slightly different position than in the previous frame. The interior of the refrigerator is more cluttered, with less space to be seen, and the door'd interior is now more open. The refrigerator's contents are more visible, with items such as fruit, vegetables, and a few items indicating that they are in the refrigerator.
- Reference: This frame captures the kitchen cabinet in a clearer state with an open door, revealing a more organized array of spice jars and boxes, all neatly aligned on a shelf. The hand is blurred in motion, indicating the action of reaching for or placing a spice jar. The spice jars vary in size and color, suggesting a variety of herbs or seasonings. No specific jar is the sole focus, but collectively they create an impression of an assortment maintained for culinary purposes.

#### Sample 351 — During

- Similarity: 0.4258
- Prediction: In this frame, the bag is now in a more streamlined state, with the handle positioned slightly more firmly, indicating that the person is attempting to open the bag. The bag's contents are now more visible, with a rounded edge indicating the bag'd contents are still present. The person's hand is now more reliant on the bag to grasp the contents, implying that the bag has been opened. The packaging is now a bit more cluttered, with more of the contents indicating a desire to open it.
- Reference: Here, the olive oil bottle's cap is being handled by a person, whose hands are the focal point of the image. The cap is grasped firmly between fingers, showing the action of capping in progress. The individual appears to be in the midst of securing the cap back onto the bottle, indicated by the positioning of the hands and the slight squeeze of the fingers, which are attempting to align the cap with the threads of the bottle. This frame captures the motion and intent to seal the bottle after use, ensuring the olive oil's freshness.

#### Sample 353 — During

- Similarity: 0.4495
- Prediction: In this frame, the hand is positioned on the top of the machine, a position that is likely to be a part of the process of adjusting the settings. The hand's position is more pronounced, suggesting that the hand has been adjusting its settings. There is no indication of the hand'ing or adjusting, but the hand appears to be holding the machine. The surrounding environment is still a little blurry, with the surrounding environment indicating that the machine is still in its initial stages of use.
- Reference: In this instance, the button is captured in the midst of being pressed. One can discern the initial stages of depression as the button yields to the finger's force. The top surface of the button, which was previously flush with the console, now shows a slight angle indicative of the pressing action, and the shadow around the finger's contact point has deepened, reflecting the change in distance between the finger and the button surface. The light reflection on the button's surface has altered slightly, conforming to the new shape as the button is pushed inward.

#### Sample 354 — During

- Similarity: 0.4748
- Prediction: In this frame, the sink is now in a more natural state, with the lid still slightly tilted, suggesting a gradual movement. The hand's motion is more pronounced, suggesting that the hand is holding the sink, rather than removing it. The sink's surface is more exposed, suggesting the sink'r position is more likely to be a re-entry or a replacement. The water level is still a little higher, suggesting there may be fewer people in the room, indicating that the sink has been tended to.
- Reference: The ladle is now in a different position, indicating a swift movement. It's closer to the center of the frame, tilted slightly more towards the camera, giving a clearer view of the bowl of the ladle which is shiny and seems well-used. The grip on the handle appears to have shifted, suggesting a dynamic action, possibly a rotation of the wrist. The background blurs with the motion, emphasizing the speed of the movement, but kitchen elements like the frying pan on the stove with sautéing contents and assorted bottles remain recognizable.

#### Sample 356 — During

- Similarity: 0.4253
- Prediction: In this frame, the kitchen is now more cluttered, with the kitchen counters and counters cluttered with food and other items. The kitchen's lighting is now dim, with a focus on the kitchen'd kitchen, which is likely a reflection of the kitchen. The counters are now more visible, with their surfaces indicating a more active or active cooking activity. The lighting is more dim, indicating that the kitchen has been preparing for the meal or cooking.
- Reference: In this scene, the pan contains a similar mixture, but the quantity of the liquid appears slightly reduced, indicating that some of the water content has evaporated due to heat. The green elements have a more wilted and cooked appearance, taking on a darker, more olive-like shade. The liquid has a few more visible bubbles, showing signs of gentle simmering, and the mixture is beginning to cling lightly to the wooden spoon, suggesting a slight thickening of the sauce or reduction in volume. The stirring motion seems to be gentle and consistent, maintaining an even cooking process.

#### Sample 359 — During

- Similarity: 0.3713
- Prediction: In this frame, the rag is now more firmly held, indicating that the water has been drained. The hands are now more engaged, demonstrating the presence of a squeezing motion, a sign of the effort to remove the soiled garment. The rag's surface is now slightly damper, revealing a more pronounced crease, reminiscent of scrubbing. The water's slickness is evident, implying that the soaked cloth is now able to absorb the water'n's moisture.
- Reference: The bin is now partially obstructed by a person's forearm, suggesting action in the process of discarding waste. The contents of the bin remain the same, densely packed and unaltered in the brief time lapse between the frames. There is no visible movement of the bin itself, indicating that the person's focus might be on another task, possibly related to cleaning or preparing to dispose of waste. The surrounding area, including the dish rack and countertop, appears unchanged, maintaining the context of ongoing kitchen use.

#### Sample 360 — During

- Similarity: 0.4085
- Prediction: In this frame, the hand is more firmly grasping the container, revealing a more streamlined appearance. The lid is now slightly more open, suggesting a closer view of the contents. The interior of the container is more spacious, with a wider range of items, including the lid's contents, indicating a greater focus on the container. The surrounding environment is more neutral, with the surrounding environment indicating the presence of a variety of items.
- Reference: The fridge door seems slightly more closed compared to the previous frame but is still not completely shut. The LED indicators remain visible and illuminated. The door handle has moved a bit towards its resting position, yet the black interior of the fridge is still partly visible. The reflections on the fridge surface appear slightly different, suggesting a subtle shift in the surroundings or lighting.

#### Sample 362 — During

- Similarity: 0.2085
- Prediction: In this frame, the rag is now more tightly held, with the fingers firmly pressed against the fabric. The grip is more firm, with a more pronounced grip on the fabric, indicating that the squeezing action has been a step forward. The fabric is now a bit more loose, with more of the fabric's surface exposed, resulting in a less brittle appearance. The rag's texture appears to be more supple, with some of the fibers shedding.
- Reference: Here, the water tap appears in a similar state as before, with water flowing from its spout. However, there's a subtle change in the positioning of the hands and the tap, indicating an interaction has occurred. The hands are now closer to the tap, implying an action in progress. The stream of water seems uninterrupted, with the liquid's surface tension visible as it flows and splashes into the basin, reflecting the kitchen's ambient light.

#### Sample 364 — During

- Similarity: 0.1178
- Prediction: In this frame, the hand is positioned on the counter, a position that is more apparent in the present frame. The hand is now positioned in a more streamlined position, indicating that the hand has been agitated. The hands are still firmly pressed against the counter and the hand appears to be attempting to move the hand. The focus is now on the hand, which is now more focused on the kitchen counter.
- Reference: In this frame, the sweet potato shows visible signs of being prepared for consumption. Slices or sections have been neatly cut, revealing its vibrant orange interior. The flesh looks soft, moist, and inviting, contrasting beautifully with the outer skin. The cuts are clean, indicating a sharp knife was used, and the edges of the slices glisten slightly, catching the light in a way that accentuates their fresh, juicy appearance.

#### Sample 365 — During

- Similarity: 0.3839
- Prediction: In this frame, the stove is still visible, with a hand motion indicating a person's presence. The person'd hand is now more focused on the surface of the stove, indicating that the burner is still active. The surface of this stove is now a bit more exposed, with the surface still a little more exposed. The stove's surface is now slightly more exposed to the light, implying that the flame is still present. The burner's position remains unchanged, with its position indicating the burner're still active, a sign of the burner still active in this frame.
- Reference: In this frame, the hob surface seems to have been partially cleaned, with less of the creamy substance visible than in the previous frame. The sheen from the moisture is still present, though it appears slightly reduced. The blue cloth is now more pronounced and is making direct contact with the surface, implying an active wiping action. Some of the surrounding kitchen items remain in view, including a wooden utensil which might have been used in cooking.

#### Sample 367 — During

- Similarity: 0.4367
- Prediction: In this frame, the jar of the saline is now in a more natural state, with the lid still slightly open, suggesting a gradual movement. The slurry is now a hazy, haze-free liquid, indicating that the ice has been poured into the jug. The water level is now slightly higher, suggesting that the water has been added to the mug, a sign of a steady flow of water. The surrounding environment is now more sterile, with a focus on the rim of the container, implying that the liquid has been placed in recirculation mode.
- Reference: In this frame, the cap's visibility is slightly better compared to the previous one. It can be discerned that it's closer to some household objects, including a rice cooker and some containers. The cap's orientation suggests that it might have been placed or dropped in a hurry. The environment still appears cluttered, but the cap now has a more central presence in the frame, indicating its significance.

#### Sample 368 — During

- Similarity: 0.2658
- Prediction: In this frame, the person's hand is more firmly grasping the plastic bag, indicating that the contents of the bag are being poured into the bag. The bag's contents are now more readily visible, with the lid revealing a sprinkling of liquid. The person'd hand is now more likely to be holding the bag, which is likely to contain a large amount of liquid, such as a liquid or powder. The contents of this bag are now positioned in a more streamlined position, implying that the bag is now being rolled up.
- Reference: In this scene, there is no direct view of the tomatoes as the can is absent from the visible countertop. However, the preparation for incorporating the tomatoes into a meal is ongoing. The countertop shows evidence of cooking activity with various items scattered around, such as a toaster, a crumpled plastic bag, and what appears to be the card of recipes or instructions. Without the presence of the tomato can, there's an implication that the tomatoes have been or are in the process of being transferred to another stage of the cooking process.

#### Sample 369 — During

- Similarity: 0.4707
- Prediction: In this frame, the rinsing spoon is now held in a more controlled position, with the water running through the surface of the spoon. The water's surface appears to be dripping, indicating that the hose has been rubbed into the spoon, allowing the water to drain. The hand's grip is more firm, implying that the spoon is being held in the hand'scooter's direction. The spoon's shape appears to have changed, revealing a slightly different appearance. The ribbing is more pronounced, resulting in fewer bubbles. The hands' movements are more relaxed, demonstrating the presence of the wringing spoon.
- Reference: In this scene, the same metal kitchen strainer is in focus, but there's a slight change in the angle, offering a different perspective. The strainer's perforations are more prominently visible, showing its detailed mesh design. There doesn't appear to be any visible residual water at the bottom in this frame. Surrounding items in the kitchen, such as the detergent and wooden cabinets, affirm its placement in a household kitchen environment. The strainer's handle, slightly more visible in this frame, shows signs of wear, consistent with frequent usage.

#### Sample 370 — During

- Similarity: 0.4297
- Prediction: In this frame, the towel is now more firmly held, with the hand motion indicating that it has been pressed against the table. The hand motion is more pronounced, indicating the hand is moving more quickly. The towel's surface is now slightly more exposed, with a slight crease in the center of the towel, suggesting that the hand has been more engaged. The fabric is now a bit more ragged, with some of the fabric separating from the table, implying that the towel has been placed in a more streamlined position.
- Reference: In this frame, the paper is in motion, evidenced by the blur and the shift in orientation from the previous state. The roll now appears slightly tilted, and the hand is grasping it more firmly, suggesting that a force is being applied. The paper's end is no longer neatly tucked in; it's starting to unravel, indicating the tearing process has begun. The image captures the very beginning of the disruption to the roll's integrity.

#### Sample 372 — During

- Similarity: 0.3695
- Prediction: In this frame, the bin's lid is now slightly more visible, indicating that it has been partially opened. The lid's position remains unchanged, suggesting that the lid is still in its current position. The object's shape is more apparent, suggesting a more gradual movement, implying that the bin is now partially open. The surrounding environment is more cluttered, suggesting the bin has been a bit more open.
- Reference: In this moment, the basket is not visible; the focus is on a person's lower body in motion, with the legs partially seen at the edge of the frame. The feet are clad in sandals, firmly planted on an orange-tiled floor that contributes to the warm color palette of the scene. The person's shadow and the floor tiles suggest a quick, perhaps downward movement, as if stepping or crouching, in the midst of an action that is not fully captured within this particular frame.

#### Sample 373 — During

- Similarity: 0.2524
- Prediction: In this frame, the hand is positioned on the counter, a position that is more apparent in the present scene. The hand is now positioned in a more streamlined position, indicating that the hand has been seated. The hands are still positioned, implying that the hands are now seated on the countertop, presumably to prepare for cooking. The kitchen is now more cluttered, with the kitchen's focus shifting to the kitchen, revealing a cluttered kitchen.
- Reference: The sandwich is now being actively cut by the knife held by the hand. The knife has made its way through the top layer of the bread, creating a visible incision. The contents of the sandwich, still mostly concealed, begin to peek through the slit. The pressure exerted by the hand and knife has slightly deformed the sandwich, compressing it a bit under the force.

#### Sample 376 — During

- Similarity: 0.3719
- Prediction: In this frame, the rinsing spoon is now in a more streamlined position, with the handle positioned slightly more vertically, indicating a steady stream of water. The hand's grip is more pronounced, suggesting a gentle movement, and the spoon's movements seem more deliberate. The water's surface appears to be a bit damp, suggesting that the water has been drained out of the spoon. The spoon' s surface is slightly more exposed, suggesting the water'ns presence is more concentrated. The ricotta-like texture of the steamed spoon' remains consistent with the boiled water's tanginess.
- Reference: In this frame, the cucumber is actively being rinsed under running water. Water droplets are seen cascading over its surface, making the cucumber appear glossy and wet. The person's hands are firmly holding the cucumber, ensuring it's thoroughly washed. The pressure from the water stream causes some reflections on the cucumber's skin, accentuating its curve and form.

#### Sample 381 — During

- Similarity: 0.3552
- Prediction: In this frame, the meat is now more seasoned and a little more tender, with the skin still slightly charred. The meat is still a bit sloppy, with a few pieces of meat still visible, indicating that the meat has been grilled. The chef's hand is now positioned in the center of the meat, presumably to ensure that the heat is evenly distributed. The skin is still slightly exposed, with some of the fat still visible. The pan is now slightly tilted, revealing a more smoky appearance, implying that the cooking process has been completed.
- Reference: In this frame, the spice application is more evident. The hand holding the spice jar is poised directly over the dish, displaying a deliberate and focused seasoning action. The spice particles are more visible on the dish, indicating a generous application. The density and spread of the spice specks suggest that the user is aiming for an even distribution across the dish, ensuring each portion receives an adequate amount of seasoning.

#### Sample 384 — During

- Similarity: 0.3759
- Prediction: In this frame, the refrigerator door is now positioned in a more streamlined position, with the lid positioned slightly higher than before. The interior of the refrigerator is now more spacious, with a wider range of items, including a glass container, a plastic bag, and a jar. The door's position is more cluttered, with items such as a pot, utensil, or other items occupying the space. The refrigerator's interior is now slightly more open, with more items ranging from a small kitchen sink to a refrigerator drawer to dozens of other items.
- Reference: The milk jug is now captured mid-air, in the process of being transported. Its orientation is slightly tilted, suggesting movement, and the handle is firmly grasped, indicating it is being carried with purpose. The jug's cap appears to be secured, and there is no evidence of spillage. The background is a blur, with the refrigerator interior and its contents such as a carton of eggs and other containers providing a static contrast to the milk jug's motion.

#### Sample 386 — During

- Similarity: 0.4717
- Prediction: In this frame, the fish is now more closely positioned, with the skin separating from the fish's surface. The fish'shield is now slightly more exposed, with a more pronounced ridge of skin visible. The skin is now a little more exposed to the water, suggesting that the fish has been steamed. The hands are now more engaged in the process, indicating that the salmon has been fully cooked.
- Reference: In this moment, the meat is being actively manipulated, with the fingers pressing into the flesh, causing slight indentations. This suggests the meat is soft and pliable, further indicating its freshness. The lighting remains consistent, casting shadows that accentuate the contours of the meat and the fingers’ imprint. The background blur suggests a swift movement, possibly a transition from one place to another. The proximity of the fingers to the meat also suggests careful handling, perhaps to prevent it from falling or to control its placement.

#### Sample 391 — During

- Similarity: 0.4745
- Prediction: In this frame, the rinsing pan is now more streamlined, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's surface is now a bit more soiled, resulting in a more uniform appearance of the scrubbing action. The ricotta-colored cloth is now visible, revealing a smoky, spongy appearance. The hand's grip is still firmly held, implying that the rag is being rubbed.
- Reference: In this frame, the chopping board's surface has significantly more water on it, with larger puddles forming in certain areas. The water droplets have spread further, covering more of the board's area. The color distinction between the wet and dry areas remains noticeable, with the wet sections showcasing a deeper shade of blue, possibly indicating that more water has been added or that the existing water has spread.

#### Sample 392 — During

- Similarity: 0.3439
- Prediction: In this frame, the hand is more firmly grasping the door, revealing a gaping gap in the middle of the door. The door's hinges are now slightly wider, suggesting a more gradual movement, indicating that the door is open. The hand's angle is slightly more angled, suggesting that the hand has been able to grasp the door and open it. The interior of the cabinet is now more cluttered, implying a cluttered kitchen or dining area. The kitchen's lighting is now dim, suggesting the kitchen'd lighting is more dim.
- Reference: The tea towel now is in the midst of being adjusted by a hand, which has caused a shift in its position. The striped pattern is slightly more bunched and creased, indicating movement. The fingers are spread wide, possibly in the initial stage of grasping or smoothing out the fabric. The motion appears to be directed upwards or towards the back of the drawer, signaling an attempt to either fully remove or better organize the tea towel within the space.

#### Sample 397 — During

- Similarity: 0.3835
- Prediction: In this frame, the kitchen sink is now in a more streamlined position, with the blades positioned in contrasting positions. The kitchen's layout is more cluttered, with a focus on the kitchen counter and the kitchen table, indicating that the kitchen has been re-opened. The lighting is dim, with ambient lighting indicating a slow motion. The counter's lighting is more dim, implying that the lighting is reflected in the kitchen. The sink's surface is slightly more exposed, suggesting that the sink is still in the same position. The countertop's color is more vibrant, suggesting a kitchen setting. The surface of the sink'r surface is more reflective, suggesting the sink has been moved. The blades are now
- Reference: The salt container seems to have been repositioned slightly. While it remains amidst other kitchen items, the shift in its placement suggests that it might have been moved or nudged. The cap appears to remain closed, indicating that the salt inside hasn't been dispensed recently in this frame. The scene appears busier than in the previous frame, perhaps indicating progression in the cooking or preparation process.

#### Sample 398 — During

- Similarity: 0.4833
- Prediction: In this frame, the rinsing spoon is now held in a more streamlined position, with the handle positioned slightly more vertically. The water's movement is more pronounced, with a broader angle indicating the presence of a larger portion of the spout. The hand's grip is more relaxed, with more movement indicating a deeper rinse. The ricotta is now more firmly held, with its surface exposed, suggesting a gradual process. The hands' movements are more relaxed and agitating, indicating that the wrung spoon is still soaking wet.
- Reference: In this frame, the jar clip top is now in a more open position, with the metal clasp completely disengaged. This provides clear access to the interior of the jar. The hands appear to be manipulating or inspecting the rubber seal and the metal clip mechanism. The orientation of the jar indicates a focused attention on the top component, possibly to ensure its cleanliness or functionality.

#### Sample 401 — During

- Similarity: 0.1684
- Prediction: In this frame, the hand is more firmly held, indicating that the hand has been a bit more engaged in the action. The hand's movement is more evident, implying that the person is holding the hand, presumably to prevent the hand from moving. The person's posture is more relaxed, suggesting that the hands are more engaged. The object's shape is more apparent, suggesting a more gradual movement. The hands are still positioned in a slightly curved position, suggesting the hand'd movement is less pronounced. The overall posture is less blurred, suggesting an effort to maintain a steady grip on the hand.
- Reference: In this scene, the hardwood floor continues to display its polished surface and warm tones. The lighting seems consistent with the previous frame, highlighting the natural grain and color variations in the wood planks. The sweeper has interacted with the floor, as evidenced by a few streaks left by the cleaning implement, showing that some of the loose particles have been gathered or displaced. However, there remains a scattering of debris and dust not yet collected by the sweeper.

#### Sample 403 — During

- Similarity: 0.3443
- Prediction: In this frame, the knife is now positioned in a more secluded position, presumably a holder for a knife. The knife's handle is now more firmly held, indicating that the knife has been inserted into the knife' blade. The blade's surface is slightly curved, suggesting that the blade is a bit looser than before. The hand's grip remains firm, implying that the hand is holding the knife, a gesture that may indicate that the cutting action is imminent. The kitchen counter appears to be a little more cluttered, with the knife still pointing to the edge of the knife.
- Reference: The onion slices have been further processed in this frame. They are now laid out on what appears to be a piece of bread or perhaps a base for a pizza or flatbread. The slices are arranged to cover most of the surface area of the bread, slightly overlapping in places. The arrangement is deliberate, ensuring even distribution and coverage. The onions still retain their fresh appearance, with the edges looking slightly translucent, a characteristic feature when onions are thinly sliced.

#### Sample 406 — During

- Similarity: 0.4187
- Prediction: In this frame, the bin's lid is now slightly more visible, with the lid positioned in a more horizontal position, indicating that the person is holding the bin. The lid's position is more apparent, with a slight movement, implying that the lid is still in the position of its original position. The bin'd lid remains in the same position, with its handle still firmly held, presumably a reversal of the previous position.
- Reference: In this frame, the strainer is still held, but now its bottom faces more towards the ground. The orange-yellow liquid that was once prominent in the strainer has lessened considerably, and the strainer appears more vacant. While traces of the liquid remain, it's evident that a substantial amount has already been poured out or drained. The strainer's white surface now contrasts with the remnants of the liquid, highlighting the empty spaces between the fine mesh.

#### Sample 408 — During

- Similarity: 0.3626
- Prediction: In this frame, the butter is now in a more pronounced state of being poured into the container. The hand is now more firmly grasping the butter, indicating that the butter has been poured onto the container, resulting in fewer and smaller pieces of butter. The butter's consistency is more consistent, suggesting that the blending process is a step forward. The tangy texture of the butter appears to be a result of the hand's action, implying that the knife is now positioned in the center of the container to ensure that the ingredients are evenly distributed.
- Reference: In this frame, the person's hand has made progress in opening the bottle. The cap seems to have been slightly loosened, allowing for the content within the bottle to be accessed soon. The fingers grasp around the neck of the bottle, exerting a gentle pressure indicating the act of unscrewing the lid. The base of the bottle remains firmly over the tortilla, poised to dispense its contents.

#### Sample 410 — During

- Similarity: 0.4949
- Prediction: In this frame, the jar of the cheese is now in a more streamlined state, with the lid still firmly attached to the plastic. The hand is now able to grasp the cheese, revealing a sprinkling of cheese on the surface. The jar's contents are now more visible, with a distinct, overlapping appearance. The cheese's texture is more consistent, with its texture contrasting with the rest of the slough. The hands are now positioned in resemblance to the cheese'd texture, indicating that the cheese has been incorporated into the cheese.
- Reference: The scene shifts slightly to show a hand actively engaged in the act of sprinkling sweetcorn onto the pizza. The kernels are in a state of descent, some possibly caught in the very moment of leaving the can, while others are likely just making contact with the saucy surface below. The sweetcorn's distribution is uneven, with a cluster gathering more densely in one area, indicating the initial point of contact from the can. The act of sprinkling is captured dynamically, with the potential for motion blur on some kernels indicating their rapid journey onto the pizza.

#### Sample 415 — During

- Similarity: 0.4865
- Prediction: In this frame, the tray is now more visible, with a slightly more rounded shape, indicating a more gradual movement. The person's hand is now positioned in the middle of the tray, presumably a hand holding the tray. The tray's surface is slightly more exposed, suggesting that the person is holding the container, rather than merely removing it. The object's shape is more pronounced, suggesting a gradual movement, and the tray'd shape is less noticeable.
- Reference: The lunch box is now opened slightly, revealing more of its interior. Through the opened part, it's noticeable that there is a light-colored content, which might be a type of food, possibly a sandwich or wrap given its layered appearance. The label on the transparent lid is more apparent in this frame, and the red hue of the box is still visible.

#### Sample 417 — During

- Similarity: 0.4629
- Prediction: In this frame, the scrubbing brush is now more firmly held, indicating that the water has been drained. The hand is now positioned in the position of the brush, presumably a hand holding the brush. The brush's surface is now slightly more exposed, revealing a more pronounced, rounded shape. The water's movement is more sporacious, implying that the brush is agitating the water, allowing the brush to move more quickly. The squeezing motion is more noticeable, demonstrating the presence of a brush or a swivel.
- Reference: In this instance, the chopping board appears closer to the camera, occupying more of the frame and giving a clearer view of its condition. The person's right hand is now visible, using a sponge to scrub the board's surface, which remains drenched in soapy water. The downward angle of the board remains the same, facilitating the rinsing process. The presence of soap suggests active cleaning, and the board's wear is even more apparent here, with the scratches and cut marks crisscrossing its surface, telling the tale of its extensive use in a kitchen.

#### Sample 420 — During

- Similarity: 0.4839
- Prediction: In this frame, the bag is now more firmly held, with the lid still firmly attached to the plastic bag. The hand's movements are more deliberate, indicating that the bag has been placed in a more streamlined position. The bag's contents are more visible, with a rounded edge and a slightly more rounded shape. The person's hand is more pronounced, suggesting that the bags are being pushed or pressed against the bag'd surface. The bags' surface is more exposed, implying that the contents are being pulled out of the bag.
- Reference: In this scene, the freezer door has moved slightly more open compared to the previous frame. The person's hand is repositioned, indicating movement. The angle of the frozen item in the hand has changed, providing a clearer view of what appears to be a zip-locked bag of food. The inner compartments of the freezer door are more visible now, with the slots designed to hold items such as ice trays or small frozen goods. The shadow cast by the door on the freezer's contents has shifted, indicating a change in the lighting angle or intensity.

#### Sample 423 — During

- Similarity: 0.4903
- Prediction: In this frame, the rag is now more tightly held, with the fingers firmly pressed against the fabric. The grip is more firm, with a more pronounced grip on the fabric, indicating that the squeezing action has been intensified. The fabric is now a bit more loose, with more of the fabric separating from the fabric and forming a clump. The creases are more noticeable, with some of the fibers shedding.
- Reference: In this frame, the cloth is being held under the stream of water from the faucet. It seems that the person is aiming to rinse the cloth, ensuring any dirt or soap is washed away. The fabric appears to be thoroughly saturated, with water visibly cascading off it. The way it's held under the faucet suggests that the person is making sure every part of the cloth gets rinsed.

#### Sample 427 — During

- Similarity: 0.3963
- Prediction: In this frame, the hand is more firmly grasping the bowl, revealing a more rounded shape. The bowl's surface is slightly blurred, suggesting a movement, indicating that the bowl is still in its original position. The hand's motion is more consistent, suggesting that the hand has been a bit more hesitant to grasp the bowl. The kitchen counter is now positioned in a slightly different position, implying that the kitchen is now more open. The palette of the bowl'd contents is more vibrant, suggesting the presence of a variety of foods, including dairy, fruit, and vegetables.
- Reference: Now, the refrigerator door is fully open, revealing more of its contents. On the door's lower shelf, there’s a glimpse of what seems to be bottled condiments, partially obscured by the open door. The second shelf of the door holds a mix of yellow and red fruits, possibly bananas and apples, held in a white wire basket, suggesting an attempt to keep fruits within easy reach. The interior light remains off, and the lower shelves inside the refrigerator are still not completely visible, but there's a suggestion of crisper drawers possibly containing more produce.

#### Sample 429 — During

- Similarity: 0.4915
- Prediction: In this frame, the scrubbing tool is now in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been sprayed on the surface. The hand's grip is more firmly held, allowing the rinsing motion to be more precise. The spout's surface appears to be a bit damper, suggesting that the lint is still present. The water's movement is more consistent, implying that the soap has been washed away the soap residue. The soap's consistency is more uniform, suggesting a deeper cleaning action.
- Reference: The bowl is now placed within the confines of the frying pan, capturing more of the viewer's attention as the hand holds it more securely. The presence of soap bubbles has diminished, revealing more of the bowl's inner surface, but a frothy cluster remains at the bottom, covering the center. The hand appears to be in the midst of a gentle swirling motion, likely aiding in the removal of the soapy solution from the bowl's surface. The grip on the bowl is firm, with the thumb pressing against the outer edge to stabilize it.

#### Sample 433 — During

- Similarity: 0.2399
- Prediction: In this frame, the door is now in a more streamlined position, with the lid still slightly open. The door's position is more pronounced, suggesting that the person is attempting to open the door, or simply removing the lid. The person's hand is still motionless, suggesting a slight movement, but the door remains open.
- Reference: Here, the cloth seems to be in a state of being actively squeezed. The fingers are pressing into the material, which is gathered and twisted to wring out the liquid. This action has created darkened wet patches on the cloth's surface, implying that the moisture is being expelled. The cloth's twisted sections are tightly compressed, and the surrounding area suggests a more vigorous motion compared to the previous state, reflecting a more dynamic phase of the wringing process.

#### Sample 436 — During

- Similarity: 0.4595
- Prediction: In this frame, the knife is now in a more streamlined position, with the blade positioned in contrasting positions with the rest of the kitchen. The knife's handle remains stationary, indicating that the knife has been inserted into the kitchen, allowing the knife to be positioned more accurately. The blade's position remains unchanged, implying that the blade is now positioned slightly away from the kitchen counter. The kitchen counter's surface is now more cluttered, revealing a cluttered kitchen area, with a kitchen sink and counter top, a counter top and counter, and a table. The counter top is now slightly elevated, displaying a variety of items, including a pot, sink, and counter.
- Reference: In this snapshot, the peeler has been set down on the cutting board, its handle extending towards the bottom edge of the frame. It lies adjacent to a vividly colored eggplant peel, showcasing the contrast between the peeler's utilitarian design and the organic curvature of the peel. The blade end of the peeler is slightly obscured by the discarded peel, indicating that it has been recently used. The surrounding area is sparsely littered with small flecks of peel and moisture, possibly from the eggplant, suggesting a scene of ongoing food preparation.

#### Sample 437 — During

- Similarity: 0.2657
- Prediction: In this frame, the sink has been lowered to a more natural position, with the water edging towards the edge of the basin. The hand is now more likely to be holding the sink, indicating that the water has been removed from the basin, thereby removing any remaining debris. The water's surface remains a little damp, suggesting that the sink may be a bit damp, but the water'n's presence is still present. The sink's current state of motion is more apparent, with a hand motion indicating a steady stream of water. The surface of the sink is now slightly tilted, suggesting a gradual movement, allowing the water to flow more smoothly. The surrounding area is now less visible, implying
- Reference: The pepper pieces remain on the wooden chopping board, but they have been slightly rearranged or shifted, possibly due to some movement or external interference. They seem to be closer to the edge of the board, hinting at a potential transition in their placement. Their bright yellow color still stands out prominently, showcasing their freshness.

#### Sample 439 — During

- Similarity: 0.4891
- Prediction: In this frame, the rag is now more firmly held, indicating that the water has been sprayed on it. The hand is now positioned in a more soiled position, presumably a rinsing motion, allowing the risins to drain. The rag's surface is now slightly damper, revealing a slightly different appearance, contrasting with the scrubbing action. The water's sludge is now less concentrated, suggesting that the lint is still present.
- Reference: In this frame, the towel is in direct contact with water, as evidenced by the splash and the distortion of light around the submerged section. The person's hands are more dynamic, with fingers spread as if vigorously shaking or washing the towel. The fabric appears to be absorbing water or being rinsed, suggested by the towel's darker coloration where the water hits it, signifying a saturation of the material. This action is causing water to ripple and splash, further indicating the forceful movement being applied to the towel.

#### Sample 441 — During

- Similarity: 0.4581
- Prediction: In this frame, the door is open, revealing a more streamlined interior. The door's handle is more pronounced, suggesting a closer grasp of the door, indicating a greater grasp of its contents. The interior of the refrigerator is now more cluttered, with the door'd interior revealing more of the items. The refrigerator's interior is now cluttered with items, including a glass container, a plastic bag, and a jar. The kitchen's counters are now more visible, with a clearer view of the kitchen counters and the door.
- Reference: The microwave door has been opened further compared to the previous state, revealing more of its light gray interior and the glass turntable within. The person's hand is now actively engaging with the handle, suggesting motion in the process of opening the door. The shadow cast by the pitcher has shifted slightly, indicating a change in the door's angle. The kettle and power cord remain stationary, serving as static points of reference amidst the dynamic action of the door opening.

#### Sample 443 — During

- Similarity: 0.4373
- Prediction: In this frame, the spoon is now positioned in a more spherical position, indicating that the spoon has been agitated. The spoon's surface is now slightly curved, revealing a smooth, rounded surface. The object's shape is more uniform, forming a rounded shape, implying that the object is being handled. The hand's motion is more pronounced, demonstrating a slight movement in the spoon'd direction.
- Reference: In this frame, the liquid's surface exhibits more motion, evidenced by the formation of ripples and waves around the beaters, a consequence of the mixer's increasing speed or more vigorous movement. The color remains consistently yellow, but the texture appears slightly aerated, with small air bubbles beginning to emerge. This suggests that the liquid is being whipped, increasing in volume, and becoming lighter as air is incorporated. The beaters are coated with a thin layer of the mixture, indicating its adherence and possibly a slight thickening in consistency.

#### Sample 444 — During

- Similarity: 0.4254
- Prediction: In this frame, the knife is now positioned in a more natural position, with the blade pointing downwards. The hand's grip remains steady, indicating that the knife has been pressed against the blade, a gesture that may indicate a slight movement. The knife's surface is slightly curved, suggesting that the blade is still firmly attached to the blade. The blade's edge remains firmly held, suggesting a sharp edge. The fingernail's position remains unchanged, implying that the hand is now holding the knife.
- Reference: In this frame, the whetstone remains in a vertical position, consistent with the previous image. The light-colored side is still facing upwards, indicating the finer grit is being used for sharpening. While the stone remains dry, there is a noticeable increase in the reflection of light, especially around the area where the blade interacts with the stone. This might suggest that the stone has accumulated fine metal particles or that there is increased friction between the blade and the stone.

#### Sample 456 — During

- Similarity: 0.3627
- Prediction: In this frame, the rinsing pot is now held in a more streamlined position, with the handle positioned slightly more vertically. The water flows more slowly, resulting in fewer bubbles, which are likely caused by the squeezing motion. The ricotta-colored surface of the pot is more reflective, indicating that the water has been drained. The person's hand is more likely to be holding the nozzle at the bottom of the hose, allowing the water to flow more quickly. The faucet's current position is more horizontal, revealing a different angle of the waterflow. The hand's angle is more angled, implying that the wand is being r
- Reference: In this frame, the decorative coffee machine is now partly obscured by a hand that's placed near or on its base, suggesting someone is interacting with or moving it. The machine retains its vibrant colors and ornate patterns, and the label or marking on the front remains indistinguishable. It's worth noting that the top portion of the coffee machine, which previously appeared open, is no longer in full view, possibly due to a change in the angle or the hand's positioning.

#### Sample 458 — During

- Similarity: 0.4130
- Prediction: In this frame, the pan is now in a more streamlined position, with the handle still positioned in the center of the pan, indicating a steady stream of water. The person's hand is now more firmly held, implying that the pan has been soiled. The pan's surface appears to be a bit damp, suggesting that the water has been running through the pan. The water's evaporation is visible, forming a hazy, smoky haze.
- Reference: In this scene, the tap remains unchanged from its initial state; the lever is still in the off position, maintaining its parallel orientation with the countertop. The tap's shiny surface shows no signs of moisture or disturbance, indicating that it has not been activated between the first and second frames. The surrounding area, including the sink and the dishes, does not show any change that would imply water has been dispensed.

#### Sample 459 — During

- Similarity: 0.2604
- Prediction: In this frame, the hand is now more firmly held, indicating that the hand has been agitated. The hand is more likely to be holding the knife, which is likely to have been a part of the kitchen or dining area. The knife's surface is slightly blurred, suggesting that the knife is still in its position. The blade's position remains unchanged, implying that the blade is still positioned in the kitchen. The kitchen's lighting is now dim, suggesting a more natural setting for the knife.
- Reference: In this scene, the can is now held aloft by a human hand, gripped firmly around its body. The lid is in a further state of detachment, peeled back to expose more of the contents within, which are indeed small, spherical, and uniformly sized, corroborating the initial presumption of peas or corn. The opening of the can now allows for a clear view into the interior where the contents are packed in liquid, likely brine or syrup, which is typical of canned produce.

#### Sample 460 — During

- Similarity: 0.3768
- Prediction: In this frame, the pan is still positioned in a position that is a bit more cluttered, with the pan's surface revealing a more streamlined appearance. The person's hand is now more focused on the pan, indicating that the person is preparing to use it. The pan'd surface is now a little more ragged, with a few spots of rust and a slight smudge on the surface. The surface is more bare, with only a small amount of visible residue. The kitchen counter is now slightly more crowded, with less space for the items on the counter. The counter's lighting is now dim, with no visible reflections. The stove's setting is still visible, with its
- Reference: In this frame, the focus is marginally clearer, showing the tap in a semi-active state. The blur has somewhat subsided, hinting that the movement has slowed down, with the hand retreating from the tap. The stream of water is still indiscernible, possibly due to the water flow being greatly reduced as the tap approaches the off position. The immediate environment of the tap shows signs of recent activity, with water droplets and splashes visible around the sink area, reflecting the previous interactions with the water flow.

#### Sample 463 — During

- Similarity: 0.4636
- Prediction: In this frame, the pan is now in a more natural state, with the lid still slightly open, suggesting a slight movement. The pan's surface is more exposed, indicating that the cooking process has been completed. The kitchen's lighting is now more dim, suggesting that the pan has been agitated. The pot's lid remains in place, suggesting the pan'd contents are still present. The surface of the pan appears to be a bit damp, suggesting it may be preparing for cooking. The rim of the pot is now slightly lowered, suggesting there may be some movement in the pan.
- Reference: In the second frame, the surroundings of the switch become slightly more discernible, but the state of the switch is still not entirely clear. The image features a hand near what appears to be the kitchen countertop or appliance interface, suggesting some interaction might be occurring. There's an indication that the hand might be grasping or reaching for something, possibly the switch. However, the exact state, whether it's turned on or off, remains ambiguous due to the blurriness.

#### Sample 467 — During

- Similarity: 0.4668
- Prediction: In this frame, the cheese has been sliced in half, with the knife still pointing at the slice, indicating that the knife has been cut. The knife's edge is now slightly curved, suggesting that the slice has been partially cut. It is now positioned in the center of the slice and the knife'd edge is still visible, implying that the cutting has been completed. The slice has now been inserted into the cheese, revealing a smooth, rounded surface. The cheese's surface is now more exposed, demonstrating the presence of a knife' blade, which is now visible in the middle of the cut.
- Reference: The sandwich remains on the same plate, but there's a noticeable shift in its position. One of the triangular halves has been slightly shifted away from its counterpart, suggesting an attempt to pick it up or adjust its position. A few crumbs can be observed near the sandwich, indicative of the movement. The grainy texture of the bread is even more pronounced in this frame, further emphasizing its whole grain nature.

#### Sample 468 — During

- Similarity: 0.4426
- Prediction: In this frame, the rinsing spoon is now held in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's surface is now more rounded, with a wider angle, allowing the spoon to be more agitated. The hand's grip is more firm, ensuring that the spoon remains firmly in place. The spoon's shape is more pronounced, with its tips angled slightly downwards, implying that the spout is being rubbed. The ribbing is more gentle, resulting in fewer drops of water.
- Reference: Here, the bell pepper is more engulfed in water, evident by the sheen over its surface that suggests a steady flow is cascading over it. The water droplets have merged into a thin film, glossing the pepper and enhancing its bright red coloration. The hand adjusts its hold, now cradling the pepper from the top, allowing water to wash over more of its surface. The angle at which the water strikes the pepper has changed slightly, indicating movement and a more thorough rinse.

#### Sample 469 — During

- Similarity: 0.4960
- Prediction: In this frame, the hand is positioned in a more relaxed position, indicating that the hand has been preparing the chicken. The hand is now more agitated, demonstrating the presence of the chicken's meat, which is a contrasting color to the previous image. The chicken'd surface is now slightly more exposed, suggesting that the chicken is still preparing for cooking. The hands are now more engaged in the action, implying that the hands are preparing to cook.
- Reference: In this frame, the cover is noticeably being interacted with, as evidenced by the hand positioning around its sides. The cover's surface still displays a sheen, reinforcing the notion that it could be a reflective material. The curvature of the cover is more prominent here, hinting at its domed shape. It appears to be slightly tilted or in motion, possibly due to the person's actions. Adjacent to the cover, one can identify a stove's burner, indicating the cover's position relative to the cooking surface.

#### Sample 470 — During

- Similarity: 0.2728
- Prediction: In this frame, the bottle is now in a more natural state of motion, with the hand positioned in the middle of the bottle. The hand's movements are more pronounced, suggesting that the bottle has been agitated, indicating that the liquid has been added to the bottle, a process that may have been initiated. The bottle's contents are still in the same state as in the previous frame, suggesting a gradual movement. The liquid content of the container is less evident, suggesting the liquid may have remained in the bottle'd container.
- Reference: In this moment, the plug is further removed from the outlet compared to the previous frame. The individual's grip on the plug is firm, indicated by the slight compression of the yellow rubber gloves around their fingers. This suggests a deliberate action, likely the act of unplugging. The plug's prongs are more visible now, and it appears to be a standard, non-grounded two-prong plug. The background remains unchanged, crowded with kitchenware and items, which are out of focus.

#### Sample 473 — During

- Similarity: 0.4256
- Prediction: In this frame, the hose is now in a more natural state, with the water slicker's surface exposed, indicating that the water has been drained. The hand's grip is now more firm, suggesting that the nozzle is being held in place. The water's flow is more pronounced, suggesting a gradual movement, implying that the stream of water is a slurry. The hose's current position is more stable, presumably due to the increased pressure on the spout. The current position of the holder is more apparent, a sign that the hand is now attempting to remove the spigot.
- Reference: In this frame, the action of opening the bottle progresses as the cap appears to be in the midst of being twisted off. The hands are positioned with one hand stabilizing the bottle while the other seems to be applying a twisting force to the cap. The cap itself shows a slight gap between it and the bottle's neck, indicating that the seal has been broken and the cap is partially unscrewed. The setting remains unchanged with kitchenware in the background, and the bottle still appears undisturbed content-wise, with no spillage present.

#### Sample 480 — During

- Similarity: 0.4679
- Prediction: In this frame, the scrubbing brush is now more firmly held, indicating that the water has been drained. The hand is now holding the rinsing spoon, presumably a risina or a small amount of soap, and the nozzle is now positioned in the center of the holder. The ricotta is now slightly more agitated, suggesting that the lint is dripping. The water level is now less effected, suggesting a more gradual movement of the brush. The brush's surface is now clearer, suggesting the brush is still able to remove the soap.
- Reference: Now, the liquid washing up is being actively applied onto the sponge. The stream of the liquid can be discerned as it makes contact with the sponge, creating a wet spot. This wet spot reflects light differently than the rest of the sponge, indicating that the sponge is beginning to absorb the liquid.

#### Sample 482 — During

- Similarity: 0.4312
- Prediction: In this frame, the foil is now more exposed, with the foil exposing more of the foil. The person's hand is now positioned in the middle of the tray, indicating that the foil has been placed in the oven. The foil is still firmly wrapped in foil, implying that the person is preparing to eat the foil, which is likely to be a meal. The creases on the foil are slightly more noticeable, suggesting that the individual is attempting to slicing the foil in a more conventional fashion.
- Reference: In this frame, the packaging of the lighter meat, possibly chicken, is being interacted with. A pair of hands can be seen grasping the package, where one hand holds the body of the package while the fingers of the other hand appear to be prying or pinching at a corner of the seal. Despite this, the plastic wrapping remains mostly undisturbed, and the meat inside the package is still concealed. There's no sign of the seal being fully breached at this point.

#### Sample 485 — During

- Similarity: 0.3845
- Prediction: In this frame, the hand is more firmly grasping the door, revealing a gaping gap in the middle of the door. The door's hinges are now slightly angled, suggesting a more gradual movement, indicating that the door is open. The hand's motion is more consistent, suggesting that the hand has been able to grasp the door and open it. The object of the hand'representative action is more evident, suggesting the door has been opened.
- Reference: In this scene, the milk carton has been released from the person's grasp and is captured in mid-descent towards the floor. The green carton with its label is in a vertical orientation, with the top side facing downward, suggesting it may not have been securely closed. The background is less cluttered here, featuring a broom and a dustpan against a wall, and what appears to be a container lid on the floor, indicating that the carton is likely falling in an area adjacent to the kitchen or a utility space.

#### Sample 490 — During

- Similarity: 0.3577
- Prediction: In this frame, the person is attempting to open the plastic bag. The person's hand is positioned in the middle of the bag, a position that indicates the person'd grasping the bag. They are now able to grasp the bag's contents, indicating that the bag has been opened. The bag'es packaging is now more visible, with the contents of the plastic bags indicating the person has grasped the bag and is preparing to open it.
- Reference: In this moment, the tortilla is being maneuvered back towards its original packaging. The hand's grip has shifted, now supporting the tortilla more from beneath, with the fingers curving upwards, cradling its base. The tortilla's flexibility is evident as it displays a gentle droop, arching downwards due to gravity. Its surface is still unblemished, and it retains the circular shape characteristic of a classic tortilla, highlighting its apparent softness and readiness for use.

#### Sample 495 — During

- Similarity: 0.2758
- Prediction: In this frame, the hand is now more firmly held, indicating that the hand has been positioned. The hand is more asymmetrical, implying that the person is holding the hand, a position that would be appropriate for a quick glance. The hands are now more aligned, suggesting that the hands are positioned in a more natural position. The palm of the hand appears to be slightly tilted in the direction of the person's movement, suggesting a slight shift in the hand's position.
- Reference: The plug remains in a similar position, but now it appears to be slightly askew, suggesting that a pulling force has been applied. The prongs are still engaged with the socket, but the angle at which the cord extends has shifted, becoming more pronounced towards the right, indicating movement. The environment is consistent with the previous frame, with the wooden chair leg, white skirting, and yellow tiling composing the surroundings. The plug's facade is more visible, and the socket looks standard with no distinct features or damage.

#### Sample 496 — During

- Similarity: 0.3191
- Prediction: In this frame, the towel is now more firmly held, with the hand motion indicating that it has been pushed or pulled. The hand is now positioned in a more pronounced position, indicating the hand is moving. The towel's surface is now slightly more exposed, with a slight change in the shape of the towel, suggesting that the hand has been more engaged. The fabric is now less revealing, and the fabric is more patterned, implying that the towel has been pulled or pulled from the table.
- Reference: In this scene, the popcorn bag is held steadily, likely immediately after being shaken, as the hand and the bag are less blurred compared to the previous frame. The text and graphics on the bag are now legible, showing icons and instructions for proper microwave use. The top of the bag appears slightly inflated, a sign that the popping process has occurred or is nearing completion. The person's grip on the bag is firm, their thumb pressing down on the front face, possibly feeling for the consistency of the popped kernels inside.

#### Sample 5 — After

- Similarity: 0.4814
- Prediction: The kitchen counter is now more cluttered, with the counter's surface a little more bare and cluttered. The counter'dishes are now more visible, with a more streamlined appearance and a broader range of items, including a white towel, a dish towel, and utensils. The kitchen's lighting is now dim, with only a few lights visible, indicating that the kitchen is still occupied. The white and blue lighting is reminiscent of a kitchen setting, with bright lights and contrasting patterns.
- Reference: This perspective offers a broader view of the floor, revealing the edges of the tiles and the base of the kitchen cabinets. Here, the floor seems to have more noticeable dark spots and streaks of moisture from the cleaning process. These marks are irregularly shaped, with some areas appearing to have been missed by the wiping, leading to an inconsistent sheen on the tile surface. The light reflection is more pronounced, making the damp areas stand out against the matte, drier parts of the floor.

#### Sample 6 — After

- Similarity: 0.4321
- Prediction: The scrubbing motion is more gradual, with the water running more smoothly. The water is now dripping from the sink, indicating that the water has been sucked out. The kitchen sink is still awash in a lukewarm state, with a steady stream of water circulating around the sink. The rinsing motion is reminiscent of a water bath, with water splashing across the surface of the sink and the water splatters.
- Reference: The chopping board is further cleaned, with the wet sheen more pronounced than in the previous frames, suggesting that more of the board's surface area has been covered by the cleaning process. The hand holding the sponge continues to scrub the board, focusing on its left side. There seems to be less visible soap foam, which could mean that the cleaning process is nearing its end, or the soap has been rinsed off more effectively.

#### Sample 8 — After

- Similarity: 0.2542
- Prediction: The hand is now positioned in the position of the hand, a position that would suggest a gradual change in the hand's position. The hand'd position is consistent with the hand holding the pot, which is likely a sign of the final phase of the process. The resulting liquid content is less evident, but the hand still maintains the grip on the pot. The surrounding environment is still a little damp, with the surrounding environment indicating that the pot is still in use.
- Reference: The toaster's lever is now completely depressed, with the slots wholly accommodating the bread for toasting. A radiant, warm orange glow emanates from within the slots, indicative of the fully active heating elements. The surrounding countertop captures the gentle light spill, creating a cozy ambiance. The power indicator light is now brightly illuminated, confirming that the toaster is in full operation. A slight hint of steam or heat waves can be seen rising, testifying to the toasting in progress.

#### Sample 15 — After

- Similarity: 0.3594
- Prediction: The jar is now more fully frosted, with the lid still firmly closed. The hand's motion is more pronounced, indicating that the jar has been partially frozen. The rim of the jug is now slightly curved, suggesting that the lid is now partially shattered. The lid is still frothy, suggesting a gradual release of the liquid, which may indicate that the liquid has been absorbed into the mug.
- Reference: The stock now appears thicker in consistency as it clings to the sides of the glass container when tilted. The surface of the stock shows waves and ripples, suggesting that it has been stirred or agitated recently. The color remains a consistent pale yellow, but there's a more pronounced sheen on the surface, potentially indicating a higher fat content or the reduction process. The glass is less full compared to the first frame, hinting at some level of evaporation or usage of the stock in between the frames.

#### Sample 20 — After

- Similarity: 0.3508
- Prediction: The paper is now more firmly held, with the hands positioned in a more slender position, indicating that the paper has been pressed into place. The paper's surface is more exposed, with a creased edge and a slight crease in the middle. The hand's movements are more deliberate, implying that the hand is attempting to grasp the paper, a process that may have been initiated by the person who is holding it. The hands are still firmly grasping the paper and the paper is still pinned to the paper.
- Reference: Here, the yogurt's state has further evolved. It has been placed down with the hand retracting from the action, implying that the positioning of the yogurt container has been completed. The container rests at an angle, distinct from its previous upright position, which contributes to a sense of completion or finality in the sequence of arranging the containers. The kitchen setting serves as a passive backdrop, with the light reflecting off the surface indicating a well-lit environment.

#### Sample 21 — After

- Similarity: 0.4634
- Prediction: The rinsing action is more streamlined, with the leaves wilting more vigorously. The water's movement is more consistent, with a more gentle hand being held on the leaf, indicating that the water has been drained. The leaves are now more firmly held, with their stems pointing downwards, implying that the leaves are being dipped in water. The leaf's surface is more exposed, with its leaves exposing more of the leaf'icon, a sign of the water'n's presence.
- Reference: The pak choi leaf is held closer to the camera, offering a more detailed perspective. Its well-hydrated state is evident from the sheen on its surface. The leaf, while still retaining its green vibrancy, has visible droplets of water clinging to it, highlighting its freshly washed status. The undulating edges of the leaf, along with the intricacies of its venation, are more discernible in this closer view.

#### Sample 24 — After

- Similarity: 0.4120
- Prediction: The bread has been partially removed from the bag, with the bread still firmly attached to the bag. The hand is now more firmly grasping the bread, indicating that the bread has not been fully removed. The bread remains intact, with no visible signs of damage or damage. The bag's contents are still visible, with only a few pieces of bread remaining.
- Reference: In this frame, the scissors have been removed from the clip, and the person's hands have changed position. The right hand now holds the clip between thumb and index finger, pulling it away from the packet. The left hand appears to be holding the packet steady. The clip has opened further, indicating that the action of cutting or prying with the scissors was successful. There is a slight disarray in the surrounding objects, such as the shifted napkin, which may imply movement in the environment.

#### Sample 26 — After

- Similarity: 0.4260
- Prediction: The tray is now in a more streamlined state, with the handle positioned slightly more firmly, indicating that the person has mastered the task of removing the foil. The hand's movements are more relaxed, suggesting that the foil has been removed, a process that has been completed. The tray's surface is more exposed, implying that the object is still being handled. The person's hands are more engaged, demonstrating that they are preparing to remove the foil, thereby removing any remaining residue.
- Reference: The cling film now exhibits more pronounced usage. It has been further unrolled and the leading edge seems to have been stretched out more than before, likely indicating that the film is being prepared for use. There are visible warps and widening in the plastic near the roll, and the stretched portion shows varying degrees of transparency due to the stretching. The person’s hands have shifted position, likely to accommodate the increased length of film that has been dispensed.

#### Sample 28 — After

- Similarity: 0.2565
- Prediction: The hand is now more firmly held, indicating that the hand is preparing to place the towel on the table. The hand's position is more relaxed, implying that the towel has been placed in the right position. The towel's surface is more exposed, suggesting that the person is now able to grasp the towel and move it around. The person's posture is more casual, demonstrating a more relaxed posture. The hands are still positioned in the same position, presumably preparing for the towel'd use.
- Reference: The tearing process is now complete, and the paper is divided into two distinct pieces. The left hand holds a completely detached segment, with a rough, frayed edge where the fibers of the paper were separated. The right hand still holds onto the original sheet, now with a complementary jagged edge at the bottom where the tear was finalized. The tear's path has left a distinctly textured edge, contrasting with the original smoothness of the intact paper.

#### Sample 31 — After

- Similarity: 0.3484
- Prediction: The surface of the kitchen is now more cluttered, with the hand scrubbing the surface more frequently. The hand's motion is more focused, indicating that the surface has been thoroughly cleaned. The surface is now a more uniform, adrift, and more sanitary, with a less noticeable streak of food residue. The kitchen's surface is more streamlined, with more of the surface smudge-free, with less of the residue visible. The person's hand is more engaged in the task, demonstrating a greater focus on the surface.
- Reference: The glass has been repositioned further to the right, confirming the continuous movement from the previous frame. The person's hand has moved along with the glass, indicating a controlled slide. The blurred reflection on the base of the glass is more pronounced, showing a consistent movement. There's a dynamic interaction between the hand and the object, where the hand's steadiness and the glass's balance appear synchronized in the action of sliding.

#### Sample 32 — After

- Similarity: 0.3759
- Prediction: The lid has been removed from the container, indicating that the lid is now fully open. The hand is now more likely to be holding the lid, implying that the container is now partially open. This is a sign that the person is now able to grasp the lid and remove it from the tray. The lid remains in the position of its original position, presumably to prevent the contents from falling out.
- Reference: The plastic wrap has been drawn further back, exposing a larger portion of the lettuce head. The leaves now have more space to fan out, and they exhibit a mixture of light and dark green shades, characteristic of the leafy layers of the head. It's evident that the lettuce is still quite fresh, with the leaves showing a healthy, plump appearance. The person's hands are more engaged in the unwrapping process, suggesting an eagerness or readiness to prepare the lettuce for consumption or use in a dish.

#### Sample 33 — After

- Similarity: 0.2778
- Prediction: The sink is now in a more natural state, with the lid still firmly attached to the sink. The kitchen's lighting is now dim, with a focus on the kitchen'd kitchen area, which is a focal point for the kitchen. The sink's surface is now more reflective, with its surface indicating a gradual movement. The water level is still visible, with no visible reflections, suggesting that the sink is still in the process of being cleaned. The surrounding environment is still cluttered, with only a few items visible, including the sink'r contents, indicating that the kitchen is still clean.
- Reference: In this frame, the cabinet door has been pulled open even more, almost to its fullest extent, allowing a full view of the shelves. The lower shelf's orderly array of cans is completely visible now, and the upper shelf reveals a collection of various-sized items that seem to be jars and other containers, some with identifiable labels, others obscured by the angle. The items on the upper shelf are less uniformly arranged than the cans below, suggesting a more casual approach to placing frequently used items within easy reach.

#### Sample 36 — After

- Similarity: 0.4299
- Prediction: The bread has been sliced, with the knife still in the middle of the action, indicating that the knife is now in the position of its intended position. The hand is now more firmly engaged in the action and the bread is now a more rounded shape, a sign of the bread's progress. The bread' texture is more consistent with the bread, which is a softer texture than the bread itself, and the knife's grip is more firm. The sandwich's surface is now slightly curved, suggesting that the bread has a slight crease, implying that the hand is still holding the bread. The knife'd edge is now visible, revealing a smoother surface, contrasting with the rest of the sandwich' appearance
- Reference: The tub has been opened, revealing the golden buttery spread inside, which has a smooth surface except for a slight disturbance where a portion has been skimmed off, most likely by the knife previously seen in the right hand. The lid has been neatly flipped open and placed back onto the tub, but slightly ajar, indicating recent use. The consistency of the butter appears soft, as is common with spreads of this type, and a small portion adheres to the knife's edge, showing it has just been used.

#### Sample 37 — After

- Similarity: 0.4955
- Prediction: The scrubbing motion is more intense, with the water running more quickly, indicating that the squeezing action has been completed. The hand is now more focused, with a more pronounced focus on the rinsing action, resulting in a smoother surface. The water's movement is more consistent, with more water being drained from the hose, ensuring that the water is able to reach the nozzle. The raffination action is more sporacious, with less water being seen, implying that the rinse has been done.
- Reference: The transformation of the spoon is evident in this frame. It is submerged in a sink filled with water and suds, surrounded by a flurry of soap bubbles. The hand, still encased in a yellow glove, is actively engaged in the cleaning motion, as denoted by the dynamic water and the changed position of the spoon. The sponge is pressed against the spoon, implying a thorough scrubbing is underway.

#### Sample 38 — After

- Similarity: 0.4516
- Prediction: The onion has been sliced into smaller pieces, revealing a more slicked portion of the onion. The knife's action is more deliberate, indicating that the onion has become more tender. The onion's skin is a little more exposed, suggesting that the knife'd action is aimed at removing the remaining pieces. The slits are a bit more precise, suggesting the onion's sprinkling of skin may have been a mistake.
- Reference: Here, the aubergine has been further divided, the knife nearing the completion of the cut, just short of the stem. The two halves are hinged at the stem end, splayed open but still connected. The cut reveals the patterned interior, with seeds dotted around the central column of flesh. The hand's grip has adjusted to the new form, with the fingers curling more around the now partially separated sections, and the thumb repositioned to prevent the halves from fully detaching.

#### Sample 39 — After

- Similarity: 0.3690
- Prediction: The sponge has a more streamlined appearance, with a cleaner, more scuffed appearance, and a longer, more uniformly shaped surface. The hand's motion is more focused, indicating that the sponge is now being washed, resulting in a cleaner surface.
- Reference: Here, the tap remains in the off position with no water emanating from the spout. The hand is actively engaged in cleaning a dish, corroborating that the tap has been turned off for a short while, as the focus has shifted to the cleaning task. The sink area still shows signs of wetness, but with no new water being added, the surfaces are likely starting to dry, especially considering the likely evaporation rate given the bright overhead lighting.

#### Sample 40 — After

- Similarity: 0.4480
- Prediction: The scrubbing motion is more intense, with the water running more quickly, indicating that the squeezing action has been completed. The water's movement is more pronounced, with a more agitated sprinkling of soapy water on the surface of the lint. The rinsing motion is less intense, demonstrating the risin' action. The hands are still firmly held, with their fingers pointing at the nozzle, ensuring that the water is sprayed into the hose.
- Reference: In this frame, the glass presents a cleaner exterior with fewer suds, implying a more thorough rinsing. The hand's grip remains firm, and the glass's angle has changed to facilitate the removal of the remaining soap and water. The interior appears clearer, with the water's surface tension holding a thin layer against the glass, reflecting the overhead lighting. The rim's cleanliness is maintained, and the overall clarity of the glass suggests that the washing process is nearing completion.

#### Sample 41 — After

- Similarity: 0.2652
- Prediction: The microwave door is now in a more natural position, with the lid still firmly closed. The hand is now able to grasp the door, revealing a gaping portion of the door. The kitchen environment is still cluttered, with a kitchen setting and a cluttered kitchen area. The door's interior is cluttered with clutter, including dishes, dishes, and other items. The surrounding environment is a blurry contrast between the kitchen and the kitchen, with only a few items visible.
- Reference: In this final frame, the milk bottle maintains its central position in the scene, with the cap clearly in a different state compared to earlier images. The hands seen in the periphery are positioned as though they are in the process of closing or have just finished closing the bottle. The cap appears to be settled more securely on the bottle, suggesting the action of sealing the bottle is either complete or nearly so. The lighting and reflections remain consistent, highlighting the bottle's curves and the cap's smooth, round shape.

#### Sample 51 — After

- Similarity: 0.2714
- Prediction: The bin is now in a more natural state, with the lid still firmly attached to the bin. The lid's position is more apparent, with a curved edge indicating the bin's movement. The bin'd contents are still visible, with no visible signs of movement.
- Reference: The image now shows the filter being inserted into a plastic housing, which is part of a larger appliance or system. The person's hands are positioned in such a way as to facilitate the careful placement of the filter back into its operational position. This housing suggests the filter is part of a mechanism that requires periodic maintenance. The edges of the filter fit snugly into the housing, indicating a proper design for ensuring that the unfiltered air or water does not bypass the filter. The area around the housing appears clean and well-maintained, highlighting the person's probable attention to regular upkeep.

#### Sample 55 — After

- Similarity: 0.4538
- Prediction: The spout is now in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's movement is more pronounced, with a broader range of movements, including a hand-held tap, which indicates that the sponging action has been completed. The rinsing motion is more focused, with more movement in the direction of the risining action. The hand's movements are more relaxed, with movement in both directions indicating a gradual movement.
- Reference: A pair of hands is seen gripping the pan, one at the handle and the other at the rim opposite the handle. The pan is being rinsed or washed as evidenced by the water running over its surface from the faucet. Some areas, particularly near the base, seem to have less water, hinting that the person might have been scrubbing or wiping those sections more vigorously.

#### Sample 56 — After

- Similarity: 0.3888
- Prediction: The box is now in a more streamlined state, with the lid still firmly attached to the top of the box. The hand is now more engaged in the action, indicating that the contents of the bag are being retrieved. The box's contents are now more readily accessible, implying that the person is now able to grasp the contents. The contents of this bag are now in the hands of the person who is holding it, presumably to ensure that the bag is not contaminated.
- Reference: The packaging is now in an advanced state of crumpling. The hand has shifted position, now grasping the lower part, indicating a progression in the crumpling process. The once cylindrical shape of the packaging is significantly distorted, with multiple folds and creases compacting it into a smaller, irregular form. The reflective surface is mostly crinkled, losing much of its initial luster and now exhibits a matte finish due to the extensive manipulation.

#### Sample 57 — After

- Similarity: 0.3193
- Prediction: The pot is now in a more natural state, with the lid still firmly closed. The hand is now more likely to be holding the pot, indicating that the water has been boiled. The water level is still a little higher than the previous frames, suggesting that the pot is still hot. The pot's surface remains a bit damp, suggesting a gradual change in the water content. The kitchen sink remains untouched, with no visible signs of cooking. The sink's interior remains cluttered, implying that the kitchen is still in the process of preparing for cooking.
- Reference: The filter is now held at a more pronounced angle, with the coffee maker slightly out of immediate reach below. The hand's grip has shifted to support the filter's base, likely to provide stability as the weight of the grounds could cause tearing or spillage if not handled carefully. The radial structure of the filter's base is more pronounced, possibly due to the changing grip and angle at which the filter is held. There's a clear intent to transport the used filter, possibly to a trash receptacle.

#### Sample 60 — After

- Similarity: 0.4413
- Prediction: The squeegee is now in a more streamlined position, with the handle positioned slightly more vertically, indicating that the water has been drained. The water's movement is more pronounced, with a broader range of movements, including a hand-held tap, which is likely to be used to rinse the squirt. The rinsing motion is more focused, with more movement in the direction of the risining action. The hand's movements are more relaxed, with their movements indicating a thorough rinse.
- Reference: The coffee pot is still in the sink but appears to be in a more upright position compared to the previous frame. The individual's fingers are wrapped around the pot's handle, suggesting an intention to lift or move it. Some water droplets remain on the pot's surface, although less froth is visible. The area around the pot's spout looks particularly wet, perhaps from a recent rinse.

#### Sample 61 — After

- Similarity: 0.4873
- Prediction: The table is now more cluttered, with the hand positioned closer to the table, indicating that the table is being wiped down. The hand is now firmly held, demonstrating the effort to clean the table. The table's surface is now slightly more exposed, with a more rounded appearance. The creases and wrinkles are more prominent, contrasting with the rest of the table'd surface.
- Reference: In this frame, the crumb has been decisively moved from its original position, now closer to the vacuum cleaner's nozzle. The disturbance in the fabric of the tablecloth around the crumb is more pronounced, with folds and creases leading towards the nozzle, visually narrating the path of movement. The crumb itself is more obscured by the shadow of the vacuum cleaner, highlighting the imminent action of it being picked up. The proximity to the nozzle and the altered lighting condition suggest the crumb's journey is nearing its end.

#### Sample 62 — After

- Similarity: 0.3684
- Prediction: The dough has been incorporated into the mixer, indicating that it has been thoroughly stirred. The hand's movements are more controlled, demonstrating that the dough has become more firmly kneaded. The consistency of the dough is more consistent, implying that the ingredients have been adrift in the mixing process. The dough's texture is more uniform, exhibiting a more pronounced texture.
- Reference: A stream of olive oil can be seen flowing from the bottle, indicating that the pouring action has commenced. The oil cascades in a smooth, continuous stream, reflecting light as it travels to the bowl. The hand holding the bottle is steady, guiding the flow of the oil to ensure it mixes evenly with the contents of the bowl. The pour is controlled, and the stream is narrow, suggesting a desire to regulate the amount of oil being added. The overall scene remains cluttered, but the act of pouring oil has become the central activity, with the hand and bottle coordinated in their purpose.

#### Sample 73 — After

- Similarity: 0.3876
- Prediction: The sponge is now more firmly held, with the water running more smoothly. The person's hand is now able to grasp the sponge, which is now being rubbed with soapy water, indicating that the sponge has been thoroughly washed. The sponge's surface appears to be a bit damp, suggesting that the water has been sprayed on the sponge. The water's consistency is more uniform, suggesting a more gradual cleaning process. The surface of the sponge appears to have been washered, with a smudge on the surface of it indicating a thorough cleaning.
- Reference: The grid now appears horizontally aligned with the edges of the sink, suggesting it has been positioned or is in the process of being set down. The hands are symmetrically placed, with each gripping opposite sides of the grid, likely exerting equal pressure to ensure its stable placement. Water beads are present on the grid, more prominently than before, possibly due to the hands' movement causing water to disperse along the grid's surface.

#### Sample 74 — After

- Similarity: 0.4615
- Prediction: The bowl has been placed in a more streamlined position, with the surface of the bowl a little more exposed. The hand is now more firmly engaged in the action, indicating that the bowl is now being wiped down. The bowl's surface is now a bit more cluttered, with a smoky appearance and a slightly more rounded shape. The surface of this bowl is more crowded, with more of the surface separating from the bowl, implying that the hand is attempting to clean the bowl.
- Reference: In this frame, the scale has been relocated further to the left, with the person's hand grasping its right edge, indicating movement. The display remains inactive, confirming that the scale has not been utilized for any weighing task up to this point. The glass platform of the scale now partially overlaps with the notebook, while the left hand steadies the bowl, ready to receive ingredients. This repositioning signals a transition from preparing to actively using the scale for the intended measuring task.

#### Sample 78 — After

- Similarity: 0.4878
- Prediction: The hand is now more firmly grasping the jar, indicating that the lid has been removed. The lid is now firmly pressed against the edge of the holder, implying that the hand is removing the lid. The hand's motion is more pronounced, suggesting that the rim is being pulled back. The jar's contents are still visible, with the lid still firmly attached to the ring.
- Reference: In this frame, the hand appears to be reaching further into the cabinet, implying that the person is likely reaching for an item at the back. The balsamic vinegar and the sea salt are still in the front, but there seems to be a subtle change in the orientation of the balsamic vinegar bottle. The items in the background are a bit more obscured due to the angle of the hand and the items in the foreground, yet the overall organization of the cabinet remains constant with no significant rearrangement of its contents.

#### Sample 83 — After

- Similarity: 0.4268
- Prediction: The jar is now in a more open position, with the lid still firmly attached to the pot. The hand is now more engaged in the action, indicating that the lid has been removed. The lid remains in the same position as the jar, implying that the hand is still holding the lid. The rim of the jug is now slightly curved, suggesting that the spout has been partially removed.
- Reference: The jar of pesto now shows clear signs of having been accessed. The pesto level appears to be slightly lower than before, with some of its contents possibly scooped out. Streaks and smudges of pesto are evident along the inner walls of the jar, indicating that someone has interacted with it, likely using the utensil. The previously undisturbed texture now seems a bit uneven with minor disruptions.

#### Sample 84 — After

- Similarity: 0.4719
- Prediction: The microwave has been removed from the kitchen, and the hand is now positioned in a more natural position, indicating that the microwave has ceased to function. The hand's motion is more pronounced, suggesting that the hand has been able to grasp the microwave's contents, which are now in the kitchen. The kitchen's interior remains unchanged, with the kitchen still cluttered with food, dishes, and other items. The microwave'd contents are still visible, with only the lid still visible. The surrounding environment is still a little blurry, with a few objects and objects in the background, including the kitchen'r kitchen counter, and a kitchen counter.
- Reference: The hand is now placed on top of the toaster, with fingers extended towards the front. This is a typical position for pushing down the toaster's lever, which is not visible in this frame. Although the actual motion of the lever is not captured, this gesture strongly implies that the toasting process is being initiated. The rest of the scene remains constant, with the cutting board and the plastic container still in their places, standing by as silent observers to the routine task unfolding.

#### Sample 86 — After

- Similarity: 0.2199
- Prediction: The bag is now in a more streamlined state, with the hand firmly grasping the bag, revealing a slender, curved portion of the bag. The hand's motion is more relaxed, indicating that the bag is being handled. The bag's contents are more readily visible, with a clearer image of the contents. The bags' shape is more pronounced, suggesting that the contents are being handled more carefully. The person's hand is more likely to be holding the bag in the hands of the person, implying that the bags are being viewed in restraining mode.
- Reference: The leek's trajectory continues its unwelcome descent, now even closer to the ground. The motion blur has intensified, especially around the green leafy ends, indicating an acceleration of its fall. The plastic sheath appears more disheveled, possibly due to air resistance and the leek's own motion. The leek's base end, once pristine white, is now almost out of view, implying it may have rotated slightly as it fell, with the possibility of impact becoming more imminent.

#### Sample 87 — After

- Similarity: 0.3538
- Prediction: The rinsing device is now in a more natural position, with the water running through the surface of the ricotta, indicating that the water has been drained. The hand's grip is still firmly held, allowing the water to drain from the nozzle, ensuring that the scrubbing action is effective. The water level is still high, suggesting that the rinse has been completed. The nozzle is now positioned in recirculation mode, demonstrating the optimum amount of water to reach the rim of the device.
- Reference: The saucepan lid in this frame appears clearer than before, hinting at the progression of the cleaning process. There are still traces of moisture, suggesting a recent rinse. The person's hands are positioned in a manner that looks like they are ensuring that all areas of the lid have been adequately addressed. The light reflections seem more consistent across the lid, indicating fewer residues or spots.

#### Sample 88 — After

- Similarity: 0.4316
- Prediction: The lid of the container is now in a more upright position, with the hand firmly holding the lid. The hand's motion is more relaxed, suggesting that the lid is now fully closed. The lid's shape is more streamlined, suggesting a gradual movement, with a focus on the contents of the lid'd container. The container's surface is more exposed, suggesting the lid has been partially closed.
- Reference: In this frame, the hands grasp the container more securely, and a notable shift in the arrangement of the cheese slices can be observed. The top slice has been disturbed from its previously neat stack, now protruding at an angle indicative of potential selection or preparation for use. This slight disarray contrasts with the earlier orderly presentation, conveying a sense of imminent consumption or culinary application.

#### Sample 89 — After

- Similarity: 0.2295
- Prediction: The kitchen's lighting is now more visible, with the light reflected off the wall and the door open. The lighting is more consistent, with a more natural, streamlined look. The light is now reflected from the kitchen' walls, indicating that the kitchen is now fully lit. The kitchen appears to be a complete mess, with no visible light or obstructions.
- Reference: In this frame, the squash container seems to retain its position from the second frame, with minimal to no noticeable difference. The label graphics remain visible, reiterating its blue and green hues. The proximity of the white cap to the container is consistent with the second frame, emphasizing that the cap has not been replaced.

#### Sample 90 — After

- Similarity: 0.3694
- Prediction: The sliced avocado is now a more ripe, slicked-off portion, with the skin still a little smoky. The skin is now more exposed, with a slender, rounded shape, indicating that the avocado has been sliced. The hand's motion is more relaxed, with its fingers pointing at the avocado, revealing a smooth, rippling surface. The avocado's skin is a bit more sloppy, with some of the flesh separating from the avocado' core, exposing the skin.
- Reference: The pepper, still vibrant and freshly cut, has been further dissected into individual segments. It remains on the same wooden cutting board, with the inside facing the viewer. The segments are arranged in an orderly fashion, fanned out from the stem, which is now at the top of the frame. Each segment is neatly sliced, with smooth edges and the seeds have been removed, indicating meticulous preparation.

#### Sample 91 — After

- Similarity: 0.4182
- Prediction: The squeegee's grip is now more firmly held, with the handle positioned more vertically, indicating that the water has been drained. The water's movement is more consistent, with a more gentle stroke, resulting in a smoother surface. The rinsing action is more gradual, with more water being dripped onto the squirt, ensuring that the raffination process is complete. The hands are still firmly seated, with their fingers pointing toward the nozzle, implying that the hand is now preparing the hose.
- Reference: In this frame, the cleaning process has advanced; the person's hands are actively scrubbing the cap with a green scrub sponge. This direct action indicates a shift from rinsing to scrubbing, likely to address the more persistent areas of buildup. The cap is positioned in a way that suggests a rotational scrubbing motion, applying the sponge's abrasive surface to the cap's top and side, where residues commonly accumulate.

#### Sample 96 — After

- Similarity: 0.3168
- Prediction: The hand is now more firmly grasping the pan, indicating that the lid has been removed. The person's hand is more relaxed, demonstrating a more natural grip on the pan. The pan's surface is more exposed, suggesting that the pan is now fully cooled. The chef's hands are still firmly gripping the pan'd surface, implying that the cooking process is complete.
- Reference: The opening of the packaging has progressed further. The plastic film has now been peeled back considerably, exposing more of the salmon's surface to the air. The top part of the packaging is visibly deformed due to the peeling, while the bottom part still clings to the fish, maintaining its original vacuum-packed appearance. The person's hands are actively working on removing the packaging, indicating a continuation of the opening process.

#### Sample 100 — After

- Similarity: 0.3878
- Prediction: The camera's focus shifts to a more streamlined frame, with the door open and the door closed. The camera is now positioned in a position that allows for a clearer view of the kitchen area. The kitchen appears to be a bit more open, with a less noticeable gap between the door and the kitchen counter. The surrounding environment is more cluttered, with less clutter and clutter, indicating that the kitchen is still open.
- Reference: The scene has now been enveloped in darkness, with the light source seemingly turned off. The absence of light has rendered the room's details nearly indiscernible, with only vague shapes and forms distinguishable in the deep shadows. What were once reflective surfaces have now blended into the obscurity, losing the luster they exhibited when illuminated. The environment exudes a sense of stillness and quiet, typical of a space where the light has been switched off and night has fallen.

#### Sample 106 — After

- Similarity: 0.4037
- Prediction: The hose is now in a more streamlined position, with the handle positioned in reversing its position, indicating that the water has been drained. The water's flow is more sporky, suggesting that the hose has been placed in agitation mode. The nozzle's surface appears to be drier, suggesting a rinsing process. The hand's movements are more relaxed, suggesting the nozzle is now agitating. The hands' posture is more relaxed and agitated, implying that the hand is now more engaged in the ribbing process.
- Reference: In this frame, the saucepan lid is being held out of the water, allowing for a clear view of its inside surface. The person's hands are holding the lid from the sides, with their thumbs on the rim, likely rinsing or inspecting it. The surface of the lid looks clean with water droplets scattered across it, reflecting light, which indicates it has likely been rinsed off. The sink appears less foamy around the area of the lid, which may be a result of the water being disturbed during the cleaning and rinsing process.

#### Sample 110 — After

- Similarity: 0.3775
- Prediction: The hand is now more firmly held, indicating that the hand is still in motion. The hand's position is more pronounced, suggesting that the hands are now in a more natural position. The creases and wrinkles are more prominent, suggesting a gradual movement, a sign of a broader range of motion.
- Reference: In this frame, the chair has been moved further from the table, and its orientation has changed noticeably. The distance between the chair and the table has increased, which is evident by the larger expanse of tiled floor now visible between them. The chair's shadow stretches out on the floor, altered by the movement and the angle of the light source. The chair's position relative to the camera has shifted, suggesting continued movement.

#### Sample 111 — After

- Similarity: 0.3744
- Prediction: The sink has been re-opened, with the water still visible, with a more streamlined appearance. The hand's movements are more deliberate, indicating that the water is still present, and the water has been removed from the sink. The water level is less noticeable, with less water dripping from the faucet, suggesting that the sink is still active. The sink's surface is more cluttered, with more water splatters, suggesting a gradual movement. The person's hand is more focused on the sink, demonstrating a heightened focus on the water. The surface of the sink appears to be a bit more damp, suggesting the water may have been drained.
- Reference: The cloth now appears to be in a more relaxed state compared to the previous frame. Its texture and spread suggest that it has been released or lessened from the squeezed position it was in earlier. While it still retains numerous folds and creases, it looks more spread out, indicating the release of pressure. The cloth continues to display signs of dampness, and its positioning suggests it's still being held or manipulated, albeit with less force than before.

#### Sample 113 — After

- Similarity: 0.3689
- Prediction: The water is now dripping from the faucet, indicating that the water has been sprayed into the faucet. The person's hand is now more engaged in the process, demonstrating the reversing action. The water's color has shifted to a more neutral hue, implying that the faucet is now fully saturated. The faucet's surface appears to be soaked in water, suggesting that the scrubbing action has been completed. The nozzle's position is more pronounced, suggesting a gradual process.
- Reference: The burner cap here presents a significant improvement in cleanliness. The majority of the surface now exhibits the metal's innate color and texture, with only a few stubborn spots of carbonized debris remaining. The cap's edges and the holes are more defined, suggesting that the cleaning has been effective in removing the layers of grime. The presence of water and suds indicates an ongoing cleaning process, and the hands appear to be conducting a final inspection or perhaps targeting the remaining soiled areas for a last scrub.

#### Sample 118 — After

- Similarity: 0.4737
- Prediction: The vegetable has been steamed, with the skin still a little charred, with a slight charring to the edges. The pan's heat is now more intense, with more of the vegetables slicing through the skin. The cooking surface is still slightly hot, with some of the skin sticking out. The kitchen is now a bit more crowded, with less of a noticeable difference in the color of the vegetable.
- Reference: In this frame, the hob shows a slight progression from the previous scenes. The hand that was adjusting the knob in the second frame has now been withdrawn, suggesting the adjustment has been completed. The wok, still on the same burner, contains the vegetables which now seem even more cooked, as indicated by their diminished structure and darker coloring from the continued application of heat. The other burners and the spoon rest remain unused, and the kitchen countertop continues to be free of any clutter. The overall setting of the hob is consistent with an ongoing cooking session that is actively monitored and adjusted by the user.

#### Sample 119 — After

- Similarity: 0.3636
- Prediction: The spout is now in a more streamlined position, with the water running through the center of the sprig. The water's movement is more consistent, with a steady stream of water scrubbing the nozzle, indicating that the rinsing process is complete. The hand's movements are more relaxed, with more movement in the direction of the water'd flow. The ristor's grip is more relaxed and the water is able to move the hose away from the holder's hand, allowing the wring to drain.
- Reference: In this frame, the V60 is again submerged, but this time the hand is employing a scrubbing brush to clean its interior. The positioning of the brush implies a focus on the inner surface of the V60, likely targeting stubborn coffee stains or residue. The vigorous motion of the hand and the dynamic swirl of the bubbles around the V60 suggest an intensive cleaning process, focused on ensuring the V60 is thoroughly scrubbed.

#### Sample 123 — After

- Similarity: 0.4908
- Prediction: The water in the sink has shifted slightly, indicating that the water is still in the bowl, a sign that the sink is now a bit more streamlined. The water's surface is more cluttered, suggesting that the bowl is still a little damp, and the water'd particles are less likely to be present. The sink's current state of motion is more apparent, suggesting a more gradual movement, with the water still circulating in the basin. The overall state of the water appears to be more stable, suggesting the water has been able to move more quickly.
- Reference: In this final frame, the hand is out of focus and appears to be retreating from the previous position above the sink, likely at the end of the washing motion. The hand is angled away from the viewer, with the heel of the palm visible and the fingers pointing off to the side of the frame. The floor is now visible, indicating that the hand has moved from the vicinity of the sink, suggesting a transition to the next phase of the hand-washing routine, possibly reaching for a towel or about to be dried.

#### Sample 124 — After

- Similarity: 0.4417
- Prediction: The salad has been steamed, with the vegetables separating from the bowl. The hands are now more engaged in the action, with a more pronounced hand motion. The greens are a little more ripe, with more of the lettuce and other vegetables forming a clump. The bowl is now more cluttered, with less space for the salad to spread out, with some of the ingredients scattered around.
- Reference: The wooden spoon appears once more in a different stage of use, its bowl now exhibiting clear signs of interaction with the food. Food residue clings to the inner surface, and the spoon is positioned at a near-vertical angle, indicating the completion of a scraping or gathering action. The handle of the spoon, consistent with the prior images, is held steadily, and the utensil is poised just above the plate, likely having just been lifted following contact with the food.

#### Sample 129 — After

- Similarity: 0.4743
- Prediction: The hand in the kitchen is now more firmly grasping the bowl, revealing a more streamlined appearance. The contents of the bowl are now more visible, including the contents of a plastic bag, which is now a clearer picture of the contents. The hand is now slightly more angled, suggesting that the bowl is now partially open. The kitchen's interior is now much more spacious, with the kitchen'd items positioned in a slightly different position. The overall appearance of the kitchen appears to be more modern, with a cluttered kitchen and kitchen counter area, and the overall appearance more familiar.
- Reference: In this frame, the drawer is fully extended, exposing its entire contents. The assortment of greens is now completely visible, including a bag that seems to contain a bulkier, possibly cruciferous vegetable like broccoli. The previously seen milk container shares the space with a dark bottle, possibly a soda or some condiment, and a pack of tortillas or flatbreads. There's also a hint of another container or packaging on the far left, obscured by the drawer's angle. The individual's hands are in motion, with one seemingly having just moved an item, evidenced by the slight blur.

#### Sample 134 — After

- Similarity: 0.4347
- Prediction: The spout is now in a more streamlined position, with the water running more smoothly. The water's flow is more concentrated, with a greater focus on the spongy areas, which are likely to be a result of the rinsing process. The hand's grip is more relaxed, with more movement, indicating that the nozzle is now positioned in optimum condition. The nozzle's surface is more rounded, with less water dripping from the hose, resulting in fewer bubbles. The hands' movements are more relaxed and more agitated, demonstrating the reversing of the water'n's movement.
- Reference: The colander is now more prominently featured, situated closer to the forefront of the frame. The faucet of the sink looms above it, suggesting that it might have been placed under the faucet for a thorough rinse. The reflective nature of the colander continues to stand out, with water droplets evident on its surface. There is a hint of movement in the frame, as evidenced by a blurred hand near the colander, suggesting active cleaning or positioning of the utensil.

#### Sample 136 — After

- Similarity: 0.4855
- Prediction: The bin's lid is now fully open, indicating that the contents of the bin are in the hands of the person who is holding it. The hand is now more likely to be holding the bin, which is likely to contain more waste. The bin remains open, with the lid still firmly attached to the bin. The lid's shape is more streamlined, suggesting that the bin is now partially closed.
- Reference: In this frame, the action of emptying the pan into the bin seems to have been completed. The bin appears fuller, with a varied assortment of discarded food items piled on top. The layers of food waste now seem to merge, making it slightly challenging to distinguish between older and newer additions. However, the presence of the previous items like pasta and vegetables is still prominent, and there's an even spread of different food types, indicating a diverse range of leftovers.

#### Sample 140 — After

- Similarity: 0.4185
- Prediction: The hand is now more firmly held, indicating that the hand is preparing to move the towel. The hand's position is more relaxed, implying that the towel has been awaited, a moment of action. The towel's surface is more exposed, suggesting that the person is now able to grasp the towel and move it around. The creases of the towel'd surface are more noticeable, highlighting the crease's movement. The cloth's texture is more consistent, contrasting with the rest of the cloth'd appearance.
- Reference: The hand now holds the glass in a more relaxed manner, with the fingers not as tightly coiled around it. The glass is positioned closer to the edge of the table, indicating a movement from its original location. The liquid level inside the glass remains consistent with the previous frames, ensuring that the contents have been stable during this movement.

#### Sample 142 — After

- Similarity: 0.4082
- Prediction: The lid is now in a more streamlined position, with the handle positioned slightly more vertically, indicating that the lid has been removed. The hand's angle is slightly more angled, suggesting that the hand is holding the lid, which is likely a step forward. The lid's position is more pronounced, suggesting a gradual movement, with a slight tilt to the right of the lid. The kitchen environment is still cluttered with clutter, including the sink, counter, and kitchenware, which are all visible.
- Reference: The surroundings in this frame blur slightly, possibly due to rapid motion or a shift in focus. The person's hands are still prominently displayed, and their interaction with the plate continues. While the sausage is not overtly visible, the positioning of the hands and the context suggests the sausage might be beneath the plate or has been moved to another location in this sequence.

#### Sample 145 — After

- Similarity: 0.2278
- Prediction: The sliced avocado is now a more ripe, slender, and more tender, with a slightly more firm texture. The hand is now more precise, and the knife is more precise than before, indicating that the avocado has been sliced. The avocado's skin is now slightly softer, with the skin separating from the avocado' core. The knife's edge is now exposed, revealing a smooth, rounded surface, a sprinkling of flesh on the avocado.
- Reference: Here, the pitta bread has been partially immersed into the hummus. A portion of the bread is submerged, gathering a generous amount of the creamy dip. The part of the pitta that's dipped in the hummus has a noticeably wet appearance, glistening from the moisture and indicating a successful scoop. The non-dipped portion remains untouched, providing a contrast to the dipped end, showcasing the effectiveness of the dip.

#### Sample 147 — After

- Similarity: 0.4063
- Prediction: The hand's grip is slightly looser, suggesting that the hand is adjusting the heat level. The knob is now positioned in a more natural position, indicating that the heat has been reduced. The hand is still holding the knob, implying that the knob is being lowered. The kitchen remains uncluttered, with the kitchen still cluttered with food and other items. The stovetop remains unoccupied, with no visible signs of cooking.
- Reference: The environment around the mixer now appears more blurred, suggesting rapid movement or a swift action taking place. The mixer, while still recognizable, seems to be in the midst of a quick rotation or shift, likely guided by the user's hand. The lid on the mixer is firmly in place, ensuring the contents inside remain secure despite the rapid movement.

#### Sample 150 — After

- Similarity: 0.3342
- Prediction: The kettle has been removed from the water, indicating that the water is now in a liquid state. The hand is now more firmly holding the kettle, implying that the action is complete. The water level is still the same, suggesting that the kettle is still in the liquid state, and the water level has been reduced. The kettle's surface is still a little damp, suggesting a gradual change in the water content of the kettle.
- Reference: The hand is now in direct contact with the spice, suggesting that the spice has been actively selected and is being removed from its original position. The other surrounding items have become secondary as the primary interaction is between the hand and the spice. The gesture of the hand indicates a firm grip, and it's evident that the spice will be used or inspected, taking it out of its passive state in the cupboard.

#### Sample 152 — After

- Similarity: 0.4553
- Prediction: The pot is now in a more natural state, with the lid still firmly attached to the pot, indicating that the water has been boiled. The hand's movements are more relaxed, suggesting that the pot is still in the pot. The water level is still a little higher than the previous frames, suggesting a gradual increase in the water content of the pot or pan. The pot's surface remains damp, suggesting the water is still present, and the pot'rsquo;s surface is still damp.
- Reference: The stove's burner remains ignited, with the blue flame continuing to burn steadily, suggesting a consistent heat level. The pan remains on the burner, and the person's hand is still in view, holding the pan's handle. The previously mentioned purple screwdriver remains adjacent to the stove but does not seem to have been moved or adjusted. The overall scene looks very similar to the previous frame, indicating that the cooking process is ongoing and stable.

#### Sample 153 — After

- Similarity: 0.3219
- Prediction: The hand's position is more relaxed, with the blades pointing towards the sink. The surface of the sink appears to be a bit cleaner, with a more streamlined appearance. The water level is less noticeable, with less water dripping from the sink, suggesting a gradual progress. The hand is now more focused on the surface, with more of the blade pointing toward the sink and the sink's surface. The sink'ed surface is more cluttered, with only a few spots of water visible, indicating a thorough cleaning.
- Reference: The scene has evolved into one where the pepper mill is being maneuvered with intention, as indicated by the hand's confident grip and the blurred motion of the mill and the hand together. This motion blur indicates a swift, directed movement, likely an action to place the pepper mill back into its rightful position or to continue with its intended use. The hand's position at the top of the mill suggests a more stabilized and deliberate control, contrasting with the previous frames.

#### Sample 154 — After

- Similarity: 0.4111
- Prediction: The tomato has been placed in a new position, with the lid still firmly attached to the pot. The hand is now more resolute, indicating that the action is complete. The lid is now firmly pressed against the pot, implying that the lid is still attached to it. The kitchen environment is still cluttered with the remains of the tomato, including the lid, and the kitchen's lighting.
- Reference: Here, the jar is again in a different position, tilted, indicating the continuation of the shaking motion. The contents remain a green blur, and the lid is still tightly sealed. The hand gripping the jar has adjusted its hold, perhaps in preparation for another shake, with thumbs pressing against one side of the jar, and fingers wrapped around the opposing side, displaying a firm grip. The background suggests a residential setting with common household items.

#### Sample 158 — After

- Similarity: 0.3631
- Prediction: The bowl is now in a more natural position, with the handle still slightly angled, suggesting a gradual movement. The hand is now more firmly in the position of the bowl, indicating that the bowl is still in its original position. The bowl's surface is now cluttered, with a cluttered appearance and a lack of movement.
- Reference: The orange has travelled further from its original position. It's almost at the edge of the table, with increased motion blur indicating its consistent movement. The reflection of the light source on the orange's skin has shifted towards the opposite side, now highlighting different surface imperfections and presenting a dynamic change in its overall visual perception.

#### Sample 160 — After

- Similarity: 0.4808
- Prediction: The rag is now more firmly held, with the fingers pointing downwards, indicating that the rag has been fully soaked. The hand's movements are more relaxed, with a more pronounced grip on the ring, a sign of the rinsing action. The ring's surface appears to be soaked, with its surface revealing a bare, dampened area. The hands' posture is more relaxed and relaxed, demonstrating the reversing motion of the hand.
- Reference: This angle provides a closer look at the dish drying area from another perspective. It shows the dish rack more prominently, revealing the details of the kitchen tools and utensils that are placed within. The presence of cleaning products, including a white bottle, indicates that the cleaning process is perhaps nearing its end, as items are likely being put away after washing. The kitchen towels and the blue bucket in the background have not been moved, maintaining the continuity of the kitchen's busy state.

#### Sample 163 — After

- Similarity: 0.3117
- Prediction: The hand is now more firmly held, indicating that the hand is preparing to move the pan. The hand's position is more relaxed, implying that the pan is now in the position of its original position. The person's posture is more comfortable, demonstrating a more relaxed posture. The pan's surface is more exposed, suggesting that the person is now able to move it.
- Reference: The tablecloth is now more spread out, showcasing more of its surface area. It drapes over part of a table and extends towards the floor. The cloth's edges are more visible, and there seems to be less movement, indicating that the process of unfolding and setting might be nearing its conclusion. The tablecloth's texture and any potential designs it might have are clearer in this frame than in the previous ones.

#### Sample 165 — After

- Similarity: 0.4990
- Prediction: The rag is now more tightly held, with the fingers firmly pressed against the fabric, indicating that the water has been drained. The hands are now more engaged in the process, with their fingers extending from the fabric's surface to the surface. The fabric's texture appears to be more pronounced, with a more rounded shape and a longer, more curved appearance. The creases are more defined, with more of the fabric forming a slouchy, ragged appearance.
- Reference: The cloth is now submerged in water, with the fingertips lightly grazing its surface, suggesting a gentle cleaning or rinsing action. The cloth appears to be more saturated, as its color is darker throughout. Bubbles are visible around the cloth, indicating recent or ongoing agitation in the water, possibly from the cloth's movement.

#### Sample 168 — After

- Similarity: 0.4786
- Prediction: The mixture is now more homogeneous, with the consistency more uniform, and the blending process more efficient. The hand is still holding the mixture, indicating that the ingredients are being stirred together. The blending action is more pronounced, with a smoother texture and a more consistent consistency. The consistency of the mixture is less pronounced and the consistency is more uniform.
- Reference: In this frame, the blender is completely still with the power button released, indicating the blending action has finished. The person's hand remains on the blender, ready to remove it from the bowl. The cord is now draped over the person’s hand, showing more of its length and suggesting the person has adjusted their hold to facilitate turning off the device. The mixture looks slightly more settled in the bowl, with fewer air bubbles, implying that it is no longer being agitated by the blender.

#### Sample 169 — After

- Similarity: 0.3705
- Prediction: The bowl is now positioned in a more soiled position, with the water running through the center of the bowl. The water's flow is more concentrated, with a greater amount of water circulating around the bowl, indicating that the water has been drained. The hand's movements are more relaxed, with more movement in the direction of the water'ing process. The bowl's surface appears to be steamed, with water dripping from the bottom of the sink. The rinsing motion is more pronounced, with some water splashing on the surface.
- Reference: The cleaning process has advanced significantly, with the water having softened and dissolved much of the residue, revealing more of the tray's underlying surface. A swirling pattern of soap suds and loosened debris is now present, creating a marbled effect across the tray. This suggests that the combined action of water and possibly detergent is breaking down the charred layers, making them easier to remove. The person's grip remains firm and controlled, facilitating thorough rinsing.

#### Sample 171 — After

- Similarity: 0.4037
- Prediction: The pan is now more streamlined, with the water sprinkling more evenly across the surface, indicating that the water has been absorbed. The water's consistency is more uniform, with a more pronounced slurry, suggesting that the pan is being boiled. The pan's surface is more crowded, with less water and less water escaping, implying that the pot is being held in a hot, soiled state. The steamed portion of the pan has been more agitated, with more water dripping from the bottom of the pot, resulting in fewer bubbles.
- Reference: The oat in this frame demonstrates further displacement and redistribution within the pan. There are more pronounced pockets of uneven distribution, indicative of more substantial agitation or movement. The edges and surface of the oat appear more irregular, with clusters and gaps more evident. While the oats still appear predominantly raw, there's a perceptible difference in their arrangement and distribution compared to the previous frames.

#### Sample 174 — After

- Similarity: 0.2871
- Prediction: The vegetables are now more seasoned, with a more pronounced aroma and flavor. The color is more vibrant, with the consistency of a steamed vegetable contrasting with the rest of the ingredients. The squeezing motion is more noticeable, indicating that the ingredients have been stirred. The consistency of the vegetables is more consistent, with some of the flavors still present. The texture of the veggies is more reminiscent of sour cream, which is a common ingredient in many recipes.
- Reference: In this frame, the colander is now positioned over the sink, as if the person is preparing to drain excess water or give the beans another rinse. The beans are settled at the bottom, still wet and shimmering under the light. The person's other hand is visible, wearing a yellow glove, possibly to protect against hot water or to keep hands clean. Below the colander, the shiny sink basin reflects the beans' colors, and the overall atmosphere suggests a diligent and thorough cooking process.

#### Sample 181 — After

- Similarity: 0.4552
- Prediction: The spout is now in a more streamlined position, with the water running through the spongy part of the bowl, indicating that the water has been drained. The hand's movements are more relaxed, demonstrating the rinsing action, which is likely to be the final stage of the filtration process. The water's surface is still damp, suggesting that the lint is still present, and the water'n's movement is a sign of the final stages of the process.
- Reference: The dish now appears to be in a more upright position compared to the previous frame. The person's hand is still gripping it firmly, suggesting that the washing action is ongoing. There are visible water trails on the dish's surface, which reflect the ambient light and suggest recent movement. The environment around the dish remains dimly lit, with other dishes and objects around it still in shadow, while the focus remains on the dish being washed.

#### Sample 182 — After

- Similarity: 0.3006
- Prediction: The hand is now more firmly engaged in the action, indicating that the hand is a more active participant. The hand's motion is more pronounced, suggesting that the action is more deliberate. The lighting is more consistent, implying that the lighting is less intense, a sign that the room is more likely to be occupied. The shadows are more noticeable, suggesting a deeper focus on the room.
- Reference: This scene shifts focus to the task at hand, where a person’s hands are visible, holding a bundle of washed clothes. The colors are vibrant, with a prominent teal shirt and a pair of white socks, which are slightly discolored, suggesting use. The clothing appears to be in a state of being removed from the washing machine, as evidenced by the manner in which they are bunched up and gripped, ready to be transferred to the next stage of laundering.

#### Sample 184 — After

- Similarity: 0.4354
- Prediction: The box is now in a more streamlined state, with the hands firmly engaged in the action. The contents of the box are now more visible, with a clearer image of the contents. The box's contents are more visible and the contents are less noticeable, indicating that the box is being handled. The hand's movements are more relaxed, demonstrating the ability to grasp the contents of a box.
- Reference: The progression in opening the cereal box is evident as the hands are now interacting with the inner plastic bag. The top of the bag has been partially torn open, with a strip of the plastic material visibly detached and hanging loosely from the rest of the bag. The opening is not yet wide enough to pour the cereal out or to see its contents clearly, but the action taken signifies the initial breach of the bag's seal, leading towards the serving of the cereal.

#### Sample 185 — After

- Similarity: 0.4780
- Prediction: The microwave door is now in a more natural state, with the hand still firmly holding the door open, indicating that the oven has been fully opened. The hand's movements are more relaxed, suggesting that the microwave has been preparing for a meal or meal. The kitchen environment is still cluttered, with a kitchen setting and a cluttered kitchen area. The door's position is more streamlined, suggesting a gradual movement, with no visible signs of progress. The microwave's interior remains unchanged, with its interior contrasting with the surrounding kitchen area, implying that the kitchen is now fully open.
- Reference: The temperature display is no longer in focus, as the user's action takes precedence in the frame. The blurred reflection on the oven door still allows a glimpse of the red digital numbers, although they are not legible. The user continues to engage with the oven’s controls, maintaining a grip on the knob. It's evident from the motion blur and hand position that the user is actively adjusting the settings. The surrounding environment remains consistent, with kitchen elements like a frying pan and what appears to be flatbread in proximity, suggesting meal preparation is underway.

#### Sample 187 — After

- Similarity: 0.3591
- Prediction: The hand is now more firmly grasping the pot, indicating that the water has been boiled. The water's consistency is more consistent, suggesting that the pot is still in the water'd state. The pot's surface is more exposed, suggesting a gradual movement, possibly a re-filling of the water. The kitchen's lighting is also more reflective, implying that the heat is reflected off the pot.
- Reference: The chicken now seems to be momentarily set aside, as the individual has completed the hand washing and is drying their hands with what appears to be a yellow kitchen cloth. The chicken remains on the cutting board as in the first frame, with no additional preparation evident. This suggests that the process of cutting the chicken has been momentarily halted while the person attends to personal cleanliness, maintaining good kitchen hygiene practices.

#### Sample 189 — After

- Similarity: 0.3179
- Prediction: The cheese has been partially cut, with the knife firmly positioned in the center of the cutting board. The knife's edge is now firmly held, indicating that the cheese has reached its final state. The cheese's texture is more consistent, with a smoother texture and a more uniform texture. The hands are now more engaged in the cutting process, demonstrating the bread's gradual progress. The sliced cheese remains a little firm, but the knife'd edge is still visible, revealing a sloppy, slender slice of cheese.
- Reference: The cake has undergone further reduction in this frame. The crumbly golden-brown top still remains prominent and offers a delightful contrast to the darker, moist interior. Yet another segment has been cut, revealing more of its luscious inside. The cake now covers just about half of the circular purple plate, with the freshly cut edge indicating the most recent slice that was taken.

#### Sample 193 — After

- Similarity: 0.4903
- Prediction: The sliced mushrooms are now more closely slicked, with the skin separating from the meat. The knife's motion is more deliberate, indicating that the knife has been shaved off the meat, revealing a more pronounced cut. The skin is more exposed, suggesting that the meat has been cut into smaller pieces. The slits are more revealing, suggesting a deeper cut.
- Reference: The knife is seen completing a cut, with a piece of tofu having just been severed, demonstrating the ease with which the knife glides through the soft material. The tofu pieces that have been cut are notably uniform in size, suggesting a meticulous approach to cutting for even cooking. One can see that the tofu is still uncooked, maintaining its raw texture and color, as it awaits the heat of the wok to transform its flavor and texture.

#### Sample 194 — After

- Similarity: 0.4545
- Prediction: The water level in the bowl has decreased, indicating that the water is now dripping from the faucet. The water is still a little hot, suggesting that the tap is still running. The hand's movements are more relaxed, demonstrating the presence of the water. The rinsing action is a clear sign of the final stages of the process.
- Reference: In this stage, the saucepan is still in the sink, and the soapy water within has become murky, likely from the dislodged food particles. The person's hand remains on the handle, possibly moving the pan to ensure that the soapy mixture reaches all areas. The water level in the pan seems consistent with the previous frame, and the foam is still present, although it may be less as the cleaning progresses.

#### Sample 196 — After

- Similarity: 0.3787
- Prediction: The tray is now in a more streamlined state, with the hands positioned more horizontally, indicating that the person has been able to grasp the tray. The hands are now more engaged in the action, demonstrating the heightened focus on the tray's surface. The tray' appearance is more reminiscent of a kitchen counter, with its creased edges and rounded corners, contrasting with the rest of the tray and the surrounding area.
- Reference: The bag now appears to be in a more finalized state of folding or sealing. The hand's grip has shifted, possibly indicating the end of the folding process. The bag's surface appears more even and settled, with fewer visible contents. The overall structure of the bag seems more compact and tidier than in the previous frames, suggesting that the action of folding or sealing is nearing its completion.

#### Sample 199 — After

- Similarity: 0.4711
- Prediction: The scrubbing motion is more pronounced, with the water dripping from the sink and the soapy residue forming on the surface. The hand's movements are more relaxed, with a more agitated hand securing the slats. The soapy water is absorbed by the soap, which is a reassuring sensation. The water's consistency is more uniform, with more water sprinkling on the lint, suggesting that the rinsing process is complete.
- Reference: The plate is now out of the water, with one hand holding it horizontally while the other hand, holding a sponge or cloth, is wiping it down. The surface of the plate looks almost completely free of soap suds, and its pattern is clear and unobstructed. The action of the hand with the sponge suggests a final wipe-down is being conducted to remove any remaining water marks or residues.

#### Sample 203 — After

- Similarity: 0.4144
- Prediction: The bottle is now in a more natural state, with the lid still attached to the bottle, indicating that the action has been completed. The hand is now more firmly held, demonstrating the heightened focus on the bottle's contents. The bottle'd contents are now more readily visible, implying that the bottle is being handled more carefully. The liquid content of the bottle has been reduced, highlighting the importance of the process.
- Reference: Now, the squash is positioned even higher, with the hand's grip adjusted accordingly to support the vegetable's weight from beneath. The fingers are curled more prominently around its body, indicating a firmer grasp as if preparing to place it down or to use it. The lighting reveals more of the squash’s textural details, highlighting its freshness and the care with which it is being handled to avoid any damage.

#### Sample 214 — After

- Similarity: 0.3549
- Prediction: The rinsing device is now in a more natural position, with the water running through the nozzle, indicating that the water has been drained. The hand's movements are more relaxed, demonstrating the ribbing action, which is likely to be a result of the scrubbing process. The water level is still a little higher than usual, suggesting that the hose is still running. The nozzle is still in the water, with a slight movement, implying that the rinse has been completed.
- Reference: In this frame, the cup is held directly below the faucet, but the faucet seems to be turned off. The cup is more filled with water, almost to the top. The water surface inside the cup is clearer, with fewer bubbles, indicating the filling process has recently completed or is nearing completion.

#### Sample 216 — After

- Similarity: 0.4477
- Prediction: The kettle has been removed from the frame, indicating that the hand is now in the position of its original position. The hand's position is more consistent with the previous frame, suggesting that the kettle is now positioned in a different position.
- Reference: In this frame, the coffee still presents an undisturbed surface, and the cup remains in the same position on the mat, but there is a subtle change in the lighting reflected off the coffee’s surface. The light seems to have shifted slightly, indicating either a minor change in the environment or the passage of time. However, the absence of any ripples or marks on the surface of the espresso suggests that it has not been moved or sipped, preserving the integrity of its initial state post-brew.

#### Sample 220 — After

- Similarity: 0.4923
- Prediction: The hose is now in a more natural position, with the water running through the nozzle, indicating that the water has been drained. The water's movement is more gradual, with a steady stream of water circulating around the hose, resulting in fewer hoses and less water. The nozzle's surface is more exposed, with water dripping from the spout, a sign of a reversing action. The hands are still firmly held, with their fingers pointing toward the rinsing device.
- Reference: In this frame, the cucumber is still under the faucet, but now it's angled differently, allowing the water to wash over another side of it. The hand has shifted position, cradling the cucumber more towards its end, which could indicate a rotation for an even wash. The other hand, previously holding a knife, is now absent from the scene, possibly set aside to facilitate better handling of the vegetable during the washing process.

#### Sample 222 — After

- Similarity: 0.3801
- Prediction: The water is now more concentrated, with the hands firmly engaged in the action. The water's surface appears to be a bit more damp, with a more pronounced crease and a slight slack in the center of the water. The hands are more agitated, with more water dripping from the water'll likely be present. The crease is more ragged, with less water splattering, and the water is more concentrated.
- Reference: The sponge is now at rest on the wooden surface next to the sink, free from any external pressure. It retains a slightly compressed form, likely due to its recent manipulation and not yet having fully rebounded to its original shape. The absence of any water being expelled or dripping suggests it has been sufficiently wrung out. Its dampness is implied by the slight glisten on its surface and the few water droplets scattered nearby.

#### Sample 223 — After

- Similarity: 0.3898
- Prediction: The plastic bag is now partially open, with the lid still firmly closed. The hand is now more likely to be holding the bag, indicating that the contents of the bag are being retrieved. The contents of this bag are now in the hands of the person who is preparing the bag. The bag's contents are now more readily accessible, implying that the bag is being accessed. The seal of the container is now firmly sealed, a sign of the effort to preserve the contents.
- Reference: The can is now more extensively opened. A greater portion of the aluminum lid has been pulled back, revealing the moist, chunky content of the tuna inside. The texture of the tuna is uneven, suggesting it may be in chunks or flakes. One can deduce from the partial view that it's possibly preserved in some form of liquid, possibly oil or brine, as it glistens slightly.

#### Sample 224 — After

- Similarity: 0.4254
- Prediction: The vegetables are now more tender, with a more pronounced texture. The skins are more charred, with the edges of the slices displaying a darker hue. The cooking process has been accelerated, with some vegetables showing signs of a softer texture.
- Reference: Now the courgette has been on the heat a bit longer. The act of stirring continues, which is an essential part of the cooking process to ensure even exposure to the heat. The pieces might have softened slightly, but there’s still no prominent change in color or char marks. The uniformity of the pieces helps in cooking them evenly, and it seems the cook is attentive to the process, as indicated by the consistent stirring and the pieces remaining intact without any signs of breaking down or overcooking.

#### Sample 225 — After

- Similarity: 0.3648
- Prediction: The blender's lid is now firmly held, with the lid still firmly attached to the blender' blade. The user's hand is now more likely to be holding the blender, which is likely to have been a previous step in the process. The hand's position is more relaxed, suggesting that the blender has been preparing to blend the ingredients. The blender remains in the hand, indicating that the user is now ready to use the blender.
- Reference: The mixture has reached a homogenously creamy state with a uniform yellow coloration and a smooth, glossy finish, consistent with a well-blended batter. The surface is free of any lumps or unincorporated patches, and the mixture now holds a ribbon-like trail from the beaters, which indicates good viscosity and structure. The overall volume appears to have increased, and the mixture maintains its shape around the beaters, demonstrating that sufficient air has been incorporated to give it a light, airy texture.

#### Sample 226 — After

- Similarity: 0.4865
- Prediction: The bread has been partially removed from the freezer, with the bread still firmly wrapped in the foil. The bread is now a more streamlined portion, with a slightly more rounded shape, indicating that the bread has not been fully removed. The hands are now more engaged in the process of removing the bread, implying that the loaf has been fully sliced. The creases on the bread are more noticeable, revealing a broader range of bread's texture and texture.
- Reference: The scissors are now absent, and the wrap has been cut, with the roll repositioned closer to the center of the counter. The cut edge of the wrap is not visible, suggesting that it has been neatly trimmed and possibly adhered to a dish or discarded. The layout of the kitchen counter shows a shift in focus towards other cooking activities, such as the microwave oven now entering the frame, hinting at the next steps in meal preparation. The wrap's previous tension is gone, indicating the cutting action is complete.

#### Sample 231 — After

- Similarity: 0.4649
- Prediction: The onion is now in a more streamlined state, with the fingers firmly pressed against the skin. The skin is now more exposed, with a broader range of movement, including the hand's movements. The fingers are more engaged, indicating that the onion has been fully inserted into the skin, allowing the skin to fully absorb the juices and nutrients it contains. The onion's surface is now a bit more exposed to the light, revealing a slightly more rounded appearance. The overall appearance of the onion is more consistent with the previous frame, with its shape and texture contrasting with the surrounding environment.
- Reference: The plastic bag's opening is now wider, with the fingers having stretched the opening further apart. The plastic material gathers and wrinkles more prominently at the points of tension near the fingers, showing increased manipulation. The potatoes inside the bag are more visible, and the bag’s form has changed from a sealed state to an open vessel, with the top part folded outward, revealing more of its contents. The plastic's texture appears softer and more pliable due to the opening action.

#### Sample 232 — After

- Similarity: 0.2331
- Prediction: The blender's lid is now firmly held, with the lid firmly pressed against the blender' blade, indicating that the blender has been fully cooled. The blender has now been fully removed, with no visible residue, suggesting that the lid is still attached to the blender. The lid remains in place, with a slight movement, implying that the blade is now fully seated.
- Reference: Here, the mixture displays more surface movement, evidenced by the ripples and peaks forming around the edges of the depression left by the mixer, signifying that the blending process is actively aerating the mixture. This active blending introduces air bubbles, which are crucial for creating a light and fluffy final product. The ingredient's color remains consistent, indicating a homogeneous mix without any color streaking or separation.

#### Sample 233 — After

- Similarity: 0.4340
- Prediction: The hand of the mat is now more firmly held, indicating that the hand is now in a more pronounced position. The hand is more flexed, demonstrating a greater grasping motion, a shift in the direction of the action. The mat's surface is now a bit more curved, suggesting that the mat has been positioned more horizontally. The surface of the table is now slightly more exposed, implying that the table has been placed in repositioning mode. The table's shape is more consistent with the rest of the frame, highlighting the heightened focus on the table' appearance.
- Reference: The plate has been placed down on the table, as evidenced by the absence of the person's hand and the stable, clear image of the plate. It rests solidly on the table, slightly overlapping the edge of the tablecloth, which is now neatly laid out without distortions. The plate's empty surface is fully visible, and it now resides next to a white tray with two pieces of food, which could suggest the person has finished serving or is about to serve themselves.

#### Sample 234 — After

- Similarity: 0.3493
- Prediction: The hand is now more firmly held, indicating that the hand is still in motion. The hand's position is more pronounced, suggesting that the person is now able to grasp the hand and move it around. The object's shape is more consistent with the hand'd motion, suggesting a more gradual movement. The hands are still in the same position, suggesting the hand has been able or is still able. The overall posture of the hand appears more relaxed, suggesting an effort to maintain a comfortable posture.
- Reference: The transformation of the mat is nearly complete. It presents itself with a sharp fold down the middle, the two halves nearly symmetrical, a sign of a deliberate and practiced movement. The orange tone of the mat now seems richer, the texture more evident as the lighting casts shadows within the folds, providing depth to the previously flat object. The mat's new shape is compact, hinting at the finality of the action, with just a corner lifted, poised for the last step in its folding sequence.

#### Sample 235 — After

- Similarity: 0.3850
- Prediction: The hand is now more firmly engaged in the action, indicating that the hand has been able to move the pot. The kitchen counter is now positioned in a position that is more likely to be used for cooking or for preparing food. The hand's position is more pronounced, suggesting that the pot is still in its current position. The pot's surface is still a little cluttered, suggesting a gradual movement, possibly a slight shift in the direction of the movement. The rim of the pot remains a tethered object, suggesting the pot may be a more stable position.
- Reference: Here, the grater has been repositioned further to the right, and its orientation has changed such that the top, where the handle is affixed, is now closest to the camera. The grater's shredding surface is now partly obscured by the handle from this angle, and the background clutter seems unchanged. This shift in position makes the grater more prominent in the frame and suggests an active engagement with it, possibly in preparation for use.

#### Sample 237 — After

- Similarity: 0.4515
- Prediction: The fish is now in a more streamlined state, with the skin separating from the meat. The person's hand is more relaxed, indicating that the fish has been fully cooked. The skin is still a little sloppy, but the texture is still consistent with the fish's texture. The fish' surface is more exposed, suggesting that the skin is a bit more tender. The chef's hands are more engaged, demonstrating a deeper penetration of the fish, which is likely a sign of the cooking process.
- Reference: The salmon is now almost entirely submerged, with only a small portion of its tail visible above the water. Bubbles rise around it, indicating the rapid descent and the displacement of water. The surrounding water appears disturbed, and the once shimmering scales are now masked by the water's overbearing presence.

#### Sample 238 — After

- Similarity: 0.3318
- Prediction: The bottle cap is now in a more upright position, with the fingers firmly pressed against the side of the bottle. The hand's angle is slightly different from the previous frame, suggesting that the bottle cap has been partially lowered. The bottle's contents are still present, with no visible signs of a previous action. The lid remains firmly attached to the bottle, with a tight grip on the cap. The cap's shape is more streamlined, indicating that the cap is being lowered, allowing the bottle to be viewed from a distance.
- Reference: The pouring action has reached its peak, with the flour leaving the jar in a fuller, more rapid stream. The pile of flour in the bowl has risen significantly, nearly doubling in size from the initial pour, and the top of the mound has a smooth, undisturbed surface. The cloud of flour dust has dissipated slightly, suggesting a slowing of the pouring action. There's a slight over-pour on the rim of the bowl, indicative of the speed and volume of the flour being transferred.

#### Sample 239 — After

- Similarity: 0.4131
- Prediction: The spout is now positioned in a more streamlined position, with the water running through the center of the sprig. The water's movement is more pronounced, with a slurry of water dripping from the bottom of the bowl. The rinsing motion is more intense, with more water splattering on the surface of the sink. The hand's movements are more relaxed, with water splashing from the sides of the basin. The sink's surface is more exposed, with less water escaping from the risina-like liquid.
- Reference: The dish is still under the stream of water, but the person's hands have changed position, suggesting a more thorough cleaning is taking place. The plate appears to be slightly cleaner than in the previous frames, with fewer food remnants visible. This implies that the water has successfully removed some of the debris. The hands are in a more manipulative position, possibly moving to start scrubbing with a sponge or to turn the dish to ensure all sides are rinsed equally.

#### Sample 240 — After

- Similarity: 0.4994
- Prediction: The pan is now more streamlined, with the ingredients incorporated more tightly, indicating that the ingredients are being stirred. The pan's surface is now slightly more exposed, implying that the pan is being stirmed more frequently. The water is now a little more spongy, suggesting that the water has been absorbed into the pan'd contents. The surface of the pan appears to be a bit more soaked in water, suggesting a more gradual cooking process.
- Reference: Here, the curry is visibly denser and has attained a thicker consistency. The ingredients within have softened significantly and have become an integral part of the curry. The simmering process seems to be at a more advanced stage, with the liquid bubbling gently. The overall hue of the curry is darker, and it looks rich and well-cooked, almost nearing its completion.

#### Sample 241 — After

- Similarity: 0.4526
- Prediction: The bowl is now in a more streamlined position, with the handle positioned slightly more vertically, indicating a gradual movement. The bowl's surface is now more cluttered, with a broader range of items and objects, including the kitchen counter, the sink, and the kitchen table. The kitchen counter is now cluttered with items, including dishes, dishes, and other items, a common feature in kitchens. The white and blue color of the bowl is consistent with the kitchen decor, with its contrasting hues and patterns.
- Reference: The ladle has been set down onto the white paper plate, with the bowl of the ladle now resting on the plate's surface. The handle extends towards the top left of the frame, crossing over the edge of the plate. The scene is largely unchanged apart from the ladle's movement; the table still holds the same items, and the glass remains untouched, with the liquid level consistent with the previous frames.

#### Sample 245 — After

- Similarity: 0.4298
- Prediction: The bowl is now more cluttered, with the ingredients positioned in a more streamlined position. The bowl's surface is more crowded, with less space for the ingredients to spread, indicating that the ingredients are being incorporated into the bowl. The hand motions are more consistent, with a slight movement in the direction of the bowl, implying that the bowl is being a bit more agitated. The blending process is more fluid, with more of the ingredients being distributed evenly across the bowl and the bowl'd contents.
- Reference: Here, the whisking has progressed further. The fork is actively churning through the egg mixture, creating a more homogeneous yellow color as the yolks and whites combine more thoroughly. The motion of the fork is more evident, indicated by the trails and ripples in the mixture. There are fewer clear whites visible, and the yolks are no longer distinct entities, signifying a deliberate and continued mixing effort to achieve a consistent blend for cooking.

#### Sample 248 — After

- Similarity: 0.3423
- Prediction: The door is now positioned in a more natural position, with the door's surface exposed. The hand's motion is more noticeable, indicating that the door has been closed. The door'd shape is more streamlined, revealing a wider range of space, including a larger window, a door handle, and a window. The light source is still visible, with a focus on the room's interior, highlighting the room as a whole.
- Reference: The light switch now shows one button fully depressed, indicating that the switch has been activated. The lighting condition, however, does not show a noticeable change from the previous frames. This could mean that the light has yet to turn on, the bulb is non-functional, or the change in lighting is too subtle to be captured by the camera. The hand remains in contact with the switch, and the shadow on the wall is consistent with the previous lighting condition.

#### Sample 250 — After

- Similarity: 0.4194
- Prediction: The spout is now in a more streamlined position, with the water running more smoothly. The water's flow is more concentrated, with a greater amount of water being drained from the spongy surface. The hand's movements are more relaxed, with more movement in the direction of the rinsing motion. The roiling action is more pronounced, with water flowing more smoothly through the nozzle. The hands' movements are less agitated, with less movement in their movements. The soapy water is still present, with no visible residue.
- Reference: The strainer is now positioned in a way that we can observe more of its mesh surface. Though still wet, it seems to have fewer water droplets than before, suggesting that the rinsing process is well underway or nearing its completion. The surrounding area and the items next to it, like a black pan, are also wet, suggesting the strainer might have been moved or shaken during the cleaning process.

#### Sample 252 — After

- Similarity: 0.2662
- Prediction: The knife is now a more precise and precise tool, indicating that the knife has been a bit more precise. The knife's surface is slightly uneven, revealing a sloppy, curved edge, a sharp edge, or a slight bend in the knife'd action. The blade's angle is slightly more pronounced, implying that the blade is a little more angled. The hand's position is more relaxed, demonstrating a smoother, more rounded motion. The surface of the knife is more ragged, displaying a slightly more firm grip, contrasting with the knife’s curved line.
- Reference: Here, the cake's integrity is further reduced by the removal of an additional slice. This action has created a larger gap in the ring, with two segments now missing. The texture of the cake is consistent with the previous images, and it continues to sit on the same decorative doily. The absence of the slices highlights the consistent golden-brown color of the cake's crust and the moistness of the interior, as inferred from the newly exposed edges.

#### Sample 253 — After

- Similarity: 0.2545
- Prediction: The sponge is now more firmly held, with the fingers pointing downwards. The sponge's surface appears to be a bit more soiled, with a more pronounced crease in the middle, indicating that the sponge has been fully soaked. The crease is more noticeable, with more of the sponge'd surface exposed, resulting in a smoother surface. The surface of the squeeze is more rounded, with less of a gap between the crease and the sponge, implying that the resulting squirt of water has been absorbed.
- Reference: The rag here has a slightly different posture, being maneuvered possibly to a different angle or direction. The grip on the rag seems firm, and its dampness is consistent with the previous frames. Some portions of the rag look more pressed down, likely from the cleaning motion and the force applied by the hand.

#### Sample 255 — After

- Similarity: 0.4137
- Prediction: The microwave door is now in a more natural position, with the hand firmly positioned in front of it. The hand's angle is slightly different from the previous frame, suggesting that the microwave door has been pushed open. The door's position is more pronounced, suggesting a gradual movement, and the microwave's interior appears to be a reflection of the microwave itself. The surrounding environment is still cluttered, with only the occasional light and a few items visible.
- Reference: Here, the hand appears to have finished its action, with the fingers slightly retracting, suggesting that a button or switch has been pressed. The positioning of the hand and fingers denotes a concluding action, hinting that the switch has been engaged or disengaged accordingly. The surroundings remain consistent with previous frames, further emphasizing the primary action involving the switch.

#### Sample 256 — After

- Similarity: 0.4070
- Prediction: The stove has been rearranged, with the lid still firmly attached to the stove, indicating that the burner is now fully cooled. The kitchen counters are now more visible, with a more streamlined appearance, reminiscent of the previous frames. The counters have been positioned in a slightly different position, with one of the handles pointing at the stove. The stove's surface is now more exposed, with only a few spots of visible light. The countertop is now cluttered with crumbs and other debris, a sign of a recent cleaning effort.
- Reference: The progression of interaction is evident as the hand has now grasped the grill grate, with fingers curled securely around one of the bars. The grate is slightly lifted, suggesting the initial stage of removal. The rest of the grill remains static, its cleanliness and the unaltered positions of the other grates indicating that this is perhaps the first grate being manipulated. The surrounding area, including a countertop and various kitchen items, remains undisturbed by the action taking place.

#### Sample 258 — After

- Similarity: 0.3458
- Prediction: The water is now dripping from the faucet, indicating that the water has been sprayed. The hand is now more likely to be holding the water, implying that the hand is preparing the water for the rinse. The water's consistency is more consistent, suggesting that the squeezing action is more gradual. The hands are still holding the hose, presumably a re-rinsing motion, and the water'n's movement is more pronounced. The hose's position is more relaxed, demonstrating that the hands are now more engaged in the water. The focus is now on the water and the nozzle, which is now in the hands of the person who is scrubbing the water to remove
- Reference: In this frame, the dish has been turned to expose a different angle to the viewer, revealing that the previously seen residues are now substantially reduced. The upper surface is now the primary focus, gleaming with moisture and displaying streaks of water that reflect the overhead lighting, indicating a recent rinse. The surrounding area of the sink is splashed with water, and the dish appears to be in the final stages of being cleaned, with only minor remnants of residue left.

#### Sample 261 — After

- Similarity: 0.4335
- Prediction: The tomato has been sliced in half, with the knife pointing at the center of the cutting board. The knife's edge is now slightly angled, suggesting that the knife is a bit more angled. The tomato's surface is slightly sloppy, with a thin layer of the tomato'd portion forming a clump of seeds. The hand motions suggest that the cutting is now a little more slouchy, indicating that the hand is preparing the tomato for cooking.
- Reference: By this point, the chilli's dispersion looks even more uniform, suggesting the individual making the pizza has made further adjustments. The slices seem to have settled onto the toppings, resting comfortably among the corn, onions, and other ingredients. The moisture or slight sheen on some of the chilli slices implies they are fresh, holding onto their natural juices.

#### Sample 264 — After

- Similarity: 0.4452
- Prediction: The water has cooled, and the noodles are now more tender, with a more pronounced texture. The water is now more scalding, with the noodles separating from the broth, indicating that the water has been absorbed into the noodles. The color of the noodles is now a vibrant hue of brown, with some of the water clumping around the edges, suggesting that the noodles may be partially cooked. The texture of the soup appears to be more acrid, with more of the liquid clumped around the noodles, forming a clunky texture.
- Reference: The stirring has become more vigorous, creating a swirling effect that momentarily reveals the bottom of the pot. The increased agitation suggests that the cook is either checking for doneness or incorporating the ingredients more thoroughly. The consistency of the curry appears to be slightly reduced from the earlier frames, with a glossier sheen on the surface, implying that some of the liquid has evaporated and the sauce has thickened. The steam is more pronounced, indicating the continuation of the cooking process.

#### Sample 265 — After

- Similarity: 0.4117
- Prediction: The bread has been partially opened, with the bread's edges exposed. The bread' s surface is slightly exposed, with a slight crease in the middle of the bread. The hand's movement is evident, with one hand firmly grasping the bread, indicating that the bread has reached its final position. The sandwich's shape is more pronounced, with its edges exposed, suggesting that the sandwich may be a more streamlined portion. The overall appearance of the sandwich is more uniform, with some of the edges showing signs of a crease or a small gap.
- Reference: The coffee bag now exhibits a more pronounced opening, with the top separated enough to reveal the inner seal and possibly some of the coffee product inside. The person's hands have adjusted their grip, indicating the opening process is nearly complete. One can infer that the aroma of the coffee may be starting to permeate the area, as opening the bag this much would release the scent. The bag maintains its central placement on the cutting board, even as it transitions from sealed to unsealed.

#### Sample 267 — After

- Similarity: 0.3872
- Prediction: The onion is now partially sliced, with the skin still exposed. The hand is now more firmly grasping the onion, indicating that the knife has been slicing the fruit. The skin is now a little more exposed, revealing a more rounded appearance. The onion's skin is still a bit sloppy, displaying a slender appearance, suggesting that the peel may have been trimmed. The knife's grip is still firm, suggesting the knife'd action is likely to be more deliberate.
- Reference: Progress in the sweetcorn's reveal is evident as the can opener has now traversed a significant portion of the can's circumference. The lid is partially detached, with a noticeable gap indicating the path the opener has taken. Corn kernels are now visible, peeking through this gap, their yellow hue contrasting with the metallic sheen of the can's interior. The user's hands are actively engaged in the process, suggesting that the opening sequence is close to completion, and the sweetcorn will soon be fully accessible.

#### Sample 271 — After

- Similarity: 0.3824
- Prediction: The bowl is now in a more natural position, with the handle still firmly held, indicating that the action has taken place. The bowl's surface is now more exposed, with a broader range of motion, including a movement in the kitchen or bathroom. The hand's movements are more relaxed, demonstrating a shift in focus from the previous frame. The kitchen's lighting is now dim, with only a few visible objects, such as the sink and counter, reflected in the background.
- Reference: The action of squeezing has resulted in a substantial amount of washing up liquid pooled at the base of the bowl, with the stream now thicker and more copious. The surface of the liquid pool is uneven, with ripples and bubbles indicating recent disturbance. Some liquid has started to spread out from the initial point of contact, with tendrils of green stretching outwards, showing the beginning stages of dispersion through the water present in the bowl.

#### Sample 272 — After

- Similarity: 0.4518
- Prediction: The spout is now held in a more streamlined position, with the water running through the center of the sprig. The water's flow is more concentrated, with a greater focus on the rinsing action, indicating that the nozzle is now rubbed with water. The reek's surface is now more spongy, with more water dripping from the hose, resulting in fewer bubbles. The hand's movements are more relaxed, with their movements indicating a thorough rinse.
- Reference: The ladle has been reoriented yet again, with the bowl now facing towards the person, who is using a sponge to scrub its interior. The sponge is held in the left hand, covered in suds, suggesting vigorous cleaning action. The stream of water from the faucet is directed at the ladle, likely to rinse off the soap as the cleaning progresses. The overall setting remains unchanged, with the cleaning materials and kitchen utensils maintaining their presence in the backdrop.

#### Sample 273 — After

- Similarity: 0.4711
- Prediction: The sink is now more streamlined, with the water running more smoothly. The hand is now able to grasp the sponge, which is now in a more soiled state, indicating that the sponge has been thoroughly washed. The water's movement is more consistent, with a squeezing motion, suggesting that the water has been sucked away. The sponge's surface is now cleaner, with less water splatter, suggesting a deeper cleaning process. The sink's current position is more cluttered, with more water circulating around the sponge. The soapy residue is visible, with some of the soapy particles lingering in the water.
- Reference: The countertop remains consistent in its dark hue. The image provides a view closer to the floor level, revealing the lower portion of the cabinets or drawers under the countertop. The hand, now empty, is moving away from the yellow plastic bag, suggesting that the contents were perhaps placed or discarded. The edge of the sink can also be spotted in this frame, reinforcing the continuity of the actions from the previous frame.

#### Sample 278 — After

- Similarity: 0.3171
- Prediction: The dough is now more firmly held, with the edges of the dough being more exposed. The hand's movements are more deliberate, indicating that the dough has been kneaded. The dough's surface is more abrasive, with a more uniform texture and a smoother surface. The hands' movements are less pronounced, implying that the flour has been placed on the dough.
- Reference: The majority of the cling film remains held aloft, displaying even more of its surface area. The presence of more pronounced wrinkles and slight deformations is evident due to the manual handling. It seems the film has yet to be fully detached from its package, and the individual's hands actively engage with it, ensuring its spread and position.

#### Sample 279 — After

- Similarity: 0.4495
- Prediction: The microwave has been moved to a more stable position, with the lid still slightly open, suggesting that the action is complete. The kitchen's lighting is now dim, with a light source indicating that the microwave is still on. The surrounding environment is still dim, including the kitchen'd kitchen counter, which is still visible in the background. The microwave's interior remains dim, indicating a gradual movement, with no visible objects or objects.
- Reference: The cabinet door is now almost completely closed, with only a small gap remaining. The motion blur has decreased, implying that the speed of the closing action has reduced as the door nears its fully closed position. The contents of the cabinet are no longer visible due to the narrow opening, and the door is nearly flush with the cabinet frame, indicating that the action of closing the cabinet is almost complete.

#### Sample 280 — After

- Similarity: 0.3573
- Prediction: The table is now more cluttered, with the surface of the table a bit more bare and cluttered. The hand is now positioned in a more natural position, indicating that the table is still in its place. The table's surface is now slightly more exposed, with a slight movement, implying that the hand is still holding the table. The surface of this table is more crowded, with more people gathered around the table, presumably a sign of the time.
- Reference: The scene remains a whirl of colors and shapes due to motion blur, with the toaster even less discernible than before. It's apparent that the camera or the person is moving quickly, creating an almost abstract composition of kitchen elements. The blur conveys a sense of urgency or haste. The toaster, while present in the scene, has become an element of the background, overshadowed by the blur of motion that dominates the frame.

#### Sample 284 — After

- Similarity: 0.3485
- Prediction: The pan is now more streamlined, with the edges of the meat separating from the vegetables. The meat has been steamed, indicating that the cooking process has been completed. The pan's surface is slightly charred, suggesting that the meat has a more pronounced texture. The surface of the pan is still covered in a thin layer of fat, suggesting a gradual cooking process. The cooking process is now complete, with a smoother surface and a longer cooking time.
- Reference: The pasta has reached a state where it looks thoroughly combined with the pesto sauce. Each rotini curl is drenched in the vibrant green sauce, reflecting a creamy and appetizing appearance. The consistency looks rich, suggesting that the ingredients have melded well. The wooden spoon appears to be scooping up a portion, possibly checking the texture or taste.

#### Sample 286 — After

- Similarity: 0.4611
- Prediction: The pan is now more streamlined, with the ingredients incorporated more evenly. The pan's surface is more crowded, with more of the ingredients being distributed evenly across the pan. The spoon's motion is more deliberate, indicating that the ingredients are being distributed more evenly across each pan.
- Reference: In this frame, the mixture has been further spread out with the help of a fork, which is also being used to gently stir the vegetables. This suggests an effort to evenly cook all pieces. Some of the vegetables, especially the tomatoes, appear to have softened slightly, as evidenced by the slight glistening and change in texture. The mixture's color remains vibrant, indicating that the cooking process is being managed carefully to avoid overcooking while ensuring that the heat is evenly distributed.

#### Sample 292 — After

- Similarity: 0.4985
- Prediction: The spout is now in a more streamlined position, with the water running more smoothly. The water is now dripping from the faucet, indicating that the spongy surface is being rinsed. The rinsing motion is more focused, with a focus on the raffination of the nozzle and the resulting soapy residue.
- Reference: The mug is in a near-upright position, and the water level has risen close to the brim, signifying that the filling process is almost complete. The stream of water has caused frothy bubbles to accumulate at the top, and the previously visible residue seems to be diluted or washed away by the continuous flow of water. The handle of the mug now points slightly left, indicating a subtle repositioning by the person handling it.

#### Sample 294 — After

- Similarity: 0.3921
- Prediction: The pan is now in a more natural state, with the surface of the pan being more exposed to the water. The person's hand is now more focused on the surface, indicating that the pan has been thoroughly cleaned. The pan's surface is now a bit cleaner, with a less noticeable streak of water on the bottom. The surface of this pan is more exposed, with more water absorbed from the surface. The kitchen sink appears to be a little more cluttered, with less water dripping from the sink. The sink's counters and sink counters are now more visible, demonstrating the presence of a sprinkling of water.
- Reference: The towel re-emerges, this time being used more deliberately. It is held in one hand, fingers extended, applying a degree of pressure against one of the stove burners, indicating a scrubbing or wiping motion. The fabric appears to be slightly more soiled than before, consistent with its use in cleaning a cooking area. The spread of the fingers and the position of the towel suggest a more focused cleaning effort is being made, possibly after a preliminary cleaning or assessment of the area's condition.

#### Sample 295 — After

- Similarity: 0.4766
- Prediction: The scrubbing motion is more pronounced, with the water running more smoothly. The hand is now more firmly held, indicating that the squeezing action has been completed. The water level is less noticeable, with a more concentrated amount of water being drained from the nozzle. The nozzle is still firmly positioned, with no visible streaks of water visible. The soapy residue remains on the surface, with some residue still visible, suggesting that the soap has been sprayed.
- Reference: The cleaning process seems to have progressed, as the strainer is now being wiped from the inside out with a white cloth that is likely absorbing moisture and dislodging any remaining particles. The sponge has been set aside, indicating that the scrubbing action has been completed. The water flow has resumed, suggesting a final rinse. The interior of the strainer looks significantly cleaner, with fewer visible food particles, and the white plastic appears to have regained some of its original brightness.

#### Sample 297 — After

- Similarity: 0.2951
- Prediction: The chicken is now a more seasoned, charred, and steamed, with the skin still a little charring. The hands are now more engaged in the process, with a heightened focus on the meat's texture and texture. The skin is now more charmed, with more of the meat separating from the skin, indicating that the chicken is ready to be cooked.
- Reference: The board is now tilted at a steeper angle towards the pan, and the garlic paste has been mostly scraped off, leaving only a slight residue on the surface. The person's grip on the knife has changed to a more precise and firm hold, focusing on ensuring that all of the garlic is removed from the board. The hand holding the board has adjusted its position to facilitate the transfer of the garlic into the pan, and the fingers are curled to avoid contact with the knife or the hot surface of the pan.

#### Sample 298 — After

- Similarity: 0.3502
- Prediction: The pan is now positioned in a more streamlined position, with the handle pointing downwards, indicating that the water has been drained. The water's surface is now more rounded, suggesting that the pan is being dipped in water. The pan's appearance is more reminiscent of a kitchen sink, with a sprinkling of soapy water on the surface, a sign of dripping water.
- Reference: The gloves in this frame are presented in a state of action. The left hand, clad in the yellow rubber glove, is actively engaged in holding a dark frying pan, while the right hand appears to be reaching towards or withdrawing from an interaction with the pan or another object just outside the frame. The gloves are more stretched across the palms and fingers compared to the previous frames, indicating a firmer grip and a dynamic movement.

#### Sample 303 — After

- Similarity: 0.4756
- Prediction: The bottle is now in a more natural state, with the lid still attached to the bottle. The hand is now more firmly held, indicating that the cap is now fully closed. The bottle's contents are still visible, with no visible signs of a previous action. The lid remains in place, with a tight grip, implying that the bottle is still in its original state.
- Reference: The scene portrays the can in a more pronounced tilted angle, suggesting an active pour. The fluid is visible midway, cascading into the already partially filled glass. The glass captures the liquid's effervescence, with bubbles hinting at the carbonated nature of the drink. The person's grip has adjusted to facilitate the pour, and the wrist's metallic accessory shines under the ambient light.

#### Sample 304 — After

- Similarity: 0.2323
- Prediction: The hose is now in a more natural position, with the water still circulating in the air, indicating that the water has been drained. The water's movement is more pronounced, suggesting that the hose has been placed in re-circulation mode. The nozzle's position is more apparent, with a broader range of motion, including a movement in the direction of the nozzle or a motion in the movement of the water. The movement of water is more evident, with water flowing from the spout to the holder of the sink.
- Reference: The transformation of the tin reaches a new phase as it now holds a quantity of water, with its surface partially submerged. The water reflects the kitchen's ambient light and surroundings, introducing a glossy sheen that contrasts sharply with the matte and tarnished finish of the tin's unwetted interior surfaces. The water's presence introduces a visual softening of the tin's hardened deposits, implying a preliminary step in a cleansing process.

#### Sample 306 — After

- Similarity: 0.4230
- Prediction: The sponge is now more firmly held, with the handle still firmly positioned, indicating that the water has been sprayed. The sponge's surface appears to be a bit damp, suggesting that the soap has been removed. The water's consistency is more pronounced, suggesting a more thorough cleaning. The soap's color is more vibrant, suggesting the soap is abrasive, and the sponge'd surface is more clean. The hand's movements are more relaxed, suggesting they are focusing on the sponge. The surface of the sponge appears to have been washed away, suggesting it has been wasstained.
- Reference: The rolling pin now rests on the edge of the sink, with attention focused on cleansing a white plate. The pin is no longer the central object of cleaning but remains in the scene, possibly awaiting a final rinse or to dry. The soapy water on the pin has formed small puddles on the stainless steel sink, separating the cleaning zones between the plate and the pin. The pin's handles protrude outward, suggesting that it might be picked up again soon.

#### Sample 308 — After

- Similarity: 0.3822
- Prediction: The rinsing device is now in a more natural position, with the water running through the surface of the ricotta, indicating that the water has been drained. The water's movement is more pronounced, with a broader range of movements, including a hand-held tap, which indicates a thorough rinse. The hands are more relaxed, with their movements indicating a deeper rinse.
- Reference: The baking tray now lies flat in the sink with a generous amount of foamy soap suds covering its surface. The water is still running, and the person's hands are actively scrubbing the tray, indicating a thorough cleaning process. The soap suds are dense and white, almost completely obscuring the surface of the tray, which suggests that a good amount of dish soap has been used to ensure a thorough cleanse. The tray is almost unrecognizable under the frothy layer, showing a significant transition from the initial state.

#### Sample 309 — After

- Similarity: 0.2786
- Prediction: The steamed broccoli is now more thoroughly soaked in water, with the skin still moistened and charred. The hands are now more engaged in the process, indicating that the squeezing action has been completed. The rinsing motion is more consistent, implying that the water has been drained out of the broccoli, resulting in a more concentrated stream of water. The water's consistency is more uniform, suggesting that the broccoli is being rinsed more thoroughly. The skin is now a little more exposed, suggesting a deeper rinse than the previous frame.
- Reference: The tap continues to be in its downward position over the sink. Water is gushing out from the spout with a higher intensity compared to the previous frame. The flow is forceful, resulting in more water splashes within the sink. The clarity and consistent nature of the water suggest it's likely at a cold temperature.

#### Sample 312 — After

- Similarity: 0.3929
- Prediction: The onion is now a more steamed, charred, and trimmed, with the skin still a little more exposed. The person's hand is now more firmly grasping the onion, indicating that the knife has been a bit more pressed. The onion's skin is now slightly soiled, revealing a smoky appearance. The knife's surface is more exposed, implying that the onion has been partially sliced. The slicing motion is more pronounced, demonstrating the emergence of a newer, more rounded onion.
- Reference: The process progresses with more green beans being trimmed and added to the collection in the colander. The person's hands are active, with the right hand holding a green bean and the left hand seeming to have just released a trimmed bean into the colander. The contrast between the trimmed beans inside the colander and the untrimmed ones still in their packaging is quite apparent. The trimmed beans have a uniform appearance, with clean cuts at both ends, while the ones awaiting preparation display their natural, uneven tips.

#### Sample 317 — After

- Similarity: 0.4375
- Prediction: The bread has been re-opened, with the bread's shape and texture more apparent. The bread is now more firmly held, with a more pronounced bite, indicating that the bread has reached its final state. The hands are now more engaged in the action, demonstrating the bread being more pressed together. The hand's movements are more relaxed, revealing the bread as a whole, a sign of the bread's progress.'
- Reference: The mozzarella now appears more evenly distributed across the dough's surface, although the distribution is not perfectly uniform, suggesting a hand-spread method. There are areas with a denser coverage and some spots that have less, showing a natural variance in the spreading technique. The individual strands of cheese are visible again and remain separate, retaining their structure without clumping or melting. The cheese still holds the pale cream color, and the lighting highlights its soft texture.

#### Sample 320 — After

- Similarity: 0.3881
- Prediction: The chicken is now positioned in a more secluded position, with the fingers firmly pressed against the skin. The hand is now more reliant on the knife, indicating that the chicken has been fully seated. The skin is now slightly exposed, suggesting that the hand is preparing the chicken for cooking. The chicken's surface is now exposed, implying that the chef has mastered the art of preparing a meal.
- Reference: The sweet potato skin here is mostly separated, with only a small portion still attached at the end of the vegetable. The accumulation of peelings on the cutting board has grown, and some peel segments have escaped onto the counter, showing the progression of the peeling task. The skin's moisture has begun to dull as exposure to the air has set in, and there is a noticeable decrease in the vibrancy of the orange color. The knife and fork are now lying on the cutting board, indicating a pause or the completion of peeling.

#### Sample 321 — After

- Similarity: 0.3734
- Prediction: The spout is now in a more streamlined position, with the water running more smoothly. The water's flow is more concentrated, with a greater focus on the spongy areas, which are likely to be a result of the rinsing process. The hand's movements are more relaxed, with more movement in the direction of the water'd flow. The reek's surface is more pristine, with less water dripping from the nozzle, suggesting that the nipples are now able to rinse away excess water.
- Reference: The pan's position has been further adjusted, with its bottom now more visible and facing upwards. This orientation suggests that the pan might have been rinsed or is in the process of being scrubbed. The previously visible dark liquid is no longer apparent, indicating it has likely been rinsed away. The hand that was holding the handle now grips the edge of the pan, giving better access to its interior for a thorough cleaning. Adjacent to the pan, the environment still has scattered utensils and dishes, some of which appear to be wet, hinting at ongoing washing activity.

#### Sample 325 — After

- Similarity: 0.4932
- Prediction: The peel has been removed, with the skin still firmly attached to the stem. The knife's action is more deliberate, indicating that the peel has a more pronounced bite, resulting in a smoother, more tender slice. The skin is now more ripe, with a larger portion of the peel separating from the skin, revealing a softer, more spongy appearance. The peel is now a little more firm, with more of the skin exposed, exposing more of its flesh.
- Reference: The transformation of the kiwi is nearly complete, with only a small portion of skin left attached. The majority of the fruit has been cleanly scooped out, sitting diced on the plate, ready for consumption. The kiwi now resembles a hollowed-out shell, with the edges of the remaining skin slightly curled inward, a testament to the meticulous peeling process. The fruit's green flesh, now detached, is neatly cut into cubes, demonstrating the careful preparation.

#### Sample 327 — After

- Similarity: 0.3894
- Prediction: The bin's lid is now positioned in a more natural position, with the lid's surface exposed, suggesting that the lid has been removed. The lid'd position is more apparent, with a curved edge indicating that the bin is now fully closed. The bin is still in its original position, and the lid remains in its current position.
- Reference: In this frame, the lunch box is in the midst of a dynamic moment, positioned at an angle that suggests it is being actively tipped over. Human hands are visible, gently guiding the box, which remains closed. The box now shows signs of contact, with a human element introduced into the scene, adding a sense of intentionality to the action. The environment remains consistent with the domestic kitchen setting, and the presence of the individual implies a deliberate interaction with the lunch box.

#### Sample 328 — After

- Similarity: 0.4019
- Prediction: The bag is now in a more streamlined state, with the lid still firmly attached to the bag. The hand is now more reliant on the bag's surface, indicating that the bag has been fully opened. The bag'd contents are still visible, with no visible signs of damage or damage. The lid remains in place, with a slight movement, implying that the contents are being discarded.
- Reference: The bread is now fully inside the toaster, no longer visible, indicating the toasting process is underway. The hand that was previously holding the bread is now absent from the frame, suggesting the person has completed the action of inserting the bread into the toaster. With the bread out of sight, the toaster becomes the new focal point, its design and the red indicator light suggesting it is working to crisp the bread slice within.

#### Sample 329 — After

- Similarity: 0.4178
- Prediction: The coffee pot is now in a more natural state, with the lid still attached to the pot. The hand is now more firmly grasping the lid, indicating that the action has taken place. The lid remains attached to its base, implying that the lid is now fully closed. The lighting is still dim, with a focus on the coffee pot's interior. The surrounding environment is still a focal point, with no visible objects or objects, such as the kitchen counter or the kitchen sink.
- Reference: The bag is significantly more open in this frame, with a substantial portion of its contents now visible. The hand is holding onto the bread, indicating an intention to possibly take it out or examine it. The surrounding items remain in place, emphasizing the main action taking place with the bag and its contents. The transparency of the bag offers a clear view of the bread inside, revealing its shape, size, and texture.

#### Sample 332 — After

- Similarity: 0.3250
- Prediction: The oven door is now fully open, with the person's hand firmly positioned in the middle of the oven. The person'd hand is now more firmly grasping the door, indicating that the oven has been closed. The door's surface is slightly curved, suggesting that the person is now able to grasp the door. The kitchen environment is still cluttered with the usual household items, including the kitchen sink, sink, and counter, as well as the surrounding area.
- Reference: The drawer now appears fully closed, with no visible gap, indicating the completion of the action. The blur has diminished, suggesting that the motion has halted, and the freezer is sealed. The surface of the drawer is smooth, and there are no signs of obstruction, indicating a successful closure. The freezer is now likely returning to its optimal temperature to preserve the contents inside.

#### Sample 333 — After

- Similarity: 0.4246
- Prediction: The jar is now in a more streamlined state, with the lid still firmly attached to the plastic. The hand is now more reliant on the spoon, indicating that the jar has been fully opened. The rim of the jug is now slightly curved, suggesting that the spoon is now positioned in descending order. The spoon's surface is now less cluttered, suggesting a gradual movement, with a focus on the rim and the spout.
- Reference: The bread re-emerges, now being handled more directly with both hands. The plastic bag appears to be peeled back further, exposing more of the bread's surface. This bread has a defined structure, possibly indicating that it is a whole piece rather than slices. The person's actions seem careful and deliberate, as if trying to preserve the bread's integrity while removing it from the bag.

#### Sample 334 — After

- Similarity: 0.3818
- Prediction: The paper bag is now in a more streamlined state, with the hand firmly holding the bag, indicating that the contents are being sucked out of the bag. The hand's movements are more deliberate, implying that the bag is being pushed open, resulting in fewer pieces of paper. The bag's contents are still in the bag'd state, displaying a slender appearance, reminiscent of a bag of rolled paper.
- Reference: The application of the creamy substance seems to have been completed. The knife, now carrying minimal residue, is pulled away from the bread, which is held steady in the other hand. The spread is more uniform across the bread's surface, though some natural undulation in its thickness remains. The crust edge of the bread appears unblemished by the spread, preserving its crisp texture. The hand holding the bread is poised as if preparing to place the bread down or to bring a second slice to complete the sandwich.

#### Sample 335 — After

- Similarity: 0.3424
- Prediction: The table is now more firmly held, with the hand positioned in the middle of the room, indicating that the table is being wiped down. The hand is now positioned slightly further away from the table, demonstrating the emergence of a newer, more pronounced hand. The table's surface is now slightly more exposed, with a more defined appearance, reminiscent of tiling or a rolled towel. The creases and wrinkles are more prominent, contrasting with the rest of the table'd surface.
- Reference: In this frame, the degreaser's presence is evidenced by a layer of liquid across the surface, with a significant reduction in airborne droplets. The hand and bottle are now absent, indicating that the spraying action has ceased. The surface of the countertop shows a consistent wet sheen, highlighting the even distribution of the degreaser. The wet area has expanded further, showing the progression of the liquid as it moves outward from the point of initial contact. The pattern of the countertop is slightly obscured by the sheen of the degreaser, displaying the product's coverage.

#### Sample 338 — After

- Similarity: 0.2209
- Prediction: The pan is now a bit more streamlined, with the edges of the meat separating from the sides, indicating that the meat has been fully cooked. The pan's surface is slightly more exposed, with a more uniform appearance of the pan'd meat, which is likely a sign of the cooking process. The meat is now more tender, with more of the skin separating, resulting in a smoother texture. The surface of the skillet is now slightly more curved, revealing a broader range of textures, including a slightly more densely-shaped texture.
- Reference: The extractor fan remains in the same state as before, maintaining its heavily used appearance with a stubborn layer of grime. The lack of light reflection on its surface reinforces the idea that the fan is not operational, and there seems to be a consistent lack of maintenance, which is evidenced by the undisturbed grease deposits. The fan's surroundings, including the wall tiles and the stovetop, also show signs of use, correlating with the condition of the fan, suggesting a kitchen that is frequently used but not frequently cleaned.

#### Sample 341 — After

- Similarity: 0.3512
- Prediction: The scrubbing motion is more streamlined, with the water running more smoothly. The hand is now more focused on the squeezing action, indicating that the water has been drained. The water's movement is more consistent, with a more gentle motion indicating the water is dripping. The rinsing motion is less pronounced, with more water being dripped onto the risotta. The hands are still firmly held, with their fingers pointing at the resealing motion.
- Reference: The tablecloth is now draped over the sink's divider, its apple design partially obscured by the curvature of the fabric as it conforms to the sink's shape. Water droplets are scattered across the surface, some merging to create larger rivulets that travel along the cloth's folds and undulations. The image conveys a sense of motion and fluidity, with the previous crispness of the apple design softened by the water's influence.

#### Sample 346 — After

- Similarity: 0.4021
- Prediction: The spout is now in a more streamlined position, with the water running more smoothly. The water's flow is more concentrated, with a greater focus on the spongy areas, which are likely to be a result of the rinsing process. The hand's grip is more relaxed, with more movement, indicating that the nozzle is now rubbed with water. The reek's surface is more rounded, with less water dripping from the hose, resulting in fewer bubbles. The hands' movements are more relaxed and more agitated, demonstrating the reversing of the water'n's action.
- Reference: The teaspoon is now being rinsed for a final time, held at the stem with the concave side once again facing the water stream. The cleansing process seems to be nearing completion, with the water flowing smoothly over the spoon's surface, indicating that any previously present debris has been cleared. The metal gleams under the water, signifying a clean and reflective finish.

#### Sample 347 — After

- Similarity: 0.4384
- Prediction: The hand of the person holding the towel is now more firmly held, indicating that the towel has been placed in a position where it is being handled. The hand is now positioned in overlapping positions, implying that the hand is a more pronounced position, a sign of the hand's effort to grasp the towel. The towel's surface is now slightly more exposed, demonstrating the hand-hand motion, allowing the towel to move more easily. The hands are still firmly grasping the towel, revealing a broader range of motions, including the hand, hand, and the towel'd surface.
- Reference: In this frame, the tea towel is almost entirely folded, with just a small section still being adjusted by a hand. The striped pattern is now displayed in layered bands, with the colors stacking upon each other due to the folding process. The overall shape of the towel has become more compact, representing a neatly arranged rectangle, while still retaining its smooth texture.

#### Sample 348 — After

- Similarity: 0.4522
- Prediction: The refrigerator door is now open, with the door open and the contents of the fridge adrift. The hand is now more firmly grasping the door, revealing a more streamlined appearance. The contents of this compartment are now more visible, including the contents, such as the contents in the refrigerator. The refrigerator's interior is now cluttered with items, including food, dishes, and other items.
- Reference: The hand in this image is in clear focus, reaching towards the spice jars with intent, specifically aiming for one of the jars on the shelf. The cabinet contents are now visible, with labels facing outward, showing a mix of perhaps ground spices or dried herbs. The environment remains consistent with the previous frames, indicating a sequence of actions in the same setting.

#### Sample 351 — After

- Similarity: 0.2801
- Prediction: The bag of rice is now in a more streamlined state, with the hands positioned more horizontally, indicating that the rice has been placed in re-ordering mode. The hands are now more engaged in the action, demonstrating the emergence of the rice as a raw product. The creases and wrinkles are more prominent, suggesting that the bag has been rearranged, a sign of the ongoing process of preparing the rice.
- Reference: In this frame, the action of capping the olive oil bottle has progressed further. The cap is now partially obscured by the hand, suggesting that it has been placed over the bottle's opening and is likely in contact with the bottle's rim. The person's hand is stretched towards the bottle, which remains out of view, and the downward pressure indicates that the cap is being twisted to secure it in place. The cap appears slightly tilted, a common occurrence when initiating the twisting motion to seal a screw-top bottle.

#### Sample 353 — After

- Similarity: 0.4538
- Prediction: The hand is now more firmly engaged in the action of removing the lid from the machine, indicating that the lid has been removed. The hand's position is more relaxed, suggesting that the hand is preparing to remove the lid. The surrounding environment is still a little damp, with the surrounding environment reminiscent of a kitchen setting. The user's hand is still holding the lid, presumably a sign of the process of adjusting the lid's function.
- Reference: The button now appears to be fully engaged, pressed down to its furthest extent. The change in elevation from its original position is apparent, with the finger firmly applying pressure. The shadow cast by the finger is now more pronounced and confined to a smaller area directly around the point of contact, indicating that the button is at its lowest position. The surface of the button that was once reflective is now mostly obscured by the finger, and the surrounding buttons remain static, undisturbed by the action of this single button being pressed.

#### Sample 354 — After

- Similarity: 0.4385
- Prediction: The pot is now in a more natural state, with the lid still firmly attached to the pot, suggesting that the water has been boiled. The hand's motion is more relaxed, indicating that the pot is still in its current state. The water level is still a little higher than the previous frames, suggesting a gradual increase in the water content of the pot. The pot's surface is still slightly damp, suggesting the pot may be a bit damper than usual. The kitchen environment is still dim, with a cluttered kitchen and bathroom area reminiscent of a kitchen or dining room setting.
- Reference: In this capture, the ladle has been placed down on the white countertop, lying flat and still. The positioning is near the bottom edge of the frame, with the handle parallel to the bottom border of the image. This suggests the completion of an action, as the hand that was holding it has now moved away, indicating release. The environment includes a sink filled with various kitchen items, signaling ongoing or recently concluded kitchen activity. The water bottle that was previously rolling has come to rest, and the wooden spoon remains undisturbed in its holder.

#### Sample 358 — After

- Similarity: 0.4780
- Prediction: The frying pan has been re-positioned, with the handle still firmly held, indicating that the heat has been applied. The hand's motion is more focused, suggesting that the pan has a more natural appearance. The kitchen's lighting is now more dim, with a focus on the kitchen'd surface, highlighting the absence of a stovetop burner. The surface of the pan is now a little more reflective, suggesting a gradual change in the lighting conditions. The rim of the oven door is now slightly wider, suggesting the oven's surface is more reflective. The pan's temperature remains the same, suggesting an increase in the heat level.
- Reference: The hob's surface gleams, with no evidence of food spills or stains, reflecting meticulous maintenance. The grilles covering the burners appear untouched, with no discoloration from heat or cooking. The knobs on the control panel are pristine, with the blue indicators sharply pointing towards the off position. The cleaning cloth has moved slightly, now positioned over one of the burners, with the hand in the same watch-wearing position, suggesting a continuous cleaning motion.

#### Sample 359 — After

- Similarity: 0.2456
- Prediction: The water is now dripping from the faucet, indicating that the water has been sucked out. The water's movement is more gradual, with the water sprinkling onto the surface of the water'll likely be more concentrated. The hands are still holding the water, demonstrating the squeezing motion, which is likely a sign of a more active watering process. The squirt is still a bit more pronounced, with a slight movement in the direction of the rinsing motion.
- Reference: In this frame, the bin remains in the same location, but the person's hand is now retracting from the area, implying that an item may have been deposited into it. The fill level of the bin appears consistent with the previous images, maintaining its overfilled state. The plastic liner bulges slightly outward, a sign of the bin's capacity being maximized. The environment around the bin, particularly the dish rack and the countertop, shows no noticeable change, reinforcing the ongoing use of the space for kitchen activities.

#### Sample 364 — After

- Similarity: 0.1853
- Prediction: The hand is now more firmly grasped, indicating that the hand is preparing to use the pot. The hand's position is more relaxed, suggesting that the pot is still in its current position. The kitchen environment is still cluttered, with the kitchen still awash in clutter and clutter. The pot's surface is still visible, with a bare countertop and counter top, a kitchen counter, and a sink. The lighting is dim, with only a few bright lights visible. The countertop is still unoccupied, with no visible signs of activity.
- Reference: Now, the sweet potato takes on a distinctly different form. It appears to be cooked or baked, with its exterior taking on a wrinkled, slightly crispy texture. The rich orange hue of its interior has deepened, becoming more caramelized and glossy. Steam rises gently from the potato, indicating its warmth, and the flesh seems to have softened further, suggesting it would easily yield to the slightest pressure from a fork.

#### Sample 365 — After

- Similarity: 0.3725
- Prediction: The pan is now more streamlined, with the edges of the pan displaying a more uniform appearance. The hand's motions are more focused, suggesting that the blade has been sprayed with more attention. The kitchen appears to be preparing for a new task, with a focus on the kitchen's surface. The surface of the kitchen is now a bit more cluttered, with more of the food and other items strewn around. The pan's overall appearance is more consistent, with some of the items indicating that the kitchen has been cleaned.
- Reference: The hob surface now appears much cleaner than in the previous frames. The creamy substance is noticeably diminished, and while there's still some sheen indicative of moisture, it's less pronounced. The cleaning action with the blue cloth seems to have been effective in removing the majority of the spill or residue. The surrounding area of the hob appears clearer, with fewer obstructions, hinting that the cleaning process is nearing completion.

#### Sample 367 — After

- Similarity: 0.3611
- Prediction: The water is now in a more streamlined state, with the spoon's grip firmly positioned, indicating that the water has been poured into the pot. The water's surface is slightly damp, implying that the spoon is now able to grasp the water'd contents. The spoon' s surface appears to be a bit damp, suggesting that the liquid has been placed in re-entry mode. The rim of the spoon appears to have been pushed back, revealing a curved edge, suggesting a gradual movement.
- Reference: The cap is more discernible in this frame, offering a clearer view. It's positioned near some jars and containers, with its design and color more evident. The environment's lighting is slightly better, highlighting the cap's features. However, the surrounding objects continue to contribute to a sense of disarray in the frame.

#### Sample 368 — After

- Similarity: 0.2679
- Prediction: The bag is now in a more open state, with the lid still partially open. The hand is now more firmly grasping the bag, indicating that the contents are being poured into the bag. The bag's contents are now more readily available, with no visible signs of contamination. The contents of the bag are now a little more pristine, with a few pieces missing. The person's hand is still firmly gripped, implying that the bag is being emptied.
- Reference: Here, the focus shifts slightly away from the preparation area, providing no direct view of the tomatoes. There's a clear indication that the cooking process is advancing with the presence of a knife and an empty plastic bag labeled with a reference to carrots, suggesting that the ingredients are being organized or prepped sequentially. The absence of the tomato can suggests that its contents have already been utilized in an earlier step, or are set aside, ready for the next stage of meal preparation.

#### Sample 369 — After

- Similarity: 0.4770
- Prediction: The rinsing device is now in a more natural position, with the water running through the surface of the ribbing, indicating that the water has been drained. The water's movement is more gradual, with a greater focus on the nozzle's surface, which is likely to be a risining process. The nozzle is now positioned in reversing mode, with water flowing through the hose and onto the rim of the device. The hand's movements are more relaxed, with more movement in the direction of the water'll flow.
- Reference: The filter in this frame appears to be in active use. Water streams down from the faucet above, cascading over the hands that are holding the strainer, washing its contents or the strainer itself. The flowing water creates a shimmering effect on the metal surface of the filter, making the perforations less discernible than in the previous frames. The force of the water appears to be causing a slight motion in the strainer, and it's evident that the cleaning or rinsing process is ongoing.

#### Sample 370 — After

- Similarity: 0.3662
- Prediction: The towel is now more firmly held, with the hand firmly positioned on the table, indicating that the hand has been a bit more engaged. The hand is now positioned in a more slender position, implying that the towel is being held in place. The towel's surface is now slightly more exposed, with a slight crease in the middle of the towel, a sign of a deeper or more gradual handling. The crease is a little more noticeable, with some of the fabric separating from the towel.
- Reference: The roll of paper shows a clear transformation, with the top sheet partially lifted and separated from the main body of the roll. The hand's position has shifted, and the paper now has a curved trajectory, indicating that it has been pulled upward. The paper's surface is more visible, revealing a zigzag pattern that was not apparent before, possibly due to the angle of separation. This frame captures a decisive moment in the tearing process.

#### Sample 371 — After

- Similarity: 0.1997
- Prediction: The vegetables are now more tender, with a more pronounced texture. The skins are more charred, with the edges of the vegetables showing signs of a softer texture.
- Reference: The spatula is now out of the pan, held aloft, indicating the end of a stirring or flipping action. The utensil appears clean, with no visible food residue, which may suggest that the food did not stick to the surface during the stirring, or it could simply be due to the angle and the distance from the camera. The hand grips the handle closer to the body of the spatula, possibly for better control during the lifting motion.

#### Sample 372 — After

- Similarity: 0.4665
- Prediction: The bin's lid is now slightly more open, indicating that the person is now in the position of a hand. The hand's motion is more consistent, suggesting that the object is now a closer match to the bin'd contents. The object's shape is more streamlined, suggesting a more gradual movement. The surrounding environment is more neutral, with the surrounding environment indicating a steady movement.
- Reference: The basket now is clearly in the grasp of a person who is leaning over it, indicating a deliberate action. The hands are visibly interacting with the contents, which include green and yellow items that could be vegetables, suggesting the basket might be used for storing food. The environment suggests an indoor setting with a rustic appeal, featuring a partially visible wall with a weathered texture, adding to the sense of an intimate, personal setting.

#### Sample 373 — After

- Similarity: 0.4668
- Prediction: The hand is now more firmly grasping the bag, indicating that the bag has been placed in a more streamlined position. The bag's surface is more cluttered, revealing a broader range of items, including the bag'd contents, such as food, clothing, and other items. The hand's focus is on the bag itself, which is now positioned in contrasting positions with the bag. The bags' surface is now slightly cluttered with items, such a bag' or bag'detection, or bag, which may be a sign of a recent change in the bag or bag.
- Reference: The knife has progressed further into the sandwich, indicating a deeper cut. The bread shows a clear separation where the knife has passed through, and the contents inside become slightly more distinguishable. The hand maintains its firm grip on the sandwich, ensuring that it stays in place while being sliced. The overall shape of the sandwich seems to have retained its integrity despite the cut.

#### Sample 376 — After

- Similarity: 0.5000
- Prediction: The rinsing of the broccoli is now more focused on the florets, with the water dripping from the bottom of the bowl indicating that the water has been drained. The water's surface is now a little more damp, with a few more drops of water indicating the risotto's condition. The florettes are now more ripe, with more water sprinkling onto the rosé, indicating a more gradual process. The hands are still agitating, with their fingers pointing at the liander, which is likely to be a result of the steamed broccoli's ribbing.
- Reference: The cucumber is still under the stream of water but appears to have been rotated or shifted slightly, ensuring that all its sides are equally rinsed. The water continues to flow over its surface, and the vegetable remains in the firm grip of the person's hands. The cucumber looks even wetter in this frame, with the water giving it a sheen that further highlights its fresh and crisp nature.

#### Sample 379 — After

- Similarity: 0.3878
- Prediction: The pot appears to be in a more active state, with the lid still firmly attached to the pot. The kitchen's lighting is now more dim, with a light source and a kitchen counter indicating that the pot is still in use. The pot's surface is still visible, with its lid still attached to a table, indicating the pot has been placed in re-use. The lighting is still dim, but the pot remains in place, implying that the lid is still attached.
- Reference: The tray is now distinctly separated from the scales. It appears to be in mid-air, being actively lifted or removed. The angle of the tray is much steeper than before, and it is evident from the shadow beneath it that it is no longer in contact with the scale's surface. The tray's position suggests it's being held by someone, though the hand is barely visible.

#### Sample 380 — After

- Similarity: 0.4904
- Prediction: The pan is now in a more streamlined position, with the lid still firmly attached to the pot, indicating that the cooking process has been completed. The pan's surface is slightly curved, suggesting that the pan is being flipped over, possibly to prevent the pan from absorbing heat. The kitchen's lighting is dim, with a light source indicating the pan has been placed on the stove. The pot's interior is cluttered with utensils, including a potholder, sink, and counter, a kitchen sink, sink and counter top, and a sink and cupboard.
- Reference: The frying pan's content remains consistent with the seasoned salmon fillets or protein pieces. However, the pieces now appear to have been cooked more evenly, with a more consistent golden-brown hue across their surface. The surrounding smaller bits or residues in the pan seem to have further reduced or have been pushed to the edges of the pan. The pan itself is still on the burner, and while it's not visibly evident, it can be assumed the heat continues to cook the contents based on the progression seen in the food.

#### Sample 381 — After

- Similarity: 0.4352
- Prediction: The meat has been sliced more closely, with the skin separating from the meat. The meat is now more tender, with a more pronounced bite of flavor. The skin is more charred, with more of the meat slicing through the meat, indicating that the meat has become more tender. The chef's hand is now positioned in the middle of the pan, allowing the meat to cook more evenly.
- Reference: The seasoning process seems to have advanced further. The hand's position has shifted, possibly suggesting a movement across the dish to ensure uniform seasoning. The spread of the spice on the dish appears denser than in the previous frames, signifying a more substantial application. The overall appearance of the dish suggests that the seasoning process is nearing its completion, as the spice particles appear to be evenly distributed across its surface.

#### Sample 384 — After

- Similarity: 0.3888
- Prediction: The refrigerator door is now in a more natural position, with the door open and the contents of the fridge firmly positioned. The door's position is more noticeable, with a clearer view of the contents and the door'd position. The kitchen's interior is more cluttered, with less clutter and clutter, indicating that the refrigerator is still open. The refrigerator's contents are more visible, with more items displaying a distinct appearance. The fridge's surroundings are more streamlined, with only a few items visible, such as the refrigerator'd contents and a door open.
- Reference: The jug is now outside the refrigerator, held by a person whose hand and lower arm are visible. The motion is more pronounced, with the background significantly more blurred due to the speed of the action. The milk's position in the person's hand has changed; it is now being transported to a new location, likely a countertop or table. The grip on the handle is tight, indicating that the milk is being moved quickly and with care to avoid spillage.

#### Sample 386 — After

- Similarity: 0.4187
- Prediction: The fish is now more fully charred, with the skin separating from the fish's surface. The fish'n's skin is now a little more exposed, with a more pronounced skeleton, suggesting that the fish has been partially charted. The hands are now more engaged in the process of removing the fish, which is likely a sign of the fish being fully soaked in water. The skin is still a bit more exposed to the water, with some of the flesh still forming a protective layer.
- Reference: The piece of meat is now in a different position, showing another angle and revealing more of its natural shape. The handling is still gentle but seems more purposeful, as if the person is ready to place it down or into a cooking vessel. The consistency of the meat's color and texture is uniform, and there's no visible tearing or breaking, which would indicate it's still intact from the handling. The meat’s position relative to the bowl has shifted, indicating a progression in the handling process.

#### Sample 391 — After

- Similarity: 0.2938
- Prediction: The scrubbing tool is now more firmly held, with the handle positioned slightly downwards, indicating that the water has been drained. The water's movement is more gradual, with a more gentle motion indicating the water is dripping. The hand's movements are more relaxed, with more movement indicating a gradual movement. The rinsing action is more pronounced, with water splashing on the surface of the slat, implying that the ristor is now able to grasp the nozzle and remove the soapy residue.
- Reference: The chopping board now appears to have even more water coverage, with nearly the entire surface gleaming with wetness. Puddles of water are more pronounced and seem to be joining together, giving the board a uniformly damp appearance. There are very few dry patches visible, and the entirety of the board has taken on the darker hue of blue seen in the wet sections from the previous frames.

#### Sample 392 — After

- Similarity: 0.4522
- Prediction: The cupboard door is now in a more natural position, with the hand firmly positioned in front of it. The hand's angle is slightly different from the previous frame, suggesting that the hand is more angled. The door's surface is more exposed, suggesting a deeper penetration of the door'd surface. The surrounding area is more visible, with a cluttered and cluttered appearance. The object's position is more apparent, with its occupants interacting with the door.
- Reference: In this frame, the tea towel has been further disturbed, with more pronounced creasing and bunching of the fabric. The hand has a firmer grasp on it, and there's a dynamic sense of movement. The fabric's position in the drawer is more disheveled, and the bright stripes are now at different angles, displaying the chaos of the movement. The tea towel seems to be either in the process of being taken out completely or rearranged significantly within the drawer.

#### Sample 393 — After

- Similarity: 0.4919
- Prediction: The slicing board has been rearranged, with the knife pointing towards the center of the board. The knife's edge is now positioned in the middle of the cutting board, indicating that the knife has been cut into the board's core. The board'd portion of the slit has been removed, revealing a more uniform slice of the knife'd board.
- Reference: In this stage, only a singular, intact red chili pepper remains on the board, its entirety in view. It appears untouched and whole, with a smooth, glossy exterior that shines under the overhead lighting. There are no remnants of seeds or pieces on the board around it, indicating it has not been sliced yet. The hands are positioned as if they are about to commence cutting, with the knife ready to make the initial incision.

#### Sample 397 — After

- Similarity: 0.4429
- Prediction: The pan is now in a more streamlined frame, with the lid still firmly attached to the pot, indicating that the pot has been placed in re-entry mode. The pan's surface is slightly curved, suggesting that the pan is still in its original position. The kitchen's lighting is dim, with a light source indicating a slow or slow motion. The pot's interior is cluttered with utensils, including a potholder, a sink, and a counter top. The lighting is consistent with the previous frames, with an emphasis on the kitchen'd kitchen setting.
- Reference: In this frame, the salt container has been repositioned even more noticeably. It's apparent that there has been some interaction with it, potentially involving its use in the cooking process. However, the cap remains in its sealed position, suggesting that no salt has been dispensed during this specific moment captured in the frame. The nearby items and their arrangement further indicate continued progress in the kitchen activities.

#### Sample 398 — After

- Similarity: 0.3607
- Prediction: The hose is now in a more natural position, with the water running through the nozzle, indicating that the water has been rinsing the hose. The hand's position is more relaxed, implying that the rizzic action is a step forward. The water level is still a little higher than the previous frames, suggesting that the rinse is now more concentrated. The nozzle is now positioned in recirculation mode, with a focus on the spout's surface, ensuring that the entire hose's contents are being rinsed.
- Reference: The jar clip top remains in the open position, with the metal clasp disengaged. The hands are more prominently holding the rubber seal and the metal clip, perhaps to adjust, clean, or ensure its proper functionality. The glass body of the jar is now more visible, reinforcing the emphasis on the maintenance or inspection of the clip top mechanism.

#### Sample 401 — After

- Similarity: 0.2327
- Prediction: The hand is now more firmly grasping the door, revealing a more pronounced grasp. The door's surface is more exposed, indicating that the door is open. The hand's movement is more deliberate, implying that the hand is attempting to open the door. The person's posture is more relaxed, suggesting that the action is more resolute. The shadow of the door'd surface is less noticeable, a sign that the person is adjusting the door to a proper level.
- Reference: Here, the floor's appearance is much the same in terms of color and sheen, with the wooden planks consistently arranged. The action of sweeping is more pronounced, with the sweeper's path slightly more visible. The small debris and particles are becoming less scattered as they are being corralled by the sweeper, which has visibly disturbed them from their resting spots. There's a sense that the cleaning process is ongoing, with some areas of the floor now appearing cleaner than before.

#### Sample 402 — After

- Similarity: 0.4372
- Prediction: The spout is now in a more natural position, with the water running through the nozzle, indicating that the water has been rinsing the sprig. The water's flow is more concentrated, with a greater focus on the raffination of the hose and the surrounding area. The nozzle is now positioned in recirculation mode, with water flowing through the surface of the bowl, ensuring that the resulting water has a filtered stream.
- Reference: Here, the carafe is captured in a different phase of the rinsing cycle. The hand has moved to grip the neck of the carafe, perhaps to shake out excess water or to angle it for a final rinse. The stream of water is directed into the carafe with less intensity, possibly to avoid water splashing back. The sink shows fewer bubbles, indicating that the soap has been largely washed away. The carafe itself looks clearer, without the foam of earlier frames, suggesting that the rinsing is nearly complete.

#### Sample 403 — After

- Similarity: 0.3572
- Prediction: The bread has been partially cut open, with the knife still firmly held in place. The bread is now a more sloppy, slender piece of bread, with a slightly more firm texture. The hands are now more engaged in the action, with their fingers pointing at the bread, indicating that the bread has become more tender. The knife's grip is more firm, with more of the bread's surface exposed, revealing a smoother surface. The sandwich's shape is more uniform, with its edges indicating a gradual progress in the breading process.
- Reference: In this frame, the onion seems to be part of a more elaborate culinary preparation. The slices are now combined with other ingredients on top of the bread or dough base. Specifically, there's an addition of what appears to be cheese or another dairy product intermingled with the onion slices. The layers suggest that the meal is being prepared with care, ensuring a blend of flavors. The presence of other ingredients along with the onion hints at a composite dish, possibly heading towards baking or cooking.

#### Sample 406 — After

- Similarity: 0.3618
- Prediction: The bin is now in a more natural position, with the lid still firmly closed. The person's hand is now more firmly held, indicating that the bin is in optimum condition. The bin's contents are still visible, including the contents of the bin' container, which is now a reusable item. The lid remains in place, with its contents still visible. The object's shape is more apparent, with a wider mouth and a longer handle, suggesting that the lid is now fully closed.
- Reference: The strainer is positioned over a receptacle, appearing almost directly above it. Very minimal traces of the orange-yellow liquid remain within the strainer, signifying that almost all of it has been emptied out. The strainer itself, mostly void of its contents, appears clean and almost pristine, with its mesh structure being more evident and discernible.

#### Sample 410 — After

- Similarity: 0.3726
- Prediction: The jar is now in a more pristine state, with the lid still securely attached to the plastic. The hand is now more engaged in the action, demonstrating the heightened focus on the jar's contents. The rim of the cylinder is now slightly curved, suggesting that the rim is a bit looser than before. The lid is now firmly held, indicating that the lid is still attached to its container.
- Reference: In this frame, the dispersal of sweetcorn across the pizza appears more complete. The kernels are spread out with a greater coverage, filling in previously bare patches of dough and sauce. The hand and can that were dispensing the sweetcorn are still present, implying the continuation of the action, yet there’s a sense that the sprinkling process is nearing its end. The kernels that have landed seem static, resting heavily upon the surface as if settling into their final position.

#### Sample 412 — After

- Similarity: 0.4195
- Prediction: The rinsing basket is now in a more natural position, with the water running through the basket, indicating that the water has been drained. The water's movement is more gradual, with a steady stream of water circulating around the basket. The rim of the basket is still firmly held, with water sprinkling from the bottom of the bowl to the sides. The hand's movements are more relaxed, with more movement in the direction of the risining basket.
- Reference: In this frame, the spring onion is undergoing a thorough rinse. The fingers have moved further up, near the middle of the stalks, ensuring a secure hold while the water cascades over the entire length of the onion. The stalks are bending gracefully under the stream of water, highlighting their fresh and pliable nature. The glistening droplets splash off the onion's surface, washing away any residual soil or debris, and the roots are now fully immersed, indicating a complete cleaning process.

#### Sample 415 — After

- Similarity: 0.4716
- Prediction: The tray is now in a more natural position, with the lid still slightly open, suggesting a gradual movement. The hand is now more likely to be holding the tray, indicating that the action has been completed. The tray's surface is more exposed, suggesting that the tray is still in its original position. The kitchen environment is still cluttered with the remains of the tray and the surrounding items, including the lid, remain intact.
- Reference: The lunch box appears to be opened even further compared to the second frame. The content inside the box is now more visible, but it remains hard to determine its exact nature. It continues to resemble layered food items like sandwiches or wraps. The transparent nature of the lid offers a clearer view into the contents, though precise details remain elusive.

#### Sample 417 — After

- Similarity: 0.4665
- Prediction: The scrubbing brush is now more firmly held, indicating that the water has been drained. The hand is now positioned in a more horizontal position, allowing the brush to reach the surface of the brush, ensuring that the brush is fully saturated. The brush's surface is now slightly dampened, demonstrating the presence of a squeezing motion. The water level is now less than the previous frame, suggesting that the scavenging action is likely to continue.
- Reference: The chopping board's position has not drastically changed, but the focus on the board is clearer as the hand has moved away, giving an unobstructed view. The board still slopes downwards, with water from the tap streaming over its surface. The water's sheen on the board's surface is less soapy, which might suggest the rinsing process is nearing completion. The light reflecting off the wet surface accentuates the scratches and signs of wear, showing the board's longevity and frequent use.

#### Sample 420 — After

- Similarity: 0.4595
- Prediction: The bag is now in a more streamlined state, with the hands positioned in overlapping positions, indicating that the person has been able to grasp the contents of the bag. The hand's movements are more relaxed, suggesting that the bag is being handled more carefully. The bag's contents are more readily visible, with a clearer image of the contents. The person's hands are more engaged, implying that the bags are being handled with greater care.
- Reference: The freezer door is now open wider than in the previous frames, with the person's hand appearing to have completed the motion of either placing or retrieving an item. The frozen bag is now partially obscured by the person's hand, but the contents still hint at a variety of colors from the possible vegetable mix inside. The compartments on the door are slightly more discernible, showing empty spaces that could be used for additional storage. The lighting remains consistent with the previous frames, illuminating the freezer's interior while casting a shadow on the surrounding floor and walls.

#### Sample 427 — After

- Similarity: 0.3114
- Prediction: The hand is now more firmly grasping the bowl, indicating that the bowl is now in its proper position. The bowl's surface is slightly curved, suggesting that the hand is a bit more angled, implying that the spoon is now positioned in the middle of the bowl. The hand's motion is more pronounced, suggesting a more gradual movement, a shift in the direction of the action. The kitchen appears to be preparing for a meal, with the bowl'd contents indicating a re-entry.
- Reference: The perspective shifts lower, and the bottom section of the refrigerator comes into view, showing clear crisper drawers that seem to hold vegetables. The door remains wide open, and the lack of illumination inside the refrigerator is more apparent, potentially indicating that the bulb is out or the refrigerator is powered off. The white interior of the refrigerator contrasts with the dark green of the vegetables, making them stand out. The bare feet of the person, visible at the bottom of the frame, indicate a casual, domestic setting.

#### Sample 431 — After

- Similarity: 0.3943
- Prediction: The rinsing action is more streamlined, with the water running more smoothly. The water's movement is more consistent, with a more pronounced flow of water, indicating that the risote has been rubbed. The hands are more engaged in the action, demonstrating the reversal of the previous position. The lint is still a little damp, but the water'n's flow is still visible. The leaves are still racked, with some of them sprinkling on the surface of the liander.
- Reference: The lettuce leaf is now out of the water stream, its surface glistening with moisture. It’s being held aloft, which allows some of the water to trickle off, reducing the excess water weight and revealing the leaf's sturdy yet flexible structure. The leaf's vivid green color remains a testament to its freshness, while the residual water droplets catch the light, giving the leaf a jewel-like appearance. The act of holding the leaf up also suggests that it is being inspected or is about to be set aside to dry.

#### Sample 433 — After

- Similarity: 0.4834
- Prediction: The hand is now more firmly in the position of the hand, indicating that the hand is still in the hand position. The hand's motion is more consistent with the hand'd motion, suggesting that the action is more deliberate. The shadow of the handle is less noticeable, suggesting a more gradual movement. The overall state of the image is more blurred, suggesting the hand may be a bit more hesitant to move.
- Reference: The cloth now appears more loosely held, with the person's grip relaxed, suggesting the squeezing action may be complete. The cloth itself looks less twisted and more spread out than in the previous frames, with some parts hanging down, indicating that it is likely in the process of being opened up after wringing. The color of the cloth remains consistent with the earlier frames, light and uniform, without any visible patterns or designs that can be made out from this perspective.

#### Sample 436 — After

- Similarity: 0.4709
- Prediction: The hand holding the knife has moved away from the kitchen counter, indicating that the knife is now in the kitchen. The knife's handle is still positioned, suggesting that the hand is now preparing the food for cooking. The kitchen counter is now more cluttered, with the kitchen area cluttered with food and other items. The hand's movements are more relaxed, implying that the chef is preparing to serve.
- Reference: The peeler now has been picked up again, and the hand that grips it exhibits a more dynamic tension, as if it is in the midst of peeling action. The peeler's blade is angled in such a way that it is ready to make contact with the eggplant, positioned to continue the peeling process. This frame captures the motion of food preparation, with the hand's positioning and the peeler's orientation suggesting a repetitive and rhythmic motion typical of peeling vegetables.

#### Sample 437 — After

- Similarity: 0.2097
- Prediction: The bowl is now more firmly held, with the lid still firmly pressed against the edge of the bowl, indicating that the water has been drained. The water's surface is now a little more damp, with a more pronounced odor, suggesting that the bowl is still a bit damp. The soiled portion of the basin is now slightly more exposed, with no visible debris, suggesting a re-sealing process. The bowl's interior is now less cluttered, with only a few small pieces of food and other items visible. The sink's focus is now on the bowl'r surface, with its spout positioned in the center of the sink, implying that the sink is
- Reference: A hand comes into the frame, moving towards the pepper pieces, suggesting an intention to pick them up or move them. The fingers are positioned in a way that they are about to grasp the pepper pieces, suggesting imminent action. The overall composition of the frame captures a moment of anticipation, as the viewer waits to see where the pepper pieces will be moved to next.

#### Sample 438 — After

- Similarity: 0.4967
- Prediction: The pan has been re-opened, with the lid still firmly attached to the burner, indicating that the heat is now circulating. The pan's surface is now more reflective, suggesting that the light is now less visible. The kitchen's lighting is now dim, with a focus on the kitchen'd lighting and the kitchen setting. The lighting is still dim, but the kitchen is still lit. The surface of the pan is now slightly darker, suggesting a more gradual change in the lighting.
- Reference: The lid is now in motion, captured in the act of being removed by a hand, which suggests interaction and activity. The hand's position and the angle of the lid suggest that the action is being performed with care, likely to check on the contents or to stir them. The lid’s glass appears clear, and there are no visible signs of steam or food residue, indicating that the cooking process may not have progressed far or the inside of the cooker is well-maintained. The perspective is closer, providing a more detailed view of the lid's edge and the hand's grip on the knob.

#### Sample 440 — After

- Similarity: 0.4061
- Prediction: The meat is now more firmly held, with the edges of the meat separating from the rest of the ingredients. The meat has been sliced into smaller pieces, indicating that the meat has a more pronounced bite. The knife's action is more deliberate, implying that the knife has been more pressed into the meat, resulting in a smoother and more uniform cut. The texture of the beef has improved, with a slight charring to the meat's surface.
- Reference: The cheese has been substantially disturbed by the scooping action, now clinging heavily to the spoon. Its pliable nature is evident as it stretches slightly, forming a peak where the spoon is lifting it away from the container. The cheese maintains its integrity despite the stretch, not breaking apart or crumbling, which signifies a soft but cohesive quality. The container from which it is being scooped shows more of its interior, indicating that a significant amount has been extracted.

#### Sample 441 — After

- Similarity: 0.4990
- Prediction: The door is now partially open, with the door's contents visible. The person's hand is now more firmly grasping the door, revealing a more streamlined appearance. The door'd interior is now cluttered with items, including food, and the kitchen's interior is cluttered and cluttered. The kitchen'es' interior is still cluttered, with a variety of items and items ranging from kitchenware to dishes to dishes. The refrigerator's door is still closed, with its contents visible, including the refrigerator'd contents.
- Reference: In this frame, the microwave door is fully open, and the interior is now completely visible. The glass turntable sits at the center, and the interior lighting of the microwave is not activated, indicating that it is not currently in operation. The user's hand has moved away from the handle, implying that the action of opening the door is complete. The surrounding items, including the kettle and pitcher, maintain their position, and the shadow on the counter has elongated, suggesting a greater angle of the door's opening in relation to the light source.

#### Sample 444 — After

- Similarity: 0.3852
- Prediction: The tinkering tool has been re-engaged, indicating that the knife is now fully engaged. The knife's surface is slightly more exposed, suggesting that the blade is still firmly attached to the blade. The blade's position is more pronounced, suggesting a more gradual movement, and the knife'rs' appearance is more consistent. The tang of the knife remains consistent, suggesting the knife has been properly inserted into the blade' base. The sharp edge of the blade remains consistent with the knife, suggesting it may be a tang or a sharpener.
- Reference: The whetstone's position remains largely unchanged, still vertically oriented with its finer grit facing upwards. A slight shadow cast on the countertop suggests that the light source may have slightly shifted or that the hand positioning has altered. The stone's surface appears more uniformly reflective, with fewer distinct patches of light reflection as seen in the previous frame. The label is still visible, albeit upside-down, and continues to be partially obscured by the user's hand.

#### Sample 453 — After

- Similarity: 0.2948
- Prediction: The sink is now more streamlined, with the water running more smoothly. The hand's movements are more deliberate, indicating that the water has been drained, resulting in a more concentrated stream of water. The water's consistency is more uniform, suggesting that the sink is still wet. The sink's surface is more cluttered, with a slushy appearance, highlighting the emergence of a newer, cleaner, and more sporacious water.
- Reference: The entirety of the counter now appears refreshed. The dust and crumbs that once littered its surface have vanished, replaced by a homogeneously clean area. There's a mild sheen, evidence of the damp cloth's recent journey across the counter. Any residual streaks that once broke the surface's uniformity have been skillfully addressed, leaving behind a counter that invites one to utilize its pristine surface.

#### Sample 456 — After

- Similarity: 0.2930
- Prediction: The spout is now in a more natural position, with the water running through the center of the sprig. The water's flow is more concentrated, with a greater focus on the rinsing action. The hand's movements are more relaxed, with more movement in the direction of the water'd flow. The raffination action is more focused on the surface of the surface, with less water escaping from the nozzle. The hands' movements are less relaxed, indicating that the water has been rubbed into the hose.
- Reference: The coffee machine remains in the same decorative design with its distinct blue and gold patterns. However, its position appears to have slightly changed, indicating that it might have been shifted or rotated. The top part of the machine is more visible than in the previous frame, and the hand that was earlier interacting with it is no longer obstructing the view. The ambiance of the surroundings seems brighter, suggesting a slight change in lighting or camera exposure.

#### Sample 458 — After

- Similarity: 0.4844
- Prediction: The pan is now positioned in a more soiled position, with the water running more smoothly. The water's movement is more consistent, with a sprinkling of soapy water on the surface of the pan, indicating that the water has been drained. The pan's surface appears to be a bit damp, with some of the water still lingering on the bottom of the bowl. The person's hand is more likely to be holding the pan in the hands of the person, implying that the pan is still soaking.
- Reference: The tap's lever now shows a noticeable change, positioned at an angle that suggests the water has been turned on. The change in the lever's angle from parallel to the countertop to a downward tilt is a clear indication of activation. While water is not visibly flowing from the spout in the frame, the position of the lever is consistent with typical tap operation for initiating water flow.

#### Sample 459 — After

- Similarity: 0.3745
- Prediction: The hand is now more firmly held, indicating that the knife is in a more active state. The knife's surface is more exposed, suggesting that the blade is still in motion, possibly a moment of action. The hand's movement is more consistent, implying that the hand is preparing to move the knife. The blade's position is more apparent, a sign that the chef has been preparing the knife for a long time. The kitchen environment is more relaxed, with the kitchen setting a focal point for the kitchen.
- Reference: The can is now in motion, as evidenced by the blurred surroundings and the dynamic angle of the can itself, suggesting that it is being moved rapidly. The blurred hand position suggests a downward action, likely placing or dropping the can into a receptacle out of frame. The lid appears to be in the same state of opening as the previous frame, not further detached, but the rapid movement has caused the contents to shift, potentially leading to the spillage of the liquid and the spherical items within.

#### Sample 460 — After

- Similarity: 0.2392
- Prediction: The pan is now in a more natural state, with the surface of the pan being more exposed to the elements. The person's hand is now more focused on the pan, indicating that the pan has been thoroughly cleaned. The pan's surface is more exposed, with a noticeable difference in color and texture. The kitchen counters are now more visible, with more of the kitchen items visible, including the stove, sink, and counter. The surface of this pan is more reflective, with visible streaks of food particles and a smoky smell.
- Reference: The scene here is noticeably clearer, suggesting a near halt in motion. The tap, with no active engagement from the hand, seems to be in a dormant state. There is no visible water flow or splash, indicating that the tap is likely fully closed. The surrounding area of the tap shows residual moisture, which, along with the absence of blur, signifies the cessation of water flow. This frame captures the conclusion of the action, with the tap now in a static and inactive state.

#### Sample 463 — After

- Similarity: 0.4295
- Prediction: The pot appears to be a little more cluttered, with the lid still firmly closed, suggesting that the pot is still in its original position. The pan's surface is slightly more exposed, suggesting a gradual movement, possibly a slight movement in the kitchen or cooking area. The pot's interior remains cluttered and uncluttered, indicating that the pan is still a bit damp. The kitchen's lighting is dim, with a light source indicating a low-level of heat. The stove's setting is still visible, with only a few visible objects visible, such as the pot'd lid, a jar, or a potholder.
- Reference: The third frame continues to showcase the kitchen environment and the hand in close proximity to the countertop or appliance interface. The specific state of the switch remains elusive, but there's a distinct impression of movement, potentially indicating the switch's activation or deactivation. The close-up nature of this frame in relation to the switch area suggests that there's an ongoing interaction, but the definitive state of the switch, either on or off, cannot be confidently ascertained.

#### Sample 468 — After

- Similarity: 0.3791
- Prediction: The rinsing device is now in a more natural position, with the water running through the surface of the risotta, indicating that the water has been drained. The water's movement is more pronounced, with a broader range of movements, including a hand-held tap, which indicates that the hose is running. The nozzle's position is more relaxed, with more water flowing through the nozzle, resulting in fewer streaks. The hand's movements are more relaxed and the water'n'drops are less noticeable, implying that the rinse has been completed.
- Reference: The bell pepper is now completely wet, with water streaming uniformly across its surface, resulting in a gleaming, reflective sheen that envelops the vegetable. The droplets are no longer individual but have formed a continuous layer, suggesting that the pepper has been turned and manipulated under the water to ensure all sides are equally cleansed. The hand's grip is steady, with the thumb pressing lightly on the stem, perhaps to prevent the pepper from slipping during the washing process.

#### Sample 469 — After

- Similarity: 0.3027
- Prediction: The hand is now more firmly grasping the bowl, indicating that the spoon is now in the hands of the person who is handling it. The hand's movements are more relaxed, suggesting that the bowl is now being handled more carefully. The bowl's surface is more exposed, suggesting a more gradual movement, with the spoon's position indicating a gradual movement. The hands are still firmly gripped, suggesting the spoon has been positioned in the hand'd position.
- Reference: The cover seems to be in a more elevated position compared to the previous frames, with the lifting process appearing almost complete. The perspective shows a more pronounced view of its underside. Shadows under the cover suggest it's hovering above its initial position, which combined with the visible hand movement, implies it's being actively lifted. The surrounding area is slightly blurred, indicating swift motion, further emphasizing the dynamic state of the cover being removed.

#### Sample 470 — After

- Similarity: 0.3402
- Prediction: The bottle is now in a more natural state, with the hand firmly holding the lid, indicating that the cap has been removed. The hand's motion is more relaxed, suggesting that the bottle is still in its original state. The bottle's contents are still present, with no visible signs of use. The lid remains in its current state, presumably a sign of the cap's final state.
- Reference: The plug is now almost completely removed from the socket, with only the tips of the prongs still in contact with the outlet. The person’s hands, still sheathed in yellow gloves, show a relaxed grip, indicating the completion of the unplugging action. The background remains cluttered, and the shadow of the person’s hands and the plug is still visible on the wall, mirroring the action above.

#### Sample 473 — After

- Similarity: 0.3175
- Prediction: The hose is now in a more natural position, with the water running through the nozzle, indicating that the water has been sprayed. The hand is now more likely to be holding the hose, implying that the squeezing action is complete. The water level is less than the previous frame, suggesting that the hand is still holding the water. The nozzle is now positioned in reversing mode, with a focus on the water's movement, resulting in fewer squirts.
- Reference: The cap is now visibly detached from the bottle, held aloft in one hand while the other continues to secure the bottle. The threading on the neck of the bottle where the cap was once secured is now exposed, and the cap's interior is visible, showing the underside which would normally be sealed against the bottle's opening. The detachment of the cap suggests the completion of the opening process. The environment and the bottle's position remain consistent, indicating that the sequence of actions occurred within a short timeframe.

#### Sample 474 — After

- Similarity: 0.3670
- Prediction: The spout is now in a more natural position, with the water running through the nozzle, indicating that the water has been drained. The water's flow is more concentrated, with a greater focus on the spongy areas of the rinsing vessel. The raffination process is more intensive, with more water being poured into the hose, resulting in fewer bubbles. The hand's movements are more relaxed, with their movements indicating a thorough rinse.
- Reference: The coffee holder is now placed directly under the water stream, and the user is manipulating it with a twisting motion, ensuring all interior surfaces are thoroughly rinsed. The water running off the holder appears clear and free of coffee debris, indicating that the holder is nearly or completely clean. The holder's metallic interior reflects the light, highlighting its cleanliness against the darkened coffee-stained areas that have now been washed away.

#### Sample 475 — After

- Similarity: 0.4462
- Prediction: The kitchen sink is now positioned in a more natural position, with the water running through the surface, indicating that the water has been sucked out. The water is now concentrated in the sink, resulting in fewer bubbles, a sign of a thorough cleaning. The kitchen's surface is now more exposed, with a smoky feel to it, reminiscent of sand. The sink's water level is less than normal, suggesting that the sink is still scrubbing the surface.
- Reference: The cutting board is now facing downward, providing a clear view of its entire surface. There are visible traces of soapy water, but they are more spread out and less foamy than before, suggesting that the board has been partially rinsed or that the soap has been distributed across the surface. The hand holding the board is cleaner, with less soapy residue, and is also holding a damp cleaning cloth, which may have been used to wipe down the board.

#### Sample 476 — After

- Similarity: 0.4519
- Prediction: The tortilla has been placed in a more sloppy position, with the tortilla's surface exposed. The tortilla'd surface is now more exposed, with a slightly more rounded shape, suggesting that the tortilla has a firmer grip. The palm of the hand is now slightly more exposed to the tortilla, indicating that the hand has been able to grasp the tortilla. The hand's motion is more pronounced, implying that the palm of hand is more engaged in the tortilla than the hand itself.
- Reference: In this frame, the salt shaker is still tilted, with a slightly adjusted angle, indicating an ongoing shaking action. The hand's movement seems more deliberate and controlled, as if the person is nearing the end of the seasoning process. Salt can be seen in mid-air, caught in the act of falling onto the cheese, which suggests that a considerable amount of shaking has already been done. The distribution of salt appears to be focused more towards the center of the flatbread.

#### Sample 477 — After

- Similarity: 0.4433
- Prediction: The rice has been thoroughly cooked, with the whites separating from the white, indicating that the water has been absorbed. The spoon is now firmly seated, allowing the rice to drain more easily. The water's consistency is uniform, suggesting that the rice has a more pronounced texture. The rice's color is more vibrant, suggesting a deeper hue in the dish.
- Reference: Here, the light maintains its vivid blue core but is surrounded by a broader, less intense outer flame, which hints at a stable and sustained heat source. The consistency of the flame's color and shape suggests that the burner is now in a steady state, providing a continuous and even heat. The light's reflection is consistent and widespread, indicating that the burner has reached an optimal operating condition, and the pot is fully enveloped in the heat, likely contributing to a steady cooking process.

#### Sample 480 — After

- Similarity: 0.4308
- Prediction: The squeezing action is more pronounced, with the water running more quickly, indicating that the squirt has been done. The water's movement is more gradual, with a more gentle motion indicating the rinsing action. The raffination of the hose appears to be complete, with no visible bubbles or splatters. The hands are still firmly held, with their fingers pointing at the nozzle, implying that the water has been drained.
- Reference: The dispensing action seems to have concluded, with a discernible portion of the sponge now saturated with the liquid washing up. The wetted area appears glossier and darker in contrast to the other parts of the sponge, suggesting that a significant amount of liquid has been absorbed.

#### Sample 482 — After

- Similarity: 0.3794
- Prediction: The foil is now a more firmly held, more slender, and more brittle. The person's hand is more pronounced, and the foil is more exposed to the air, indicating that the foil has been partially inserted. The foil's surface is more uniform, with the foil'd edges more exposed. The overall appearance of the foil appears to be more akin to a clinging object, with a slight crease in the foil.
- Reference: The packaging now shows clear signs of being tampered with. The hand continues its interaction with the lighter meat's package, and it appears that a portion of the seal is being lifted or pulled back. The action suggests that the individual is in the process of opening the packaging to access the meat inside. Although the seal isn't entirely removed, a partial view of the meat inside becomes visible, indicating that the package is no longer in its original, untouched state.

#### Sample 485 — After

- Similarity: 0.3488
- Prediction: The cabinet's handle is now more firmly held, with the hand extending slightly towards the door, indicating that the door is open. The hand is now positioned in a position that allows the door to be opened, allowing the door's contents to be easily seen. The door'd interior is now slightly more open, revealing a more spacious and spacious space. The kitchen's lighting is now dim, with a light source indicating a possible opening. The cabinet is now fully open, with its contents visible, displaying a heightened sense of security.
- Reference: The milk carton has now made contact with the floor, resting on its side with the top facing the wall. It is placed near a corner where the wall meets the floor, and the person’s hand is reaching towards it, possibly to pick it up or prevent spillage. The immediate vicinity is relatively bare, apart from a television and cleaning equipment, which implies that the carton might be in a transitional area such as a corridor leading away from the kitchen.

#### Sample 489 — After

- Similarity: 0.4670
- Prediction: The oven door is now in a more natural position, with the person's hand positioned in the middle of the frame. The person'd hand is now positioned slightly further away from the oven, indicating that the oven has been placed in optimum conditions. The oven's interior remains unchanged, with a consistent appearance of a kitchen setting, including the oven'rs and oven'laid.
- Reference: The hand is now in contact with the timer, with the index finger pressing down on it. This physical contact indicates that the user is actively interacting with the timer, most likely pressing a button to either stop or start it. The display of the timer is still not fully visible, but the fact that the finger is pressing down suggests that the display might be about to change or has just changed. The kitchen backdrop is consistent with the previous frames, emphasizing the everyday nature of the activity.

#### Sample 490 — After

- Similarity: 0.4388
- Prediction: The bread has been partially removed from the pan, with the bread still firmly wrapped in the foil. The person's hand is now more engaged in the action, demonstrating the bread's ability to be fully sliced. The bread' texture is more consistent with the texture of the bread, which is a savory delight. The hands are now more reliant on the bread to grasp the bread and ensure that it remains intact.
- Reference: The tortilla is now partially folded, with the hand actively pinching one edge, guiding it into the confines of the plastic packaging. The tortilla has transformed from its previously flat and open state to a semi-crumpled form, bending to accommodate the reinsertion process. This action creates creases and wrinkles on its surface, a stark contrast to the previously smooth appearance. The tortilla is now interacting with its packaging, which bears bold colors and brand markings that suggest a commercial origin.

#### Sample 491 — After

- Similarity: 0.4123
- Prediction: The kale is now more ripe and charred, with the leaves a little more exposed. The knife's blade is now angled slightly, indicating that the kalette has been trimmed. The leaves are now more uniformly sliced, with a few more pieces of the halibut still visible. The halved kalis are now a bit more steamed, with more leaves and stems separating from the florets. The blade is still a tadling motion, with some of the leaves still retaining their shape.
- Reference: By this point, the coriander has undergone more significant cutting. The leaves and stems are more dispersed across the board, with clear distinctions between the cut and uncut parts. Some of the leaves are more finely chopped than in the previous frame, and there's an increase in the amount of visible cutting board space, indicating the progress in the preparation.

#### Sample 495 — After

- Similarity: 0.3741
- Prediction: The hand of the holder is now more firmly held, indicating that the hand is now in a more active position. The hand is still positioned in squat position, presumably to prevent the scuff from forming. The holder's position is more pronounced, suggesting that the ring is now positioned more close to the edge of the handle. The hands are still firmly pressed against the crease, implying that the handle is now slightly curved. The palm of the hand appears to be a reversal of the previous frame's hand, suggesting a gradual movement.
- Reference: In this frame, the plug is now half-out of the socket, with the prongs partially visible and the plug's body tilted downwards at an angle indicative of it being in motion. The motion seems to be a result of the pulling force applied to the cord, which is more taut and directed sharply to the bottom right. The plug's removal from the socket has not been completed yet, as the electrical connection appears to be still partially intact. The environment remains unchanged, continuing to suggest a domestic interior with minimalistic design elements.

#### Sample 496 — After

- Similarity: 0.3555
- Prediction: The towel is now in a more streamlined position, with the hand firmly holding the folded edge of the towel, indicating that the hand has been positioned in repositioning the towel. The hand's motion is more relaxed, revealing a creased or wrinkled surface, a sign of a deeper or more gradual movement. The towel's surface is more exposed, demonstrating a gradual movement, implying that the towel has been placed in reassuring the hand. The crease is a contrast to the previous frame, suggesting that the hands have been seated on the towel and are now positioned on the table.
- Reference: The focus here is closely on the bag, held outstretched in one hand, displaying the 'THIS SIDE UP' instruction clearly, signifying the correct orientation for microwave cooking. The bag appears more bloated than in the previous frame, suggesting the popcorn has fully popped. The text on the bag is sharp and readable, showing a caution for the contents being hot. The person's handling of the bag, with a single hand from the bottom, indicates confidence that the popping is complete and readiness to open the bag.

#### Sample 497 — After

- Similarity: 0.4175
- Prediction: The hand is now more firmly held, indicating that the knife is now in its proper position. The knife's grip is more firm, suggesting that the blade is now positioned in a more pronounced position. This frame shows the knife'd position, which is likely a result of the knife being positioned at the right angle, a position that could indicate a slight shift in the knife position.
- Reference: The yellow glove continues to be the focal point in this frame. The hand wearing the glove has shifted its position once more, suggesting the wearer is moving quickly through various tasks. The glove remains intact without any visible wear or tear, suggesting it is durable. From this angle, a portion of the hand without the glove is also visible, juxtaposing the bare skin with the gloved hand and providing a clear demarcation of where the glove begins or ends.

#### Sample 498 — After

- Similarity: 0.4625
- Prediction: The hand is now more firmly grasping the pot, indicating that the lid has been removed. The lid is now slightly positioned, suggesting that the pot is still in its original position. The hand's motion is more pronounced, suggesting a gradual movement, with the pot still firmly in place. The surrounding environment is more calm, with no visible movement, such as a chopping or sweeping motion.
- Reference: Now, the milk bottle is being held more upright, and the person's hand is placed on the bottom, steadying it. The cap seems to be completely removed, as evidenced by the absence of the white color at the bottle’s neck where the cap should be. The person's other hand is not visible in the frame, possibly engaged in the act of removing the cap completely. The background remains consistent with the previous frames, displaying a static domestic kitchen scene, with no significant changes to the placement of the items around.

#### Sample 5 — Transition

- Similarity: 0.4829
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the counter. Initially, the counter is in a state of disarray, with no visible signs of activity. As the frames progress, the person's movements are blurred, indicating that the counter has been placed in re-ordering. By the final frame, the countertop is clearly in pristine condition, with the counter's surface still visible, with a clearer and cleaner appearance. The consistent movement of the hand, the utensils, and the overall arrangement of the table are indicative of a deliberate action.
- Reference: The progression of frames shows the floor undergoing a cleaning process. Initially, the floor is marked with small debris and minor smudges. As the wiping begins, a damp streak becomes evident, indicating that the floor is being actively cleaned. By the final frame, the presence of moisture is more widespread, with visible streaks of wetness and a more uneven appearance due to the wiping. The cleaning has made the dirt on the floor more apparent, creating a contrast between the cleaned and yet-to-be-cleaned areas, showcasing the floor's transition from a dry, dusty state to a wet, cleaner surface.

#### Sample 8 — Transition

- Similarity: 0.4443
- Prediction: Over the course of these three frames, there's a clear progression in the state of the machine's control panel. Initially, the hand is engaged, with the knob positioned in the middle of the screen, indicating the user's intention to turn the knob. As the frames progress, the user is seen interacting with the control panel, implying the user has stepped in to control the machine. The hand's interaction with the controls is a subtle transition, highlighting the gradual change in the control settings. The consistent state of control is evident throughout the sequence, with a consistent hand-held display of the controls and the control knob indicating that the user will be able to control
- Reference: As the video progresses through the three frames, the toaster transitions from a dormant, inactive state to a fully operational one. Initially, it rests passively with all indicators suggesting non-use. However, as the frames advance, the toaster's lever is actuated, marking the beginning of its function. The inner glow and increasingly bright power light signal the toaster's heating elements coming to life, culminating in the third frame where it's evident that the toasting process is in full swing. The evolving luminosity within the slots and the changing position of the lever chronicle the journey of a simple machine springing into action, transforming raw bread slices into delightful toast.

#### Sample 20 — Transition

- Similarity: 0.4729
- Prediction: The sequence of frames captures a clear progression in the state of the paper. Initially, it is a state of rest, with no visible signs of use. As the frames progress, the paper is progressively withdrawn, with the paper indicating its use. By the final frame, the person's hand is engaged in a deliberate action, demonstrating the importance of the process. The paper's state of being is evident, with its shape and texture contrasting with the person who is handling it.
- Reference: Analyzing the state change of the yogurt across the three frames, one can observe a deliberate and sequential arrangement. Initially, the yogurt is being positioned as part of a set, with careful attention to the orientation and order. As the sequence progresses, the yogurt is moved with intention, showcased by the hand's secure grip and focused placement. By the final frame, the yogurt has been repositioned at a distinct angle, marking the conclusion of its movement. This deliberate progression indicates a methodical approach, possibly for an organizational or display purpose within the context of the kitchen environment.

#### Sample 22 — Transition

- Similarity: 0.3246
- Prediction: Over the course of these three frames, there is a clear progression in the state of the meat. Initially, the meat is fully sliced, with the skin still exposed. As the frames progress, the person's hand begins to remove the meat, revealing a more pronounced and charred appearance. As they progress, there's a noticeable change in the meat's state of being, with a gradual change in its shape and texture. The hand's movements are evident, with their hands demonstrating a precise and deliberate motion, indicating that the meat has been fully slicked. The process of removing the meat from the meat reflects the methodical nature of the process, with each frame highlighting a different action.
- Reference: Observing the garlic press across these frames, one can trace the process of mincing a clove of garlic. Initially, the press is open with the garlic clove placed inside, awaiting pressure. As we progress, the user applies force, bringing the handles together, causing the inner plunger to push the garlic against the press head. By the final frame, the press handles are almost closed, indicating the clove has been crushed, though the resulting minced garlic is not yet visible. The user’s hands display increasing tension, a reflection of the effort required to extract the essence of the garlic through the metal grid into the awaiting dish.

#### Sample 26 — Transition

- Similarity: 0.4905
- Prediction: Over the progression of these frames, the paper undergoes a clear transition from being untouched to being fully inserted. Initially, the person's hand is unsure of where the paper is, but as the frames progress, the hand's movements become more deliberate, indicating that the paper has been inserted into the paper. As the frames move forward, the hands' movements become less deliberate, suggesting that the person is preparing to insert the paper into the tray. The hand'
- Reference: Over the course of these frames, the cling film transitions from a dormant state to active use. Initially, it is seen in a static, untouched state, but as the person’s hands engage with the material, it begins to unravel, displaying the effects of the pull—slight wrinkles form, and the transparency of the film varies with tension. By the final frame, the film has been significantly drawn out, reflecting a common household task where cling film is prepared to seal or protect food items, with the motion and force exerted by the hands altering its pristine condition to one that's ready for application.

#### Sample 27 — Transition

- Similarity: 0.4878
- Prediction: Over the progression of these frames, the box transitions from a partially opened to a fully opened one. Initially, the person's hand is hesitant to open the box, indicating that the person is trying to open it. As the frames progress, the hand's movements become more deliberate, revealing the contents of the box. By the final frame, the hands are able to open and close the box's contents, demonstrating the action of opening the box to open its contents. The person'
- Reference: The sequence of images illustrates a gradual opening of a Twinings tea box over three stages. Initially, the box is intact, with the cellophane just beginning to be peeled back. In the second stage, the cellophane is removed, and one flap of the box is opened, revealing the silver foil bag inside. By the third stage, the opening process is near completion, with both flaps of the box opened wide and the contents almost ready to be fully revealed. The steady hands of the person indicate a careful and deliberate action, ensuring that the tea bag is not damaged during the unboxing.

#### Sample 28 — Transition

- Similarity: 0.4045
- Prediction: Over the progression of these frames, the table undergoes a noticeable transformation from a partially uncovered surface to a fully uncovered one. Initially, the surface is a bit damp, with no visible signs of wear or tear. As the frames progress, the person's hand moves closer to the surface, indicating that the table is being used for cleaning. By the final frame, the hand's movements are more deliberate, demonstrating the process of removing the table's surface. The consistent pattern of the table surface, the consistent hand'
- Reference: The paper undergoes a visible transformation across the three frames: from an intact, untouched state to a partially torn state, and finally to a fully torn and separated state. The initial grip and force application result in a rough, uneven tear, highlighting the random nature of paper tearing by hand without a pre-folded line. The tearing process reveals the fibrous interior of the paper, a stark contrast to its initially smooth exterior. This sequence captures the progression of tearing, emphasizing the irreversible change from a whole to a separated state, demonstrating the physical properties of paper under stress.

#### Sample 31 — Transition

- Similarity: 0.4416
- Prediction: Over the course of these frames, there's a clear progression in the state of the counter. Initially, the counter is in a state of disarray, with no visible or noticeable debris. As the frames progress, the cleaning action is evident, with the person's hand indicating a thorough cleaning. By the final frame, the surface is progressively cleaner, with less debris and less visible marks. The consistent, consistent, and consistent cleaning process is evident throughout the frame, demonstrating the effectiveness of the cleaning process.
- Reference: The progression across the three frames reveals the glass being moved in a smooth, lateral motion from left to right across the wooden table surface. Initially at rest, the glass is engaged by the person's hand, inducing a slide that carries through to the subsequent frames. The steadiness of the hand and the unaltered upside-down position of the glass throughout suggest a deliberate and controlled action, with no signs of tipping or erratic movement, portraying a simple but precise maneuver. The light reflecting off the base of the glass shifts accordingly, marking the path and speed of the motion.

#### Sample 33 — Transition

- Similarity: 0.4236
- Prediction: The sequence of frames captures a dynamic sequence of action with the ice. Initially, the icing is in a state of rest, with no visible signs of activity. As the frames progress, the lid is removed, indicating the action of the icidal action. As we move forward, the liquid's state is blurred, with the lid positioned in re-positioning mode, implying the action is complete. The ice's surface remains unchanged, with its shape and texture reminiscent of a kitchen sink. The consistent movement of the lid, the consistent movement in the icy environment, and the consistent motion of the blades suggest a deliberate action.
- Reference: The sequence of images captures the gradual opening of a kitchen cabinet. Initially, the cabinet is only slightly open, providing a limited view of its organized lower shelf. As the frames progress, the door swings wider with each successive image, revealing more of the interior. From a neatly arranged collection of cans on the lower shelf to a more assorted arrangement of jars and containers on the upper shelf, the opening door parallels an increasing reveal of the cabinet's contents. The movement appears smooth, indicating a well-used and familiar action in the domestic setting, perhaps preparing for meal preparation or the resumption of kitchen activities.

#### Sample 36 — Transition

- Similarity: 0.4727
- Prediction: The progression of the sandwich's lifelong state is a clear progression from a pristine state to a state of disintegration. Initially, it is untouched, but as the frames progress, it becomes more and more cluttered, indicating a deliberate action. As the frames advance, the sandwich is positioned in a position that is primarily used for cooking, a transition from being a static state to being re-engaged with its contents. The hand's movements, from the hand to the sandwich, are evident, demonstrating a conscious effort to ensure that the sandwich remains intact and ready for use. The sandwich'
- Reference: Between the first and the third frame, there has been a progression from an unopened state to use. Initially, the butter tub is intact, with its contents concealed and untouched. As the frames progress, the hands and knife convey an intention to use, culminating in the third frame where the lid has been opened, and the spread has been partially scooped. The knife now holds a sample of the spread, signaling that it has been disturbed for the first time. The continuity of the scene is marked by the consistent positioning of the tub and the utensils, with the only changes occurring in the state of the butter and the position of the lid.

#### Sample 39 — Transition

- Similarity: 0.3570
- Prediction: Over the course of these frames, there's a clear progression in the cleaning process of the pan. Initially, the pan is in a state of disarray, with no visible or visible debris. As the frames progress, the cleaning action is emphasized, with the cleaning agent displacing the pan's surface, indicating a thorough cleaning. By the final frame, the dish appears to be awash in scrubbing, with a visible residue of soap and water. The consistent cleaning action, from the beginning to the end, is indicative of a more thorough cleaning process.
- Reference: The tap undergoes a transition from a state of active water flow to being turned off across these frames. Initially, the tap is open with water flowing out, as evidenced by the stream and wet surfaces. In the subsequent frame, the tap is seen in the off position, with the hand retracting from what appears to be the action of closing it. By the final frame, the tap remains off, and the individual's attention has turned to other tasks, confirming that the water flow has been successfully halted. The surrounding wetness on the sink decreases progressively, indicating the cessation of water and the passage of time since the tap was turned off.

#### Sample 41 — Transition

- Similarity: 0.3908
- Prediction: Over the progression of these three frames, the microwave door transitions from being partially open to fully open. Initially, the door is a clear sign of the person's presence, with the hand indicating that the door has been opened. As the frames progress, the hand's movements become more deliberate, indicating the door's movement. By the final frame, the person is able to see the door open, implying that the person has been seated or is about to be seated. The consistent state of the door remains unchanged, with a slight shift in the angle of the hand, highlighting the action of the microwave's interaction with the door.
- Reference: The progression of these frames captures a small but telling narrative of domestic life. Initially, the milk bottle appears abandoned and potentially open, vulnerable to spilling or contamination. As the frames advance, human interaction becomes evident, with the bottle being given attention, likely to prevent wastage or for storage after use. The cap, initially ambiguous, moves towards a state of being firmly placed back on the bottle. This sequence reflects a moment of care or routine within the kitchen's daily rhythm, a choreography of use and maintenance often overlooked.

#### Sample 45 — Transition

- Similarity: 0.3625
- Prediction: The progression of the milk shaker across these frames captures a clear progression in the state of its contents. Initially, it is a state of rest, with the shaker firmly anchored in the shaken milk. As the frames progress, the shake's movement becomes more deliberate, with a more pronounced motion, indicating the shake was agitated. By the final frame, the shaking has been stepped up, with shakers indicating a gradual movement in the milk's contents. The shaker's movements are a subtle transition, demonstrating the transition from a static state to a dynamic one, with shaking indicating an action
- Reference: The jam's transition from the jar to the bowl showcases its sticky and thick properties. Initially, it forms a cohesive shape on the fork, resisting the pull of gravity. As the fork moves away from the jar, the jam stretches into a thin, resistant strand, demonstrating its adhesive quality. Finally, the jam is deposited into the bowl, leaving a trail and losing its defined shape, reflecting its semi-liquid state that allows it to be spread while still maintaining a degree of thickness that prevents immediate flattening.

#### Sample 51 — Transition

- Similarity: 0.3126
- Prediction: Over the progression of these three frames, the bin undergoes a dynamic change in its state. Initially, it is partially open, with no visible signs of activity. As the frames progress, the lid is progressively opened, indicating a more active action. As we move forward, the contents of the bin are revealed, revealing a clearer and more visible view of the contents. The consistent state of the lid's position, the consistency of its contents, and the blurring of the surrounding environment suggest a deliberate action.
- Reference: The progression from the first to the third frame demonstrates the process of maintaining a cylindrical filter. Initially, the filter is shown partially obscured and in the midst of inspection, indicating the start of a maintenance activity. As the sequence progresses, the filter is removed and displayed in full view, revealing the extent of dirt accumulation and suggesting a thorough inspection or cleaning is underway. By the final frame, the filter is being reinserted into its housing, signaling the completion of the maintenance task. This sequence encapsulates a routine yet crucial aspect of ensuring the efficiency and longevity of the appliance or system the filter is part of.

#### Sample 57 — Transition

- Similarity: 0.3660
- Prediction: Over the course of these three frames, there's a clear progression in the state of the pot. Initially, the pot is in a state of rest, with the lid open and the pot's contents positioned in receptive positions. As the frames progress, the person's hand is engaged in adjusting the pot to the appropriate temperature, indicating that the pot has been fully cooled. As they progress, there is a noticeable change in the pot setting, with a more or less constant change in temperature. The consistent state of heat throughout the frame suggests a gradual change in pot settings, resulting in optimum pot settings. The consistency of the water level, the consistency of its surface, and the consistent movement of the lid suggest a deliberate action to ensure that the water is not dripping or leaking.
- Reference: The sequence of images chronicles the process of removing a used coffee filter from the coffee maker. Initially, the filter is shown seated within the machine, saturated with coffee grounds from recent use. As the sequence progresses, the filter is lifted and angled in preparation for disposal. The hand's grip adjusts to maintain control over the filter and its contents, preventing any spillage of the grounds. The careful handling reflects an understanding of the filter's fragility when wet and the need for a deliberate movement to avoid making a mess. The transition from the coffee maker to its intended destination is portrayed with attention to the filter's integrity and the containment of the used grounds.

#### Sample 61 — Transition

- Similarity: 0.4232
- Prediction: The sequence of frames captures a dynamic sequence of the table's unfolding. Initially, the table is positioned in a state of rest, with the paper being positioned on the table. As the frames progress, the hand's movements become more deliberate, indicating that the paper is being shifted. By the final frame, the paper has been positioned, with its surface positioned and the paper positioned more evenly. The hand'
- Reference: The journey of the crumb across these frames tells a story of displacement and cleaning. Initially stationary and almost camouflaged by the tablecloth's pattern, the crumb is subtly jostled by the unseen forces exerted by the approaching vacuum cleaner. As the cleaner moves closer, the crumb's environment becomes visibly disturbed, with the material of the tablecloth wrinkling and shifting. Finally, the crumb is drawn into the shadow of the vacuum cleaner, its final moments on the table marked by a dramatic change in light and position, signifying the crumb's inevitable conclusion of being vacuumed away.

#### Sample 62 — Transition

- Similarity: 0.4032
- Prediction: Over the course of these frames, the flour undergoes a noticeable transformation from a hazy state of kneading to a more streamlined, more pronounced state of incorporation. Initially, the dough is a mess, with no visible signs of mixing or separating. As the frames progress, the hand's movements become more deliberate, indicating that the dough has been thoroughly incorporated into the mixture. By the final frame, the knicking action has become more consistent, with the dough forming a smoother and more uniformly distributed. The progression of the flour's state is indicative of a change in the flour
- Reference: The transition of the olive oil from containment to release is captured across the frames. Initially, the oil is securely enclosed within the bottle, its potential to enhance the dish latent. As the cap is removed and the bottle is tipped, the olive oil is on the cusp of transformation, from an individual ingredient to an integral part of a culinary mixture. Finally, the oil is liberated, joining the other components in the bowl, its glistening stream signifying the merging of separate elements to create a cohesive whole. This progression from anticipation to action reflects a common, yet pivotal moment in cooking, where the precise addition of an ingredient can alter the character of a dish.

#### Sample 86 — Transition

- Similarity: 0.4556
- Prediction: Over the progression of these three frames, the bag undergoes a dynamic transition from being partially concealed to being fully opened. Initially, the person is hesitant to open the bag, but as the frames progress, the hand's movements become more deliberate, indicating that the bag is being opened. By the final frame, the hands are more engaged in the action, demonstrating the gradual movement of the bag. The blurring of the person's actions and the blurring between the two frames suggest a transition from a static state to a more dynamic state, implying a person'
- Reference: The leek, originally in a state of transition from bag to counter, has undergone a rapid and unscheduled descent to the floor. Initially held in a stable position, it has slipped from the person’s grasp, flipping end over end as it falls. The stages of its fall are marked by the increasing disarray of the plastic wrap and the blurring of its leaves, telling a story of motion and gravity at work. This sequence captures the leek's accidental journey from control to chaos, each frame depicting a further stage of its unintended flight towards the floor.

#### Sample 89 — Transition

- Similarity: 0.3485
- Prediction: Over the progression of these three frames, the microwave undergoes a subtle transition from a partially open state to a fully closed state. Initially, the light is dimmed, with the switch indicating that the microwave is closed. As the frames progress, the lighting changes to accentuate the transition, with a gradual change in the light's position. By the final frame, the kitchen appears to be fully open, with its lights dimmed and the door open, indicating the microwave has been closed. The transition from the fully closed position to the fully open position is a clear sign of the microwave's closing state, with no noticeable change in its position or the lighting's state.
- Reference: Throughout the progression of the three frames, the squash container undergoes subtle shifts in positioning. Initially, it stands upright in the first frame with the cap removed. As we transition to the second frame, a minor tilt or movement is evident, though the cap's position remains unchanged. By the third frame, the container seems to stabilize, reflecting a similar state as observed in the second frame. Throughout this progression, the container remains unsealed, implying a continuous phase of usage or preparation for consumption.

#### Sample 90 — Transition

- Similarity: 0.4812
- Prediction: The progression of the sliced avocado undergoes a clear transformation from a whole avocado to a partially sliced piece. Initially, the avocado is whole, with the skin still intact. As the frames progress, the knife's action becomes more deliberate, revealing the avocado's flesh and removing the skin. The process is a reminder of the importance of preserving the avocado for the preparation of meals, and the avocado itself is replete with flavor and texture. The transition from being whole to being sliced is reminiscent of a chef's knife, with a sharp edge and a smooth, slicing motion.
- Reference: The pepper's transformation is methodical and precise. Initially presented as a halved piece, it then becomes the focal point as it's sliced into segments, and finally, arranged neatly with its seeds removed. Across the frames, the pepper's bright yellow hue remains consistent, yet its form evolves from a whole, unaltered vegetable to a prepared ingredient ready for culinary use. The changes in its state are deliberate, indicating a step-by-step preparation process likely leading up to a recipe.
Frame_1:
The pepper lies on the cutting board, freshly halved with a vibrant, glossy yellow exterior that catches the light, signaling the firmness of its flesh. The cut end of the pepper is clean, suggesting a sharp knife was used. The seeds and pith, hidden from view, are assumed intact, as there is no evidence of them on the board. The position of the pepper, with the stem end away from the hand, hints at the initial stage of slicing, where the first cut has been made to open the pepper for further cutting or de-seeding.

Frame_2:
The pepper now reveals its interior, cut into two distinct halves with the seeds and pith exposed. It is open like a book, with the seeds concentrated near the stem, which remains attached to one of the halves. The interior flesh is a pale yellow, contrasting with the richer hue of the outer skin, and the membranes are pronounced, dividing the inner space into segments. The pepper rests with its insides facing upward, ready for the next step of preparation.

Frame_3:
In this frame, the pepper has been transformed into a series of slender slices, laid out in a fan shape that displays both the bright exterior and the lighter interior flesh. The seeds have been removed, indicating a thorough cleaning. Each slice is uniform in thickness, evidencing a deliberate and careful cutting technique. The knife used has left smooth edges, and the pepper pieces are arranged neatly for presentation or cooking.

State_change_caption:
The progression of the pepper's preparation reveals a methodical process. Initially, it is presented as a halved item with hidden seeds, then transitions to an open state with its core exposed, highlighting the natural partitioning of its flesh. Finally, it is cleanly segmented into even slices, seeds removed, and meticulously arranged. This sequence showcases not only the steps of preparing the pepper but also the care taken to maintain its aesthetic and structural integrity throughout the process. The change from a whole vegetable to a prepped ingredient is done with precision, preparing it for its final culinary destination.

#### Sample 95 — Transition

- Similarity: 0.4886
- Prediction: Over the progression of these three frames, the box transitions from a partially open state to a fully opened state. Initially, the person's hand is demonstrating a willingness to open the box, indicating a desire to open it. As the frames progress, the hands are demonstrating the action of opening the box. By the final frame, the hand is showing the contents of the box in a clear, revealing state, implying that the contents are being accessed. The person'
- Reference: The lettuce transitions from being stored to being prepped for use. Initially, it's in a chilled, inert state, enclosed within the refrigerator environment. Then it's in motion, indicating transit from the fridge to a preparation area. Finally, the lettuce becomes the focal point of an imminent action, with hands ready to open the bag, which suggests that the lettuce is about to be transformed from its packaged state to a component of a meal or perhaps transferred to a different storage container for extended freshness. The surrounding blur in the second frame emphasizes the movement and the shift from one state to the next, while the third frame's clearer, more static environment suggests readiness for the next step in the lettuce's usage.

#### Sample 107 — Transition

- Similarity: 0.4946
- Prediction: Over the course of these frames, the dough undergoes a noticeable transformation from a hazy state of kneading to a more streamlined state of incorporation. Initially, the flour is a bit sticky, but as it becomes more incorporated, the texture becomes more uniform and the dough becomes more cohesive. By the final frame, the k
- Reference: The biscuit mixture undergoes a visible transformation across the three frames. Initially, the biscuits retain their shape but are soon subjected to pressing and mixing, breaking them down into smaller fragments. As the process unfolds, the biscuits combine with the chocolate, becoming less distinct and more integrated into a cohesive blend. The hands actively work the mixture, indicating a tactile approach to achieve a thorough blend. This progression suggests a recipe that requires the biscuits to transition from solid pieces to a malleable, unified mixture, likely as a base or component for a dessert.

#### Sample 109 — Transition

- Similarity: 0.4397
- Prediction: Over the progression of these frames, the icing board undergoes a noticeable transformation. Initially, it is a bare and unadorned surface, with no visible or visible signs of use. As the frames progress, the person's movements and actions become more deliberate, indicating a more active and active action. By the final frame, the board is more fully positioned, demonstrating a gradual change in its position and shape. The consistent pattern of the coiled and rolled edges, the consistent movement of the hand, and the consistent motion of the blade, suggest a deliberate action
- Reference: The progression of the glove's state across the three frames showcases its role in the kitchen workflow. Initially laid out, it serves as a silent participant in meal preparation. As it is donned in the second frame, it becomes an active tool in the cleansing process, hinting at human interaction and the routine of maintaining cleanliness. Finally, its restful drape over the sink's edge signifies the end of its immediate utility. The glove's journey from inert to active, then back to a state of rest, mirrors the rhythms of domestic life, where objects are enlivened by human use and then returned to their inanimate repose, awaiting the next call to service.

#### Sample 110 — Transition

- Similarity: 0.4504
- Prediction: Over the progression of these three frames, the hand's uniformity and posture are captured in a sequence of action. Initially, it is positioned in pristine condition, with no visible signs of wear or tear, and then it is moved to a more stable position, indicating a gradual movement. As the frames progress, the hands' movements become more deliberate, revealing a variety of different actions and actions. The hand'
- Reference: The chair undergoes a transition from being partially tucked under the table to being pulled out and away from it. The shift in its shadow and the changing perspective of the chair's legs and seat in relation to the surrounding objects, like the table and the floor tiles, indicate the motion. Throughout the frames, the chair's position relative to the fixed elements in the room, such as the table and stove, highlights the trajectory of movement. The consistent lighting across the frames accentuates the changing angles and positions of the chair, marking the progress of its movement within the space.

#### Sample 119 — Transition

- Similarity: 0.4486
- Prediction: The progression of the squeegee's transformation from a partially rinsed to a fully rinsed state is evident across the three frames. Initially, the rinsing process is a gradual process, with the utensils being positioned in a downward motion, indicating the final rinse. By the final frame, the water level is reduced, with a focus on the surface and the resulting raffination of the surface. The consistent movement of the hand, a shift in the direction of the water, indicates a thorough cleaning of the vessel, highlighting the progress of the cleaning process.
- Reference: The sequence of frames captures the V60 undergoing a thorough cleaning process. Initially fully submerged to soak and loosen any coffee residue, it is then partially lifted out of the water for inspection and targeted cleaning. The final frame shows a more aggressive cleaning with a brush, indicating a step-up in the cleaning effort to address any persistent stains. Throughout these frames, the V60 is handled with care, and the cleaning action is methodical, reflecting the importance of maintaining the purity of flavor for future coffee brewing. The water's agitation and the evolving position of the V60 demonstrate a progression from soaking to active cleaning, and finally to detailed scrubbing, ensuring a comprehensive cleanse of the coffee dripper.
Frame_1:
The V60 is submerged in a basin of soapy water, enveloped by a froth of bubbles, indicating the commencement of the cleaning process. A hand is visible, gripping the V60 from the top, likely having just placed it into the water. The position of the V60, with its opening directed downwards, suggests that any loose coffee grounds have likely been rinsed away or are in the process of being dislodged by the water's embrace. The translucency of the water surrounding the V60 is clouded, possibly by the initial release of coffee residue.

Frame_2:
Now partially elevated from the sudsy bath, the V60 reveals its conical shape and the residual coffee markings within. The hand's grip has shifted to the upper rim, facilitating a careful inspection or preparation for a more targeted cleaning. Water droplets cling to the exterior, reflecting the kitchen's lighting, and the remnants of coffee stains are more pronounced against the V60's otherwise clean interior, signaling that some areas might require additional attention.

Frame_3:
The hand actively employs a scrubbing brush on the V60's interior, suggesting a shift to a more aggressive cleaning method. The V60 is tilted, optimizing the angle for thorough scrubbing, as the bristles of the brush work against the interior surface. The motion of scrubbing is implied by the position of the brush and the hand's orientation, focused on eradicating any stubborn stains or residue that may have clung after the initial soak.

State_change_caption:
Across the sequence, the V60's cleaning journey is evident. Initially nestled in the water for a soak, it is next examined and scrutinized for remaining impurities after being lifted from the water. This progression from soaking to inspection sets the stage for the final, vigorous scrubbing captured in the last frame. The transition from gentle rinsing to active scrubbing demonstrates a methodical approach to ensure the V60 is restored to a state befitting its use in brewing clean, untainted coffee. The careful handling throughout underscores the importance placed on maintaining the V60's condition.

#### Sample 123 — Transition

- Similarity: 0.4681
- Prediction: Over the course of these three frames, there is a clear progression in the state of the sink. Initially, the sink is in a state of disarray, with no visible signs of activity. As the frames progress, the water level changes to a more stable state, with the sink's surface becoming more exposed and the water's contents less visible. By the final frame, the surface is more exposed, with a less noticeable change in the water content. The transition from the sink to the water is largely a blur, with only a few visible changes in the overall state of water quality.
- Reference: The hand demonstrates a progression of motion associated with thorough hand-washing. Initially, the hand engages with the water, likely activating soap and starting to cleanse. As the frames progress, the hand's movements become more pronounced, suggesting a vigorous scrubbing action, pivotal for effective cleaning. By the final frame, the hand moves away from the water source, indicating the rinse phase is concluding. Throughout the sequence, the motion blur and changing position of the hand relative to the sink and the surrounding environment narrate a common but critical personal hygiene practice. The hand's journey from initial immersion to final withdrawal signifies the near completion of the cleansing process.

#### Sample 131 — Transition

- Similarity: 0.4642
- Prediction: Over the course of these three frames, the rag transitions from being partially soaked to being fully soaked. Initially, the cloth is firmly held, with the hands positioned in a downward motion. As the frames progress, the person's actions change from a gentle hand to a more vigorous one, indicating a thorough cleaning. By the final frame, the hands are firmly engaged, demonstrating a clean, sanitized surface. The cloth's transition from being fully wet to being thoroughly washed is a clear sign of a cleaning process that is aimed at a particular area.
- Reference: The sequence of images captures the motion of a yellow, square-cutout grid being manipulated by a person's hand above a kitchen sink. Initially, the grid is held vertically, as if it were being lifted or turned. Progressing through the frames, the grip and orientation of the grid change, indicating a rotation or flipping motion. By the final frame, the grid is nearly horizontal and appears to be carefully positioned towards the sink, which suggests it is being placed within or aligned with the sink for a purpose, such as drying dishes or protecting the sink's surface. The movement is smooth and deliberate, reflecting the person's intent to adjust the grid's position within the domestic context.

#### Sample 145 — Transition

- Similarity: 0.2199
- Prediction: The progression of the sliced banana undergoes a clear transformation from a whole to a fully sliced piece. Initially, the banana is untouched, with no visible signs of ripening. As the frames progress, the avocado is progressively sliced, with the skin separating from the avocado. The process of removing the avocado from its packaging is evident, with a fresh, ripe avocado revealing a pristine, slicked-out portion. The resulting ripened avocado is now a part of a larger, more nutritious meal, a source of protein and a nutritious source of fiber.
- Reference: From its initial resting state atop the cutting board, the pitta undergoes a transformation through human interaction. Initially displayed in its full, untouched form, it's then gently grasped, indicating the commencement of an action. As we progress to the final frame, the piece of pitta's purpose is revealed: to be a medium for the hummus. Its partial submersion in the creamy dip not only alters its appearance, with one end now glistening and coated, but also its texture, absorbing the hummus and becoming a delightful blend of soft bread and rich, flavorful dip.

#### Sample 147 — Transition

- Similarity: 0.4823
- Prediction: Over the course of these three frames, there's a clear progression in the state of the gas burner. Initially, the burner is inactive, with no visible signs of use. As the frames progress, the user's hand is engaged, indicating that the burner has been turned on. As this sequence progresses, the hand's interaction with the burner becomes more deliberate, implying that the user is adjusting the burner settings. The consistent state of interaction with its knobs, and the constant interaction with their contents, suggest a gradual change in the burner's state.
- Reference: Starting from a stable position, the blender is initially interacted with by the user who seemingly prepares or adjusts it for a specific task. As the frames progress, the mixer is visibly subjected to a more dynamic and swift movement. The rapid action and the blurring surroundings in the third frame highlight a significant change from the initial state, suggesting a turn or adjustment made with intent or purpose by the user. This transformation signifies the progression from a static position to an active or dynamic state, emphasizing the user's active engagement with the appliance.

#### Sample 150 — Transition

- Similarity: 0.4209
- Prediction: Over the course of these three frames, the kettle undergoes a clear transition from being a state of rest to being withdrawn. Initially, the saucepan is in a position of rest, with the lid positioned in re-positioning mode. As the frames progress, the hand's movements become more deliberate, indicating that the kettle is being redirected. By the final frame, the person's actions become more pronounced, implying that the saucepan has been withdrawn from its position. The consistent state of the kettle's state of reposessed state is evident throughout the sequence, with a consistent hand'
- Reference: Over the course of these three frames, the spice undergoes a transformation from a passive and partly concealed item within a cluttered cupboard to an object of focus and interaction. Initially nestled among various kitchen items, its importance becomes apparent as other objects are moved aside, allowing it clearer visibility. As the frames progress, the intention of interaction becomes clearer, culminating in the hand's direct contact and the spice's removal from its resting place, indicating its imminent use or inspection in the kitchen's activities.

#### Sample 153 — Transition

- Similarity: 0.3398
- Prediction: Over the course of these frames, there's a clear progression in the cleaning process. Initially, there is a noticeable presence of stains, with the first frame showing a visible streak of a scrubbing pad. As the frames progress, there appears to be a gradual change in the surface of the counter, with a more visible and progressively cleaner surface. By the third frame, there seems to be less of soiled, with more of the cloth wringing and the sink slammed against the counter. The process continues, with each frame indicating a different action. The consistent pattern of the cleaning action across the frames suggests a thorough cleaning process, with
- Reference: The sequence of images captures a dynamic progression: starting with the pepper mill in a state of uncontrolled descent, then being caught and held firmly, and finally being moved purposefully to a new location or state. The action begins with a state of disorder, indicated by the pepper mill's tilt and the hurried hand movements, then transitions to a controlled grasp that corrects the mill's trajectory, and culminates in a deliberate and controlled motion, likely to reposition the mill. This progression showcases a quick response to an unexpected situation, leading to the stabilization and purposeful handling of the kitchen utensil.

#### Sample 157 — Transition

- Similarity: 0.3795
- Prediction: Over the course of these frames, the cloth undergoes a noticeable transformation from a state of wilting to a fully soaked state. Initially, the fabric is firmly saturated with water, indicating a gradual rinsing process. As the frames progress, the water's state changes to slushy, resulting in a more soaked and drier fabric. By the final frame, the wringing action is complete, demonstrating the gradual re-rinking of the cloth, implying a reversing of the action. The transition from soaking to raffination is a clear sign of the process's effectiveness
- Reference: Over the course of these three frames, the sink transitions from a state of post-use with residual water and suds to an active cleaning scenario. The flow and direction of water change as the person interacts with the faucet, adjusting the water's trajectory and presumably the temperature. The consistency of suds near the drain suggests a continual cleaning process. The person's hands move from a relaxed position to one that is more involved in the task, demonstrating the dynamic nature of the task of washing. The stationary position of cleaning implements and dish soap signifies a controlled environment where the main activity is centered around the use of water in the sink basin.

#### Sample 158 — Transition

- Similarity: 0.4690
- Prediction: Over the progression of these three frames, the table undergoes a dynamic change in its state. Initially, it is a little cluttered, but as the frames progress, it becomes more and more open, indicating a more active interaction. As the frames advance, the person's movements become more deliberate, implying a shift in the position of the table. The consistent movement of the chair, the overlapping of the items on the table, and the emergence of the person in the kitchen are indicative of a deliberate action. The transition from the upright position to the position is reminiscent of sweeping or sweeping, a motion that is characterized by a movement of slats, swivels, or a hand-held device.
- Reference: From a position of rest, the orange has been subjected to an external force, setting it into motion across the table. The transition in its state is evident through the progressive distortion of details on its skin and the shift in reflected light. As it traverses the wooden expanse, it not only changes its position but also its interaction with the ambient environment, exemplified by varying highlights and shadows. This journey from stillness to movement showcases the orange's transient and dynamic nature when acted upon.

#### Sample 163 — Transition

- Similarity: 0.4711
- Prediction: Over the progression of these three frames, the hand's uniformity and posture change from a passive position to a more active one. Initially, the hands are positioned in a position to grasp the hand, indicating a shift in their posture. As the frames progress, the person's movements become more deliberate, demonstrating a shifting focus on the hand and the hand itself. The hand'
- Reference: Starting from a mostly folded or bunched state, the tablecloth undergoes a transformation as it's progressively unfurled across the frames. The sense of motion and activity is evident, with the cloth moving from being largely concentrated in one area to spreading out, covering more of the surrounding environment. By the third frame, the tablecloth's placement seems almost finalized, with reduced movement and a more settled appearance, indicating the nearing completion of the unfolding and setting process.

#### Sample 166 — Transition

- Similarity: 0.4572
- Prediction: The sequence of frames captures a clear progression in the state of the rag. Initially, it is a state of disarray, with no visible signs of action. As the frames progress, the agitation of the cloth becomes evident, with the cloth firmly positioned, indicating a re-rinsing process. As we move to the final frame, the cloth's state of rest is evident, demonstrating a gradual movement of the hand, a sign of a more active and active action. The transition from the rigors of the drying process to the repositioning of the garment is reminiscent of resetting the cloth, reversing the motion of the action.
- Reference: The sequence of images captures a clear progression in the interaction between the person and the bottle. Initially, the bottle is at rest with an open cap. As the frames advance, the person's hand engages with the bottle, specifically the cap, moving from touching to turning. The cap transitions from a state of being unsecured to one where it is being tightened. This motion is consistent with the typical method of closing a bottle, and the person's grip and wrist movement indicate a deliberate action to seal the bottle, likely concluding the task at hand.

#### Sample 167 — Transition

- Similarity: 0.4906
- Prediction: Over the course of these three frames, the sponge undergoes a noticeable transformation from a state of rest to a pause in the process. Initially, it is a little damp, but as it is being drained, the water's surface becomes more exposed, indicating that the sponge is being used. As the frames progress, the sink's state of hydration becomes more active, with the water circulating more vigorously, resulting in a more pronounced flow of water. By the final frame, the squeaking action is complete, with a water-filled sponge indicating the completion of the process,
- Reference: The sequence of the frames captures a progressive change in the state of the tap, beginning with a steady stream of water, transitioning through an interrupted flow, and concluding with the cessation of water discharge. The hand engaging with the tap serves as the agent of change, exerting control over the water flow. This sequential action reflects a common, deliberate action to conserve water or to conclude a cleaning task. The consistency of the environment around the tap emphasizes the focused change in the tap's state, from open to closed, as the primary activity within these frames.

#### Sample 170 — Transition

- Similarity: 0.2968
- Prediction: The progression of the squid's life spans from a state of rest to a process of cooking. Initially, the gill is in a position to be brushed, then a slurry is thrown in, indicating a final action. As the frames progress, the chef's hand moves to the next frame, demonstrating the action of squeezing the worms. The squish's state of being is evident, with the grate positioned in sweeping motions, implying a deliberate action. The hand's movements are consistent throughout the sequence, highlighting the action's
- Reference: Over the course of the three frames, the pepper's state transitions from being actively dispensed to resting on the tomatoes. Initially, the pepper is in motion, captured as it leaves the shaker and begins to settle on the tomato slices. By the second frame, the application of the pepper appears to have reached its peak, with visible grains dotting the surface of the tomatoes. In the final frame, the action of seasoning is complete, and the pepper has ceased its trajectory, now lying static on the tomatoes. The sequence captures the essence of seasoning - a momentary action that changes the state of both the ingredient and the final dish.

#### Sample 171 — Transition

- Similarity: 0.4713
- Prediction: Over the course of these frames, the rice undergoes a clear transformation from a state of being partially cooked to a fully cooked state. Initially, the water is a source of moisture, indicating that the rice is being cooked, resulting in a more uniform and uniform texture. As the water becomes more agitated, the grain appears to be loosened, forming a uniform, uniform texture, implying that the water has been boiled. By the final frame, the steamed rice is preparing to be served, demonstrating the transition from being a slurry to
- Reference: Throughout the progression of these three frames, there's a discernible shift in the state of the oat within the pan. Initially, the oat seems to be in a static and uniformly spread state. However, as we move to the subsequent frames, subtle signs of movement and redistribution become evident. By the third frame, the oat has experienced more pronounced agitation, leading to clear disruptions in its uniformity and resulting in noticeable gaps and clusters. This change suggests a dynamic process, possibly influenced by external factors such as shaking or stirring, altering the oat's state and distribution within the pan.

#### Sample 182 — Transition

- Similarity: 0.3383
- Prediction: Over the progression of these frames, there's a clear progression in the state of the oven. Initially, the oven is a little bit damp, with no visible signs of wear or discoloration. As the frames progress, the person's hand is more likely to be a professional or home-owner, indicating that the oven has been properly tended. By the final frame, the door is open, revealing a more open and inviting space, demonstrating the process of removing the oven from its position. The transition from the initial state of being a damp and damp oven to a fully open one is reminiscent of the process described in the previous frame.
- Reference: The series of images collectively narrate the progression of a laundry routine. Initially, the preparatory action of dispensing detergent is suggested, though the actual liquid is not seen, possibly due to the timing of the snapshot. As the sequence advances, there is an interlude marked by a lone sock on the floor, which points to a common mishap during laundry tasks. The final frame resolves into the act of removing the clothes from the washing machine, indicating the completion of the washing cycle. The clothes' journey from being washed to being ready for drying is depicted subtly through these snapshots, highlighting the ordinary yet essential chore of laundry management.

#### Sample 187 — Transition

- Similarity: 0.3945
- Prediction: The sequence of frames captures a clear progression in the handling of the jar. Initially, it is a state of rest, with no visible signs of action. As the frames progress, the holder is positioned, indicating a gradual movement, with the lid positioned in a position that indicates the action of the hand. The hand's movements are evident, with a steady hand motion, implying a deliberate action. The jar's state of motion is reminiscent of a kitchen sink, with its slats and handles positioned strategically, demonstrating a dynamic movement.
- Reference: The chicken has undergone a minimal change in state across these frames, primarily being the person's interaction with it. Initially, it is presented as having been recently sliced, with no further processing. Subsequently, there is a transition to hand washing, which indicates the chicken handling is momentarily paused. Finally, the person dries their hands, preparing to resume interaction with the chicken. The chicken's state remains constant as a raw, roughly cut ingredient, awaiting further preparation such as seasoning or cooking. Throughout these frames, the focus is not so much on the transformation of the chicken itself, but rather on the hygienic practices surrounding its preparation.

#### Sample 211 — Transition

- Similarity: 0.4587
- Prediction: Over the progression of these frames, the cloth undergoes a noticeable transformation from a state of wilting to a more active state of cleaning. Initially, it is a bare, bare-kneading state, with the cloth's surface exposed to the water. As the frames progress, the water's state changes from squeaking to soaking, with a gradual increase in the amount of water being absorbed. By the final frame, the wavy fabric is more fully soaked, with more water being distributed, indicating a deeper cleaning process. The transition from soaking to wringing is reminiscent of the process of a sponge being wrung, with its wrinkly appearance and the resulting wrintiness.
- Reference: The progression of the sink's state from the first to the third frame narrates a short story of kitchen clean-up. Initially, we see the sink area with splashes of water and a single piece of vegetable debris, hinting at prior use. As time progresses, there's evidence of active cleaning—the presence of water streaks, and cleaning implements suggest the person is midway through the task. By the third frame, the cleaning appears nearly complete; the sink is wetter, the debris has been removed, and the person's hands are together in a gesture that often signifies a job well done. Throughout these frames, the state of the sink transitions from used and in need of attention to clean and orderly, reflecting the mindful efforts of the individual tending to the kitchen's cleanliness.

#### Sample 225 — Transition

- Similarity: 0.3970
- Prediction: Over the course of these three frames, the blender undergoes a clear transition from a state of rest to a fully engaged, paused, and re-engaged position. Initially, the user is positioned on the top of the blender, indicating a gradual blending process. As the frames progress, the hand is progressively engaged, suggesting a more active or pause-driven action. By the final frame, the person is firmly engaged, with the blender's lid still firmly closed, implying a complete blending. The user's movements are consistent throughout the sequence, demonstrating a steady, steady, and consistent motion.
- Reference: The mixture undergoes a noticeable transformation through the frames. Initially, it starts with a lumpy and uneven texture, a common state before ingredients are fully mixed. As the blending proceeds, there's a clear transition from this coarse start to a smoother consistency. By the end, the mixture evolves into a homogenous, airy, and glossy batter, reflecting the thorough integration of all ingredients. This progression is typical for mixtures where air incorporation is essential, often seen in recipes for cakes, muffins, or other baked goods, where aeration contributes to a light and tender final product.
Frame_1:
The mixture presents a vivid yellow hue, likely indicative of egg-based ingredients, with visible streaks of white and patches of different consistencies, suggesting the initial incorporation of ingredients. There is a discernible unevenness, with some areas appearing more liquid and others showing soft peaks, possibly from an uneven mixing speed or the starting phase of ingredient integration. The surface reveals air bubbles being folded into the blend, a sign of the mechanical action from the beaters beginning to aerate the mixture.

Frame_2:
There is a notable reduction in the streaking of the mixture, indicating a progression toward uniformity. The color is now more consistent throughout, without the distinct white areas seen previously, implying a better combination of ingredients. The texture is creamier, and the previous soft peaks have started to settle into a more cohesive batter. The beaters are well-coated, and the mixture exhibits a sheen, suggesting the development of a silky structure, characteristic of a well-emulsified blend.

Frame_3:
The mixture has reached a homogenously creamy state with a uniform yellow coloration and a smooth, glossy finish, consistent with a well-blended batter. The surface is free of any lumps or unincorporated patches, and the mixture now holds a ribbon-like trail from the beaters, which indicates good viscosity and structure. The overall volume appears to have increased, and the mixture maintains its shape around the beaters, demonstrating that sufficient air has been incorporated to give it a light, airy texture.

State_change_caption:
Throughout the frames, the mixture evolves significantly. Initially, the mixture is rough and variegated, with distinct colors and textures indicating the beginning of the blending process. As the blending continues, there's a clear progression toward a more homogeneous state, with the texture smoothing out and the color becoming uniform. By the final frame, the mixture has transformed into a creamy, airy, and smooth batter, a sign of proper technique and the readiness for the next step in the recipe. This transformation is critical for achieving the desired end product in baking, where the consistency of the batter can greatly influence the texture and rise of the baked good.

#### Sample 226 — Transition

- Similarity: 0.4891
- Prediction: Over the course of these three frames, the package undergoes a clear transition from being fully uncovered to being partially uncovered. Initially, the packaging is untouched, with no visible signs of damage or degradation. As the frames progress, the person's hands move from one hand to the other, revealing the packaging's state of being fully exposed. The hands' movements are evident, with the packaging indicating a gradual change in the packaging state. The progression of the packaging to be fully embraced, with its contents indicating the presence of a potential source of food or a source of protein, is a key
- Reference: The wrap undergoes a transformation through these frames, from being an uncut piece draped over the counter's edge to being cut with precision. Initially, it is presented in a state of potential use, and through the frames, it encounters the shears that alter its form. The cutting process is deliberate, resulting in the wrap's detachment from its roll, and the aftermath shows a tidy work area, signifying the end of this particular task. The overall sequence captures a brief yet significant moment in the broader context of kitchen activities, from preparation to the eventual cooking phase.

#### Sample 231 — Transition

- Similarity: 0.4641
- Prediction: Over the course of these three frames, the onion undergoes a clear transition from being partially uncovered to being fully opened. Initially, the person's hand is hesitant, but as the frames progress, the action becomes more deliberate, indicating that the onion is being fully uncovered. As the frames advance, the hand's movements become more deliberate and pronounced, implying that the person is preparing to open the onion. The person'
- Reference: The plastic bag undergoes a clear transformation across the three frames, starting from a sealed and taut condition to an increasingly open state. Initially, the plastic shows tension and resistance, but as the fingers work to open it, this tension gives way to a more relaxed and malleable form. The opening action results in the gradual revelation of the bag’s contents, changing the plastic’s shape and the distribution of the items inside. The process of opening alters the bag from a closed container to one ready for the retrieval of its contents, with visible changes in the plastic's texture and form.

#### Sample 232 — Transition

- Similarity: 0.4627
- Prediction: Over the course of these three frames, the blender undergoes a clear transition from a state of rest to a more active and agitated state. Initially, the lid is still firmly attached to the blender, with the user's hand positioned at the top of the blender. As the frames progress, the user is now engaged in a deliberate action, indicating that the blender is ready to be used. The blender's position is a subtle transition from being a static and unresponsive state to agitating and releasing the blender'
- Reference: The progression of the ingredient's state from the first to the third frame demonstrates the dynamic process of blending. Initially, the mixture presents a smooth and well-incorporated state. As the mixing continues, it begins to show signs of agitation, with the surface forming depressions and peaks that indicate active mixing. Throughout the process, the consistency of the batter remains thick and stable, with no signs of separation, suggesting that it's nearing the desired state for baking where air has been sufficiently incorporated to ensure a good rise. The uniformity of the color also suggests that the ingredients are well-emulsified, providing a stable base for the finished product.

#### Sample 236 — Transition

- Similarity: 0.3785
- Prediction: The progression of the cheese's lifecycle traces a clear progression from a pristine state to a fully melted state. Initially, the cheese is untouched, with no visible signs of separating. As the frames progress, the knife is progressively slicing the cheese, revealing a series of small pieces of cheese. The cheese'
- Reference: Over the course of these frames, the butter transitions from a freshly unwrapped, solid state to a more spreadable consistency as it warms slightly from room temperature and the heat of the hands. Initially, the butter's resistance to spreading creates a rough, textured surface on the bread. As the spreading progresses, the butter starts to give way, becoming more malleable, which is evidenced by the increasing coverage on the bread. The unevenness of the spread throughout suggests a battle against the butter's firmness, a common scenario when butter has not been given time to soften adequately before use.

#### Sample 238 — Transition

- Similarity: 0.3615
- Prediction: Over the course of these three frames, the bottle undergoes a clear transition from being fully closed to being fully opened. Initially, the cap is positioned in a state of disengagement, with the lid firmly pressed against the bottle. As the frames progress, the person's hand moves from one side to the other, indicating the action of removing the cap. By the final frame, the lid is fully open, with a slight movement, demonstrating the action's impact on the bottle's contents. The person'
- Reference: The flour undergoes a dynamic transition across the three frames, starting with a gentle introduction into the bowl, increasing to a swift pour, and culminating in a substantial deposit of flour. The initial light dusting evolves into a significant mound, reflecting the increasing volume and momentum of the pour. The flour's consistency remains constant, fine and powdery, but its behavior changes from a delicate stream to a more forceful waterfall. This progression is marked by the growing cloud of flour dust, the rising mound within the bowl, and the change in the flour's surface from scattered to smooth and peaked. The action captures the careful control yielding to the forces of gravity and volume as the contents of the jar deplete.

#### Sample 240 — Transition

- Similarity: 0.4390
- Prediction: Over the course of these frames, the rice undergoes a clear transformation from a static state to a more dynamic state. Initially, the sauce is a little clumpy, with a few pieces of the rice sticking out, and the water rushing through the rice. As the stirring progresses, the water is able to move the rice into a softer, more liquid-filled state, indicating that the rice is being stirred. By the final frame, the cooking process has been completed, with the rice forming a smooth, spongy texture, with no lumps or lumps. The consistency of the sauce remains consistent throughout the course, and it's likely that the water has been boiled to provide a uniform texture throughout the rice's cooking process.
- Reference: From the first to the third frame, there is a noticeable transformation in the state of the curry. Initially starting as a lighter, broth-like mixture with distinct floating ingredients, it transitions into a denser, more cohesive dish. As the cooking progresses, the liquid content reduces, and the curry takes on a richer hue, signifying the melding of flavors and ingredients. By the third frame, the curry exhibits a thick, integrated consistency, with the ingredients softened and fully incorporated, indicating its near completion in the cooking process.

#### Sample 241 — Transition

- Similarity: 0.4033
- Prediction: The sequence of frames captures a clear progression in the handling of the ice cube. Initially, it is a static, unbalanced state, with no visible movement. As the frames progress, the icing is positioned in a position that indicates a gradual change in the direction of the action. By the final frame, the action is merely a transition, with the icicles and the crumbs indicating a change in direction. The consistent movement of the lid, the constant motion of the blade, and the constant movement of its surface indicate a deliberate action.
- Reference: Between the three frames, the primary change involves the red ladle's position as it is manipulated by an unseen diner. Initially, it rests within the white bowl; then, it's in mid-air, indicating a motion of being placed down; and finally, it comes to rest on the white paper plate. The motion is deliberate and careful, ensuring the ladle does not contact other items on the table. Throughout this sequence, the rest of the setting remains static, highlighting the singular action of the ladle being moved after a meal. This action is part of the post-meal cleanup process, as the utensil is being set aside, possibly in preparation for washing.

#### Sample 243 — Transition

- Similarity: 0.4786
- Prediction: The sequence of frames captures the progression of a person's action on the paper. Initially, the paper is essentially resting on a table, with its edges exposed. As the frames progress, the person'
- Reference: Over the sequence of images, the baking paper transitions from a state of disarray to a more structured form. Initially, it is spread out with edges protruding in different directions, reflecting the beginning of the folding process. As we progress, the hands become more involved, delicately manipulating the paper into a sharper fold, which is indicative of a step-by-step approach. By the final frame, the paper has taken on a more defined and functional shape, likely in preparation for use in baking or cooking, with the focus on making the paper fit a specific dimension or purpose. The continuity of the environment and the items on the counter suggest that this activity is part of a broader cooking or preparation task within a domestic kitchen.

#### Sample 251 — Transition

- Similarity: 0.4797
- Prediction: The progression of the milk's state from a static state to a flowing state is a clear transition from agitation to re-flow. Initially, the milk is agitated, with the nozzle pointing downward, indicating a gradual flow of milk. As the milk settles into its resting position, the resulting stream of milk becomes more pronounced, with a more rounded and rounded shape. The milk'
- Reference: The transition of the water from the first frame to the last captures a journey from stillness to dynamic action. Initially resting calmly within its vessel, the water is undisturbed and contained. As it begins its transition, it is poured onto the appliance's surface, spreading unevenly and pooling in certain areas, showcasing the fluidity and adaptability of water to its container. In the final frame, the water is actively being poured, its smooth stream disrupted upon contact with the hot appliance, demonstrating the transformative energy that occurs when water interacts with varying temperatures and surfaces. This progression not only illustrates the inherent properties of water but also its behavior under different conditions and manipulations.

#### Sample 253 — Transition

- Similarity: 0.3240
- Prediction: The sponge undergoes a visible transformation from a state of wilting to a fully saturated state. Initially, it is a bare, bare-kneaded vessel, exhibiting a prominent blotchy appearance. As the frames progress, the sponge becomes more fully saturated, indicating a more active and re-distributing action. By the final frame, the blotting action is complete, with the sponge forming a smooth, sprinkling mass, demonstrating a deeper and more concentrated action. The sequence captures the progression of a sponge's state of being fully saturated and able to hold its shape, forming an oiled state, a
- Reference: Throughout the three frames, there's a notable progression in the rag's movement and use. Initially, it's captured mid-motion, actively cleaning, with its wetness prominently displayed. As we progress, the rag's details become more pronounced, hinting at the varying pressure and angles it's being used at. By the third frame, the rag's positioning and the hand's grip indicate a potential shift in cleaning direction or a momentary pause, yet the purpose - cleaning - remains evident. The consistent moisture level across the frames underscores its primary role in this setting.

#### Sample 267 — Transition

- Similarity: 0.4672
- Prediction: The progression of the onion's peeling progresses from a partially untouched state to a fully-engaged position. Initially, the onion is untouched, with no visible signs of the peel. As the frames progress, the peeling begins to become more pronounced, with the onion firmly inserted into the skin. The hand's movements are evident, with their hands positioned in a slender position, indicating the action of the knife. The gradual movement of the blades, ranging from slicing to squeezing, is indicative of the action's graduality, resulting in securing the onion. The progression is marked by the gradual emergence of the rind, with its tangy, tanginess indicating that the onion has been fully sliced.
- Reference: The sequence of frames captures the gradual unveiling of the sweetcorn, beginning with its concealed state within a sealed can and transitioning towards its exposure as an ingredient ready for use. Initially, the can sits dormant, the sweetcorn hidden from view, its potential as a pizza topping only implied. The narrative then shifts as the can opener engages, piercing the metal lid and commencing its journey around the rim, revealing more of the sweetcorn with each twist. By the final frame, the transformation is nearly complete, with the sweetcorn almost fully exposed, transitioning from a contained food product to an active participant in the cooking process, its golden kernels ready to join the array of pizza toppings.

#### Sample 271 — Transition

- Similarity: 0.4167
- Prediction: Over the progression of these three frames, the ice tray undergoes a clear transition from being a static state to being agitated. Initially, it is in a state of rest, with no visible signs of activity. As the frames progress, the person's movements become more deliberate, indicating that the icing has been removed. By the final frame, the action is complete, with the chopping action indicating the completion of the action. The consistent, consistent, and consistent movement of the utensils, the consistent movement in the holder, and the consistent motion of the hand are indicative of the activity of the dishwasher.
- Reference: The progression of the washing up liquid from Frame 1 to Frame 3 showcases a transition from a single, undisturbed streak to a disturbed, bubbly pool. Initially, the liquid is laid down gently, creating a sleek trail. As more pressure is applied to the bottle, the liquid's volume increases, and the force of the liquid hitting the pooled water creates ripples and splashes. By the third frame, the liquid has started to merge with the water, creating a diluted mixture ready for washing up, evidenced by the expanding reach of the liquid and the formation of bubbles. The liquid's viscosity becomes more apparent as it interacts with the water, altering its pristine initial state into a functional soapy solution.

#### Sample 278 — Transition

- Similarity: 0.3677
- Prediction: The progression of the dough's state across these frames shows a clear progression in the preparation process. Initially, it is a state of adolent, with no visible signs of forming. As the frames progress, the dough is progressively rolled out, with the rolling agent firmly embedded in the dough. The rolling agent's movements are evident, with a smooth surface and a uniform distribution of the rolling agents, indicating that the dough has been prepared. The dough'
- Reference: Over the progression of these three frames, the cling film evolves from being mostly contained within its box to being widely spread out and manipulated by the user. Initially, only a small portion is visible, displaying minor wrinkles. As the frames advance, the film is extended more and more, showing an increase in creases and overlaps, likely due to the force of extraction and the manual handling. This transition underscores the film's flexible nature and its responsiveness to human touch and movement.

#### Sample 281 — Transition

- Similarity: 0.4981
- Prediction: Over the progression of these frames, there's a noticeable progression in the state of the table. Initially, it's in a state of disarray, with no visible signs of a spill or spill. As the frames progress, the table is progressively rearranged, with the hand indicating the action of cleaning. By the final frame, the hand is demonstrating the action, with a visible sign of the cleaning action. The table's state of cleanliness is evident throughout the sequence, with its surface exhibiting a clearer and cleaner appearance.
- Reference: From the initial application of the detergent in a fine mist, there is a transition to spreading and then actively wiping the liquid across the surface. The droplets first seen are no longer distinguishable as individual particles but have merged into streaks and then into a more homogenous layer of moisture. The cleaning action evolves from a gentle application to a more forceful movement, indicating a progression from the distribution of the cleaning agent to the actual cleaning process, with the aim of leaving the surface clean and streak-free. The change in the cloth's appearance, from being relatively dry to becoming damp and heavy with detergent, marks the stages of cleaning.

#### Sample 286 — Transition

- Similarity: 0.4628
- Prediction: Over the course of these frames, the rice undergoes a noticeable transformation from a state of being a biting and separating to a more pronounced, blending state. Initially, the sauce is a little biting, with the ingredients forming a uniform, clumping texture. As the stirring progresses, the ingredients begin to blend together, forming an even, layered texture. By the final frame, the dish is firmly incorporated into the pot, indicating that the rice has been thoroughly stirred and is ready to be served. The consistency of the sauce, as well as the consistency of its contents, is indicative of a smoother texture and a deeper flavor profile.
- Reference: As the mixture transitions from the white bowl to the pan, there's a visible change in its state. Initially, it's just being introduced to the heat, with the vegetables looking firm and just starting to cook in the oil. Progressing through the frames, there's a slight softening of the ingredients, especially noticeable in the tomatoes. The cook is actively spreading and stirring the mixture, promoting even cooking. The vegetables maintain their vibrancy throughout, which is indicative of a controlled cooking process that hasn't yet reached the stage of caramelization or significant softening that would come with prolonged heat exposure.

#### Sample 289 — Transition

- Similarity: 0.4712
- Prediction: The progression of the tin's rinsing progresses from a partially submerged state to a fully rubbed state. Initially, the risins are positioned in a position that allows the water to reach the bottom of the teacup, indicating a thorough rinse. As the frames progress, the water level is reduced, demonstrating a more thorough rinse, ensuring that the tea cup is rinsed thoroughly. By the final frame, the teapot is positioned with its lid closed, allowing the water and soap to reach into the tea bowl. The transition from ribbing to r
- Reference: Over the course of these frames, the tupperware transitions from being in the initial stages of rinsing, where the focus is on removing the bulk of the soap suds and debris, to the concluding phase, where the water rinses off the final traces of soap. The changes are subtle but evident, with the initial vigorous bubbling giving way to a calmer water flow, and the handgrip and container orientation shifting to ensure that all interior surfaces have been addressed. The progressive stages reflect a methodical and efficient cleaning process, moving from ensuring coverage to finalizing the rinse.

#### Sample 294 — Transition

- Similarity: 0.4239
- Prediction: Over the course of these three frames, the cooker undergoes a noticeable transformation from a state of wilting to a fully oiled state. Initially, the stove is in a relatively active state, with the surface of the pan being exposed to the cleaning agent. As the frames progress, the cleaning process becomes more intensive, with a more concentrated focus on the surface and the cleaning action. By the final frame, the cooking process is becoming more streamlined, with more and more of the surface being wiped away. The consistent cleanliness of the stove, the consistent use of soap and the consistent presence of the cleaning agents, are indicative of a thorough cleaning process.
- Reference: The progression of the towel's state indicates a series of cleaning actions. Initially presented as a recently used but still serviceable item, it then becomes absent from view, presumably set aside for a moment where the cleaning focus shifts to another object. Upon its return, the towel is employed with more intent and vigor, now visibly dirtier, having absorbed more residues from the cleaning surface. This evolution illustrates a typical cleaning process, where a towel is used, evaluated, and reused with increasing intensity until the task is complete or the towel requires laundering.

#### Sample 297 — Transition

- Similarity: 0.4243
- Prediction: The progression of the chicken's transformation from a whole to a minced one reveals a clear progression in the preparation process. Initially, the chicken is essentially intact, with no visible signs of cooking. As the frames progress, the hands are engaged in the process, demonstrating the skillful handling of the meat. The hand's movements, from the initial slicing motion to the final cut, are indicative of the methodical handling of a meal. The consistent movement of the hands, from cutting to the cutting, is indicative of preparing the chicken for cooking.
- Reference: The progression of these frames shows the process of preparing and cooking garlic. Initially, we see the clove intact, indicating the starting point of the culinary action. As we move to the next frame, the garlic has been crushed into a paste, reflecting the transformation from raw ingredient to a form that can be easily mixed with other components of the dish. Finally, the garlic is transferred into the pan, completing its journey from a solid clove to a cooking element that will infuse the dish with flavor. The careful manipulation of the knife and board by the cook's hands underscores the attention to detail and the methodical approach to incorporating the garlic into the meal.

#### Sample 298 — Transition

- Similarity: 0.4524
- Prediction: Over the course of these three frames, the pan undergoes a noticeable transformation from a state of rest to a process of cleaning. Initially, it is a bit damp, with no visible or visible residue. As the frames progress, the water level is less than ideal, with the pan indicating a more active cleaning process. By the final frame, the spout is positioned in a position that is agitated, indicating that the water has been drained out, resulting in fewer and less soiled areas. The pan's transition from being a resting state to
- Reference: The sequence of images captures the progressive movement of a pair of yellow rubber gloves engaged in kitchen tasks. Initially, the left glove is seen gripping a white bowl, suggesting the commencement of a washing or cleaning action. Moving to the second image, both hands are occupied, with one hand stabilizing a pot and the other in motion, indicative of a multitasking scenario. By the third frame, there's a distinct change, as the gloves are now repositioned to handle a frying pan, suggesting the completion of one task and the beginning of another. Throughout the sequence, the gloves remain taut and appear well-fitted to the user's hands, their bright yellow color standing out against the backdrop of kitchen utensils and appliances. The gloves’ texture and sheen alter slightly with the changing angles and actions, reflecting their flexible and water-resistant nature.

#### Sample 304 — Transition

- Similarity: 0.4071
- Prediction: The sequence of frames captures a clear progression in the washing of the tupperware. Initially, the utensils are in a state of disarray, with no visible signs of food or water. As the frames progress, the hands are engaged in sweeping the trays, indicating a thorough cleaning. By the final frame, the hand is able to remove the wares, demonstrating a meticulous cleaning process. The consistent movement of the hands, the shifting motions of the hand, and the constant movement of their movements are indicative of a
- Reference: The tin's journey through these frames is a visual narrative of restoration. Initially, it stands as a testament to its robust utility, bearing the marks of many uses. As water is introduced, it takes on a dynamic role, actively engaging with the tin to begin a transformation. The water's force is evident in the way it interacts with the seasoned surface, and finally, the tin sits with water pooled within, a temporary reservoir that hints at the potential for renewal. This progression is not just physical but symbolic, echoing the cycle of use, wear, and rejuvenation inherent in the life of a well-loved kitchen implement.

#### Sample 305 — Transition

- Similarity: 0.3591
- Prediction: Over the course of these frames, the chili undergoes a noticeable transformation from a state of being gathered and discarded to a more pronounced release. Initially, the chilli is positioned in a position that indicates the presence of the chili, indicating the presence or absence of the chillis. As the frames progress, the lid is removed, revealing the chili's contents, implying the presence
- Reference: As the sequence progresses, there is a clear transition from a static, somewhat disordered countertop to one that is the focus of active tidying. Initially, the countertop appears merely wiped down with residual moisture, then transitions to a state of active cleaning with the person's hands and sponge in motion. By the third frame, the cleanliness is maintained despite the ongoing meal preparation, showcasing the individual's diligence in keeping the space orderly. The consistent presence of the person's hands and the movement of the sponge indicate a methodical cleaning process, maintaining order amidst the culinary activity.

#### Sample 308 — Transition

- Similarity: 0.3856
- Prediction: The progression of the rinsing of the colander continues to highlight the methodical handling of the dish. Initially, the coulis is positioned in a position that is angled to ensure the water's flow. As the frames progress, the water flows downwards, indicating that the cowel is being rinsed. By the final frame, the angled position is a step forward, demonstrating the effective handling of ripping the co
- Reference: The progression of cleaning the baking tray is quite evident across the three frames. Initially, the tray was being rinsed, with the water pressure aimed at dislodging the large particles and debris. Moving on, it was tilted to facilitate the removal of these particles, allowing a more targeted rinse. Finally, the application of soap and active scrubbing suggests a meticulous cleaning process is underway. Throughout these stages, the tray transitions from heavily soiled to being covered in soap suds, which marks the midway point of the washing cycle, leading towards a fully cleaned state. The person's consistent handling and methodical cleaning process indicate an effective and routine approach to dishwashing.

#### Sample 309 — Transition

- Similarity: 0.3635
- Prediction: The progression of the chicken's transformation from a partially steamed state to a fully sanitized state is evident across the three frames. Initially, the chicken is essentially in a state of rest, with its skin still exposed. As the frames progress, the hands are engaged in removing any remaining dirt or debris, indicating that the chicken has been thoroughly rinsed. By the final frame, the hand is demonstrating a more thorough cleaning, highlighting the process of removing the chicken from its state of being fully soaked and ready for use. The consistent movement of the hands, a sign of the thoroughness of the cleaning process, suggests that the method is a
- Reference: Over the course of these frames, the tap undergoes a clear transition in its functionality. Initially, it's in a dormant state with no water flow. However, as time progresses, water begins to stream out, and by the third frame, the intensity of this flow has increased substantially. This progression indicates the tap being turned on and adjusted to release water at a faster rate. The entire scene captures the tap's transition from a static state to one of full operation, showcasing the simple yet essential function of such a household fixture.

#### Sample 320 — Transition

- Similarity: 0.2549
- Prediction: The progression of the chicken's transformation from a fully seasoned meat to a partially seasoned, charred meat is evident across the three frames. Initially, the chicken is positioned in a position that is primarily a frying pan, with the meat positioned on the side of the pan. As the frames progress, the meat is progressively removed from the pan, indicating that the meat has been fully cooked. The hand's motions are indicative of the meat's preparation, with a steady hand motion indicating the final action. The chicken'
- Reference: Over the course of these frames, the sweet potato skin transitions from freshly cut to completely separated. Initially, the skin is freshly peeled, with vibrant colors and moisture that highlight its recent contact with the flesh. As the peeling continues, more of the flesh is exposed, and the skin's texture and color change slightly due to air exposure. In the final frame, there is a substantial amount of peel removed, evidencing the work done, and the skin that remains on the sweet potato shows signs of drying out. The process reflects a meticulous peeling technique aimed at preserving as much of the sweet potato flesh as possible while removing the skin.
Frame_1:
The skin of the sweet potato is mid-peel, with a segment hanging off the edge of the vegetable, poised to be removed. It exhibits a rich, deep orange hue indicative of its freshness and nutritional content. The texture of the recently cut skin appears slightly moist and shiny, contrasting with the dry, matte outer surface. The peeling action has produced a few errant strands of skin that have curled away from the starchy interior, creating a small pile on the edge of the cutting board, which is speckled with moisture and small flecks of the sweet potato flesh.

Frame_2:
The sweet potato now reveals more of its vibrant orange flesh as the skin has been further peeled back. The skin itself is thinner and more fragmented than before, indicative of the peeling process becoming more refined as it progresses. Pieces of the skin are now strewn across the cutting board in a more dispersed pattern, and some have fallen to the stovetop, suggesting a rapid peeling motion. The knife, still held firmly, continues to work closely against the flesh, ensuring minimal wastage of the vegetable, while the brightness of the skin has begun to wane as it dries out.

Frame_3:
Here, the sweet potato skin has been almost entirely removed, with only a small portion left at the tip. The collection of peeled skin has grown substantially, covering a significant area of the cutting board. The skin's color has dulled slightly, losing some of its initial vibrancy as it succumbs to the air's oxidizing effects. The knife and fork are now at rest beside the pile of peelings, and the skin's moisture has visibly reduced, appearing drier and starting to curl at the edges.

State_change_caption:
Observing the state of the sweet potato skin across these frames shows a clear progression in the peeling process. The initial frame displays a just-begun peel with a skin rich in color and moisture. Moving to the next, there is a noticeable increase in the quantity of skin removed, with evidence of technique refinement and speed. By the final frame, the skin has mostly been stripped away, leaving behind a more extensive and drier collection of peelings. The transformation is marked by a gradual loss of moisture and color in the skin, as well as a shift from a few large pieces to many smaller, drier fragments.

#### Sample 325 — Transition

- Similarity: 0.4872
- Prediction: The progression of the slicing process takes place across the three frames. Initially, the sliced sprigs are untouched, with no visible skin. As the frames progress, the hands are engaged in the process, ensuring that the resulting pieces are uniformly sliced. By the final frame, the process is complete, with the ripe spirules and the rinds being removed. The methodical nature of the cutting process is evident, with each frame highlighting a different action, demonstrating the precise and precise preparation of the cut.
- Reference: The kiwi undergoes a visible transition across the three frames, from an almost whole fruit with minimal peeling to a fully prepared, edible state. Initially, it exhibits a moist surface with a partially retracted skin, then progresses to a state of further peeling, exposing more of its succulent green interior. Finally, the kiwi is transformed into a collection of bite-sized pieces, neatly cubed and separated from the now largely discarded skin. The methodical process reflects a careful effort to maximize the fruit's yield while minimizing waste.

#### Sample 327 — Transition

- Similarity: 0.4967
- Prediction: Over the progression of these three frames, the trash can undergoes a dynamic change in its state. Initially, it is a state of rest, with no visible obstructions. As the frames progress, the person's hand moves closer to the trashcan, indicating that the person is removing the trash. The person'
- Reference: The sequence depicts a clear progression of the lunch box's state: starting from rest, transitioning through a rapid motion, and finally, the act of being purposefully tipped over by a person. Initially, the box is at rest, secure and undisturbed on the kitchen counter. Then, it enters a state of motion, captured as a blur, signifying a swift change from stillness to movement. Lastly, the hands that appear to be tilting the box reveal the intent behind the motion, showcasing the transition from inanimate placement to human interaction. The entire sequence captures the lunch box's journey from static repose to dynamic action, underscored by the visible human agency.

#### Sample 328 — Transition

- Similarity: 0.4137
- Prediction: Over the course of these three frames, the bag undergoes a clear transition from being partially closed to being fully opened. Initially, the person's hand is hesitant, indicating that the bag is being opened. As the frames progress, the hand's movements become more deliberate, implying that the person is attempting to open the bag. By the final frame, the hands are engaged in a deliberate, deliberate action, demonstrating the action's impact on the bag's contents. The progression of the bag reflects the changing state of the person, a shift in the direction of the action, with the bag becoming more open and revealing its contents.
- Reference: The sequence captures a simple yet ubiquitous kitchen ritual: the toasting of a slice of bread. Initially presented in hand, the bread slice is a static object, yet full of potential. As it is inserted into the toaster, there is a transition from potential to process—the bread begins its transformation. The final frame culminates in the bread's disappearance inside the toaster, a visual cue that the physical state of the bread is changing from soft to toasted, even though the process is hidden from view. This sequence is a snapshot of everyday life, a familiar action paused in time and broken down into the individual steps that lead to the satisfying crunch of a freshly toasted slice of bread.

#### Sample 335 — Transition

- Similarity: 0.3073
- Prediction: The sequence of frames captures a clear progression in the state of the mat. Initially, it is a state of rest, with the mat being positioned in a position that indicates the presence of a person or object. As the frames progress, the mat is positioned, with its surface positioned and positioned at a level that indicates a repositioning of the surface. By the final frame, the person is demonstrating the action of removing the mat, indicating the action is complete. The hand's movements are evident throughout the sequence, with a consistent hand motion, demonstrating a deliberate action to remove the mat from its position. The transition from the initial state of repost to the subsequent state of re-positioning is reminiscent of sweeping the mat to a more resolute position, implying a shift in the direction of the action.
- Reference: Over the course of these frames, the degreaser transitions from a freshly sprayed mist to a settled layer of cleaning agent on the countertop. Initially, the liquid is airborne, caught in the act of being dispensed. As the spray continues, the droplets begin to fall and spread across the surface, moving from a state of suspension to contact. By the final frame, the spray action has stopped, and the degreaser has formed an even layer across the countertop, indicating the completion of the application phase and the beginning of its cleaning action. The progression shows an effective dispersion method, covering the targeted area thoroughly with the cleaning agent.

#### Sample 336 — Transition

- Similarity: 0.4920
- Prediction: Throughout the sequence, the coffee maker undergoes a meticulous process of rinsing. Initially, the water is filtered out, with the coffee filter positioned in a position that allows the water to reach the bottom of the coffeemaker. As the frames progress, the cup is positioned, ensuring that the water flows through the filter and into the coffee grounds. The hand's movements, ranging from a gentle hand to a more vigorous hand, are evident throughout the process, demonstrating the thoroughness of the cleaning process. The consistent flow of water, the consistent water flow, and the consistent hand'
- Reference: Over the course of the three frames, there is a clear progression in the state of the cutlery from being soapy to becoming increasingly rinsed. The transition from the initial fork with noticeable soap suds to the knife, which shows a focused rinse down the blade, to another fork with reduced suds illustrates a methodical process of cleaning kitchen utensils. The consistent flow of water and the changing angles at which the cutlery is held under the faucet reflect an attentive approach to ensure that all remnants of soap and debris are removed from the items being washed.

#### Sample 338 — Transition

- Similarity: 0.4030
- Prediction: Over the course of these frames, the meat undergoes a noticeable transformation from a state of rest to a cooking process. Initially, it is a smoky, greasy, and a bit charred, but as it is being stirred, it becomes more brittle and brimmed with flavor. As the final frame progresses, the cooking process becomes more fluid, with the meat separating from the pan, indicating a more gradual cooking process, with a less-pronounced charring. The transition from sloshing to frying is reminiscent of a slow cooker, with its cooking stages indicating the final stages of cooking.
- Reference: Throughout the sequence of images, the extractor fan exhibits a static condition with no observable changes in its state. It is characterized by a persistent layer of grease that covers the entirety of its visible surface, displaying a gradient of discoloration indicative of long-term exposure to cooking fumes and heat. The fan's unchanged condition across the frames implies that it has not been activated, cleaned, or altered in any way during the short timespan depicted in the series of images. This continuity reflects a consistent environment where the fan is subjected to the same kitchen activities without any intervening maintenance.
Frame_1:
The extractor fan exhibits a heavy accumulation of residue, predominantly in the center, which hints at a prolonged absence of deep cleaning. The grease spots are not uniform, with some areas denser and darker, suggesting repeated exposure to steam and smoke, possibly from high-heat cooking. The fan appears to be static, as the surrounding air and surfaces are clear, showing no signs of steam or smoke being actively drawn in. The lighting in the kitchen casts a soft glow on the tiles, but the fan's surface seems to absorb rather than reflect light, underscoring the thickness of the grime covering it.

Frame_2:
Continuing from the previous state, the extractor fan's condition remains unchanged, with the same pattern of grease and dirt. The distribution of grime appears uninterrupted across the fan's surface, indicating that no cleaning or usage has occurred between this frame and the previous one. The kitchen's lighting conditions remain consistent, and the fan continues to show no sign of operation, with no visible vibration or motion to suggest it is active. The environment suggests that the fan has been dormant, and the buildup on its surface has been left untouched.

Frame_3:
As before, the fan shows no signs of recent activity or cleaning. The layer of grease remains as thick and undisturbed as in the earlier frames, with no fresh streaks or smudges that would indicate recent wiping. There's a continuity in the kitchen's atmosphere, with the same lighting conditions and no additional movement or steam, reinforcing the extractor's non-operational state. The fan seems to have become a static fixture, with its condition reflective of a consistent lack of attention to cleanliness or use.

State_change_caption:
Across the three frames, there is a conspicuous absence of any change in the state of the extractor fan. It remains consistently coated with a layer of grime that suggests significant elapsed time since its last cleaning. The fan shows no signs of recent operation, as there is no disturbance in the grease pattern that would indicate movement or airflow. The consistent lighting and lack of motion blur in and around the fan's environment further support the conclusion that it has not been turned on or interacted with during the time lapse these frames represent. The extractor's state is indicative of neglect both in terms of cleaning and in terms of usage, as it seemingly remains an inactive appliance amidst the kitchen's activities.

#### Sample 341 — Transition

- Similarity: 0.3521
- Prediction: The progression of the chopping board across these frames shows a clear progression in the rinsing process. Initially, the board is being rinsed, with the water running through the board. As the frames progress, the water's flow becomes more concentrated, with a more concentrated stream of water scrubbing the board, indicating a thorough cleaning. By the final frame, the squeegee's movements are streamlined, with water flowing through the boards, ensuring that the board's surface is clean and ready for the next rinse. The consistent movement of the board across the frames suggests a methodical approach to the blendeding process, with each frame indicating different steps.
- Reference: The tablecloth transitions from a static, artistically displayed kitchen item to an object in the midst of washing. Initially laid out with a prominent apple design, it is subjected to a cascade of water, which introduces a new texture and sheen, altering its appearance and form. As the cleaning progresses, the tablecloth takes on a more functional role, its aesthetic momentarily set aside for practicality. The water's impact is evident in the evolving state of the fabric, from dry and smooth to wet and contoured, highlighting the cloth's transition through the stages of cleaning.

#### Sample 348 — Transition

- Similarity: 0.4496
- Prediction: Over the progression of these three frames, the refrigerator undergoes a clear transition from being partially open to fully open. Initially, the fridge is partially closed, with the hand indicating that the door is open. As the frames progress, the hand's movements become more deliberate, revealing the contents of the fridge. By the final frame, the person's actions become more intentional, indicating the action of opening the fridge door. The consistent state of the refrigerator's contents, the consistent hand'
- Reference: Across the sequence, the spice jar undergoes a transition from being a blur in motion, possibly being moved or selected, to being the object of focus with a hand reaching towards it in the final frame. The state change of the spice indicates interaction, possibly the process of selection for use in cooking. The motion from one frame to the next suggests the dynamic environment of a kitchen in use, where ingredients are actively being handled. The clear progression from blur to focus conveys the steps taken in preparing to use the spice, demonstrating a moment in the culinary preparation process.
Frame_1:  
The image captures a moment of rapid movement, evidenced by the significant blur across the scene. Amidst the swift motion, a spice jar appears to be the subject of the action, though its details are obscured due to the speed of the movement. The surroundings are a flurry of colors and shapes, with hints of other stationary items in the background that contrast with the jar’s velocity. The positioning suggests that the spice jar is either being quickly picked up or put down, but the exact nature of the herb or spice inside the jar is indistinguishable in this dynamic state.

Frame_2:  
Here, a kitchen cabinet is open, showing an organized collection of spice jars and packets inside. The spice in question seems to be at rest, nestled among its counterparts in a well-maintained culinary arsenal. The contents of the jars are varied, with different hues indicating a range of spices. The hand captured in the frame is moving, blurring the detail and suggesting the ongoing action of selecting or rearranging the jars. This moment is static for the spices, yet indicative of an imminent change as the hand moves amongst them.

Frame_3:  
In this clear and steady frame, the focus is on the interaction between the hand and the spice jars. One particular jar is being targeted, and the hand is caught in the act of grasping it. The spice jar and the hand are both in sharp focus, with the details of the jar label and the person's skin texture visible. The other jars remain stationary, creating a backdrop for the main action. The intention to use or move this specific spice is evident, with the hand's positioning suggesting a gentle yet firm grip.

State_change_caption:  
The progression of these frames depicts the dynamic state of a spice jar being manipulated in a kitchen setting. Initially, the jar is a blur, suggesting rapid movement as part of the selection or cooking process. As the sequence advances, the environment stabilizes, and the spice jars come to rest, allowing for a clear view of the orderly storage. The final state of motion is focused and deliberate, with a hand selecting a specific jar, likely for culinary use. This evolution from a rapid blur to a targeted selection captures the essence of kitchen activity, where ingredients are in constant flux until needed, at which point they are handled with precision and intent.

#### Sample 351 — Transition

- Similarity: 0.4823
- Prediction: The sequence of frames captures a clear progression in the state of the bag. Initially, the bag is untouched, with no visible signs of use. As the frames progress, the person's hands move more slowly, indicating that the bag has been accessed. By the final frame, the hand's movements are evident, with the bag firmly anchored in the bag, demonstrating the action of removing the bag from its packaging. The progression of the bags' state is a subtle reminder of the process of preparing for a meal or to prepare for preparing to eat
- Reference: Over the course of the three frames, the olive oil bottle undergoes a transition from being open to being sealed. Initially, the cap is resting independently on the stovetop, separated from the bottle. Moving to the second frame, the cap is picked up and aligned with the bottle for recapping. By the third frame, the action is nearly complete, with the cap being twisted onto the bottle to form an airtight seal. This sequence captures a common yet precise task, requiring fine motor skills to ensure the cap is correctly threaded and the contents of the bottle are preserved. The process is a small but integral part of kitchen activities, reflecting both the use and storage aspects of cooking ingredients.

#### Sample 355 — Transition

- Similarity: 0.4294
- Prediction: The progression of the pak cho
- Reference: The pak choi leaf undergoes a clear transformation across the three frames. Initially whole and just touched by the knife, it is then seen mid-slice with the knife cutting through its fibrous stem and delicate leaf. By the final frame, the leaf is transformed into neatly cut sections. The process reflects a careful and purposeful effort to prepare the pak choi for cooking, maintaining the integrity of the leafy greens while creating bite-sized pieces suitable for a dish. The slicing is methodical, maintaining the freshness and structure of the pak choi throughout the process.

#### Sample 358 — Transition

- Similarity: 0.4600
- Prediction: Over the course of these three frames, the hoboscope undergoes a noticeable transformation from a state of disarray to a more active and re-energized state. Initially, the hawaii is in a position where it is positioned in sweeping motions, with the spout pointing downwards, indicating a gradual shift in the direction of the sweeping movement. As the frames progress, the person's movements are progressively shifted to the right, implying a shift in direction. The consistent movement of the ho
- Reference: Over the progression of these frames, the hob remains remarkably unchanged, indicating a state of cleanliness and non-use before and during the wiping process. The hand, methodically moving the cloth over the hob's surface, suggests a routine cleaning rather than a response to a recent cooking session. The consistency of the control knobs' positions throughout the frames confirms that the hob has not been used during this sequence. The main alteration is the movement of the cleaning cloth, which traces a path across the hob, likely picking up any unseen particles or smudges, ensuring the surface remains spotless.

#### Sample 359 — Transition

- Similarity: 0.2842
- Prediction: The cloth transitions from a state of being partially saturated and rinsing to a more concentrated state of wringing and scrubbing. Initially, the cloth is a bit
- Reference: Analyzing the bin across the three frames, its state remains consistently full, with the contents reaching above its rim throughout. There is a subtle implication of additional waste being added, as indicated by the human interaction in frames two and three. However, there is no significant visible change to the volume of waste in the bin, suggesting that if something was added, it was small. The environment around the bin stays static, with no observable adjustments to the items on the countertop or within the dish rack. The plastic liner shows a slight bulge in the last frame, which might be a result of the bin being further filled or simply from the movement of the bag as waste was added.

#### Sample 361 — Transition

- Similarity: 0.4555
- Prediction: The progression of the bacon's packaging reveals a clear progression in the preparation of its preparation. Initially, the bacon is fully sliced, with the skin exposed. As the frames progress, the person's hand begins to remove the bacon, revealing a more pristine and pristine state. The hands' movements are evident, with their hands demonstrating the process of removing the bacon. The process of the sliced bacon is a subtle transition from being fully shredded to being partially sliced. The progression from being a partially shredded bacon to being fully
- Reference: The sequence of images captures a moment-by-moment transformation of the red pepper from its packaged state to being prepped for cooking. Initially, the pepper sits undisturbed, secure in its plastic wrap with other colorful companions. As the moments pass, human interaction introduces change; the hand selects the red pepper, repositions it, and the knife is poised to cut. Finally, the knife slices through the plastic, an act that converts the pepper from a packaged good to a ready-to-use ingredient. This progression not only depicts the physical state change of the pepper but also the methodical approach taken to prepare it for inclusion in a meal.

#### Sample 362 — Transition

- Similarity: 0.4696
- Prediction: Over the course of these frames, the cloth undergoes a noticeable transformation from a partially soaked and dripping state to a fully soaked state. Initially, the fabric is firmly wrung out, with the water drained out, indicating a gradual wringing process. As the frames progress, the water's texture becomes more pronounced, with a more brittle appearance and a less pronounced odor. By the final frame, the wick's state is more streamlined, with its water content progressively decreasing, demonstrating a reversing process
- Reference: The transition of the tap's state across these frames illustrates a gradual reduction of water flow, which is controlled by the manipulation of the tap's handle. Initially, the water gushes out in a steady stream, a clear sign of the tap being fully opened. As the sequence progresses, human intervention is evidenced by the hands moving closer to the tap, culminating in the final frame where the flow has been significantly decreased. This progression indicates a deliberate action to conserve water or to conclude a task that required its use, reflecting an everyday conservation effort or the completion of a utilitarian activity.
Frame_1:
The water tap is captured in mid-use, with water flowing out at a steady rate. The tap, likely made of stainless steel, is turned to a position indicative of an open valve, allowing a substantial amount of water to pour out. The stream is forceful and abundant, causing a splash against the base of the sink, where a pool of water is already forming. The person’s hands are positioned beneath the flowing water, suggesting either the rinsing of objects or perhaps the washing of hands. Light reflects off the wet surfaces, creating a sense of movement and activity.

Frame_2:
In this instance, the water tap continues to be in the open position, but the hands are now grasping it, preparing to make an adjustment. The water flow remains consistent and plentiful, cascading into the sink with vigor. The hands are poised in a manner that indicates imminent action towards the tap, with thumbs pressing against one side, likely applying pressure to begin the process of turning it off. The surrounding items in the sink remain static, providing a contrast to the dynamic action centered around the tap.

Frame_3:
The tap has now been nearly closed, evidenced by the significantly reduced flow of water. The stream has dwindled to a thin, gentle pour, a stark contrast to the robust flow seen previously. The hands have turned the tap to nearly the off position, with only a slight opening allowing a small amount of water to escape. The action of turning off the water is almost complete, and the reduced flow indicates a near stop to the water output. The surrounding area in the sink is less disturbed by the water, as the force and volume have decreased.

State_change_caption:
Across the sequence of these frames, there is a clear and deliberate progression from a full flow of water to almost none. The interaction with the tap begins with it fully open, allowing a strong stream of water. As the hands engage with the tap, turning it clockwise, the flow diminishes accordingly. By the last frame, the tap is almost completely turned off, with just a trickle of water left escaping. This sequence captures the concluding action of a routine task, likely the conservation of water after use. The change in flow is smooth and controlled, showing a common daily action of switching off a tap.

#### Sample 364 — Transition

- Similarity: 0.2185
- Prediction: The sequence of frames captures a clear progression in the use of the kitchen sink. Initially, it is positioned in a state of rest, with no visible action. As the frames progress, the sink's position becomes more apparent, with the hand indicating its presence. As it is placed, the hand's movements become more deliberate, indicating the presence of the sink. The hand'
- Reference: Over the span of these frames, the sweet potato undergoes a captivating transformation. Initially, it sits in its whole, untouched state, exuding natural freshness and earthly charm. As we progress, the tuber is carefully dissected, revealing its juicy, vibrant core, and setting the stage for its culinary destiny. By the end, the sweet potato, having been cooked or baked, has transformed into a tantalizing dish, with textures and colors enhanced, promising a delightful taste and aroma to whoever is about to enjoy it. The journey showcases not just a physical change, but a sensory evolution, inviting onlookers to appreciate the culinary art and nature's bounty.

#### Sample 365 — Transition

- Similarity: 0.4159
- Prediction: Over the course of these frames, there's a clear progression in the state of the stovetop. Initially, the stove is in a state of disarray, with no visible signs of cooking or cooking. As the frames progress, the person's hand is progressively moving towards the stove, indicating a more active and thorough cleaning. By the final frame, the surface is a little more bare, with the stove's surface indicating that the stove has been cleaned. The consistent, uniformity of the surface, the consistent movement of the hand, and the consistent motion of the burners, suggest a processional approach to the task of cleaning the stove
- Reference: Throughout the progression of these frames, the state of the hob surface has undergone a significant transformation. Starting with a noticeable amount of spilled substance and moisture, there has been a systematic reduction in the residue and sheen with each frame. The presence and action of the blue cloth have been instrumental in this change. From the initial spotting of the spill to the near completion of the cleaning process, the hob's state has shifted from messy to mostly clean, showcasing the effectiveness of the cleaning effort.

#### Sample 367 — Transition

- Similarity: 0.4185
- Prediction: The progression of the syrup across these frames captures a clear progression in the state of the sugar. Initially, it is a state of disarray, with no clear indication of the presence of the salt. As the frames progress, the syrup becomes more pronounced, with the spoon indicating the presence or absence of the sand. As we move forward, the spoon's motion becomes more deliberate, indicating a gradual movement in the direction of the action. The consistency of the spoon and the hand's movements are indicative of a deliberate action, demonstrating the gradual movement of the shaker.
- Reference: Over the course of the three frames, the cap undergoes subtle changes in its position and visibility. Initially obscured and in the periphery, it gradually moves to a more central position in the viewer's field of vision. The illumination improves slightly across the frames, revealing more of the cap's details. Throughout the progression, the cap seems to be in a state of rest amidst a disorderly setting, but its prominence becomes more pronounced with each successive frame.

#### Sample 368 — Transition

- Similarity: 0.4284
- Prediction: Over the progression of these three frames, the bag undergoes a clear transition from being partially opened to being fully opened. Initially, the person's hand is hesitant, indicating that the bag is being opened. As the frames progress, the hand's movements become more deliberate, demonstrating the action of releasing the bag. By the final frame, the hands are engaged in a deliberate, deliberate action, revealing the contents of the bag, highlighting the action's significance. The person'
- Reference: Over the course of these three frames, the chopped tomatoes transition from being freshly opened in their can to being absent from the visible area, indicating their progression in the cooking process. Initially, the tomatoes are presented in their raw, canned state, ready for use. As the frames advance, the tomatoes themselves are not directly shown, but the surrounding evidence of cooking activity suggests that they have been set aside or added to a dish that's being prepared. The progression of the ingredients from packaged to being part of a meal preparation is subtly indicated by the changing state of the kitchen countertop, from the organized beginning to a more active cooking stage.

#### Sample 371 — Transition

- Similarity: 0.4696
- Prediction: Over the course of these frames, the courgette undergoes a noticeable transformation from a raw state to a cooked one. Initially, they are distinctly fresh and crisp, with no visible signs of cooking or cooking. As they cook, the vegetables become more tender and charred, indicating that they are being cooked to their desired texture. The stirring and stirring are evident, demonstrating the gradual change in the cour
- Reference: The spatula's journey begins with anticipation, held ready above the pan, then it dives into the action, pressing into the chopped vegetables, stirring them around. This motion is purposeful, ensuring an even sauté. Finally, the utensil is lifted, pausing in the air, completing the cycle of cooking action. Throughout these frames, the spatula's role is pivotal in the manipulation of the food, working in harmony with the cook's movements to achieve the culinary goal. The sequence shows a progression from readiness to action to a brief rest, reflecting the rhythm of cooking.

#### Sample 373 — Transition

- Similarity: 0.4230
- Prediction: The sequence of frames captures a clear progression in the state of the cheese. Initially, it is untouched, with no visible signs of use. As the frames progress, the cheese is positioned in a position that indicates a deliberate action, indicating the cheese's presence. As it is placed, the person's movements are evident, demonstrating the action's impact on the cheese, implying a gradual change in the cheese state. The cheese'
- Reference: Starting from an untouched state, the sandwich undergoes a transformation as it is being sliced. Initially, the bread appears whole and uncut, with its contents hidden. As the knife begins its descent, the sandwich's structure is disturbed, revealing a peek of its inside ingredients. By the third frame, the knife has made a significant cut, leading to a clear distinction between the two halves of the sandwich, showcasing the sandwich's interior more prominently. The transition from whole to being sliced captures the meticulous process of preparing the sandwich for consumption.

#### Sample 378 — Transition

- Similarity: 0.4927
- Prediction: Over the course of these frames, the vegetables undergo a clear transformation from a state of rest to a place of cooking. Initially, they are largely uncooked, with no visible signs of cooking or cooking. As the frames progress, they become more tender, with the vegetables progressively removing the skins and forming a more uniform texture. The constant movement of the vegetables suggests a deliberate cooking process, indicating that the cooking process is complete. The consistent movement of ingredients, the constant movement in the pan, and the constant motion of the pan's movement suggest a
- Reference: Over the sequence, the hob's state transitions from active cooking to an implied pause. Initially, the hob is the center of activity with vegetables being sautéed on a lit burner. As the scene moves to the countertop, the focus on the hob is momentarily lost, suggesting a brief intermission in its use, with the user's attention diverted to other preparatory tasks or to the oven. Finally, the user's attention seems entirely redirected from the hob towards the oven, indicating a progression in the cooking process or a multitasking scenario where the hob's contents require less immediate supervision. Throughout these frames, the hob remains in a consistent state of use, with one burner visibly operational.

#### Sample 381 — Transition

- Similarity: 0.4272
- Prediction: The progression of the meatcase's transformation from a fully cooked, unbroken piece of meat to a seasoned, charred piece of food. Initially, the meat is a state of being, with its skin still exposed, indicating that it has been grilled. As the frames progress, the cooking process becomes more deliberate, with the meat progressively separating from the meat, revealing a more seasoned and charring-like texture. The process is reminiscent of a cooking process that involves the preparation of shredded meat, with a focus on the preparation and preparation of the final product.
- Reference: Over the course of these three frames, the seasoning process undergoes a noticeable transformation. Initially, the application is tentative and sparse, with only a few specks of spice evident on the dish. As the frames progress, there's a clear increase in the density and spread of the spice particles, indicating a deliberate and consistent seasoning approach. The hand's movement, paired with the changing distribution of the spice, paints a picture of a methodical and attentive culinary process, ensuring that every portion of the dish receives its fair share of flavor.

#### Sample 391 — Transition

- Similarity: 0.4345
- Prediction: Over the progression of these frames, the tray undergoes a clear transformation from being partially rinsed to being agitated. Initially, the trays are positioned in a position that allows the water to reach the surface, indicating that the water has been drained. As the frames progress, the water is shifted to the side, demonstrating the process of rinsing the tray. By the final frame, the drying process is complete, highlighting the transition from a soiled tray to a clean, rubbed tray. The consistent pattern of the tray's appearance, the consistent use of soap and water, and the consistent movement of the rags indicate a thorough cleaning process.
- Reference: Over the span of these three frames, there's a noticeable progression in the wetness of the chopping board. Starting from scattered droplets in the initial frame, the water coverage intensifies, with the board transitioning from being partially wet to almost fully saturated by the third frame. This indicates that water is continuously being added or spread across the board's surface. The board's color evolves in tandem with this change, deepening in hue as more of its area becomes wet.

#### Sample 392 — Transition

- Similarity: 0.4737
- Prediction: Over the progression of these three frames, the cabinet transitions from being partially open to being fully opened. Initially, the person's hand is a clearer, more discerning observer, indicating that the action is taking place. As the frames progress, the hand's movements become more deliberate, revealing the object's contents. By the final frame, the door is open, demonstrating the action's impact on the cabinet. The person'
- Reference: Throughout the sequence, the tea towel transitions from a loosely placed item in the drawer to one that's actively being manipulated. Initially, it lies casually draped, its vivid stripes providing a pop of color against the wooden backdrop. As the hand intervenes, the fabric gathers and folds, with the direction and intent of the movement becoming more apparent. By the final frame, the tea towel's state reflects the consequences of this interaction—a more crumpled presence, embodying the dynamic nature of household tasks and the temporary disorder that often precedes tidiness.

#### Sample 401 — Transition

- Similarity: 0.2745
- Prediction: Over the progression of these frames, there is a clear progression in the state of the kitchen sink. Initially, it's a state of being partially open, with no visible or visible obstructions. As the frames progress, the person's hand moves closer to the sink, indicating that the sink is now fully open. By the final frame, the sink appears to be fully closed, with the person indicating the sink's closure. The transition from being partially closed to fully open is reminiscent of the process of a kitchen sink being opened, with a person'
- Reference: As the sweeping process progresses through these frames, the floor undergoes a subtle transformation from a state of light disarray to a cleaner condition. Initially, small particles are distributed across the hardwood surface, but as the sweeper moves across the floor, these particles are being gathered, altering the floor's appearance. The sweeping action creates streaks and changes the distribution of light and shadow, making the cleaned areas slightly more reflective. The overall effect is a gradual enhancement of the floor's cleanliness, showcasing the efficacy of the sweeping in progress.
Frame_1:
The floor presents itself with a polished sheen, its wooden planks arranged neatly in a herringbone pattern. The warm brown tones of the wood are complemented by the ambient light, which accentuates the natural grain and subtle imperfections within each plank. Upon closer inspection, fine particles of dust and small debris can be observed settled between the ridges of the wood's texture, hinting at a surface that has been undisturbed for a period. The debris is not pervasive but localized, suggesting light foot traffic or recent activity that has slightly marred the otherwise pristine condition of the floor.

Frame_2:
The condition of the floor in this instance shows evidence of recent interaction with the cleaning tool. The previously noted dust and debris appear to be disturbed, with some particles now adhering to the sweeper's pad, while others are pushed into small, irregular gatherings. The strokes of the sweeper leave behind faint trails on the wooden surface, indicating the direction of the clean-up effort. Despite these changes, the overall ambiance of the room is maintained, with the floor's natural beauty still prominent beneath the transient markings of the cleaning process.

Frame_3:
Further changes in the floor's condition are evident here, with a more uniform appearance emerging as the sweeping action progresses. The gatherings of dust and debris have been further consolidated, making the previously affected areas appear cleaner and more orderly. The sweeper's path is more defined, suggesting a methodical approach to the task. The floor's inherent luster begins to reclaim its dominance as the fine particles are systematically removed, restoring the wood's smooth texture and reflective qualities to the forefront.

State_change_caption:
The transformation of the floor across these frames reveals the dynamic nature of routine cleaning. Initially, the surface is characterized by scattered debris and a latent need for attention. As the sweeper makes its way across the floor, there's a discernible shift from a lightly sullied state to one that is more refined. The motion of the sweeper not only displaces and collects the particulate matter but also seems to rejuvenate the wood's finish. By the final frame, the result of the sweeping is a more homogenized and visually pleasing surface, indicative of the cleaning process's effectiveness in restoring order and sheen to the floor.

#### Sample 403 — Transition

- Similarity: 0.4452
- Prediction: The progression of the bacon's state is a clear transition from a fully untouched state to a more fully incorporated state. Initially, the bacon is untouched, with no visible signs of a physical or chemical damage. As the frames progress, the knife's movements become more deliberate, indicating that the bacon has been sliced and is being sliced. The hand's motions are a subtle reminder of the process, demonstrating the gradual movement of the knife, a process that is characterized by a smoother, more pronounced cut. The consistent movement of both hands, reflected in the crispness of the slices, suggests a deliberate and deliberate action, resulting in a crisp, slicing-like texture.
- Reference: Over the course of these three frames, the onion undergoes a transition from being a stand-alone prepared ingredient to becoming an integral component of a more complex dish. Initially, it's presented in its sliced form, clearly showcased on a plate. As the scenes progress, the onion becomes a part of a layered culinary creation, suggesting an evolving recipe. By the third frame, the onion, while still recognizable, is now harmoniously combined with other ingredients, ready for the next steps in the cooking process. This progression highlights the versatility of the onion and its role in enhancing the flavors of a dish.

#### Sample 405 — Transition

- Similarity: 0.4605
- Prediction: Over the course of these frames, the cloth undergoes a noticeable transformation from a state of wilting to a fully soaked state. Initially, it is a bare, bare-kneaded garment, with a visible layer of water on its surface. As the frames progress, the water's state changes from soaking to soaking, with the cloth becoming more soaked and soaked in water. By the final frame, the wavy fabric is more fully absorbed, with water dripping onto the cloth's surface, indicating a more thorough cleaning. The transition from soaked to soaked is reminiscent of the process of rinsing, with each frame demonstrating a different stage of the drying process.
- Reference: As the cleaning progresses from the top of the drying rack to the bottom, there's a notable change in the position of the hand and sponge, moving systematically downward with each frame. The methodical cleaning pattern indicates a thorough and sequential approach, ensuring no part of the rack is missed. The surrounding environment remains unchanged, emphasizing the singular focus on the task of cleaning the rack. The water's surface in the sink subtly reacts to the cleaning actions above, with the level of disturbance decreasing as the hand moves lower, away from the water's surface.

#### Sample 406 — Transition

- Similarity: 0.4793
- Prediction: Over the course of these three frames, the bin undergoes a dynamic process of removing waste from the trash can. Initially, the lid is partially open, with the lid firmly closed. As the frames progress, the person's hand moves closer to the lid, revealing a more streamlined and streamlined appearance. By the final frame, the contents of the bin are removed, with a final touch of the lid's closure. The progression of the images captures the dynamic nature of the process, with each frame highlighting a different action.
- Reference: As we traverse through the frames, there's a pronounced evolution in the state of the strainer. Beginning with a substantial amount of orange-yellow liquid, there's a clear progression of this liquid being drained or poured out. The liquid's presence diminishes considerably from the first to the third frame, with the strainer transitioning from being nearly full to almost entirely empty. This sequence paints a picture of an action being carried out methodically, showcasing the draining process in its different stages, from initiation to near completion.

#### Sample 408 — Transition

- Similarity: 0.4585
- Prediction: The progression of the butter's state across these frames shows a clear progression in its state. Initially, it is untouched, with no visible signs of use. As the frames progress, the butter begins to crack, indicating that the butter has been poured into the container. As time progresses, the knife's action becomes more deliberate, revealing the butter, demonstrating the process of preparing the butter. The butter'
- Reference: Over the course of the three frames, there is a noticeable transition of the bottle from a closed state to an open one. Initially, the bottle is securely closed with the cap fastened tightly. As the frames progress, there is an evident effort to unscrew the lid, with the hand adjusting its grip around the bottle's neck. By the third frame, the cap has been entirely removed, and the bottle is positioned in a manner indicating an impending action of pouring or spreading its contents onto the underlying surface. Throughout this progression, the bottle remains over the tortilla, suggesting a deliberate intent to add its content to the meal being prepared.

#### Sample 410 — Transition

- Similarity: 0.3208
- Prediction: The sequence of frames captures the progression of the jar's state from a state of rest to a fully opened and reopened. Initially, the holder is positioned in a position to ensure the contents are not disturbed, and then the divider is pushed out, indicating the contents have been removed. As the frames progress, the hand's movements become more deliberate, demonstrating the action of removing the cylinder's contents. The hand'
- Reference: The progression of sweetcorn from can to pizza captures a brief narrative of pizza preparation in these frames. Initially, the sweetcorn is introduced to the pizza, finding a home among the stripes of sauce. As we move to the next scene, there is an active engagement, a deliberate scattering that increases the sweetcorn's presence across the pizza's canvas. By the final frame, the act of sprinkling sweetcorn reaches a crescendo, culminating in a more uniform distribution, filling the space with color and texture. The narrative is one of addition and integration, with each frame representing a moment in the transformation of raw ingredients into a pre-baked culinary creation.

#### Sample 411 — Transition

- Similarity: 0.3976
- Prediction: The sequence of frames captures a clear progression in the handling of the chopping board. Initially, the board is positioned in a state of rest, with the blades positioned on the ground. As the frames progress, the person's hands move from one side to the other, indicating the action of removing the board. By the final frame, the action is complete, with a hand firmly grasping the board, ensuring that the board has been thoroughly rinsed. The consistent movement of the blade, the hand's motion, and the hand-hand motion are indicative of a deliberate action.
- Reference: The sequence of images captures the progression of a kitchen task involving a pot. Initially, the pot is left unattended in the sink, filled with leftovers and a fork, set in a cluttered and active kitchen environment. Subsequently, the pot is removed from the scene, leaving behind a space that indicates recent activity and the ongoing process of cleaning up. Finally, the pot reappears, this time being handled by someone who is in the act of covering it with a lid, likely signaling the end of its use and the transition to storage or further cleaning. This progression illustrates the common kitchen routine of dealing with cookware after a meal has been consumed.

#### Sample 412 — Transition

- Similarity: 0.4542
- Prediction: Over the course of these frames, the chopping board undergoes a clear transformation from being partially rinsed to being fully rinsed. Initially, the board is positioned in a position that allows the water to reach the surface, indicating that the water has been drained. As the frames progress, the water's movement changes to a more gentle, more controlled position, implying that the board has been thoroughly rinsed. By the final frame, the bowl is firmly held, demonstrating the proper handling of the board, ensuring that the cleaning process is complete. The consistent movement of the water, the consistent handling of water, and the consistent movement
- Reference: The progression observed in the spring onion's state from the first to the third frame demonstrates a systematic cleaning process. Initially presented in a dry state, the onion is then subjected to a rinse, evidenced by the water droplets forming on its surface. As the frames advance, the onion is held more securely, and the water pressure increases, causing the stalks to bend and reveal their fresh and crisp quality. The final frame encapsulates the conclusion of the rinsing, with the onion fully saturated and its roots drenched, signifying readiness for subsequent culinary use.

#### Sample 422 — Transition

- Similarity: 0.4680
- Prediction: Over the progression of these frames, the timer transitions from a state of being partially open to a fully closed state, with the person's hand indicating that the time has been taken. The person'
- Reference: Over the course of the three frames, the oven glove undergoes a clear transition. Initially, it is partially on, indicating the beginning of an action. In the following scene, the glove is completely removed or set aside, hinting at a brief interlude or the completion of an intermediate task. Finally, the glove is properly worn, signifying readiness for a task requiring thermal protection. This sequence suggests a dynamic kitchen environment where tasks are being performed in a non-linear fashion, with the glove being donned and doffed as necessary. The presence and position of the oven glove serve as an indicator of the actions and intentions of the person in the kitchen.

#### Sample 430 — Transition

- Similarity: 0.4903
- Prediction: Over the progression of these frames, the crock undergoes a clear transition from being fully uncovered to being fully opened. Initially, the person's hand is positioned at the top of the cylinder, indicating that the ice has been poured into the jar. As the frames progress, the hand's movements become more deliberate, revealing the icy contents of the container. By the final frame, the hands are positioned in a more pronounced position, demonstrating the gradual movement of the lid, resulting in the emergence of a new layer of ice.
- Reference: Over the course of these three frames, the plastic bag transitions from a restive, partially crumpled state to an active, fully open state. Initially, the bag sits with a closed mouth, exhibiting a recently disturbed state. Progressing through the sequence, hands intervene to manipulate the bag, pulling it apart to reveal its interior. By the final frame, the transformation is complete, with the bag held open, ready to receive or dispense its contents. This evolution is marked by the stretching of the plastic, the widening of the mouth, and the change in the bag's surface texture, from crumpled to stretched smooth.

#### Sample 433 — Transition

- Similarity: 0.3941
- Prediction: Over the progression of these three frames, the door transitions from a partially open state to a fully closed state. Initially, the lid is a bit blurry, with no visible movement. As the frames progress, the hand's movements become more deliberate, indicating that the door is open or closed. The hand'
- Reference: Throughout the frames, the cloth undergoes a clear transformation associated with the act of squeezing out liquid. Initially held in a preparatory grip, it is then firmly wrung, which is evident from the twisting and compacting of the material. As the sequence progresses, the intensity of the squeeze lessens, and the cloth begins to unfold and relax. This indicates the end of the active wringing phase, transitioning towards the cloth being unfurled to either be used again or to dry out completely. The fabric's moisture content seems to have decreased, judging by the less saturated appearance in the final frame, which suggests that the squeezing action effectively expelled liquid from the cloth.

#### Sample 437 — Transition

- Similarity: 0.4601
- Prediction: Over the progression of these three frames, the tin undergoes a clear transition from being awash in soap and water to being swept away. Initially, the container is positioned in a state of disarray, with no visible or visible debris. As the frames progress, the contents are retrieved, with the lid firmly placed, indicating a thorough cleaning. By the final frame, the lid is fully drained, with a clean surface to be seen, highlighting the process of rinsing and scrubbing. The progression of the utensils across these frames is indicative of a
- Reference: Over the course of the three frames, the pepper pieces undergo subtle yet noticeable shifts in their position on the chopping board. Initially scattered haphazardly, they experience a minor rearrangement, possibly due to external forces or preparatory actions for the next step in the cooking process. By the third frame, human intervention is evident as a hand enters the frame, poised to pick up or move the pepper pieces, indicating the progression from preparation to active utilization of the ingredients. This sequence portrays a typical kitchen scene where ingredients are prepared and then used in the cooking process.

#### Sample 447 — Transition

- Similarity: 0.4120
- Prediction: Over the progression of these three frames, the pot undergoes a clear transition from being a state of rest to being re-engaged. Initially, the lid is positioned in a position that indicates the presence of the pot, indicating the action of the person or the pot itself. As the frames progress, the person's hand is shifted to the right, implying the action is taking place. The person'
- Reference: The progression of the food processor's state unfolds in a meticulous cleaning routine. Initially, it is presented as a freshly washed item inside the dishwasher, surrounded by other clean dishes. The subsequent frame captures a moment of additional rinsing, indicating a personal touch to the standard cleaning process. Finally, the processor is seen being settled back into the dishwasher, not for another wash cycle, but rather for orderly storage. This sequence of actions not only emphasizes cleanliness but also the care taken in maintaining kitchen appliances, ensuring they are ready for their next use.

#### Sample 453 — Transition

- Similarity: 0.4832
- Prediction: Over the course of these frames, there's a clear progression in the cleaning process. Initially, the sponge is in a state of disarray, with no visible or noticeable debris. As the frames progress, the cleaning action is accelerated, with the sponge progressively removing and reorganizing. By the final frame, the sink is more thoroughly cleaned, with less water and less residue, indicating a thorough cleaning. The consistent state of cleanliness throughout the frames suggests a
- Reference: As the frames progress, the counter undergoes a dramatic transformation. What begins as a surface layered with imperfections, dust, and remnants, soon witnesses a division, a split between the cleaned and the cluttered. The dance of the cloth, dampened with intent, choreographs this change. By the final frame, the counter has shrugged off its prior state, embracing cleanliness and uniformity, telling a silent tale of care and maintenance.

#### Sample 459 — Transition

- Similarity: 0.3413
- Prediction: The sequence of frames captures a clear progression in the handling of the chopping board. Initially, it is positioned in a position that indicates a deliberate action, with the hand positioned at the center of the board, indicating a quick and deliberate action. As the frames progress, the hand's movements become more deliberate, implying a gradual movement, with a hand pointing at the board and a person's actions. The hand'
- Reference: Transitioning from the first to the last frame, the can undergoes a series of changes. Initially, it is at rest on the countertop, with the lid partially opened, revealing a static glimpse of its contents. As the sequence progresses, the can is picked up, its lid further retracted to display the peas or corn more clearly. In the final frame, the can is in swift motion, likely being disposed of or transferred to another area. Throughout this transition, the contents remain consistent, but their visibility increases as the lid is peeled back, and finally, the motion likely causes a disturbance of the contents, hinting at a change in their arrangement.

#### Sample 460 — Transition

- Similarity: 0.3820
- Prediction: Over the course of these frames, there's a clear progression in the state of the pan. Initially, the pan is in a state of disarray, with no visible signs of cooking or cooking. As the frames progress, the person's actions are evident, with the pan being progressively agitated and removing any remaining food or debris. By the final frame, the skillet is a more streamlined, more sanitary state, with less residue and less visible marks. The consistent movement of the hand, the constant movement of his hands, and the consistent movement in the pan's direction suggest a deliberate cooking process.
- Reference: Transitioning from the initial frame to the last, the sequence displays a rapid deceleration of both hand movement and water flow. Initially, the blur and lack of clear water stream suggest a tap being swiftly turned off. As the sequence progresses, the reduction in motion blur and hand retreat reflect the decreasing flow of water, culminating in the final frame where stillness prevails. The tap, once engaged in delivering water, now stands idle, having completed the transition from active to inactive, evidenced by the absence of water flow and the calm state of the surrounding area.

#### Sample 463 — Transition

- Similarity: 0.4262
- Prediction: Over the course of these three frames, the pot undergoes a subtle transformation from a state of rest to a position of cooking activity. Initially, the pan is positioned in a secluded position, indicating a cooking activity, possibly a meal or a pot of soup. As the frames progress, the lid is removed, revealing a more open and streamlined surface. The pan's appearance, from its slats to its handles, is indicative of a deliberate cooking activity that has taken place. The consistent movement of the pot's lid, the constant movement of its handle, and the constant motion of the pan'
- Reference: Over the course of the three frames, there's a perceptible sense of progression and movement, especially around the switch area. The images give an impression that the hand is reaching for, interacting with, or moving away from the switch. The exact transition from the "on" to "off" state (or vice versa) is not explicitly captured, but the sequence implies a deliberate action concerning the switch. The blurriness and rapid movement suggest that there might be a swift change in the state of the switch, but the specific details of that transition remain inconclusive based on the provided frames.

#### Sample 468 — Transition

- Similarity: 0.4159
- Prediction: Throughout the sequence, the chopping board undergoes a clear transformation from being partially rinsed to being re-handled. Initially, the board is positioned in a position that allows the water to reach the surface, ensuring that the water is filtered out. As the frames progress, the water's flow becomes more concentrated, indicating that the rinsing process is complete. By the final frame, the bowl is firmly held, allowing the water and water to flow through the board, demonstrating the thoroughness of the scrubbing process. The consistent water flow throughout the board reflects the thorough cleaning process, highlighting the effectiveness of the cleaning
- Reference: Throughout these frames, the bell pepper transitions from a dry state with scattered water droplets to a fully rinsed vegetable with a slick, wet surface. Initially, the rinse is gentle, affecting only part of the pepper's surface, but gradually, the entire pepper becomes enveloped in water. The hand's grip changes to expose different angles of the pepper to the stream, indicating a deliberate and methodical cleaning process. The consistent stream of water over the bell pepper not only cleanses but also accentuates its fresh, vibrant appearance.

#### Sample 469 — Transition

- Similarity: 0.4809
- Prediction: The sequence of frames captures a clear progression in the handling of the jar. Initially, the holder is positioned in a position that is a bit resting, indicating that the ring is being handled. As the frames progress, the hand's movements are more deliberate, demonstrating that the action is taking place. By the final frame, the hands are engaged in preparing the ramekin, implying that the hand is preparing to serve. The hand'
- Reference: Starting from its initial state where it rests on the appliance, there is a gradual and evident progression in the cover's movement across the frames. Initially, slight elevation suggests the beginning of the lift. As we move to the next frame, there's clear interaction with hands surrounding and tilting it, indicating an active and deliberate action of removal. By the final frame, the cover is almost entirely lifted, showcasing the culmination of the removal process, with the motion and environment around it capturing the rapidity and fluidity of the action. The entire sequence demonstrates a steady progression from a static state to dynamic motion.

#### Sample 470 — Transition

- Similarity: 0.3623
- Prediction: The sequence of frames captures a clear progression in the state of the bottle. Initially, it is in a state of rest, with no visible action. As the frames progress, the bottle is positioned in sweeping motions, indicating a gradual movement. As we move forward, the liquid is progressively agitated, with the hand indicating its presence. The liquid's state is a subtle transition, highlighting the action of the hand, a shift in the direction of the action. The consistency of the liquid'
- Reference: Over the course of the three frames, the plug undergoes a clear transition from being partially inserted in the power outlet to almost completely removed. Initially, the plug is seen in a semi-attached state, with the person’s hands positioned to start the unplugging process. As the sequence progresses, the hands are observed pulling the plug out, demonstrating more of the metal prongs in the process. By the final frame, the plug is nearly detached, signifying the end of the action. This sequence showcases a careful and deliberate movement, likely performed to disconnect the appliance without causing damage to the plug or the outlet.

#### Sample 477 — Transition

- Similarity: 0.2689
- Prediction: Over the course of these three frames, the rice undergoes a noticeable transformation from a state of being partially cooked to a fully cooked state. Initially, the water is a clear, hazy liquid, with a few grains and a little water clumping. As the stirring progresses, the grains are progressively incorporated into the water, indicating that the rice has been thoroughly stirred. By the final frame, the grain has been absorbed, and the water has dissolved, demonstrating a more streamlined and uniform cooking process. The transition from soaking to cooking is reminiscent of a cooking process that involves a
- Reference: Observing the progression of the light in these frames depicts the ignition and stabilization of a gas burner's flame. Initially, a magenta glow indicates the initial light-up, followed by a transition to a bright blue as the flame becomes more intense and the gas combustion reaches a higher efficiency. Finally, the flame settles into a steady state, with a strong blue core and a constant outer flame, signifying a sustained and even heat source. This progression is typical for gas burners, as the color and intensity of the flame can indicate the stage of heating and the efficiency of the fuel being burned.

#### Sample 490 — Transition

- Similarity: 0.4123
- Prediction: Over the progression of these frames, the package undergoes a clear transition from being fully opened to being fully uncovered. Initially, the packaging is essentially unopened, with no visible signs of the person's presence. As the frames progress, the person begins to engage in a more deliberate action, revealing the contents of the package. By the final frame, the packaged product is fully engulfed, with the person demonstrating the action's significance. The person'
- Reference: The tortilla undergoes a noticeable transition across the three frames, driven by the careful manipulation of the hand. Initially presented as a flat, supple disc, it begins a journey back to its pack, its shape and texture remaining relatively intact. As the motion progresses, the tortilla succumbs to the forces exerted by the hand and gravity, bending and folding, altering its form. This evolution from a flat entity to a conforming, folded object encapsulates a simple, yet precise action of returning the tortilla to its storage, a mundane task executed with an everyday grace and necessity.

#### Sample 491 — Transition

- Similarity: 0.4950
- Prediction: Over the course of these frames, the pak choi undergoes a clear transformation from a freshly cut leaf to a slicked, sliced piece. Initially, the leaves are pristine, with the stems separating from the leaves. As the frames progress, the leafs are progressively trimmed, with a more slender appearance. The leaves are now arranged in a manner that is consistent with the preparation of the steamed pak, indicating a thorough cleaning. The process is evident in the final frame, with each frame highlighting a different action, demonstrating the process of preparing the
- Reference: Starting from a fresh and untouched state, the coriander undergoes a transformation across the three frames. Initially presented in a whole and unprocessed form, the herb is gradually dissected, with leaves and stems becoming increasingly separated and chopped. As the frames progress, there's a noticeable increase in the distribution of cut coriander pieces on the board, showcasing the stages of the herb being prepared for a culinary purpose. The evolution of the coriander's state is evident in the increasing fragmentation and dispersion of its components.

#### Sample 495 — Transition

- Similarity: 0.3247
- Prediction: The sequence of frames captures a dynamic sequence of actions on the kitchen counter. Initially, the counter is positioned in a position that is primarily occupied by the person. As the frames progress, the person's movements become more deliberate, indicating that the counter has been placed in re-entry mode. By the final frame, the action is complete, with the counter positioned and ready to be used. The consistent pattern of the hand's movement across the frames suggests a deliberate action, implying that the person is attempting to place the counter in pause mode. The progression of the counter's actions is a subtle reminder of the process of preparing for a meal or meal.
- Reference: Throughout the sequence of images, there is a clear progression in the state of the plug as it transitions from being fully inserted to partially removed from the wall socket. Initially, the plug is firmly in place, but as the sequence progresses, a pulling force acts upon it, evidenced by the change in the angle and tension of the cord. By the final frame, the plug is only halfway engaged with the socket, and the movement suggests a deliberate action to disconnect the plug. The unplugging appears to be done with some haste or urgency, as the cord is taut and the action swift. This sequence captures the very moment of electrical disconnection, a commonplace yet crucial action in daily life.

#### Sample 496 — Transition

- Similarity: 0.3296
- Prediction: The sequence of frames captures a dynamic sequence of actions. Initially, the paper is positioned in a state of rest, with the hand guiding it. As the frames progress, the hand's movements become more deliberate, indicating that the paper has been positioned. By the final frame, the person's actions become more intentional, implying that the hand is attempting to place the paper in re-positioning mode. The hand'
- Reference: Across these frames, the package undergoes a visible transformation from a blurred object in motion to a stilled and focused item, indicating the transition from shaking to a pause. The bag inflates progressively, as evidenced by the increasing puffiness, which is a tell-tale sign of the popcorn being heated and popped inside. The person's interaction with the package evolves from vigorous shaking to a careful examination, and finally, to a display and preparation to open, following the instructions for a presumably hot and ready-to-eat snack.


## Interpretation Notes

- BLEU and ROUGE-L measure lexical overlap with reference captions.
- Semantic similarity measures embedding-based caption similarity.
- Temporal alignment aggregates semantic similarity across the four stages.
- Low-similarity cases are candidates for manual review, not confirmed factual errors.
