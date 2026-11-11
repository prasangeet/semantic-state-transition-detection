# OSCaR-Lite Evaluation Report

- Generated: 2026-11-10T10:15:29.896692+00:00
- Samples evaluated: 500

## Temporal Stage Metrics

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic Similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.3377 | 0.1659 | 0.0835 | 0.0435 | 0.2247 | 0.5528 |
| During | 0.3149 | 0.1624 | 0.0815 | 0.0416 | 0.2332 | 0.5553 |
| After | 0.3127 | 0.1609 | 0.0812 | 0.0423 | 0.2262 | 0.5548 |
| Transition | 0.3261 | 0.1788 | 0.0986 | 0.0589 | 0.2525 | 0.6012 |

## Temporal Alignment

- Overall temporal score: 0.5660

| Stage | Semantic Alignment |
|---|---:|
| Before | 0.5528 |
| During | 0.5553 |
| After | 0.5548 |
| Transition | 0.6012 |

## Qualitative Error Analysis

- Similarity threshold: 0.5000
- Low-similarity cases: 715

| Stage | Low-Similarity Cases | Rate | Mean Similarity |
|---|---:|---:|---:|
| Before | 205 | 0.4100 | 0.5528 |
| During | 183 | 0.3660 | 0.5553 |
| After | 191 | 0.3820 | 0.5548 |
| Transition | 136 | 0.2720 | 0.6012 |

### Cases for Manual Inspection

#### Sample 5 — Before

- Similarity: 0.2883
- Prediction: The countertop appears to be in a state of flux, indicating a recent change in the position of the counter. It appears to have been placed on a table or counter, presumably to serve as a storage space for food or other household items. The counter's surface is slightly tilted toward the right, suggesting a gradual shift in the direction of the movement of the kitchen counter.
- Reference: The floor is comprised of square, mustard-yellow tiles with slightly darker grout lines that create a grid-like pattern across the surface. In this scene, a few small, dark specks and light smudges are scattered across the tiles, indicating either bits of dirt or minor stains. The floor's glossy finish reflects some of the overhead lighting, which highlights the imperfections and the wear of the tiles, such as faint scratches and slight discoloration in places, suggesting this is a well-used area.

#### Sample 8 — Before

- Similarity: 0.4249
- Prediction: The coffee maker is positioned on a counter in a kitchen, with the lid open, indicating that it's ready to be used. It's surrounded by a white countertop, which appears to be a microwave oven, with a removable lid, suggesting that it may be plugged in. The interior of the coffee maker has a chrome-plated handle and a stainless-steel top, suggesting a potential use for a coffee machine. There are no other items on the counter, such as a pot or pot, and there's no indication of a particular type of coffee.
- Reference: The toaster, with a reflective stainless steel surface, sits idly on a countertop, surrounded by ambient light. Its two slots are vacant, and there’s no visible sign of any toasted bread within. The toaster's temperature dial is at its midpoint, suggesting a medium toast setting, while the lever is in its uppermost position, indicating it hasn’t been pressed down. The power indicator light, located on the side, is not illuminated, suggesting that the toaster is currently off.

#### Sample 9 — Before

- Similarity: 0.4484
- Prediction: The tomato appears to be in the middle of a cooking process, with a thin layer of flesh surrounding it, indicating that it is in the process of being sliced. The tomato's skin is exposed, suggesting that it may have been sliced too early. The knife's edge is positioned against the tomato, which is poised to be sliced at a 45-degree angle, implying that the knife has been slicing the tomato in a circular motion.
- Reference: The pepper, vibrant red in color, lies intact on the cutting board. Its skin is glossy, reflecting the light from the surrounding environment. The stem protrudes upward, indicating the top side of the vegetable, and the overall shape of the pepper appears robust and fresh, untouched by any cutting or slicing.

#### Sample 12 — Before

- Similarity: 0.4968
- Prediction: The bin appears to be in the middle of a kitchen sink, with a lid that appears to have been partially opened. The bin's lid is visible, suggesting that it may have been thrown away, indicating that it is not yet fully closed. It is positioned in a position that indicates that the bin has been emptied, implying that the lid is still open, and that the contents of the bin are still present.
- Reference: The basket appears to be partially open with some items inside, although the exact content is not entirely discernible due to the oblique angle of the shot. Adjacent to the basket, there's a surface with a blurry orange and red pattern, perhaps a textile or a rug. A portion of a purple object, likely related to the basket or its contents, is visible to the left. The surrounding environment includes a floor with tiles, suggesting an indoor setting.

#### Sample 15 — Before

- Similarity: 0.4274
- Prediction: The jar appears to be in the hands of a person attempting to open the lid, indicating that they are preparing to eat. The lid is partially closed, suggesting that the contents of the jar are not yet being poured out. The liquid content is likely to be contained within a small amount of liquid, suggesting a gradual release of the liquid. The container's surface is slightly damp, suggesting there may be a slight movement in the process of emulsifying the contents.
- Reference: In this scene, the stock appears to be at an early stage of preparation. The liquid's surface is slightly rippled, perhaps due to recent stirring, and a light sheen can be seen, hinting at the presence of oils or fats. The coloration of the stock is a pale yellow, suggesting it might be a chicken or vegetable broth. The glass containing the stock shows that the mixture is almost full, and there are no visible solid particles or ingredients, indicating a clear and potentially strained mixture.

#### Sample 20 — Before

- Similarity: 0.3750
- Prediction: The paper appears to be in the hands of a person with a knife, suggesting that they are preparing to eat. The paper is positioned on a table, with its edges exposed, indicating that it has been placed in a position where it can be easily accessed. The person's hand appears to have grasped the paper, implying that it is in the process of being sliced. There is a thin layer of paper on the table, which suggests that the person is preparing for a meal.
- Reference: The yogurt in this frame appears to be in a state of being intentionally arranged. One can observe that a hand is positioning a yogurt container, which is upright and has a lid depicting some form of fruit, likely indicating the flavor. The placement is precise and seems to be part of an organized pattern, with two other yogurt containers already placed in proximity: one upright and another on its side, possibly to showcase the brand or variety. The environment suggests that the action is taking place in a kitchen, given the presence of a microwave, stove, and various kitchen items in the background.

#### Sample 22 — Before

- Similarity: 0.2540
- Prediction: The skin of the chicken appears to be in a state of transition, with a thin layer of skin on the surface of the meat. The skin is exposed to the light, indicating that the meat is being prepared for cooking. The knife's edge is visible, suggesting that the person is attempting to remove the skin from the chicken. There are no visible marks or markings on the skin, which indicate that the skin has been partially removed.
- Reference: The garlic press appears to be in the initial stages of use, with a clove of garlic placed within its chamber. The device is oriented horizontally, held firmly in the user’s hands over a pan containing uncooked spaghetti. The handles of the garlic press are slightly apart, suggesting that the squeezing action has just begun. The press itself is constructed of metal, likely stainless steel, with a grid of small holes at its head through which the garlic will be extruded. The user's grip is confident, indicating the commencement of the pressing process.

#### Sample 24 — Before

- Similarity: 0.4402
- Prediction: The bag appears to be in a kitchen, with a plastic lid and a spherical shape, suggesting a person is preparing to open the bag. The bag's interior is cluttered, with its contents scattered around the bag, indicating that the bag has been opened. There are no visible objects, such as a knife or a spoon, suggesting the bag is in the process of being opened.
- Reference: A pair of scissors is opened and inserted into a notch of a blue plastic clip, which is mounted on the edge of a packet labeled "Funghi Porcini". The scissors' handles are blue, and the blades silver, with one blade partially inserted into the clip's opening. The person holding the scissors appears to be right-handed, as inferred by the thumb and fingers' positioning. The clip is halfway along the length of the packet, suggesting the intention to either open or reseal it. Surrounding the scene are various kitchen items, including dishes in an orange drying rack, a roll of paper towels, and a white napkin.

#### Sample 26 — Before

- Similarity: 0.4864
- Prediction: The paper appears to be in a state of transition, with a thin layer of paper on the surface of the paper, indicating that it is in the process of being rolled. The paper's surface appears to have been rolled, suggesting that the person is preparing to roll the paper. The person's hand is positioned at the edge of the tray, implying that they are preparing for the roll to roll.
- Reference: The cling film appears tightly wound around a yellow cylindrical cardboard tube, its roll relatively untouched and pristine. It's gripped firmly in a person’s hands, one thumb positioned near the film’s end, suggesting preparation for unrolling. The film itself shows no signs of stretching or distortion, and the plastic’s translucent sheen is consistent, reflecting the light evenly, indicating it has not yet been pulled or manipulated.

#### Sample 28 — Before

- Similarity: 0.4370
- Prediction: The table appears to be in a state of transition, with a person's hand positioned on the edge of the table, indicating a moment of contemplation. The table is positioned in the middle of a kitchen counter, suggesting a place for a meal or a quick meal. The surface of the counter is cluttered, suggesting that there may be a variety of food items on the table. The counter's surface appears to have been wiped down, suggesting it has been scuffed or soiled. The countertop is surrounded by a number of other items, including a dish towel, a towel, and a plate.
- Reference: The sheet of paper is grasped firmly in the person's right hand, held vertically, with the bottom edge parallel to the drawer's edge and the top edge oriented upwards. The hand appears to be in the initial phase of tearing, with the fingers positioned in a way that suggests force is about to be applied. The paper itself looks pristine, uncreased, and undamaged, with its white surface catching the light, indicating a smooth, possibly new sheet. There is no visible wear or prior folding, and the edges are crisp and straight.

#### Sample 30 — Before

- Similarity: 0.3622
- Prediction: The crockpot appears to be in a boiling state, with a sprinkling of water on the bottom, indicating it's in the early stages of cooking. It's positioned in the middle of a kitchen sink, with the lid open, suggesting a simmering stream of water. The water's surface is slightly damp, suggesting that the water hasn't been dripping from the bottom of the pot, implying a slow cooking process. There's also a slight amount of water present in the pan, which suggests that there's still a lot of water left in the pot.
- Reference: The colander is positioned above the left sink basin, securely held by a hand enveloped in a yellow rubber glove. It appears to be filled to the brim with freshly rinsed rice grains that are clumped together, suggesting that the rice has just been washed and is possibly still absorbing water. The colander itself is metallic, with a pattern of round perforations throughout, ideal for draining water while retaining the small grains. Light reflects off the wet surfaces of the colander and the rice, indicating the presence of moisture.

#### Sample 31 — Before

- Similarity: 0.3844
- Prediction: The countertop appears to be in a state of flux, with a light brown hue indicating a recent cleaning process. A hand is positioned on the edge of the countertop, pointing to a kitchen counter that appears to have been recently cleaned. There is a visible handprint on the surface of the counter, suggesting a thorough cleaning process is underway. The counter appears to contain a variety of items, including a dish towel, a plate, and a bowl.
- Reference: The glass, appearing to be a standard pint-size, is situated upside down on the tabletop, its opening facing down. The translucent material suggests it's made of a typical glass composition, possibly indicating recent usage as there are no visible residues on its inner surface. The base of the glass, now at the top, reflects a smidgen of light, hinting at a relatively clean and glossy finish. The glass is positioned slightly off-center to the left in the viewer's perspective, with ample space around it, undisturbed and static in its placement.

#### Sample 32 — Before

- Similarity: 0.4819
- Prediction: The lid of the container appears to be open, with a spherical shape, suggesting a person is preparing to open the container. The lid is positioned in a horizontal position, indicating that the container has been opened. The person's hand is pointing at the container, suggesting that it's in the process of opening.
- Reference: The lettuce is enveloped in a clear, plastic wrap, appearing crisp and fresh with a bright green color that suggests it has been recently purchased or harvested. The leaves are tightly packed, indicating the lettuce is likely a head of iceberg or a similar variety, known for its dense, rounded shape. The plastic wrap is intact, with no visible tears or openings, preserving the lettuce's moisture and freshness. The surrounding area is cluttered with kitchen items, but the lettuce is the focal point, resting on a white, rectangular container with grooves, which may be a lid to another container or a cutting board.

#### Sample 33 — Before

- Similarity: 0.4073
- Prediction: The saucepan appears to be in a kitchen setting, with a lid positioned on top of the saucepan, indicating that it has been placed in the right position. The saucepan's lid is positioned in the middle of the pan, suggesting that it may have been placed at a different angle from the stove. The pan's surface is slightly tilted toward the camera's perspective, which suggests that the saucepan is still in its original position. There are no visible objects in the background, such as a plate or a pot, but there are a number of other objects, including a bowl, a spoon, and a hand-held kitchen knife.
- Reference: The cabinet appears to be slightly ajar with the door swung open to a small degree, allowing a glimpse of its contents. On the lower shelf, there are visible stacks of cans that seem to be in a neat order, with labels facing forward, making them easily identifiable. Above, on the upper shelf, the blur obstructs a clear view, but it suggests the presence of additional items, possibly more cans or containers, hinting at a well-stocked and organized space. The edge of the cabinet door shows a handle, indicating the manner in which it is meant to be opened further.

#### Sample 36 — Before

- Similarity: 0.4707
- Prediction: The butter appears to be freshly sliced, with a slightly smoky texture and a light brown color. Its surface is a dark brown, indicating that it has not yet been fully sliced. The knife's edge is positioned against a white background, suggesting that the butter has been placed in a position where it can be easily seen. The butter's texture is reminiscent of a buttery texture, suggesting a smooth texture.
- Reference: The butter is encased in a rectangular plastic tub with a bright blue lid, prominently featuring the brand "FLORA" and a sunflower image indicating a light, sunflower-based spread. The lid is securely attached, showing no signs of having been opened. The spread inside is unseen, implying a fresh, untouched state. The tub rests on a kitchen counter, held firmly by a left hand, with the right hand holding a butter knife poised to lift the lid, indicating an imminent action of usage.

#### Sample 41 — Before

- Similarity: 0.3084
- Prediction: The microwave appears to be in a closed position, with its lid partially open. Its interior is cluttered with a variety of items, including dishes, dishes, and utensils, including a pot of water. The interior of the microwave is dimly lit, suggesting that it is not yet fully operational. There are no visible objects in the kitchen, such as a dish or a bowl of food, but there are a number of items on the counter.
- Reference: The milk bottle, with a classic white and yellow design suggesting a standard pasteurized variety, rests on its side near the kitchen sink's edge. Its cap, a vibrant red that contrasts starkly with the bottle's muted tones, is partially obscured from view, suggesting it may not be fully secured. Shadows cast across the bottle indicate ambient lighting from above, and a slight reflection hints at the bottle's glossy surface, likely plastic. The positioning of the bottle, coupled with nearby kitchen items, gives the impression of a hurried or cluttered setting.

#### Sample 43 — Before

- Similarity: 0.4725
- Prediction: The coffee appears to be in the hands of a person with a spoon, indicating that it has been placed in a hot pot. The spoon is positioned in the middle of the cup, pointing at the coffee's surface, suggesting that it is a medium-sized coffee filter. The coffee is surrounded by a thin layer of whipped cream, which appears to have been poured onto the coffee grounds, implying that there is still a lot of coffee left in the cup.
- Reference: The sugar jar appears closed and placed to the left of a hand mixer and a box of tea, just in front of a power strip crowded with various plugs. It's a clear jar with a visible fill line of sugar, indicating it is nearly full. The lid is white with a flip-top mechanism that is currently in a closed position, securing the contents within. The jar sits on a kitchen countertop made of speckled grey material, and there is an assortment of kitchenware and other items in the immediate vicinity.

#### Sample 45 — Before

- Similarity: 0.4919
- Prediction: The jar appears to be in the hands of a person holding a spoon, indicating that they are about to pour a liquid into it. The spoon is positioned in a hand-held position, suggesting that the liquid is being poured into the jar. The container's contents are clearly visible, with the lid positioned slightly above the bowl, suggesting a slight movement.
- Reference: The jam appears as a concentrated, viscous mass, clinging persistently to the fork's tines, indicating its thick, gelatinous consistency. A prominent dollop of jam rests atop the tines, with its deep red hue and glossy sheen suggesting a fruit-based composition, likely berry. The surface tension of the jam is evident, with the mass not yet succumbing to gravity, hinting at the presence of pectin which is common in jams to give them structure.

#### Sample 51 — Before

- Similarity: 0.2670
- Prediction: The bin appears to be in a state of transition, suggesting a gradual movement of the bin's contents. The bin is positioned in the middle of a kitchen counter, indicating that there is a lot of food on the counter. The lid is partially open, suggesting that there may be a small amount of food in the bin.
- Reference: The image captures a cylindrical filter component, partially obscured by the person's hand as they are in the midst of removing or inspecting it. The filter's exterior is predominantly white, with some areas of discoloration, suggesting it may have accumulated dust or other particulate matter. The top portion of the filter appears to be a semi-transparent material, possibly a fine mesh designed to trap contaminants. The texture of the surface suggests a fibrous material, commonly used in filters to enhance their trapping capability. There is visible debris collected on the filter's surface, indicating it has been in use and is performing its function of purifying the air or water it is designed for.

#### Sample 56 — Before

- Similarity: 0.3598
- Prediction: The box appears to be in a closed position, with its contents positioned in the middle of a kitchen counter, indicating that the person is preparing to open the box. The box's contents are clearly visible, with the lid positioned at the top of the box, suggesting that it has been opened.
- Reference: The packaging appears largely intact but slightly compressed at the top, suggesting the initial stages of crumpling. The shiny blue and silver hues reflect light, indicating its metallic nature, likely aluminum. A human hand with a fair complexion is visible, with fingers gently curving around the top part of the packaging. This crumpling action has not yet deformed the original cylindrical shape significantly, leaving the majority of the packaging still resembling its original form.

#### Sample 57 — Before

- Similarity: 0.4214
- Prediction: The pot appears to be in the middle of a pot, with its lid open, indicating that it has been placed in a position where it can be easily accessed. Its interior is cluttered with a variety of items, including dishes, pots, and utensils, which are likely to be used to prepare food. The pot is positioned on a flat surface, with the lid open to reveal a sink, sink, and basin. The water level is moderate, suggesting that there may be a slight amount of water in the pot.
- Reference: The coffee filter is depicted being held at a slight angle above the coffee maker. It appears to be a used filter, given the dark, wet coffee grounds that fill it to near capacity, suggesting a recently completed brewing cycle. The filter's structure, a basket shape with radial ribs, indicates that it is designed to fit snugly within the coffee maker's compartment. A few coffee grounds have spilled onto the machine's surface, and the filter's rim is stained, showing signs of frequent use.

#### Sample 58 — Before

- Similarity: 0.4824
- Prediction: The kitchen sink appears to be in the middle of a busy kitchen, with a person's hand hovering at the edge of the sink, indicating that the sink is about to open. The sink's surface is cluttered, suggesting that there may be a small amount of food in the sink. The kitchen's lighting is dim, suggesting it's a kitchen setting.
- Reference: A partially open cupboard is captured mid-action, its white door swung outward to the right, revealing a glimpse into the cabinet's interior. The door, equipped with a sleek, metallic handle on its left side, hangs slightly askew, indicating a swift movement. Inside, a variety of items are visible but not clearly discernible due to the motion blur. The cupboard's contents appear to include a mixture of possibly kitchen-related objects, stacked or organized in a manner that suggests everyday use. The blur obscures details, but the suggestion of shapes and colors indicates the presence of utensils or tools.

#### Sample 59 — Before

- Similarity: 0.4304
- Prediction: The mushrooms appear to be in the early stages of cooking, indicating that they're in the process of being cooked. They're positioned in a position that indicates they've been sitting for a long time, implying that they haven't been fully cooked yet. There's a slight amount of movement in the pan, suggesting that it's not yet ready to be cooked.
- Reference: The pan reveals a mix of chopped leeks and onions at an early stage of cooking, exhibiting a vibrant blend of greens and whites. The vegetables appear freshly tossed, resting loosely atop one another, with the light sheen of oil glistening on their surfaces, indicating that they have just started to sweat. The pieces are distinct and retain their individual form, showing no signs of caramelization or significant softening. The wooden spatula, held by a person's hand, is positioned as if it has just been used to stir or mix the contents, preparing for even cooking.

#### Sample 61 — Before

- Similarity: 0.4953
- Prediction: The table appears to be in a state of disarray, with a white surface that appears to have been sprayed with soap and water. A hand is positioned on top of the table, indicating that someone is attempting to clean the table. The surface is a dark brown, suggesting that it may have been washed or wiped with soap or water. The person's hand is visible, suggesting a hand is engaged in the process of cleaning the table itself. There are no visible marks or markings on the table surface, which indicate that the table is being cleaned.
- Reference: The crumb is resting on a patterned tablecloth, noticeably contrasting with its surroundings due to its darker color against the lighter background. The material appears to be coarse and grainy, suggesting it might be a fragment of bread or a baked product. Its irregular shape and small size make it seem inconspicuous amidst the table's pattern, which consists of square motifs with various illustrations. The crumb's position near the edge of the table places it in a precarious situation, poised for movement.

#### Sample 62 — Before

- Similarity: 0.2278
- Prediction: The dough appears to be a mixture of flour and baking powder, with a light brown hue, suggesting it has been incorporated into a recipe. Its texture is reminiscent of a paste, indicating that it has not yet been fully incorporated. The consistency of the dough is uneven, suggesting that there may be some mixing involved.
- Reference: A bottle of olive oil is introduced into the scene, appearing on the right side of the image, held by a hand with fingers wrapped around its neck. The bottle cap is still on, indicating the oil has not yet been used. The label is facing away from the camera, obscuring the brand and specific type of olive oil. The bottle is tilted at a slight angle, suggesting the person is about to pour the oil into a bowl containing a mixture, likely in preparation for adding the oil to the ingredients. The surrounding area is cluttered with various cooking utensils and containers, but the focus is on the imminent action of pouring.

#### Sample 63 — Before

- Similarity: 0.3772
- Prediction: The tomato appears to be freshly sliced, indicating that it has been placed in a pre-prepared dish. Its shape is reminiscent of a bowl, with a rounded edge, suggesting that it may have been thrown at a table or counter. The texture of the tomato's surface is slightly uneven, suggesting it may not be fully incorporated into the dish, which is likely a deliberate attempt to ensure that the tomato remains intact.
- Reference: A bowl sits on a countertop cluttered with various kitchen appliances and items, holding a mixture that appears to be in the initial stages of preparation. In the bowl, there is a raw egg, its yolk intact and sunny, surrounded by a clear viscous albumen, with flecks of black pepper scattered throughout, providing a stark contrast to the pale yellow and translucent whites. The egg has been cracked open recently, as suggested by the lack of disturbance in the albumen and the yolk's domed shape, indicating minimal interaction with the fork lying beside it.

#### Sample 66 — Before

- Similarity: 0.4861
- Prediction: The stovetop appears to be in the middle of a kitchen setting, with a gas burner in the center of the stove. The burner is positioned on a flat surface, indicating that the burner is not yet fully cooled. The flame appears to have been turned off, suggesting that there may be a slight change in the temperature of the burner. There are no visible marks or markings on the stovetop, which indicate that the stove is not functioning properly.
- Reference: The burner cap is being held by a pair of hands, with fingers slightly curled around its edges, indicating a gentle grip. The cap appears to be a standard circular stove burner cap, commonly found in home kitchens, with concentric rings and a central raised area where it sits atop the burner head. It's positioned above the stainless steel sink, catching the light in a way that highlights its metallic finish and the subtle signs of wear and tear from regular use, such as slight discoloration or staining. The background is cluttered with kitchen items, suggesting a domestic setting where cooking is frequently done.

#### Sample 73 — Before

- Similarity: 0.4453
- Prediction: The sink appears to be in a state of flux, indicating that it has been recently washed. The surface of the sink is covered with a layer of soapy water, suggesting that it may have been soiled. The person's hand is positioned on the edge of the basin, pointing to the sink's surface, suggesting a recent cleaning process. There is a small amount of soap and water on the sink surface, indicative of a thorough cleaning.
- Reference: The grid is held at a diagonal angle, with the top right corner slightly elevated compared to the bottom left, creating a visible slant across the image. The fingers of the right hand are wrapped around the top edge, securing it with a firm grip, while the thumb extends towards the center to stabilize the position. The grid's metal rods gleam with moisture, indicating recent cleaning or contact with water, and droplets are scattered across the surrounding sink area, reflecting the grid's recent movement.

#### Sample 74 — Before

- Similarity: 0.4368
- Prediction: The surface of the bowl appears to be in a state of flux, indicating that there is still a lot of dust on the surface. The bowl is positioned in the middle of a kitchen counter, with a thin layer of flour and a few grains scattered across the surface, suggesting that there may be a bit of dust in the bowl. The surface appears to have been sanded down, suggesting a gradual process of scrubbing the surface with the flour, which could indicate that the flour has been incorporated into the bowl's surface.
- Reference: The scale is a compact, digital model with a clear glass platform, resting on a black granite countertop. It is positioned to the right side of the bowl filled with a white powdery substance, presumed to be flour. The scale appears to be turned off, as no digital numbers or lights are visible on its display. It is situated next to an open notebook, with its top edge aligned with the spiral binding, suggesting that it might be used for recording measurements. Surrounding the scale are scattered ingredients and kitchen tools, indicating an ongoing cooking or baking process.

#### Sample 77 — Before

- Similarity: 0.2801
- Prediction: The button appears to be in the middle of a kitchen counter, indicating that it has been placed in a position where it can be easily accessed. The button is positioned in the center of the counter, with a hand resting on the top of the button, suggesting that it is currently in the process of being pressed. The fingernail's surface is slightly curved, suggesting a slight movement, and there is no indication that the button has been pressed yet. There are no visible marks or markings on the button itself, which suggests that it may be pressed against the counter.
- Reference: The milk container is initially captured with the lid firmly secured on top. The smooth, white surface of the container suggests that it's made of plastic, and it appears to be a standard size, suggesting it may contain a liter or so of milk. The container is grasped by a hand, presumably in preparation for opening.

#### Sample 83 — Before

- Similarity: 0.4263
- Prediction: The tomato appears to be in a sealed container, with a spherical shape, indicating it is in the process of being opened. A hand is attempting to open the tomato, which is positioned in the middle of a kitchen counter, suggesting that the person is preparing to eat. The tomato's surface is a dark brown color, suggesting it may have been thrown out of its packaging, implying that it has not yet been opened. There is no indication of the person's intent to open or close the container, which suggests that it is not yet ready to be opened.
- Reference: The jar of pesto is in its initial state, with the cap still firmly sealed, ensuring the freshness and flavor of its contents. The dark green hue of the pesto is slightly visible through the clear glass, suggesting it hasn't been disturbed recently. Around the mouth of the jar, there is no indication of residue or spills, indicating that it might be a new or very well-kept jar.

#### Sample 84 — Before

- Similarity: 0.3934
- Prediction: The microwave appears to be in a closed position, with its lid partially open, indicating that it is in the process of being opened. The interior of the microwave is cluttered with a variety of items, including food, dishes, and other items. The microwave's interior is dimly lit, suggesting that it may be a microwave oven. The surrounding area is a kitchen setting, with the kitchen sink, counter, and counter-top positioned in the middle of the frame. The kitchen area has a wide range of kitchenware, including utensils, dishware, and kitchenware.
- Reference: A hand is reaching towards the toaster's power plug, which is connected to a white double socket mounted on a tiled wall above a gray countertop. The toaster itself is a four-slice model with a metallic finish, reflecting the ambient light of the room. It sits idle with its control knobs turned to a neutral position, and the bread slots appear empty. To the right of the toaster, there's a clear plastic container and a colorful cutting board with the words "SLICE," "CHOP," and "PEEL" in a playful typography, hinting at food preparation activities.

#### Sample 85 — Before

- Similarity: 0.4933
- Prediction: The peach appears to be in the middle of a peeling process, indicating that it is in the process of being sliced. The fruit is ripe, with a smoky hue, suggesting that it has been sliced at a rapid pace. The knife is positioned in the center of the peach, pointing at the knife's edge, which indicates that the knife has just been slicing the fruit.
- Reference: The kiwi fruit is shown in various stages of preparation. One kiwi has been sliced horizontally into two halves, revealing the vibrant green flesh and small black seeds inside. Another half of the kiwi appears to have been partially scooped out, with some of the flesh remaining attached to the skin. On the plate, there are remnants of the scooped-out fruit, hinting at the scooping process that has been taking place. Additionally, the shiny metal spoon appears to have traces of the kiwi's juicy flesh on it.

#### Sample 88 — Before

- Similarity: 0.4642
- Prediction: The lid of the jar appears to be partially open, with a spherical shape, suggesting a person is attempting to open the lid. The lid is positioned on a flat surface, indicating that the lid is in the process of being opened. The person's hand is pointing at the lid, suggesting that it's about to be opened.
- Reference: The food container in view is semi-transparent with a blue rimmed lid, partially ajar, revealing its contents. Inside, a layered arrangement of cheese, discernible by its yellow-white hues and distinctive edging, is stacked with precision. Each slice is partially overlapped by the next, creating an ordered appearance. The container is held by a pair of hands, with the lid being gently lifted, indicating the initial stage of unveiling the contents.

#### Sample 89 — Before

- Similarity: 0.1888
- Prediction: The door appears to be open, with a gap in the middle of the frame, suggesting that the door is open. The door's hinges are slightly tilted, indicating that there is a slight movement in the room. The interior of the door seems to be partially open, suggesting the door may be closed.
- Reference: The squash container, predominantly white with touches of blue, rests atop a gray counter. It stands upright, showcasing its slender and elongated design. The label, although not entirely discernible, carries hints of blue and green graphics, likely illustrating the flavor or variety of the squash. Adjacently, a white cap lies on the counter, suggesting it's been recently removed or will be placed back on the container.

#### Sample 90 — Before

- Similarity: 0.4876
- Prediction: The avocado appears to be partially ripe, with a smoky exterior and a bright green hue. It is sliced in a circular motion, with the skin revealing a smooth, slender, fleshy appearance. The avocado's flesh is slightly charred, suggesting that it may have been sliced at a later stage. The blades of the avocado are positioned in the middle of the fruit, indicating a gradual process of slicing.
- Reference: The pepper is positioned on a wooden cutting board, cut-side down with its stem end facing left, indicating that an initial slice has been made to separate it into two halves. Its vibrant yellow skin is smooth and shiny, reflecting the light, with a slight variance in hue, suggesting natural rippling or indentations. The interior is not visible in this frame, but the intact silhouette suggests the seeds and inner membranes are likely still present.

#### Sample 92 — Before

- Similarity: 0.4694
- Prediction: The sink appears to be in a state of flux, suggesting that the water has been drained out of the sink. The sink's surface is slightly tilted, indicating that there is a slight amount of water in the sink, which may indicate that the sink is not yet fully emptied. The faucet appears to have been refilled with water, suggesting a recent change in the direction of the water's movement. The surrounding area is cluttered with a variety of items, including dishes, dishes, and kitchenware.
- Reference: A porcelain plate rests precariously on a white plastic dish drainer, tilting towards the edge, as if caught mid-movement. Its surface is glossy, reflecting the light overhead, indicating either a clean sheen or the presence of water. The plate’s rim is designed with a delicate curve, suggesting a subtle elegance. Its bottom is partially visible, and the brand mark is faintly discernible, implying a bottom-heavy tilt that could cause it to slip off the rack. The dish drainer's slats cast linear shadows on the plate's surface, adding to the sense of it being in a transient state.

#### Sample 94 — Before

- Similarity: 0.4278
- Prediction: The bacon appears to be in a state of transition, indicating that it's in the process of being sliced. The knife's edge is visible, suggesting that the knife has been inserted into the meat, implying that the meat has been partially cooked. The meat appears to have been partially sliced, with the knife pointing towards the meat's surface, suggesting a gradual process of slicing.
- Reference: A substantial block of chocolate, seemingly dark with a dense structure and studded with visible inclusions such as nuts or dried fruits, rests partially unwrapped from its aluminum foil. The person's hands are poised in a manner that suggests they are in the initial phase of cutting, with the knife's blade lightly indenting the surface but not yet fully committing to the slice. The chocolate's glossy sheen indicates a smooth, rich texture, and the knife's edge reflects a readiness to penetrate the confection.

#### Sample 97 — Before

- Similarity: 0.4712
- Prediction: The box appears to be in a closed position, with its contents visible in the middle of the frame. A hand is positioned on the edge of the box, indicating that it is preparing to open. The box's contents are clearly visible, suggesting that the person is attempting to open the box.
- Reference: The cereal appears to be contained within a transparent plastic bag that is held open by a hand. The bag is partially obscured by the edges of a red cereal box, indicating that the bag was likely removed from this box. The contents of the bag are not fully visible due to the angle, but one can discern the presence of multiple, small, grain-based pieces typical of dry breakfast cereal. There is no apparent motion of the cereal within the bag, suggesting that the action of extracting the cereal has just begun or is momentarily paused.

#### Sample 99 — Before

- Similarity: 0.4010
- Prediction: The surface of the counter appears to be in a state of flux, indicating that there is still a lot of work to be done on it. A hand is positioned on top of it, suggesting that a person is attempting to clean it. The surface appears to have been sanitized, possibly by a hand washing machine user, with a few drops of dish soap and a handful of crumbs on the counter. The countertop is cluttered with crumbs and other debris, implying that there may be a bit of work being done on the surface.
- Reference: The surface in this frame appears to be a wooden table with a visible grain pattern. Multiple objects are resting on it, including a red container, a bowl with some contents, a blue object, a green shape, a clear glass, and a clear container holding what looks like baked goods. Shadows of these objects, as well as reflections from the surroundings, can be observed on the table, giving an impression of ambient lighting.

#### Sample 100 — Before

- Similarity: 0.3709
- Prediction: The cabinet appears to be in a state of transition, with a slight hint of movement, suggesting a gradual movement. The cabinet's surface is slightly blurred, suggesting that it may be a partially closed cabinet. The door's hinges are visible, indicating that the cabinet has been closed for a few seconds, possibly a moment or two.
- Reference: The image captures an illuminated environment where light diffuses softly across various surfaces, indicating an active light source within the room. The light reflects off the tiled flooring, creating a pattern of highlights and shadows that suggest a glossy finish on the tiles. The countertop to the right also catches the light, indicating its polished surface, and various kitchenware items reflect the light differently, from the metallic sheen of pots and pans to the more subdued reflection of ceramic dishes. The light appears to be emanating from a point above the scene, casting a consistent glow across the room.

#### Sample 101 — Before

- Similarity: 0.4232
- Prediction: The jar appears to be in the hands of a person attempting to remove a piece of cheese from a plate, indicating that the cheese has been placed in a position where it can be easily grasped. The spoon's handle is positioned at the center of the jar, suggesting that the hand is holding the cheese in its hands, implying that the person is preparing the cheese.
- Reference: The milk in the container appears to be in an initial stage of stirring, with the surface showing a mild disturbance. There is a visible swirl starting to form, indicating the motion of a spoon or a stirrer recently having passed through it. The consistency of the milk seems uniform and no significant mixing of any added ingredient is apparent yet. The color is a uniform creamy white, and the viscosity appears to be typical of milk, without any signs of thickening or curdling.

#### Sample 107 — Before

- Similarity: 0.4652
- Prediction: The dough appears to be in the early stages of development, indicating that it has been incorporated into a recipe. The texture of the dough seems to be a mixture of flour, flour, and other ingredients, with a few exceptions, such as oats, rye, and sorghum. The dough's texture is reminiscent of a flour-based dough, which has a grainy texture, suggesting that the dough may be ready for use.
- Reference: The biscuit appears to be in its initial stage of being pressed, with its texture still visible, suggesting that it has just begun to be mixed or crushed. It's surrounded by an assortment of kitchen appliances and utensils, indicating that preparation is underway. The area looks cluttered, with a glass of something powdery next to the bowl, possibly an ingredient yet to be added. The biscuits retain their integrity to some extent, as the pressing has seemingly just commenced.

#### Sample 109 — Before

- Similarity: 0.2680
- Prediction: The kitchen sink appears to be in a state of transition, suggesting a recent change in the position of the sink. The sink's surface is slightly tilted toward the camera, suggesting that the sink may be positioned in the middle of a kitchen counter, indicating a moment of transition. The countertop appears to have been partially wiped down, suggesting it may have been wiped with a cloth or paper towel. The surface of the kitchen sink is cluttered, suggesting there may be some sort of debris on the counter or counter.
- Reference: A rubber glove, seemingly of a durable material and a vivid yellow hue, is placed on the edge of a wooden cutting board that is resting on a kitchen countertop. The glove's fingers are splayed outwards, revealing its inner surface and suggesting it has recently been removed. Adjacent to the glove is a blue cutting board, which bears marks of use, a testament to recent culinary activity. A spoon and a knife lay on the blue board, indicating a pause in meal preparation or the aftermath of cooking.

#### Sample 110 — Before

- Similarity: 0.3885
- Prediction: The kitchen counter appears to be positioned in a position where it is positioned at the center of the frame. Its shape is reminiscent of a kitchen counter, with a rectangular shape and a rounded edge. The counter's surface is slightly tilted, suggesting that the counter is tilting downwards, indicating that there is a slight movement in the area. The countertop appears to have been placed on a table or counter, possibly to serve as a storage space for food or other items.
- Reference: The chair appears in a position where it is partially tucked under a table. The tablecloth is colorful with a pattern, resting on a table with a light-colored surface. The chair itself has a cushioned seat with a light fabric, and the backrest is not visible in this angle. The floor is tiled, reflecting the chair's shadow and some light. The chair is angled such that one leg is closer to the camera, suggesting it may have been in motion or is about to be moved.

#### Sample 112 — Before

- Similarity: 0.3947
- Prediction: The box appears to be in a closed position, with its contents positioned in the middle of a kitchen counter. The box's interior is cluttered with a variety of items, including a bowl, a plastic bag, and a tray. A hand grasps the box, indicating that it's in the process of being opened.
- Reference: The image captures a blur of movement, likely due to the camera's swift motion. Amidst this swirl of colors and shapes, the focus is on a partially visible bag of coffee. The bag is not clearly discernible, but the slight crinkling texture suggests it may have been recently handled or is in the process of being moved. The surrounding environment is a jumble of kitchenware and appliances, all blending into the scene's dynamic and hasty vibe.

#### Sample 114 — Before

- Similarity: 0.4063
- Prediction: The garlic cloves are positioned on a cutting board in the middle of a kitchen counter, indicating that they are in the process of being sliced. The blades of the garlic peeler are visible, suggesting that they have just been sliced and ready to be sliced. The skin of the cloves appears to be partially sliced, with a thin layer of skin on the surface of the blades, suggesting a gradual process of peeling.
- Reference: The onion's outer skin is largely intact, giving it a dry and slightly glossy appearance. One can observe a purplish-red hue, characteristic of many onion varieties. The hands are gently holding the onion, with the fingers positioning around it, ready to peel or make an incision. The skin seems tight against the inner layers, indicative of a fresh onion, and there's little to no visible damage or blemishes on the skin's surface.

#### Sample 116 — Before

- Similarity: 0.4530
- Prediction: The bowl appears to be in a state of flux, indicating that it has not yet been fully emptied, suggesting that it may have been thrown away. The bowl's surface is cluttered with a variety of items, including a handful of dried fruit, a jar of dried vegetables, and a large bowl of ice cubes. Its contents are scattered around the bowl, implying that there may be a lot of food on the bowl.
- Reference: The ingredients appear to be in the early stages of preparation. A variety of food items are visible, most notably diced sweet potatoes that are collected inside a white bowl. On the countertop, there's evidence of fresh preparation with discarded peels and cut-offs from what seems like vegetables and fruits. To the side, there's a knife resting on a chopping board, indicating recent use. Some other ingredients, like canned goods and possibly some spices or seasonings, are also present nearby.

#### Sample 118 — Before

- Similarity: 0.3670
- Prediction: The vegetable appears to be in the middle of a cooking process, indicating that it has just started to cook. It's a bright green color, with hints of brown or brownish hues, suggesting that it's not yet ready to eat. The vegetables appear to be slightly charred, suggesting they've been preparing for a long time.
- Reference: The hob presents a white stove with four gas burners of varying sizes, organized in a traditional layout with two rows and two columns. The burners are capped with black grates, suitable for holding cookware securely. In this scene, a wok is placed on the front right burner, filled with a mix of vegetables that appear to be in the early stages of cooking, indicated by their vibrant colors and rigid textures. The knobs for gas control are aligned on the front panel, each corresponding to one of the burners. The control knob for the wok's burner is turned on, suggesting an active flame heating the pan. A spoon rest lies empty next to the hob, and the wooden countertop that surrounds the stove is clear of any other kitchen utensils or ingredients.

#### Sample 124 — Before

- Similarity: 0.3380
- Prediction: The salad appears to be in the hands of a person preparing a salad, with a thin layer of lettuce, indicating that it has been placed in a bowl. The leaves appear to be a mixture of green and yellow leaves, suggesting that they have been steamed or boiled, implying that they've been tossed before. The leafs are positioned in the middle of the salad, suggesting they're preparing for a particular dish, such as a vegetable salad.
- Reference: The wooden spoon in view exhibits a clean and unused appearance with a smooth, glossy finish indicative of minimal prior usage. The utensil is grasped firmly in the person’s right hand, its bowl facing downwards towards the plate below. The positioning of the spoon, coupled with the direction of the individual's grip, suggests an impending action, likely to involve contact with the plate's contents. The spoon's handle extends towards the edge of the frame, slightly tilted, enhancing the sense of anticipated movement.

#### Sample 131 — Before

- Similarity: 0.3646
- Prediction: The rag appears to be in the hands of a person with a knife, indicating that it has been recently washed. Its surface is slightly damp, suggesting that it may be wet or damp. The cloth's texture is a mixture of sand and water, with hints of mud and grime. The person's hand is positioned on the edge of the rag, presumably a beginner's grip, with her fingers pointing downwards. She's holding a small amount of the cloth in her hand, which indicates she's preparing to use it.
- Reference: The grid appears to be a lightweight, flexible plastic object, predominantly yellow in color with a matrix of uniform square cut-outs. It is being held by a person's hand, which is visible in the image, suggesting the grid is being moved or manipulated in some way. The orientation of the grid is such that the longer side is vertical, and the shorter side is horizontal, indicating that it may be in the process of being turned or flipped. The surrounding context, a kitchen sink area with various cleaning items, suggests that the grid may be a dish rack component or a similar utensil used in kitchen organization.

#### Sample 140 — Before

- Similarity: 0.3791
- Prediction: The towel appears to be in the hands of a person, with a hand on one side and a palm on the other. The towel is positioned in the middle of the frame, with the palm facing outwards, suggesting that the person is holding the towel. The person's hand is slightly tilted toward the towel, indicating that the towel has been placed in a position where it can be easily accessed.
- Reference: In this frame, the glass is grasped firmly by a hand, with fingers encircling its circumference. The glass appears to be partially filled with a clear liquid, as evident by the meniscus visible just below the rim. The base of the glass is securely placed on a wooden table with distinct grain patterns, while the surroundings exhibit a homey atmosphere with a wooden flooring and a portion of a chair visible.

#### Sample 142 — Before

- Similarity: 0.3677
- Prediction: The lid of the saucepan appears to be in a position that indicates it is in the process of being removed from the burner. The lid's surface is slightly tilted, suggesting that the lid has been placed in the right position. A hand grasps the lid, indicating that it's about to be removed. The person's hand is positioned on the edge of the pan, suggesting a slight movement. There's a gap between the lid and the saucepan's edge, which suggests that there's still room for the lid to remain.
- Reference: In this frame, the sausage is not immediately visible, suggesting it may be obscured or hidden beneath other objects on the countertop. Various items, including a bottle, a knife, and a plate, are scattered around the area, which could be potentially concealing the sausage. The dominant visual elements are a person's hands, which appear to be in the midst of handling or interacting with an item, possibly the plate, implying that the sausage might be under it or being prepared for covering.

#### Sample 145 — Before

- Similarity: 0.2963
- Prediction: The tomato appears to be sliced in a medium-sized portion, with a thin layer of white flesh surrounding it, suggesting that it is in the process of being sliced. The tomato's flesh is ripe, indicating that it has not yet been fully sliced, and the knife's grip is firmly pressed against the tomato, implying that the knife has been inserted into the tomato. The texture of the tomato contrasts with the rest of the avocado, which appears to have been sliced at a very slow pace, hinting at the initial stages of slicing.
- Reference: The piece of pitta bread is placed atop a round wooden cutting board. One can observe that the pitta is neither completely flat nor too puffed up, suggesting it has been lightly handled or possibly folded. From this angle, it appears slightly uneven in texture, indicative of its natural and rustic quality. The bread's surface appears soft and somewhat porous, likely making it ideal for dipping or holding fillings.

#### Sample 146 — Before

- Similarity: 0.4556
- Prediction: The saucepan appears to be in the middle of a kitchen setting, with a lid positioned on top of the saucepan, suggesting that it's about to be placed in a position where it can be easily accessed. It's positioned in the center of the frame, with the lid pointing outward, indicating that the saucepan has been placed in its place. The saucepan's interior is cluttered, with no visible objects, including a pot, sink, or other items. The pan's lighting is dim, suggesting a low-light setting.
- Reference: The tupperware in the frame is partially visible, with its open side facing downwards toward the counter. It appears to be a rectangular container made of a translucent, frosted plastic that diffuses the view of its interior. The lid is not attached, suggesting that the tupperware has either been recently used or is about to be used. Light reflects off its smooth surface, and the container's textured sides indicate it may have a grip-friendly design. The container is positioned next to a stack of plates and appears to be in motion, as indicated by the slight blur around the edges.

#### Sample 147 — Before

- Similarity: 0.3433
- Prediction: The stovetop appears to be in a neutral state, with a sprinkling of oil on it, suggesting that the burner is not yet fully cooled. The burner's surface is bare, and there are no visible signs of cooking or cooking. There is no indication of a pot or pot burner, and the flame appears to have been turned off.
- Reference: The mixer is prominently positioned on a kitchen countertop, close to the stovetop area. It appears to be a modern blender with a transparent container, a white base, and a lid. The blender's power cord extends towards an electrical socket, indicating it's ready for use. A hand, presumably the user's, is seen reaching out and grasping the blender's base, suggesting an imminent action or movement.

#### Sample 148 — Before

- Similarity: 0.4843
- Prediction: The bottle appears to be empty, with the lid positioned in the middle of the frame, suggesting that it is in the process of being opened. The bottle's interior is cluttered with a variety of items, including a jar, a plastic container, and a glass container. The lid is positioned on a white plate, suggesting a close-up view of the bottle.
- Reference: A carton of milk stands partially obscured behind a slightly open cupboard door, poised in the corner of a kitchen countertop. Its cap is firmly secured, indicating that it has not yet been opened. The carton, predominantly white with red accents, suggests a commercial brand, likely refrigerated before being placed here. Ambient light casts soft shadows around it, highlighting the unbroken seal of the cap and the untouched state of the carton, as if it has just been taken out from a grocery bag or refrigerator, waiting to be used.

#### Sample 150 — Before

- Similarity: 0.4127
- Prediction: The saucepan appears to be in the middle of a kitchen sink, with a handle pointing downwards, indicating that the saucepan is about to be placed in a position where it can be easily accessed. The saucepan's lid is positioned on top of the saucepan, suggesting that there is a slight movement in the process of removing the saucepan from the burner. The kitchen sink's surface is slightly tilted toward the camera's perspective, suggesting a gradual movement.
- Reference: The spice is initially placed in a relatively hidden position within the cupboard, surrounded by various other items such as bottles, jars, and containers of varying sizes and shapes. The visibility of the spice is partially obscured due to its placement and other items around it. There is a sense of stillness, with the spice resting comfortably, untouched and undisturbed in its familiar environment.

#### Sample 153 — Before

- Similarity: 0.3333
- Prediction: The countertop appears to be in a state of disrepair, indicating a recent cleaning process. The counter's surface is cluttered with a variety of items, including dishes, dishes, and utensils. A person's hand is visible, suggesting a thorough cleaning process is underway.
- Reference: The pepper mill appears to be in motion, falling towards the ground. The motion blur present in the image suggests rapid movement, and the position of the pepper mill, tilted at an angle, indicates it has just been knocked or is slipping from its standing position. The proximity of the hand and the cloth suggest an attempt to catch or stabilize the falling object. There's a dynamic interaction between the hand, the cloth, and the pepper mill, captured in the midst of an unexpected shift from stability to motion.

#### Sample 155 — Before

- Similarity: 0.4472
- Prediction: The soup appears to be in a medium-sized bowl, with a thin layer of sauce on the bottom, indicating that it has been simmering for at least a few minutes. The sauce appears to have been poured into a saucepan, which is positioned in the middle of the pan, implying that it's being stirred vigorously. There are no visible bubbles, suggesting that the sauce is still a little hot. The texture of the sauce appears slightly smoky, suggesting a light coating of sauce.
- Reference: The mixture in the pan appears smooth and glossy, with a rich, deep chocolate hue indicating it is well-combined. A swirling pattern is created by the wooden spoon being dragged through the mixture, suggesting a thick consistency that holds shape momentarily before settling back into a flat surface. The reflective sheen on top signifies a high fat content, possibly from chocolate or butter, and the lack of any lumps or graininess implies that the ingredients have been thoroughly melted and integrated.

#### Sample 157 — Before

- Similarity: 0.3531
- Prediction: The cloth appears to be in the hands of a person, with a smoky complexion, indicating it is in the process of being washed. The cloth's surface is slightly damp, suggesting that it may have been soaked for a long time. The person's hand is positioned in the middle of the cloth, pointing to the direction of washing.
- Reference: The sink appears moderately used with visible water droplets around the basin and a few soap suds clinging to the surface, indicating recent activity. A standard silver faucet with a single handle is situated over the sink, slightly askew to the right, suggesting it has been handled recently. The stainless-steel basin has a dull sheen, with some areas reflecting light more than others due to the uneven distribution of moisture. A yellow sponge is resting at the corner, and a bottle of dish soap is within reach, signifying a dishwashing task either just commenced or paused momentarily.

#### Sample 158 — Before

- Similarity: 0.3429
- Prediction: The table appears to be in a state of disarray, suggesting that it has been placed in the middle of a busy kitchen or dining room. Its surface is cluttered with a variety of items, including dishes, dishes, and utensils, which are likely to have been placed on the table prior to the camera's close-up. The table is positioned in the center of the frame, indicating that there is a lot of room for the table to move around. There are several objects in the background, including a tablecloth, a chair, and an umbrella.
- Reference: The orange rests on a smooth, matte surface, likely a wooden table. Its glossy skin reflects a muted light, emphasizing the deep, sun-kissed hue typical of ripe oranges. There are slight imperfections visible on its skin, perhaps a small scar or two, and minute, pitted details, reminding the viewer of its organic nature.

#### Sample 160 — Before

- Similarity: 0.4490
- Prediction: The rag appears to be soaked in soapy water, indicating it has been washed. Its surface is slightly damp, suggesting it may be wet or damp. The cloth's texture is reminiscent of a sponge, with a thin layer of soapy residue on the surface of the rag. The person's hand is positioned in the middle of the cloth, suggesting that it is still wet.
- Reference: The kitchen sink area is cluttered with various dishes and utensils. A person's arms are visible, with their hands engaged in adjusting the faucet, perhaps in preparation for dishwashing. The water is running, and there's a visible stream flowing from the tap, indicating that cleaning activities are in progress. The left sink basin is filled with water, while the right one contains several submerged items, possibly soaking. On the counter, a white dish rack is loaded with a stack of clean white plates, along with other kitchen tools and utensils that seem freshly washed and are left to dry.

#### Sample 161 — Before

- Similarity: 0.4333
- Prediction: The bag appears to be in the hands of a person, with a hand in the middle of the frame, suggesting that the person is attempting to open the bag. The bag's interior is cluttered, indicating that the bag is not yet fully closed, and there is no indication of the person's intent to open it.
- Reference: The image reveals the interior of a cylindrical bin, which appears to be a washing machine drum, with a textured white exterior and a dark, shadowy interior. The rim of the drum is partially illuminated by a striking pink and white light source, creating a stark contrast with the darkness inside. A pair of hands, protected by bright yellow rubber gloves, reaches into the drum, suggesting the commencement of a task. The reflection on the drum's surface indicates a nearby metallic object, possibly a utility that is within the vicinity of the bin.

#### Sample 162 — Before

- Similarity: 0.4885
- Prediction: The jar appears to be in the hands of a person with a hand on it, indicating that someone is attempting to open it. The lid is partially open, suggesting that someone has just opened the jar. The contents of the container are clearly visible, including a handful of dried fruit, which appears to have been thrown into the container. The container's surface is cluttered, suggesting there may be a variety of items in the container, such as fruit, vegetables, and other items.
- Reference: A hand is extending towards a cluttered dish rack, reaching for a large, black ceramic mug. This action seems to be part of an ongoing task, possibly related to organizing or cleaning the kitchen area. The mug appears to be substantial in size, suggesting it is intended for generous servings of beverages. The dish rack is filled with various kitchenware, including plates, bowls, and a vividly colored silicone lid, indicating a mix of cleaning and storage functions. The presence of the hand suggests that someone is in the midst of kitchen duties, possibly tidying up after a meal.

#### Sample 163 — Before

- Similarity: 0.3359
- Prediction: The hand is positioned in the middle of a kitchen counter, with a knife in the center of it, pointing to the kitchen counter. Its shape is reminiscent of an open kitchen drawer, with the handle pointing downwards, indicating a position for the hand to grasp. The person's hand appears to be in a hurry, suggesting that the hand is in the process of removing the knife from the counter.
- Reference: The tablecloth is captured mid-motion, suggesting that it's in the process of being unfolded or placed. Its edges can be seen fluttering, with one corner appearing closer to the viewer's perspective. The cloth's texture and pattern are not fully discernible due to the action's swift nature and the image's blur. The majority of the tablecloth remains bunched up or folded, indicating that the unfolding has just begun.

#### Sample 164 — Before

- Similarity: 0.4874
- Prediction: The mixture appears to be in the early stages of mixing, indicating that it's not yet fully incorporated. The texture of the mixture is reminiscent of a flour mixture, with a light, slightly lumpy consistency, suggesting that the ingredients are still a little moist. There is a slight smudge on the surface of the dough, which may indicate that there's still some work to be done.
- Reference: A hand is immersed in a clear glass mixing bowl containing a mixture of flour and a brown substance, likely a spice or flavoring. The fingers are splayed, indicating the beginning of a mixing process. The flour appears to be untouched except for the area around the hand where the ingredients are starting to blend. The texture of the mix looks powdery and dry, characteristic of flour that has not yet fully absorbed any wet ingredients.

#### Sample 166 — Before

- Similarity: 0.4374
- Prediction: The cloth appears to be in the hands of a person, with a slight smirk on its face, indicating that it has just been washed. The cloth's surface is slightly damp, suggesting that there may be a bit of moisture present in the cloth, which is likely a sign that the cloth is still wet. The fabric's texture is reminiscent of sandpaper or mud, which indicates that it may have been soaked in water for a long time.
- Reference: The bottle appears almost centrally placed on a wooden surface, lying on its side with the cap partially obscured by the hand of a person. This person's hand is also grasping a sponge or cloth, hinting at a cleaning activity possibly having just occurred. The bright red cap of the bottle is not fully tightened, suggesting either recent use or preparation for use. Surrounding the bottle are various other cleaning supplies, including a clear plastic bottle and a green bottle with a label, creating a cluttered but utilitarian atmosphere.

#### Sample 170 — Before

- Similarity: 0.2948
- Prediction: The kitchen sink appears to be in the middle of a kitchen counter, with a large bowl containing a wide variety of food items, including rice, beans, and vegetables. The sink's surface is cluttered, indicating that there is still a lot of work to be done. The kitchen counter appears to have been partially emptied, suggesting that there may have been a bit of work involved. There is a thin layer of paper on the bottom of the sink, which indicates that there has been some sort of work going on. There are several other items on the counter, including a plate, a bowl, and a spoon.
- Reference: A hand is captured in the midst of a dynamic action, positioned above a plate of freshly sliced tomatoes, holding a dual-sectioned spice shaker with a clear body, revealing two separate compartments containing white and darker granules, presumably salt and pepper. The motion is frozen in time, with a small mound of the darker spice poised on the edge of the shaker, suggesting that some of the contents have already been dispensed onto the tomatoes. The scene is indicative of seasoning in progress, with the intent to enhance the flavor of the tomatoes.

#### Sample 171 — Before

- Similarity: 0.4178
- Prediction: The pan appears to be in the middle of a cooking process, indicating that there is still a lot of work to be done. The pan's surface is covered with a thin layer of water, which indicates that the pan has been simmering for a long time, resulting in a boil that appears to have reached a boiling point. The water's consistency is a bit sticky, suggesting that it may be a little too hot for the pan to handle.
- Reference: The oat appears to be somewhat settled in the pan, suggesting that it may have been recently poured in or has been resting for a while. The texture and spread of the oat across the surface indicate that it might be uniformly distributed, with very minimal clumping or clustering. There are subtle variations in the color and density of the oats, indicating that they are likely raw and uncooked. No overt signs of movement or agitation can be discerned from this particular frame.

#### Sample 174 — Before

- Similarity: 0.4280
- Prediction: The vegetables appear to be in the early stages of cooking, indicating that they've been preparing for a long time. They're clumping together, suggesting they're still in the process of cooking. The texture of the vegetables appears to be a mixture of green and brown, with hints of a light brownish hue, suggesting that they may be ready to be cooked.
- Reference: The colander is held at an angle, allowing viewers to peer inside and see its contents. Inside the colander, a mix of beans in various colors - ranging from yellow and white to deep red and brown - is prominently displayed. Droplets of water can be inferred, suggesting that the beans have been recently rinsed or washed. Surrounding the colander are various kitchen items and ingredients, creating a lively culinary scene. The person's hand grips the colander's handle firmly, suggesting an intention to shake or move it.

#### Sample 180 — Before

- Similarity: 0.3866
- Prediction: The pizza appears to be in a medium-sized bowl, with a thin layer of cheese embedded in the center. Its surface is slightly uneven, suggesting that it may be a little too thick, but it's not necessarily a good choice for a pizza. The crust is a light brown, indicating that it hasn't yet reached the desired consistency. The toppings are scattered across the surface of the pizza, implying that they've been sprayed with olive oil.
- Reference: The tomato is depicted in a relatively unaltered state, with a spoon resting against a round flatbread that has a smattering of tomato sauce in the center. The sauce appears freshly spread, with a vivid red hue and discernible chunks, indicating the sauce may be homemade or chunky in style. The spoon, with a hint of sauce on its surface, suggests the action of spreading has just occurred. The sauce is not evenly distributed, with a heavier concentration towards the center and mere smears and dollops radiating outward, implying a hurried or imprecise application.

#### Sample 182 — Before

- Similarity: 0.3752
- Prediction: The floor appears to be in a state of disarray, with a smoky hue, suggesting a person's presence. The surface appears to have been swept away by a hand, indicating that the person is attempting to remove it from the floor. There is a slight movement in the room, suggesting that the floor is being swept back and forth.
- Reference: A clear glass container, possibly a laundry detergent dispenser, is upturned, with its contents seemingly in the process of being poured out, although the liquid is not visible. The container is held aloft by a person whose arms and lower body are visible, but the upper body and head are out of the frame. Below, to the right of the washing machine, lies a blue box of detergent, resting on its side. The washing machine door is open, revealing a glimpse of colorful clothes inside, but the focus is not on the clothes at this moment.

#### Sample 183 — Before

- Similarity: 0.4308
- Prediction: The hob appears to be positioned on a stovetop, with a smoky surface, suggesting a recent cleaning process. The surface of the hob seems to be slightly damp, indicating that there may be a small amount of soap or soap residue on the surface. There is a visible hand-held device indicating the presence of soap residue, which could indicate a cleaning process is underway.
- Reference: The table appears to be a part of a kitchen counter. On its surface, there are multiple objects: a set of stove burners, a dish rack filled with clean dishes, and a sink next to the dish rack. There is also a piece of meat, possibly ham, placed on a green cutting board. Adjacent to these items, a person's hand can be seen holding a cloth, indicating an action, possibly wiping or cleaning. There's a water bottle near the stove and some other objects near the sink. The table appears to be made of a white material, possibly a type of stone or laminate, and has a smooth surface.

#### Sample 185 — Before

- Similarity: 0.3726
- Prediction: The microwave is positioned on a kitchen counter, with its lid open, indicating that it's ready to be used. The interior of the microwave appears to be in a state of transition, suggesting that there's still a lot of work to be done. There's a person's hand in the middle of the kitchen, presumably preparing a meal or preparing for a cooking session. The microwave's interior is cluttered with a variety of items, including a pot, a bowl, and a dish.
- Reference: The oven’s digital display is highlighted in bright red, showing a temperature setting of 180 degrees, likely in Celsius given the context. This specific reading indicates a moderate baking temperature, commonly used for a wide range of dishes, from baked goods to casseroles. The reflective glass surface of the oven door mirrors the interior racks and elements, hinting at a clean and possibly recently unutilized state. The user's hand, adorned with a fitness tracker, suggests an attention to detail and precision, pressing a button on the control panel likely to adjust the temperature, as indicated by the finger's position.

#### Sample 187 — Before

- Similarity: 0.3002
- Prediction: The kitchen sink appears to be in a state of flux, suggesting that it has been thrown out of its container. The sink's surface is cluttered with a variety of items, including a bowl, a pot, and a dish. The kitchen's lighting is dim, indicating that there may be a sudden movement in the sink.
- Reference: The chicken appears to be in the initial stages of preparation, with a few pieces lying irregularly on a wooden chopping board. The pieces are uneven in size and shape, suggesting they have been roughly chopped, and the texture looks somewhat ragged, indicating a less than smooth cut, possibly due to the use of a non-professional or slightly blunt kitchen knife. The board itself has a few stray chicken pieces scattered about, and there is no sign of any seasoning or marinade on the meat, implying the chicken is plain and possibly recently removed from its packaging.

#### Sample 188 — Before

- Similarity: 0.4785
- Prediction: The hob appears to be in the middle of a cooking process, with a sprinkling of oil on the surface of the hob, indicating that it's about to be cooked. It's positioned in a position that's not yet ready for use, suggesting that there's still a lot of work to be done. There's also a slight movement on the stovetop, which suggests that there may be a bit of cooking going on.
- Reference: The image showcases a stovetop with two visible burners. The one on the left has a clear indicator, showing that its heat setting is on '1', which indicates a low or minimum heat setting. Meanwhile, the burner on the right has a clear digital display, presenting the heat setting at '9', signifying that it's operating at a high or maximum heat level. The overall ambiance of the stovetop suggests a cooking session in progress, with batter being poured into pans, likely for pancakes.

#### Sample 189 — Before

- Similarity: 0.4289
- Prediction: The pizza appears to be in the middle of a baking sheet, with a thin layer of dough surrounding it. Its surface is slightly uneven, suggesting that there may be a small amount of dough on the bottom of the slice. The crust is a light brown, indicating that it's being prepared for baking. The knife's edge is positioned against the edge of the pizza, implying that the knife has been pressed against the surface of the dough.
- Reference: The cake appears to be a crumbly-textured delight, perhaps a streusel or a crumble-topped cake, with a golden-brown surface. A small segment of the cake has been sliced away, revealing a moist, darker interior which contrasts with the crumbly topping. The slice's cut edges are jagged, indicating the cake's dense and rich composition. The cake is placed on a vibrant purple circular plate, and roughly three-fourths of the cake remains intact.

#### Sample 193 — Before

- Similarity: 0.3368
- Prediction: The mushroom appears to be in the process of being chopped, indicating that it is in the early stages of maturing. The knife's blade is positioned at the center of the mushroom, suggesting that the knife has been preparing the meat for cooking. The mushrooms appear to be ripe, with a thin layer of flesh on top, indicative of the preparation of the meat.
- Reference: A wooden cutting board is positioned over the edge of a stovetop, featuring several freshly cut, irregularly shaped pieces of tofu, each exhibiting a spongy texture and a pale cream color, indicative of firm tofu that has not yet been cooked or seasoned. The tofu appears moist, likely from being recently pressed or cut, with small beads of water visible on its surface. The board shows remnants of moisture and small bits of tofu residue, suggesting it has been used to cut the tofu into these sizable chunks.

#### Sample 194 — Before

- Similarity: 0.4869
- Prediction: The bowl appears to be in the middle of a kitchen sink, with a sprinkling of soapy water on the bottom. The water is dripping from the bottom of the bowl, indicating that the water has been drained. The bowl's interior is cluttered with soapy residue, suggesting that there may be a lot of soap in the bowl. There is a slight amount of soap on the surface, suggesting the bowl is still wet.
- Reference: The saucepan is in the midst of a cleaning process, with water being poured into it, likely to loosen and remove the remnants of a meal. The pan appears to have had a soup or a stew, as evidenced by the liquid and bits of food clinging to its sides. Suds form on the surface, indicating the presence of soap, which is being added from a green bottle held by the individual cleaning it. The pan is tilted, allowing the water and soap to mix and reach all parts of the interior.

#### Sample 196 — Before

- Similarity: 0.4546
- Prediction: The paper appears to be in the hands of a person with a hand on it, indicating that someone is preparing to open it. The paper's surface is a dark brown color, suggesting that it may be a light-colored piece of paper. The person's hand is positioned on the edge of the paper, suggesting a slight movement, and the paper is likely to be folded or folded.
- Reference: The bag appears to be in a semi-folded state, with the top part being held by a hand, suggesting an ongoing action. The bag's label and some of its contents are visible, suggesting it might not be fully closed or sealed. The texture and wrinkles on the bag's surface indicate that it's not in a pristine or straightened condition, and there's some degree of manipulation that has already occurred.

#### Sample 197 — Before

- Similarity: 0.4821
- Prediction: The kitchen counter appears to be positioned in a position where it's likely to be placed in the middle of a kitchen counter. It's positioned on a counter with a white surface, indicating that there is a lot of space on the counter. The counter's surface is slightly tilted, suggesting that there may be a bit of room on it. The countertop appears to have been placed on top of the counter, possibly to serve as a storage space for food or other items.
- Reference: A pot with a steamy lid sits atop a gas stove, indicating something is being cooked. The stovetop is stainless steel and reflects the surrounding items, including another pot and a grater. The kitchen counter appears messy with a spill near the stovetop, and various kitchen tools are strewn about, including a grater, a pair of tongs, and a bottle, possibly of oil or vinegar. A person's arm is in motion, wiping the counter with a white paper towel, suggesting an attempt to tidy up. The blurred motion of the hand implies swift movement, likely in the midst of cleaning.

#### Sample 198 — Before

- Similarity: 0.4871
- Prediction: The towel appears to be in a kitchen sink, with a spherical shape, indicating it has been placed in the kitchen. It is positioned in the middle of the kitchen counter, with the handle pointing downwards, suggesting a position for the towel to be placed. The towel's surface is a dark brown color, suggesting that it may have been placed on a table or counter before being placed on the towel. The cloth's texture is reminiscent of a paper towel, suggesting it may be a type of paper towel.
- Reference: The bowl in this frame is positioned near several kitchen tools and gadgets. Adjacent to the bowl, a red bag, which appears to be holding a powdery substance, is positioned upright. The top of the bowl is exposed, suggesting that the contents (if any) inside are visible. Surrounding the bowl, there's an assortment of items, including a sandwich press, a white controller, and a radio, among other things.

#### Sample 203 — Before

- Similarity: 0.3422
- Prediction: The jar appears to be empty, with a sprinkling of water on the bottom, suggesting that it has been drained. The bottle's lid is positioned in a position that indicates it is in the process of being emptied, indicating that there is still room for the jar to remain. The container's surface is slightly tilted, suggesting a gradual movement of the bottle, which is likely a sign that the lid is about to be removed.
- Reference: The squash is being held in the left hand of the person, with the focus on its bottom part, which is nestled securely in the palm. The squash appears to be a common variety, with a smooth, bright outer skin, suggesting it's ripe and ready for consumption or cooking. The hand gripping it is slightly tilted, indicating either the beginning or the end of a movement. The person’s thumb and fingers are not applying much pressure, implying a gentle touch, possibly to check its firmness or to move it without causing any bruising.

#### Sample 204 — Before

- Similarity: 0.4685
- Prediction: The surface of the oven appears to be in a state of flux, indicating that there is a significant amount of light in the room. The light source is visible, suggesting that there may be a slight movement in the oven or oven. The surface appears to have been sprayed with a light-colored liquid, possibly a mixture of flour and baking powder, which could indicate that the oven is not yet fully cooled.
- Reference: The light appears to be brightly illuminating the space, casting a strong and focused glow on the wall. The intensity of the light creates contrasting shadows, especially in the corners where the walls meet. The presence of the light seems to emphasize the texture of the wall, revealing any minor imperfections or blemishes present.

#### Sample 208 — Before

- Similarity: 0.4862
- Prediction: The sink appears to be in the middle of a kitchen sink, with a sprinkling of soapy water on the surface. The sink's surface is cluttered with soapy residue, indicating that there is still a lot of soap left on the sink. There is a thin layer of soap on the bottom of the sink, suggesting that there may be a bit of soap in the sink or a small amount of soap spilled onto the sink surface.
- Reference: The wooden spoon appears partially submerged in a sink full of sudsy water, with its handle pointing upwards and angled slightly to the right. The spoon's bowl is visible above the waterline, reflecting light and revealing its smooth, curved interior. The handle, stained darker towards the end, suggests frequent use, indicating that this utensil has been part of many cooking processes. Surrounding the spoon are a plethora of dishes and utensils, suggesting an active kitchen environment.

#### Sample 210 — Before

- Similarity: 0.4235
- Prediction: The chopping board appears to be in a state of flux, indicating that it has been recently washed. The surface of the board is slightly damp, suggesting that it may have been sanitized, possibly by a hand. The blades are visible, suggesting a thorough cleaning process is underway. There is a noticeable amount of soapy water on the board, suggesting it may be abrasive.
- Reference: The image captures a partially translucent bar of soap that has been used to some extent, evident from the smoothed edges and rounded corners. It rests against the vivid green surface of a plastic cutting board, with suds and water droplets scattered across the board's surface, indicating recent or ongoing washing activity. The bar of soap appears slick and wet, reflecting the light in the room, which enhances its glossy appearance. It's held firmly by a person's hand, suggesting a deliberate action of cleaning or scrubbing is taking place.

#### Sample 211 — Before

- Similarity: 0.4177
- Prediction: The cloth appears to be wet, indicating it is in the process of being washed. Its texture is reminiscent of a sponge, with a smoky texture and a light-colored hue. The cloth's surface is slightly damp, suggesting it may have been soaked in soap or water for a few minutes. The person's hand is visible, suggesting that the cloth is still wet.
- Reference: The sink is in a state of disarray with a single carrot peel resting on the wooden counter, indicating recent use. Water splashes and droplets are scattered around the sink area, and on the metallic surface, signifying that it has been recently rinsed or used. The sink itself is a stainless steel dual-basin with the right side featuring a garbage disposal cover. The basin is dry, and there are no dishes, soap, or sponges within it, suggesting that a cleaning activity may have just commenced or concluded. A person's hands are visible, one holding a damp rag, which is poised as if in the middle of a wiping motion, suggesting that cleaning is underway.

#### Sample 212 — Before

- Similarity: 0.3361
- Prediction: The door appears to be open, with a gaping hole in the side of the door, suggesting that the door is open. The door's hinges appear to be partially closed, indicating that there is a slight movement in the process of opening the door. The surrounding area is cluttered, suggesting a gradual movement, which may be indicative of a person's handling of the item.
- Reference: The image shows a digital oven timer with the display clearly visible against a stainless steel backdrop. The timer is set at a specific time, though the exact digits are not clearly discernible due to the angle and distance. The display is illuminated in a cool blue light, indicating that the oven is active or in the process of being set. The digits appear to be stable, with no visible blinking that would suggest the time is being adjusted at this moment. The user's hand is poised near the controls, suggesting that they have just interacted with the timer or are about to.

#### Sample 216 — Before

- Similarity: 0.4122
- Prediction: The pot appears to be in the middle of a kitchen sink, with a handle pointing downwards, indicating that it has been placed in a position where it can be easily accessed. The lid is positioned on top of the pot, suggesting that it is in the process of being placed. The pot's surface is slightly tilted, suggesting a slight tilt. The surrounding area is cluttered with other items, including dishes, dishes, and utensils.
- Reference: The coffee appears to be freshly brewed, exhibiting a dark, rich hue characteristic of a robust espresso shot. It's settled into a classic espresso cup, the surface smooth and undisturbed, with a slightly reflective sheen indicating its hot, liquid state. The cup, with its handle to the left, suggests that it has just been placed on the mat and the brewing process has recently concluded. The absence of crema, the creamy froth on top of an espresso, could imply either the espresso has settled a bit or the coffee's crema layer was thin to begin with, which can be indicative of the coffee's strength or the brewing method used.

#### Sample 222 — Before

- Similarity: 0.4381
- Prediction: The cloth appears to be in the hands of a person, indicating that it is in the process of being washed. The cloth's texture is reminiscent of mud or mud, with a slight hint of water, suggesting that the cloth is still wet. The person's fingers are pointing at the cloth, which appears to have been soaked for a long time, implying that it has been soaking for some time.
- Reference: The sponge appears heavily saturated with water, indicated by its swollen size and the darkened coloration, a common sign of absorption. It's being compressed by a firm grip, causing a clear stream of water to be forcefully expelled, evidenced by the droplets in motion around the sponge. This action also reveals the sponge's porous texture as the pressure pushes the water out through its many cavities, conforming to the shape of the hand that is squeezing it.

#### Sample 225 — Before

- Similarity: 0.4390
- Prediction: The blender is positioned on a counter in a kitchen, with a hand on the handle, suggesting that it's in the middle of a cooking process. The blender's lid appears to be open, indicating that the blender is in the process of preparing food. The user's hand seems to be holding the blender, which is likely preparing a batch of food. There's no indication of the blender itself being in use, but there's a slight movement of the blades, suggesting the blender may be in use for a short period of time.
- Reference: The mixture presents a vivid yellow hue, likely indicative of egg-based ingredients, with visible streaks of white and patches of different consistencies, suggesting the initial incorporation of ingredients. There is a discernible unevenness, with some areas appearing more liquid and others showing soft peaks, possibly from an uneven mixing speed or the starting phase of ingredient integration. The surface reveals air bubbles being folded into the blend, a sign of the mechanical action from the beaters beginning to aerate the mixture.

#### Sample 231 — Before

- Similarity: 0.3763
- Prediction: The onion appears to be partially ripe, indicating that it has been partially sliced. It is positioned in the middle of a kitchen counter, with a small portion of the onion positioned on top of it. The person's hand is firmly grasping the onion, suggesting that it may be preparing to eat.
- Reference: The plastic bag appears to be tightly sealed with its contents under slight pressure, as evidenced by the bulging nature and rounded edges at the top. The fingers of the hands pulling at the bag suggest the beginning of an opening action, with the plastic demonstrating a degree of tension and resistance. This tension is visible in the slight creases and stretched appearance around the areas where the fingers make contact. The bag is translucent, revealing a glimpse of the round, light-colored objects inside, likely potatoes, packed closely together.

#### Sample 232 — Before

- Similarity: 0.3594
- Prediction: The blender is positioned in the middle of a kitchen counter, with a hand on the handle, indicating that it has been placed in a position where it can be easily accessed. The blender's lid is partially open, suggesting that it is in the process of removing the lid from the blender, which is likely to be in use for at least a few minutes. The blades of the blender are visible, with the blades pointing downwards, suggesting a gradual movement.
- Reference: The ingredient in the bowl appears to be a thick, vividly yellow mixture, indicative of a batter infused with either a generous amount of egg yolk or another yellow coloring component such as turmeric or saffron. It's glossy and smooth on the surface, suggesting that it has been well mixed to incorporate air, which is often a desired quality in batters for leavening purposes. The consistency is uniform without any visible lumps, implying that the dry and wet ingredients have been thoroughly combined.

#### Sample 233 — Before

- Similarity: 0.3707
- Prediction: The towel appears to be in the hands of a person with a hand on it, indicating that it is in the process of drying. The towel's surface is slightly exposed, suggesting that it may be a light-colored towel, possibly a wicker towel, or a dish towel. The cloth's texture is reminiscent of an oiled towel, suggesting a delicate texture. The fabric's hues are muted, suggesting it may have been washed before drying.
- Reference: The plate is being held in a person's right hand, slightly tilted towards the camera, and it is almost entirely empty except for a few minor specks, possibly crumbs. The person's arm is extended towards a table that has a decorative tablecloth with a geometric circular pattern. The lighting is warm, suggesting an indoor setting, and the plate has a visible design along its rim, featuring a narrow, darker border that could be an ornate pattern or a manufacturer's mark.

#### Sample 234 — Before

- Similarity: 0.4661
- Prediction: The table appears to be in a state of transition, suggesting a gradual movement. The surface of the table is slightly tilted, suggesting that it's positioned at the center of the frame, indicating that the table has been placed in the middle of a room. The table's surface appears to have been placed on a flat surface, possibly a table or a counter, implying a position for the table to be placed. The person's hand is positioned on the table, suggesting they're preparing for a meal.
- Reference: The mat lies in partial view, a blur of tangerine hues cast upon its textured surface, suggesting a fabric with a likely cotton blend, its edges curled upwards, revealing its use. The corner closest to the viewer is lifted, caught in mid-motion, indicative of the initial stage of folding. It's set against a background of kitchen chaos—pots and pans in disarray, containers of varying sizes scattered atop a counter—each object softly distorted by the swift movement captured in this frame.

#### Sample 238 — Before

- Similarity: 0.3952
- Prediction: The bottle appears to be in the hands of a person, with its contents positioned on a plate, suggesting that the person is preparing to open it. The bottle's contents are clearly visible, with the lid positioned in the middle of the bottle, indicating that the bottle is in the process of being opened. The person's hand is likely holding the bottle in a hands-free motion, implying that they are attempting to open the bottle.
- Reference: A glass jar, nearly full of white flour, is being tilted over a large mixing bowl, allowing a gentle cascade of flour to fall into the bowl. The flour appears fine and powdery, suggesting a soft, sifted texture. It forms a small mound within the bowl, and there's a visible dusting of flour escaping into the air, reflecting the light and creating a soft haze around the jar's opening. The flow from the jar is steady but controlled, indicating a careful pouring motion by the person handling the ingredients.

#### Sample 240 — Before

- Similarity: 0.4811
- Prediction: The soup appears to be in the middle of a cooking process, indicating that it's in the early stages of cooking. It's a medium-sized soup, with a slightly thick consistency, suggesting that the ingredients are still being stirred. The texture of the soup seems to be a mixture of flour and water, which may indicate that the soup has been simmering for a long time, possibly a few minutes.
- Reference: The curry appears to be in its initial stages of cooking. The ingredients in the pot are partially submerged in liquid, hinting at a simmering process. The consistency at this point looks more broth-like, with visible solids and pieces floating around. There's a notable translucence to the liquid, suggesting that the curry hasn't thickened or fully integrated its components yet.

#### Sample 241 — Before

- Similarity: 0.3567
- Prediction: The kitchen sink appears to be in a state of flux, indicating that it has been sanitized. The sink's surface is cluttered with a variety of items, including dishes, dishes, and utensils, all of which appear to have been placed on the sink. The bowl is positioned in the middle of a kitchen counter, suggesting that there is a lot of work to be done. There are a number of items in the sink, including a dish towel, a plate, and an ice cube tray.
- Reference: A red soup ladle with a long handle is resting inside a deep, circular white bowl. The bowl is placed on a white paper plate that shows remnants of food particles, suggesting a meal was recently consumed. Adjacent to the bowl is a clear glass, about a quarter full with a yellowish liquid, possibly a beverage. The table setting includes a folded yellow napkin under the bowl and a portion of a white paper plate visible in the foreground, suggesting the presence of another dining space opposite the viewer.

#### Sample 242 — Before

- Similarity: 0.4960
- Prediction: The jar appears to be in the hands of a person, with a hand on the lid, suggesting that someone is attempting to open the jar. The lid is positioned in a horizontal position, indicating that it is in the process of being opened. The contents of the container appear to be a mixture of ice, water, and a liquid, which suggests that the lid has been partially opened.
- Reference: The image reveals a translucent package with a green flip-top lid nestled among various kitchen items on a yellow and white checkered shelf liner. It rests partially on a white cylindrical container to its right and is surrounded by an array of other objects, including a green fruit, a striped cup, and assorted ceramics. The package's lid appears firmly closed, and its position on the shelf suggests it hasn't been moved recently, as indicated by the lack of space around it for easy retrieval.

#### Sample 243 — Before

- Similarity: 0.4914
- Prediction: The paper appears to be in the hands of a person who is attempting to open it. The paper is positioned on a table, with its edges exposed, indicating that it is in the process of being opened. The person's hand appears to have grasped the paper, suggesting that the person is preparing to open the paper.
- Reference: The baking paper appears to be in the initial stages of folding, with multiple unevenly torn sheets scattered across a kitchen counter. The surface of the counter is cluttered with various items including kitchen utensils, a blue kettle, a sandwich toaster, and a bag of what seems to be cookies or crackers. One larger piece of baking paper is partially folded in a somewhat haphazard manner, with its edges not aligning neatly, indicating a casual or rushed approach to the task at hand.

#### Sample 244 — Before

- Similarity: 0.4599
- Prediction: The stainless steel spoon appears to be in the hands of a person attempting to clean it. The spoon's handle is positioned in the middle of the kitchen counter, with a handle pointing downwards, indicating that it is in the process of being washed. There is a visible stream of soapy water on the spoon, suggesting that it has been soiled.
- Reference: The potato peeler is gripped firmly in a person's hand, its metallic surface partially obscured by a froth of soap suds, evidence of a thorough scrubbing in progress. Water cascades from the tap, splashing around the utensil, enhancing the sheen on its curved peeling blade. The spongy texture of the yellow and green sponge is saturated with water, making it swell against the steel structure of the peeler.

#### Sample 248 — Before

- Similarity: 0.2357
- Prediction: The door appears to be open, with a gaping gap between the door handle and the door frame, suggesting that the door is open or closed. The interior of the door seems to be partially open, indicating that there is still room for the door to open.
- Reference: The light switch appears to be in an inactive state, with the toggle buttons in a neutral position, not pressed down. The ambient lighting in the room remains dim, indicating that the electrical circuit connected to the light source is incomplete. The shadow cast on the wall by the hand and the switch assembly suggests a faint light source elsewhere in the room, not from the intended fixture, and the overall atmosphere is one of low illumination.

#### Sample 252 — Before

- Similarity: 0.3131
- Prediction: The sandwich appears to be partially sliced, with a thin layer of sliced fruit on the side. A hand is attempting to slice through the sandwich, indicating that it is in the process of being sliced. The sandwich's texture is reminiscent of a slicing knife's edge, suggesting a smoother texture. The surface of the sandwich is slightly uneven, suggesting that there may be a small amount of food on the sandwich.
- Reference: The cake presents as an almost complete ring, set against a decorative lace doily. It appears to be a dense, golden-brown bundt cake with a moist-looking crumb, suggesting a rich and buttery composition. A single slice has been neatly removed, placed back in its original position, slightly askew to indicate it has been cut. Crumbs dot the doily around the cake's base, and the inner circle of the bundt shape is clear, revealing the doily's intricate pattern.

#### Sample 253 — Before

- Similarity: 0.2888
- Prediction: The frying pan appears to be in the middle of a cooking process, indicating that it has been frying for a long time. The pan's surface is covered with a thin layer of grease, suggesting that it may have been preparing for cooking. The surface of the pan is slightly damp, suggesting it may be a bit wet. The knife's edge is visible, suggesting a gradual movement of the blade, which could indicate that the pan has just started cooking.
- Reference: The rag, mostly blurred due to motion, is clutched by a hand and seems to be in the process of wiping or cleaning. The fabric appears to be somewhat damp, reflecting light in certain areas, indicating moisture. There's a sense of dynamic movement in the rag's position, with the fabric bunching up slightly under the pressure of the hand.

#### Sample 255 — Before

- Similarity: 0.4381
- Prediction: The microwave appears to be in a closed position, with its lid open, indicating that it is in the process of being opened. Its interior is cluttered with a variety of items, including dishes, dishes, and utensils. The microwave's exterior is dimly lit, suggesting that it may be a microwave oven or microwave oven. The interior of the microwave has a chrome-plated handle, suggesting a hand-held device.
- Reference: The image captures a hand reaching out towards an area, presumably where the switch is located. The fingers are extended, suggesting intent to interact with something, possibly to activate or deactivate it. The background reveals a kitchen setting with various appliances, but the main focal point appears to be the action of the hand. The exact state of the switch itself is not immediately clear from this angle, but the intentionality of the hand movement suggests that it is about to engage with it.

#### Sample 258 — Before

- Similarity: 0.3739
- Prediction: The kitchen sink appears to be in the hands of a person, with its handle positioned in the middle of the sink, indicating that it has been sanitized. The person's fingernails are positioned on the sink's edge, suggesting that they've been agitated. The sink surface appears to have been dampened, with a thin layer of soapy water spilled onto the sink surface. The hand's fingers are visible, suggesting a thorough cleaning process is underway.
- Reference: The rectangular dish, positioned in the lower left quadrant, displays a well-used appearance with burnt-on residues covering its inner surface. A smattering of droplets surrounds the pan, suggesting recent attempts at cleaning or soaking. The wear and stains indicate that the dish has likely been through a cooking process that involved high heat, such as roasting or baking, which has resulted in the caramelization of food remnants adhering persistently to the metal.

#### Sample 267 — Before

- Similarity: 0.2842
- Prediction: The avocado appears to be in the hands of a person attempting to peel it. The avocado's skin is exposed, suggesting that it is in the process of peeling, indicating that the person is preparing to peel the avocado.
- Reference: The sweetcorn is sealed within a can, the top of which is intact and unopened. It sits on a white cutting board, surrounded by the remnants of previously chopped red onions. The can's label faces upwards, displaying its contents to the viewer, and no tools are present to suggest the beginning of an opening process. The environment suggests the preparation of a meal, likely involving the sweetcorn as a topping, indicated by the presence of two pizzas in the background awaiting further ingredients.

#### Sample 268 — Before

- Similarity: 0.4922
- Prediction: The tray appears to be in the hands of a person, with its handle pointing downwards, indicating that it is in the process of being rinsed. Its surface is slightly damp, suggesting that the water has been dripping from the bottom of the tray, resulting in a sticky residue. The tray's surface appears to have been washed with soap and water, suggesting it may have been soaked for a few minutes.
- Reference: The chopping block is positioned directly under the faucet, with a steady stream of water pouring onto its surface. It's held at a slight angle, allowing the water to run off towards the bottom left corner, indicating that the block is being rinsed. The vivid green color of the block is made more intense by the wetness, and water droplets are visible, bouncing off the surface. The person's hands grasp the block firmly, one hand on each side, fingers extended, suggesting the initial phase of cleaning. The sink appears to be a standard stainless steel model, and the presence of other washed items in the drying rack, including a white mug and a plate with a green sponge, suggests a typical kitchen setting.

#### Sample 272 — Before

- Similarity: 0.4056
- Prediction: The saucepan appears to be in the hands of a person, with its handle positioned in the middle of the kitchen counter. Its surface is covered with a thin layer of soapy water, indicating that it is being washed. The water's abrasions are visible, suggesting that the water has been dripping from the bottom of the saucepan, resulting in a smoky residue.
- Reference: The ladle appears to be partially submerged in water, with its bowl facing downwards, allowing the stream of tap water to flow directly into it. The handle of the ladle is gripped firmly in the person's right hand, with fingers wrapped around it, suggesting that it is either being positioned for washing or is in the initial stages of rinsing. The surrounding area of the sink is cluttered, with various kitchen utensils and cleaning supplies in proximity, indicating an ongoing cleaning task. Bubbles or suds are not visible on the ladle at this stage, which could imply that it has not yet been soaped or is in the process of a preliminary rinse.

#### Sample 273 — Before

- Similarity: 0.3248
- Prediction: The sink appears to be in the middle of a kitchen sink, with a sprinkling of soapy water on the surface, suggesting that it has been soiled. The sink's surface is cluttered with soapy residue, indicating that there is still a lot of soap left on the sink. There is a slight amount of soap on the bottom of the sink, which suggests that there may be a bit of soap residue on the top of the basin.
- Reference: The top appears to be a flat surface, likely made of a dark material, perhaps a type of stone or synthetic countertop material. The image captures a moment where a hand is holding a white mug with a pinkish glowing base, and the contents inside the mug resemble some type of food, possibly dumplings or a similar dish. The surrounding area of the top shows a stove or cooktop with at least two burners, one of which has a dark pan placed on it.

#### Sample 275 — Before

- Similarity: 0.4390
- Prediction: The coffee pot appears to be in the hands of a person, with a hand on the handle, suggesting that the person is preparing to use the pot. The pot's lid is positioned in the middle of the frame, indicating that it has been placed in a position where it can be easily accessed. It is surrounded by a series of nozzles, which indicate that the pot is in the process of being filled with water.
- Reference: The cap burner in this frame is positioned amidst other objects within the vicinity. It seems to be resting securely on the burner base. The reflection and shadow patterns on its surface suggest ambient lighting from above. The cap's edges are distinct, and the inner section shows slight color variations, possibly from usage or lighting effects. The immediate surroundings have other kitchen items, but the cap burner is the focal point.

#### Sample 278 — Before

- Similarity: 0.2193
- Prediction: The dough appears to be in the hands of a person with a knife, indicating that it is in the process of being rolled. The texture of the dough seems to be a mixture of flour and water, suggesting that the dough has been rolled in a particular way. The dough's texture is reminiscent of the texture of an egg, implying that it's a medium-sized dough.
- Reference: The film cling is held within its cardboard package, with only a portion of it being visibly pulled out. The transparent film, as it exits the box, displays some wrinkles and irregularities in its structure, likely due to the extraction process. The edge of the cling film is still connected to the box's serrated cutting edge, suggesting it has yet to be torn off for use.

#### Sample 279 — Before

- Similarity: 0.4756
- Prediction: The microwave appears to be in a closed position, with its lid partially open, suggesting that it is not yet fully closed. It is positioned in the middle of a kitchen counter, with a visible portion of the microwave's interior exposed, suggesting a gradual movement. The kitchen counter appears to have been closed for a few seconds, indicating that the microwave is still open. The surrounding area, including the kitchen counter and the microwave, is likely occupied by a person or a family member, implying that they are engaged in some sort of activity.
- Reference: The cabinet appears partially open, with its door ajar, revealing contents that include a variety of items such as food containers and perhaps small kitchen appliances. The interior shelves are not fully visible, but from what can be seen, they appear to be moderately filled. The cabinet's exterior is white, matching the general color scheme of the kitchen, and it has a handle that is not clearly visible due to the angle of the shot. The blur in the image suggests motion, indicating the cabinet door is in the process of being moved.

#### Sample 280 — Before

- Similarity: 0.4938
- Prediction: The table appears to be in the middle of a kitchen counter, with a white surface that appears to have been placed on top of it. It is positioned in a horizontal position, indicating that the table has been placed in the center of the kitchen counter. The table's surface is slightly tilted, suggesting that there may be a slight movement in the room. The lighting is dim, suggesting a light setting.
- Reference: The toaster is obscured and indistinct, captured in a motion-blurred image, indicating rapid movement either of the toaster or the camera. The blurred lines and smeared colors suggest a swift action taking place. The surrounding environment is a kitchen, with a stovetop visible and various kitchen items in a state of disarray, implying a dynamic scene. The toaster itself is not clearly visible, but it seems to be in the process of being covered or uncovered hastily, as indicated by the position of a hand and a cloth in the foreground.

#### Sample 281 — Before

- Similarity: 0.3639
- Prediction: The table appears to be in a state of flux, with a smoky hue, suggesting a recent change in the lighting conditions. A hand is positioned on the edge of the table, indicating a cursory glance at the table's surface. There is a slight movement in the hand's direction, suggesting that there may be a moment or two before the table is placed on the table.
- Reference: A hand is pressing the nozzle of a spray bottle, emitting a fine mist of detergent onto a white surface. The detergent disperses in small, glistening droplets, creating a slightly irregular pattern due to the angle and pressure of the spray. The light reflects off the droplets, highlighting their presence against the matte finish of the surface. The shadow of the person holding the bottle is cast over the area, suggesting an indoor setting with a light source above.

#### Sample 282 — Before

- Similarity: 0.4949
- Prediction: The garlic cloves are positioned on a cutting board in the middle of a kitchen counter, indicating that they are in the process of being sliced. The skin is exposed, with a thin layer of skin surrounding the cloves, suggesting that they may have been sliced too early. The cloves appear to be ripe, with the skin separating from the skin, suggesting a gradual process of peeling.
- Reference: A translucent, slightly crumpled piece of onion skin rests precariously on the edge of a white cutting board. The board is sprinkled with flecks of freshly chopped green herbs and minute pieces of onion, indicating recent use. A person's hand is caught in motion, with fingers partially open, as they have just released the onion skin. The skin itself catches the light, giving it a slightly glossy appearance amidst the otherwise matte surroundings of the kitchen counter.

#### Sample 285 — Before

- Similarity: 0.4703
- Prediction: The spoon appears to be in the hands of a person, with its handle positioned in the middle of the kitchen counter, indicating that it is in the process of being washed. The spoon's surface is covered with a thin layer of soapy water, suggesting that it has been soaked for a long time. The hand's movements indicate that the spoon is in a state of soaking, implying that there is a slight amount of soap on the surface of the spoon.
- Reference: The lemon squeezer piece is held in a vertical orientation with its lower section submerged in soapy water. It's grasped firmly at its upper end by a hand adorned with a black wrist accessory, suggesting the initiation of the cleaning process. The squeezer's metallic surface is partially visible, reflecting the overhead lighting, and hints of water droplets or residues cling to its curved contours. It's not yet clear how soiled the squeezer is, as the view is obstructed by the water and the hand's position.

#### Sample 286 — Before

- Similarity: 0.4752
- Prediction: The soup appears to be in the middle of a cooking process, indicating that it has been simmering for a long time. Its texture is a mixture of brownish brown, with a slight hint of spice, suggesting that it may be a medium-rare or medium-low-fat content. The soup's consistency is reminiscent of an oil-based soup, implying that it's not yet fully cooked. There's a thin layer of sauce on the bottom of the soup, which suggests that there's still a lot of sauce left.
- Reference: The mixture appears to be a blend of diced vegetables, possibly including yellow bell peppers and tomatoes, which suggest a preparation for a dish that requires sautéing. The vegetables are vibrant and appear freshly cut, showing no signs of browning or overcooking. They are glistening, indicating the presence of oil in the pan which has been used for cooking. The mixture is not yet fully spread out in the pan, as it is being poured from a white bowl, suggesting this is the initial stage of cooking where the ingredients are just starting to heat up.

#### Sample 288 — Before

- Similarity: 0.4177
- Prediction: The sink appears to be in the middle of a kitchen sink, with a sprinkling of soapy water spilling out of the bottom. The sink's surface is cluttered with soapy residue, indicating that there is still a lot of soap on the bottom of the sink. The faucet is positioned near the sink, suggesting that the water has been dripping from the bottom, implying that the sink is a bit soiled.
- Reference: A plate is held under a running tap, with water forcefully cascading over its surface, generating a dynamic spray and causing some foam to scatter. The plate itself appears partially cleaned, as the water's impact has likely dislodged some debris, evidenced by the clearer area on the plate's surface closest to the water stream. The peripheral regions still hold remnants of suds, indicating the cleaning process is not yet complete. A gloved hand grips the edge, suggesting an ongoing manual effort to remove any remaining food particles or stains.

#### Sample 293 — Before

- Similarity: 0.4920
- Prediction: The bowl appears to be in the hands of a person, with its handle positioned in the middle of the kitchen counter, indicating that it is in the process of being rinsed. The bowl's surface is covered with a thin layer of soapy water, suggesting that it has been washed in a sink. The water's odours suggest that the bowl may have been soaked in soap, which is indicative of the presence of soap in the bowl.
- Reference: The colander appears prominently in the upper part of the frame, held by a person's hands. It is angled such that the bottom faces slightly away from the viewer, suggesting that it may have just been picked up or is in the process of being moved. The colander's interior is not fully visible due to its position, but it seems to be empty and clean, without any food particles or residue clinging to the holes. The lighting casts a soft glow on the white surface of the colander, highlighting its perforated pattern and the water droplets clinging to its surface, indicating recent rinsing.

#### Sample 294 — Before

- Similarity: 0.2072
- Prediction: The gas cooker appears to be in a state of flux, with a smoky surface, suggesting a recent change in the cooking process. The burner is positioned on a flat surface, indicating that there is still a lot of work to be done. There is a noticeable amount of dust on the surface of the cooker, suggesting that it may be a bit damp.
- Reference: The towel appears to be a crumpled mass of white fabric, lightly soiled with what could be remnants of food or grease, suggesting recent use in wiping or cleaning. It's held loosely in the hand, with fingers slightly curled around it, indicating a casual or in-between action moment. The texture of the towel seems soft and pliable, showing no signs of stiffness, and the stains are not overly pronounced, indicating that the towel might still be in a usable condition for further cleaning tasks.

#### Sample 295 — Before

- Similarity: 0.4946
- Prediction: The bowl appears to be in the hands of a person, with a hand firmly grasping it, indicating that it is in the process of being washed. The bowl's surface is covered in a thin layer of soapy water, suggesting that it has been sanitized. Its surface appears to have been cleaned, suggesting it is still wet, and its contents appear to be a mixture of soap and water.
- Reference: The strainer is held firmly in one hand, positioned under a running tap with water cascading through its numerous vertical slits. Its white plastic surface is dotted with remnants of food particles, particularly concentrated at the base where they seem to resist the rinse. The wear on the strainer's surface suggests frequent use, highlighted by the contrast of clean water flowing over less pristine areas. The strainer's grid-like interior is clearly visible, acting as a barrier to the larger debris while allowing water to pass through.

#### Sample 297 — Before

- Similarity: 0.4230
- Prediction: The chicken is positioned on a cutting board in a kitchen, with a sharp edge and a thin layer of skin, indicating it is in the process of being cut. The skin appears to be in the middle of a cooking process, suggesting that the chicken has been preparing for a long time. The knife's edge is visible, suggesting a gradual cutting process, and the meat is still a bit raw.
- Reference: The cutting board is held at an angle, with the edge slightly elevated over a pan filled with other ingredients. A single garlic clove rests on the board, and it appears partially crushed, with its papery skin still attached but flayed open, indicating that it has been prepared for mincing or crushing. The garlic’s yellowish hue suggests it's fresh, and there's a visible moistness on the clove, possibly from the garlic juice being released due to the pressure applied. The person's hand is positioned as if they have just finished or are about to continue the crushing process.

#### Sample 298 — Before

- Similarity: 0.2751
- Prediction: The frying pan appears to be in the middle of a cooking process, with a sprinkling of oil on the bottom, indicating that it has been heated. The pan's surface appears to have been sprayed with oil, suggesting that there may be a slight amount of grease on it, implying that the pan is in the process of cooking. The surface of the pan seems to be slightly damp, possibly due to the presence of soap residue, which could indicate that it is still a bit wet.
- Reference: The gloves appear to be durable rubber kitchen gloves, commonly used for washing dishes or cleaning to protect the hands from water and detergents. They are bright yellow, a standard color which suggests their use in household chores. The gloves extend to the mid-forearm, providing ample coverage. In this frame, the glove on the left hand is gripping a white bowl near the sink, fingers curved around the edge, indicating a firm grip. The texture of the gloves seems slightly wrinkled, a characteristic that often occurs when the material is flexed.

#### Sample 301 — Before

- Similarity: 0.4249
- Prediction: The cloth appears to be soaked in a stream of water, indicating that it is being washed. The cloth's surface is covered with a thin layer of soapy water, suggesting that the water has been dripping from the cloth. The person holding the cloth seems to be holding a small amount of the cloth, which appears to have been soaked for a long time. The water's movement is indicative of a water-based solution, implying that the cloth is still wet.
- Reference: The peeler is being held over the sink by a person's right hand. It appears to be positioned horizontally, with the blade facing downwards and water droplets seen on and around it, suggesting that it has been rinsed or is currently being rinsed. The grip of the peeler, seen in a bright green color, stands in contrast to the silvery metallic part, and the tool appears to be in a state of use.

#### Sample 303 — Before

- Similarity: 0.4817
- Prediction: The lid of the bottle appears to be open, with a man's hand grasping it, suggesting that the bottle is in the process of being opened. The bottle's contents are clearly visible, with the lid positioned in the middle of a kitchen counter, indicating that the lid has been opened.
- Reference: The aluminum beverage can is captured in a near-upright position on a wooden table. A person's hand, adorned with a metallic watch, is gently grasping the can from its side, with fingers wrapped around its circumference. There is another circular object on the table, possibly a glass coaster or the can's lid. The table surface has a rich wood grain, with visible streaks and knots, and there's a black mat adjacent to the can.

#### Sample 304 — Before

- Similarity: 0.2721
- Prediction: The kitchen sink appears to be in a state of flux, with a spherical shape that appears to have been partially drained. Its surface is cluttered and cluttered, suggesting that it may be in the process of being emptied or thrown away. The sink's surface appears to contain a variety of items, including a dish towel, a paper towel, and a plastic bag. The camera's focus is on the kitchen sink, which is positioned in the middle of a kitchen counter, indicating that there may be a small amount of food or other items in the sink.
- Reference: The tin presents as a well-used baking dish with signs of extensive wear, indicating a history of repeated culinary ventures. Its surface is mottled with baked-on residues and staining that speak to a rich tapestry of past meals, perhaps sweet or savory dishes that have left their indelible mark over time. The corners and edges of the tin exhibit darker discoloration, particularly pronounced in areas where heat would have been most intense, further testifying to its service in many a heated oven.

#### Sample 305 — Before

- Similarity: 0.2967
- Prediction: The vegetable appears to be in a pot of boiling water, indicating that it has been simmering for a long time. Its texture is reminiscent of a soupy broth, with a hint of salt, suggesting that it may be ready for cooking. The surface of the vegetable appears slightly damp, suggesting it may have been boiled or boiled before being placed on a plate.
- Reference: The countertop is partially visible, composed of a light-colored, solid surface with few distinct features. To the left, there's a stainless steel double sink with one basin empty and the other holding a plastic dish rack filled with kitchen utensils and plates. A solitary, well-used sponge rests on the divider between the sinks. The countertop adjacent to the sink appears wet, possibly from recent cleaning or dishwashing activities, with water droplets scattered across the surface. Visible in the lower right corner is an individual's forearm, lending a sense of scale and human presence to the scene.

#### Sample 306 — Before

- Similarity: 0.4894
- Prediction: The wok appears to be in the middle of a kitchen sink, with a sprinkling of soapy water on the surface. A hand is attempting to clean the wok's interior, indicating it's in the process of being washed. There's a visible stream of soap suds on the bottom of the bowl, suggesting a thorough cleaning.
- Reference: The rolling pin appears to be in the early stages of cleaning, held at a slight angle over a green chopping board, indicating a recent transition from usage to washing. The handles and body of the pin show flour residue, likely from dough preparation, emphasizing its recent use in baking. The surrounding countertop is speckled with flour and water droplets, hinting at the rolling pin's contribution to the kitchen activity. A dishwashing liquid bottle and a clear glass bowl rest near the pin, suggesting preparations for a thorough cleaning.

#### Sample 309 — Before

- Similarity: 0.3661
- Prediction: The chicken is placed in a kitchen sink, with a thin layer of water on the bottom, indicating that it has been washed. The water's surface is slightly damp, suggesting that there may be a bit of moisture present. The chicken's skin appears to be bare, suggesting it may have been soaking for a long time. The camera's focus is on the chicken, which is positioned at a 45-degree angle, with its surface exposed to the water and the surrounding area. The person's hand is visible, suggesting he is attempting to remove the chicken from the sink.
- Reference: In this frame, the metallic tap over the kitchen sink is positioned in a downward angle. The faucet appears to be turned off, as there is no visible flow of water emanating from it. The surface of the tap is reflective, and a chain-like apparatus is attached near its base, possibly serving as a plug mechanism for the sink.

#### Sample 315 — Before

- Similarity: 0.4779
- Prediction: The onion appears to be in the middle of a cooking process, indicating that it is in the process of being sliced. The onion's skin is exposed to the light, suggesting that it has just been sliced and is ready to be cooked. The knife's edge is positioned against the side of the onion, suggesting a close-up view of the vegetable.
- Reference: The peeler in this frame is positioned slightly off-center on the green cutting board, resting next to a partially peeled cucumber. The handle of the peeler, appearing to be made of black plastic, is oriented toward the lower left corner of the image, suggesting it has just been used or is about to be used. There's a noticeable piece of cucumber skin attached to the blade, indicating recent activity. Its blade, which is metallic and has a slot in the middle presumably for peeling efficiency, shines under the kitchen light, contrasting with the green hues of the cucumber and the cutting board.

#### Sample 317 — Before

- Similarity: 0.2950
- Prediction: The bag appears to be in a state of transition, indicating that it has been placed in the hands of a person who is preparing to eat it. The bag's packaging is clearly visible, suggesting that the person is in the process of preparing the bag. The person's hand is positioned in the middle of the bag, implying that they are preparing for a meal.
- Reference: The mozzarella is presented as a mound of shredded cheese, with elongated, irregular strands that suggest a soft and pliable texture. Each piece varies slightly in size, indicative of being hand-grated or roughly processed. The cheese is loosely piled, with some strands dangling off the edges of the pile, and it is being sprinkled onto a circular dough base. The color is a uniform pale cream, characteristic of fresh mozzarella, with no signs of melting or clumping, suggesting it has been recently taken out of its packaging and is at a cool room temperature.

#### Sample 319 — Before

- Similarity: 0.4099
- Prediction: The avocado appears to be freshly sliced, with a thin layer of white flesh surrounding it, suggesting that it has been partially sliced. The texture of the avocado is slightly smoky, indicating that there may be a slight blemish on the avocado's surface, implying that it may not be fully sliced yet. The knife's edge indicates that the avocado has been sliced in a circular motion, suggesting a gradual process of slicing the avocado, which is likely to take a few minutes.
- Reference: The sandwich rests open-faced on a white cutting board with an intricate black illustration, offering a glimpse into the initial stages of preparation. The bottom slice of bread is topped with a layer of green lettuce leaves, crisp and freshly torn, peeking out unevenly from the edges. The top slice of bread is absent, indicating the sandwich maker's process is still underway. Ingredients are scattered around the board: a jar of pickles, a pack of sliced cheese still partly wrapped, and a container of lettuce, suggesting a variety of textures and flavors to be added.

#### Sample 320 — Before

- Similarity: 0.3736
- Prediction: The chicken appears to be in the process of being sliced, with a thin layer of meat embedded in the middle. The meat is sliced into bite-sized pieces, indicating that it has been partially cooked. The skin is a dark brown color, suggesting that the meat has not yet been fully cooked. There are no visible markings or markings on the meat, which indicate that the chicken is still being prepared for cooking.
- Reference: The sweet potato skin appears freshly sliced, revealing a bright orange interior, indicative of a recent cut. The peel segments are irregular in shape and size, scattered haphazardly on the wooden cutting board, some still attached to chunks of the sweet potato flesh. The edges of the skin are slightly curled up, a natural response to being separated from the dense, moist flesh. One can observe the contrast between the rough, textured outer surface of the peel and the smooth, moist inner surface that was against the sweet potato flesh.

#### Sample 324 — Before

- Similarity: 0.4012
- Prediction: The fish appears to be in the early stages of cooking, with a thin layer of meat on top, indicating it's in the process of being cooked. The flesh appears to have been partially cooked, with the skin still slightly charred, suggesting that the fish has been preparing for cooking. The knife's edge is visible, hinting at the beginning of the cooking process, suggesting the fish may be preparing to be cooked.
- Reference: A small portion of sweet potato is visible on a white cutting board. The sweet potato chunk appears freshly cut, with a bright orange interior that stands in contrast to its brown, slightly rough skin. The knife, which likely was used for the cutting, rests next to the potato piece, and it glistens subtly, hinting at its recent use. The way the potato sits on the board suggests it's been placed there momentarily, perhaps after being cut, and there's a certain rawness to its appearance, characteristic of fresh produce.

#### Sample 325 — Before

- Similarity: 0.4638
- Prediction: The onion appears to be partially sliced, with a thin layer of skin and a smoky exterior. A hand is attempting to peel the onion, which is positioned in the middle of a kitchen counter, indicating that it's in the process of being sliced. The onion's skin is still visible, suggesting that it has been slicing for a long time. The knife's edge is slightly slanted, suggesting a sharper cutting action.
- Reference: The kiwi fruit appears freshly cut, its vibrant green flesh exhibiting moisture indicative of recent slicing. Portions of the fruit are intact with the brown, fuzzy skin partially peeled back, revealing the emerald interior speckled with tiny black seeds. The peeled skin curls away from the flesh, suggesting a deliberate and careful effort to preserve as much of the edible portion as possible. The kiwi sits on a cutting board that shows signs of previous use, with moisture and residue from the fruit.

#### Sample 328 — Before

- Similarity: 0.4391
- Prediction: The bag appears to be in the hands of a person, with its contents positioned in the middle of the frame, indicating that the person is preparing to open the bag. The bag's contents are clearly visible, suggesting that the individual is attempting to open it. The person's hand is positioned on the side of the bag, implying that they are holding the bag in their hands.
- Reference: The slice of bread is being held by a person's hand, captured mid-motion as it's moved towards a toaster. The bread appears to be a piece of wholegrain or multigrain toast, with visible seeds and grains throughout its surface, suggesting a health-conscious choice. The hand gripping it seems to be in the midst of an action, likely having just retrieved it from the bread bag resting on the counter. The bread itself is in focus, with the background slightly blurred due to the movement, emphasizing the slice as the central element of the frame.

#### Sample 332 — Before

- Similarity: 0.3829
- Prediction: The oven door appears to be open, with a person's hand in the middle of the door, indicating that someone is preparing to open the door. The door is partially closed, suggesting that the oven is still open. The interior of the oven appears to have been partially opened, suggesting the oven has not yet been fully opened.
- Reference: The freezer drawer is captured in mid-motion, slightly ajar with a gap visible between the drawer and the freezer frame, indicating that it has just begun to close. The edges of the drawer exhibit a matte finish, perhaps due to the cold temperature within, while the contents remain obscured by the blurred motion. The slight angle and position of the drawer suggest a quick, perhaps forceful movement, with the potential for items inside to shift due to the speed of closure.

#### Sample 334 — Before

- Similarity: 0.2730
- Prediction: The box appears to be in a kitchen setting, with a plastic lid and a spherical shape, suggesting a person is preparing to open the box. The box's interior is cluttered, indicating that there is a lot of room for the box to be opened. There are several items on the box, including a tray, a bowl, and an ice cube tray, all of which are visible in the background.
- Reference: A slice of bread is being held in a hand, slightly angled to the side, displaying its golden-brown exterior with slight toasting around the edges. The bread's porous texture is evident, with small air pockets and a gentle crust. The hand is midway through spreading a thick, white, creamy substance, likely mayonnaise or a similar condiment, across the surface of the bread. The spreading is uneven, with more of the substance near the knife edge and less toward the far side, indicating the action is not yet complete. The substance's peaky texture suggests it has a stiff consistency.

#### Sample 335 — Before

- Similarity: 0.3222
- Prediction: The table appears to be in a state of transition, with a white surface and a reflective surface surrounding it. A hand is positioned on top of the table, indicating that someone is preparing to place a new piece of paper on the table. The table is surrounded by a number of other items, including a dish towel, a bowl, and an ice cube tray.
- Reference: The degreaser appears as a white mist, consisting of fine droplets in mid-air, captured as they disperse across the surface in the upper right quadrant of the frame. The motion of the degreaser is dynamic, indicating that it has just been sprayed from the bottle, which is held in the right hand of the individual. The droplets are densest nearest the nozzle, indicating the recent activation of the spray mechanism. Below the area of the spray, the countertop remains visibly dry, reflecting the light from above, suggesting that the degreaser has not yet had time to settle or spread across the surface.

#### Sample 336 — Before

- Similarity: 0.4419
- Prediction: The coffee pot appears to be in the hands of a person who is attempting to clean it. The water flows into the pot from the faucet, indicating that the water has been drained out of the pot, resulting in a sludge-like substance on the bottom. The surface of the coffee pot is covered with a thin layer of soapy water, suggesting that it is being washed. There are no visible marks of soap or soap on the inside of the cup, suggesting a thorough cleaning process.
- Reference: A hand is gripping a piece of cutlery, a fork, under a stream of water flowing from a silver-colored faucet with a slight curvature. The tines of the fork are positioned downwards, perpendicular to the stream, suggesting the initial action of rinsing. Soap bubbles cling to the base of the tines and handle, indicating recent scrubbing activity. The surrounding area is cluttered, with other kitchen items and a purple sponge visible, and a bottle of liquid soap prominently in the background, contributing to the domestic cleaning context.

#### Sample 338 — Before

- Similarity: 0.3719
- Prediction: The pan appears to be in the middle of a cooking process, indicating that it has just started to cook. The pan's surface is slightly tilted, suggesting that the pan has been placed in a pre-heated position, implying that the heat has reached a low level. The surface of the pan seems to be a medium-high temperature, suggesting a moderate amount of heat. There are no visible signs of cooking, with the pan indicating a slow cooking process.
- Reference: The extractor fan situated above the stove is in a visibly used state, with a distinct pattern of grease and vapor deposits concentrated in the center, spreading outwards to the edges. The coloration of these deposits varies from dark brown at the center to a lighter, amber-like hue towards the periphery, indicating a combination of both recent use and an accumulation over time. The fan's surface has a matte finish, which suggests it is not currently in operation, as an active fan would likely reflect some of the ambient light from the surrounding area.

#### Sample 341 — Before

- Similarity: 0.2693
- Prediction: The chopping board appears to be in the hands of a person in a kitchen setting. The board is positioned in the middle of the kitchen counter, with a handle pointing downwards, indicating that it is in the process of being cleaned. The surface of the board is slightly damp, suggesting that the water has been sprayed on it. The blades are visible, suggesting a thorough cleaning process is underway.
- Reference: The tablecloth appears predominantly white with a large, vivid green apple design in the center, suggesting a fresh, crisp theme. It is stretched out across the surface, occupying a significant portion of the frame, with an emphasis on the apple's detailed depiction that includes a spectrum of green shades and visible brush strokes, adding a textured, artistic touch. The tablecloth's edges are not visible, indicating it is fully spread out, and the surface wrinkles suggest it has been used rather than freshly laundered or ironed.

#### Sample 348 — Before

- Similarity: 0.4890
- Prediction: The refrigerator is positioned in a kitchen, with its door open, revealing a door that appears to be partially open. The interior of the fridge is cluttered with a variety of items, including a dish, a bowl, and a glass container. The refrigerator's door is open, suggesting a close-up view of the contents of the refrigerator.
- Reference: The image shows a blurry close-up of a kitchen counter with a spice jar in a state of motion, likely in the midst of being handled. Due to the motion blur, specific details about the spice jar, such as brand or content, are indiscernible. The surrounding environment suggests a domestic kitchen with a stainless-steel appliance, possibly a dishwasher, and a cabinet above filled with an assortment of other spice jars and items.

#### Sample 351 — Before

- Similarity: 0.3374
- Prediction: The bag appears to be in the hands of a person, with its contents positioned on a plate, suggesting that the person is preparing to eat. The bag is positioned in a kitchen setting, indicating that the bag is being prepared for use. The person's hand appears to have grasped the bag, implying that it is in the process of being placed on the plate.
- Reference: The olive oil bottle appears to be a standard size, with a metallic cap that is placed adjacent to the bottle on a black, glossy stovetop surface, reflecting the ambient light. The bottle itself is not in view, suggesting it may be upright and out of the frame or placed elsewhere. The cap is positioned with its open end facing upwards, indicating it has just been removed and set aside temporarily. Nearby, there are scattered items on the stovetop, including a paper bag and what appears to be a packet of food, contributing to a sense of ongoing kitchen activity.

#### Sample 353 — Before

- Similarity: 0.2831
- Prediction: The coffee pot is positioned on a counter in a kitchen, with the lid open, indicating that it is in the process of cooking. A hand is pointing at the top of the pot, suggesting that there is a slight movement in the pot. The pot appears to be empty, but the lid is still attached to the pot's lid, suggesting it may be empty. There are no visible objects, such as a pot or a lid, and there is no indication that the lid has been removed.
- Reference: The button appears to be in a neutral state, unpressed and intact, showing no signs of deformation or displacement. It is situated among a cluster of other buttons, all of which seem to be similarly at rest. The surface of the button reflects a certain amount of ambient light, indicating a smooth, possibly plastic material. Its color blends with the surrounding buttons, suggesting a user interface designed for uniformity. The finger is positioned above the button, casting a slight shadow, but not yet exerting any pressure that would indicate activation.

#### Sample 354 — Before

- Similarity: 0.3897
- Prediction: The sink appears to be in a state of transition, with the sink's surface exposed, suggesting that the sink has been sanitized. A hand is positioned on top of the sink, indicating that it is preparing to serve a meal or other meal. The sink is surrounded by a number of other items, including a pot, sink, and a sink.
- Reference: A ladle with a bright yellow handle and a reflective, stainless steel scoop is held mid-air, seemingly captured in the midst of an action. Its position is off-center towards the lower part of the frame, pointing diagonally upwards, suggesting an upward or forward motion. The ladle's handle appears sturdy and ergonomic, with a slight curvature that fits comfortably in a grip, as indicated by the fingers wrapped securely around it. The scene is domestic, with a kitchen countertop visible, and various items such as a wooden spoon resting in a white spoon rest, a clear glass with a green motif, and a plastic water bottle in motion, caught mid-roll towards the edge of the counter.

#### Sample 356 — Before

- Similarity: 0.3877
- Prediction: The stove appears to be in a state of flux, indicating that it is not yet ready to be used. It is positioned on a table, with a sloping surface, suggesting that it has not yet been used. The stove's lighting is dim, suggesting a low-light setting, and the stove itself appears to have been placed in the middle of the room. The kitchen area is cluttered with clutter, including a kitchen sink, sink, and counter, which may have been wiped down. There are no other items on the stove, such as a pot or utensil, and there is no visible evidence of cooking.
- Reference: The mixture in the pan appears to be in the initial stages of cooking, with a moderate amount of clear liquid pooling around the ingredients. Scattered throughout the liquid are green components, which resemble sliced green parts of spring onions or possibly green bell peppers, not yet softened by the heat. Their shapes are irregular, and they float separately in the liquid without clumping together. There is a visible sheen on the surface, indicating the presence of oil or another cooking fat, aiding in the sautéing process. The edges of the mixture are not sticking to the pan, suggesting that it is being stirred frequently or that the heat is appropriately moderated.

#### Sample 359 — Before

- Similarity: 0.2575
- Prediction: The cloth appears to be in the hands of a person, with a smoky complexion, indicating it is in the process of being washed. The cloth's surface is slightly damp, suggesting that it may be soaked in soap or water for a few minutes. The person's fingers are visible, suggesting the cloth is still wet.
- Reference: The bin is situated in the lower right corner of the image, just beside a white dish rack that houses various kitchen utensils. It appears slightly overfilled, with its contents reaching above the rim, indicating a pressing need for emptying. A clear plastic bag lines the bin, and items within seem to be a mix of food waste and other household refuse, suggesting recent kitchen activity. The positioning of the bin, tucked away under the counter, implies an efficient use of space in a kitchen where activities are underway.

#### Sample 360 — Before

- Similarity: 0.4618
- Prediction: The kitchen sink appears to be in a state of transition, suggesting a person's hand is preparing to open the door. The sink's interior is cluttered with a variety of items, including dishes, dishes, and utensils. The kitchen's lighting is dim, indicating a low-light situation.
- Reference: The fridge door is partially opened, revealing a black interior. A few LED indicators are illuminated on the external interface of the fridge, positioned on the upper right side. The door handle is oriented towards the left, indicating that the door is ajar. The surroundings reflect a dim light on the glossy surface of the fridge, adding to the ambiance.

#### Sample 361 — Before

- Similarity: 0.4186
- Prediction: The bacon appears to be partially sliced, with a thin layer of meat on top, indicating that it is in the process of being sliced. The skin is a dark brown, slightly smoky brown, with no discernible markings or markings, suggesting that the bacon is being prepared for cooking. The person's hand is positioned in the middle of the bacon, presumably preparing to slice it.
- Reference: The pepper is fully encapsulated in a clear plastic wrap, presenting a vivid contrast against the yellow cutting board. It's nestled between a green and a yellow pepper, suggesting they are part of a multi-colored pack. The untouched plastic suggests the initial stage of the culinary preparation process. The individual's hand is positioned over the green pepper, implying an imminent action, perhaps to commence the unwrapping or cutting. The surrounding area is littered with onion skins and garlic cloves, indicating ongoing cooking activity.

#### Sample 362 — Before

- Similarity: 0.3948
- Prediction: The cloth appears to be in the hands of a person, with the fingers pointing downwards, indicating that it is in the process of being rubbed. The cloth's surface is slightly damp, suggesting that it may be wet or damp. The person's fingers are visible, suggesting the cloth is still wet, and there is no indication that the cloth has been washed.
- Reference: The water tap, constructed of a material with a metallic sheen, is captured at the moment it is releasing water. The flow is moderate, creating a cascade that impacts the sink's basin and generates a spray of water droplets visible against the basin's surface. The tap's handle is positioned at an angle that suggests it is in the 'on' position, allowing water to flow freely. Surrounding the faucet, various kitchen items can be discerned, contributing to a scene of domesticity.

#### Sample 364 — Before

- Similarity: 0.2822
- Prediction: The kitchen sink appears to be in a state of transition, suggesting that the sink has been placed on a table or counter. The sink's surface is cluttered with a variety of items, including a bowl, a pot, and a dish. The kitchen's lighting is dim, indicating that there may be a sudden movement of the sink.
- Reference: The sweet potato in this frame exudes a fresh and robust appearance. Its skin, mostly smooth with a few natural blemishes, holds a rich orange-brown hue, hinting at its natural earthy origins. The oblong shape of the tuber is accentuated by subtle curves and a slightly tapered end. There's a faint glisten on its surface, perhaps from being freshly washed or due to ambient light. One can almost sense its starchy texture and sweet aroma just by looking at it.

#### Sample 367 — Before

- Similarity: 0.3449
- Prediction: The water appears to be in a liquid state, suggesting that it is not yet fully cooled. The water's surface is slightly damp, suggesting a gradual movement of the water, which suggests that the water has been drained. The object of the hand is positioned in the middle of the glass, indicating a steady motion, implying a slight movement. There is a thin layer of water on the surface, suggesting the water is still wet.
- Reference: The cap appears to be in a dimly lit setting, making the details slightly obscured. From the visible portion, it seems to be situated amidst various household items. The angle at which the cap is positioned does not offer a full view, providing only a partial glimpse of it. The surrounding environment has a chaotic appearance with multiple objects scattered around, drawing attention away from the cap itself.

#### Sample 368 — Before

- Similarity: 0.3542
- Prediction: The bag appears to be in a closed position, with its contents positioned in the middle of a kitchen counter. The person's hand is likely preparing to open the bag, indicating that they are about to open it. The contents of the bag are clearly visible, suggesting that the person has just opened the bag.
- Reference: The tomatoes appear freshly opened from a sealed, rectangular plastic can, with the lid being peeled back by a pair of hands. The contents are vibrant red chopped tomatoes, steeped in their own juice, with a noticeable gleam that suggests a high moisture content. Small bits of tomato pulp and seeds are visible, indicating a coarse chop. The can's label, facing downwards, is not fully visible, but the color and texture are unmistakably those of canned chopped tomatoes.

#### Sample 369 — Before

- Similarity: 0.4536
- Prediction: The cloth appears to be soaked in a stream of water, indicating it is being washed. Its surface is slightly damp, with a thin layer of water on its surface, suggesting that the water has been drained. The cloth's texture is reminiscent of a paper towel, and the water's odours suggest that the fabric may have been soaked for a long time.
- Reference: The filter appears to be a metal kitchen strainer with multiple perforations, primarily used for draining food items. Its surface glistens with moisture, suggesting it has recently come into contact with water or some liquid. Settled at the bottom of the filter is a small amount of residual water, reflecting the ambient light. The metal has a worn look, showing signs of use with visible mineral deposits or staining. Next to the filter, one can observe a green liquid detergent container, further indicating the kitchen context.

#### Sample 371 — Before

- Similarity: 0.3596
- Prediction: The courgette appears to be in the early stages of cooking, indicating that it has just started to cook. Its skin is revealing, suggesting that it may be a little charred, but it's not yet fully cooked. The texture of the courgettes suggests that they've been sitting for a long time, possibly a few minutes or so.
- Reference: The spatula is held at a slightly angled position, hovering over a pan that contains diced vegetables, presumably being sautéed. The hand grasping it appears to be mid-stir, suggesting a gentle but firm motion. The utensil itself looks to be made of a dark material, possibly non-stick plastic or silicone, suited to the task of cooking without scratching the pan's surface. Its flat edge and slotted design indicate that it's meant for flipping or turning food items while allowing excess oil or liquid to drain through the openings.

#### Sample 372 — Before

- Similarity: 0.4186
- Prediction: The bin appears to be in a closed position, with its lid partially open, suggesting that the contents of the bin are still in the open position. The bin's interior is cluttered with a variety of items, including a plastic bag, a paper towel, and a tin can. The camera's focus is on the bin itself, which appears to have been partially emptied, indicating that there may be a few items in the bin.
- Reference: The basket appears in a dynamic state, captured in a blurred motion suggesting swift movement. The contents within the basket are indistinguishable due to the high speed of the action, with colors melding into streaks across the frame. The basket's form is elongated horizontally, indicating rapid horizontal displacement, possibly due to it being dropped or thrown. The surrounding environment is also captured in a blur, with the flooring providing the only stable visual anchor, its orange hue casting a warm tone on the scene.

#### Sample 375 — Before

- Similarity: 0.4949
- Prediction: The bowl appears to be in the hands of a person in a kitchen setting. The bowl is covered with a thin layer of soapy water, indicating that it is in the process of being washed. There is a visible stream of soap suds on the surface of the bowl, suggesting that it has been sanitized. The water's abrasions suggest that the bowl is still wet, and the soap's residue suggests that it may have been soaked.
- Reference: A white ceramic dish is held above a stainless steel sink, partially filled with water and suds. The surface of the dish is visibly soiled with remnants of food, suggesting that it has just been used and is awaiting cleaning. The surrounding area shows a cluttered kitchen setting with various cooking utensils and dishes piled up, indicating a meal has recently been prepared and consumed. The presence of a sponge and dish soap nearby implies readiness for the dishwashing process to commence. The bottom of the dish is facing the camera, with water droplets and a thin film of grease reflecting the overhead light, highlighting the need for a thorough scrub.

#### Sample 376 — Before

- Similarity: 0.4437
- Prediction: The broccoli appears to be in the hands of a person holding a knife, indicating that it is in the process of being rinsed. Its surface is bare, suggesting that it has not yet been washed. The water level is low, suggesting it is still wet, and there is no indication that the water has been drained. There is a slight amount of water on the surface of the broccoli, which suggests that it may be soaking for a while.
- Reference: The cucumber appears to be relatively dry and untouched by water. The person's hands are not yet interacting with the cucumber directly. The cucumber's skin looks smooth with a shiny green hue, indicative of its freshness. There are no apparent blemishes or imperfections on the visible part of the cucumber, and it rests against the side of the sink, yet to be cleaned.

#### Sample 378 — Before

- Similarity: 0.4575
- Prediction: The vegetable appears to be in the middle of a cooking session, indicating that it's about to be ready to eat. It's positioned on a cutting board with a sharp edge, suggesting that it has been preparing for a long time. The knife's edge is slightly curved, suggesting it may have been slicing the vegetable, implying that it may be a medium-sized piece of vegetable.
- Reference: A gas hob displays a single black pan centered on the front right burner, which is alight, suggesting cooking is in progress. The pan contains diced vegetables, primarily zucchini and carrots, being sautéed, as evidenced by the glossy sheen, possibly from oil. Cooking utensils — a spatula and a spoon — rest on the counter, within easy reach. To the left, a plate with remnants of food and a white spatula suggest a meal is being prepared or has recently been consumed. The hob appears to be clean, and the knobs on the hob front are in an undisturbed position, indicating a single burner in use.

#### Sample 379 — Before

- Similarity: 0.3557
- Prediction: The kitchen sink appears to be in a state of transition, suggesting a recent change in the position of the sink. The sink's surface is slightly tilted, suggesting that it's positioned at a slight angle, indicating that the sink has been placed in the right position. The kitchen's lighting is dim, suggesting the sink is positioned in the middle of the room, implying a gradual movement. There are no visible objects, such as a pot, sink, or counter, suggesting there's still room to maneuver.
- Reference: The tray is situated on the scales, appearing relatively stationary. The tray itself has a clean and shiny surface with an almost reflective quality. It sits flush against the scale's surface, suggesting that it's resting firmly and has not yet been disturbed.

#### Sample 381 — Before

- Similarity: 0.1969
- Prediction: The meat appears to be in the middle of a cooking process, indicating that it has been preparing for a long period of time. The meat is covered in a thin layer of fat, suggesting that it may be a medium-sized piece of meat. The skin is a dark brown, with a light brown hue, suggesting it may have been cooked before.
- Reference: The spice jar appears to be in its early stages of application. The jar's cap, equipped with perforated holes for even distribution, is slightly tilted, hinting at the intent to pour. Yet, only a minute amount of spice seems to have been dispersed from the jar, likely just the beginning of the seasoning process. The surrounding area on the dish contains sporadic and minimal specks of the spice, indicating that the seasoning process has just started.

#### Sample 392 — Before

- Similarity: 0.3818
- Prediction: The cabinet appears to be in a state of transition, with a person's hand hovering over the door, suggesting that someone is attempting to open the door. The cabinet's interior is cluttered, with its contents scattered across the floor, indicating a gradual movement. The door's hinges are partially closed, suggesting the door may be partially open. The interior of the cabinet shows a variety of objects, including a kitchen counter, a sink, and a cupboard.
- Reference: A tea towel is partially draped over the edge of an open drawer. The towel exhibits a vibrant stripe pattern with bold colors—yellow, pink, blue, green, and white—creating a lively contrast against the wooden tones of the drawer. It appears to be a linen material, given its texture and slight wrinkles, indicative of recent use or hasty storage. The tea towel is positioned such that it could easily slip off the drawer's edge, suggesting that it wasn't placed with long-term storage in mind.

#### Sample 397 — Before

- Similarity: 0.3245
- Prediction: The knife appears to be in the middle of a kitchen counter, with a sharp edge and a slender blade pointing downwards. The knife's handle is slightly tilted, suggesting that the knife is positioned in a position where it can be easily accessed. The blade's surface is slightly uneven, suggesting it may be a medium-sized piece of wood, possibly a hardwood, or a light-colored one. The edge of the blade is angled slightly downwards, suggesting a gradual movement, possibly from one side to the other. The angle of the knife suggests that the blade may have been pressed against the counter, indicating a slight movement.
- Reference: The salt appears to be contained within a typical cylindrical container with a white cap, likely designed with a flip-top for easy pouring or shaking. The container rests among an array of other kitchen items, and the immediate surroundings give no clear indication of any recent interaction or disturbance involving the salt. The placement and orientation of the salt container suggest that it has been set down after use or it's awaiting its turn for inclusion in the culinary process.

#### Sample 399 — Before

- Similarity: 0.4381
- Prediction: The box appears to be empty, with its contents positioned in the middle of the frame. A hand is attempting to open the top of the box, indicating that it is preparing to open. The person's fingers are pointing at the box's contents, suggesting that they are preparing for a meal or other activity.
- Reference: The bottle appears upright and closed, positioned adjacent to the sink's edge. It's a rectangular prism-shaped container with a distinct soy milk branding, prominently featuring the word "SOY" in capital letters and an image of a soybean pod. The carton's top is intact, suggesting it has not yet been opened or altered. Its pristine condition indicates that it has likely just been taken out of a shopping bag or removed from storage, ready for use.

#### Sample 401 — Before

- Similarity: 0.3563
- Prediction: The cloth appears to be in a position that indicates it has been placed on a table or counter, possibly in the kitchen. It is positioned in the middle of a kitchen counter, with a gap in the center of the cloth, indicating that the cloth is being placed on top of the counter. The cloth's surface is slightly exposed, suggesting that the fabric may have been placed underneath the counter or counter.
- Reference: The floor appears to be a hardwood surface, exhibiting a rich, warm brown hue with a polished finish that reflects a bit of the surrounding light. The planks are arranged in a traditional staggered pattern, which creates a flow across the floor, adding to the sense of space within the room. There are some small debris and dust particles scattered sparsely across the surface, indicating a need for cleaning. The floor's condition is overall tidy, but the presence of these small particles suggests recent foot traffic or activity.

#### Sample 403 — Before

- Similarity: 0.4490
- Prediction: The bacon appears to be in the hands of a person with a knife, suggesting that they are preparing to eat it. The knife's handle is positioned at the center of the bacon, indicating that it is in the process of being sliced. The bacon's texture is reminiscent of an egg roll, implying that it's a medium-sized piece of bread that's likely to be sliced into bite-sized pieces.
- Reference: The onion appears to be in the initial stages of preparation. It is sliced into semi-circular or crescent-shaped pieces, with the pieces neatly arranged on a plate. The thickness of each slice is relatively consistent, suggesting that the onion has been methodically and carefully prepared. Around the plate, other ingredients, such as olives, are visible, implying that the onion might be an integral part of a broader recipe. The vibrant, off-white to pale yellow coloration of the onion slices indicates freshness.

#### Sample 406 — Before

- Similarity: 0.3081
- Prediction: The bin appears to be in a state of transition, with the lid partially open, suggesting a gradual movement. The lid's surface is slightly tilted, indicating that the bin is not yet fully closed. The bin's interior is cluttered, suggesting that there may be a gap between the lid and the bin, which may be partially closed. There are no visible objects in the frame, such as a person's hand or a plastic bag.
- Reference: The strainer appears to be held at an angle, capturing the viewer's immediate attention. It contains a vivid, possibly viscous, orange-yellow liquid that seems to be either being poured into or is about to be drained from the strainer. The liquid's bright hue contrasts with the white of the strainer, and there are several distinct streams and drops evident, suggesting a dynamic moment of motion or transition.

#### Sample 410 — Before

- Similarity: 0.2452
- Prediction: The jar appears to be in the hands of a person, with its contents positioned in the middle of the frame. The lid is partially open, suggesting that the person is attempting to open the jar. The bottle's contents are clearly visible, indicating that it is in the process of being opened. The person's hand is positioned on the side of the bottle, implying that they are preparing to open it.
- Reference: A partially completed pizza with a base of dough prominently displays a smattering of sweetcorn kernels. These golden nuggets of corn are scattered across the pizza in a casual, seemingly haphazard fashion, dotting the surface with their sunny hues. The sweetcorn appears to have been freshly sprinkled, with some kernels resting atop streaks of tomato sauce, while others find themselves nestled between the creamy white of the dough. There’s a sense of motion, perhaps captured mid-action, as if the sweetcorn has just tumbled from the can and landed in a random array on the pizza.

#### Sample 412 — Before

- Similarity: 0.3062
- Prediction: The chopping board appears to be in the hands of a person holding a kitchen knife. The board is positioned in a horizontal position, with the blades pointing downwards, indicating that it has been recently washed. The surface of the board is covered with a thin layer of soapy water, suggesting that it may be abrasive or damp. The water's surface is slightly wet, suggesting a waterlogged surface.
- Reference: The spring onion appears freshly introduced into a kitchen sink area, its roots still intact, suggesting recent procurement, possibly from a garden or market. The onion's white bulbous end displays a healthy sheen, indicative of moisture retention, while the green stalks exhibit a vibrant color, with no visible wilting, indicating freshness. The onion is held at a slight angle, with fingers gripping firmly around the lower green stalks, preparing for a rinse or a cut.

#### Sample 420 — Before

- Similarity: 0.4699
- Prediction: The bag appears to be partially open, with its contents positioned in the middle of the frame. Its shape is reminiscent of a plastic grocery bag, with a slightly curved edge and a rounded edge, suggesting that the contents may have been thrown out. The bag's interior is cluttered, with the contents of the bag being stacked on top of each other, indicating that the bag has been opened. The camera's focus is on the bag itself, which appears to have been placed in a position where it can be easily seen.
- Reference: The freezer appears to be a standard upright model with a front-facing door, partially open, revealing a glimpse of its contents. A frozen item, possibly a bag with a colorful mixture that could be frozen vegetables, is held in a person's hand, suggesting they are either placing it into or removing it from the freezer. The door itself has an integrated handle at the top, and there are visible compartments on the door's inner side, although the contents are not clear. The lighting is dim, casting a soft glow inside the freezer, which contrasts with the darker room beyond.

#### Sample 422 — Before

- Similarity: 0.4830
- Prediction: The oven appears to be in a state of transition, with the oven's interior illuminated by a light source, suggesting that the oven may be preparing for a meal or cooking session. Its interior is cluttered with a variety of items, including a pot, a microwave, and a stovetop. The oven is positioned in the middle of a kitchen area, indicating that there is a lot of room for the oven to cook.
- Reference: The oven glove appears to be partially on the person's hand, with the fingers not fully inserted into the glove's finger compartments, indicating a hurried or in-process action of putting it on. The glove itself is a light color, possibly white or a light shade of grey, and shows signs of wear such as slight discoloration or stains. The thumb of the glove seems to be properly worn, but the rest of the fingers are yet to be snugly fitted. The overall position of the hand and the glove suggests the individual is either about to engage with something hot or has just completed a task requiring thermal protection.

#### Sample 427 — Before

- Similarity: 0.4391
- Prediction: The bottle appears to be in a glass container with a lid, indicating that it has been opened. The bottle is positioned in the middle of the frame, with the lid positioned at the top of the bottle, suggesting that the bottle is still in its packaging. Its contents are positioned on a shelf, implying that it may have been opened before the camera was able to take a closer look at the bottle. There is a slight movement in the bottle's packaging, suggesting a gradual movement, and the bottle itself appears to have been open for a moment or two.
- Reference: The refrigerator's top shelf is partially visible, housing a carton of eggs with several eggs missing, suggesting recent use. The middle shelf is empty, indicating either a recent clearing or pending restocking. The lower section, less discernible due to the angle, appears to contain some indistinct items, potentially vegetables. The door is ajar, and the interior light is off, implying that the door has been open for a while or the automatic light function is not active. To the right of the refrigerator, there is a countertop with a coffee machine and a stainless steel pot, indicating the proximity of the kitchen's cooking area.

#### Sample 430 — Before

- Similarity: 0.4868
- Prediction: The container appears to be in the hands of a person, with a hand clasped around the edge of the container, suggesting that the person is preparing to open the container. The container's surface is a dark brown, indicating that it has been sealed. The person's hand is positioned in a position that indicates that the container has been opened.
- Reference: The plastic bag in question appears to be partially crumpled and compact, resting on the kitchen counter. It is not fully open, suggesting that its contents have not yet been fully removed. The bag's mouth is not stretched wide, indicating that the opening action has either just begun or is about to commence. It has a translucency that allows the inside or the lack of contents to be partially visible, and its thin material has some creases and folds from its previously stored state.

#### Sample 433 — Before

- Similarity: 0.3686
- Prediction: The door appears to be partially open, with a gaping hole in the side of the door, suggesting that the door is partially closed. The door's hinges are visible, suggesting the door has been closed for a moment, indicating that there is a slight movement in the room.
- Reference: The cloth appears to be partially scrunched in the person's hand, showing signs of having been twisted or wrung out. Its texture looks damp and heavy, suggesting it has absorbed a significant amount of water or another liquid. The cloth's color is not fully discernible due to the motion blur and lighting, but it seems to have a light tone, possibly white or cream. The person's grip on the cloth is firm, as indicated by the tautness on the visible portion, indicating that the squeezing action has just been performed or is about to be initiated.

#### Sample 436 — Before

- Similarity: 0.3274
- Prediction: The kitchen sink appears to be in the middle of a kitchen counter, with a large bowl containing a variety of food items. It is positioned on a counter in the center of the room, indicating that there is a lot of work to be done. The sink's surface is cluttered, suggesting that there may have been a bit of work done. There are several items on the counter, including a bowl, a plate, and a spoon.
- Reference: The peeler appears to be in a resting position, nestled comfortably in the grip of a person's hand. The metallic blade, designed to strip away the outer layers of vegetables, reflects the ambient light, hinting at its sharpness and readiness for use. Surrounding the peeler are the evidences of its recent work: small, thin pieces of peel that have been expertly removed from the partially visible eggplant, suggesting a meticulous and careful peeling process. The hand holding the peeler shows a relaxed yet purposeful hold, indicating a brief pause in the action, perhaps as the person assesses their next move.

#### Sample 437 — Before

- Similarity: 0.1616
- Prediction: The sink appears to be in a state of flux, indicating that there is still a lot of water on the bottom of the sink, suggesting that the water has been drained. The sink's surface is cluttered with a variety of items, including dishes, dishes, and utensils, implying that there may have been a bit of water in the sink. The water level is low, suggesting there may be a slight amount of water present in the basin, which could indicate that the sink is not yet full.
- Reference: The pieces of pepper are strewn about on a wooden chopping board. Their fresh, vibrant yellow hue contrasts starkly with the brown backdrop of the board. They appear to be freshly chopped, with a few seeds evident among the pieces, and the wetness of the freshly cut vegetable glistening in the ambient light.

#### Sample 438 — Before

- Similarity: 0.4464
- Prediction: The kitchen appears to be in a state of flux, with a few items scattered around the room, such as a pot, a microwave, and a stove. The lighting is dim, suggesting that there is a lot of light in the room. It's possible that the light is coming from the stove or from the oven, which could indicate that the oven is not yet fully operational. The kitchen has a variety of items on the counter, including dishes, utensils, and other household items.
- Reference: The lid is positioned on a red-colored slow cooker that sits on a grey countertop. The lid's handle appears to be a black, round knob that is potentially made of a heat-resistant material, typically used for kitchen cookware. The glass of the lid looks to be in a clean state with minimal to no condensation, indicating either a cold state of the cooker or the beginning of its cooking cycle. Around the lid, the surrounding area is illuminated with natural light, reflecting off the lid's surface, creating a slight glare.

#### Sample 439 — Before

- Similarity: 0.4168
- Prediction: The scourer appears to be in the hands of a person attempting to remove a scrubbing pad from a kitchen sink. It is positioned in the middle of the kitchen counter, with its handle pointing downwards, indicating that it is in the process of being rubbed. The cloth is soaked in soapy water, suggesting that it may have been washed. The hand's movements indicate that it has been rinsing, which indicates that the scouring pad is still wet.
- Reference: The towel appears to be a standard kitchen towel with a predominantly yellow hue, featuring a red pattern, which suggests a possible decorative or functional design. It is being held by a person whose hand and forearm are visible in the image. The towel is partially crumpled and in motion, which blurs the details of its design and exact shape, as the person seems to be in the process of either picking it up or beginning to use it. The background reveals a typical kitchen countertop with various items scattered around, indicating that cleaning or cooking activities may be taking place.

#### Sample 445 — Before

- Similarity: 0.4958
- Prediction: The wok appears to be in the process of being rinsed, indicating that it is in the early stages of cleaning. The surface of the wok is covered with a thin layer of soapy water, suggesting that it has been washed. The water's odours suggest that it may be abrasive or smudge-prone, implying that the water has been sprayed on it.
- Reference: The pan appears to have just been placed under running water, with soap suds clinging to the blackened inner surface, indicating a recent attempt at cleaning. The individual is using a stiff-bristled brush to scrub the pan, with their right hand gripping the handle and their left hand providing additional support. The position of the brush and the direction of the water suggest an action of scrubbing in progress. Around the sink, there are signs of recent kitchen activity, including a discarded towel and cut pieces of yellow sponge or food on the counter.

#### Sample 448 — Before

- Similarity: 0.4609
- Prediction: The washing machine is positioned in a dark room, with a white door and a black handle, suggesting that it's in the middle of a room. It's positioned on a flat surface, indicating that there's no room for the washing machine, which is likely to be a dishwasher. The machine's interior is cluttered, with only a few items visible, such as a hand-held soap dispenser, a coffee maker, and an oven. The surrounding area has a variety of other items, including a kitchen sink, microwave, and dishwasher.
- Reference: The coffee machine sits on a kitchen counter, displaying a standby mode, indicated by the lack of illuminated buttons or indicators. Its carafe is absent from the heating plate, suggesting that it has either been removed for cleaning or to serve coffee. A cluster of wires is visible near the machine, with a possible power cord extending towards an electrical outlet. The surrounding area is cluttered with various items, but the machine itself appears clean and in good condition, waiting for interaction to commence its brewing cycle.

#### Sample 453 — Before

- Similarity: 0.4848
- Prediction: The sink appears to be in a state of flux, indicating that there is a significant amount of water on the surface of the sink. The sink's surface is covered with a thin layer of soapy water, suggesting that there may be a small amount of soap left on the sink surface. The water level in the sink is low, suggesting a moderate amount of liquid is present, and the sink itself appears to have been soiled.
- Reference: The counter surface gleams under the ambient lighting, revealing its untouched state. There's a layer of dust particles on it, interspersed with a few stray crumbs, possibly remnants from a prior meal. Alongside the particles, faint streaks, possibly from water or other liquid residues, mar the otherwise smooth surface. The imperfections on the counter are evident and they clearly need attention.

#### Sample 458 — Before

- Similarity: 0.3856
- Prediction: The wok appears to be in the middle of a kitchen sink, with a sprinkling of soapy water on the surface, suggesting that it is in the process of being rinsed. The pan's interior is cluttered with dishes, dishes, and utensils, indicating that there is still a lot of work to be done. There is a thin layer of soap on the bottom of the wok, which may indicate that it has been soiled.
- Reference: The tap is in an off position, with the lever aligned parallel to the countertop, indicating no water flow. Its metallic surface reflects the ambient light, and no water droplets are visible on or around the spout, further confirming it hasn't been used immediately prior. The tap's position, far from the basin edge, suggests it is designed to accommodate a variety of dish sizes for washing.

#### Sample 459 — Before

- Similarity: 0.4164
- Prediction: The knife appears to be in the middle of a kitchen counter, with a handle pointing downwards, indicating it is in the process of being removed from the kitchen counter. The knife's handle is positioned in a horizontal position, suggesting that the knife has been removed from its handle. The blade's surface is exposed, suggesting a gradual movement of the blade, implying that the blade has been discarded.
- Reference: The image reveals a standard-sized, cylindrical can positioned near the edge of a countertop, partially opened with a lid attached. The pull-tab of the can has been engaged and is bent at an angle, indicating the lid has been partially peeled back. The metallic interior surface of the can reflects the ambient light, highlighting the exposed content which appears to be a type of food, possibly a canned fruit or vegetable, showing a glimpse of small, rounded items consistent with peas or corn.

#### Sample 460 — Before

- Similarity: 0.2926
- Prediction: The pan appears to be in the middle of a cooking process, with a sprinkling of oil on the surface of the pan, indicating that there is still a lot of work to be done on the pan. The pan's surface is covered in a thin layer of oil, suggesting that there may be a bit of work involved. There are no visible marks or marks on the bottom or sides, implying that there has been a little work done.
- Reference: The image captures a motion-blurred scene where the water tap appears to be at a critical transition point. The blurred state of the hand and the tap suggest a dynamic interaction, with the tap likely in the process of being turned off. The water flow is not clearly visible, indicating either a rapid movement that the camera could not freeze or a very thin stream of water that blends into the surrounding blur. Drops of water can be inferred to be present, possibly splashing or just ceasing to fall, reflecting the hurried action taking place.

#### Sample 464 — Before

- Similarity: 0.4201
- Prediction: The kale appears to be in the early stages of its preparation, indicating that it is in the process of being chopped. The leaves appear to be ripe, suggesting that they may have been discarded or thrown away. The leafy greens are a vibrant green, with a bright green hue, suggesting they may be discarded.
- Reference: The lettuce in this frame appears freshly cut, with pieces ranging in size from larger chunks to finer bits. The varied sizes suggest that the cutting has just started, and the user hasn't yet achieved a consistent chop size. The bright green color of the lettuce indicates its freshness, and some of the edges of the lettuce pieces appear slightly jagged, showing the initial cuts.

#### Sample 465 — Before

- Similarity: 0.4895
- Prediction: The mug appears to be in the hands of a person, with its lid partially open, suggesting that it is in the process of being placed in a dishwasher. Its interior is cluttered with a variety of items, including a toothbrush, a dish towel, and a bowl of ice cubes. The rim of the mug is visible, indicating that there is a lot of work to be done.
- Reference: The bowl, exhibiting a glossy black finish, is held at an angle, allowing residual water and suds to cascade towards the nearest edge, indicating the commencement of the rinsing process. Water droplets and streaks of soap are visible across the interior surface, accentuating its curvature and reflecting the overhead lighting. The bowl's exterior is also flecked with water spots and suds, suggesting a recent wash. A dish rack with a few other utensils is partially visible in the upper left corner, while a pink sponge, a steel scrubber, and a green scrub lie abandoned to the side, marking a pause in the washing activity.

#### Sample 468 — Before

- Similarity: 0.3206
- Prediction: The chopping board appears to be in the hands of a person holding a kitchen knife, with its handle positioned in the middle of the kitchen counter. The blades are positioned at a slight angle, indicating that they are in the process of being slicked. The surface of the board is covered with a thin layer of soapy water, suggesting that the water has been sprayed on it. The water's surface is slightly wet, suggesting a waterlogged surface.
- Reference: The bell pepper appears freshly introduced to the stream of water, its vibrant red skin displaying a matte finish with several droplets starting to form on the surface. The droplet pattern is sparse, indicating that the rinsing process has just begun. The pepper is held from the bottom by a hand, with fingers slightly curled around its curves, ensuring a secure grip. The light reflects differently on the dry and wet parts of the pepper, highlighting its plump and firm condition.

#### Sample 469 — Before

- Similarity: 0.4211
- Prediction: The kitchen sink appears to be in a state of flux, indicating that it has been partially emptied. The sink's surface is cluttered with a variety of items, including a dish towel, a plate, and a bowl. The kitchen's lighting is dim, suggesting that there may be a light source nearby.
- Reference: The cover appears to be initially situated atop a cooking appliance, with only a small portion of the object being captured in this frame. From what's discernible, the cover's surface appears glossy, possibly indicating it's made of a material like glass or polished metal. There's also a reflection on its surface, hinting at overhead lighting in the room. The edges of the cover seem to be slightly elevated, suggesting that the person might be starting the process of lifting it or that it's not entirely sealed on the appliance.

#### Sample 470 — Before

- Similarity: 0.3627
- Prediction: The bottle appears to be in the hands of a person, with its lid open, indicating that it is in the process of being opened. The bottle's interior is cluttered with a variety of items, including a jar, a bowl, and a tray. The lid is positioned in a horizontal position, suggesting that the bottle has been opened.
- Reference: The plug appears to be partially inserted into a power outlet, which is located close to a cluttered area, possibly a kitchen counter, given the presence of various kitchen items and food packages. The outlet itself is standard, likely designed for two-pronged plugs, and the plug is white, contrasting with the cream-colored wall. The person's hands are gloved in yellow, suggesting the maintenance of hygiene or protection from dirt. The plug is captured in the midst of an action, with the person's hands positioned as if they are in the process of gently pulling or manipulating the plug.

#### Sample 473 — Before

- Similarity: 0.4595
- Prediction: The jar appears to be in the hands of a person, with its lid positioned in the middle of the kitchen counter, indicating that it has been placed in a position where it is likely to be thrown or thrown. The lid's surface is slightly tilted towards the camera, suggesting that the person is attempting to remove the lid from the jar.
- Reference: The bottle appears to be a sturdy plastic container, primarily blue in color with a textured design enhancing grip. Its cap, also blue but of a slightly different shade, is secured tightly to the bottle, which seems to be in the process of being opened by a pair of hands. These hands exhibit a firm grip on the bottle, with the cap still in place, indicating the initial stage of opening. The contents of the bottle are not visible, suggesting it might be opaque, and there's a noticeable absence of any liquid spillage, implying that the bottle is likely full or unopened.

#### Sample 476 — Before

- Similarity: 0.3680
- Prediction: The pizza appears to be in a medium-sized bowl, with a thin layer of cheese embedded in the middle. Its surface is slightly uneven, suggesting that it may have been a pre-made pizza, but it's not yet ready to be rolled into a loaf. The crust is a light brown, indicating that it hasn't been rolled yet, and there's no indication that the toppings have been placed on it yet.
- Reference: The salt shaker is inverted, with its opening directed towards a mound of shredded cheese on a round flatbread. It's being held by a hand mid-motion, implying that the action of shaking has just begun or is about to begin. The shaker's lid is white, suggesting a contrast with the surrounding ingredients and the warm tones of the kitchen. There's no visible salt coming out yet, indicating this is the initial stage of seasoning. The hand looks to be giving a slight shake, with salt potentially starting to disperse.

#### Sample 477 — Before

- Similarity: 0.3374
- Prediction: The soup appears to be in the middle of a cooking process, indicating that it's in the early stages of cooking. It's covered in a thin layer of water, suggesting that it has been simmering for a long time. The surface of the soup seems to be a mixture of flour and water, with a light brown hue, suggesting a medium-sized amount of flour. The texture of the sauce appears slightly spongy, indicative of the presence of flour or other solid ingredients.
- Reference: The light in this frame emanates a magenta hue, suggesting the early stages of ignition. The intensity is moderate, indicative of the gas burner beginning to engage, with the flame just starting to find its full strength. The light casts a gentle but defined glow on the surrounding area, illuminating the edges of the pot and creating a soft reflection on the cooktop. It is contained primarily under the pot, providing a focused source of heat with minimal diffusion into the surrounding environment.

#### Sample 482 — Before

- Similarity: 0.3609
- Prediction: The foil appears to be in a state of readiness, indicating that it is in the process of being placed on a plate. The foil's surface is slightly exposed, suggesting that it may be partially melted. The person's hand is likely preparing to remove the foil from the plate, implying that they are preparing for a meal.
- Reference: The packaging, in this frame, is intact with no apparent tampering or alterations. A package of red meat rests on the countertop, untouched and in its original state. Adjacently, there's a package of chicken or some lighter meat. The package has a label attached to it, displaying some information, potentially related to its weight and price, but the exact details cannot be discerned. The plastic seal around both these meat packages is undisturbed, signaling that the items have not been accessed yet.

#### Sample 485 — Before

- Similarity: 0.3863
- Prediction: The cabinet appears to be in a state of transition, with a person's hand hovering over it, suggesting that someone is attempting to open the door. The cabinet's interior is cluttered, with its contents scattered across the floor, suggesting a possible attempt to open or close the door, indicating that the person is preparing to open it.
- Reference: The milk carton appears to be in a person's hand, which is in motion, likely towards a surface or a designated storage area. The carton is predominantly green with visible text and imagery, suggesting it is a branded product with some sort of label design. The positioning of the hand and the blurred background suggest a swift movement, with the focus being on placing the milk carton down. The surrounding area is cluttered with various kitchen items, indicating the setting might be a kitchen counter or a similar domestic space.

#### Sample 486 — Before

- Similarity: 0.4724
- Prediction: The glove appears to be in the hands of a person, with its fingers pointing downwards, indicating that it is in the process of removing the gloves. The glove's surface is slightly exposed, suggesting that the gloves are still wet. The fingernails appear to be positioned in the palm of the person's dominant hand, suggesting a gradual movement of the fingers.
- Reference: The hand in this frame appears to be in motion, with a slightly open palm showing. Some fingers appear slightly bent, hinting at a gentle gripping or holding action. There's a glimpse of a shadowy reflection on the floor, suggesting that the hand might be near an object or surface which is causing this shadow. The overall state of the hand conveys a sense of action or movement, perhaps as part of a larger gesture or task.

#### Sample 488 — Before

- Similarity: 0.4561
- Prediction: The leaf of the broccoli appears to be in the hands of a person holding it, indicating that it is in the process of being prepared for cooking. The leaves appear to be ripe, with the stems pointing towards the kitchen, suggesting that they may be ready to be cooked. The person's hands are positioned in the middle of the plate, pointing at the leaf's stems, which indicate that they are preparing to cook.
- Reference: The leaf in question is being held under a stream of clear water from a modern, metallic faucet, which is gushing directly onto its surface. The leaf's vibrant green shades suggest it is fresh, possibly a type of lettuce, and it exhibits a slight curvature due to the pressure of the water. Droplets of water cascade over the contours and edges, reflecting the light and creating a speckled pattern of wetness across the leaf's surface. The person's hands are gently manipulating the leaf, ensuring all parts of it come into contact with the cleansing flow.

#### Sample 490 — Before

- Similarity: 0.4215
- Prediction: The package appears to be in the hands of a person attempting to open it. The person's hand is positioned in the middle of the packaging, indicating that they are preparing to open the package. The contents of the package are clearly visible, with the packaging containing a wide variety of foods, including fruits, vegetables, and dairy products.
- Reference: The tortilla appears freshly lifted from the stack, held by a hand wearing a checkered shirt, indicating the beginning of an action. It exhibits slight flexing at the edges, a common characteristic of a pliable, room-temperature tortilla. The smooth, pale surface of the tortilla contrasts with the more textured and vibrant packaging from which it was taken, and the surrounding kitchen paraphernalia—like the bag of chips and container of sugar in the background—provides a casual, domestic setting.

#### Sample 491 — Before

- Similarity: 0.2759
- Prediction: The boiled pak choi appears to be in a state of transition, indicating that it has been boiled for the first time. Its texture is reminiscent of a freshly-baked bok choy, with a crisp, tangy texture and a smooth texture. The leaves appear to be ripe, suggesting that they may have been cooked for a long time.
- Reference: The coriander appears freshly placed on a wooden cutting board. The stems and leaves are still mostly intact, exhibiting a rich green hue. Some of the leaves are slightly overlapped, and a few of the stems extend outward, hinting that they haven't been worked with yet. The coriander's overall appearance suggests it's in its natural, untouched state on the board, ready to be processed.

#### Sample 494 — Before

- Similarity: 0.3692
- Prediction: The stove appears to be in a state of transition, with a smoky interior and a brightly lit interior. It's positioned on a flat surface, indicating it's not yet ready to be used, suggesting that it may be a microwave oven. The stove's interior is cluttered, suggesting a lack of space. There are no visible objects, such as a pot or pot, but there are a number of objects in the background, including a kitchen counter, a sink, and an oven.
- Reference: In this frame, the door is almost entirely closed. The door's handle, located on the right side, appears to be in its resting position, suggesting that it hasn't been fully engaged yet. Shadows cast from the door onto the adjacent surfaces indicate that ambient light is coming from the left side of the frame. The door seamlessly blends into the cabinetry, making it difficult to discern any clear boundaries at first glance.

#### Sample 495 — Before

- Similarity: 0.3562
- Prediction: The kitchen counter appears to be positioned in the middle of a kitchen counter, with a white handle pointing downwards, suggesting a position for the counter to be placed. The counter's surface is slightly tilted, suggesting that the counter is positioned at the center of the counter, indicating that there is a gap between the counter and the counter. The countertop appears to have been placed in a sloping position, implying that it is not yet ready for use. There are no visible marks or markings on the counter or counter, suggesting the counter may be empty.
- Reference: The electrical plug, white in color with two prongs, is securely inserted into a wall socket. The plug's cord extends towards the bottom right corner of the image, indicating that it is under some tension, possibly from the device it is connected to or from the act of being pulled. The wall socket is situated close to the corner of two walls meeting, and the plug itself is partially obscured by a wooden chair leg, hinting at a domestic setting. The flooring is tiled in a warm yellow hue, and the skirting is white, matching the plug and socket.

#### Sample 496 — Before

- Similarity: 0.3765
- Prediction: The towel appears to be in the hands of a person, presumably preparing to take a shower. It is positioned in a position that indicates it is in the process of being placed on a table or counter. The towel's surface is a dark brown, indicating it has not yet been washed. Its texture is slightly uneven, suggesting that it may be a light-colored towel. The cloth's texture suggests that the towel is still damp, with a slight crease to the surface.
- Reference: The package appears to be a microwavable popcorn bag, captured in a blurred state due to rapid movement, possibly being shaken or turned over. Its surface is a mix of printed instructions and safety warnings, typical of instant snack packaging. The blurriness suggests that the package is being handled actively, and there is a notable lack of visible wear or tear, indicating that it might have just been taken out of the microwave. The surrounding area is dimly lit, and kitchen appliances are in close proximity, reinforcing the setting of a home kitchen.

#### Sample 498 — Before

- Similarity: 0.4675
- Prediction: The kitchen sink appears to be in a state of transition, suggesting that it has been placed on a table or counter. The sink's surface is slightly tilted, suggesting a gradual movement of the sink, indicating that the sink is not yet fully positioned. It is positioned in the middle of a kitchen counter, with a hand pointing towards the sink. There is a gap between the sink and the countertop, which suggests that there may be a slight movement in the sink or countertop.
- Reference: The milk bottle is a transparent, plastic jug with a white handle and cap, indicative of a standard milk container one might find in a supermarket. It's placed on its side, with the handle facing upwards, suggesting it has been casually laid down rather than carefully positioned. The cap appears to be securely fastened, and there's no visible distortion of the bottle's shape, indicating that the bottle has not been squeezed or otherwise manipulated. It rests near the edge of the countertop, surrounded by various kitchen appliances and items, including a toaster, a kettle, and an empty mug, hinting at a domestic setting perhaps in the midst of preparing a meal or a drink.

#### Sample 5 — During

- Similarity: 0.2974
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating a more gradual movement of the kitchen counter. The counter's surface is now cluttered with crumbs and other debris, suggesting a recent change in the position of the counter.
- Reference: The floor appears to remain consistently colored with the same mustard-yellow tiles, but the angle of the shot reveals more of the tile area. Additional small debris and smudges are present, and a damp streak is now visible, likely from the wiping motion. The streak has a darker shade than the rest of the floor, indicating that the floor may have been somewhat dirty before being wiped, and the wetness is bringing out the contrast in the tile's coloration.

#### Sample 7 — During

- Similarity: 0.4975
- Prediction: In this frame, the bin's lid is positioned in a slightly different position, indicating that it has been opened. The person's hand appears to be holding the bin, which is likely a part of its contents. The lid's surface is slightly blurred, suggesting that the lid is partially open. The object's surroundings are more cluttered, implying that there is a greater emphasis on the contents of the bin.
- Reference: The jar is now in motion, caught mid-air with its label oriented towards the camera. Its trajectory appears to be downwards, indicating it has been dropped. The lid remains firmly affixed, and no contents are visible escaping from the jar. The blurred background due to the motion suggests a rapid descent. The person’s foot and the striped sock are prominent in the frame, possibly the inadvertent catalysts for the jar’s sudden journey towards the floor.

#### Sample 8 — During

- Similarity: 0.3192
- Prediction: In this frame, the blender's lid is positioned in a slightly different position from the previous frame. The person's hand appears to be holding the lid, indicating that the lid has been removed from the machine. The surrounding area, including the sink, remains unchanged, with no visible signs of activity.
- Reference: The same toaster now displays subtle differences. The lever has been slightly pushed downwards, but not entirely, hinting at the beginning of the toasting process. The slots still appear vacant, and there isn't any visible toasted bread. However, there's a soft glow starting to emanate from the slots, suggesting that the heating elements are beginning to activate. The power indicator light has a dim glow, further affirming the initial stages of the toasting process.

#### Sample 12 — During

- Similarity: 0.4757
- Prediction: In this frame, the bin's lid is positioned in a slightly different position, indicating that it has been partially opened. The lid's position remains unchanged, suggesting that the lid is partially open. The object's shape remains consistent with the previous frame, suggesting a gradual movement of the bin.
- Reference: The basket's opening seems slightly wider in this frame as compared to the previous, hinting at some movement. The basket's content remains elusive, and its surroundings look similar to the previous frame with the patterned textile or rug in proximity. Parts of the person's legs and feet are visible, clad in flip-flops. The floor tiles continue to suggest an indoor environment.

#### Sample 15 — During

- Similarity: 0.4434
- Prediction: In this frame, the jar's lid has been removed from the pot, indicating that it has been poured into the pot. The lid is now slightly tilted, suggesting that the contents of the container have been removed. The spoon's grip remains steady, suggesting a steady movement in the direction of the action.
- Reference: The stock, now in a different container, displays a more disturbed surface, likely from recent agitation. Condensation is evident on the inside surface of the pot's lid, suggesting that the stock has been heated for some time and has reached a simmering or boiling state. Some small particles or residues can be observed near the center of the pot, possibly remnants of the ingredients used to flavor the broth. The overall color of the stock remains consistent, maintaining its pale yellow hue.

#### Sample 19 — During

- Similarity: 0.4905
- Prediction: In this frame, the onion has been partially removed from the cutting board, indicating that the knife has been slicing the onion. The knife's blade is now positioned in the center of the onion, presumably removing any remaining skin. The onion's skin is now more exposed to the knife, suggesting that it may have been partially cut off.
- Reference: In this moment, the carrot's transformation is underway. Strips of orange peel spiral away from the carrot, showcasing the peeling process's progress. The vegetable itself now has intermittent patches of lighter orange where the outer layer has been removed, revealing the lighter flesh beneath. The person's hands have adjusted their position slightly, providing stability and precision as they maneuver the peeler along the carrot's contour. The peeler is held at an angle optimal for removing the skin without cutting too deeply into the vegetable.

#### Sample 21 — During

- Similarity: 0.2938
- Prediction: In this frame, the ricotta lettuce has been placed in a pot of water. The water's movement is more gradual, indicating that the water has been sucked away from the lettuce. The leaf's surface is more exposed, suggesting that it has been partially boiled. The hands are more likely to be holding the lettuce in their hands, implying that they are preparing the lettuce for rinsing.
- Reference: The leaf is now being held up, allowing for a clearer view of its size and shape. It exhibits a shiny appearance, indicative of the moisture it has just been subjected to. The leaf's stem or base, which is slightly paler than the rest of the leaf, appears firm and unblemished. The main vein running through the middle of the leaf is prominently visible, leading to the numerous smaller veins branching out.

#### Sample 22 — During

- Similarity: 0.4395
- Prediction: In this frame, the meat is now firmly grasped by a hand. The skin is now more exposed to the knife's action, indicating that the meat has been partially removed from the skin. The hand's grip is more firm, suggesting that the hand is attempting to remove the meat from the meat.
- Reference: In this moment, the garlic press is engaged more fully. The hands of the user have brought the handles closer together compared to the previous frame, applying pressure to crush the garlic clove inside. There is visible strain in the hand muscles, evidenced by the tighter grip on the handles. The chamber where the garlic resides is obscured from view, but the action implies that the garlic is being pressed through the holes, though no garlic is yet emerging. The positioning of the press over the pan remains unchanged, signaling readiness to deposit the garlic directly into the waiting dish.

#### Sample 24 — During

- Similarity: 0.4945
- Prediction: In this frame, the bread has been placed in the hands of a person. The person's hand is positioned on the edge of the bread, indicating that the bread is ready to be sliced. The bread's surface is slightly creased, suggesting that it may have been sliced before the person touched the bread. The hand's grip remains firm, and the bread still has a firm grip on its surface.
- Reference: The scene remains consistent with the first frame, displaying the same person's hands, kitchen setting, and objects. However, the position of the scissors has slightly shifted; the blades appear to be wedged more firmly into the clip, indicating that the clip may have been pried open further. The person's grip on the scissors and the packet has tightened, as seen by the fingers' placement, suggesting increased effort is being applied. The packet remains stationary, and there's no visible movement of the contents or change in the placement of surrounding items.

#### Sample 26 — During

- Similarity: 0.4343
- Prediction: In this frame, the person holding the tray now has a more pronounced grip on the tray, indicating that they are attempting to remove the foil. The person's hand is now more engaged in the action, implying that the foil has been removed from the tray. The tray's surface is more exposed, suggesting that there may be a gap between the foil and the paper.
- Reference: In this scene, the cling film has been partially unrolled, with the loose end extending away from the roll. The person's hands are in motion, with one hand holding the roll steady and the other beginning to pull and stretch the film from its roll. The film displays slight wrinkles near the leading edge, a testament to the tension being applied. There's a distinct contrast between the taut, straightened portion being pulled and the still orderly coiled remainder on the roll.

#### Sample 28 — During

- Similarity: 0.2292
- Prediction: In this frame, the person's hand moves closer to the kitchen counter, revealing a more detailed view of the kitchen. The kitchen counter is now positioned in a slightly different position, indicating that there is a larger portion of the counter space to work with. The counter's surface appears to be slightly tilted, suggesting that there may be a gap between the counter and the counter.
- Reference: In this moment, the paper is captured mid-tear, exhibiting a jagged, uneven line running down from the top edge where the tear has begun. The person's right hand continues to secure the top portion of the paper, while the left hand has begun to pull away the bottom segment, creating a clear division. The tear is not straight, indicating that the force applied by the hands is uneven or that the paper's resistance is causing a non-linear rip. The brightness of the light on the paper accentuates the texture of the torn edge.

#### Sample 30 — During

- Similarity: 0.3733
- Prediction: In this frame, the crockpot has been placed in a pot of boiling water, indicating that the water has been boiled. The person's hand appears to be holding it, implying that they are attempting to rinse it. The water is now dripping from the bottom of the pot, suggesting that there may be a small amount of water left in the pot.
- Reference: The colander is now tilted slightly to the side, causing some of the rice grains to shift towards the edge closest to the sink. This change in angle suggests that the person is beginning to shake or tap the colander to encourage excess water to drain from the rice. The hand gripping the colander has adjusted to accommodate the tilt, and the rice appears less clumped, with individual grains becoming more discernible as they spread out due to the movement.

#### Sample 31 — During

- Similarity: 0.4460
- Prediction: In this frame, the person's hand is more focused on the surface of the kitchen counter, indicating that there is more work to be done, such as scrubbing the counter with a cloth or paper towel. The object's focus is more on the cleaning process, suggesting that the cleaning solution has been sprayed on the counter. The area around the counter appears more cluttered, suggesting a more active cleaning action.
- Reference: In this instance, the glass maintains its upside-down orientation, but there is a noticeable shift in its position on the tabletop. The person's hand is in motion, with fingers and thumb appropriately placed to apply force to the glass's base. The movement suggests a slide across the wooden surface, as evidenced by the change in the light reflection pattern on the glass's base, which now has a slightly blurred appearance due to the motion.

#### Sample 32 — During

- Similarity: 0.3808
- Prediction: In this frame, the lid has been removed from the container, indicating that it is now in the hands of the person who is holding it. The person's hand appears to be holding the lid, implying that the lid is still attached to the container.
- Reference: The lettuce is in the process of being unveiled; the plastic wrap has been partially removed, revealing the top of the lettuce head. The leaves at the crown appear slightly more relaxed than before, likely due to the removal of the constraining wrap. The green hue of the leaves is consistent, displaying no signs of wilting or discoloration, which emphasizes the freshness of the produce. The person handling the lettuce has initiated the unwrapping from the top, peeling the plastic down and away from the lettuce, indicating a preparation to use the lettuce imminently.

#### Sample 33 — During

- Similarity: 0.4666
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating that it has been placed in a different position. The kitchen sink's position remains unchanged, suggesting that the kitchen is now positioned in the same position as the sink. The lighting is more dim, suggesting a more gradual movement of the sink, which is likely a reflection of the kitchen's lighting conditions.
- Reference: The cabinet door is now open wider than in the previous frame, revealing more of its contents. The lower shelf still displays the orderly arrangement of cans, and now, the upper shelf's contents become partially visible, featuring what appears to be a row of upright standing bottles or jars. The arrangement suggests a systematic approach to organizing the items by size or type. The cabinet's interior is bathed in the ambient light of the room, which casts soft shadows and gives a homely atmosphere to the kitchen storage space.

#### Sample 36 — During

- Similarity: 0.3980
- Prediction: In this frame, the bread has been placed in a new position, with a slightly different shape than the previous frame. The bread's surface has been reshaped, revealing a more rounded shape, indicating that it has been cut. The knife's edge is now positioned on top of the bread, suggesting a slight movement. The sandwich's shape remains the same, with the bread still firmly attached to the sandwich.
- Reference: The scene is largely unchanged with the same blue-lidded butter tub in view. However, there's a subtle shift in the positioning of the hands and the butter knife. The right hand still grips the knife, now slightly repositioned, suggesting movement. The butter tub remains closed, and there is no additional evidence of the contents being disturbed. The anticipation of the spread's use is still present, reflected in the slight adjustment of the hands, preparing for the opening of the tub.

#### Sample 41 — During

- Similarity: 0.3268
- Prediction: In this frame, the microwave door is now positioned in a slightly different position, indicating that it has been partially opened. The person's hand is still motionless, suggesting that there is a slight movement in the process of opening or closing the door. The interior of the cabinet remains unchanged, with the kitchen and counter area still visible.
- Reference: Here, the milk bottle appears more prominently in the foreground, its label more visible, confirming its identity as a household dairy product. The red cap now seems more defined and appears to be partially twisted open, indicating recent or imminent use. The angle of the bottle suggests that it has been nudged or moved, possibly by the person whose hands are in view. The surrounding area remains cluttered, with kitchen utensils and containers in close proximity to the bottle, further emphasizing the dynamic nature of this domestic scene.

#### Sample 43 — During

- Similarity: 0.4665
- Prediction: In this frame, the coffee grounds are now in the hands of a hand-held spoon, indicating that they have been stirred. The spoon's surface appears to be slightly dampened, suggesting that the water has been agitated. The cup's contents appear to be more concentrated, suggesting a more gradual movement of the spoon. The hand's motion suggests that there may be a small amount of water in the cup, possibly a drop or two.
- Reference: In this scene, the sugar jar has been grasped by a hand, suggesting an intent to use it. The lid remains closed, but the jar has been relocated slightly to the right, closer to the center of the counter, and it now sits directly beside a plate that holds a teabag. The hand that holds the jar is partially obscuring it, with the thumb positioned near the flip-top lid, possibly poised to open it. The surrounding items remain unchanged, maintaining the casual disarray of a lived-in space.

#### Sample 45 — During

- Similarity: 0.4194
- Prediction: In this frame, the spoon is now positioned in a hand-held position. The spoon's surface is slightly tilted, indicating that it has been agitated. The hand's motion is evident, suggesting that the spoon has been exerted more or less on the spoon.
- Reference: In this scene, the jam is in the process of being transferred from the jar to the mixing bowl. It is stretched between its container and the fork, creating a slender, slightly curved bridge of jam. The elasticity of this bridge shows the jam's sticky and pliable nature, and the sheen on its surface reflects the light, further accentuating its smooth texture. This intermediate state between the jar and the bowl shows the jam's ability to retain its shape even when being moved.

#### Sample 46 — During

- Similarity: 0.4704
- Prediction: In this frame, the utensil is now in a more streamlined position, with the handle positioned in the middle of the kitchen counter. The person's hand appears to be engaged in rinsing it, indicating that the water has been sprayed on it. The water's surface appears to have been washed away, suggesting that there may have been a small amount of soap or soap residue on the surface.
- Reference: Here, the scissors are seen in a more active state of being cleaned. One blade is covered with white, foamy suds, indicating the presence of soap or detergent. The other blade remains visible and gleams even more prominently, possibly due to the cleaning. The hands grip the scissors in a manner suggesting that they are being scrubbed or brushed, and there's a clear intention to thoroughly clean the instrument.

#### Sample 51 — During

- Similarity: 0.4046
- Prediction: In this frame, the bin's lid is positioned in a slightly different position, indicating that it has been partially opened. The lid's position remains unchanged, suggesting that the lid is partially open, and the contents of the bin remain intact. The object's surroundings remain blurred, implying that there is a slight movement in the process of opening the lid.
- Reference: In this frame, the filter is now fully exposed, held aloft between the person's hands. The debris that was hinted at in the previous frame is now clearly visible, showing a collection of dust, lint, and possibly pet hair clumped together along the folds of the filter's mesh. This accumulation signifies that the filter has been actively filtering out these particles from the environment. The color contrast between the collected dirt and the original white of the filter accentuates the filter's need for cleaning or replacement. The fingers of the person handling the filter are splayed, indicating a gentle yet firm grip, likely to avoid damaging the filter or spilling the trapped debris.

#### Sample 56 — During

- Similarity: 0.4348
- Prediction: In this frame, the milk carton has been placed in a new position. The person's hand is positioned at the top of the box, indicating that the milk has been poured into the container. The contents of the container are still visible, including the milk, as well as the milk's contents. The box's interior appears to have been partially emptied, suggesting that the contents may have been discarded.
- Reference: In this frame, the packaging is further crumpled, with more pronounced deformations. The hand actively pinches the packaging near its center, causing creases and folds to form. The metallic material shows increased signs of manipulation, with the reflective surface now marred by irregularities from the pressure being applied. The crumpling action is more evident here, as the hand's grip tightens to compact the material further.

#### Sample 57 — During

- Similarity: 0.3757
- Prediction: In this frame, the pot's lid has been removed from the burner, indicating that it has been placed in a different position. The person's hand appears to be holding the pot, implying that the lid is still in the position of its original position.
- Reference: In this view, the filter is captured mid-removal, slightly lifted from the coffee maker's well. The moist coffee grounds cling together, exhibiting the filter's effectiveness in maintaining the grounds' mass without spillage. The filter shows a slight deformation, likely from the weight of the wet grounds, and the hand's grip has tightened, causing the filter edges to crinkle. The positioning of the hand suggests the intention to dispose of the contents, as it is held away from the body to prevent spillage on clothing.

#### Sample 60 — During

- Similarity: 0.3761
- Prediction: In this frame, the squeegee is now held in a more controlled position, indicating that it has been rinsing. The hand's grip is now more firmly held, suggesting that the water is dripping from the hose. The water's droplets appear to be more concentrated than before, suggesting a change in the direction of the movement.
- Reference: In this scene, the coffee pot is again within the sink, but now, the user is directly interacting with the lid mechanism. The hand grips the lid, which is angled slightly open, likely to rinse or wash its interior components. Water, along with some frothy soap suds, remains on the exterior surface of the pot. The pot's spout is directed downward, indicating that any residual liquid inside might be draining out.

#### Sample 61 — During

- Similarity: 0.3383
- Prediction: In this frame, the table is now positioned in a more natural position, with a slightly different shape than the previous frame. The hands are now more engaged in the action, indicating that the table has been placed in the correct position. The table's surface appears to have been moved, suggesting that it has been adrift, possibly due to a hand-held device.
- Reference: The crumb has undergone a subtle but noticeable shift; it now appears slightly displaced from its original position, indicating the initial stages of being swept by the vacuum cleaner's suction. The change in lighting around it suggests movement, with a slight blur to its edges caused by the motion of the tablecloth or the disturbance in the air from the vacuum. There's a sense of dynamic transition, as the crumb is caught in the moment between stillness and being vacuumed away.

#### Sample 62 — During

- Similarity: 0.3770
- Prediction: In this frame, the flour has been added to the mixture, indicating that it has been incorporated into the dough. The texture of the dough is more consistent, with a smoother texture and a more uniform texture. The hand's motion is more pronounced, suggesting that the dough has been placed in a pre-mixed state.
- Reference: The olive oil bottle is now in a more pronounced tilted position, and the cap has been removed, revealing the dark opening at the top ready for dispensing the oil. The hand's grip on the bottle appears firm, suggesting a deliberate action is about to take place. However, there's no visible stream of oil yet, indicating the pouring has not started. The anticipation of the oil being added to the contents of the bowl builds as the hand positions the bottle directly above the bowl's rim, preparing to combine the liquid with the other ingredients.

#### Sample 63 — During

- Similarity: 0.4838
- Prediction: In this frame, the tomato has been placed in a bowl with a spoon, indicating that it has been agitated. The spoon's motion indicates that the ingredients have been incorporated into the bowl, implying that the contents of the bowl have been stirred together. The container's surface appears to be slightly tilted, suggesting that there may be a slight movement in the direction of the mixing process.
- Reference: The contents of the bowl show signs of being mixed, as the egg's yolk now presents a disrupted surface, with strands of the albumen beginning to blend into the yolk. The pepper specks are more widely distributed, some sinking into the depths of the egg mixture, while others cling to the emerging strands of egg white. The fork's position has changed, implying it has been used to stir the ingredients together, but the mixture remains only partially combined with clear distinctions between the yolk and the whites still visible.

#### Sample 73 — During

- Similarity: 0.2925
- Prediction: In this frame, the scrubbing brush is now in the hands of a more experienced person, indicating that the water has been sprayed on it. The person's hand appears to be holding the brush, suggesting that the brush has been washed away. The brush's surface appears to have been cleaned, suggesting a thorough cleaning of the surface.
- Reference: In this instance, the grid is more level, held steadily in place by the right hand gripping the top edge. The left hand comes into play, with fingers positioned on the lower left corner, possibly exerting a slight force to maintain the grid's balance or to manipulate it further. The sink appears wet, and the grid itself shows evidence of water exposure, as indicated by the water droplets clinging to the metal bars and reflecting the ambient light.

#### Sample 74 — During

- Similarity: 0.4332
- Prediction: In this frame, the spoon's position has changed slightly, indicating that it has been agitated by a hand. The hand's motion is more pronounced, suggesting that the spoon is agitating the surface of the bowl. The bowl's surface appears to be slightly dampened, possibly due to a spill or spill.
- Reference: The scale has been moved closer to the center of the countertop, and it is now directly adjacent to the bowl containing the flour. It is still turned off, with no numerical display visible, which implies that it has not yet been used for weighing. Its position relative to the bowl suggests preparation for measuring ingredients, as it is now in a more convenient location for the person to transfer contents into the bowl. The surrounding kitchenware and ingredients remain unchanged, maintaining the scene of an active kitchen environment.

#### Sample 77 — During

- Similarity: 0.3941
- Prediction: In this frame, the button appears to be in a new position, indicating that it has been pressed. The fingernail is now positioned in the center of the button's handle, implying that the hand is pressed against the button. The hand's motion is more pronounced, suggesting that the button has been touched.
- Reference: The milk container's lid has been slightly loosened in this frame. The hand's grip on the container has tightened, indicating a deliberate action to open it. There's a slight tilt to the container, suggesting the user might be trying to pour or check the contents inside. However, the lid is not entirely off, and no milk has been dispensed yet.

#### Sample 83 — During

- Similarity: 0.4134
- Prediction: In this frame, the lid has been removed from the jar, indicating that it has been placed in a new position. The person's hand is now positioned in the middle of the container, implying that they are preparing to open the lid. The contents of the lid remain intact, with the lid still firmly attached to the container.
- Reference: In this snapshot, the jar of pesto has been opened, and its rich, verdant contents are more exposed to the viewer. The cap has been removed, revealing a full jar with pesto filled almost to the brim. The texture appears thick and consistent, with specks of ingredients like basil, garlic, and pine nuts scattered uniformly throughout. A spoon or some instrument has been inserted into the pesto, possibly taking out or stirring the contents.

#### Sample 84 — During

- Similarity: 0.4166
- Prediction: In this frame, the microwave's lid is positioned in a slightly different position, indicating that it has been opened. The person's hand appears to be holding the lid, presumably to prevent the microwave from igniting, implying a slight movement. The kitchen's lighting is still dim, suggesting that the microwave may be preparing for a meal or other meal.
- Reference: The hand has withdrawn from the socket area, suggesting that the toaster has been activated. There are no visible changes to the toaster's external appearance, as the mechanical action of starting the toasting process is internal. The kitchen counter remains unchanged, and the toaster maintains its polished metallic sheen. The cable runs from the back of the toaster and is plugged into the same double socket as before, indicating continuity in the scene.

#### Sample 86 — During

- Similarity: 0.2777
- Prediction: In this frame, the bag appears to be in the hands of the person who is holding it. The person's hand is positioned in the middle of the bag, indicating that the bag has been opened. The bag's contents are still visible, but there is a slight shift in the direction of the movement of the hand. The hand's motion is more pronounced, suggesting that the person is holding the bag.
- Reference: In this snapshot, the leek is in the midst of a dynamic, albeit unintended, journey as it descends towards the floor. The white end, previously pointing downwards, now inclines towards the camera, hinting at a flipping motion. The plastic wrap has loosened in places, a testament to the forces at play, and the leek's green tops appear more splayed, no longer neatly aligned due to the movement. The blurring of its edges suggests a swift motion, further highlighting the unexpected descent.

#### Sample 88 — During

- Similarity: 0.4652
- Prediction: In this frame, the lid of the jar has been removed from the container. The hand is now holding the lid, indicating that the contents of the container have been removed. The lid's position remains unchanged, suggesting that the lid has been partially removed.
- Reference: The container now appears more open, the lid fully removed and set aside, indicating a progression in the act of uncovering the food within. The slices of cheese are displayed more prominently, their full circular shapes and pale coloration more apparent against the deeper tone of the container's base. The hands reposition slightly, suggesting preparation for the next action, perhaps to extract a slice or to further inspect the contents.

#### Sample 89 — During

- Similarity: 0.4229
- Prediction: In this frame, the light bulb has moved away from its original position, indicating that it is now in a more natural position. The light source's focus remains on the bulb, which is still visible in the background, and the surrounding area, which appears to be a reflection of the light source, has been blurred, suggesting that the light is moving away from the bulb.
- Reference: The container appears to be at a slightly different angle, giving an impression of being either moved or possibly tilted. It continues to reveal its label, with the blue and green graphics more prominent in this frame. The white cap remains off, placed close to the base of the container. Nearby objects and the counter’s surface indicate that the location remains consistent with the previous frame.

#### Sample 90 — During

- Similarity: 0.4110
- Prediction: In this frame, the peach has been partially sliced, with the skin still firmly attached to the stem. The knife is now positioned in the middle of the fruit, revealing a sprinkling of flesh on the side of the peel. The hand's grip remains firm, indicating that the peel has been slicked into the flesh.
- Reference: Here, the pepper appears more prominently in the foreground, having been repositioned and partially sliced into segments. It rests with the interior facing upwards, revealing a pale inner flesh, ridged with white membranes that cradle a cluster of seeds at the stem end. The slices are clean and the pepper's structure remains intact, though it is now open and exposed, with the previously concealed interior now in view.

#### Sample 92 — During

- Similarity: 0.4841
- Prediction: In this frame, the sink has been moved to a new position, indicating that the water has been drained. The person's hand is now positioned in a more natural position, with the sink's surface exposed, suggesting a gradual change in the direction of the water's movement.
- Reference: The plate now appears in a different orientation, held by a hand wearing a silver watch, suggesting a right-handed individual. It is captured at an angle that exposes its circular form and the slightly upturned edge. The plate’s underside is more visible, revealing a manufacturer's stamp and a ring of unglazed porcelain where the plate would sit during firing. Droplets of water are scattered across the surface, hinting at a recent wash. The fingers are curled around the edge, gripping it securely, and there’s a dynamic tension as if the plate is being moved purposefully.

#### Sample 96 — During

- Similarity: 0.4748
- Prediction: In this frame, the lid has been removed from the pan. The person's hand is now positioned on the side of the pan, presumably to remove the contents of the container. The lid's surface appears to have been partially removed, indicating that the contents are still in the pan's packaging.
- Reference: In this moment, the person has partially peeled back the top layer of the plastic seal, starting the process of opening. The opening is at the initial stage, with just the corner of the packaging being lifted. The seal's detachment is most noticeable at the top left corner where the individual's fingers are pulling the material away, revealing a glimpse of the salmon's surface beneath. The packaging still retains its original shape, but the airtight seal has been compromised.

#### Sample 97 — During

- Similarity: 0.3371
- Prediction: In this frame, the box is now in the hands of a person who is attempting to open it. The person's hand is positioned in the middle of the box, indicating that they are preparing to open the box. The box's contents are still visible, but there is a slight shift in the direction of the action, suggesting that the person is focusing more on the contents.
- Reference: In this moment, the cereal is in the process of being poured. A stream of small, flaky, tan-colored cereal pieces cascades from the bag into a bowl held below with the same hand that was holding the bag open in the previous frame. The flow of the cereal is steady, indicating that the bag has been tilted sufficiently to allow the contents to exit freely. The flakes catch the light as they fall, suggesting a light, crispy texture, and they accumulate in the bowl, already containing a modest amount of cereal.

#### Sample 100 — During

- Similarity: 0.3588
- Prediction: In this frame, the refrigerator door is positioned in a slightly different position from the previous frame, indicating that it has been partially closed. The door's position remains unchanged, suggesting that there is a slight movement in the process of closing the door. The surrounding environment is more reminiscent of a kitchen setting, with a light source and a nearby kitchen counter.
- Reference: In this image, the environment has transitioned into a state of semi-darkness, with the light source significantly reduced. The glow that previously brightened the entire room is now subdued, with shadows beginning to dominate the space. The reflective surfaces that once gleamed under the light now present muted reflections, and the overall visibility in the room has decreased. It appears as though the light source is in the process of being extinguished, capturing the room in an intermediate stage between light and dark.

#### Sample 103 — During

- Similarity: 0.4463
- Prediction: In this frame, the person's hand is more focused on the kitchen counter, indicating that there's been a shift in the position of the stove. The counter's surface appears to be slightly tilted, suggesting that there may be a slight movement in the direction of the counter. The countertop's position remains unchanged, with the counter and counter still positioned in the same position.
- Reference: In this scene, the countertop presents a cleaner appearance with a much-reduced number of visible items. The wet area has expanded, with the sheen of water covering a larger portion of the surface, hinting at a more thorough wipe-down. The sink is now in full view, showing evidence of recent use with water stains around the drain. The countertop's surface is smooth and uninterrupted, devoid of the dish rack and kitchenware previously seen, suggesting they have been moved or tidied away.

#### Sample 105 — During

- Similarity: 0.4809
- Prediction: In this frame, the bowl has been placed in a different position, indicating that the water has been drained. The person's hand appears to be holding the bowl, implying that they are attempting to rinse it. The bowl's surface appears to have been soiled, suggesting that there may be a slight movement in the process of rinsing the bowl.
- Reference: The saucepan is now being held by a person's hand, with the handle gripped firmly. It's tilted over the sink, allowing the excess liquid to drain away. A small amount of steam can be observed rising from the pan, suggesting that the contents are still hot. The pasta within looks compacted due to the angle of the pan, and it's clear that it's being held in this position to let the water escape through a colander or lid that's being used to retain the pasta.

#### Sample 110 — During

- Similarity: 0.3834
- Prediction: In this frame, the holder of the microwave oven has been moved to a new position, indicating that it has been placed in a different position. The holder's position remains unchanged, suggesting that the oven is still in its original position, and that there is a slight shift in the position of the oven.
- Reference: The chair is now seen at a different angle and slightly further away from its original position under the table. The cushion is still visible, and the chair's wooden frame has come into clearer view, indicating that it has been pulled back or to the side. The tablecloth and table surface are no longer in the immediate vicinity of the chair, emphasizing its movement. The lighting conditions remain consistent with the first frame, and the shadow cast by the chair has shifted accordingly.

#### Sample 113 — During

- Similarity: 0.4828
- Prediction: In this frame, the sink appears to be in a more concentrated state, with a larger portion of the surface exposed. The person's hand is now more likely to be holding the sink, indicating that the water has been drained. The sink's surface appears to have been soaked in water, suggesting that it has been washed away.
- Reference: In this frame, the burner cap still shows signs of soiling, but there's a noticeable change in its appearance. The central area and the edges look slightly cleaner, revealing the metal's original color and sheen beneath the once-uniform layer of grime. It's clear that some of the residue has been scrubbed off, as evidenced by the lighter patches and streaks on the cap's surface. Water continues to bead on the cap, and the person's hands show more purposeful movement, indicating a more thorough cleaning action is taking place.

#### Sample 116 — During

- Similarity: 0.4207
- Prediction: In this frame, there's a noticeable difference in the position of the bowl. The bowl's surface appears to be slightly tilted, indicating that it has been agitated, possibly by a hand or a chopping motion. The object's position remains unchanged, suggesting that the bowl has been placed in a different position.
- Reference: The focal point in this scene continues to be the white bowl with diced sweet potatoes. They seem to be soaking in a liquid, possibly water or a marinade. This liquid gives the sweet potatoes a slightly glossy appearance. Surrounding the bowl are other ingredients, including a clear container holding what looks like a slice of lemon, two cans that seem to contain some sort of sauce or preparation, and a packaged item with indistinct labeling. The area appears slightly tidier compared to the previous frame.

#### Sample 119 — During

- Similarity: 0.4843
- Prediction: In this frame, the utensil is now held in a more controlled position, with the water dripping onto the surface. The person's hand is now more likely to be holding it, indicating that the water has been rinsing it.
- Reference: The V60 is now captured at a different angle, partially lifted out of the water, allowing a clearer view of its condition. It's being held by the rim, fingers gripping the upper edge, revealing a glimpse of the inner filter area that still contains some residual coffee grounds or staining. The motion of the water around it suggests that it is being actively cleaned, likely involving a swirling or shaking action to dislodge any remaining coffee debris.

#### Sample 124 — During

- Similarity: 0.3870
- Prediction: In this frame, the lettuce has been rearranged in a more streamlined fashion, with a slightly different shape and texture. The leaves are more uniformly arranged, indicating that they've been added to the salad. The hands are now more involved in the process of preparing the salad, implying that the ingredients have been incorporated into the salad's composition.
- Reference: In this instance, the spoon's orientation has shifted; it now rests within the confines of the plate, cradling a small portion of the meal's remnants. The bowl of the spoon is partially obscured by food particles, indicating it has been actively used. The utensil's handle reflects a secure hold within the individual's grasp, and the angle of the spoon suggests a motion of scooping or scraping the plate. The wooden texture remains visible, though slightly less pronounced due to the overlay of food.

#### Sample 127 — During

- Similarity: 0.4231
- Prediction: In this frame, the rag is now in a more concentrated state, indicating that the water has been drained out of the cloth. The rag's surface appears to be a bit damper, suggesting that there may have been a few drops of water dripping onto the fabric. The person's hand is now more firmly gripped, implying that they are attempting to remove the excess water.
- Reference: The faucet is now in a different state with the handle lowered towards the sink, reducing the water flow to a mere trickle. The diminished water stream produces less disturbance in the sink basin, resulting in a calmer surface with only a few ripples emanating from the point where the water meets the stainless steel. The handle's position closer to the sink indicates the tap is in the process of being turned off.

#### Sample 131 — During

- Similarity: 0.2826
- Prediction: In this frame, the rag is now in the hands of a person who is scrubbing it with a cloth. The person's hand is now more firmly held, indicating that the cloth has been washed. The cloth's surface appears to be damp, suggesting that the water has been sucked out of the cloth.
- Reference: In this scene, the grid is being held at a slightly different angle, with the person's hand gripping it firmly. The fingers are wrapped around one edge, implying a secure hold, likely in the midst of turning or positioning the grid. The grid remains yellow and retains its pattern of square openings, but the perspective has changed slightly, offering a view that emphasizes the grid's thickness and the shadows cast by the overhead lighting. This perspective also gives a clearer view of the sink and the countertop, reinforcing the domestic setting.

#### Sample 133 — During

- Similarity: 0.4583
- Prediction: In this frame, the lid of the jar has been removed from the container. The lid is now positioned in the middle of the container, indicating that it has been opened. The person's hand appears to be attempting to open the lid, implying that the lid has been partially closed. The contents of the lid are still visible, with the lid's surface exposed.
- Reference: In this stage, the can's lid shows more progress in the opening process. The cutting has advanced around the circumference, and the lid now has a larger exposed area, almost half of it separated from the rim. The hand grips the can opener at a different angle, suggesting the action of turning the tool has continued from the initial puncture. The manual can opener's cutting wheel has moved along the lid, leaving a jagged metal edge in its wake.

#### Sample 140 — During

- Similarity: 0.4344
- Prediction: In this frame, the towel is now in a more streamlined position, with a slightly different shape. The person's hand is now positioned on top of the towel, indicating that the towel has been placed on the table. The towel's surface appears to have been taken apart, suggesting that it may have been thrown or washed.
- Reference: The hand's grip on the glass has slightly shifted, and it seems to be in the process of either lifting or moving the glass. The amount of liquid in the glass appears consistent with the previous frame, suggesting no spillage has occurred in the interim. The glass is hovering just above the wooden table, and its shadow, albeit blurry, can be discerned on the table surface beneath.

#### Sample 142 — During

- Similarity: 0.4129
- Prediction: In this frame, the lid has been removed from the sink, indicating that it is now in the hands of a person. The person's hand appears to be holding the lid, implying that the lid is still attached to the sink.
- Reference: The frame offers a clearer view of the kitchen setting, but the sausage remains elusive. While the person's hands dominate the frame, drawing attention to the plate they're holding, the sausage is not directly visible. It's plausible that the sausage is now beneath the plate, given the positioning and movement of the hands, indicating an action related to covering or unveiling.

#### Sample 145 — During

- Similarity: 0.4527
- Prediction: In this frame, the fruit has been partially sliced, with the skin still firmly attached to the stem. The knife's grip is now more pronounced, indicating that the knife has been inserted into the fruit. The fruit's flesh is now firmly pressed against the skin, revealing a smoky appearance.
- Reference: In the second image, the piece of pitta is being interacted with; the person's fingers are grasping one edge of it. This handling causes a slight curvature in the bread, making the middle portion elevate a tad, readying it for the dipping process. The fingers appear to be holding the pitta gently, ensuring it doesn't break or crumble, maintaining its structural integrity. The subtle shadows cast by the fingers on the bread accentuate its textured surface.

#### Sample 149 — During

- Similarity: 0.4207
- Prediction: In this frame, the scrubbing tool is now in the hands of a more experienced person, indicating that the water has been washed away. The person's hand appears to be holding the tool in the hand, implying that it has been sprayed with water. The object's surface is slightly different from the previous frame, suggesting that there may have been a change in the position of the brush.
- Reference: The cutting board remains the focal point, now wet, indicating the commencement of the rinsing process. Water droplets and streams can be seen on the surface, reflecting light and giving the board a glossy sheen. This change in texture from dry to wet is the most noticeable difference. The countertops around still hold the same items, untouched from their position in the previous frame, reinforcing the singular focus of the activity on the board itself.

#### Sample 150 — During

- Similarity: 0.2640
- Prediction: In this frame, the kettle's handle is positioned in a slightly different position from the previous frame, indicating that it has been agitated. The person's hand appears to be holding the kettle, implying that they are adjusting the temperature of the water.
- Reference: The spice is now more visible, suggesting that some items have been moved or repositioned. The surroundings still include various kitchen items, but the focus is increasingly on the spice. The proximity of a hand to the spice indicates imminent interaction or the possibility that the spice will be picked up or moved shortly. The spice has not yet been completely taken out, but it's clear that it's in the process of being accessed.

#### Sample 153 — During

- Similarity: 0.4257
- Prediction: In this frame, the person's hand is more focused on the kitchen counter, indicating that there's been a change in the position of the sink. The surface of the countertop appears to have been wiped down with a damp cloth, suggesting that there may be a slight movement in the process of cleaning the countertop.
- Reference: In this instance, the pepper mill is grasped firmly in the hand, suggesting that the previous state of falling has been arrested. The hand's grip is tight around the pepper mill's middle section, which is often designed to be ergonomically suitable for such a hold. The other hand remains in contact with the cloth, possibly stabilizing the situation or preparing to resume cleaning. The orientation of the pepper mill is now more vertical, indicating control has been re-established over its movement.

#### Sample 158 — During

- Similarity: 0.4269
- Prediction: In this frame, the kitchen sink has been moved to a new position, with a more streamlined appearance and a sharper focus on the surface. The kitchen counter is now positioned in a slightly different position from the previous frame, indicating that it has been placed in the same position as the kitchen counter. The hand-held camera's focus is now more focused on the kitchen area, which is likely a reflection of the kitchen's current state.
- Reference: Now, the orange has begun to move, evident from a slight blurring on one side, indicating the direction of the push. The previously highlighted scars and details are somewhat distorted due to the motion. The area of the table now occupied by the orange is darker, suggesting that the light source is constant, and the orange's position has indeed changed.

#### Sample 160 — During

- Similarity: 0.4516
- Prediction: In this frame, the rag is now in the hands of a person who is holding it. The hand's grip is now more firm, indicating that the water has been drained. The rag's surface appears to be dampened, suggesting that it has been washed away. The palm of the hand is now slightly tilted, suggesting a more gradual movement.
- Reference: The perspective has shifted to provide an overview of the dish drying area. The white dish rack now occupies the central portion of the frame, holding the same white plates and an assortment of utensils and kitchenware, suggesting that no additional items have been added since the last frame. A blue bucket is positioned to the left of the rack, and various cleaning products are visible, hinting at a well-utilized kitchen space. The sink is out of view, but the presence of the dish rack and cleaning items suggests ongoing dishwashing or kitchen cleaning activities.

#### Sample 162 — During

- Similarity: 0.4841
- Prediction: In this frame, the jar's lid is now positioned in a slightly different position, indicating that it has been taken out of its container. The hand's motion indicates that the lid has been removed from the container, implying that the contents are still in the container.
- Reference: The focus of this scene shifts to a transparent blue plastic measuring jug with white markings, which indicate measurements. The jug, which is now the central object being handled, is being retrieved from the same dish rack, revealing its storage alongside everyday kitchen items. It's positioned next to stacked white plates and near a colorful silicone lid, emphasizing the jug's functional role in cooking or baking. The jug’s clear plastic material contrasts with the other opaque items, highlighting its purpose for measuring liquids with precision.

#### Sample 163 — During

- Similarity: 0.4191
- Prediction: In this frame, the person's hand moves closer to the edge of the kitchen counter, revealing a gaping gap in the middle of the counter. The hand's grip is slightly more firm, indicating that the hand is engaged in a more deliberate action, implying a slight shift in the position of the hand.
- Reference: In this frame, the tablecloth appears to have been further unfurled, covering more surface area of the floor and furniture around it. There's a hint of its material and perhaps a design or pattern, although it's not entirely clear due to the dynamic nature of the scene. There's still a sense of movement, suggesting that the action of setting or straightening the tablecloth is ongoing.

#### Sample 166 — During

- Similarity: 0.4623
- Prediction: In this frame, the rag is now in the hands of a person who is holding it. The person's hand appears to be holding it, indicating that it has been agitated. The rag's surface is slightly different from the previous frame's state, suggesting a more gradual movement. The hand's grip is more firm, suggesting that it is exerting more pressure on the cloth.
- Reference: In this scene, the bottle has been rotated slightly counter-clockwise by the person's hand, which is now in direct contact with the cap. The bottle remains on its side, and the cap appears more visible and slightly more secured than before, although not yet fully closed. The person's wristwatch is now more prominent, indicating the passage of time or perhaps a change in the angle of the hand's movement. The environment remains unchanged with the same array of cleaning products around, emphasizing the continuity of the setting.

#### Sample 169 — During

- Similarity: 0.4862
- Prediction: In this frame, the rinsing spoon is now held in the hands of a person who is preparing to rinse it. The hand's grip is now more firm, indicating that the water has been sucked out of the spoon, allowing the water to drain away from the spoon's surface.
- Reference: In this stage, the person has altered their grip on the tray, securing it with both hands while water continues to cascade over its surface. The shift in position has led to a visible change in the residue pattern; there are now clear streaks where the water has begun to dislodge and wash away some of the charred material. The water's impact is most noticeable where it hits the surface directly, demonstrating the initial effectiveness of the rinsing action in removing the burnt remnants.

#### Sample 170 — During

- Similarity: 0.4149
- Prediction: In this frame, the chicken is now in a more streamlined state, with a slightly different shape and texture. The chicken's surface appears to have been steamed, indicating that the cooking process has begun. The hand's movements indicate that the chicken has been placed in the pan, possibly to prepare for cooking.
- Reference: The hand appears to have completed the action of seasoning, as evidenced by the change in the positioning of the spice shaker, now held with a more relaxed grip. The distribution of the spices on the tomatoes is more apparent, with individual grains of the darker spice visible against the vibrant red of the sliced tomatoes. The tomatoes exhibit a glistening surface, likely due to the freshly applied seasoning interacting with the tomato juices, enhancing the visual appeal and suggesting a readiness for the next step in preparation or consumption.

#### Sample 171 — During

- Similarity: 0.4551
- Prediction: In this frame, the rice appears to be a bit more seasoned, with a more sprinkling of salt. The spoon's movements seem to be more deliberate, indicating that the rice is being stirred. The water's consistency is more uniform, suggesting that the water has been drained out of the rice.
- Reference: In this frame, the oat seems to exhibit signs of subtle movement. There's a hint of displacement, as the oat's edges show slight shifting from their original position. The overall spread remains relatively uniform, but there are indications of mild disturbances within the surface, suggesting that some agitation or mixing might have taken place. The oats still retain their raw appearance, with no evident signs of cooking or moisture absorption.

#### Sample 174 — During

- Similarity: 0.2678
- Prediction: In this frame, the carrots appear to be in a more concentrated state of cooking, indicating that they have been added to the pan. The color of the vegetables appears to be more vibrant, suggesting that they've been preparing for a longer time. The greens are now more visible, with a slightly darker hue contrasting against the greens.
- Reference: The colander, still held by the person's hand, now appears to be in a slightly different position, closer to a stainless steel sink. The mix of beans remains inside, glistening with moisture, indicating that they are still wet from rinsing. A few beans seem to be closer to the edge, perhaps ready to fall out if the colander is shaken more vigorously. Adjacent to the colander are kitchenware items such as cups and bowls, and nearby are opened cans, giving context to a meal preparation.

#### Sample 182 — During

- Similarity: 0.3892
- Prediction: In this frame, the towel's handle is now more firmly held, indicating that it has been taken apart. The hand's motion is more pronounced, suggesting that the towel is still in its original position. The object's shape is more apparent, implying that the hand is holding the towel in a slightly different position than the previous frame.
- Reference: The scene is centered around the base of the washing machine, where a single black sock with a green toe and heel accent lies on the yellowish floor, indicating it might have been dropped inadvertently. The blue detergent box from the previous scene is still present, now more prominently in view. The washing machine's door remains open, but the clothes inside are not the main focus of this frame either, suggesting a pause in the laundry process.

#### Sample 184 — During

- Similarity: 0.4529
- Prediction: In this frame, the box's contents are now more visible. The person's hand is now more engaged in the action of removing the contents from the box, indicating that the contents have been removed. The contents of the box are now in the hands of the person who is holding the box.
- Reference: In this snapshot, the top of the cereal box has been successfully opened, revealing an inner packaging which is typically a plastic bag that holds the cereal to maintain its freshness. The hands have pulled the flaps fully apart, and the inner bag is now visible, with multiple folds indicating that it has not yet been disturbed. This bag appears to be still sealed, and the cereal remains contained within, unseen. The anticipation of the cereal's appearance is palpable as the next step will likely involve opening this inner seal.

#### Sample 185 — During

- Similarity: 0.4227
- Prediction: In this frame, the microwave's lid is positioned in a slightly different position, indicating that it has been touched. The person's hand appears to be holding the oven door open, implying that they are preparing to open the door. The kitchen's interior remains unchanged, with the kitchen counters and counters still visible, as well as the door's surrounding furniture.
- Reference: In this scene, the temperature display reads a much higher value of 556, an unusual and likely erroneous display since conventional ovens typically don’t reach such extreme temperatures. This could indicate that the user is in the process of setting or adjusting the temperature and has possibly overshot the desired temperature setting. The user’s action of turning a knob, usually associated with increasing or decreasing the oven's temperature, supports this. The digits are bright and unambiguous against the dark background of the oven’s control panel.

#### Sample 187 — During

- Similarity: 0.4118
- Prediction: In this frame, the pot is now in a more natural state of motion, with the lid still firmly attached to the pot, indicating that it has been agitated. The hand's movements are more pronounced, suggesting that the pot has been placed on the counter or in the kitchen counter. The pot's surface appears to be slightly tilted, possibly due to the movement of the hand or the pot itself.
- Reference: In this scene, the individual is engaged in the process of washing their hands over the sink, which suggests an intermediate step between handling the chicken. The chicken is not visible in this frame, but the action indicates a pause in the preparation process, likely for hygiene purposes after having manipulated the raw chicken. The running water and the posture of the hands being rubbed together are clear indications of thorough cleaning, which is a critical step in preventing cross-contamination in the kitchen.

#### Sample 189 — During

- Similarity: 0.3551
- Prediction: In this frame, the cheese has been placed on a cutting board. The knife's edge is now positioned at the center of the cutting board, indicating that the knife has been inserted into the cheese. The cheese's surface appears to have been sliced, with a thin layer of cheese embedded in the surface, suggesting that the cheese is being sliced.
- Reference: The cake, still maintaining its crumbly texture on the surface, has now been further reduced in size. An additional portion has been sliced away, and this new slice showcases the cake's uniform interior, which is noticeably darker than its topping. The golden topping creates a stark contrast against the darker, moist center. Now, more than half of the cake remains on the plate, with its exposed interior providing a glimpse into its delectable consistency.

#### Sample 198 — During

- Similarity: 0.4509
- Prediction: In this frame, the tea towel has been placed in a new position. It is now more firmly held, indicating that it has been taken apart. The person's hand is still holding the towel, implying that they are holding it in their hands. The towel's surface appears to be slightly dampened, suggesting that it may have been partially soaked.
- Reference: In this frame, the bowl remains in the same general vicinity, but there's a noticeable difference in its presentation. A striped blue and white towel with flower patterns is now draped over part of the bowl, covering a portion of its opening. The towel does not completely obscure the bowl's interior, but it significantly reduces the visibility of its contents. Nearby objects, such as the sandwich press and red bag, remain in their previous positions.

#### Sample 203 — During

- Similarity: 0.3631
- Prediction: In this frame, the bottle is now in the hands of a hand-held device, indicating that it has been taken out of its container. The hand's motion is evident, suggesting that the bottle has been placed in a position where it can be easily accessed. The bottle's contents are clearly visible, with the lid still firmly attached to the bottle.
- Reference: In this instance, the squash is shown at a different angle, slightly more elevated than before, allowing a view of its side. The grip on the squash has changed; the fingers seem to be more spread out, adjusting the balance and grip as the squash is being manipulated. The skin of the squash still appears undamaged and firm, reflecting its freshness. The motion blur around the fingers suggests a swift, yet controlled movement.

#### Sample 209 — During

- Similarity: 0.4841
- Prediction: In this frame, the pan is now positioned in a more streamlined position, indicating that the pan has been heated. The pan's surface appears to be a bit hotter, suggesting that the cooking process has started to take a step forward. The surface of the pan appears to have been heated to a medium-high temperature, implying that the heat has intensified. The spoon's motion indicates that there is a slight movement in the pan, which may indicate that the skillet is heating more quickly.
- Reference: In this frame, the omelette looks further along in the cooking process. Most of its surface now exhibits a matte finish, suggesting that the egg mixture has solidified more uniformly. There are fewer evident runny or liquid portions, implying a consistent heat distribution and continuous cooking. The edges of the omelette seem slightly curled up, hinting at a potential readiness for flipping or folding.

#### Sample 210 — During

- Similarity: 0.4746
- Prediction: In this frame, the kitchen sink has been sanitized, indicating that it has been thoroughly washed. The person's hand is now more focused on the sink, suggesting that the water has sucked away some of the soapy residue. The sink's surface appears to be a bit damper, possibly due to the presence of a small amount of soap on the surface. The hands are now more engaged in the process of scrubbing the sink to remove any remaining soap residue.
- Reference: In this perspective, the soap appears more foamy and sudsy, with a thicker layer of soap suds on its surface. The surrounding area is more cluttered, and the soap is now at an angle, which implies a vigorous scrubbing motion has been applied. The increased number of soap bubbles suggests that the soap has been more actively used, possibly with more water added to generate lather. The grip on the soap has shifted, indicating a different angle or approach to washing has been taken.

#### Sample 211 — During

- Similarity: 0.4150
- Prediction: In this frame, the water is now more concentrated, indicating that it has been drained. The hands are now more engaged in the process of rinsing, implying that the water has soaked into the fabric, resulting in a more concentrated stream of water. The cloth's surface appears to be more damp, suggesting that there may have been a slight movement in the direction of the water's movement.
- Reference: The sink now displays evidence of cleaning activity. There are streaks of moisture across the basin, particularly around the drain, indicative of a wiping action. To the right of the sink, cleaning implements including a sponge and a metallic scrubber can be seen, along with a spray bottle, likely containing a cleaning agent. A black-handled frying pan and other kitchen utensils are drying in a white dish rack. The individual's hands are still present, with the right hand grasping a carrot peel, possibly preparing to discard it, while the left hand rests on the counter, not actively engaged in the cleaning process.

#### Sample 212 — During

- Similarity: 0.3987
- Prediction: In this frame, the person's hand is positioned in a slightly different position, indicating that they are preparing to open the door. They are now able to see through the door's window, which has been partially closed, and their fingers are still pointing at the door, suggesting that the door is still open. The person in the position of the hand is more likely to be holding the door closed, implying a slight movement in the process of opening the door or closing it.
- Reference: This frame captures the oven timer in an out-of-focus state, with the camera motion suggesting a swift movement either of the camera or the user's hand. Due to the blurriness, the exact time on the timer cannot be determined. However, the blue illumination of the timer's display persists, which continues to indicate active use. The surrounding environment is also blurred, emphasizing the motion and rendering details indistinct.

#### Sample 216 — During

- Similarity: 0.4286
- Prediction: In this frame, the kettle's lid is positioned in a slightly different position, indicating that it has been agitated. The person's hand appears to be holding the kettle, implying that they are preparing to cook. The kettle remains in the same position as in the previous frame, with the lid still in place.
- Reference: Here, the coffee remains untouched and static, maintaining its dark coloration that suggests it is still hot and freshly made. There is no visible motion or disturbance to the surface, and the coffee's consistency appears smooth, without any signs of separation or layering that sometimes occur as an espresso settles. The positioning of the cup is unchanged from the prior frame, reinforcing the lack of interaction since the espresso was poured. The coffee's stillness hints at a brief interlude between brewing and consumption.

#### Sample 217 — During

- Similarity: 0.4120
- Prediction: In this frame, the lid has been removed from the sink, indicating that it has been placed in a different position. The person's hand appears to be holding the lid, implying that the lid is still in the position of its original position. There is a slight shift in the angle of the lid's position, suggesting that the water has been drained from the bottom of the sink. The lid remains in the same position as in the previous frame.
- Reference: In this blurred frame, the action is captured mid-motion, reflecting a swift movement. The basket, now moving, is at the center, creating a whirl of colors around it. The person's hand is a blur, indicating the rapid movement of opening or possibly detaching the basket from the appliance. The background is indecipherable due to the motion blur, but splashes of orange and white suggest the continuation of the kitchen counter's cluttered state. The focus is solely on the action and the basket, with details obscured by the speed of the movement.

#### Sample 220 — During

- Similarity: 0.3956
- Prediction: In this frame, the rinsing spoon is now in the hands of a more experienced person, likely a chef. The spoon's surface appears to be slightly damper than before, indicating that the water has been drained. The hand's grip is slightly more firm, suggesting that the spoon is being held more or less still.
- Reference: Here, the cucumber is positioned under a running tap, with a stream of water cascading over its curved surface, which suggests the washing process is ongoing. The hand gripping the cucumber adjusts its hold, now supporting it from underneath to allow the water to run along its entire length. The pressure of the water causes slight ripples along the skin of the cucumber, and droplets bounce off, creating a dynamic scene where the focus is on ensuring the vegetable is thoroughly cleansed.

#### Sample 222 — During

- Similarity: 0.4897
- Prediction: In this frame, the rag is now more firmly held, indicating that the water has been drained. The hands are now more engaged in the process of rinsing the cloth, which is likely a sign of the drying process.
- Reference: In this frame, the sponge still looks damp but less engorged compared to the previous state, suggesting that a significant amount of water has already been wrung out. The grip on the sponge has been relaxed, allowing it to expand slightly, but it maintains a compressed shape due to the residual pressure from the fingers. The water is no longer being ejected with the same intensity, implying that the action of squeezing has been partially released.

#### Sample 225 — During

- Similarity: 0.2570
- Prediction: In this frame, the blender's lid remains firmly attached to the bowl, indicating that it has been removed from the bowl. The user's hand appears to be engaged in a more deliberate action, implying that he is attempting to remove the lid from the blender. The surrounding area, including the bowl's interior, remains unchanged, suggesting that the blender has been placed on the counter.
- Reference: There is a notable reduction in the streaking of the mixture, indicating a progression toward uniformity. The color is now more consistent throughout, without the distinct white areas seen previously, implying a better combination of ingredients. The texture is creamier, and the previous soft peaks have started to settle into a more cohesive batter. The beaters are well-coated, and the mixture exhibits a sheen, suggesting the development of a silky structure, characteristic of a well-emulsified blend.

#### Sample 226 — During

- Similarity: 0.4505
- Prediction: In this frame, the bread has been placed in the hands of the person who is holding it. The person's hand is now more firmly grasped, indicating that the bread is ready to be sliced. The bread's surface appears to have been partially sliced, suggesting that the person is attempting to slice the bread into bite-sized pieces.
- Reference: Here, the scissors have made contact with the wrap, capturing the moment where the blades begin to slice through the material. The wrap's tension appears uneven, with a slight ruffling near the point of contact with the scissors. The person's grip on the wrap and scissors is steady and firm, providing control over the cutting action. The surrounding kitchen items remain unchanged, maintaining the focus on the task at hand. The wrap itself has a slight wrinkle near the cutting area, a common trait when handling such materials.

#### Sample 231 — During

- Similarity: 0.3897
- Prediction: In this frame, the onion has been placed in a new position. The person's hand is now able to grasp the onion's skin, revealing a more revealing appearance. The onion's skin is now more exposed to the camera's light, indicating that the onion is still in its original position.
- Reference: In this frame, the opening of the plastic bag has progressed. The fingers have pried apart the top edges, creating a visible opening through which the contents could be accessed. The plastic is now less tense, and the opening is wider, suggesting the bag’s seal has been broken. The opening's edges curl outward slightly, indicating the flexibility and reduced pressure on the plastic. The contents remain mostly obscured, but the act of opening has caused slight shifts in the position of the potatoes inside.

#### Sample 232 — During

- Similarity: 0.4773
- Prediction: In this frame, the blender's lid is positioned in a slightly different position, indicating that it has been agitated. The lid's surface appears to be a bit damper, suggesting that the blender may be agitating more. The hand's motion is more pronounced, implying that the hand is holding the blender in place. The liquid content of the blender remains the same, with the lid still firmly attached to the blender.
- Reference: In this scene, the ingredient maintains its rich yellow hue and glossy texture, but there is a slight change in the surface consistency. A depression is visible where the hand mixer's blades have just passed through, indicating the mixture’s thickness and ability to hold shape momentarily before settling. This texture suggests that the batter is not too runny, maintaining a certain body that could be suitable for a recipe requiring structural integrity, like a cake or bread.

#### Sample 233 — During

- Similarity: 0.4799
- Prediction: In this frame, the towel is now in a more natural position, with the person's hand holding it. The hand is now more firmly grasping the towel, indicating that it has been placed on the table or counter. The towel's surface appears to be a bit damper, suggesting that the towel has been agitated, possibly by a hand-held device.
- Reference: In this frame, the plate is in motion, captured while being moved swiftly to the left by the person's right hand. Due to the quick movement, the plate and the hand appear slightly blurred. The plate itself is still nearly empty, and the same design details are visible along the rim. The geometric pattern on the tablecloth is more distorted due to the perspective shift, and the shadow of the person’s hand is now cast on the tablecloth, indicating the plate is being moved closer to the table's surface.

#### Sample 236 — During

- Similarity: 0.4438
- Prediction: In this frame, the cheese has been placed on a cutting board. The knife's edge is positioned at the center of the cheese, indicating that the knife has been inserted into the cheese. The cheese's surface appears to have been cut off, suggesting that it has been removed from the cutting board, which is now in a circular motion. The slice of cheese remains intact, with no visible signs of damage.
- Reference: The butter is now showing signs of yielding to the warmth of the room and the pressure from the knife. We can observe that a portion has been successfully spread across the bread's surface, creating a thin, uneven layer. The knife is held at an angle that suggests a forceful application, necessary due to the butter's initial stiffness. Some areas of the butter layer are thicker, indicating the inconsistent texture resulting from the spread of a still somewhat firm butter.

#### Sample 238 — During

- Similarity: 0.2548
- Prediction: In this frame, the bottle is now in a more upright position, indicating that it has been opened. The person's hand is now positioned in the middle of the bottle's opening, implying that the cap has been closed. The lid remains firmly attached to the bottle, suggesting that the seal has been tightened.
- Reference: The jar of flour is now inverted completely, positioned directly above the bowl to maximize the flow of flour. The powdery substance seems to be pouring out more quickly, as evidenced by a thicker stream forming a more substantial pile on top of the previously deposited flour. The white mound in the bowl has grown noticeably, and a cloud of flour dust is more pronounced around the rim of the jar, signifying a brisk pouring action.

#### Sample 240 — During

- Similarity: 0.4290
- Prediction: In this frame, the pot appears to be in a more active state, indicating that the water has reached a boiling point. The pan's surface is now more exposed, suggesting that the cooking process has started to take a turn. The spoon's motion indicates that the liquid has been absorbed into the pot's contents, implying that the pot has been stirred.
- Reference: In this frame, the curry seems to have progressed further in the cooking process. The liquid content appears to have reduced slightly, giving the mixture a denser look. The ingredients are more pronounced and seem to be softening and integrating into the liquid. The color has also darkened a bit, indicating the amalgamation of spices and ingredients, and it exudes a richer appearance.

#### Sample 241 — During

- Similarity: 0.4127
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating that it has been placed in a different position. The surface of the sink appears to be slightly tilted away from the kitchen counter, suggesting that the sink is now positioned in the same position as the sink. The sink's surface appears to have been moved, suggesting a gradual shift in the direction of the kitchen's movement.
- Reference: The ladle appears to have been lifted from the bowl and is now hovering above the plate, with its bowl-end pointing downwards, poised to be placed down. The liquid in the glass remains at the same level, and the surrounding items on the table, such as the remote control, the blue bowl with green beans, and the yellow-lidded container, remain unmoved. The table's surface is visible, showing more of the texture and the edge of the white paper plate in the foreground.

#### Sample 244 — During

- Similarity: 0.3673
- Prediction: In this frame, the utensil has been placed in a different position, with a slightly different angle. The person's hand is now holding it, indicating that the water has been rinsing it. The water's surface appears to be soiled, suggesting that there may have been a bit of debris on the surface.
- Reference: In this instant, the peeler appears to be more engulfed by the sudsy froth, with the sponge compressing even further into its form, pressing the cleansing agents deep into the peeler's joints and blade. The water's flow from the faucet continues uninterrupted, washing away some of the soapy mixture, revealing a bit more of the peeler's handle and the swivel mechanism that allows the blade to adjust to the contours of a potato.

#### Sample 247 — During

- Similarity: 0.2334
- Prediction: In this frame, the utensil is now in the hands of a person who is scrubbing it. The hand's movements are more controlled, indicating that the water has been sucked out of the urn, allowing the soap to settle on the surface. The soap's consistency is more pronounced, suggesting that the soap has a more active role in the cleaning process.
- Reference: In this scene, the blender is still inverted, but now water is actively flowing from the faucet into the blender's interior. The stream of water is causing a bubbly reaction, likely mixing with the remaining residue inside the blender, creating more froth that is visible through the transparent plastic. The lid remains off to the side, and the water's force seems to be targeting the bottom, now the highest point, of the blender's interior.

#### Sample 252 — During

- Similarity: 0.2995
- Prediction: In this frame, the butter has been placed in the hands of a handkerchief, indicating that the knife has been inserted into the butter. The knife's edge is slightly curved, suggesting that the butter is being pressed against the butter's surface. The hand's grip remains firm, with the knife still firmly gripping the butter, implying a slight movement.
- Reference: In this frame, the cake remains largely the same, still maintaining its ringed bundt form. The slice that was previously cut and replaced askew is now absent, removed from the frame entirely. This subtraction leaves a clear demarcation where the slice once was, disrupting the cake's continuity. The doily beneath remains visible, and there are no additional crumbs or changes in the cake's texture or coloration.

#### Sample 253 — During

- Similarity: 0.4673
- Prediction: In this frame, the sponge appears to be in a more active state, indicating that it has been agitated, possibly by a hand or a spoon. The surface of the sponge's surface is more exposed, suggesting that it may have been sprayed with water. The brush's bristles indicate that the sponge has been thoroughly washed, and there are no visible streaks of water on the surface.
- Reference: In this frame, the rag is more distinctly visible, showing its textured surface more clearly. It's still being held firmly, emphasizing its utilitarian function in cleaning. The wetness of the rag is evident, with certain portions appearing more saturated than others. Its edges are splayed out a bit, showcasing its length and breadth.

#### Sample 258 — During

- Similarity: 0.4196
- Prediction: In this frame, the squeegee's hands are now more engaged in the process of rinsing, indicating that the water has been sucked out of the hose. The person's hand is now more focused on the nozzle, which appears to be swiping away the excess water. The water's droplets appear to be more concentrated than before, suggesting that there may be a slight movement in the direction of the rinse.
- Reference: The dish now appears closer to the center of the frame, reflecting a slight shift in focus during the cleaning process. Water droplets and suds cling to its surface, evidencing the use of soap or detergent for cleansing. The presence of a blue scrubbing brush in the sink basin implies that a manual scrubbing action has been or will be applied to the dish. There is less visible residue on the pan's surface compared to the previous state, suggesting that some cleaning has already taken place.

#### Sample 260 — During

- Similarity: 0.4398
- Prediction: In this frame, the kitchen sink has been moved to a new position, with a more streamlined appearance. The surface of the sink is now more cluttered and cluttered, indicating that there is more work to be done, such as scrubbing or cleaning the floor. The kitchen's lighting is now dim, suggesting that there may be a slight movement in the kitchen.
- Reference: In this snapshot, the kitchen counter continues to hold the focal point with a clear sign of the detergent's presence. The wet area on the counter appears more spread out, indicating it has either been smeared or that more detergent has been applied. A hand is more actively involved in the frame, possibly in the midst of wiping or spreading the detergent. Additionally, a bottle, presumably containing the detergent, is in closer proximity, suggesting it might have been used recently.

#### Sample 261 — During

- Similarity: 0.4082
- Prediction: In this frame, the tomato has been placed in the hands of a person. The person's hand is now positioned on the cutting board, indicating that the knife has been inserted into the tomato. The tomato's surface appears to have been sprayed with oil, suggesting that the oil has absorbed some of the oil's moisture.
- Reference: In this subsequent moment, the chilli slices appear to have been more evenly distributed across the pizza's surface. Their distinct red shade contrasts with the surrounding ingredients, making them a standout feature. The edges of some chilli slices look slightly curled, possibly from the knife's pressure during slicing or the natural drying process after being cut.

#### Sample 267 — During

- Similarity: 0.4228
- Prediction: In this frame, the onion has been sliced in half, revealing a new layer of skin. The skin is now more exposed to the knife's action, indicating that it has been partially cut off. The hand's grip remains firm, implying that the knife is now engaged in the process of cutting the onion.
- Reference: In this scene, the can of sweetcorn is undergoing the initial stages of being opened. A can opener has been affixed to the top, its handles gripped firmly in the user's hands. The blade has punctured the lid, as evidenced by the slight separation visible along the can's edge where the opener has begun its work. The opening process appears to be at the very start, with only a small portion of the lid cut, and the sweetcorn remains concealed inside, its state still mostly a mystery beyond the label's promise.

#### Sample 271 — During

- Similarity: 0.3520
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating that it has been placed in a different position. The sink's surface appears to be slightly tilted away from the kitchen counter, suggesting that it may have been taken out of the dishwasher. The kitchen's lighting is now more reflective, implying that there is a slight change in the lighting conditions.
- Reference: In this moment, the bottle of washing up liquid is actively being squeezed, indicated by the blurred motion of the hand and the bottle's deformation. The stream is dynamic; a splash is just beginning as the liquid hits the accumulated pool in the bowl, causing slight ripples to emerge. Droplets may be starting to scatter due to the force of impact, and the stream itself is likely becoming erratic as the pressure changes with the squeezing action.

#### Sample 278 — During

- Similarity: 0.3555
- Prediction: In this frame, the dough is now more firmly kneaded, indicating that it has been pressed into place. The hand's movements are more pronounced, suggesting that the dough has been placed in a predetermined amount of time. The dough's surface appears to be a little looser than before, with a slight crease in the middle of the dough.
- Reference: The cling film has been further pulled out from its package, stretching across the length of the scene in front of the person. The film appears to have more noticeable creases and overlaps, and the extended portion is held aloft by the individual's hands. The packaging is in a nearly vertical position, indicating the force exerted to extract the film.

#### Sample 279 — During

- Similarity: 0.4630
- Prediction: In this frame, the microwave has been moved to a new position, indicating that it is in a more active state. The kitchen's lighting is now more dim, suggesting that there is a slight change in the angle of the microwave's position. The surrounding area, including the kitchen, remains unchanged, implying that the microwave is still in its current position.
- Reference: In this frame, the cabinet door is still ajar but appears to be more closed than in the previous frame, suggesting a continued motion towards closing. The items inside the cabinet remain the same, and there is no significant change in the organization or arrangement of the contents. The blur is still present, reinforcing the idea of movement. The angle of the door compared to the previous frame suggests it has been moved slightly but is not yet fully closed.

#### Sample 280 — During

- Similarity: 0.4770
- Prediction: In this frame, the table appears to be in a state of disarray, suggesting that someone is attempting to move the table. The surface of the table is now more cluttered, indicating that there is a slight movement in the process of removing the table from the frame. The table's surface appears to have been swept away, implying that someone has taken the table and placed it on the counter.
- Reference: In this snapshot, the toaster is again partially visible, caught mid-motion. A hand is grasping a drawer handle, possibly searching for an item or in the process of storing something. The motion blur permeates the scene, creating an effect that implies swift, perhaps frantic, activity. The cabinet's wood grain and the handle's details are smeared across the image due to the motion, suggesting that the focus of the action has quickly shifted from the toaster to the drawer.

#### Sample 281 — During

- Similarity: 0.4470
- Prediction: In this frame, the table's surface appears to be a bit cleaner than before, indicating a more gradual movement of the hand. The person's hand is now positioned in a slightly different position, suggesting that the hand is focusing more on the table. The table is now more cluttered, with a larger portion of the table still visible. The hand's position remains unchanged, suggesting a slight movement in the direction of the action.
- Reference: The hand has shifted position, now wiping the surface with a yellow cleaning cloth. The once visible droplets of detergent are now smeared into streaks, evidence of the wiping motion. The dampness on the surface is more widespread, with the sheen of the liquid reflecting the overhead light, indicating the cleaner has been spread over a larger area. The pressure exerted by the hand is visible in the compressed, crumpled state of the cloth.

#### Sample 282 — During

- Similarity: 0.4772
- Prediction: In this frame, the garlic cloves are now more firmly held, indicating that they have been partially removed from the skin. The skin is now more exposed to the knife's action, implying that the knife has been progressively removing the cloves. The person's hand is more likely to be holding the clove in one hand, with the other hand pointing at the clove.
- Reference: The onion skin now appears more prominently as the hand has grasped a fresh onion, preparing to peel it further. The skin, still glistening, has been moved slightly, showing more of its curved shape that follows the contour of the onion. It looks more wrinkled compared to its initial state, with the edges curling inward, a common characteristic after being detached from the moist layers beneath.

#### Sample 295 — During

- Similarity: 0.4667
- Prediction: In this frame, the utensil has been placed in a different position, with the person's hand holding it, indicating that the water has been sprayed on it. The hand's grip is now more firm, suggesting that the soap has absorbed some of the soap's water, allowing the soap to saturate the surface. The hands are now more engaged in the process of scrubbing, implying that there is a greater focus on the cleaning process.
- Reference: The strainer now cradles a vibrant blue sponge, its rough texture indicating its abrasive capabilities for cleaning. Water no longer flows through it; instead, the focus has shifted to the manual scrubbing action, which is suggested by the positioning of the hands and the sponge. Small bubbles from detergent residues cling to the inner walls of the strainer, and the previously visible food particles appear diminished, a result of the ongoing cleaning effort.

#### Sample 297 — During

- Similarity: 0.4387
- Prediction: In this frame, the chicken is now positioned in a more secluded position, with the chicken's skin exposed, indicating that it has been sliced. The person's hand appears to be attempting to slice the chicken, implying that the knife has been used to cut the meat into smaller pieces. The knife's grip remains firm, suggesting that the meat has been removed from the cutting board.
- Reference: In this moment, the person's hands show motion, with the fingers of one hand holding the board steady and the other using the flat side of a knife blade to scrape the garlic off the board. The garlic is no longer in a solid clove form but is now a smeared, pasty consistency, spread thinly across the board. This indicates that the garlic has been crushed to a degree that it's almost paste-like, ready to be added to the pan for cooking. The action of scraping suggests that the person is transferring the garlic into the pan, as the garlic paste is gathered towards the edge of the board.

#### Sample 298 — During

- Similarity: 0.3143
- Prediction: In this frame, the sink has been placed in a different position, indicating that the water has been drained. The hand is now holding the sink, implying that it has been washed away. The surface of the sink appears to be slightly dampened, suggesting that there may have been a slight movement in the direction of the cleaning process.
- Reference: Here, the gloves are again in focus, with the left hand visibly holding onto a pot's edge and the right hand slightly raised, suggesting a moment of transition or the performance of a task requiring a two-handed approach. The bright yellow rubber material of the gloves continues to be prominent, and they maintain a sheen that could either be from the material's natural finish or a slight dampness, possibly from exposure to water.

#### Sample 303 — During

- Similarity: 0.4851
- Prediction: In this frame, the bottle cap is now in a more upright position, indicating that the hand is holding the bottle. The hand's grip is now more pronounced, suggesting that the bottle is being held by the hand. The bottle's contents are still visible, with the lid still firmly attached to the bottle, implying that the cap is still in its original position.
- Reference: In this snapshot, the same aluminum beverage can is now slightly tilted. The person's hand, identifiable from the same metallic wrist accessory, appears to be pouring liquid from the can into a transparent glass that already has some fluid. The glass exhibits a hint of condensation, indicating the chilliness of its content. The table retains its wooden aesthetic, and the black mat and a fork are visible nearby.

#### Sample 304 — During

- Similarity: 0.4798
- Prediction: In this frame, the utensil is now in the hands of a person who is preparing to rinse it. The person's hand is still motionless, indicating that the water has been sucked out of the urn, possibly to prevent a spill. The hand's grip remains steady, suggesting that there may be a slight movement in the process of rinsing or scrubbing it.
- Reference: In this moment, the tin is captured mid-transition, the focus of a simple yet crucial kitchen task. Water is being poured into the tin, producing a dynamic interplay of fluidity against the rigid, stained background of the tin's interior. The stream of water appears forceful, suggesting a vigorous pour, and its impact on the tin’s surface creates a scattering of water droplets and rivulets that momentarily disturb the residual patterns of baked-on remnants.

#### Sample 305 — During

- Similarity: 0.2860
- Prediction: In this frame, the vegetables are positioned in a slightly different position, indicating that they've been stirred. The pan's surface appears to be slightly tilted, suggesting that there's a slight movement in the direction of the cooking process. There's also a noticeable difference in the color of the vegetables, which may be due to a change in temperature or the presence of a certain amount of water in the pan.
- Reference: The perspective shifts to show more of the countertop's expanse, revealing a clean, clutter-free surface that extends towards a cooking area. An array of beer bottles of various sizes and labels stands in an irregular formation near the edge, alongside a pair of clear glasses, one upright and the other tipped over. A wooden spoon lies on a white spoon rest, next to a skillet on the stove filled with a sautéed mixture, indicating a meal preparation in progress. The person's hands are now in view, one holding a sponge, suggesting active cleaning.

#### Sample 310 — During

- Similarity: 0.3038
- Prediction: In this frame, the knife's surface appears to be a bit darker, indicating a more gradual change in the position of the blade. The hand's motion is more pronounced, suggesting that the blade has been pressed against the surface. The surface of the knife is now slightly creased, suggesting a slight shift in the direction of the movement.
- Reference: In this scene, the tray is shown in a similar state to the first, maintaining its worn appearance with streaks and spots of oil glistening lightly across its surface. The placement of the three dough balls remains unchanged; however, the perspective is slightly different, indicating a shift in the camera angle or the tray's position. The dough balls appear untouched and consistent in their shape and size with the previous frame, reinforcing the notion that they are in a static state of rest.

#### Sample 312 — During

- Similarity: 0.3439
- Prediction: In this frame, the onion has been partially thawed, indicating that it has been steamed. The person's hand is now positioned in the middle of the onion, implying that they are holding the onion in their hands. The onion's skin is now more exposed, suggesting that the onion may have been boiled.
- Reference: The scene continues with the preparation of the green beans. Here, the person's hands are seen holding a bean between the thumb and forefinger, suggesting the act of snapping or trimming the ends. The discarded pieces of trimmed ends are more prominent on the countertop, creating a scattered array of green against the dark surface. The white colander still cradles the trimmed beans, which maintain their bright green color, a sign of their freshness. The lighting casts shadows on the beans and the person's hands, enhancing the texture and depth of the image.

#### Sample 317 — During

- Similarity: 0.4885
- Prediction: In this frame, the bread has been placed in the hands of a person. The person's hand appears to be grasping at the bread, indicating that the bread is still in its packaging. The bread's surface is slightly exposed, suggesting that it may have been partially removed from the bread. The hand's grip is more firm, implying that the hand is exerting more pressure on the bread to ensure that it does not fall apart.
- Reference: In this frame, the mozzarella appears as a blur, with the individual strands indistinguishable due to motion. The spreading action has been captured mid-motion, creating a smear across the visual field that conveys the movement of either the hand or the camera. The cheese is in transition, neither in its original piled state nor settled on the dough, and there is a sense of dynamic interaction between the cheese, the hand, and the dough. This represents a moment where the mozzarella is being actively manipulated.

#### Sample 319 — During

- Similarity: 0.4239
- Prediction: In this frame, the tomato has been sliced in half, with the center being slightly exposed. The hands are now more involved in the process of slicing, indicating that the knife has been used to cut the tomato into pieces. The knife's blade is now positioned in the center of the tomato, implying that it has been partially cut.
- Reference: In this moment, the sandwich begins to take on a more complex structure. The same bottom slice of bread, previously adorned only with lettuce, now also carries a generous addition of sliced ham, its pink hues contrasting with the green lettuce. The maker's hand firmly presses down on the top slice of bread, which has been placed over the ingredients, indicating the action of closing the sandwich. The surrounding area remains cluttered with the aforementioned ingredients and utensils, highlighting the dynamic nature of the meal's assembly.

#### Sample 327 — During

- Similarity: 0.3595
- Prediction: In this frame, the lid of the sink has been moved to a more stable position, indicating that the water has been drained. The person's hand appears to be holding the lid, suggesting that the liquid has been removed from the sink.
- Reference: The image captures a motion blur, indicating rapid movement, with the lunch box becoming an elongated smear across the visual field. Due to the swift motion, the box's details are indiscernible, and the once discernible shapes are now streaks of white and gray, blending with the blurred background. The perspective has shifted dramatically, signaling that the lunch box is in the midst of being tipped over, though its contents and final position remain uncertain in this snapshot of action.

#### Sample 328 — During

- Similarity: 0.2469
- Prediction: In this frame, the bag appears to be in the hands of the person who is holding it. The person's hand is positioned in the middle of the bag, indicating that the bag has been opened. The bag's contents are still visible, including the contents of the plastic bag, which has been placed in the bag. The camera's focus is now on the bag and its contents, which are likely to be contained within the bag itself.
- Reference: Here, the slice of bread is partially inside the toaster, with only a small portion protruding above the slot. It sits within a gray toaster that seems to be of a modern design, with the red light on the control panel indicating that the toaster is on and actively toasting. The bread has begun its transformation from a soft, pliable state to one that will become crispy and golden-brown, the anticipation of that textural change implicit in the image.

#### Sample 329 — During

- Similarity: 0.4163
- Prediction: In this frame, the coffee pot is now positioned in a slightly different position, indicating that it has been agitated. The person's hand is more likely to have grasped the lid of the pot, implying that the cup has been placed in the same position as before. The surrounding environment remains unchanged, including the kitchen, which is cluttered with clutter and clutter.
- Reference: The bag now seems more exposed as compared to the previous frame. The hand appears to be actively engaging with the bag, either adjusting or opening it. The bread inside is more clearly visible, showing its texture and confirming that it is indeed a bread bag. The orange label on the bag is also clearer, and the overall placement of the bag has slightly shifted, implying some interaction has taken place.

#### Sample 332 — During

- Similarity: 0.3231
- Prediction: In this frame, the oven door is positioned in a slightly different position. The person's hand is more firmly grasping the door, indicating that the oven has been opened. The interior of the oven appears to be more open, suggesting a closer view of the kitchen. The kitchen's lighting is more dim, suggesting that there may be a slight movement in the oven.
- Reference: In this instance, the freezer drawer is almost entirely closed, with only a slender sliver of space visible, signifying the near completion of the closing action. The swift movement is evident from the blur of the drawer's edges, and there is a discernible decrease in the gap from the previous state. The contents are still not in clear view, but the drawer appears to be secure, indicating that items inside are less likely to be disturbed.

#### Sample 333 — During

- Similarity: 0.4496
- Prediction: In this frame, the cheese has been placed in the hands of a person, presumably a chef, who is preparing to prepare a meal. The person's hand appears to be grasping at the cheese, implying that the cheese is being poured into a bowl. The hand's grip is slightly more firm, indicating that there may be a slight movement in the process of preparing the cheese. The texture of the cheese remains consistent with the cheese's texture and texture, suggesting that it may be ready for use.
- Reference: In this scene, the bread is no longer in view, implying that the person might have moved it out of the frame or placed it down on the countertop. The focus is blurred, capturing the dynamic movement within the kitchen space, which includes a glimpse of kitchen appliances and a blurred image of what could be a stovetop. The absence of the bread in this frame interrupts the continuity of its handling, suggesting a swift, perhaps hasty, motion.

#### Sample 334 — During

- Similarity: 0.4491
- Prediction: In this frame, the paperclip has been placed in the hands of a person. The person's hand appears to be grasping at the edge of the parchment paper, indicating that it has been inserted into the paper. The paperclip's surface is slightly curved, suggesting that it may have been partially inserted. The hand's grip remains firm, implying that the action is aimed at removing the parchment from the sheet.
- Reference: The same hand now holds the knife at a different angle, pointing more towards the bottom corner of the frame, which suggests that the spreading motion has continued. The creamy substance appears more evenly distributed across the bread's surface, though there are still areas of varying thickness. The hand's grip on the knife has shifted slightly, now more in control, and the knife itself has less of the white substance on its blade, indicating that most of it has been transferred to the bread. The bread slice remains angled, and the crust is more prominently in view.

#### Sample 335 — During

- Similarity: 0.2829
- Prediction: In this frame, the table is now positioned in a more natural position, with a slightly different shape than the previous frame. The person's hand is now more firmly grasping the table, indicating that the table has been placed on the table. The table's surface appears to have been taken apart, suggesting that it may have been a discarded piece of furniture.
- Reference: The degreaser now shows a different stage of application. The mist has settled slightly, with fewer droplets suspended in mid-air, and more visible accumulation on the surface, forming irregular patterns where the liquid has begun to settle. The hand holding the bottle has moved marginally to the right, indicating the continuation of the spraying action. The countertop reflects less light where the degreaser has settled, indicating the surface is now moistened by the liquid. The spread of the degreaser is more widespread, covering a larger area than in the previous frame.

#### Sample 338 — During

- Similarity: 0.1154
- Prediction: In this frame, the egg appears to be in a more active state, indicating that it's being stirred. The spoon's motion seems to indicate that the egg has been placed in the center of the pan, implying that it has been inserted into the pan. The egg's surface appears to have been agitated, suggesting that the cooking process has begun.
- Reference: Upon closer inspection, the extractor fan presents a consistent appearance of wear, with no discernible changes in the distribution or intensity of the grease marks compared to the previous state. The uniformity of the discoloration suggests that the fan has been subjected to a steady amount of heat and airborne particles over a considerable duration. There is no evidence of any cleaning attempts, as the patterns of grease remain uninterrupted and widespread across the entire surface of the fan.

#### Sample 347 — During

- Similarity: 0.4617
- Prediction: In this frame, the tea towel has been placed in a new position. It is now positioned in the hands of a person who is holding it. The person's hand appears to be grasping at the towel, implying that the hand is holding the towel. The towel's surface is now more exposed, indicating that the towel is being handled.
- Reference: The towel is now in an intermediate state of being folded. One can see a hand grasping a portion of the towel, which suggests that it's in the process of being manipulated or adjusted. The colorful stripes are still visible, but not in their entirety as before, given that a part of the towel is overlapped. The fabric's texture seems consistent with the previous frame, smooth and free of significant wrinkles or creases.

#### Sample 348 — During

- Similarity: 0.4096
- Prediction: In this frame, a person's hand grabs the door of the refrigerator, revealing a gap in the middle of the door. The door is now partially open, suggesting a closer view of the contents of the freezer. The interior of the fridge appears to be more spacious, indicating that there are more items on the counter or in the fridge.
- Reference: This frame captures the kitchen cabinet in a clearer state with an open door, revealing a more organized array of spice jars and boxes, all neatly aligned on a shelf. The hand is blurred in motion, indicating the action of reaching for or placing a spice jar. The spice jars vary in size and color, suggesting a variety of herbs or seasonings. No specific jar is the sole focus, but collectively they create an impression of an assortment maintained for culinary purposes.

#### Sample 349 — During

- Similarity: 0.4366
- Prediction: In this frame, the microwave has been placed in a different position. The person's hand is now positioned at the edge of the microwave, indicating that the microwave is still in the position of its predecessor. The microwave remains in the same position as in the previous frame, with the microwave still in its original position.
- Reference: In this frame, the person's hand is in direct contact with the left switch. The finger is pressing down on the upper part of the switch, and due to the angle and the motion blur, it's unclear if the switch has been flipped yet. The absence of a red band on the switch could indicate that it has already been turned on, or it may still be in the process of being flipped. The pressure applied by the finger is evident from the slight deformation of the skin, showing the action in progress. The kettle remains plugged in, and the general disarray of the kitchen remains unchanged.

#### Sample 351 — During

- Similarity: 0.4646
- Prediction: In this frame, the plastic bag is now in the hands of a person who is holding it. The person's hand appears to be grasping the bag, indicating that the bag has been opened. The bag's contents are still visible, including the contents of the bag itself, as well as the packaging's packaging.
- Reference: Here, the olive oil bottle's cap is being handled by a person, whose hands are the focal point of the image. The cap is grasped firmly between fingers, showing the action of capping in progress. The individual appears to be in the midst of securing the cap back onto the bottle, indicated by the positioning of the hands and the slight squeeze of the fingers, which are attempting to align the cap with the threads of the bottle. This frame captures the motion and intent to seal the bottle after use, ensuring the olive oil's freshness.

#### Sample 353 — During

- Similarity: 0.3272
- Prediction: In this frame, the coffee pot's lid is positioned in a slightly different position from the previous frame, suggesting that it has been placed in the same position as the previous one. The person's hand appears to be holding the lid, indicating that the lid has been removed from the machine. The surrounding environment is similarly disrupted, implying that the user is attempting to remove the lid.
- Reference: In this instance, the button is captured in the midst of being pressed. One can discern the initial stages of depression as the button yields to the finger's force. The top surface of the button, which was previously flush with the console, now shows a slight angle indicative of the pressing action, and the shadow around the finger's contact point has deepened, reflecting the change in distance between the finger and the button surface. The light reflection on the button's surface has altered slightly, conforming to the new shape as the button is pushed inward.

#### Sample 354 — During

- Similarity: 0.4866
- Prediction: In this frame, the sink has been moved to a new position, with the lid still positioned in the middle of the kitchen counter. The hand is now positioned at the top of the sink, indicating that the sink is still in its current position. The sink's surface is now slightly tilted, suggesting that the water has been drained. The surrounding area is now more cluttered, implying that there is less of a gap between the sink and the sink.
- Reference: The ladle is now in a different position, indicating a swift movement. It's closer to the center of the frame, tilted slightly more towards the camera, giving a clearer view of the bowl of the ladle which is shiny and seems well-used. The grip on the handle appears to have shifted, suggesting a dynamic action, possibly a rotation of the wrist. The background blurs with the motion, emphasizing the speed of the movement, but kitchen elements like the frying pan on the stove with sautéing contents and assorted bottles remain recognizable.

#### Sample 356 — During

- Similarity: 0.4589
- Prediction: In this frame, the kitchen has been moved to a new position, with the kitchen still visible, indicating that there is a movement in the kitchen. The kitchen appears to be preparing for a meal or other activity, possibly a quick meal or a light meal. The lighting is dim, suggesting that there may be a sudden change in the lighting conditions.
- Reference: In this scene, the pan contains a similar mixture, but the quantity of the liquid appears slightly reduced, indicating that some of the water content has evaporated due to heat. The green elements have a more wilted and cooked appearance, taking on a darker, more olive-like shade. The liquid has a few more visible bubbles, showing signs of gentle simmering, and the mixture is beginning to cling lightly to the wooden spoon, suggesting a slight thickening of the sauce or reduction in volume. The stirring motion seems to be gentle and consistent, maintaining an even cooking process.

#### Sample 359 — During

- Similarity: 0.4208
- Prediction: In this frame, the rag is now in a more concentrated state, indicating that the water has been sucked out of the cloth. The cloth's surface appears to have been soaked in water, suggesting that it has been washed away. The person's hand appears to be exerting more pressure on the cloth, implying that the cloth is being soaked.
- Reference: The bin is now partially obstructed by a person's forearm, suggesting action in the process of discarding waste. The contents of the bin remain the same, densely packed and unaltered in the brief time lapse between the frames. There is no visible movement of the bin itself, indicating that the person's focus might be on another task, possibly related to cleaning or preparing to dispose of waste. The surrounding area, including the dish rack and countertop, appears unchanged, maintaining the context of ongoing kitchen use.

#### Sample 360 — During

- Similarity: 0.4676
- Prediction: In this frame, the person's hand moves closer to the kitchen counter, revealing a larger portion of the food container. The contents of the container are more visible, including the lid, which appears to be partially open, and the lid's handle, which is positioned in the center of the tray. The hand's motion is more pronounced, indicating that the person is attempting to open the container.
- Reference: The fridge door seems slightly more closed compared to the previous frame but is still not completely shut. The LED indicators remain visible and illuminated. The door handle has moved a bit towards its resting position, yet the black interior of the fridge is still partly visible. The reflections on the fridge surface appear slightly different, suggesting a subtle shift in the surroundings or lighting.

#### Sample 362 — During

- Similarity: 0.4536
- Prediction: In this frame, the rag is now in a more concentrated state, indicating that the water has been drained. The rag's surface appears to be slightly dampened, suggesting that it has been partially soaked or washed. The cloth's texture seems to be more pronounced, suggesting a deeper penetration of the water.
- Reference: Here, the water tap appears in a similar state as before, with water flowing from its spout. However, there's a subtle change in the positioning of the hands and the tap, indicating an interaction has occurred. The hands are now closer to the tap, implying an action in progress. The stream of water seems uninterrupted, with the liquid's surface tension visible as it flows and splashes into the basin, reflecting the kitchen's ambient light.

#### Sample 363 — During

- Similarity: 0.3368
- Prediction: In this frame, the kitchen sink appears to be in a different state of motion. It's a bit more cluttered, but it's still a little closer to the edge of the kitchen counter, suggesting a more gradual movement. The kitchen's lighting is more dim, suggesting that there's been a slight shift in the angle of the sink, indicating that there may be a gap between the kitchen and the sink.
- Reference: The locker in this frame is more obscured than in the previous one, though it remains open. It's challenging to make out specific items due to the angle and blurriness of the image, but it seems that the contents remain unchanged from the previous glimpse. The focus is slightly shifted towards the countertop, yet the open door still captures a significant portion of the frame.

#### Sample 364 — During

- Similarity: 0.2179
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating that it has been placed in a different position. The kitchen sink is now positioned in the same position as the kitchen counter, suggesting that the kitchen's position has changed. The lighting is more reflective, suggesting a shift in the direction of the kitchen or kitchen.
- Reference: In this frame, the sweet potato shows visible signs of being prepared for consumption. Slices or sections have been neatly cut, revealing its vibrant orange interior. The flesh looks soft, moist, and inviting, contrasting beautifully with the outer skin. The cuts are clean, indicating a sharp knife was used, and the edges of the slices glisten slightly, catching the light in a way that accentuates their fresh, juicy appearance.

#### Sample 365 — During

- Similarity: 0.4955
- Prediction: In this frame, the stove has been moved to a new position, indicating that there is more activity on the burner. The person's hand appears to be holding the stovetop, presumably aimed at removing any remaining residue. The surface of the burner appears to have been cleaned, suggesting that there may have been a few drops of soap on the surface.
- Reference: In this frame, the hob surface seems to have been partially cleaned, with less of the creamy substance visible than in the previous frame. The sheen from the moisture is still present, though it appears slightly reduced. The blue cloth is now more pronounced and is making direct contact with the surface, implying an active wiping action. Some of the surrounding kitchen items remain in view, including a wooden utensil which might have been used in cooking.

#### Sample 367 — During

- Similarity: 0.4735
- Prediction: In this frame, the water is now in a more concentrated state, indicating that it has been added to the pot. The water's surface appears to be slightly dampened, suggesting that the water has been poured into the pot, rather than being poured directly into the water. The object of the hand is now more likely to be a spoon or a utensil, implying that the liquid has been stirred.
- Reference: In this frame, the cap's visibility is slightly better compared to the previous one. It can be discerned that it's closer to some household objects, including a rice cooker and some containers. The cap's orientation suggests that it might have been placed or dropped in a hurry. The environment still appears cluttered, but the cap now has a more central presence in the frame, indicating its significance.

#### Sample 368 — During

- Similarity: 0.3088
- Prediction: In this frame, the person's hand is positioned in front of the plastic bag. The bag's contents are now more visible, with the contents of the bag being more visible. The hands are more engaged in the process of removing the bag, which is likely to be the first time the person has touched the bag.
- Reference: In this scene, there is no direct view of the tomatoes as the can is absent from the visible countertop. However, the preparation for incorporating the tomatoes into a meal is ongoing. The countertop shows evidence of cooking activity with various items scattered around, such as a toaster, a crumpled plastic bag, and what appears to be the card of recipes or instructions. Without the presence of the tomato can, there's an implication that the tomatoes have been or are in the process of being transferred to another stage of the cooking process.

#### Sample 370 — During

- Similarity: 0.4613
- Prediction: In this frame, the tea towel has been placed in a new position. It is now more firmly held, indicating that it has been taken apart. The hands are now more engaged in the action, implying that the towel is being pressed against the table surface. The hand's movements are more deliberate, suggesting that the hand is attempting to grasp the towel. The fabric of the towel appears to have been pushed against the fabric, suggesting a movement in the direction of the action.
- Reference: In this frame, the paper is in motion, evidenced by the blur and the shift in orientation from the previous state. The roll now appears slightly tilted, and the hand is grasping it more firmly, suggesting that a force is being applied. The paper's end is no longer neatly tucked in; it's starting to unravel, indicating the tearing process has begun. The image captures the very beginning of the disruption to the roll's integrity.

#### Sample 372 — During

- Similarity: 0.3358
- Prediction: In this frame, the bin's lid is positioned in a slightly different position, indicating that it has been partially opened. The lid's position remains unchanged, suggesting that the contents of the container have been removed from the inside of the bin. The object's surroundings remain blurred, implying that there is still a gap between the lid and the outside of the bag.
- Reference: In this moment, the basket is not visible; the focus is on a person's lower body in motion, with the legs partially seen at the edge of the frame. The feet are clad in sandals, firmly planted on an orange-tiled floor that contributes to the warm color palette of the scene. The person's shadow and the floor tiles suggest a quick, perhaps downward movement, as if stepping or crouching, in the midst of an action that is not fully captured within this particular frame.

#### Sample 373 — During

- Similarity: 0.4128
- Prediction: In this frame, the cheese has been placed on a plate, presumably to serve as a condiment. The person's hand is now positioned in the middle of the plate, suggesting that the cheese is being placed on top of it. The menu appears to have been taken out of the tray, indicating that there is still a large amount of cheese left on the plate.
- Reference: The sandwich is now being actively cut by the knife held by the hand. The knife has made its way through the top layer of the bread, creating a visible incision. The contents of the sandwich, still mostly concealed, begin to peek through the slit. The pressure exerted by the hand and knife has slightly deformed the sandwich, compressing it a bit under the force.

#### Sample 376 — During

- Similarity: 0.4278
- Prediction: In this frame, the rinsing spoon is now in the hands of a person who is attempting to rinse it. The spoon's grip is slightly more firm, suggesting that the water has been sucked out of the spoon, allowing the water to drain away from the spoon. The hand's fingers appear to be holding the spoon in their hands, indicating that the spoon is still in the hand. The water level appears to be higher than usual, suggesting a steady stream of water.
- Reference: In this frame, the cucumber is actively being rinsed under running water. Water droplets are seen cascading over its surface, making the cucumber appear glossy and wet. The person's hands are firmly holding the cucumber, ensuring it's thoroughly washed. The pressure from the water stream causes some reflections on the cucumber's skin, accentuating its curve and form.

#### Sample 379 — During

- Similarity: 0.4299
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating that it has been placed in a different position. The kitchen sink's position remains unchanged, suggesting that the kitchen is now positioned in the same position as the previous frame. The hand-held camera's focus is now on the kitchen counter, which is positioned at the center of the kitchen.
- Reference: In this frame, the tray remains on the scales, but it appears to be slightly tilted, indicating that it is in the process of being moved or adjusted. The light seems to reflect differently on the tray's surface, hinting at the slight change in its position. Around the tray, other objects remain relatively unchanged.

#### Sample 381 — During

- Similarity: 0.3294
- Prediction: In this frame, the meat has been placed in a hot skillet, indicating that it has been heated to a medium-high temperature. The pan's surface is now slightly tilted, suggesting that the heat has been absorbed into the meat. The meat is now positioned in the center of the skillet, with a thin layer of meat on the bottom of the pan.
- Reference: In this frame, the spice application is more evident. The hand holding the spice jar is poised directly over the dish, displaying a deliberate and focused seasoning action. The spice particles are more visible on the dish, indicating a generous application. The density and spread of the spice specks suggest that the user is aiming for an even distribution across the dish, ensuring each portion receives an adequate amount of seasoning.

#### Sample 384 — During

- Similarity: 0.3545
- Prediction: In this frame, the refrigerator door is positioned in a slightly different position, suggesting a more gradual movement of the door. The interior of the refrigerator is now more cluttered, with fewer items and less space. The door's hinges are more prominent, indicating that the door has been opened.
- Reference: The milk jug is now captured mid-air, in the process of being transported. Its orientation is slightly tilted, suggesting movement, and the handle is firmly grasped, indicating it is being carried with purpose. The jug's cap appears to be secured, and there is no evidence of spillage. The background is a blur, with the refrigerator interior and its contents such as a carton of eggs and other containers providing a static contrast to the milk jug's motion.

#### Sample 391 — During

- Similarity: 0.3737
- Prediction: In this frame, the rinsing pan is now in a more natural state, indicating that the water has been drained. The person's hand appears to be holding the pan, implying that they are attempting to rinse it. The water's consistency is more uniform, suggesting that there may be a slight movement in the direction of the sink.
- Reference: In this frame, the chopping board's surface has significantly more water on it, with larger puddles forming in certain areas. The water droplets have spread further, covering more of the board's area. The color distinction between the wet and dry areas remains noticeable, with the wet sections showcasing a deeper shade of blue, possibly indicating that more water has been added or that the existing water has spread.

#### Sample 393 — During

- Similarity: 0.4461
- Prediction: In this frame, the knife has moved closer to the cutting board. The knife's edge is now positioned in the center of the knife, indicating that it has been slicked into the desired shape. The blade's surface appears to be slightly curved, suggesting that the knife is moving forward. The hand's position remains unchanged, with the knife still positioned at the edge of the board.
- Reference: The chopping of the chili has progressed; more slices of the chili pepper now lay in a scattered arrangement on the cutting board. The hands have moved slightly, with the fingers curled in preparation for another cut, showcasing safe cutting techniques. The pile of sliced chili pieces appears to be more substantial, and the seeds are more prominently on display amongst the slices, further hinting at the chili's intensity. The knife is at rest, suggesting a momentary pause in the action.

#### Sample 397 — During

- Similarity: 0.4744
- Prediction: In this frame, the kitchen sink has been moved to a new position, indicating that it has been placed in a different position. The kitchen's lighting is now more dim, suggesting that the kitchen has been preparing for a meal or other activity. The hand-held camera's focus is now on the kitchen counter, suggesting a shift in the direction of the kitchen.
- Reference: The salt container seems to have been repositioned slightly. While it remains amidst other kitchen items, the shift in its placement suggests that it might have been moved or nudged. The cap appears to remain closed, indicating that the salt inside hasn't been dispensed recently in this frame. The scene appears busier than in the previous frame, perhaps indicating progression in the cooking or preparation process.

#### Sample 401 — During

- Similarity: 0.3681
- Prediction: In this frame, the person's hand moves closer to the edge of the kitchen counter, revealing a gaping gap in the middle of the counter. The hand's position is slightly different from the previous frame, suggesting a more gradual movement of the hand, indicating that the hand is more engaged in the action. The object's shape is more pronounced, suggesting that it is more likely to be a piece of wood or a plastic container.
- Reference: In this scene, the hardwood floor continues to display its polished surface and warm tones. The lighting seems consistent with the previous frame, highlighting the natural grain and color variations in the wood planks. The sweeper has interacted with the floor, as evidenced by a few streaks left by the cleaning implement, showing that some of the loose particles have been gathered or displaced. However, there remains a scattering of debris and dust not yet collected by the sweeper.

#### Sample 403 — During

- Similarity: 0.4707
- Prediction: In this frame, the bread has been placed on a cutting board. The person's hand is now positioned on top of the bread, indicating that it has been sliced. The bread's surface appears to be slightly slanted, suggesting that the bread is being sliced in a circular motion. The knife's edge is slightly curved, suggesting a slight movement in the process of cutting the bread.
- Reference: The onion slices have been further processed in this frame. They are now laid out on what appears to be a piece of bread or perhaps a base for a pizza or flatbread. The slices are arranged to cover most of the surface area of the bread, slightly overlapping in places. The arrangement is deliberate, ensuring even distribution and coverage. The onions still retain their fresh appearance, with the edges looking slightly translucent, a characteristic feature when onions are thinly sliced.

#### Sample 406 — During

- Similarity: 0.4370
- Prediction: In this frame, the bin's lid is positioned in a slightly different position, indicating that it has been partially opened. The person's hand is still motionless, suggesting that the lid is partially open. The lid's surface is slightly blurred, suggesting a gradual movement of the bin, which is likely a sign that the bin has been closed.
- Reference: In this frame, the strainer is still held, but now its bottom faces more towards the ground. The orange-yellow liquid that was once prominent in the strainer has lessened considerably, and the strainer appears more vacant. While traces of the liquid remain, it's evident that a substantial amount has already been poured out or drained. The strainer's white surface now contrasts with the remnants of the liquid, highlighting the empty spaces between the fine mesh.

#### Sample 408 — During

- Similarity: 0.4521
- Prediction: In this frame, the butter has been poured into a bowl, indicating that it has been stirred. The hand is now holding the butter in a circular motion, implying that the butter is being poured onto the bowl. The knife's handle is now positioned in the middle of the bowl, suggesting that the hand is attempting to grasp the butter.
- Reference: In this frame, the person's hand has made progress in opening the bottle. The cap seems to have been slightly loosened, allowing for the content within the bottle to be accessed soon. The fingers grasp around the neck of the bottle, exerting a gentle pressure indicating the act of unscrewing the lid. The base of the bottle remains firmly over the tortilla, poised to dispense its contents.

#### Sample 410 — During

- Similarity: 0.3179
- Prediction: In this frame, the olive oil is now in the hands of a man who is attempting to remove the olives from the kitchen counter. The man's hand is positioned on the edge of the olive, indicating that the olive has been removed. The palm of the man is now positioned at the center of the palm, implying that he is removing the olive from the palm of his hand. The person's fingers are still firmly pressed against the olive's surface, suggesting that they are engaged in some sort of action.
- Reference: The scene shifts slightly to show a hand actively engaged in the act of sprinkling sweetcorn onto the pizza. The kernels are in a state of descent, some possibly caught in the very moment of leaving the can, while others are likely just making contact with the saucy surface below. The sweetcorn's distribution is uneven, with a cluster gathering more densely in one area, indicating the initial point of contact from the can. The act of sprinkling is captured dynamically, with the potential for motion blur on some kernels indicating their rapid journey onto the pizza.

#### Sample 415 — During

- Similarity: 0.4986
- Prediction: In this frame, the tray is now positioned in a slightly different position. The person's hand is now more visible, indicating that they are holding the tray. The tray's contents are still visible, including the contents of the container, as well as the lid, which has been removed from the tray and placed on a counter. The camera's focus is now on the tray, which is now partially open.
- Reference: The lunch box is now opened slightly, revealing more of its interior. Through the opened part, it's noticeable that there is a light-colored content, which might be a type of food, possibly a sandwich or wrap given its layered appearance. The label on the transparent lid is more apparent in this frame, and the red hue of the box is still visible.

#### Sample 420 — During

- Similarity: 0.4589
- Prediction: In this frame, the bag appears to be in the hands of the person who is holding it. The person's hand is positioned in the middle of the bag, indicating that they are preparing to open the bag. The bag's contents are still visible, but there is a slight shift in the direction of the movement of the hand, suggesting that the bag has been placed in a more upright position.
- Reference: In this scene, the freezer door has moved slightly more open compared to the previous frame. The person's hand is repositioned, indicating movement. The angle of the frozen item in the hand has changed, providing a clearer view of what appears to be a zip-locked bag of food. The inner compartments of the freezer door are more visible now, with the slots designed to hold items such as ice trays or small frozen goods. The shadow cast by the door on the freezer's contents has shifted, indicating a change in the lighting angle or intensity.

#### Sample 424 — During

- Similarity: 0.4832
- Prediction: In this frame, the person's hand is more pronounced, indicating that they are attempting to open the package. The person' s hands are more rounded, suggesting that their fingers are more engaged in the process of opening the bag. The contents of the bag appear to be a mixture of fresh and dried fruit, with a hint of a tangy texture. The bag's contents are less noticeable, but there is a slight movement in the direction of the opening.
- Reference: The plastic bag has undergone further manipulation. The blue scissors have progressed further along the top, creating a longer incision into the bag. It's evident that the initial cut made in the previous frame has been extended, and the bag is being opened more widely. The individual's grip on the bag and scissors has shifted slightly to facilitate the continuation of the cut.

#### Sample 427 — During

- Similarity: 0.2704
- Prediction: In this frame, the bowl is now positioned in a slightly different position from the previous frame, indicating that it has been taken apart. The bowl's surface appears to be slightly tilted, suggesting that it may have been taken out by a hand. The hand's motion indicates that the bowl has been placed in the correct position, implying that the hand is holding the bowl.
- Reference: Now, the refrigerator door is fully open, revealing more of its contents. On the door's lower shelf, there’s a glimpse of what seems to be bottled condiments, partially obscured by the open door. The second shelf of the door holds a mix of yellow and red fruits, possibly bananas and apples, held in a white wire basket, suggesting an attempt to keep fruits within easy reach. The interior light remains off, and the lower shelves inside the refrigerator are still not completely visible, but there's a suggestion of crisper drawers possibly containing more produce.

#### Sample 430 — During

- Similarity: 0.3973
- Prediction: In this frame, the person's hand is positioned on top of the container, with the lid firmly pressed against the edge of the tray, indicating that the container has been placed in the correct position. The hand's grip is slightly more firm, suggesting that the person is holding the container in the hands of another person. The container's surface appears to be a bit looser than before, implying that the hand may have grasped the container.
- Reference: The plastic bag now shows signs of manipulation, with the top edges being pulled apart, indicating that the opening process is underway. The opening is wider compared to the previous state, revealing more of the bag's interior though it is still not fully expanded. The bag's texture is more pronounced due to the stretching of the material, and there appears to be more light reflecting off its surface, which could be due to the opening motion creating a flatter surface on top.

#### Sample 433 — During

- Similarity: 0.2693
- Prediction: In this frame, the person's hand moves closer to the door, revealing a gap in the middle of the frame, suggesting that the door has been closed. The door's hinges are still visible, indicating that there is a slight movement in the process of closing the door.
- Reference: Here, the cloth seems to be in a state of being actively squeezed. The fingers are pressing into the material, which is gathered and twisted to wring out the liquid. This action has created darkened wet patches on the cloth's surface, implying that the moisture is being expelled. The cloth's twisted sections are tightly compressed, and the surrounding area suggests a more vigorous motion compared to the previous state, reflecting a more dynamic phase of the wringing process.

#### Sample 436 — During

- Similarity: 0.4323
- Prediction: In this frame, the knife's handle is positioned in a slightly different position, indicating that the knife has been moved. The blade's position remains unchanged, suggesting that it has been agitated, possibly by a hand-held device, such as a spoon or a utensil. The person's hand appears to be pointing at the knife, which appears to have been pressed against the edge of the knife.
- Reference: In this snapshot, the peeler has been set down on the cutting board, its handle extending towards the bottom edge of the frame. It lies adjacent to a vividly colored eggplant peel, showcasing the contrast between the peeler's utilitarian design and the organic curvature of the peel. The blade end of the peeler is slightly obscured by the discarded peel, indicating that it has been recently used. The surrounding area is sparsely littered with small flecks of peel and moisture, possibly from the eggplant, suggesting a scene of ongoing food preparation.

#### Sample 437 — During

- Similarity: 0.2769
- Prediction: In this frame, the sink has been placed in a different position, indicating that the water has been drained. The person's hand appears to be holding the sink, implying that they are attempting to clean it. The water level is slightly lower than in the previous frame, suggesting that there may be a slight movement in the direction of the sink.
- Reference: The pepper pieces remain on the wooden chopping board, but they have been slightly rearranged or shifted, possibly due to some movement or external interference. They seem to be closer to the edge of the board, hinting at a potential transition in their placement. Their bright yellow color still stands out prominently, showcasing their freshness.

#### Sample 443 — During

- Similarity: 0.4431
- Prediction: In this frame, the spoon is positioned in the middle of the bowl. The spoon's surface is slightly tilted, indicating that the spoon has been agitating the bowl's contents. The object's shape is more uniformly distributed across the bowl, forming a smooth, rounded shape.
- Reference: In this frame, the liquid's surface exhibits more motion, evidenced by the formation of ripples and waves around the beaters, a consequence of the mixer's increasing speed or more vigorous movement. The color remains consistently yellow, but the texture appears slightly aerated, with small air bubbles beginning to emerge. This suggests that the liquid is being whipped, increasing in volume, and becoming lighter as air is incorporated. The beaters are coated with a thin layer of the mixture, indicating its adherence and possibly a slight thickening in consistency.

#### Sample 444 — During

- Similarity: 0.4266
- Prediction: In this frame, the knife's handle is positioned in a slightly different position, indicating that it has been pressed against the edge of the blade. The hand's grip remains steady, suggesting that the blade is still firmly attached to the blade, and that the knife is now firmly placed on the blade's edge. The knife remains in the same position as the previous frame, with the blade still holding the blade in place.
- Reference: In this frame, the whetstone remains in a vertical position, consistent with the previous image. The light-colored side is still facing upwards, indicating the finer grit is being used for sharpening. While the stone remains dry, there is a noticeable increase in the reflection of light, especially around the area where the blade interacts with the stone. This might suggest that the stone has accumulated fine metal particles or that there is increased friction between the blade and the stone.

#### Sample 448 — During

- Similarity: 0.4979
- Prediction: In this frame, the person's hand is positioned at the top of the machine's door, indicating that the machine has been opened. The hand's position remains unchanged, suggesting that the hand is engaged in the process of opening the door. The surrounding area, including the door itself, remains unchanged.
- Reference: In this moment, the machine remains in focus, with a human hand reaching towards the control panel. The power button, or a possibly a brew button, is now visibly engaged, as indicated by the green light that wasn't illuminated before. This suggests the initiation of the coffee brewing process. The machine still lacks its carafe on the heating plate, and the absence of any audible or visual signs of brewing (like steam or the sound of water heating) implies that the brewing cycle has just been activated.

#### Sample 453 — During

- Similarity: 0.4208
- Prediction: In this frame, the person's hand is now more focused on the sink, indicating that the water has been drained. The sink's surface appears to be a bit damper, possibly due to the presence of a larger amount of water in it. The hand's focus is now on the faucet, which is now positioned in the center of the frame. The water's droplets appear to be more concentrated than before, suggesting that there may have been a slight movement in the process of cleaning the sink.
- Reference: A damp cloth makes its presence known on the counter. One can now see a clear division where the cloth has passed: one side pristine and clean, the other still holding onto the dust and crumbs. The streaks from the previous frame seem to have dissolved under the wetness of the cloth, but not entirely gone. The difference between the cleaned and yet-to-be-cleaned areas is quite stark, showcasing the effect of the wiping process.

#### Sample 456 — During

- Similarity: 0.4721
- Prediction: In this frame, the rinsing pot is now held in a different position than in the previous frame. The person's hand is more likely to be holding the pot under the faucet, indicating that the water has been sprayed into the pot. The water's surface appears to be drier, suggesting that there may be a more concentrated stream of water.
- Reference: In this frame, the decorative coffee machine is now partly obscured by a hand that's placed near or on its base, suggesting someone is interacting with or moving it. The machine retains its vibrant colors and ornate patterns, and the label or marking on the front remains indistinguishable. It's worth noting that the top portion of the coffee machine, which previously appeared open, is no longer in full view, possibly due to a change in the angle or the hand's positioning.

#### Sample 459 — During

- Similarity: 0.2143
- Prediction: In this frame, the kitchen sink has been moved to a new position, with a more streamlined appearance and a sharper edge. The kitchen sink is now in a different position from the previous frame, indicating that it has been removed from the kitchen counter, possibly to prevent spills. The sink's surface is now more exposed, suggesting that it may have been wiped down. The hand's motion is more pronounced, implying that the hand is holding the sink.
- Reference: In this scene, the can is now held aloft by a human hand, gripped firmly around its body. The lid is in a further state of detachment, peeled back to expose more of the contents within, which are indeed small, spherical, and uniformly sized, corroborating the initial presumption of peas or corn. The opening of the can now allows for a clear view into the interior where the contents are packed in liquid, likely brine or syrup, which is typical of canned produce.

#### Sample 460 — During

- Similarity: 0.3641
- Prediction: In this frame, the pan's surface appears to be in a more natural state, with a slight change in the position of the burner. The person's hand seems to be focusing more on the surface, indicating that the burner has been agitated, possibly by a hand-held device. The surface of the pan is slightly different from the previous frame, suggesting that there may have been a shift in the direction of the cooking process.
- Reference: In this frame, the focus is marginally clearer, showing the tap in a semi-active state. The blur has somewhat subsided, hinting that the movement has slowed down, with the hand retreating from the tap. The stream of water is still indiscernible, possibly due to the water flow being greatly reduced as the tap approaches the off position. The immediate environment of the tap shows signs of recent activity, with water droplets and splashes visible around the sink area, reflecting the previous interactions with the water flow.

#### Sample 463 — During

- Similarity: 0.4062
- Prediction: In this frame, the pot appears to be in a more active state, indicating that the water has been boiled. The pan's surface appears to have been partially cooled, suggesting that the cooking liquid has been removed from the pot. The pot's lid remains firmly attached to the pot, which is likely a sign of the cooking process.
- Reference: In the second frame, the surroundings of the switch become slightly more discernible, but the state of the switch is still not entirely clear. The image features a hand near what appears to be the kitchen countertop or appliance interface, suggesting some interaction might be occurring. There's an indication that the hand might be grasping or reaching for something, possibly the switch. However, the exact state, whether it's turned on or off, remains ambiguous due to the blurriness.

#### Sample 467 — During

- Similarity: 0.4449
- Prediction: In this frame, the cheese has been placed on a cutting board. The knife's edge is positioned at the center of the cheese, indicating that the knife has been inserted into the cheese. The cheese's surface is slightly creased, suggesting that the cheese is being pressed against the edge of the cutting board, implying that it has been cut. The hand's position remains unchanged, with the knife still positioned in the middle of the slice.
- Reference: The sandwich remains on the same plate, but there's a noticeable shift in its position. One of the triangular halves has been slightly shifted away from its counterpart, suggesting an attempt to pick it up or adjust its position. A few crumbs can be observed near the sandwich, indicative of the movement. The grainy texture of the bread is even more pronounced in this frame, further emphasizing its whole grain nature.

#### Sample 468 — During

- Similarity: 0.4239
- Prediction: In this frame, the rinsing spoon is now held in a different position than in the previous frame. The water's movement is more pronounced, with the spoon's movements indicating that the water has been sucked away from the surface of the spoon. The person's hand is more likely to be holding the spoon under the faucet, allowing more time for the water to drain.
- Reference: Here, the bell pepper is more engulfed in water, evident by the sheen over its surface that suggests a steady flow is cascading over it. The water droplets have merged into a thin film, glossing the pepper and enhancing its bright red coloration. The hand adjusts its hold, now cradling the pepper from the top, allowing water to wash over more of its surface. The angle at which the water strikes the pepper has changed slightly, indicating movement and a more thorough rinse.

#### Sample 469 — During

- Similarity: 0.4521
- Prediction: In this frame, the person's hand is positioned in a slightly different position, indicating that they are preparing to eat. They are now able to grasp the container's contents, which are more or less in the same position as before. The object's shape is more apparent, suggesting that the container has been placed in the correct position. The hand's posture is more relaxed, implying that the person is holding the container.
- Reference: In this frame, the cover is noticeably being interacted with, as evidenced by the hand positioning around its sides. The cover's surface still displays a sheen, reinforcing the notion that it could be a reflective material. The curvature of the cover is more prominent here, hinting at its domed shape. It appears to be slightly tilted or in motion, possibly due to the person's actions. Adjacent to the cover, one can identify a stove's burner, indicating the cover's position relative to the cooking surface.

#### Sample 470 — During

- Similarity: 0.3165
- Prediction: In this frame, the bottle has been placed in a new position, with the lid still firmly attached to the bottle. The person's hand appears to be holding the bottle, indicating that they are preparing to open it. The bottle's contents are still in the same position as in the previous frame, suggesting that the bottle is still in its original position. The liquid content of the bottle remains the same, and there is no noticeable difference between the current state and the previous image.
- Reference: In this moment, the plug is further removed from the outlet compared to the previous frame. The individual's grip on the plug is firm, indicated by the slight compression of the yellow rubber gloves around their fingers. This suggests a deliberate action, likely the act of unplugging. The plug's prongs are more visible now, and it appears to be a standard, non-grounded two-prong plug. The background remains unchanged, crowded with kitchenware and items, which are out of focus.

#### Sample 473 — During

- Similarity: 0.3482
- Prediction: In this frame, the hose is now in the hands of a person who is holding the nozzle. The person's hand appears to be engaged in a more deliberate action, indicating that the water has been drained. The hose's surface appears to have been sprayed with water, implying that it has been washed away.
- Reference: In this frame, the action of opening the bottle progresses as the cap appears to be in the midst of being twisted off. The hands are positioned with one hand stabilizing the bottle while the other seems to be applying a twisting force to the cap. The cap itself shows a slight gap between it and the bottle's neck, indicating that the seal has been broken and the cap is partially unscrewed. The setting remains unchanged with kitchenware in the background, and the bottle still appears undisturbed content-wise, with no spillage present.

#### Sample 474 — During

- Similarity: 0.4419
- Prediction: In this frame, the rinsing spoon is now held in a different position, with the handle positioned slightly more vertically, indicating that the water has been sucked out of the spoon. The spoon's surface appears to be drier, and the water's flow seems to be more concentrated, suggesting that the spoon is being rubbed more vigorously. The hand's grip is more relaxed, and there's less of a gap between the spoon and the spoon, implying that the soap has been washed away some of the soap residue.
- Reference: In this frame, the holder's position has shifted slightly, with the person's hand now holding it upright under the stream of water. The holder's interior is less visible, but water can be seen splashing around the rim and the inner filter section. The water appears clearer than before, suggesting that most of the coffee grounds have been washed away. The exterior is also exposed to the water, indicating an ongoing effort to clean both inside and out.

#### Sample 477 — During

- Similarity: 0.4928
- Prediction: In this frame, the soup has been stirred more vigorously, indicating that it's ready to be served. The spoon's motion indicates that the ingredients are being added to the pan, which is likely a step in the process of preparing the soup. The color of the soup appears to be more vibrant, with a hint of a darker hue.
- Reference: In this frame, the flame beneath the pot has transitioned to a more vibrant blue at the core with hints of purple and lighter blue tones extending outward, reflecting a higher intensity and a more complete combustion. The light is stronger and brighter, showing that the burner is fully active now. The pot is bathed in this vivid light, with increased clarity seen in the reflection on the cooktop and the pot's sides, indicating a rise in temperature and energy being directed towards the contents of the pot.

#### Sample 480 — During

- Similarity: 0.4571
- Prediction: In this frame, the rinsing cup is now in a more concentrated state, indicating that the water has been sucked out of the container. The cup's surface appears to be slightly dampened, suggesting that there may be a slight movement in the water's movement. The person's hand is still holding the cup, implying that they are attempting to rinse it.
- Reference: Now, the liquid washing up is being actively applied onto the sponge. The stream of the liquid can be discerned as it makes contact with the sponge, creating a wet spot. This wet spot reflects light differently than the rest of the sponge, indicating that the sponge is beginning to absorb the liquid.

#### Sample 481 — During

- Similarity: 0.4513
- Prediction: In this frame, the rinsing pot is now in a more natural state, with the lid still slightly tilted, suggesting that the water has been sucked out of the pot. The person's hand appears to be holding the pot, indicating that the lid has been removed from the sink. The water level appears to have decreased, suggesting a deeper cleaning process.
- Reference: Now the jug begins to fulfill its purpose, with a steady stream of clear water cascading into it from the faucet above. The flow is centralized, targeting the heart of the jug’s basin, causing a swirl of bubbles to form on the surface as air is displaced by the incoming water. The hand adjusts slightly to stabilize the jug against the force of the water, while the level of the liquid rises visibly, indicating the jug's capacity is being tested.

#### Sample 482 — During

- Similarity: 0.4283
- Prediction: In this frame, the foil has been partially thawed. The person's hand is now more firmly grasping the foil, indicating that the foil is still in its packaging. The foil's surface appears to be more exposed to the light, implying that it may have been exposed to a light source, such as a stove or oven.
- Reference: In this frame, the packaging of the lighter meat, possibly chicken, is being interacted with. A pair of hands can be seen grasping the package, where one hand holds the body of the package while the fingers of the other hand appear to be prying or pinching at a corner of the seal. Despite this, the plastic wrapping remains mostly undisturbed, and the meat inside the package is still concealed. There's no sign of the seal being fully breached at this point.

#### Sample 485 — During

- Similarity: 0.4508
- Prediction: In this frame, a hand is positioned in front of the door, revealing a gaping gap between the door and the kitchen counter. The person's hand appears to be holding the door open, indicating that the door has been closed. The door's position is slightly blurred, suggesting that the person is attempting to open the door or close the door.
- Reference: In this scene, the milk carton has been released from the person's grasp and is captured in mid-descent towards the floor. The green carton with its label is in a vertical orientation, with the top side facing downward, suggesting it may not have been securely closed. The background is less cluttered here, featuring a broom and a dustpan against a wall, and what appears to be a container lid on the floor, indicating that the carton is likely falling in an area adjacent to the kitchen or a utility space.

#### Sample 490 — During

- Similarity: 0.3067
- Prediction: In this frame, the person is attempting to open the plastic bag. The person's hand is positioned in the middle of the bag, with the bag's edges exposed, indicating that the bag has been opened. The bag is now firmly wrapped in the plastic, which is likely a protective layer to protect it from the elements.
- Reference: In this moment, the tortilla is being maneuvered back towards its original packaging. The hand's grip has shifted, now supporting the tortilla more from beneath, with the fingers curving upwards, cradling its base. The tortilla's flexibility is evident as it displays a gentle droop, arching downwards due to gravity. Its surface is still unblemished, and it retains the circular shape characteristic of a classic tortilla, highlighting its apparent softness and readiness for use.

#### Sample 491 — During

- Similarity: 0.4542
- Prediction: In this frame, the pak choi has been partially thawed, indicating that the leaves have been thoroughly trimmed. The leaves are now arranged in a single layer on a cutting board, implying that they have been trimmed to the desired length. The knife's blade is now positioned at the center of the bok choy, suggesting that the knife has been slicked into the leaf.
- Reference: In this frame, the coriander has been partially cut, with both stems and leaves scattered across the cutting board. Some of the leaves appear to have been separated from their respective stems, and a few stems lay isolated, showing signs of recent slicing. There's a discernible difference in the arrangement of the coriander on the board, illustrating the ongoing process of cutting and prepping the herb.

#### Sample 494 — During

- Similarity: 0.4898
- Prediction: In this frame, the oven has been moved to a more stable position, indicating that it is still in its original position. The kitchen's lighting is now more reflective, suggesting that the oven is still occupied. The interior of the oven remains consistent with the previous frame, suggesting a gradual shift in the oven's position.
- Reference: The door is now partially open, revealing a portion of its contents. The handle, still on the right, is slightly more visible, indicating that it's been turned or pulled. A bit more light spills from the interior, making the adjacent surfaces brighter. The transition between the door and its surrounding cabinetry is more evident due to the door's changed position.

#### Sample 495 — During

- Similarity: 0.1989
- Prediction: In this frame, the rag is now in the hands of a person. The hand's movements seem to have been more deliberate, indicating that the person is attempting to remove it from its position. The rag's surface appears to be in a state of transition, suggesting that it has been taken out of place. The person's posture is more relaxed, suggesting a shift in the direction of the action.
- Reference: The plug remains in a similar position, but now it appears to be slightly askew, suggesting that a pulling force has been applied. The prongs are still engaged with the socket, but the angle at which the cord extends has shifted, becoming more pronounced towards the right, indicating movement. The environment is consistent with the previous frame, with the wooden chair leg, white skirting, and yellow tiling composing the surroundings. The plug's facade is more visible, and the socket looks standard with no distinct features or damage.

#### Sample 496 — During

- Similarity: 0.3735
- Prediction: In this frame, the tea towel is now positioned in a more streamlined position, with a slightly more rounded shape. The person's hand is now more pronounced, indicating that the towel has been placed on a table or counter. The towel's surface appears to be a bit looser than before, suggesting that it may have been pressed against the table or countertop. The hand's movements are more deliberate, implying that they are holding the towel in their hands, rather than attempting to grasp it.
- Reference: In this scene, the popcorn bag is held steadily, likely immediately after being shaken, as the hand and the bag are less blurred compared to the previous frame. The text and graphics on the bag are now legible, showing icons and instructions for proper microwave use. The top of the bag appears slightly inflated, a sign that the popping process has occurred or is nearing completion. The person's grip on the bag is firm, their thumb pressing down on the front face, possibly feeling for the consistency of the popped kernels inside.

#### Sample 5 — After

- Similarity: 0.4311
- Prediction: In this frame, the kitchen sink is now positioned in a more natural position, indicating that it has been removed from its original position. The kitchen's surface appears to have been wiped down with a damp cloth, suggesting that there is still a lot of debris on the surface.
- Reference: This perspective offers a broader view of the floor, revealing the edges of the tiles and the base of the kitchen cabinets. Here, the floor seems to have more noticeable dark spots and streaks of moisture from the cleaning process. These marks are irregularly shaped, with some areas appearing to have been missed by the wiping, leading to an inconsistent sheen on the tile surface. The light reflection is more pronounced, making the damp areas stand out against the matte, drier parts of the floor.

#### Sample 6 — After

- Similarity: 0.4738
- Prediction: In this frame, the kitchen sink appears to have been sanitized, indicating that the water has been drained out of the sink. The hand is now positioned in a position to ensure that the sink's surface is clean and the water is running smoothly. The kitchen's counters are still visible, suggesting that the kitchen is preparing for the next step of scrubbing.
- Reference: The chopping board is further cleaned, with the wet sheen more pronounced than in the previous frames, suggesting that more of the board's surface area has been covered by the cleaning process. The hand holding the sponge continues to scrub the board, focusing on its left side. There seems to be less visible soap foam, which could mean that the cleaning process is nearing its end, or the soap has been rinsed off more effectively.

#### Sample 8 — After

- Similarity: 0.4438
- Prediction: In this frame, the hand is holding the button on the coffee maker, indicating that it has been activated. The hand's position remains unchanged, suggesting that the button has been placed in a different position from the previous frame. The user's hand appears to be engaged in the process of adjusting the button's settings, which may indicate a change in the position of the button.
- Reference: The toaster's lever is now completely depressed, with the slots wholly accommodating the bread for toasting. A radiant, warm orange glow emanates from within the slots, indicative of the fully active heating elements. The surrounding countertop captures the gentle light spill, creating a cozy ambiance. The power indicator light is now brightly illuminated, confirming that the toaster is in full operation. A slight hint of steam or heat waves can be seen rising, testifying to the toasting in progress.

#### Sample 12 — After

- Similarity: 0.4239
- Prediction: In this frame, the bin's lid is now in a more natural position, indicating that the lid has been removed. The lid's position remains unchanged, suggesting that the bin has been partially removed.
- Reference: In this frame, the basket appears almost entirely open, revealing more of its inside, yet the content remains not fully discernible. There's a more prominent view of the person's legs and feet, standing beside the basket. The patterned textile or rug, and the tiled floor remain consistent in the scene.

#### Sample 15 — After

- Similarity: 0.3677
- Prediction: In this frame, the jar has been removed from the burner, indicating that the contents of the pot have been removed. The lid has now been removed, with the lid still firmly attached to the pot. The jar's contents are now in a more concentrated state, suggesting that there may be a slight movement in the process of removing the lid.
- Reference: The stock now appears thicker in consistency as it clings to the sides of the glass container when tilted. The surface of the stock shows waves and ripples, suggesting that it has been stirred or agitated recently. The color remains a consistent pale yellow, but there's a more pronounced sheen on the surface, potentially indicating a higher fat content or the reduction process. The glass is less full compared to the first frame, hinting at some level of evaporation or usage of the stock in between the frames.

#### Sample 18 — After

- Similarity: 0.4850
- Prediction: In this frame, the blender's lid has been removed, indicating that it is no longer in use. The user's hand appears to be engaged in a reversing action, implying that the blender is now inactive. The hand's position remains unchanged, suggesting that the blade is still attached to the bowl.
- Reference: The immersion blender is now fully engaged in the blending process, as evidenced by the increased disturbance in the liquid mixture, which now exhibits visible whirls and ripples. The person's hands are firmly in control, with one hand on the container providing stability and the other operating the blender with a purposeful grip. The shadow cast by the blender is more pronounced, indicating a slight change in the time of day or a shift in the light source. The environment remains consistent with the previous frames, with kitchen items in the background, yet the person's focus is solely on the task at hand.

#### Sample 20 — After

- Similarity: 0.2963
- Prediction: In this frame, a hand is holding a piece of paper in the middle of the tray, indicating that the paper has been removed from the tray. The paper's surface appears to have been partially removed, suggesting that the hand is attempting to remove the paper. The person's hand is still firmly grasping the paper, implying that they are removing the paper or wrapping it in some other way.
- Reference: Here, the yogurt's state has further evolved. It has been placed down with the hand retracting from the action, implying that the positioning of the yogurt container has been completed. The container rests at an angle, distinct from its previous upright position, which contributes to a sense of completion or finality in the sequence of arranging the containers. The kitchen setting serves as a passive backdrop, with the light reflecting off the surface indicating a well-lit environment.

#### Sample 21 — After

- Similarity: 0.4512
- Prediction: In this frame, the ricotta leaf has been placed in a bowl of water, indicating that the water has been drained. The leaf's surface appears to have been soaked in the water, suggesting that it has been thoroughly washed away. The hand's movements indicate that the leaf is now being held, with the fingers pointing at the leaf.
- Reference: The pak choi leaf is held closer to the camera, offering a more detailed perspective. Its well-hydrated state is evident from the sheen on its surface. The leaf, while still retaining its green vibrancy, has visible droplets of water clinging to it, highlighting its freshly washed status. The undulating edges of the leaf, along with the intricacies of its venation, are more discernible in this closer view.

#### Sample 24 — After

- Similarity: 0.4586
- Prediction: In this frame, the bread has been placed in a new position, with the bread's surface exposed. The bread is now firmly grasped by the hand, indicating that the bread is ready to be sliced. The hand's grip is still firm, and the bread seems to be ready for use.
- Reference: In this frame, the scissors have been removed from the clip, and the person's hands have changed position. The right hand now holds the clip between thumb and index finger, pulling it away from the packet. The left hand appears to be holding the packet steady. The clip has opened further, indicating that the action of cutting or prying with the scissors was successful. There is a slight disarray in the surrounding objects, such as the shifted napkin, which may imply movement in the environment.

#### Sample 26 — After

- Similarity: 0.4350
- Prediction: In this frame, the foil has been removed from the tray, indicating that it has been partially removed. The person's hand is now more engaged in the action of removing the foil, implying that the foil is being removed from its packaging. The foil's surface is more exposed, suggesting that there may be a gap between the foil and the tray's edge.
- Reference: The cling film now exhibits more pronounced usage. It has been further unrolled and the leading edge seems to have been stretched out more than before, likely indicating that the film is being prepared for use. There are visible warps and widening in the plastic near the roll, and the stretched portion shows varying degrees of transparency due to the stretching. The person’s hands have shifted position, likely to accommodate the increased length of film that has been dispensed.

#### Sample 28 — After

- Similarity: 0.2243
- Prediction: In this frame, the hand is now positioned on top of the sink, demonstrating a shift in the position of the bowl. The bowl's surface appears to have been partially removed, suggesting that the bowl has been placed in a different position. The hand's movements are more relaxed, indicating that there may be a slight movement in the bowl or the bowl itself.
- Reference: The tearing process is now complete, and the paper is divided into two distinct pieces. The left hand holds a completely detached segment, with a rough, frayed edge where the fibers of the paper were separated. The right hand still holds onto the original sheet, now with a complementary jagged edge at the bottom where the tear was finalized. The tear's path has left a distinctly textured edge, contrasting with the original smoothness of the intact paper.

#### Sample 31 — After

- Similarity: 0.4682
- Prediction: In this frame, the person's hand is now more focused on the surface of the cloth, indicating that the cleaning process has been completed. The cloth's surface appears to have been cleaned, suggesting that there is still a lot of work to be done.
- Reference: The glass has been repositioned further to the right, confirming the continuous movement from the previous frame. The person's hand has moved along with the glass, indicating a controlled slide. The blurred reflection on the base of the glass is more pronounced, showing a consistent movement. There's a dynamic interaction between the hand and the object, where the hand's steadiness and the glass's balance appear synchronized in the action of sliding.

#### Sample 32 — After

- Similarity: 0.4331
- Prediction: In this frame, the lid has been removed from the container, indicating that it is now in the hands of the person who is holding it. The person's hand is still firmly grasping the lid, which is likely a sign that the lid is in the process of being removed. The contents of the container are still visible, including the lid's contents, as well as the lid itself.
- Reference: The plastic wrap has been drawn further back, exposing a larger portion of the lettuce head. The leaves now have more space to fan out, and they exhibit a mixture of light and dark green shades, characteristic of the leafy layers of the head. It's evident that the lettuce is still quite fresh, with the leaves showing a healthy, plump appearance. The person's hands are more engaged in the unwrapping process, suggesting an eagerness or readiness to prepare the lettuce for consumption or use in a dish.

#### Sample 33 — After

- Similarity: 0.1972
- Prediction: In this frame, the sink appears to be in a more active state, indicating that the water has been drained. The hand's movements are more pronounced, suggesting that the sink has been taken out of action. The sink's surface appears to have been soiled, suggesting a gradual change in the water's state. The kitchen's lighting is still dim, suggesting the sink may be a source of heat.
- Reference: In this frame, the cabinet door has been pulled open even more, almost to its fullest extent, allowing a full view of the shelves. The lower shelf's orderly array of cans is completely visible now, and the upper shelf reveals a collection of various-sized items that seem to be jars and other containers, some with identifiable labels, others obscured by the angle. The items on the upper shelf are less uniformly arranged than the cans below, suggesting a more casual approach to placing frequently used items within easy reach.

#### Sample 36 — After

- Similarity: 0.3831
- Prediction: In this frame, the bread has been placed in a resealable plastic bag, indicating that it has been removed from its packaging. The bread is now firmly pressed against the edge of the bag, suggesting that the bread is being handled with care. The palm of the hand appears to be firmly grasping the bread, implying that the hand is holding the bread in place.
- Reference: The tub has been opened, revealing the golden buttery spread inside, which has a smooth surface except for a slight disturbance where a portion has been skimmed off, most likely by the knife previously seen in the right hand. The lid has been neatly flipped open and placed back onto the tub, but slightly ajar, indicating recent use. The consistency of the butter appears soft, as is common with spreads of this type, and a small portion adheres to the knife's edge, showing it has just been used.

#### Sample 38 — After

- Similarity: 0.4995
- Prediction: In this frame, the onion has been slicked open, revealing a charred portion of the onion. The knife's edge is visible, indicating that the onion is now fully sliced and ready to be sliced. The onion's skin is exposed, suggesting that the knife has been used to slice the onion in a more precise fashion. The peeler's fingers are positioned on the cutting board, ensuring that there is sufficient room for the onion to remain intact.
- Reference: Here, the aubergine has been further divided, the knife nearing the completion of the cut, just short of the stem. The two halves are hinged at the stem end, splayed open but still connected. The cut reveals the patterned interior, with seeds dotted around the central column of flesh. The hand's grip has adjusted to the new form, with the fingers curling more around the now partially separated sections, and the thumb repositioned to prevent the halves from fully detaching.

#### Sample 41 — After

- Similarity: 0.4051
- Prediction: In this frame, the microwave door is positioned in a slightly different position, indicating that it has been opened. The person's hand appears to be grasping at the door, suggesting that the door has been closed. The door's contents are still visible, including the contents of the microwave, as well as the door itself.
- Reference: In this final frame, the milk bottle maintains its central position in the scene, with the cap clearly in a different state compared to earlier images. The hands seen in the periphery are positioned as though they are in the process of closing or have just finished closing the bottle. The cap appears to be settled more securely on the bottle, suggesting the action of sealing the bottle is either complete or nearly so. The lighting and reflections remain consistent, highlighting the bottle's curves and the cap's smooth, round shape.

#### Sample 45 — After

- Similarity: 0.4082
- Prediction: In this frame, the spoon is now firmly held in place, indicating that it is ready to be used. The spoon's surface appears to be slightly dampened, suggesting that the spoon has been agitated. The hand's movements seem to have shifted away from the spoon, suggesting a more gradual movement of the spoon.
- Reference: The jam is now in a more disheveled state, with some of it smeared on the side of the bowl and a smaller quantity adhering to the fork. It has lost its initial compact shape, becoming more spread out and less uniform. The strands that once connected the jam to the jar have been broken, leaving behind only a thin, tapering trail from the fork to the last of the jam's body, suggesting the completion of the transfer process.

#### Sample 51 — After

- Similarity: 0.3481
- Prediction: In this frame, the bin's lid is positioned in a slightly different position, indicating that the lid has been removed from the bin. The lid's position remains unchanged, suggesting that the bin has been partially removed.
- Reference: The image now shows the filter being inserted into a plastic housing, which is part of a larger appliance or system. The person's hands are positioned in such a way as to facilitate the careful placement of the filter back into its operational position. This housing suggests the filter is part of a mechanism that requires periodic maintenance. The edges of the filter fit snugly into the housing, indicating a proper design for ensuring that the unfiltered air or water does not bypass the filter. The area around the housing appears clean and well-maintained, highlighting the person's probable attention to regular upkeep.

#### Sample 53 — After

- Similarity: 0.3844
- Prediction: In this frame, the rice appears to be fully cooked, indicating that the cooking process has been completed. The surface of the rice seems to be slightly charred, suggesting that it may have been partially cooked. The water's consistency is more pronounced, suggesting a more gradual cooking process. The spoon's motion indicates that the rice has been thoroughly stirred, possibly with a fork or spatula.
- Reference: The cooking process has progressed, as evidenced by the fewer visible bubbles and a thicker consistency of the curry. The ingredients have broken down further, becoming a part of the sauce, and the oil is more pronounced on the surface, suggesting a completion of the frying stage. The wooden spatula is partially submerged, illustrating the increased density of the curry.

#### Sample 56 — After

- Similarity: 0.3759
- Prediction: In this frame, the box has been placed in a new position, with the lid open, indicating that the contents of the box have been removed. The person's hand is still holding the box, which is likely a sign that the lid has been removed from the box.
- Reference: The packaging is now in an advanced state of crumpling. The hand has shifted position, now grasping the lower part, indicating a progression in the crumpling process. The once cylindrical shape of the packaging is significantly distorted, with multiple folds and creases compacting it into a smaller, irregular form. The reflective surface is mostly crinkled, losing much of its initial luster and now exhibits a matte finish due to the extensive manipulation.

#### Sample 57 — After

- Similarity: 0.3549
- Prediction: In this frame, the pot's lid has been removed from the burner, indicating that the water has been drained out of the pot. The person's hand is still holding the lid, which is likely a sign that the pot has been placed in a proper setting. The water level remains consistent with the previous frame, suggesting that there may be a change in the position of the lid.
- Reference: The filter is now held at a more pronounced angle, with the coffee maker slightly out of immediate reach below. The hand's grip has shifted to support the filter's base, likely to provide stability as the weight of the grounds could cause tearing or spillage if not handled carefully. The radial structure of the filter's base is more pronounced, possibly due to the changing grip and angle at which the filter is held. There's a clear intent to transport the used filter, possibly to a trash receptacle.

#### Sample 58 — After

- Similarity: 0.4902
- Prediction: In this frame, the person's hand is more firmly grasped, indicating that the door has been closed. The door's contents are still visible, including the contents of the drawer, as well as the door itself, which appears to be partially open. The hand's focus is now on the door, which is now partially closed.
- Reference: In this frame, the cupboard door is at its maximum aperture, swung entirely to the right, exposing the contents comprehensively. It reveals a more orderly arrangement within the cabinet, with items stored in their designated places. Several utensils, possibly including spoons or spatulas, hang from a rack, while other tools are neatly placed in compartments or holders. The image's angle offers a bird's-eye view of the cupboard, showcasing the efficiency of space utilization within.

#### Sample 61 — After

- Similarity: 0.4169
- Prediction: In this frame, the table has been placed in a position where the hand is holding the table, indicating that the table is now in the position of its original position. The hand is now positioned in the middle of the table and the table's surface appears to have been wiped down. The table has now been placed on a flat surface, with the table still in the same position as the table in the previous frame.
- Reference: In this frame, the crumb has been decisively moved from its original position, now closer to the vacuum cleaner's nozzle. The disturbance in the fabric of the tablecloth around the crumb is more pronounced, with folds and creases leading towards the nozzle, visually narrating the path of movement. The crumb itself is more obscured by the shadow of the vacuum cleaner, highlighting the imminent action of it being picked up. The proximity to the nozzle and the altered lighting condition suggest the crumb's journey is nearing its end.

#### Sample 62 — After

- Similarity: 0.3583
- Prediction: In this frame, the flour has been incorporated into the dough, resulting in a smoother and more uniform dough. The dough is now more dense, with a more uniform texture and consistency, indicating that the ingredients have been thoroughly incorporated. The hand's movements indicate that the dough has been thoroughly stirred, which indicates that it is ready to be kneaded.
- Reference: A stream of olive oil can be seen flowing from the bottle, indicating that the pouring action has commenced. The oil cascades in a smooth, continuous stream, reflecting light as it travels to the bowl. The hand holding the bottle is steady, guiding the flow of the oil to ensure it mixes evenly with the contents of the bowl. The pour is controlled, and the stream is narrow, suggesting a desire to regulate the amount of oil being added. The overall scene remains cluttered, but the act of pouring oil has become the central activity, with the hand and bottle coordinated in their purpose.

#### Sample 63 — After

- Similarity: 0.3920
- Prediction: In this frame, the tomato has been placed in a single layer on a plate, indicating that it has been partially removed from the plate. The tomato's surface appears to be partially covered, suggesting that there may have been a deliberate effort to remove the tomato from the bowl. The hands are now more involved in the process of removing the tomato, implying that the tomato may have remained in the bowl for a long time.
- Reference: The bowl now holds a more homogenized mixture, with the egg yolk and whites thoroughly combined into a cohesive, light yellow substance. The pepper flecks are evenly dispersed throughout, and the mixture has a slightly frothy texture, indicating vigorous mixing. The fork is actively being used, its tines coated with the egg mixture, showing an ongoing process of agitation that's leading to the incorporation of air, which is essential for a fluffy texture upon cooking.

#### Sample 73 — After

- Similarity: 0.4706
- Prediction: In this frame, the sink has been sprayed with water, indicating that it is now fully soaked. The person's hand is still holding the sponge, which appears to have been washed, and the sponge's surface appears to be slightly dampened, suggesting that the sponge has been thoroughly rinsed.
- Reference: The grid now appears horizontally aligned with the edges of the sink, suggesting it has been positioned or is in the process of being set down. The hands are symmetrically placed, with each gripping opposite sides of the grid, likely exerting equal pressure to ensure its stable placement. Water beads are present on the grid, more prominently than before, possibly due to the hands' movement causing water to disperse along the grid's surface.

#### Sample 83 — After

- Similarity: 0.2973
- Prediction: In this frame, the man is holding the garlic clove, indicating that he is about to remove it from the kitchen counter. The hand is still firmly grasping the clove, suggesting that the garlic has been removed from its container. The chef's hand appears to be removing the clove from the container, implying that the clove has been partially removed.
- Reference: The jar of pesto now shows clear signs of having been accessed. The pesto level appears to be slightly lower than before, with some of its contents possibly scooped out. Streaks and smudges of pesto are evident along the inner walls of the jar, indicating that someone has interacted with it, likely using the utensil. The previously undisturbed texture now seems a bit uneven with minor disruptions.

#### Sample 86 — After

- Similarity: 0.1673
- Prediction: In this frame, the person's hand is more firmly grasping the bag, indicating that the bag has been placed in the hands of the person who is holding it. The bag's contents appear to have been removed from the bag and the bag is now in a more upright position. The hand's movements are more relaxed, suggesting that they are preparing to open the bag.
- Reference: The leek's trajectory continues its unwelcome descent, now even closer to the ground. The motion blur has intensified, especially around the green leafy ends, indicating an acceleration of its fall. The plastic sheath appears more disheveled, possibly due to air resistance and the leek's own motion. The leek's base end, once pristine white, is now almost out of view, implying it may have rotated slightly as it fell, with the possibility of impact becoming more imminent.

#### Sample 87 — After

- Similarity: 0.4330
- Prediction: In this frame, the rinsing device is now in a more natural position, with the water dripping out of the handle. The hand's grip is tighter, indicating that the water has been drained away from the inside of the device. The water level appears to be at an all-time low, suggesting that there may be a slight movement in the water's direction.
- Reference: The saucepan lid in this frame appears clearer than before, hinting at the progression of the cleaning process. There are still traces of moisture, suggesting a recent rinse. The person's hands are positioned in a manner that looks like they are ensuring that all areas of the lid have been adequately addressed. The light reflections seem more consistent across the lid, indicating fewer residues or spots.

#### Sample 88 — After

- Similarity: 0.4379
- Prediction: In this frame, the lid has been removed from the container, indicating that it is now in the hands of the person holding it. The person's hand is still firmly grasping the lid, which is likely a sign that the lid is in the process of being removed.
- Reference: In this frame, the hands grasp the container more securely, and a notable shift in the arrangement of the cheese slices can be observed. The top slice has been disturbed from its previously neat stack, now protruding at an angle indicative of potential selection or preparation for use. This slight disarray contrasts with the earlier orderly presentation, conveying a sense of imminent consumption or culinary application.

#### Sample 89 — After

- Similarity: 0.3191
- Prediction: In this frame, the door has been closed, revealing a gaping gap in the middle of the frame, indicating that the door is closed. The shadow of the door's surface is evident, suggesting that there may be a slight movement in the process of closing the door or removing it from the frame.
- Reference: In this frame, the squash container seems to retain its position from the second frame, with minimal to no noticeable difference. The label graphics remain visible, reiterating its blue and green hues. The proximity of the white cap to the container is consistent with the second frame, emphasizing that the cap has not been replaced.

#### Sample 90 — After

- Similarity: 0.4441
- Prediction: In this frame, the peach has been partially sliced, indicating that it has been fully sliced. The peeler's hand is now positioned in the middle of the fruit's skin, revealing a sprinkling of flesh on the skin. The knife's edge is slightly curved, suggesting that the fruit has been sliced in a circular motion.
- Reference: The pepper, still vibrant and freshly cut, has been further dissected into individual segments. It remains on the same wooden cutting board, with the inside facing the viewer. The segments are arranged in an orderly fashion, fanned out from the stem, which is now at the top of the frame. Each segment is neatly sliced, with smooth edges and the seeds have been removed, indicating meticulous preparation.

#### Sample 91 — After

- Similarity: 0.4678
- Prediction: In this frame, the squeegee has been placed in a position where the water has been rinsing it, indicating that the water is now being drained. The hand's movements are more relaxed, suggesting a more thorough rinse. The water level appears to be a little higher, suggesting that there may be some movement in the water's direction.
- Reference: In this frame, the cleaning process has advanced; the person's hands are actively scrubbing the cap with a green scrub sponge. This direct action indicates a shift from rinsing to scrubbing, likely to address the more persistent areas of buildup. The cap is positioned in a way that suggests a rotational scrubbing motion, applying the sponge's abrasive surface to the cap's top and side, where residues commonly accumulate.

#### Sample 96 — After

- Similarity: 0.2761
- Prediction: In this frame, the person's hand is more firmly grasped, indicating that they are preparing to eat. The hands are now more engaged in the process of preparing the food, implying that the food is ready for cooking.
- Reference: The opening of the packaging has progressed further. The plastic film has now been peeled back considerably, exposing more of the salmon's surface to the air. The top part of the packaging is visibly deformed due to the peeling, while the bottom part still clings to the fish, maintaining its original vacuum-packed appearance. The person's hands are actively working on removing the packaging, indicating a continuation of the opening process.

#### Sample 97 — After

- Similarity: 0.4648
- Prediction: In this frame, the box has been placed in a new position. The hand is now more engaged in the action of removing the box from its original position, indicating that it has been removed. The contents of the box are still visible, including the box's contents, as well as the packaging. The person's hand is still firmly grasping the box, which is likely a sign that the box is being removed.
- Reference: The action has progressed further, with the cereal continuing to pour out of the bag, which is now captured mid-swing as the hand is moving. The cereal pieces appear more blurred due to the motion, giving a sense of the speed at which they are being dispensed. The bowl below is no longer visible, but one can infer that it is continuing to collect the cereal. The rapid movement of the hand and bag implies an attempt to control the quantity being poured or to shake out the last pieces from the bag.

#### Sample 100 — After

- Similarity: 0.3985
- Prediction: The camera's focus shifts to a more detailed view of the kitchen, indicating that there is a greater amount of activity in the kitchen. The kitchen appears to have been closed, with the door still open, suggesting that there may be a gap between the kitchen and the refrigerator.
- Reference: The scene has now been enveloped in darkness, with the light source seemingly turned off. The absence of light has rendered the room's details nearly indiscernible, with only vague shapes and forms distinguishable in the deep shadows. What were once reflective surfaces have now blended into the obscurity, losing the luster they exhibited when illuminated. The environment exudes a sense of stillness and quiet, typical of a space where the light has been switched off and night has fallen.

#### Sample 104 — After

- Similarity: 0.4706
- Prediction: In this frame, the lettuce has been partially thawed, indicating that it has been thoroughly washed. The hands are now more engaged in the process of removing the leaves, which are likely to be a part of the preparation process. The greens appear to have been thoroughly rinsed, with the leaves still slightly damp and wilted.
- Reference: In this frame, the beans are being actively placed into the colander, with the hand's grip adjusted to control the placement. The green beans inside the colander appear more numerous now, indicating that the trimming task is well underway. The trimmed ends of the beans are clearly visible, and the beans' bright green hue remains consistent, suggesting that they are being processed shortly after being cut to preserve their freshness. The kitchen sink and countertop continue to serve as a backdrop to this meticulous preparation task.

#### Sample 110 — After

- Similarity: 0.3957
- Prediction: In this frame, the hand is now positioned in a more streamlined position, indicating that it has been taken out of the kitchen. The hand's focus is now on the surface of the oven, suggesting that the oven has been removed from the oven and replaced with a new one.
- Reference: In this frame, the chair has been moved further from the table, and its orientation has changed noticeably. The distance between the chair and the table has increased, which is evident by the larger expanse of tiled floor now visible between them. The chair's shadow stretches out on the floor, altered by the movement and the angle of the light source. The chair's position relative to the camera has shifted, suggesting continued movement.

#### Sample 111 — After

- Similarity: 0.3574
- Prediction: In this frame, the sink appears to have been sanitized, indicating that it has been thoroughly washed. The person's hand is now more focused on the sink, suggesting that the water has been drained. The sink's surface appears to be cleaner, with a more streamlined appearance.
- Reference: The cloth now appears to be in a more relaxed state compared to the previous frame. Its texture and spread suggest that it has been released or lessened from the squeezed position it was in earlier. While it still retains numerous folds and creases, it looks more spread out, indicating the release of pressure. The cloth continues to display signs of dampness, and its positioning suggests it's still being held or manipulated, albeit with less force than before.

#### Sample 113 — After

- Similarity: 0.3705
- Prediction: In this frame, the sink is now more firmly held, indicating that it has been fully rinsed. The person's hands are now more engaged in the process of rinsing the sink, which is likely a sign of a more thorough cleaning. The water level appears to have decreased, suggesting that the sink has been thoroughly washed.
- Reference: The burner cap here presents a significant improvement in cleanliness. The majority of the surface now exhibits the metal's innate color and texture, with only a few stubborn spots of carbonized debris remaining. The cap's edges and the holes are more defined, suggesting that the cleaning has been effective in removing the layers of grime. The presence of water and suds indicates an ongoing cleaning process, and the hands appear to be conducting a final inspection or perhaps targeting the remaining soiled areas for a last scrub.

#### Sample 119 — After

- Similarity: 0.4234
- Prediction: In this frame, the spout is now held in a position that allows the water to drain from the inside of the bowl. The water's flow is more concentrated, indicating that the bowl has been rinsing, rather than being sprayed. The hand's movements are more relaxed, suggesting that the water has drained away from the bowl's surface.
- Reference: In this frame, the V60 is again submerged, but this time the hand is employing a scrubbing brush to clean its interior. The positioning of the brush implies a focus on the inner surface of the V60, likely targeting stubborn coffee stains or residue. The vigorous motion of the hand and the dynamic swirl of the bubbles around the V60 suggest an intensive cleaning process, focused on ensuring the V60 is thoroughly scrubbed.

#### Sample 136 — After

- Similarity: 0.4806
- Prediction: The bin's lid is now fully open, indicating that the contents of the bin have been removed. The person's hand is now positioned in the middle of the action, revealing a slight movement in the process of removing the lid. The object's contents remain in the same position as in the previous frames, with the lid still firmly attached to the bin.
- Reference: In this frame, the action of emptying the pan into the bin seems to have been completed. The bin appears fuller, with a varied assortment of discarded food items piled on top. The layers of food waste now seem to merge, making it slightly challenging to distinguish between older and newer additions. However, the presence of the previous items like pasta and vegetables is still prominent, and there's an even spread of different food types, indicating a diverse range of leftovers.

#### Sample 142 — After

- Similarity: 0.3953
- Prediction: In this frame, the lid has been removed from the pot, indicating that the lid is now fully open. The person's hand is now more likely to be holding the lid, implying that they are preparing to place the lid on top of the pot.
- Reference: The surroundings in this frame blur slightly, possibly due to rapid motion or a shift in focus. The person's hands are still prominently displayed, and their interaction with the plate continues. While the sausage is not overtly visible, the positioning of the hands and the context suggests the sausage might be beneath the plate or has been moved to another location in this sequence.

#### Sample 145 — After

- Similarity: 0.2634
- Prediction: In this frame, the fruit has been partially sliced, indicating that it has been fully sliced. The knife's edge has been shaved off, suggesting that the fruit is now sliced into smaller pieces. The fruit's skin has been exposed to the cold, resulting in a smoother, more tender slice of fruit.
- Reference: Here, the pitta bread has been partially immersed into the hummus. A portion of the bread is submerged, gathering a generous amount of the creamy dip. The part of the pitta that's dipped in the hummus has a noticeably wet appearance, glistening from the moisture and indicating a successful scoop. The non-dipped portion remains untouched, providing a contrast to the dipped end, showcasing the effectiveness of the dip.

#### Sample 147 — After

- Similarity: 0.3561
- Prediction: In this frame, the user's hand is positioned on the side of the stove, indicating that the burner has been turned on. The hand's position is consistent with the previous frame, suggesting that the user is now adjusting the heat level of the burner.
- Reference: The environment around the mixer now appears more blurred, suggesting rapid movement or a swift action taking place. The mixer, while still recognizable, seems to be in the midst of a quick rotation or shift, likely guided by the user's hand. The lid on the mixer is firmly in place, ensuring the contents inside remain secure despite the rapid movement.

#### Sample 150 — After

- Similarity: 0.2938
- Prediction: In this frame, the kettle is now in a more upright position, with the lid still firmly attached to the pot. The person's hand appears to be holding the kettle, indicating that the action has taken place. The water level remains the same, suggesting that the kettle has been placed in the correct position. The liquid level remains consistent with the previous frames, suggesting a gradual increase in the volume of the kettle.
- Reference: The hand is now in direct contact with the spice, suggesting that the spice has been actively selected and is being removed from its original position. The other surrounding items have become secondary as the primary interaction is between the hand and the spice. The gesture of the hand indicates a firm grip, and it's evident that the spice will be used or inspected, taking it out of its passive state in the cupboard.

#### Sample 153 — After

- Similarity: 0.3656
- Prediction: In this frame, the person's hand is now more focused on the surface of the sink, indicating that there is more work to be done. The sink's surface appears to be a bit cleaner than before, suggesting that the cleaning process has been a step forward. The water level appears to have decreased, suggesting a more gradual movement of the hand, which may indicate a deeper cleaning effort.
- Reference: The scene has evolved into one where the pepper mill is being maneuvered with intention, as indicated by the hand's confident grip and the blurred motion of the mill and the hand together. This motion blur indicates a swift, directed movement, likely an action to place the pepper mill back into its rightful position or to continue with its intended use. The hand's position at the top of the mill suggests a more stabilized and deliberate control, contrasting with the previous frames.

#### Sample 158 — After

- Similarity: 0.3936
- Prediction: In this frame, the bowl has been moved away from its original position, indicating that it is now in a different position from the previous frame. The bowl's surface appears to have been rearranged, suggesting that the bowl is now positioned in the same position as the previous frames. The object's position remains unchanged, implying that it has been placed in the correct position.
- Reference: The orange has travelled further from its original position. It's almost at the edge of the table, with increased motion blur indicating its consistent movement. The reflection of the light source on the orange's skin has shifted towards the opposite side, now highlighting different surface imperfections and presenting a dynamic change in its overall visual perception.

#### Sample 162 — After

- Similarity: 0.4263
- Prediction: In this frame, the jar is now in a new position, with the lid still attached to the top of the container. The person's hand is now more focused on the container, indicating that the lid has been removed. The jar's contents are still visible, including the contents of the bottle and the lid.
- Reference: The measuring jug is now being held aloft, providing a clearer view of its design and scale. The white measurement markings are visible, suggesting that the jug can measure significant volumes, suitable for a variety of kitchen tasks. The action of lifting the jug implies that it has been selected for use, and the person’s task progression is evident as the hand grips it firmly, ready to measure ingredients. The surrounding environment remains a backdrop of kitchenware and utensils, unchanged from the previous activities.

#### Sample 163 — After

- Similarity: 0.2586
- Prediction: In this frame, the person's hand is positioned on the edge of the kitchen counter, indicating that the food has been placed on the counter. The hand's focus is on the food, which appears to be preparing for cooking. The hands are still holding the food in their hands, suggesting that they are preparing to eat it.
- Reference: The tablecloth is now more spread out, showcasing more of its surface area. It drapes over part of a table and extends towards the floor. The cloth's edges are more visible, and there seems to be less movement, indicating that the process of unfolding and setting might be nearing its conclusion. The tablecloth's texture and any potential designs it might have are clearer in this frame than in the previous ones.

#### Sample 166 — After

- Similarity: 0.4628
- Prediction: In this frame, the rag is now in the hands of the person holding it, indicating that it has been thoroughly washed. The person's hand appears to be engaged in a more deliberate action, possibly a rinsing motion. The rag's surface appears to have been dampened, suggesting that the water has been drained out of the cloth. The hand's movements are more relaxed, suggesting a deeper cleaning process.
- Reference: The bottle now shows a notable change as the person's hand has shifted position, indicating an action of twisting or securing the cap. The cap seems to be in the process of being fastened onto the bottle, as inferred by the alignment of the person's fingers, which suggest a gripping and turning motion. The surrounding objects remain static, with the kitchen sink and tiles forming a consistent backdrop, but the dynamic hand movement draws the focus to the action of closing the bottle.

#### Sample 169 — After

- Similarity: 0.3978
- Prediction: In this frame, the bowl is now positioned in a position that allows the water to drain away from the inside of the bowl. The water's surface appears to have been drained out, indicating that the bowl has been rinsing. The hand's movements are more relaxed, suggesting that the water has sucked away some of the excess water. The bowl's shape appears to be more streamlined, suggesting a more thorough rinse.
- Reference: The cleaning process has advanced significantly, with the water having softened and dissolved much of the residue, revealing more of the tray's underlying surface. A swirling pattern of soap suds and loosened debris is now present, creating a marbled effect across the tray. This suggests that the combined action of water and possibly detergent is breaking down the charred layers, making them easier to remove. The person's grip remains firm and controlled, facilitating thorough rinsing.

#### Sample 170 — After

- Similarity: 0.4020
- Prediction: In this frame, the frying pan has been removed from the burner, indicating that the cooking process has been completed. The pan's surface appears to be in a state of disintegration, suggesting that there may have been a sudden change in the position of the pan. The person's hand is still motion-free, with the pan still tilted in the direction of the burner.
- Reference: In this frame, the hand and the shaker are no longer directly over the tomatoes, indicating the conclusion of the seasoning process. The focus has shifted, and the spice shaker is now oriented towards a different part of the kitchen counter. The tomatoes rest undisturbed on the plate, their seasoned surface untouched since the last action. The background contains elements such as a knife, an empty plate, and packaged food items, suggesting that the preparation of a meal is underway, with the seasoning of the tomatoes being one of the steps in the culinary process.

#### Sample 171 — After

- Similarity: 0.4567
- Prediction: In this frame, the pot is now positioned in a position where the water has reached a boiling point, indicating that the pot has reached its boiling point. The pan's surface appears to be slightly tilted, suggesting that the water is still able to circulate through the pot. The spoon's movements indicate that there may be a slight movement in the pot's direction, possibly due to the water's evaporation.
- Reference: The oat in this frame demonstrates further displacement and redistribution within the pan. There are more pronounced pockets of uneven distribution, indicative of more substantial agitation or movement. The edges and surface of the oat appear more irregular, with clusters and gaps more evident. While the oats still appear predominantly raw, there's a perceptible difference in their arrangement and distribution compared to the previous frames.

#### Sample 174 — After

- Similarity: 0.3030
- Prediction: In this frame, the carrots appear to be fully cooked, indicating that they've been partially removed from the pan. The color of the vegetables appears to be more vibrant, suggesting that the cooking process has been completed. The carrots are now a bit more charred, with a darker hue to them, suggesting a more gradual cooking process.
- Reference: In this frame, the colander is now positioned over the sink, as if the person is preparing to drain excess water or give the beans another rinse. The beans are settled at the bottom, still wet and shimmering under the light. The person's other hand is visible, wearing a yellow glove, possibly to protect against hot water or to keep hands clean. Below the colander, the shiny sink basin reflects the beans' colors, and the overall atmosphere suggests a diligent and thorough cooking process.

#### Sample 182 — After

- Similarity: 0.2593
- Prediction: In this frame, the person's hand is positioned in the middle of the room, indicating that the door is open. The lighting is dim, suggesting that there may be a gap between the window and the door, which is likely a sign that the person is attempting to close the door.
- Reference: This scene shifts focus to the task at hand, where a person’s hands are visible, holding a bundle of washed clothes. The colors are vibrant, with a prominent teal shirt and a pair of white socks, which are slightly discolored, suggesting use. The clothing appears to be in a state of being removed from the washing machine, as evidenced by the manner in which they are bunched up and gripped, ready to be transferred to the next stage of laundering.

#### Sample 187 — After

- Similarity: 0.3809
- Prediction: In this frame, the pot appears to have been removed from its container, indicating that it has been placed in a new position. The person's hand appears to be removing the pot from the container, suggesting that the pot is still in its current position.
- Reference: The chicken now seems to be momentarily set aside, as the individual has completed the hand washing and is drying their hands with what appears to be a yellow kitchen cloth. The chicken remains on the cutting board as in the first frame, with no additional preparation evident. This suggests that the process of cutting the chicken has been momentarily halted while the person attends to personal cleanliness, maintaining good kitchen hygiene practices.

#### Sample 189 — After

- Similarity: 0.3073
- Prediction: In this frame, the cheese has been partially cut off, with the knife still firmly attached to the cutting board. The knife's blade is now positioned in the middle of the cheese, indicating that the knife has been inserted into the cheese. The cheese's texture is more uniform, with a smoother texture than the previous frame.
- Reference: The cake has undergone further reduction in this frame. The crumbly golden-brown top still remains prominent and offers a delightful contrast to the darker, moist interior. Yet another segment has been cut, revealing more of its luscious inside. The cake now covers just about half of the circular purple plate, with the freshly cut edge indicating the most recent slice that was taken.

#### Sample 190 — After

- Similarity: 0.4645
- Prediction: In this frame, the chopping board has been removed from the cutting board, indicating that the knife has been slicked. The knife's blade is now positioned in the middle of the board, suggesting that there is still room for the knife to cut through the board. The board's surface appears to have been trimmed, suggesting a more thorough cut.
- Reference: Further slices of the spring onions have been added to the growing pile, and the bunch is noticeably diminished, indicating the progress of the task. The varying shades of green to white gradient in the onion rings become more pronounced as they accumulate, giving a visual representation of the onion's natural color transition. The remaining unsliced portion of the bunch shows signs of handling, with some of the green stalks bent where they have been held back to facilitate the cutting. The knife, a constant in the process, rests momentarily on the cutting board, its blade smeared with the fresh remnants of the onions, pausing in action.

#### Sample 196 — After

- Similarity: 0.4172
- Prediction: In this frame, the bread has been placed in a new position, with the hands firmly engaged in the action. The person's hands are now positioned in the middle of the bread, indicating that the bread is ready to be sliced. The bread's surface appears to have been partially sliced, suggesting that the hand is preparing to slice the bread.
- Reference: The bag now appears to be in a more finalized state of folding or sealing. The hand's grip has shifted, possibly indicating the end of the folding process. The bag's surface appears more even and settled, with fewer visible contents. The overall structure of the bag seems more compact and tidier than in the previous frames, suggesting that the action of folding or sealing is nearing its completion.

#### Sample 203 — After

- Similarity: 0.3389
- Prediction: In this frame, the bottle has been placed in a new position, indicating that it has been taken out of its original position. The hand is now positioned on top of the bottle, with the bottle's handle positioned at the center of the frame. The bottle appears to have been removed from its container, and the lid has been removed.
- Reference: Now, the squash is positioned even higher, with the hand's grip adjusted accordingly to support the vegetable's weight from beneath. The fingers are curled more prominently around its body, indicating a firmer grasp as if preparing to place it down or to use it. The lighting reveals more of the squash’s textural details, highlighting its freshness and the care with which it is being handled to avoid any damage.

#### Sample 209 — After

- Similarity: 0.4972
- Prediction: In this frame, the pan has a more streamlined appearance, indicating that it has been fully cooked. The pan's surface appears to have been partially covered with oil, suggesting that the oil has been removed from the pan. The edges of the pan seem to be slightly charred, possibly due to the frying process.
- Reference: The omelette here presents a mostly solidified texture, with its surface appearing evenly cooked. The coloration is consistently pale yellow, denoting that the raw, brighter yellow sections observed earlier have been thoroughly cooked. Its structure remains flat, occupying the expanse of the pan, but with slightly crisped and elevated edges, indicating that it may soon be ready for the final stages of preparation, like adding fillings or serving.

#### Sample 211 — After

- Similarity: 0.4585
- Prediction: In this frame, the water is now more concentrated, indicating that the cloth has been washed away. The cloth's surface appears to be damp, suggesting that the water has been drained out of the cloth. The water's color has shifted to a more neutral hue, suggesting a gradual wringing of the fabric, possibly a sign of a rinsing process.
- Reference: In this view, the sink appears to be in the final stages of being wiped down. The person's clasped hands convey a sense of completion or a pause in the activity. The stainless steel surface of the sink is now visibly wetter than in the previous frames, with water covering a greater area of the basin and reflecting light, suggesting a more thorough cleaning has taken place. The counter has been cleared of the carrot peel seen earlier, and the rag previously held in the person's hand is no longer visible, possibly set aside after finishing the wiping.

#### Sample 212 — After

- Similarity: 0.4686
- Prediction: In this frame, the person's hand is positioned at the edge of the kitchen counter, indicating that the door is closed. The hand's angle is slightly different from that of the previous frame, suggesting that the hand is still in the position of the door handle. The object's focus is now on the kitchen area, which is more likely to be a kitchen item, such as a pot or pan.
- Reference: The final image returns to a clearer state similar to the first, with the user's hand retracting from the oven controls. The timer display is again visible, showing a different set of digits, which implies that the user has successfully input or adjusted the time. The blue backlight of the timer is consistent across all frames, providing a visual continuity. The kitchen setting remains unchanged, with the focus solely on the user's interaction with the oven timer.

#### Sample 215 — After

- Similarity: 0.3299
- Prediction: In this frame, the fish's skin appears to have been partially removed, indicating that the fish has been thoroughly rinsed. The hands are now more engaged in the process of peeling the fish, which is likely a sign of the final stages of the process. The skin's surface is more exposed, suggesting that there may be more work to be done on the fish.
- Reference: In this frame, the chicken thigh has undergone a significant transformation. The flesh has been largely pulled apart, revealing the more fibrous strands of the meat. There is a noticeable difference in the thigh's volume as it has spread out across the hands, indicating the progression of the shredding. The meat's color remains consistent, but the texture is now varied, with some pieces appearing more stringy and others still clinging together in larger chunks.

#### Sample 216 — After

- Similarity: 0.4458
- Prediction: In this frame, the kettle has been placed in a new position, with the lid still attached to the top of the pot. The person's hand appears to be holding the kettle, indicating that it is ready to be used. The water level remains the same, suggesting that the kettle is still in its current position.
- Reference: In this frame, the coffee still presents an undisturbed surface, and the cup remains in the same position on the mat, but there is a subtle change in the lighting reflected off the coffee’s surface. The light seems to have shifted slightly, indicating either a minor change in the environment or the passage of time. However, the absence of any ripples or marks on the surface of the espresso suggests that it has not been moved or sipped, preserving the integrity of its initial state post-brew.

#### Sample 222 — After

- Similarity: 0.4044
- Prediction: In this frame, the rag is now more firmly held, indicating that it has been fully soaked. The rag's surface appears to have been partially soaked, suggesting that the water has been drained out of the cloth. The cloth's texture appears to be more abrasive than the previous frames, suggesting a more gradual process of rinsing.
- Reference: The sponge is now at rest on the wooden surface next to the sink, free from any external pressure. It retains a slightly compressed form, likely due to its recent manipulation and not yet having fully rebounded to its original shape. The absence of any water being expelled or dripping suggests it has been sufficiently wrung out. Its dampness is implied by the slight glisten on its surface and the few water droplets scattered nearby.

#### Sample 223 — After

- Similarity: 0.3715
- Prediction: In this frame, the lid has been removed from the container, indicating that the contents of the container have been removed. The hand is now able to grasp the inside of the lid, allowing the contents to fall into the container's opening. The lid's surface appears to have been partially removed, suggesting that there may be a gap between the lid and the container.
- Reference: The can is now more extensively opened. A greater portion of the aluminum lid has been pulled back, revealing the moist, chunky content of the tuna inside. The texture of the tuna is uneven, suggesting it may be in chunks or flakes. One can deduce from the partial view that it's possibly preserved in some form of liquid, possibly oil or brine, as it glistens slightly.

#### Sample 225 — After

- Similarity: 0.3642
- Prediction: In this frame, the blender's lid has been removed from the bowl, indicating that it has been fully cooled. The user's hand appears to be engaged in a reversing action, implying that the blender has been cooled to a more stable state. The focus is now on the blending process, which is likely to take longer than usual, with the user still holding the lid on the blender.
- Reference: The mixture has reached a homogenously creamy state with a uniform yellow coloration and a smooth, glossy finish, consistent with a well-blended batter. The surface is free of any lumps or unincorporated patches, and the mixture now holds a ribbon-like trail from the beaters, which indicates good viscosity and structure. The overall volume appears to have increased, and the mixture maintains its shape around the beaters, demonstrating that sufficient air has been incorporated to give it a light, airy texture.

#### Sample 226 — After

- Similarity: 0.4599
- Prediction: In this frame, the bread has been partially removed from the oven, indicating that it has been completely removed. The bread is now in a more open state, with the bread's surface exposed. The hands are now more engaged in the process of removing the bread, implying that the bread is being partially removed.
- Reference: The scissors are now absent, and the wrap has been cut, with the roll repositioned closer to the center of the counter. The cut edge of the wrap is not visible, suggesting that it has been neatly trimmed and possibly adhered to a dish or discarded. The layout of the kitchen counter shows a shift in focus towards other cooking activities, such as the microwave oven now entering the frame, hinting at the next steps in meal preparation. The wrap's previous tension is gone, indicating the cutting action is complete.

#### Sample 229 — After

- Similarity: 0.4791
- Prediction: In this frame, the ingredients are more evenly distributed, indicating that the ingredients have been thoroughly stirred. The texture of the vegetables appears to be more consistent, suggesting that they've been incorporated into the cooking process. The consistency of the ingredients is more uniform, suggesting a smoother texture.
- Reference: In this instance, the curry is being actively stirred, with a hand in motion, suggesting the cook's engagement in ensuring even cooking. The stirring action creates waves and folds within the curry, bringing different ingredients to the surface. Flecks of spices, possibly cumin or coriander, are visible, hinting at the complex flavor profile being cultivated within the pan. The steam rising from the pan suggests a maintained cooking temperature conducive to flavor development.

#### Sample 231 — After

- Similarity: 0.3056
- Prediction: In this frame, the onion has been removed from the kitchen counter, indicating that it has been partially removed. The person's hand is now in the position of removing the onion, implying that the onion is now partially removed from its container. The onion's surface is more exposed, suggesting that it may be partially removed, or that the individual's fingers are now able to grasp the onion.
- Reference: The plastic bag's opening is now wider, with the fingers having stretched the opening further apart. The plastic material gathers and wrinkles more prominently at the points of tension near the fingers, showing increased manipulation. The potatoes inside the bag are more visible, and the bag’s form has changed from a sealed state to an open vessel, with the top part folded outward, revealing more of its contents. The plastic's texture appears softer and more pliable due to the opening action.

#### Sample 232 — After

- Similarity: 0.4873
- Prediction: In this frame, the blender's lid has been removed from the bowl, indicating that it has been fully incorporated into the bowl. The hand's position is more relaxed, suggesting that the blender is now in the process of blending the ingredients together. The lid's surface appears to have been partially absorbed by the blender, which is likely a sign that the lid is still in place.
- Reference: Here, the mixture displays more surface movement, evidenced by the ripples and peaks forming around the edges of the depression left by the mixer, signifying that the blending process is actively aerating the mixture. This active blending introduces air bubbles, which are crucial for creating a light and fluffy final product. The ingredient's color remains consistent, indicating a homogeneous mix without any color streaking or separation.

#### Sample 233 — After

- Similarity: 0.3407
- Prediction: In this frame, the towel is now in a more streamlined position, with a slightly more rounded shape. The hand's movements are more deliberate, indicating that the towel has been placed in the correct position. The surface of the towel appears to have been wiped down, with the towel's surface still damp and damp. The person's posture is more relaxed, with her hands resting on the towel, demonstrating a relaxed posture.
- Reference: The plate has been placed down on the table, as evidenced by the absence of the person's hand and the stable, clear image of the plate. It rests solidly on the table, slightly overlapping the edge of the tablecloth, which is now neatly laid out without distortions. The plate's empty surface is fully visible, and it now resides next to a white tray with two pieces of food, which could suggest the person has finished serving or is about to serve themselves.

#### Sample 234 — After

- Similarity: 0.3147
- Prediction: In this frame, the person's hand is positioned on the edge of the kitchen counter, indicating that the oven has been closed. The hand is now in a more relaxed position, suggesting that the kitchen is still open. The shadow of the oven's surface is more apparent, implying that there is still a gap between the oven and the counter.
- Reference: The transformation of the mat is nearly complete. It presents itself with a sharp fold down the middle, the two halves nearly symmetrical, a sign of a deliberate and practiced movement. The orange tone of the mat now seems richer, the texture more evident as the lighting casts shadows within the folds, providing depth to the previously flat object. The mat's new shape is compact, hinting at the finality of the action, with just a corner lifted, poised for the last step in its folding sequence.

#### Sample 235 — After

- Similarity: 0.3600
- Prediction: In this frame, a hand is positioned on top of the stovetop, indicating that it has been removed from the burner. The stovetop remains in the same position as the previous frame, suggesting that the burner has been moved away from its original position. The kitchen appears to be in a state of flux, with only a few items still visible, such as a pot or pan.
- Reference: Here, the grater has been repositioned further to the right, and its orientation has changed such that the top, where the handle is affixed, is now closest to the camera. The grater's shredding surface is now partly obscured by the handle from this angle, and the background clutter seems unchanged. This shift in position makes the grater more prominent in the frame and suggests an active engagement with it, possibly in preparation for use.

#### Sample 237 — After

- Similarity: 0.4524
- Prediction: In this frame, the fish has been fully cooked, with the skin still moistened and charred. The person's hand is now more likely to be removing the skin, indicating that the fish is ready to be removed. The fish's surface appears to be more exposed to the light, suggesting that the cooking process is complete. The chef's hands are now more engaged in the process of peeling the fish.
- Reference: The salmon is now almost entirely submerged, with only a small portion of its tail visible above the water. Bubbles rise around it, indicating the rapid descent and the displacement of water. The surrounding water appears disturbed, and the once shimmering scales are now masked by the water's overbearing presence.

#### Sample 238 — After

- Similarity: 0.3142
- Prediction: In this frame, the bottle is now in a more upright position, indicating that it has been fully opened. The person's hand is now more engaged in the process of opening the bottle, implying that the contents of the bottle have been fully incorporated into the container. The bottle's contents are still in the container, with the lid still attached to the bottle.
- Reference: The pouring action has reached its peak, with the flour leaving the jar in a fuller, more rapid stream. The pile of flour in the bowl has risen significantly, nearly doubling in size from the initial pour, and the top of the mound has a smooth, undisturbed surface. The cloud of flour dust has dissipated slightly, suggesting a slowing of the pouring action. There's a slight over-pour on the rim of the bowl, indicative of the speed and volume of the flour being transferred.

#### Sample 240 — After

- Similarity: 0.4532
- Prediction: In this frame, the pot appears to be fully cooked, indicating that the heat has reached a simmering state. The pan's surface appears to have cooled slightly, suggesting that the cooking process has started to take a turn. The surface of the pot seems to be a bit hot, possibly due to the presence of a large amount of water in the pan, which could indicate that the water has cooled sufficiently to allow the pot to continue cooking.
- Reference: Here, the curry is visibly denser and has attained a thicker consistency. The ingredients within have softened significantly and have become an integral part of the curry. The simmering process seems to be at a more advanced stage, with the liquid bubbling gently. The overall hue of the curry is darker, and it looks rich and well-cooked, almost nearing its completion.

#### Sample 241 — After

- Similarity: 0.4974
- Prediction: In this frame, the bowl appears to have been removed from the kitchen counter, indicating that it is no longer in use. The bowl's surface appears to be in a state of disrepair, suggesting that the bowl has been placed on the counter or in the kitchen sink. The hand's motion seems to be reversing, with the bowl still pointing toward the counter, possibly indicating a more gradual movement.
- Reference: The ladle has been set down onto the white paper plate, with the bowl of the ladle now resting on the plate's surface. The handle extends towards the top left of the frame, crossing over the edge of the plate. The scene is largely unchanged apart from the ladle's movement; the table still holds the same items, and the glass remains untouched, with the liquid level consistent with the previous frames.

#### Sample 244 — After

- Similarity: 0.4987
- Prediction: In this frame, the utensil is now held in the hands of a person who is rinsing it. The person's hand is still firmly held, indicating that the water has been sucked out of the urn. The water's consistency is uniform, suggesting that there may be a slight movement in the direction of squeezing.
- Reference: The peeler now emerges from the suds, having been subjected to a vigorous cleanse. The hand's movement has shifted, possibly indicating a final rinse or the start of a new scrubbing cycle. The blade and handle of the peeler are clearer to see now, reflecting the overhead lighting, while fewer bubbles cling to its surface, a sign of the rinsing process displacing the soapy residue.

#### Sample 245 — After

- Similarity: 0.4080
- Prediction: In this frame, the ingredients have been placed in a separate bowl, indicating that they are ready to be poured into a bowl. The bowl's contents are now in the center of the bowl, suggesting that the ingredients are in the middle of the mixing process. The spoon's movements indicate that there is still a lot of work to be done, with the bowl still firmly positioned on the counter.
- Reference: Here, the whisking has progressed further. The fork is actively churning through the egg mixture, creating a more homogeneous yellow color as the yolks and whites combine more thoroughly. The motion of the fork is more evident, indicated by the trails and ripples in the mixture. There are fewer clear whites visible, and the yolks are no longer distinct entities, signifying a deliberate and continued mixing effort to achieve a consistent blend for cooking.

#### Sample 248 — After

- Similarity: 0.3141
- Prediction: In this frame, the door has been partially closed, indicating that there is no longer a gap between the door and the wall. The door's surface appears to have been partially sealed, suggesting that there may be a slight movement in the process of closing the door.
- Reference: The light switch now shows one button fully depressed, indicating that the switch has been activated. The lighting condition, however, does not show a noticeable change from the previous frames. This could mean that the light has yet to turn on, the bulb is non-functional, or the change in lighting is too subtle to be captured by the camera. The hand remains in contact with the switch, and the shadow on the wall is consistent with the previous lighting condition.

#### Sample 250 — After

- Similarity: 0.4637
- Prediction: In this frame, the bowl appears to have been sprayed with water, indicating that the water has been drained out of the bowl. The hand's movements seem to be more relaxed, suggesting that the bowl is now being sanitized. The water's surface appears to be drier, suggesting a more thorough cleaning process. The hands' movements are more agitated, implying that there is a greater amount of water in the bowl, which may indicate that the scrubbing process is complete.
- Reference: The strainer is now positioned in a way that we can observe more of its mesh surface. Though still wet, it seems to have fewer water droplets than before, suggesting that the rinsing process is well underway or nearing its completion. The surrounding area and the items next to it, like a black pan, are also wet, suggesting the strainer might have been moved or shaken during the cleaning process.

#### Sample 252 — After

- Similarity: 0.3782
- Prediction: In this frame, the knife's edge has been shaved off, indicating that the knife has been fully engaged in the action. The knife is now positioned in the center of the knife, with the knife resting on the edge of the parchment paper, implying that it has been partially cut off. The hand's position is more relaxed, suggesting a smoother surface to be used to cut the knife.
- Reference: Here, the cake's integrity is further reduced by the removal of an additional slice. This action has created a larger gap in the ring, with two segments now missing. The texture of the cake is consistent with the previous images, and it continues to sit on the same decorative doily. The absence of the slices highlights the consistent golden-brown color of the cake's crust and the moistness of the interior, as inferred from the newly exposed edges.

#### Sample 253 — After

- Similarity: 0.4334
- Prediction: In this frame, the sponge appears to be fully absorbed by the water, indicating that it has been fully drained. The surface of the sponge is more exposed, suggesting that the water has been sucked away from the sponge's surface. The hand's movements indicate that the sponge has been thoroughly soaked in the water. The sponge is now more exposed to the water's movement, implying that it may have been partially soaked or washed.
- Reference: The rag here has a slightly different posture, being maneuvered possibly to a different angle or direction. The grip on the rag seems firm, and its dampness is consistent with the previous frames. Some portions of the rag look more pressed down, likely from the cleaning motion and the force applied by the hand.

#### Sample 255 — After

- Similarity: 0.4916
- Prediction: In this frame, the microwave's handle is positioned in a slightly different position from the previous frame, indicating that the hand is now engaged. The hand's angle is slightly different from that of the previous frames, suggesting that the microwave is now in the same position as before. The surrounding environment, including the kitchen, remains unchanged, with the kitchen still cluttered and uncluttered.
- Reference: Here, the hand appears to have finished its action, with the fingers slightly retracting, suggesting that a button or switch has been pressed. The positioning of the hand and fingers denotes a concluding action, hinting that the switch has been engaged or disengaged accordingly. The surroundings remain consistent with previous frames, further emphasizing the primary action involving the switch.

#### Sample 256 — After

- Similarity: 0.4278
- Prediction: In this frame, the stove appears to have been removed from the kitchen, indicating that there is no longer any residue left on the surface of the stovetop. The person's hand is now more focused on the kitchen counter, suggesting that there may have been a change in the position of the burner. The kitchen counter appears to be in a more neutral position, with a slightly different appearance from the previous frame. The countertop appears to look more modern and modern, with the counter's surface reminiscent of a kitchen counter.
- Reference: The progression of interaction is evident as the hand has now grasped the grill grate, with fingers curled securely around one of the bars. The grate is slightly lifted, suggesting the initial stage of removal. The rest of the grill remains static, its cleanliness and the unaltered positions of the other grates indicating that this is perhaps the first grate being manipulated. The surrounding area, including a countertop and various kitchen items, remains undisturbed by the action taking place.

#### Sample 261 — After

- Similarity: 0.3561
- Prediction: In this frame, the tomato has been placed on a cutting board, indicating that it has been sliced. The hands are now more involved in the process of slicing, implying that there is a slight movement in the direction of the cutting. The tomato's surface appears to have been partially cut off, suggesting that there may have been a splintered portion of the tomato.
- Reference: By this point, the chilli's dispersion looks even more uniform, suggesting the individual making the pizza has made further adjustments. The slices seem to have settled onto the toppings, resting comfortably among the corn, onions, and other ingredients. The moisture or slight sheen on some of the chilli slices implies they are fresh, holding onto their natural juices.

#### Sample 262 — After

- Similarity: 0.4613
- Prediction: In this frame, the slicing board has been rearranged, indicating that the knife has been removed from the cutting board. The knife's blade is now positioned in the middle of the board, with the knife pointing downwards. The board's surface appears to have been partially trimmed, suggesting that there may be more work to be done on the board.
- Reference: In this frame, the quantity of chopped spring onion has increased notably, filling a larger area of the blue chopping board. The cuts are still even, indicating a steady hand and deliberate technique. The previously unchopped portion of the spring onion is now significantly reduced, with only a small section left to be diced. The clear commitment to uniformity in the chopping process is evident in the pile's consistency.

#### Sample 267 — After

- Similarity: 0.3610
- Prediction: In this frame, the onion has been partially removed from the cutting board, indicating that it is now partially thawed. The knife's grip remains firm, suggesting that the knife is now firmly engaged in the process of cutting the onion. The onion's skin appears to have been partially cut off, with the knife still firmly gripped by the onion, implying that the onion is now fully sliced.
- Reference: Progress in the sweetcorn's reveal is evident as the can opener has now traversed a significant portion of the can's circumference. The lid is partially detached, with a noticeable gap indicating the path the opener has taken. Corn kernels are now visible, peeking through this gap, their yellow hue contrasting with the metallic sheen of the can's interior. The user's hands are actively engaged in the process, suggesting that the opening sequence is close to completion, and the sweetcorn will soon be fully accessible.

#### Sample 270 — After

- Similarity: 0.4348
- Prediction: In this frame, the onion has been sliced into smaller pieces, indicating that it has been partially slicked. The knife's blade is now positioned in the middle of the onion, allowing the knife to slice through the onion more easily. The onion's skin appears to have been partially cut off, suggesting that the knife has been used to cut the onion in a more precise fashion.
- Reference: Here, the cutting action has been completed, and the broccoli has been divided into smaller segments. The hand is shown in a relaxed state, no longer holding the knife, which suggests the cutting task is done. Several individual florets have been separated from the main stalk and are spread out on the cutting board, some of which have small pieces of the stem attached. The remaining main stem of the broccoli is now clearly visible with a freshly cut cross-section.

#### Sample 271 — After

- Similarity: 0.4938
- Prediction: In this frame, the bowl has been placed in a new position, with the handle positioned slightly away from the sink, indicating that the bowl is still in its current position. The bowl's surface appears to have been wiped down, suggesting that it has been re-used. The hand's movements suggest that there may be a change in the position of the bowl, which is likely a result of the cleaning process.
- Reference: The action of squeezing has resulted in a substantial amount of washing up liquid pooled at the base of the bowl, with the stream now thicker and more copious. The surface of the liquid pool is uneven, with ripples and bubbles indicating recent disturbance. Some liquid has started to spread out from the initial point of contact, with tendrils of green stretching outwards, showing the beginning stages of dispersion through the water present in the bowl.

#### Sample 278 — After

- Similarity: 0.3500
- Prediction: In this frame, the dough has been kneaded into a more uniform shape, indicating that it has been fully rolled. The hand's movements have been more deliberate, implying that the dough is now being rolled in a circular motion. The dough's surface appears to have been partially rolled, suggesting that the rolling motion has been completed.
- Reference: The majority of the cling film remains held aloft, displaying even more of its surface area. The presence of more pronounced wrinkles and slight deformations is evident due to the manual handling. It seems the film has yet to be fully detached from its package, and the individual's hands actively engage with it, ensuring its spread and position.

#### Sample 279 — After

- Similarity: 0.4614
- Prediction: In this frame, the microwave has been removed from the kitchen, indicating that it is no longer in use. The person's hand is still motionless, suggesting that there is no movement in the kitchen. The kitchen's lighting is still dim, with only a few lights visible in the background. The camera's focus is now on the microwave's interior, with the kitchen setting still visible.
- Reference: The cabinet door is now almost completely closed, with only a small gap remaining. The motion blur has decreased, implying that the speed of the closing action has reduced as the door nears its fully closed position. The contents of the cabinet are no longer visible due to the narrow opening, and the door is nearly flush with the cabinet frame, indicating that the action of closing the cabinet is almost complete.

#### Sample 280 — After

- Similarity: 0.3349
- Prediction: In this frame, the table is now positioned in a more streamlined position, with a slightly more rounded appearance. The surface of the table appears to have been partially removed, indicating that the table has been placed in the correct position. The table's surface appears to be slightly soiled, suggesting that it may have been wiped with soap or water.
- Reference: The scene remains a whirl of colors and shapes due to motion blur, with the toaster even less discernible than before. It's apparent that the camera or the person is moving quickly, creating an almost abstract composition of kitchen elements. The blur conveys a sense of urgency or haste. The toaster, while present in the scene, has become an element of the background, overshadowed by the blur of motion that dominates the frame.

#### Sample 281 — After

- Similarity: 0.4686
- Prediction: In this frame, the surface of the table is now more cluttered, with a smoky appearance. The hand's movements are more deliberate, indicating that there is more work to be done on the table. The table's surface appears to have been thoroughly cleaned, with no visible streaks or blemishes, suggesting a thorough cleaning.
- Reference: The movement continues with the hand vigorously wiping the surface, leaving a trail of cleaner in its wake. The cloth appears more saturated with detergent, as evidenced by the more uniform sheen on the surface and the fewer visible streaks. The hand's motion has become more pronounced, with the cloth now occupying a different position, indicating a continuous, circular wiping pattern intended to cover and clean the surface thoroughly.

#### Sample 284 — After

- Similarity: 0.4182
- Prediction: In this frame, the pan has been flipped over, indicating that the ingredients have been added to the pan. The pan's surface appears to be slightly tilted, suggesting that there is a slight movement in the cooking process. The bottom of the pan appears to have been partially removed from the pan, implying that the pan is now partially covered with the ingredients.
- Reference: The pasta has reached a state where it looks thoroughly combined with the pesto sauce. Each rotini curl is drenched in the vibrant green sauce, reflecting a creamy and appetizing appearance. The consistency looks rich, suggesting that the ingredients have melded well. The wooden spoon appears to be scooping up a portion, possibly checking the texture or taste.

#### Sample 294 — After

- Similarity: 0.4466
- Prediction: In this frame, the pan's surface appears to have been thoroughly cleaned, indicating that it has been thoroughly rinsed. The person's hand seems to be focusing more on the surface of the pan, which is likely a sign of a more thorough cleaning process. The water level in the pan appears to be lower, suggesting that there may be a significant amount of water being sucked into the pan.
- Reference: The towel re-emerges, this time being used more deliberately. It is held in one hand, fingers extended, applying a degree of pressure against one of the stove burners, indicating a scrubbing or wiping motion. The fabric appears to be slightly more soiled than before, consistent with its use in cleaning a cooking area. The spread of the fingers and the position of the towel suggest a more focused cleaning effort is being made, possibly after a preliminary cleaning or assessment of the area's condition.

#### Sample 295 — After

- Similarity: 0.4806
- Prediction: In this frame, the utensil has been placed in a bowl with a clean surface, indicating that the water has been drained. The hand is now positioned in the middle of the bowl to ensure that there is no residue left on the surface. The soapy water is displeasing the bowl, which is likely a sign of a more thorough cleaning.
- Reference: The cleaning process seems to have progressed, as the strainer is now being wiped from the inside out with a white cloth that is likely absorbing moisture and dislodging any remaining particles. The sponge has been set aside, indicating that the scrubbing action has been completed. The water flow has resumed, suggesting a final rinse. The interior of the strainer looks significantly cleaner, with fewer visible food particles, and the white plastic appears to have regained some of its original brightness.

#### Sample 297 — After

- Similarity: 0.4426
- Prediction: In this frame, the chicken is now in a more or less complete state of cooking. The skin has been partially removed from the chicken, indicating that it has been fully cooked. The knife's focus is now on the meat, with the fingers pointing towards the meat. The chicken's skin is now more exposed to the light, suggesting that it may be ready for cooking.
- Reference: The board is now tilted at a steeper angle towards the pan, and the garlic paste has been mostly scraped off, leaving only a slight residue on the surface. The person's grip on the knife has changed to a more precise and firm hold, focusing on ensuring that all of the garlic is removed from the board. The hand holding the board has adjusted its position to facilitate the transfer of the garlic into the pan, and the fingers are curled to avoid contact with the knife or the hot surface of the pan.

#### Sample 298 — After

- Similarity: 0.3598
- Prediction: In this frame, the sink has been removed, indicating that the water has been drained out of the sink. The water's surface appears to be soiled, suggesting that the sink is now able to drain the excess water. The hand's movements indicate that there is still a lot of water in the sink, which may indicate that the tap is still running. The sink's current position indicates that there may be a significant amount of water on the sink surface, possibly indicating a dripping of water.
- Reference: The gloves in this frame are presented in a state of action. The left hand, clad in the yellow rubber glove, is actively engaged in holding a dark frying pan, while the right hand appears to be reaching towards or withdrawing from an interaction with the pan or another object just outside the frame. The gloves are more stretched across the palms and fingers compared to the previous frames, indicating a firmer grip and a dynamic movement.

#### Sample 299 — After

- Similarity: 0.4316
- Prediction: In this frame, the pan's surface appears to be a bit darker, suggesting that the cooking process has been a little more active. The cook's hand seems to be holding the pan at a steady pace, indicating that the heat has been exerted on the surface of the pan, which is likely a sign of a more gradual cooking process.
- Reference: The kitchen's perspective has dramatically shifted to showcase other areas, including a countertop with a toaster, a cup, and other miscellaneous items. The stovetop and its controls are no longer the central focus, and there's minimal interaction with the temperature settings. The viewer's attention is directed more towards the broader kitchen environment rather than specific temperature adjustments on the stove.

#### Sample 301 — After

- Similarity: 0.4567
- Prediction: In this frame, the water is now dripping from the faucet, indicating that the water has been fully drained. The hand's movements are more relaxed, with the water's sprinkling on the surface of the faucet's surface, suggesting a more gradual rinsing of the water. The hands' posture is more relaxed and relaxed, implying that they are now able to hold the water in their hands. The water level appears to be increasing, suggesting that there may be a slight increase in the amount of water that has been dripped onto the surface.
- Reference: The peeler, now held in the person's right hand, is positioned vertically with the blade section pointing upwards. This orientation allows any residual water to drip off from the peeler, ensuring it is free of moisture post-rinsing. The green grip is vividly visible, and the entire peeler looks relatively clean and well-maintained, prepared for its next use or storage.

#### Sample 303 — After

- Similarity: 0.4823
- Prediction: In this frame, the bottle is now in a more upright position, indicating that the cap has been removed from the bottle. The hand's grip remains steady, suggesting that the bottle has been placed in the correct position. The bottle's contents remain intact, including the contents of the cap, as well as the cap itself.
- Reference: The scene portrays the can in a more pronounced tilted angle, suggesting an active pour. The fluid is visible midway, cascading into the already partially filled glass. The glass captures the liquid's effervescence, with bubbles hinting at the carbonated nature of the drink. The person's grip has adjusted to facilitate the pour, and the wrist's metallic accessory shines under the ambient light.

#### Sample 304 — After

- Similarity: 0.3330
- Prediction: In this frame, the sink is now in a more natural position, with a sprinkling of water on the surface of the sink. The water's surface appears to have been drained, indicating that the water has been sucked out. The hand's motion seems to be reversing the direction of the action, implying that the sink has been removed from the surface.
- Reference: The transformation of the tin reaches a new phase as it now holds a quantity of water, with its surface partially submerged. The water reflects the kitchen's ambient light and surroundings, introducing a glossy sheen that contrasts sharply with the matte and tarnished finish of the tin's unwetted interior surfaces. The water's presence introduces a visual softening of the tin's hardened deposits, implying a preliminary step in a cleansing process.

#### Sample 306 — After

- Similarity: 0.4139
- Prediction: In this frame, the sponge appears to have been sprayed with water, indicating that it has been thoroughly washed. The sponge's surface appears to be slightly dampened, suggesting that the water has been drained out of the sponge. The person's hand is still holding the sponge, which is likely a sign that the sponge has been rinsed.
- Reference: The rolling pin now rests on the edge of the sink, with attention focused on cleansing a white plate. The pin is no longer the central object of cleaning but remains in the scene, possibly awaiting a final rinse or to dry. The soapy water on the pin has formed small puddles on the stainless steel sink, separating the cleaning zones between the plate and the pin. The pin's handles protrude outward, suggesting that it might be picked up again soon.

#### Sample 308 — After

- Similarity: 0.4237
- Prediction: In this frame, the rinsing device is now in a more natural position, with the water evaporating from the inside of the bowl. The hand's grip is more relaxed, indicating that the water has been drained away from the bowl and into the surrounding area. The water's surface appears to be saturated with water, suggesting that there may be a slight movement in the water flow.
- Reference: The baking tray now lies flat in the sink with a generous amount of foamy soap suds covering its surface. The water is still running, and the person's hands are actively scrubbing the tray, indicating a thorough cleaning process. The soap suds are dense and white, almost completely obscuring the surface of the tray, which suggests that a good amount of dish soap has been used to ensure a thorough cleanse. The tray is almost unrecognizable under the frothy layer, showing a significant transition from the initial state.

#### Sample 309 — After

- Similarity: 0.2773
- Prediction: In this frame, the chicken's skin appears to be fully soaked in water, indicating that it has been thoroughly rinsed. The hands are now more engaged in the process of slicing the chicken, which is likely a step closer to removing the excess water from the chicken. The skin's surface is more exposed to the water, suggesting that the chicken has been partially soaked.
- Reference: The tap continues to be in its downward position over the sink. Water is gushing out from the spout with a higher intensity compared to the previous frame. The flow is forceful, resulting in more water splashes within the sink. The clarity and consistent nature of the water suggest it's likely at a cold temperature.

#### Sample 312 — After

- Similarity: 0.4103
- Prediction: In this frame, the onion has been removed from the cutting board, indicating that it has been partially thawed. The person's hand is now more firmly grasping the onion, which is likely a sign that the vegetable has been thoroughly washed and is ready to be sliced. The onion's skin appears to have been partially removed, suggesting that the knife has been used to cut the onion in a more precise fashion.
- Reference: The process progresses with more green beans being trimmed and added to the collection in the colander. The person's hands are active, with the right hand holding a green bean and the left hand seeming to have just released a trimmed bean into the colander. The contrast between the trimmed beans inside the colander and the untrimmed ones still in their packaging is quite apparent. The trimmed beans have a uniform appearance, with clean cuts at both ends, while the ones awaiting preparation display their natural, uneven tips.

#### Sample 317 — After

- Similarity: 0.3844
- Prediction: In this frame, the bread has been placed on a counter, indicating that it is ready to be sliced. The hands are now more engaged in the process of slicing, implying that the bread is now fully sliced and ready for use. The bread's surface is slightly exposed, suggesting that the hand is now able to grasp the bread, which is likely a key part of the preparation process.
- Reference: The mozzarella now appears more evenly distributed across the dough's surface, although the distribution is not perfectly uniform, suggesting a hand-spread method. There are areas with a denser coverage and some spots that have less, showing a natural variance in the spreading technique. The individual strands of cheese are visible again and remain separate, retaining their structure without clumping or melting. The cheese still holds the pale cream color, and the lighting highlights its soft texture.

#### Sample 319 — After

- Similarity: 0.4227
- Prediction: In this frame, the tomato has been partially sliced, indicating that it has been fully sliced. The hands are now more involved in the process of slicing the tomato, which is likely a step in the right direction. The tomato's surface is slightly exposed, with the skin exposed, suggesting that it may have been partially cut off. The knife's edge is still visible, and there is a slight crease in the center of the tomato.
- Reference: Here, the sandwich appears almost complete. The top slice of bread has been folded over, partially covering the layers of lettuce and ham beneath it. The hand of the sandwich maker is in the process of fine-tuning the assembly, with fingers gently adjusting the fillings to ensure an even distribution. The area around the sandwich seems undisturbed from the previous state, with the open container of lettuce and unused slices of cheese suggesting that no further ingredients will be added to this particular sandwich.

#### Sample 320 — After

- Similarity: 0.4011
- Prediction: In this frame, the chicken has been partially removed from the pan, indicating that it is now in the hands of the person who is preparing the dish. The chicken's skin is now more exposed to the knife's action, implying that the hand is now engaged in the process of removing the chicken. The hand's position is more relaxed, suggesting that the chicken is now ready for cooking.
- Reference: The sweet potato skin here is mostly separated, with only a small portion still attached at the end of the vegetable. The accumulation of peelings on the cutting board has grown, and some peel segments have escaped onto the counter, showing the progression of the peeling task. The skin's moisture has begun to dull as exposure to the air has set in, and there is a noticeable decrease in the vibrancy of the orange color. The knife and fork are now lying on the cutting board, indicating a pause or the completion of peeling.

#### Sample 327 — After

- Similarity: 0.4722
- Prediction: In this frame, the lid has been removed from the sink, indicating that it is no longer in use. The person's hand appears to be holding the lid, which is likely a sign that the lid is being removed. The object's shape is more apparent in this frame than in the previous frames, suggesting that it may have been partially removed.
- Reference: In this frame, the lunch box is in the midst of a dynamic moment, positioned at an angle that suggests it is being actively tipped over. Human hands are visible, gently guiding the box, which remains closed. The box now shows signs of contact, with a human element introduced into the scene, adding a sense of intentionality to the action. The environment remains consistent with the domestic kitchen setting, and the presence of the individual implies a deliberate interaction with the lunch box.

#### Sample 328 — After

- Similarity: 0.4272
- Prediction: In this frame, the lid has been removed from the bag, indicating that the contents of the bag have been removed. The person's hand is now in the position of removing the bag's contents, implying that the bag has been partially removed.
- Reference: The bread is now fully inside the toaster, no longer visible, indicating the toasting process is underway. The hand that was previously holding the bread is now absent from the frame, suggesting the person has completed the action of inserting the bread into the toaster. With the bread out of sight, the toaster becomes the new focal point, its design and the red indicator light suggesting it is working to crisp the bread slice within.

#### Sample 329 — After

- Similarity: 0.4110
- Prediction: In this frame, the lid of the coffee pot has been removed from the pot, indicating that the lid has been completely removed. The hand is now in the position of removing the lid, implying that the cap has been placed on the pot. The lid's position remains unchanged, suggesting that the cup has been partially removed from its container. The liquid content of the pot remains the same as in the previous frames.
- Reference: The bag is significantly more open in this frame, with a substantial portion of its contents now visible. The hand is holding onto the bread, indicating an intention to possibly take it out or examine it. The surrounding items remain in place, emphasizing the main action taking place with the bag and its contents. The transparency of the bag offers a clear view of the bread inside, revealing its shape, size, and texture.

#### Sample 332 — After

- Similarity: 0.3632
- Prediction: In this frame, the person's hand is more firmly grasping the oven door, indicating that the oven has been closed. The door's surface appears to be partially open, suggesting that the person is now able to open the door. The interior of the oven appears to have been partially closed, with the oven's interior still visible.
- Reference: The drawer now appears fully closed, with no visible gap, indicating the completion of the action. The blur has diminished, suggesting that the motion has halted, and the freezer is sealed. The surface of the drawer is smooth, and there are no signs of obstruction, indicating a successful closure. The freezer is now likely returning to its optimal temperature to preserve the contents inside.

#### Sample 334 — After

- Similarity: 0.4566
- Prediction: In this frame, the paperclip has been removed from the bag, revealing a more streamlined appearance. The paperclip is now firmly held in place by the hand, indicating that it has been partially removed. The hand's movement is evident, implying that the knife is engaged in a deliberate action to remove the plastic wrap.
- Reference: The application of the creamy substance seems to have been completed. The knife, now carrying minimal residue, is pulled away from the bread, which is held steady in the other hand. The spread is more uniform across the bread's surface, though some natural undulation in its thickness remains. The crust edge of the bread appears unblemished by the spread, preserving its crisp texture. The hand holding the bread is poised as if preparing to place the bread down or to bring a second slice to complete the sandwich.

#### Sample 335 — After

- Similarity: 0.3253
- Prediction: In this frame, the mat is now more firmly held, indicating that it has been placed in a position where it can be easily removed. The hands are now more engaged in the action, suggesting that the mat has been taken apart. The surface of the mat appears to have been wiped down with a cloth or paper towel, implying that there is still a lot of dust on the surface.
- Reference: In this frame, the degreaser's presence is evidenced by a layer of liquid across the surface, with a significant reduction in airborne droplets. The hand and bottle are now absent, indicating that the spraying action has ceased. The surface of the countertop shows a consistent wet sheen, highlighting the even distribution of the degreaser. The wet area has expanded further, showing the progression of the liquid as it moves outward from the point of initial contact. The pattern of the countertop is slightly obscured by the sheen of the degreaser, displaying the product's coverage.

#### Sample 337 — After

- Similarity: 0.4523
- Prediction: In this frame, the spoon appears to have been removed from the kitchen counter, indicating that it is now in the hands of the person who is preparing the meal. The spoon's position remains unchanged, suggesting that the hand is now engaged in a more deliberate action, such as removing the spoon from the table or placing it on the counter.
- Reference: The cutting board now rests in a new position, having been moved significantly from its original placement. It is now more centered on the wooden countertop, which aligns with a typical preparatory position for chopping or assembling ingredients. The green specks are less scattered than before, possibly due to the board's movement consolidating them. The hand's relaxed posture suggests the action of moving the board has been completed, and the scene is poised for the next step in food preparation.

#### Sample 338 — After

- Similarity: 0.2659
- Prediction: In this frame, the pan is now positioned in a more streamlined position, indicating that the pan has been fully cooked. The pan's surface appears to be slightly tilted, suggesting that the heat has reached a low level, implying that the cooking process has been completed. The surface of the pan seems to be a little more exposed, suggesting the pan may have been a bit too hot for the pan to handle.
- Reference: The extractor fan remains in the same state as before, maintaining its heavily used appearance with a stubborn layer of grime. The lack of light reflection on its surface reinforces the idea that the fan is not operational, and there seems to be a consistent lack of maintenance, which is evidenced by the undisturbed grease deposits. The fan's surroundings, including the wall tiles and the stovetop, also show signs of use, correlating with the condition of the fan, suggesting a kitchen that is frequently used but not frequently cleaned.

#### Sample 341 — After

- Similarity: 0.4549
- Prediction: In this frame, the utensil has been placed in a position that allows the water to drain away from the surface. The hand's grip is more relaxed, indicating that the water has been drained. The water's movement is more pronounced, suggesting that there may be a pause in the process of rinsing.
- Reference: The tablecloth is now draped over the sink's divider, its apple design partially obscured by the curvature of the fabric as it conforms to the sink's shape. Water droplets are scattered across the surface, some merging to create larger rivulets that travel along the cloth's folds and undulations. The image conveys a sense of motion and fluidity, with the previous crispness of the apple design softened by the water's influence.

#### Sample 347 — After

- Similarity: 0.4576
- Prediction: In this frame, the towel has been placed in a position where it has been hand-held, indicating that it is now in the hands of the person who is holding it. The person's hand appears to be holding the towel, implying that the towel is now being held by someone. The towel's surface is slightly more exposed, suggesting that it may have been partially wiped or washed with soap and water.
- Reference: In this frame, the tea towel is almost entirely folded, with just a small section still being adjusted by a hand. The striped pattern is now displayed in layered bands, with the colors stacking upon each other due to the folding process. The overall shape of the towel has become more compact, representing a neatly arranged rectangle, while still retaining its smooth texture.

#### Sample 348 — After

- Similarity: 0.4418
- Prediction: In this frame, the person's hand is positioned in front of the refrigerator door, revealing the contents of the freezer compartment. The door's contents are still visible, including the refrigerator's lid, which has been partially opened. The refrigerator door is now closed, indicating that there is no longer enough room for the refrigerator to be open.
- Reference: The hand in this image is in clear focus, reaching towards the spice jars with intent, specifically aiming for one of the jars on the shelf. The cabinet contents are now visible, with labels facing outward, showing a mix of perhaps ground spices or dried herbs. The environment remains consistent with the previous frames, indicating a sequence of actions in the same setting.

#### Sample 351 — After

- Similarity: 0.3845
- Prediction: In this frame, the plastic bag has been removed from the kitchen counter, indicating that it is now in the hands of a person who is preparing to prepare food. The person's hand is still firmly grasping the bag, implying that the bag is now partially removed. The bag's contents are still visible, including the contents of the bag and its contents, as well as the bag itself.
- Reference: In this frame, the action of capping the olive oil bottle has progressed further. The cap is now partially obscured by the hand, suggesting that it has been placed over the bottle's opening and is likely in contact with the bottle's rim. The person's hand is stretched towards the bottle, which remains out of view, and the downward pressure indicates that the cap is being twisted to secure it in place. The cap appears slightly tilted, a common occurrence when initiating the twisting motion to seal a screw-top bottle.

#### Sample 353 — After

- Similarity: 0.3080
- Prediction: In this frame, the lid of the coffee pot has been removed from the machine, indicating that it is no longer in use. The user's hand is now able to grasp the lid, which is likely a sign that the lid has been reattached.
- Reference: The button now appears to be fully engaged, pressed down to its furthest extent. The change in elevation from its original position is apparent, with the finger firmly applying pressure. The shadow cast by the finger is now more pronounced and confined to a smaller area directly around the point of contact, indicating that the button is at its lowest position. The surface of the button that was once reflective is now mostly obscured by the finger, and the surrounding buttons remain static, undisturbed by the action of this single button being pressed.

#### Sample 356 — After

- Similarity: 0.4270
- Prediction: In this frame, the pot appears to have been removed from the burner, indicating that it is no longer in use. The pan's surface appears to be in a state of disrepair, suggesting that the burner has been removed, possibly due to a sudden change in the position of the burner.
- Reference: At this point, the mixture shows further signs of cooking, with even less liquid visible. The green components now appear more thoroughly cooked, with a subdued green color and more pronounced softness. The reduced liquid has a glossier look, indicating that the flavors are concentrating and the oil is emulsifying with the water content to create a more cohesive sauce. The edges of the pan show small bits of the mixture, which could suggest some caramelization or simply remnants from stirring. The wooden spoon is now resting, which might indicate a momentary pause in stirring, perhaps to evaluate the state of the mixture.

#### Sample 358 — After

- Similarity: 0.4985
- Prediction: In this frame, the frying pan appears to have been removed from the burner, indicating that it is no longer in use. The hand's motion seems to be reversing the position of the pan's blades, suggesting that they may have been wiped with a damp cloth or paper towel.
- Reference: The hob's surface gleams, with no evidence of food spills or stains, reflecting meticulous maintenance. The grilles covering the burners appear untouched, with no discoloration from heat or cooking. The knobs on the control panel are pristine, with the blue indicators sharply pointing towards the off position. The cleaning cloth has moved slightly, now positioned over one of the burners, with the hand in the same watch-wearing position, suggesting a continuous cleaning motion.

#### Sample 359 — After

- Similarity: 0.3992
- Prediction: In this frame, the rag is now more firmly held, indicating that the water has been drained out of the cloth. The rag's surface appears to be damp, suggesting that it has been washed away. The water's color has shifted to a more neutral hue, suggesting a gradual process of rinsing. The cloth's texture has improved, with a softer feel to it.
- Reference: In this frame, the bin remains in the same location, but the person's hand is now retracting from the area, implying that an item may have been deposited into it. The fill level of the bin appears consistent with the previous images, maintaining its overfilled state. The plastic liner bulges slightly outward, a sign of the bin's capacity being maximized. The environment around the bin, particularly the dish rack and the countertop, shows no noticeable change, reinforcing the ongoing use of the space for kitchen activities.

#### Sample 362 — After

- Similarity: 0.3942
- Prediction: In this frame, the water has been drained out of the cloth, indicating that it has been thoroughly washed away. The cloth's surface appears to have been soaked in water, suggesting that the water is now able to drain through the cloth. The water's color has shifted to a more neutral hue, implying that the cloth has been partially soaked.
- Reference: The tap now shows a significant alteration in the flow of water, which is reduced to a trickle, signifying the nearing of the cessation of the flow. The hands have engaged with the tap, likely manipulating the handle to adjust the water's volume. The diminished stream suggests a gentle arching trajectory as gravity pulls the water down. This minimal flow creates a less vigorous impact on the sink's surface, resulting in fewer splashes.

#### Sample 363 — After

- Similarity: 0.4249
- Prediction: In this frame, the kitchen sink appears to have been removed from the cabinet, indicating that it has been reattached. The kitchen's interior is now more cluttered, with fewer items on the counter and less space in the cabinet. The overall appearance of the kitchen appears to be more modern and contemporary, contrasting with the rest of the cabinet's appearance.
- Reference: The perspective is similar to the second frame, with the locker still open and the contents unchanged. The blurriness continues, indicating ongoing motion, either of the locker door or the camera. Kitchenware is partially visible on the top shelf, and the door's position seems consistent with the previous frames, suggesting that it has been open throughout and that no significant interaction with the locker has occurred between the frames.

#### Sample 364 — After

- Similarity: 0.2029
- Prediction: In this frame, the hand is positioned on top of the kitchen counter, indicating that it has been placed in a position where it is likely to be used as a cooking tool. The hand's focus is now on the kitchen, with the kitchen still visible. The kitchen appears to be preparing for a meal or other meal, and there is a slight movement in the kitchen.
- Reference: Now, the sweet potato takes on a distinctly different form. It appears to be cooked or baked, with its exterior taking on a wrinkled, slightly crispy texture. The rich orange hue of its interior has deepened, becoming more caramelized and glossy. Steam rises gently from the potato, indicating its warmth, and the flesh seems to have softened further, suggesting it would easily yield to the slightest pressure from a fork.

#### Sample 365 — After

- Similarity: 0.1817
- Prediction: In this frame, the stove is now positioned in the center of the room, with the blades pointing downwards. The person's hand is now more focused on the surface of the stove, indicating that there is a greater focus on the cooking process. The kitchen appears to be preparing for a meal, with a focus on preparing the food for the next stage of cooking.
- Reference: The hob surface now appears much cleaner than in the previous frames. The creamy substance is noticeably diminished, and while there's still some sheen indicative of moisture, it's less pronounced. The cleaning action with the blue cloth seems to have been effective in removing the majority of the spill or residue. The surrounding area of the hob appears clearer, with fewer obstructions, hinting that the cleaning process is nearing completion.

#### Sample 367 — After

- Similarity: 0.4528
- Prediction: In this frame, the spoon is now in a more relaxed position, indicating that the water has been poured into the pot. The spoon's surface appears to be slightly dampened, suggesting that there may be a slight movement in the direction of the pouring process. The water's consistency seems to be more uniform, suggesting a gradual release of the liquid, which is likely due to the presence of a large amount of water in the pan.
- Reference: The cap is more discernible in this frame, offering a clearer view. It's positioned near some jars and containers, with its design and color more evident. The environment's lighting is slightly better, highlighting the cap's features. However, the surrounding objects continue to contribute to a sense of disarray in the frame.

#### Sample 368 — After

- Similarity: 0.3175
- Prediction: In this frame, the person's hand is more firmly grasped, indicating that they are preparing to open the bag. The contents of the bag are now in the hands of the person who opened the bag, which is likely a sign that the bag has been opened.
- Reference: Here, the focus shifts slightly away from the preparation area, providing no direct view of the tomatoes. There's a clear indication that the cooking process is advancing with the presence of a knife and an empty plastic bag labeled with a reference to carrots, suggesting that the ingredients are being organized or prepped sequentially. The absence of the tomato can suggests that its contents have already been utilized in an earlier step, or are set aside, ready for the next stage of meal preparation.

#### Sample 370 — After

- Similarity: 0.3379
- Prediction: In this frame, the towel has been placed on a flat surface, with the handle positioned at the center of the table. The hand is now firmly grasping the towel, indicating that it has been pressed against the table surface. The towel's surface appears to have been partially wiped down, suggesting that the towel is still damp. The hands are still holding the towel in their hands, implying that they are attempting to clean the towel.
- Reference: The roll of paper shows a clear transformation, with the top sheet partially lifted and separated from the main body of the roll. The hand's position has shifted, and the paper now has a curved trajectory, indicating that it has been pulled upward. The paper's surface is more visible, revealing a zigzag pattern that was not apparent before, possibly due to the angle of separation. This frame captures a decisive moment in the tearing process.

#### Sample 371 — After

- Similarity: 0.2979
- Prediction: In this frame, the vegetables appear to be more tender, indicating that they've been partially cooked. The color of the vegetables appears to be slightly darker, suggesting that the cooking process has been a bit more intensive. The pan's heat is now more intense, with the vegetables exhibiting a more pronounced hue of browning.
- Reference: The spatula is now out of the pan, held aloft, indicating the end of a stirring or flipping action. The utensil appears clean, with no visible food residue, which may suggest that the food did not stick to the surface during the stirring, or it could simply be due to the angle and the distance from the camera. The hand grips the handle closer to the body of the spatula, possibly for better control during the lifting motion.

#### Sample 372 — After

- Similarity: 0.3754
- Prediction: In this frame, the person's hand is positioned in a slightly different position, indicating that the door has been closed. The object's focus is now on the door itself, which is more likely to be a hinged door, rather than a closed one. The door's surface appears to have been partially closed, suggesting that the person is attempting to open the door.
- Reference: The basket now is clearly in the grasp of a person who is leaning over it, indicating a deliberate action. The hands are visibly interacting with the contents, which include green and yellow items that could be vegetables, suggesting the basket might be used for storing food. The environment suggests an indoor setting with a rustic appeal, featuring a partially visible wall with a weathered texture, adding to the sense of an intimate, personal setting.

#### Sample 373 — After

- Similarity: 0.2482
- Prediction: In this frame, the hand grabs the plastic bag and places it on a counter, indicating that the bag has been removed. The bag's contents are still visible, including the contents of the bag, as well as other items in the bag. The person's hand is still motion-free, with the bag still firmly attached to the counter.
- Reference: The knife has progressed further into the sandwich, indicating a deeper cut. The bread shows a clear separation where the knife has passed through, and the contents inside become slightly more distinguishable. The hand maintains its firm grip on the sandwich, ensuring that it stays in place while being sliced. The overall shape of the sandwich seems to have retained its integrity despite the cut.

#### Sample 379 — After

- Similarity: 0.3197
- Prediction: In this frame, the pot appears to have been removed from the burner, indicating that it has been placed in a different position. The pot's surface appears to be slightly tilted away from the stove, suggesting that the pot is still in its original position.
- Reference: The tray is now distinctly separated from the scales. It appears to be in mid-air, being actively lifted or removed. The angle of the tray is much steeper than before, and it is evident from the shadow beneath it that it is no longer in contact with the scale's surface. The tray's position suggests it's being held by someone, though the hand is barely visible.

#### Sample 380 — After

- Similarity: 0.4385
- Prediction: In this frame, the pot appears to have been removed from the burner, indicating that it has been placed in a different position. The person's hand is now more likely to be holding the pot, implying that the pot has been removed. The pan's surface appears to be slightly dampened, suggesting that there may have been a change in the position of the pot.
- Reference: The frying pan's content remains consistent with the seasoned salmon fillets or protein pieces. However, the pieces now appear to have been cooked more evenly, with a more consistent golden-brown hue across their surface. The surrounding smaller bits or residues in the pan seem to have further reduced or have been pushed to the edges of the pan. The pan itself is still on the burner, and while it's not visibly evident, it can be assumed the heat continues to cook the contents based on the progression seen in the food.

#### Sample 381 — After

- Similarity: 0.3807
- Prediction: In this frame, the meat has been removed from the pan, indicating that it has been partially removed. The meat is now firmly placed on a cutting board, implying that the knife has been used to cut the meat into bite-sized pieces. The chef's hand appears to be holding the meat in place, suggesting that the meat may have been slicked into the pan.
- Reference: The seasoning process seems to have advanced further. The hand's position has shifted, possibly suggesting a movement across the dish to ensure uniform seasoning. The spread of the spice on the dish appears denser than in the previous frames, signifying a more substantial application. The overall appearance of the dish suggests that the seasoning process is nearing its completion, as the spice particles appear to be evenly distributed across its surface.

#### Sample 384 — After

- Similarity: 0.4189
- Prediction: In this frame, the refrigerator door is positioned in a position where it's more likely to be open, indicating that there is a greater amount of space in the fridge for food or other items. The door's focus is now on the contents of the refrigerator, with the kitchen still visible. The interior of the fridge appears to be cluttered, with only a few items visible, such as the refrigerator's contents.
- Reference: The jug is now outside the refrigerator, held by a person whose hand and lower arm are visible. The motion is more pronounced, with the background significantly more blurred due to the speed of the action. The milk's position in the person's hand has changed; it is now being transported to a new location, likely a countertop or table. The grip on the handle is tight, indicating that the milk is being moved quickly and with care to avoid spillage.

#### Sample 386 — After

- Similarity: 0.4820
- Prediction: In this frame, the fish's surface is more exposed, indicating that the fish has been fully cooked. The hands are now more engaged in the process of removing the fish from the skin, which is likely a sign of the final stages of the cooking process.
- Reference: The piece of meat is now in a different position, showing another angle and revealing more of its natural shape. The handling is still gentle but seems more purposeful, as if the person is ready to place it down or into a cooking vessel. The consistency of the meat's color and texture is uniform, and there's no visible tearing or breaking, which would indicate it's still intact from the handling. The meat’s position relative to the bowl has shifted, indicating a progression in the handling process.

#### Sample 389 — After

- Similarity: 0.4981
- Prediction: In this frame, the kitchen sink is now positioned in a position where it's more likely to be placed in the center of the room. The door is now open, indicating that there is a gap between the cabinet and the sink. The kitchen appears to have been partially closed, suggesting that the sink is still open.
- Reference: The locker's door is now fully open, revealing its inner shelves and their contents more clearly. The lower part of the locker seems to contain a white microwave oven, and a part of a grocery bag can be seen protruding slightly from the locker's interior. The appliances from the previous frame are still in view on the countertop, with the kettle now lit, indicating it's in use. The user's arm is more extended, suggesting the action of opening the door was recently completed.

#### Sample 391 — After

- Similarity: 0.3723
- Prediction: In this frame, the kitchen sink has been sanitized, indicating that it has been thoroughly rinsed. The hands are now more engaged in scrubbing the sink, which is likely a step in the process of rinsing the sink. The water level appears to have decreased, suggesting that the sink is now being rubbed with soapy water.
- Reference: The chopping board now appears to have even more water coverage, with nearly the entire surface gleaming with wetness. Puddles of water are more pronounced and seem to be joining together, giving the board a uniformly damp appearance. There are very few dry patches visible, and the entirety of the board has taken on the darker hue of blue seen in the wet sections from the previous frames.

#### Sample 392 — After

- Similarity: 0.3590
- Prediction: In this frame, the person's hand is more firmly grasped, indicating that the door has been closed. The door's contents are still visible, including the contents of the container, as well as the door itself, which is now partially open. The hand's position is more relaxed, suggesting that the object is more likely to be in the hands of the person who is holding the door.
- Reference: In this frame, the tea towel has been further disturbed, with more pronounced creasing and bunching of the fabric. The hand has a firmer grasp on it, and there's a dynamic sense of movement. The fabric's position in the drawer is more disheveled, and the bright stripes are now at different angles, displaying the chaos of the movement. The tea towel seems to be either in the process of being taken out completely or rearranged significantly within the drawer.

#### Sample 397 — After

- Similarity: 0.4568
- Prediction: In this frame, the pot appears to have been removed from the kitchen counter, indicating that it has been placed in a different position. The pot's surface is now more exposed, suggesting that the pot has been removed. The chef's hand appears to be holding the pot, implying that he or she is removing the pot from the stove.
- Reference: In this frame, the salt container has been repositioned even more noticeably. It's apparent that there has been some interaction with it, potentially involving its use in the cooking process. However, the cap remains in its sealed position, suggesting that no salt has been dispensed during this specific moment captured in the frame. The nearby items and their arrangement further indicate continued progress in the kitchen activities.

#### Sample 398 — After

- Similarity: 0.4483
- Prediction: In this frame, the utensil has been removed from its handle, indicating that the water has been rinsing. The hand's position is more relaxed, suggesting a more thorough rinse. The water's consistency is more consistent, suggesting that there may have been a few drops of water on the surface. The hands' posture is less relaxed, implying that they are more engaged in the rinse process.
- Reference: The jar clip top remains in the open position, with the metal clasp disengaged. The hands are more prominently holding the rubber seal and the metal clip, perhaps to adjust, clean, or ensure its proper functionality. The glass body of the jar is now more visible, reinforcing the emphasis on the maintenance or inspection of the clip top mechanism.

#### Sample 401 — After

- Similarity: 0.2869
- Prediction: In this frame, the person's hand is more firmly grasped, indicating that the hand is now in a more natural position. The hand's posture is more relaxed, suggesting that the person is more likely to hold the tray upright. The shadow of the tray's surface is more apparent, implying that the tray is now partially closed. The object's shape, such as a towel or a cloth, appears to have been partially removed from the tray.
- Reference: Here, the floor's appearance is much the same in terms of color and sheen, with the wooden planks consistently arranged. The action of sweeping is more pronounced, with the sweeper's path slightly more visible. The small debris and particles are becoming less scattered as they are being corralled by the sweeper, which has visibly disturbed them from their resting spots. There's a sense that the cleaning process is ongoing, with some areas of the floor now appearing cleaner than before.

#### Sample 403 — After

- Similarity: 0.3275
- Prediction: In this frame, the bread has been partially removed from the cutting board, indicating that the knife has been inserted into the bread. The bread's surface appears to have been partially cut off, with the knife's edge still visible. The hand's movement is evident, suggesting that the bread is now partially cut open. The hands' movements are consistent with the previous frame's focus on the bread, which suggests that it may have been sliced before the knife was inserted.
- Reference: In this frame, the onion seems to be part of a more elaborate culinary preparation. The slices are now combined with other ingredients on top of the bread or dough base. Specifically, there's an addition of what appears to be cheese or another dairy product intermingled with the onion slices. The layers suggest that the meal is being prepared with care, ensuring a blend of flavors. The presence of other ingredients along with the onion hints at a composite dish, possibly heading towards baking or cooking.

#### Sample 406 — After

- Similarity: 0.3010
- Prediction: In this frame, the bin's lid has been removed from the bin, indicating that it is now in its final position. The person's hand appears to be engaged in a more deliberate action, implying that the lid is now fully closed. The lid's position remains unchanged, suggesting that the bin is now partially closed.
- Reference: The strainer is positioned over a receptacle, appearing almost directly above it. Very minimal traces of the orange-yellow liquid remain within the strainer, signifying that almost all of it has been emptied out. The strainer itself, mostly void of its contents, appears clean and almost pristine, with its mesh structure being more evident and discernible.

#### Sample 410 — After

- Similarity: 0.3481
- Prediction: In this frame, the jar has been removed from the kitchen counter, with the lid still attached to the container. The hand's grip is now more firm, indicating that the lid has been partially removed. The jar's contents are still in the container, with no visible signs of cooking.
- Reference: In this frame, the dispersal of sweetcorn across the pizza appears more complete. The kernels are spread out with a greater coverage, filling in previously bare patches of dough and sauce. The hand and can that were dispensing the sweetcorn are still present, implying the continuation of the action, yet there’s a sense that the sprinkling process is nearing its end. The kernels that have landed seem static, resting heavily upon the surface as if settling into their final position.

#### Sample 412 — After

- Similarity: 0.4330
- Prediction: In this frame, the rinsing pan is now in a more natural position, with the water evaporating from the bottom of the pan, indicating that the water has been drained. The water's consistency is more uniform, suggesting that the pan has been washed more frequently. The hand's movements are more relaxed, implying that there is a slight movement in the direction of the water. The kitchen's lighting is still dim, with only a few drops of water on the surface of the kitchen counter.
- Reference: In this frame, the spring onion is undergoing a thorough rinse. The fingers have moved further up, near the middle of the stalks, ensuring a secure hold while the water cascades over the entire length of the onion. The stalks are bending gracefully under the stream of water, highlighting their fresh and pliable nature. The glistening droplets splash off the onion's surface, washing away any residual soil or debris, and the roots are now fully immersed, indicating a complete cleaning process.

#### Sample 417 — After

- Similarity: 0.4905
- Prediction: In this frame, the scrubbing brush is now more firmly held, indicating that the water has been rinsing the brush. The brush's surface appears to be soiled, suggesting that the brush has been thoroughly washed away. The hand's movements are more relaxed, suggesting a more thorough cleaning of the brush, which is likely aimed at removing any remaining soap residue.
- Reference: The chopping board's position has not drastically changed, but the focus on the board is clearer as the hand has moved away, giving an unobstructed view. The board still slopes downwards, with water from the tap streaming over its surface. The water's sheen on the board's surface is less soapy, which might suggest the rinsing process is nearing completion. The light reflecting off the wet surface accentuates the scratches and signs of wear, showing the board's longevity and frequent use.

#### Sample 420 — After

- Similarity: 0.4998
- Prediction: In this frame, the person's hand is more firmly grasping the plastic bag, indicating that the bag has been fully opened. The bag's contents are more readily visible, including the contents of the bag, as well as the contents in the bag. The hand's focus is now on the bag itself, which is more likely to be in the hands of the person who is handling it.
- Reference: The freezer door is now open wider than in the previous frames, with the person's hand appearing to have completed the motion of either placing or retrieving an item. The frozen bag is now partially obscured by the person's hand, but the contents still hint at a variety of colors from the possible vegetable mix inside. The compartments on the door are slightly more discernible, showing empty spaces that could be used for additional storage. The lighting remains consistent with the previous frames, illuminating the freezer's interior while casting a shadow on the surrounding floor and walls.

#### Sample 422 — After

- Similarity: 0.4926
- Prediction: In this frame, the oven has been removed from its original position, indicating that it is no longer in use. The person's hand is still motionless, suggesting that there is no movement in the oven. The kitchen environment remains unchanged, with the kitchen still cluttered and cluttered with food, dishes, and other items.
- Reference: The oven glove reappears in the scene, this time being worn correctly with the person's hand fully inserted into the glove. The fit appears snug and proper, covering the wrist and extending past the beginning of the forearm. The glove seems to be clean and in good condition, with no visible signs of wear or damage. This suggests that the individual is prepared to either handle something hot or is in the midst of doing so, with the glove serving its intended purpose of protecting the hand from high temperatures.

#### Sample 427 — After

- Similarity: 0.3291
- Prediction: In this frame, the bowl is now in a more pristine state, with a clearer image of the bowl's surface. The hand's focus is now on the bowl, which is now positioned in the center of the frame, indicating that the bowl has been placed in the correct position. The bowl appears to have been taken out of its original position, but the hand still maintains a steady grip on it, suggesting that it may have been removed from the bowl.
- Reference: The perspective shifts lower, and the bottom section of the refrigerator comes into view, showing clear crisper drawers that seem to hold vegetables. The door remains wide open, and the lack of illumination inside the refrigerator is more apparent, potentially indicating that the bulb is out or the refrigerator is powered off. The white interior of the refrigerator contrasts with the dark green of the vegetables, making them stand out. The bare feet of the person, visible at the bottom of the frame, indicate a casual, domestic setting.

#### Sample 430 — After

- Similarity: 0.3988
- Prediction: In this frame, the lid has been removed from the container, indicating that the contents of the container have been removed. The person's hand is still holding the lid, which is likely a sign that the container has been partially removed from its container. The lid's surface appears to be slightly dampened, suggesting that the liquid has been absorbed into the container's contents.
- Reference: Here, the bag is held open more deliberately, with fingers gripping the edges, causing further stretching of the material. The mouth of the bag is now wide open, and the interior is fully exposed, suggesting that the contents can be easily accessed or have already been removed. The bag's material is stretched taut at the opening, with fewer creases, and the light reflects evenly across its surface, indicating the smoothness caused by the tension in the material.

#### Sample 431 — After

- Similarity: 0.2763
- Prediction: In this frame, the rinsing is complete, indicating that the water has been drained out of the hose. The water's consistency is more uniform, suggesting that there may be a slight movement in the direction of the rinse. The hand's movements are more relaxed, suggesting a more thorough rinse.
- Reference: The lettuce leaf is now out of the water stream, its surface glistening with moisture. It’s being held aloft, which allows some of the water to trickle off, reducing the excess water weight and revealing the leaf's sturdy yet flexible structure. The leaf's vivid green color remains a testament to its freshness, while the residual water droplets catch the light, giving the leaf a jewel-like appearance. The act of holding the leaf up also suggests that it is being inspected or is about to be set aside to dry.

#### Sample 433 — After

- Similarity: 0.3934
- Prediction: In this frame, the person's hand is positioned in a slightly different position, indicating that the door has been closed. The door's current position indicates that there is no movement in the door or the door itself, implying that the person has been able to open the door.
- Reference: The cloth now appears more loosely held, with the person's grip relaxed, suggesting the squeezing action may be complete. The cloth itself looks less twisted and more spread out than in the previous frames, with some parts hanging down, indicating that it is likely in the process of being opened up after wringing. The color of the cloth remains consistent with the earlier frames, light and uniform, without any visible patterns or designs that can be made out from this perspective.

#### Sample 436 — After

- Similarity: 0.4688
- Prediction: In this frame, the spoon is now positioned on the counter, indicating that it has been removed from the kitchen counter. The person's hand appears to be engaged in a more deliberate action, suggesting that the spoon has been placed in the kitchen. The spoon's position suggests that the hand is preparing for another task, such as cooking.
- Reference: The peeler now has been picked up again, and the hand that grips it exhibits a more dynamic tension, as if it is in the midst of peeling action. The peeler's blade is angled in such a way that it is ready to make contact with the eggplant, positioned to continue the peeling process. This frame captures the motion of food preparation, with the hand's positioning and the peeler's orientation suggesting a repetitive and rhythmic motion typical of peeling vegetables.

#### Sample 437 — After

- Similarity: 0.3879
- Prediction: In this frame, the bowl has been placed in a position where the water has been drained, indicating that it has been thoroughly rinsed. The bowl's surface appears to be slightly dampened, suggesting that the water is still able to drain from the bowl. The hand's movements suggest that the bowl is now agitated, possibly with the water running through it.
- Reference: A hand comes into the frame, moving towards the pepper pieces, suggesting an intention to pick them up or move them. The fingers are positioned in a way that they are about to grasp the pepper pieces, suggesting imminent action. The overall composition of the frame captures a moment of anticipation, as the viewer waits to see where the pepper pieces will be moved to next.

#### Sample 439 — After

- Similarity: 0.4544
- Prediction: In this frame, the scrubbing brush is now more firmly held, indicating that it has been rinsing. The brush's surface appears to have been thoroughly rinsed, suggesting that the water has been removed from the brush. The hand's movements are more relaxed, suggesting a more thorough cleaning of the brush, which is likely a sign that the brush has been thoroughly washed.
- Reference: Now, the towel seems to be in a different state of use, as the person's hands are gripping it firmly and it's being wrung out, judging by the twisted form of the towel and the way the hands are positioned. The towel has darkened considerably, likely due to the absorption of water, and the red patterns on it have become more prominent against the now darker yellow background. The action of wringing is implied by the tension seen in the person's forearms and the twisted contour of the towel, with droplets of water likely being expelled from the fabric.

#### Sample 440 — After

- Similarity: 0.3297
- Prediction: In this frame, the meat has been placed in a single layer, indicating that it has been partially removed from the pan. The surface of the meat appears to have been thoroughly cooled, with no visible signs of cooking. The meat's texture has improved, suggesting that it may have been a bit more tender than previously thought. The knife's edge is slightly curved, suggesting a slight movement in the process of removing the meat from the skillet.
- Reference: The cheese has been substantially disturbed by the scooping action, now clinging heavily to the spoon. Its pliable nature is evident as it stretches slightly, forming a peak where the spoon is lifting it away from the container. The cheese maintains its integrity despite the stretch, not breaking apart or crumbling, which signifies a soft but cohesive quality. The container from which it is being scooped shows more of its interior, indicating that a significant amount has been extracted.

#### Sample 443 — After

- Similarity: 0.4831
- Prediction: In this frame, the spoon has been withdrawn from the bowl, indicating that the contents of the bowl have been removed from the spoon. The spoon's surface appears to be slightly dampened, suggesting that there may be a small amount of liquid left in the bowl. The object's shape is more uniform, with a smoother surface and a more uniform texture.
- Reference: Here, the liquid displays a higher degree of aeration as evidenced by the larger and more numerous air bubbles on the surface and around the beaters. This increased aeration hints at a further transformation into a frothier and lighter mixture, perhaps evolving towards a stage suitable for baking or cooking applications that require a fluffy consistency. The liquid's surface has a more textured appearance, with varying heights and areas of density as a result of the mixing action, which is now more vigorous and thorough.

#### Sample 444 — After

- Similarity: 0.3237
- Prediction: In this frame, the tinkering tool appears to be fully engaged, indicating that the knife has been properly inserted into the blade. The knife's surface is slightly uneven, suggesting that it may have been partially inserted. The sharp edge of the knife appears to have been pushed against the blade's edge, implying that the blade has been pressed against the edge.
- Reference: The whetstone's position remains largely unchanged, still vertically oriented with its finer grit facing upwards. A slight shadow cast on the countertop suggests that the light source may have slightly shifted or that the hand positioning has altered. The stone's surface appears more uniformly reflective, with fewer distinct patches of light reflection as seen in the previous frame. The label is still visible, albeit upside-down, and continues to be partially obscured by the user's hand.

#### Sample 447 — After

- Similarity: 0.4869
- Prediction: In this frame, the sink has been placed in a new position, with the lid facing downwards, indicating that the water has been drained. The person's hand is still holding the lid, which is likely a sign that the sink is about to be filled with water. The sink's surface appears to be slightly dampened, suggesting that there may be a slight movement in the process of removing the lid from the sink.
- Reference: The scene shifts to a close-up view of the food processor, now repositioned back onto the dishwasher's lower rack, indicating a return to its storage place after the rinse. The hand is seen in the midst of securing the lid onto the processor base, with the alignment of the lid's feed tube and the base's central column suggesting a final step in the cleaning process. The utensils around it, including a ladle and a sieve, remain static, pointing to a paused moment in the midst of kitchen tidy-up activities.

#### Sample 453 — After

- Similarity: 0.4451
- Prediction: In this frame, the sink appears to have been sanitized, indicating that it has been thoroughly washed. The person's hand is now more focused on the sink, suggesting that the water has been drained out of the sink. The sink's surface appears to be cleaner, with fewer streaks of water visible. The water's consistency is more uniform, suggesting a more gradual cleaning process.
- Reference: The entirety of the counter now appears refreshed. The dust and crumbs that once littered its surface have vanished, replaced by a homogeneously clean area. There's a mild sheen, evidence of the damp cloth's recent journey across the counter. Any residual streaks that once broke the surface's uniformity have been skillfully addressed, leaving behind a counter that invites one to utilize its pristine surface.

#### Sample 456 — After

- Similarity: 0.4391
- Prediction: In this frame, the rinsing device is now in a more natural position, with the water dripping out of the handle, indicating that the water has been drained. The hand's movements are more relaxed, suggesting that there is a slight movement in the water's direction, possibly a change in the position of the hand. The water level appears to be at a higher or lower level, suggesting a thorough cleaning of the device.
- Reference: The coffee machine remains in the same decorative design with its distinct blue and gold patterns. However, its position appears to have slightly changed, indicating that it might have been shifted or rotated. The top part of the machine is more visible than in the previous frame, and the hand that was earlier interacting with it is no longer obstructing the view. The ambiance of the surroundings seems brighter, suggesting a slight change in lighting or camera exposure.

#### Sample 459 — After

- Similarity: 0.4037
- Prediction: In this frame, the kitchen sink is now in a more streamlined position, indicating that it has been removed from the kitchen counter. The person's hand is now positioned on the edge of the sink, suggesting that the sink is still in its current position. The kitchen appears to be preparing for a meal or other activity, with the sink still positioned in the middle of the kitchen.
- Reference: The can is now in motion, as evidenced by the blurred surroundings and the dynamic angle of the can itself, suggesting that it is being moved rapidly. The blurred hand position suggests a downward action, likely placing or dropping the can into a receptacle out of frame. The lid appears to be in the same state of opening as the previous frame, not further detached, but the rapid movement has caused the contents to shift, potentially leading to the spillage of the liquid and the spherical items within.

#### Sample 460 — After

- Similarity: 0.3859
- Prediction: In this frame, the pan's surface appears to be a bit cleaner, with a more streamlined appearance. The person's hand is now more focused on the surface, indicating that the pan has been thoroughly cleaned. The surface of the pan appears to have been sanitized, suggesting that there may be some residue left behind from the cleaning process.
- Reference: The scene here is noticeably clearer, suggesting a near halt in motion. The tap, with no active engagement from the hand, seems to be in a dormant state. There is no visible water flow or splash, indicating that the tap is likely fully closed. The surrounding area of the tap shows residual moisture, which, along with the absence of blur, signifies the cessation of water flow. This frame captures the conclusion of the action, with the tap now in a static and inactive state.

#### Sample 463 — After

- Similarity: 0.4297
- Prediction: In this frame, the pot appears to have been removed from the burner, indicating that the pot has been removed. The pan's surface appears to be in a state of flux, suggesting that the pan has been partially removed from its cooking surface. The pot's lid remains in place, with the lid still attached to the pot.
- Reference: The third frame continues to showcase the kitchen environment and the hand in close proximity to the countertop or appliance interface. The specific state of the switch remains elusive, but there's a distinct impression of movement, potentially indicating the switch's activation or deactivation. The close-up nature of this frame in relation to the switch area suggests that there's an ongoing interaction, but the definitive state of the switch, either on or off, cannot be confidently ascertained.

#### Sample 468 — After

- Similarity: 0.4608
- Prediction: In this frame, the rinsing device is now in a more natural position, with the water dripping onto the surface. The hand's movements are more relaxed, indicating that the water has been drained away from the surface of the device. The water's surface appears to have been washed away, suggesting that there may have been a few drops of water on the surface, which may have caused the water to settle. The person's hands appear to be more engaged in the process, with their fingers pointing toward the surface to ensure that the surface remains clean. The hands' movements are less agitated, and the water appears to be sprinkling around the edge of the handle.
- Reference: The bell pepper is now completely wet, with water streaming uniformly across its surface, resulting in a gleaming, reflective sheen that envelops the vegetable. The droplets are no longer individual but have formed a continuous layer, suggesting that the pepper has been turned and manipulated under the water to ensure all sides are equally cleansed. The hand's grip is steady, with the thumb pressing lightly on the stem, perhaps to prevent the pepper from slipping during the washing process.

#### Sample 469 — After

- Similarity: 0.3771
- Prediction: In this frame, the spoon is now in a more streamlined position, indicating that it has been removed from the kitchen counter. The hand is now more focused on the spoon, suggesting that the spoon has been placed in its proper position. The spoon's surface appears to have been wiped down, with the spoon still firmly attached to the counter.
- Reference: The cover seems to be in a more elevated position compared to the previous frames, with the lifting process appearing almost complete. The perspective shows a more pronounced view of its underside. Shadows under the cover suggest it's hovering above its initial position, which combined with the visible hand movement, implies it's being actively lifted. The surrounding area is slightly blurred, indicating swift motion, further emphasizing the dynamic state of the cover being removed.

#### Sample 470 — After

- Similarity: 0.3214
- Prediction: In this frame, the bottle has been placed in a new position, with the lid still attached to the bottle. The person's hand is now engaged in the process of removing the cap from the bottle, indicating that the cap has been removed. The liquid content of the bottle remains consistent with the previous frames, suggesting that the bottle may have been discarded.
- Reference: The plug is now almost completely removed from the socket, with only the tips of the prongs still in contact with the outlet. The person’s hands, still sheathed in yellow gloves, show a relaxed grip, indicating the completion of the unplugging action. The background remains cluttered, and the shadow of the person’s hands and the plug is still visible on the wall, mirroring the action above.

#### Sample 473 — After

- Similarity: 0.3628
- Prediction: In this frame, the hose has been placed in a more upright position, indicating that the water has been drained out of the nozzle. The hand's movements are more relaxed, suggesting that there is a slight movement in the water's direction. The hose's surface appears to have been sprayed with water, implying that it has been fully soaked or washed. The water level appears to be at a higher than usual level, suggesting a gradual process of rinsing.
- Reference: The cap is now visibly detached from the bottle, held aloft in one hand while the other continues to secure the bottle. The threading on the neck of the bottle where the cap was once secured is now exposed, and the cap's interior is visible, showing the underside which would normally be sealed against the bottle's opening. The detachment of the cap suggests the completion of the opening process. The environment and the bottle's position remain consistent, indicating that the sequence of actions occurred within a short timeframe.

#### Sample 474 — After

- Similarity: 0.4957
- Prediction: In this frame, the utensil has been placed in a position where the water has been rinsing, allowing the water to reach the surface. The hand's movements are more relaxed, indicating that the water is being rubbed into the urn. The water's consistency is more consistent, suggesting that the raffination process is complete. The hands' movements are less agitated, suggesting a more thorough rinse.
- Reference: The coffee holder is now placed directly under the water stream, and the user is manipulating it with a twisting motion, ensuring all interior surfaces are thoroughly rinsed. The water running off the holder appears clear and free of coffee debris, indicating that the holder is nearly or completely clean. The holder's metallic interior reflects the light, highlighting its cleanliness against the darkened coffee-stained areas that have now been washed away.

#### Sample 476 — After

- Similarity: 0.3873
- Prediction: In this frame, the tortilla has been placed on a counter, indicating that it has been removed from the oven. The tortilla's surface appears to have been partially removed, suggesting that the tortilla may have been placed in the oven before being removed. The palms of the tortilla are now positioned in the middle of the plate, with the palms pointing toward the center of the pizza. The hands are now more engaged in the process of removing the tortilla, implying that there is still a lot of work to be done.
- Reference: In this frame, the salt shaker is still tilted, with a slightly adjusted angle, indicating an ongoing shaking action. The hand's movement seems more deliberate and controlled, as if the person is nearing the end of the seasoning process. Salt can be seen in mid-air, caught in the act of falling onto the cheese, which suggests that a considerable amount of shaking has already been done. The distribution of salt appears to be focused more towards the center of the flatbread.

#### Sample 477 — After

- Similarity: 0.4980
- Prediction: In this frame, the rice appears to be fully cooked, indicating that the water has reached a simmering stage. The spoon's motion indicates that the rice has reached its boiling point, which is likely due to the presence of a large amount of water in the pan. The color of the rice seems to be more vibrant, with a slightly darker hue to the rice.
- Reference: Here, the light maintains its vivid blue core but is surrounded by a broader, less intense outer flame, which hints at a stable and sustained heat source. The consistency of the flame's color and shape suggests that the burner is now in a steady state, providing a continuous and even heat. The light's reflection is consistent and widespread, indicating that the burner has reached an optimal operating condition, and the pot is fully enveloped in the heat, likely contributing to a steady cooking process.

#### Sample 480 — After

- Similarity: 0.3972
- Prediction: In this frame, the spout is now in a more streamlined position, with a clearer, more rounded shape. The hand's movements seem to be more relaxed, indicating that the water has been drained out of the nozzle. The water's surface appears to be drier than before, suggesting that the rinsing process has been completed.
- Reference: The dispensing action seems to have concluded, with a discernible portion of the sponge now saturated with the liquid washing up. The wetted area appears glossier and darker in contrast to the other parts of the sponge, suggesting that a significant amount of liquid has been absorbed.

#### Sample 481 — After

- Similarity: 0.4913
- Prediction: In this frame, the rinsing device is now in a more natural position, with the water running through the nozzle. The person's hand is still holding it, indicating that the water has been drained out of the hose. The water level appears to be at a higher level, suggesting that the nipples have been rinsed away.
- Reference: The jug, still under the firm control of the hand, now contains water up to a significant level. The surface of the water appears disturbed and dynamic, as the force of the water creates turbulence. It is not yet full, providing a glimpse into the progression of filling, where the once empty space is now partially occupied by water. The hand's grip on the handle appears relaxed yet attentive, suggesting an ongoing process that requires monitoring.

#### Sample 482 — After

- Similarity: 0.4796
- Prediction: In this frame, the foil has been partially removed from the oven, indicating that it has been completely removed. The foil's surface is slightly exposed, suggesting that the foil is being partially removed, implying that the person is now removing the foil. The person's hand is still firmly grasping the foil, which is likely a sign of the bread's readiness to be sliced.
- Reference: The packaging now shows clear signs of being tampered with. The hand continues its interaction with the lighter meat's package, and it appears that a portion of the seal is being lifted or pulled back. The action suggests that the individual is in the process of opening the packaging to access the meat inside. Although the seal isn't entirely removed, a partial view of the meat inside becomes visible, indicating that the package is no longer in its original, untouched state.

#### Sample 485 — After

- Similarity: 0.4405
- Prediction: In this frame, the hand is positioned in a slightly different position, indicating that the door has been closed. The door's contents are still visible, including the contents of the container, as well as the contents inside the container. The object's shape, such as a plastic bag, is now more prominently displayed in this frame. The person's hand appears to be attempting to open the door, revealing a gap between the contents and the camera's focus.
- Reference: The milk carton has now made contact with the floor, resting on its side with the top facing the wall. It is placed near a corner where the wall meets the floor, and the person’s hand is reaching towards it, possibly to pick it up or prevent spillage. The immediate vicinity is relatively bare, apart from a television and cleaning equipment, which implies that the carton might be in a transitional area such as a corridor leading away from the kitchen.

#### Sample 490 — After

- Similarity: 0.4285
- Prediction: In this frame, the bread has been partially removed from the pan. The person's hand is now more firmly grasping the bread, indicating that the bread is ready to be sliced. The bread's texture is more consistent, with a smoother texture and a crisper appearance. The hands are now more engaged in the process of preparing the bread.
- Reference: The tortilla is now partially folded, with the hand actively pinching one edge, guiding it into the confines of the plastic packaging. The tortilla has transformed from its previously flat and open state to a semi-crumpled form, bending to accommodate the reinsertion process. This action creates creases and wrinkles on its surface, a stark contrast to the previously smooth appearance. The tortilla is now interacting with its packaging, which bears bold colors and brand markings that suggest a commercial origin.

#### Sample 491 — After

- Similarity: 0.4445
- Prediction: In this frame, the pak choy has been removed from the cutting board, indicating that the knife has been slicked open. The knife's blade is now positioned in the middle of the chopping board, with the blade pointing downwards. The leaves are now arranged in a single layer, forming a sprinkling of leaves and stems, which are now more uniformly distributed across the board.
- Reference: By this point, the coriander has undergone more significant cutting. The leaves and stems are more dispersed across the board, with clear distinctions between the cut and uncut parts. Some of the leaves are more finely chopped than in the previous frame, and there's an increase in the amount of visible cutting board space, indicating the progress in the preparation.

#### Sample 492 — After

- Similarity: 0.4923
- Prediction: In this frame, the bowl appears to have been sprayed with water, indicating that the water has been drained out of the bowl. The hand's movements indicate that the bowl has been thoroughly rinsed, and the water is now able to reach the bowl's surface.
- Reference: The pot's position has been adjusted, with the opening tilted upwards, allowing a better angle for the individual to clean the inside. The pot is now held at a tilt, and the water is splashing into the interior, likely rinsing away the remaining soap suds. There's a visible reduction in the amount of foam and bubbles, indicating that the pot is nearing the end of the washing process. The individual's grip has shifted, with fingers wrapped around the rim and the handle, providing stability as they clean. The yellow sponge is now clearly visible, and its placement suggests the individual is focusing on scrubbing a specific area inside the pot.

#### Sample 494 — After

- Similarity: 0.3089
- Prediction: In this frame, the microwave has been removed from the kitchen, indicating that it is no longer in use. The interior of the microwave is now cluttered with a variety of items, including dishes, pots, and other items. The kitchen's focus is now on the kitchen area, which includes the kitchen counter, oven, and microwave.
- Reference: In this frame, the door is fully open, or nearly so. Its interior is now clearly visible, showcasing the contents and shelves within. The handle is in its most extended position, suggesting that the door has reached its maximum opening capacity. The illumination inside the compartment contrasts with the dimmer ambient light of the room, accentuating the contents within the door.

#### Sample 495 — After

- Similarity: 0.3438
- Prediction: In this frame, the hand is now positioned on the edge of the kitchen counter, indicating that it has been placed in a position where it is likely to be used for cooking. The hand's focus is now on the surface of the counter, suggesting that the hand has been positioned in the same position as before, implying that it is now in the position of its intended use. The palm of the hand appears to be slightly tilted forward, suggesting a slight shift in the direction of the action. The hands are still positioned at the center of the table, with the palm resting on the counter.
- Reference: In this frame, the plug is now half-out of the socket, with the prongs partially visible and the plug's body tilted downwards at an angle indicative of it being in motion. The motion seems to be a result of the pulling force applied to the cord, which is more taut and directed sharply to the bottom right. The plug's removal from the socket has not been completed yet, as the electrical connection appears to be still partially intact. The environment remains unchanged, continuing to suggest a domestic interior with minimalistic design elements.

#### Sample 496 — After

- Similarity: 0.3148
- Prediction: In this frame, the paper towel is now in a more streamlined position, with a slightly more rounded shape. The hand's movements are more deliberate, indicating that the towel has been placed in the correct position. The paper towel's shape is more consistent with the rest of the fabric, suggesting that it may have been taken from a previous position.
- Reference: The focus here is closely on the bag, held outstretched in one hand, displaying the 'THIS SIDE UP' instruction clearly, signifying the correct orientation for microwave cooking. The bag appears more bloated than in the previous frame, suggesting the popcorn has fully popped. The text on the bag is sharp and readable, showing a caution for the contents being hot. The person's handling of the bag, with a single hand from the bottom, indicates confidence that the popping is complete and readiness to open the bag.

#### Sample 8 — Transition

- Similarity: 0.4830
- Prediction: Over the course of these three frames, there's a clear progression in the state of the blender. Initially, it's in a state of rest, with the user's hand indicating that the blender is ready for use. As the sequence progresses, the hand's interaction with the blender becomes more evident, implying that the user is engaged in the process of adjusting the blender's settings. By the final frame, the blender appears to be ready to be used, and the person's actions are clearly visible.
- Reference: As the video progresses through the three frames, the toaster transitions from a dormant, inactive state to a fully operational one. Initially, it rests passively with all indicators suggesting non-use. However, as the frames advance, the toaster's lever is actuated, marking the beginning of its function. The inner glow and increasingly bright power light signal the toaster's heating elements coming to life, culminating in the third frame where it's evident that the toasting process is in full swing. The evolving luminosity within the slots and the changing position of the lever chronicle the journey of a simple machine springing into action, transforming raw bread slices into delightful toast.

#### Sample 15 — Transition

- Similarity: 0.3992
- Prediction: Over the course of these three frames, there's a clear progression in the state of the jar's contents. Initially, it's in a state of disintegration, but as the hand engages it, the contents begin to fall apart. By the final frame, the lid is open, indicating that the contents have been removed from the container. The hand's actions are indicative of the process of removing the contents of the container, which is likely a step in the kitchen's preparation process.
- Reference: Over the course of the three frames, the stock undergoes a notable transformation in its preparation and presentation. Initially presented in a clear state with a gentle ripple, it transitions to a heated state with evidence of simmering in the second frame. By the third frame, the stock has thickened, likely due to a combination of evaporation and reduction, with the consistency appearing more viscous. The continuous pale yellow color and sheen on the surface suggest a consistent base ingredient, while the various states of agitation and heating reveal the progression of the cooking process.

#### Sample 21 — Transition

- Similarity: 0.4416
- Prediction: Over the progression of these frames, the halibut undergoes a noticeable transformation. Initially, it's being thoroughly rinsed, with the leaves exposed. As the final frame progresses, the water is drained and the leaves are exposed, indicating a thorough rinse. By the third frame, the lettuce is being fully rinsed and ready to be washed, highlighting the process of rinsing and preparing it for cooking.
- Reference: Over the course of the three frames, the pak choi leaf undergoes a noticeable transformation. Initially, it is introduced to the water, undergoing a thorough rinse which lends it a fresh and rejuvenated appearance. As the frames progress, the leaf is lifted and maneuvered, allowing viewers to witness its pristine state post-rinsing. By the final frame, the leaf, though still wet, is no longer under the direct flow of water, and its intricate details, such as the venation pattern and droplets on its surface, become the focal points. This progression underscores the meticulous care taken in cleaning the vegetable, emphasizing its freshness and readiness for culinary use.

#### Sample 22 — Transition

- Similarity: 0.1851
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the meat. Initially, the meat is fully charred, with the skin still exposed. As the frame progresses, the person begins to remove the meat from the skin, indicating that the meat has been partially removed. By the final frame, the process is complete, and the meat appears to be fully cooked. This progression is indicative of a transformation in the meat's state of being, with a gradual change in the skin's texture.
- Reference: Observing the garlic press across these frames, one can trace the process of mincing a clove of garlic. Initially, the press is open with the garlic clove placed inside, awaiting pressure. As we progress, the user applies force, bringing the handles together, causing the inner plunger to push the garlic against the press head. By the final frame, the press handles are almost closed, indicating the clove has been crushed, though the resulting minced garlic is not yet visible. The user’s hands display increasing tension, a reflection of the effort required to extract the essence of the garlic through the metal grid into the awaiting dish.

#### Sample 27 — Transition

- Similarity: 0.4908
- Prediction: Over the progression of these frames, there is a clear progression in the state of the box. Initially, the box is partially open, with no visible signs of the contents. As the sequence progresses, the person's hand moves closer to the box, indicating that the contents are being accessed. By the final frame, the hand's hands are engaged in the process of removing the box's contents, demonstrating a gradual change in the action of the hand. This progression is indicative of a methodical approach to preparing the box for use.
- Reference: The sequence of images illustrates a gradual opening of a Twinings tea box over three stages. Initially, the box is intact, with the cellophane just beginning to be peeled back. In the second stage, the cellophane is removed, and one flap of the box is opened, revealing the silver foil bag inside. By the third stage, the opening process is near completion, with both flaps of the box opened wide and the contents almost ready to be fully revealed. The steady hands of the person indicate a careful and deliberate action, ensuring that the tea bag is not damaged during the unboxing.

#### Sample 28 — Transition

- Similarity: 0.2566
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the tray. Initially, it's in a state of disarray, with no visible signs of activity. As the frames progress, the tray's surface becomes more cluttered, indicating a more active action. By the final frame, the person's actions are evident, with the tray indicating that they're preparing to use it. This progression is indicative of a
- Reference: The paper undergoes a visible transformation across the three frames: from an intact, untouched state to a partially torn state, and finally to a fully torn and separated state. The initial grip and force application result in a rough, uneven tear, highlighting the random nature of paper tearing by hand without a pre-folded line. The tearing process reveals the fibrous interior of the paper, a stark contrast to its initially smooth exterior. This sequence captures the progression of tearing, emphasizing the irreversible change from a whole to a separated state, demonstrating the physical properties of paper under stress.

#### Sample 30 — Transition

- Similarity: 0.4171
- Prediction: Over the course of these frames, there's a clear progression in the state of the chicken. Initially, it's in a state of disarray, with no visible signs of food or water. As the sequence progresses, the chicken appears to have been thoroughly rinsed, ready to be served. By the final frame, there is a noticeable change in the chicken's state of cleanliness, indicating that the water has been drained out, and the chicken is ready for cooking.
- Reference: Observing the colander throughout these frames, it is evident that there is a progressive action taking place. Initially, the rice is soaked and the colander is level. As the frames advance, the colander is tilted and shaken side to side, which causes the grains to redistribute and the water to drain more efficiently. This sequence of motion is consistent with the method of preparing washed rice for cooking, ensuring that it is adequately drained and loose before being added to a pot or rice cooker. The gradual tilting and the increased visibility of separate grains reflect the meticulous process of draining rice, a crucial step in many culinary traditions.

#### Sample 31 — Transition

- Similarity: 0.4342
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the countertop. Initially, it's in a state of disarray, with no visible signs of food or spills. As the frames progress, the person's actions become more visible, indicating a thorough cleaning of the surface. By the final frame, the surface appears to have been thoroughly cleaned, and the cleaning is complete. The consistency of the counter's surface is consistent with the cleaning process, suggesting a cleaner surface.
- Reference: The progression across the three frames reveals the glass being moved in a smooth, lateral motion from left to right across the wooden table surface. Initially at rest, the glass is engaged by the person's hand, inducing a slide that carries through to the subsequent frames. The steadiness of the hand and the unaltered upside-down position of the glass throughout suggest a deliberate and controlled action, with no signs of tipping or erratic movement, portraying a simple but precise maneuver. The light reflecting off the base of the glass shifts accordingly, marking the path and speed of the motion.

#### Sample 36 — Transition

- Similarity: 0.4887
- Prediction: Over the course of these three frames, the sandwich undergoes a transformation from a pristine state to a state of disintegration. Initially, it's untouched, but as the frame progresses, it becomes more and more intertwined with the bread. As the final frame advances, the bread's surface is exposed, indicating a gradual change in the sandwich's shape. The sandwich'
- Reference: Between the first and the third frame, there has been a progression from an unopened state to use. Initially, the butter tub is intact, with its contents concealed and untouched. As the frames progress, the hands and knife convey an intention to use, culminating in the third frame where the lid has been opened, and the spread has been partially scooped. The knife now holds a sample of the spread, signaling that it has been disturbed for the first time. The continuity of the scene is marked by the consistent positioning of the tub and the utensils, with the only changes occurring in the state of the butter and the position of the lid.

#### Sample 39 — Transition

- Similarity: 0.3657
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the pan. Initially, it's in a state of disarray, with no visible or visible debris. As the frames progress, the pan's surface appears to be scrubbing, indicating a thorough cleaning. By the final frame, there is a visible reduction in the amount of soap and water on the pan, suggesting a more thorough cleaning of the surface. The consistency of the soapy water, as well as the constant movement of the sponge, are indicative of a cleaning process.
- Reference: The tap undergoes a transition from a state of active water flow to being turned off across these frames. Initially, the tap is open with water flowing out, as evidenced by the stream and wet surfaces. In the subsequent frame, the tap is seen in the off position, with the hand retracting from what appears to be the action of closing it. By the final frame, the tap remains off, and the individual's attention has turned to other tasks, confirming that the water flow has been successfully halted. The surrounding wetness on the sink decreases progressively, indicating the cessation of water and the passage of time since the tap was turned off.

#### Sample 41 — Transition

- Similarity: 0.3631
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the oven door. Initially, it's partially open, with the door opening and closing. As the frames progress, the door's position changes to a slightly more open position, indicating that the door has been opened or closed. By the final frame, it is almost fully open, suggesting that the oven has been closed or closed for some time. This progression is indicative of a gradual change in the oven's interior state, which is likely a result of the person's interaction with the oven.
- Reference: The progression of these frames captures a small but telling narrative of domestic life. Initially, the milk bottle appears abandoned and potentially open, vulnerable to spilling or contamination. As the frames advance, human interaction becomes evident, with the bottle being given attention, likely to prevent wastage or for storage after use. The cap, initially ambiguous, moves towards a state of being firmly placed back on the bottle. This sequence reflects a moment of care or routine within the kitchen's daily rhythm, a choreography of use and maintenance often overlooked.

#### Sample 51 — Transition

- Similarity: 0.3782
- Prediction: Over the progression of these three frames, the trash can undergoes a subtle change in its state. Initially, it's partially open, with no visible signs of activity. As the frames progress, the person's interaction with the trash is evident, indicating a deliberate action. By the final frame, the lid is fully open, suggesting a close-up of the contents of the trashcan. Throughout the sequence, there is a clear progression in the state of the waste bin, with the remains of the lid and the surrounding environment blurring.
- Reference: The progression from the first to the third frame demonstrates the process of maintaining a cylindrical filter. Initially, the filter is shown partially obscured and in the midst of inspection, indicating the start of a maintenance activity. As the sequence progresses, the filter is removed and displayed in full view, revealing the extent of dirt accumulation and suggesting a thorough inspection or cleaning is underway. By the final frame, the filter is being reinserted into its housing, signaling the completion of the maintenance task. This sequence encapsulates a routine yet crucial aspect of ensuring the efficiency and longevity of the appliance or system the filter is part of.

#### Sample 59 — Transition

- Similarity: 0.3868
- Prediction: Over the course of these three frames, there's a clear progression in the cooking process of the chicken. Initially, it's raw and ready to be cooked, but as it cooks, it starts to become more tender and tender, indicating that the cooking has been done. As the cooking progresses, the color of the meat begins to change, with a gradual change in color and texture. By the final frame, the chicken is starting to turn golden brown, with the skin still showing signs of ageing.
- Reference: From the initial frame to the last, there's a clear progression in the cooking process. Initially, the leeks and onions are bright and firm, just starting to cook. As time passes, they begin to wilt, soften, and release moisture, with the edges of the onions turning translucent. The continuous action of the spatula stirring through the frames indicates an attentive cooking process, aimed at achieving an even sauté. By the final frame, the vegetables have lost some of their vibrant coloring, becoming softer and more amalgamated, which is characteristic of the softening and mingling of flavors that occurs with thorough cooking.

#### Sample 61 — Transition

- Similarity: 0.3873
- Prediction: The sequence of frames captures a clear progression in the state of the table mat. Initially, it's in a state of disarray, with no visible signs of wear or tear. As the frames progress, the mat's surface becomes more pronounced, indicating that it has been agitated. By the final frame, there's an apparent change in the position of the mat, suggesting that the mat has been placed in the correct position. The hand's movements are evident throughout the sequence, suggesting a deliberate action,
- Reference: The journey of the crumb across these frames tells a story of displacement and cleaning. Initially stationary and almost camouflaged by the tablecloth's pattern, the crumb is subtly jostled by the unseen forces exerted by the approaching vacuum cleaner. As the cleaner moves closer, the crumb's environment becomes visibly disturbed, with the material of the tablecloth wrinkling and shifting. Finally, the crumb is drawn into the shadow of the vacuum cleaner, its final moments on the table marked by a dramatic change in light and position, signifying the crumb's inevitable conclusion of being vacuumed away.

#### Sample 62 — Transition

- Similarity: 0.4420
- Prediction: Over the course of these three frames, the flour undergoes a noticeable transformation from a dispersed state to a fully incorporated state. Initially, it's in a state of disintegration, but by the final frame, it has become more incorporated and incorporated into the batter. The hand's movements are evident throughout the process, indicating that the flour has been thoroughly stirred and is ready to be used. The consistency of the dough remains consistent throughout the frames, with the consistency becoming uniform and uniform throughout the entire process.
- Reference: The transition of the olive oil from containment to release is captured across the frames. Initially, the oil is securely enclosed within the bottle, its potential to enhance the dish latent. As the cap is removed and the bottle is tipped, the olive oil is on the cusp of transformation, from an individual ingredient to an integral part of a culinary mixture. Finally, the oil is liberated, joining the other components in the bowl, its glistening stream signifying the merging of separate elements to create a cohesive whole. This progression from anticipation to action reflects a common, yet pivotal moment in cooking, where the precise addition of an ingredient can alter the character of a dish.

#### Sample 63 — Transition

- Similarity: 0.4302
- Prediction: Over the course of these three frames, there's a clear progression in the state of the cheese. Initially, it's in a state of disarray, with the cheese separating from the rest of the ingredients. As the sequence progresses, the cheese becomes more evenly distributed, indicating that the cheese has been incorporated into the dish. By the final frame, the process is complete, and the cheese is ready to be served.
- Reference: The egg mixture undergoes a visible transformation across these frames. Initially, the egg is in its raw, unaltered state with a distinct separation between yolk and whites. As we progress, the yolk is broken down and the whites begin to merge, with the pepper becoming more integrated. By the final frame, the action of mixing has created a uniform, airy mixture, indicative of a well-mixed scramble or omelette base. This progression reflects the methodical process of preparing eggs for cooking, where the initial stage of distinct components gradually evolves into a single, smooth preparation ready for the pan.

#### Sample 72 — Transition

- Similarity: 0.4932
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the bowl. Initially, it's in a state of disarray, with no visible signs of activity. As the frames progress, the bowl's surface becomes more cluttered, indicating a more active action. By the final frame, it appears to be in an active state, with the bowl now partially emptied and ready to be used.
- Reference: The progression of the saucepan lid across these frames indicates a sequence of drying or clearing away after washing. Initially seen in a controlled grip, the lid is subjected to a brisk motion, as denoted by the blur, suggesting a shake to remove excess water. Subsequently, the lid is lowered, closer to the countertop, which may indicate the final stage of the drying process before the lid is put away. Throughout this progression, the person’s hands remain protected by the cloth, signifying the careful handling of the potentially wet or hot lid. The movement from frame to frame captures the fluidity and routine nature of kitchen chores.

#### Sample 73 — Transition

- Similarity: 0.4930
- Prediction: Over the course of these three frames, there's a clear progression in the cleaning process of the pan. Initially, the pan is in a state of disarray, with no visible signs of soap or water. As the frames progress, the person's hands are engaged in rinsing the pan, indicating a thorough cleaning. By the final frame, there is a noticeable reduction in the amount of soap and water on the pan's surface, suggesting a more gradual cleaning process. The consistency of the sponge's appearance throughout the frames suggests a
- Reference: Observing the grid across these frames shows a clear progression in its manipulation. Initially held at an angle, the grid is being adjusted, moved, or possibly cleaned. From the slanted hold, it transitions to a more balanced position, with both hands engaging to steady it. The final position is more settled, with a horizontal alignment that indicates a deliberate placement within the sink. Throughout this sequence, the presence of water droplets evolves from sparse to more dispersed, suggesting the grid has undergone a cleaning or rinsing process, with the hands' movements causing water to spread across its metallic surface.

#### Sample 74 — Transition

- Similarity: 0.4640
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the rice. Initially, it's in a state of disarray, with no visible or visible debris. As the sequence progresses, the rice becomes more and more agitated, indicating that it has been removed from the bowl. By the final frame, the spoon's movements become more deliberate, suggesting that the rice has been placed on top of the bowl, possibly to serve as a pretext for preparing the meal. This progression is indicative of a thorough cleaning process, with a focus on the rice's cleanliness throughout the course.
- Reference: Over the course of the three frames, the scale is systematically repositioned on the countertop, moving from the right-hand side towards the center, and then overlapping with the notebook to the left. The scale remains unused throughout, as indicated by the absence of a lit display or visible digits, implying a pre-weighing stage. The person's hands suggest a methodical process of setting up, first clearing the space and then positioning the scale for optimal use. This sequence of movements reflects a deliberate preparation for the accurate measurement of ingredients, a critical step in the culinary process.

#### Sample 86 — Transition

- Similarity: 0.2920
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the freezer. Initially, the freezer's contents are visible, but as the sequence progresses, they become increasingly blurred, indicating that the freezer is being used. By the final frame, there is a noticeable shift in the direction of the food's movement, implying that it's being withdrawn from the container. This progression is indicative of the process of preparing the freezer for use.
- Reference: The leek, originally in a state of transition from bag to counter, has undergone a rapid and unscheduled descent to the floor. Initially held in a stable position, it has slipped from the person’s grasp, flipping end over end as it falls. The stages of its fall are marked by the increasing disarray of the plastic wrap and the blurring of its leaves, telling a story of motion and gravity at work. This sequence captures the leek's accidental journey from control to chaos, each frame depicting a further stage of its unintended flight towards the floor.

#### Sample 89 — Transition

- Similarity: 0.3907
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the oven. Initially, the oven's light is dim, but as the frame progresses, it becomes more visible. By the third frame, the light is less visible, and the oven is now almost fully open. This progression suggests a gradual change in the oven setting, indicating that the oven has been switched on or off.
- Reference: Throughout the progression of the three frames, the squash container undergoes subtle shifts in positioning. Initially, it stands upright in the first frame with the cap removed. As we transition to the second frame, a minor tilt or movement is evident, though the cap's position remains unchanged. By the third frame, the container seems to stabilize, reflecting a similar state as observed in the second frame. Throughout this progression, the container remains unsealed, implying a continuous phase of usage or preparation for consumption.

#### Sample 91 — Transition

- Similarity: 0.4343
- Prediction: Over the course of these three frames, there's a noticeable progression in the cleaning process of a can
- Reference: Over the course of these frames, the burner cap undergoes a noticeable transformation from being passively soaked to actively rinsed and then scrubbed. Initially resting among other components, it transitions to a focal point of cleaning under running water. The hands that once held it loosely now engage in a deliberate scrubbing action, indicating an escalation in the cleaning intensity. The cap's journey from a static state in murky waters to a dynamic cleaning under clear running water signifies a progressive effort to restore its cleanliness and shine.

#### Sample 100 — Transition

- Similarity: 0.4645
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the refrigerator. Initially, it's partially open, with no noticeable change in its state of being. As the frames progress, the fridge's surface becomes more exposed, indicating a gradual change in the shape of the fridge. By the final frame, the refrigerator is almost completely closed, with only a slight shift in its shape. This progression is indicative of a rapid and deliberate action, with the refrigerator's state becoming increasingly blurred.
- Reference: Progressing through the frames, there is a clear transition from a well-lit space to one shrouded in darkness. Initially, the light bathes the room, highlighting textures and surfaces with its bright presence. As the sequence progresses, the light diminishes rapidly, giving way to creeping shadows that transform the room's atmosphere. The final state is one of complete darkness, a stark contrast to the initial frame, indicating that the light source has been effectively extinguished, capturing the essence of a room at rest after the light is turned off. The progression not only alters the visual aspects of the space but also suggests a change in ambience from the lively brightness of an active kitchen to the tranquil dimness of the same space at rest.

#### Sample 110 — Transition

- Similarity: 0.3791
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the oven miter. Initially, it's in a state of disarray, with no visible signs of activity. As the frames progress, the hand's movements become more deliberate, indicating that the miter is being moved. By the final frame, the glove's position becomes more relaxed, suggesting that the hand is moving more quickly. This progression is indicative of a gradual change in the oven's temperature, implying a shift in the direction of the kitchen setting.
- Reference: The chair undergoes a transition from being partially tucked under the table to being pulled out and away from it. The shift in its shadow and the changing perspective of the chair's legs and seat in relation to the surrounding objects, like the table and the floor tiles, indicate the motion. Throughout the frames, the chair's position relative to the fixed elements in the room, such as the table and stove, highlights the trajectory of movement. The consistent lighting across the frames accentuates the changing angles and positions of the chair, marking the progress of its movement within the space.

#### Sample 112 — Transition

- Similarity: 0.4699
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the box. Initially, it's in a state of disarray, with the box's contents visible. As the sequence progresses, the person's hand moves closer to the box, indicating that the action is complete. By the final frame, the box appears to be fully open, with its contents concealed. The hand's movements are consistent throughout the sequence, suggesting a deliberate action, likely aimed at removing the box from its state.
- Reference: The sequence of images depicts the progression of sealing a bag of coffee. Initially caught in a blur, the bag’s interaction with the hands becomes the focus. Starting from being grasped and maneuvered for closure, the bag then undergoes the precise action of sealing, with the hands pinching and rolling its top. By the final frame, the bag is nearly sealed, showcasing a meticulous effort to maintain the coffee's aroma and quality. Throughout these frames, the bag transitions from being an object at rest to one being secured for storage, all within the context of a domestic kitchen setting.

#### Sample 119 — Transition

- Similarity: 0.4409
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the funnel. Initially, it's being rinsed with soap and water. As the sequence progresses, the water's flow becomes more concentrated, indicating a more thorough cleaning. By the final frame, the squeegee's position is more relaxed, suggesting that the rinsing process is complete. The consistency of the water, the hand's grip, and the constant movement of the spoon are indicative of a thorough cleaning process.
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

- Similarity: 0.4854
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the sink. Initially, it's in a state of disrepair, with no visible signs of action. As the frames progress, the sink appears to be in an active state, indicating a change in the water level. By the final frame, it appears to have been agitated, suggesting that the water has been withdrawn from the sink, implying that the sink is now fully emptied. Throughout the sequence, the kitchen appears to undergo a transformation, with the sink becoming more visible and the sink's surface progressively deteriorating.
- Reference: The hand demonstrates a progression of motion associated with thorough hand-washing. Initially, the hand engages with the water, likely activating soap and starting to cleanse. As the frames progress, the hand's movements become more pronounced, suggesting a vigorous scrubbing action, pivotal for effective cleaning. By the final frame, the hand moves away from the water source, indicating the rinse phase is concluding. Throughout the sequence, the motion blur and changing position of the hand relative to the sink and the surrounding environment narrate a common but critical personal hygiene practice. The hand's journey from initial immersion to final withdrawal signifies the near completion of the cleansing process.

#### Sample 127 — Transition

- Similarity: 0.4647
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the cloth. Initially, it's in a state of disarray, with no visible signs of water or soap present. As the frames progress, the cloth becomes more agitated, indicating that the water has been drained out. By the final frame, it appears to be fully soaked, with a clear layer of water on the cloth's surface. This transition is indicative of the process of rinsing the cloth,
- Reference: The sequence of the frames captures the transition of the tap from being fully open to completely shut off. Initially, with the handle raised, a steady stream of water flows into the sink. As the handle is lowered, the water flow diminishes significantly, showing the direct correlation between handle position and water flow. Finally, with the handle laid flat against the sink, the water ceases to flow, signaling the tap's closure. Throughout this progression, the changing water dynamics—from turbulent to tranquil—visually narrate the tap's journey from activity to rest.

#### Sample 131 — Transition

- Similarity: 0.2343
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the rag. Initially, it's in a state of disrepair, with no visible signs of wear or damage. As the frames progress, the cloth's surface becomes more exposed, indicating a thorough cleaning process. By the final frame, it appears to have been fully soaked and ready to be washed. The consistency of the cloth remains consistent throughout the drying process, suggesting a gradual change in the drying state.
- Reference: The sequence of images captures the motion of a yellow, square-cutout grid being manipulated by a person's hand above a kitchen sink. Initially, the grid is held vertically, as if it were being lifted or turned. Progressing through the frames, the grip and orientation of the grid change, indicating a rotation or flipping motion. By the final frame, the grid is nearly horizontal and appears to be carefully positioned towards the sink, which suggests it is being placed within or aligned with the sink for a purpose, such as drying dishes or protecting the sink's surface. The movement is smooth and deliberate, reflecting the person's intent to adjust the grid's position within the domestic context.

#### Sample 135 — Transition

- Similarity: 0.4921
- Prediction: Over the course of these three frames, there's a noticeable progression in the handling of a cutting board. Initially, it's being rinsed with soap and water, with a focus on removing any remaining dirt or debris. As the frames progress, the hand's grip changes to a more gentle angle, ensuring that the cutting board is fully rinsed. By the final frame, the person's hands are engaged in rinsing the board, indicating a thorough cleaning of the board. The consistency of the water's flow and the presence of the soapy water suggest a methodical approach to cleaning the board's surface.
- Reference: Throughout these frames, the spatula undergoes a visible transition from being actively rinsed to being prepped for drying. Initially, it is thoroughly soaked, positioned to maximize the water’s contact with its surface, ensuring a comprehensive cleanse. As it is repositioned and lifted away, the water’s grip lessens, leaving behind a pattern of droplets that reveals the spatula's design and structure. By the final frame, the spatula is almost ready to be dried, with water no longer being actively applied, signifying the near end of the washing process. The changing angle and position of the spatula in relation to the water flow demonstrate a deliberate and methodical approach to rinsing the utensil.

#### Sample 142 — Transition

- Similarity: 0.4404
- Prediction: Over the course of these three frames, there's a clear progression in the state of the pot. Initially, it's in a state of disarray, with the lid partially open. As the sequence progresses, the person's hand moves closer to the pot, indicating that the lid has been removed. By the final frame, the lid is fully open, and the person is able to remove the lid. This sequence captures the action of removing the lid from the pot as well as the process of preparing the pot for cooking.
- Reference: Throughout these three frames, the exact state of the sausage remains ambiguous due to its concealed nature. Initially, various items around the countertop might be obscuring the view of the sausage. As the frames progress, there is a recurring theme of the hands' interaction with the plate, hinting that the sausage could be under it. The movement and possible actions related to the sausage indicate a transition from a potentially exposed state to a covered or relocated state, although its exact position and condition remain a mystery within the presented frames.

#### Sample 145 — Transition

- Similarity: 0.2621
- Prediction: Over the course of these frames, the banana undergoes a transformation from a whole avocado to a partially sliced piece of fruit. Initially, it's untouched, but as the frame progresses, it becomes more and more fully sliced. As the frames progress, the avocado's surface becomes more exposed, revealing a layer of flesh, indicating that the avocado has been thoroughly sliced and is ready to be served. By the final frame, there's an apparent change in the banana's state, with the skin separating from the avocado, suggesting a gradual process of slicing.
- Reference: From its initial resting state atop the cutting board, the pitta undergoes a transformation through human interaction. Initially displayed in its full, untouched form, it's then gently grasped, indicating the commencement of an action. As we progress to the final frame, the piece of pitta's purpose is revealed: to be a medium for the hummus. Its partial submersion in the creamy dip not only alters its appearance, with one end now glistening and coated, but also its texture, absorbing the hummus and becoming a delightful blend of soft bread and rich, flavorful dip.

#### Sample 146 — Transition

- Similarity: 0.4798
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the pot. Initially, it's in a state of disarray, with the pot still partially open. As the sequence progresses, the pot's surface becomes more exposed, indicating a gradual change in its position. By the final frame, the lid's position is blurred, suggesting that the pot has been removed from the burner. This progression is indicative of a rapid change in the pot, which is likely a result of the cooking process.
- Reference: The tupperware's journey across these frames suggests a dynamic kitchen environment. Initially, it appears freshly used or ready for use, resting beside plates. As the frames progress, the tupperware is in motion, indicating it is being actively handled, likely by someone tidying up or organizing the space. The movement from one side of the frame to the center, and finally towards the edge of the counter, tells a story of changing kitchen states—from preparation or unpacking to the conclusion of an activity, where the tupperware is set aside, possibly to be stored or filled with leftovers. The absence of the lid throughout suggests a temporary status, as if its use is not yet fully completed.

#### Sample 150 — Transition

- Similarity: 0.3881
- Prediction: Over the course of these three frames, there's a clear progression in the state of the kettle. Initially, it's in a state of disarray, with the kettle's lid positioned in the middle of the room. As the frames progress, the kettle appears to be fully withdrawn, indicating that the kettle has been placed in the correct position. By the final frame, however, there is a noticeable shift in the angle of the hand's grip, suggesting a gradual change in the position of the handle. This progression is indicative of a person's intent on preparing the kettle for cooking.
- Reference: Over the course of these three frames, the spice undergoes a transformation from a passive and partly concealed item within a cluttered cupboard to an object of focus and interaction. Initially nestled among various kitchen items, its importance becomes apparent as other objects are moved aside, allowing it clearer visibility. As the frames progress, the intention of interaction becomes clearer, culminating in the hand's direct contact and the spice's removal from its resting place, indicating its imminent use or inspection in the kitchen's activities.

#### Sample 153 — Transition

- Similarity: 0.4562
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the counter. Initially, the counter is in a state of disrepair, with no visible signs of wear or discoloration. As the frames progress, there is a clear transition in the cleaning process, with the person focusing on the counter's surface. By the final frame, there appears to be a gradual change in the cleanliness of the countertop, indicating a more thorough cleaning. The consistent movement of the hand, from the beginning to the end, is indicative of a thorough cleaning process.
- Reference: The sequence of images captures a dynamic progression: starting with the pepper mill in a state of uncontrolled descent, then being caught and held firmly, and finally being moved purposefully to a new location or state. The action begins with a state of disorder, indicated by the pepper mill's tilt and the hurried hand movements, then transitions to a controlled grasp that corrects the mill's trajectory, and culminates in a deliberate and controlled motion, likely to reposition the mill. This progression showcases a quick response to an unexpected situation, leading to the stabilization and purposeful handling of the kitchen utensil.

#### Sample 154 — Transition

- Similarity: 0.4978
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the tomato. Initially, it's in a state of disarray, but as the frames progress, the tomato's contents become more visible. As the camera progresses, the person's interaction with the tomato becomes more visible, indicating that the action is ongoing. By the final frame, the lid is removed from the tomato, suggesting that the container has been removed from its packaging.
- Reference: The sequence of images captures the dynamic motion of the jar, which is being vigorously shaken by a pair of hands. Initially, the jar is caught in a swift, twisting movement, blurring the contents within. As the motion progresses, the jar appears to be momentarily steadied in the second frame, possibly at the peak of the shaking cycle. In the third frame, the jar is in the midst of another shake, tilted at an angle, with the hands repositioning for continued motion. Throughout the sequence, the jar's contents are consistently blurred, indicating that the shaking is thorough and vigorous.

#### Sample 158 — Transition

- Similarity: 0.3281
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the bowl. Initially, it's in a state of disarray, but as the frames progress, the bowl's position becomes more apparent. By the final frame, it appears to have been repositioned, indicating that the bowl has been moved away from the table. This progression is indicative of a person's interaction with the bowl, which is likely a part of their daily routine.
- Reference: From a position of rest, the orange has been subjected to an external force, setting it into motion across the table. The transition in its state is evident through the progressive distortion of details on its skin and the shift in reflected light. As it traverses the wooden expanse, it not only changes its position but also its interaction with the ambient environment, exemplified by varying highlights and shadows. This journey from stillness to movement showcases the orange's transient and dynamic nature when acted upon.

#### Sample 162 — Transition

- Similarity: 0.4546
- Prediction: Over the progression of these three frames, the jar undergoes a clear transition from a static state to a dynamic one. Initially, it's resting on a table, but as it moves closer to the table, it becomes more and more agitated. As the frame progresses, the hand's movements become more deliberate, indicating a shift in the direction of the action. By the final frame, the person's motions become more pronounced, suggesting that they are engaged in a deliberate action. This sequence captures the moment when a person engages in an action, implying a particular action or setting.
- Reference: The sequence of images documents the progression of a task focused on the blue plastic measuring jug. Initially obscured by a black mug and other kitchen items, the jug is then identified and retrieved, indicating its selection from among the assorted kitchenware. The transition from resting amidst dishes to being purposefully held signals a shift from storage to active use. This progression underscores a moment in the routine of kitchen work, where tools are chosen and prepared for a specific culinary task, reflecting both the organization of the space and the intention of the user.

#### Sample 163 — Transition

- Similarity: 0.4427
- Prediction: Over the progression of these three frames, the glove undergoes a clear transition from a state of rest to an activity. Initially, it's in a position of rest, but as it moves closer to the surface, the person's movements become more pronounced. As the frames progress, the gloves become more engaged in their action, indicating that they're ready to be used. By the final frame, they've become more relaxed, and the glove's grip becomes more firm, suggesting that the person is preparing to use it.
- Reference: Starting from a mostly folded or bunched state, the tablecloth undergoes a transformation as it's progressively unfurled across the frames. The sense of motion and activity is evident, with the cloth moving from being largely concentrated in one area to spreading out, covering more of the surrounding environment. By the third frame, the tablecloth's placement seems almost finalized, with reduced movement and a more settled appearance, indicating the nearing completion of the unfolding and setting process.

#### Sample 166 — Transition

- Similarity: 0.3803
- Prediction: Over the course of these three frames, the cloth undergoes a noticeable change in its state of being. Initially, it's in a state of disrepair, with no visible signs of wear or degradation. As the frames progress, it becomes more and more agitated, indicating that the cloth has been thoroughly washed and dried. By the final frame, it appears to have been fully soaked, with the cloth's surface exposed, suggesting that there is a significant amount of moisture present. The transition from a static state to a more active state is indicative of a thorough cleaning process.
- Reference: The sequence of images captures a clear progression in the interaction between the person and the bottle. Initially, the bottle is at rest with an open cap. As the frames advance, the person's hand engages with the bottle, specifically the cap, moving from touching to turning. The cap transitions from a state of being unsecured to one where it is being tightened. This motion is consistent with the typical method of closing a bottle, and the person's grip and wrist movement indicate a deliberate action to seal the bottle, likely concluding the task at hand.

#### Sample 170 — Transition

- Similarity: 0.4099
- Prediction: Over the course of these frames, there's a noticeable progression in the state of the chicken. Initially, it's in a state of disarray, with no visible signs of cooking. As the final frame progresses, the chicken is agitated, indicating that it has been removed from the pan. By the third frame, it appears to have been removed, with the chicken still in the pan, ready to be served. The hand's movements are evident throughout the sequence, suggesting that the chicken has been thoroughly cleaned and is ready for use.
- Reference: Over the course of the three frames, the pepper's state transitions from being actively dispensed to resting on the tomatoes. Initially, the pepper is in motion, captured as it leaves the shaker and begins to settle on the tomato slices. By the second frame, the application of the pepper appears to have reached its peak, with visible grains dotting the surface of the tomatoes. In the final frame, the action of seasoning is complete, and the pepper has ceased its trajectory, now lying static on the tomatoes. The sequence captures the essence of seasoning - a momentary action that changes the state of both the ingredient and the final dish.

#### Sample 176 — Transition

- Similarity: 0.4114
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the grater. Initially, it's being rinsed with water, and then rinsing. As the frames progress, the water is agitated, indicating that the rag has been thoroughly rinsed. By the final frame, the ratchet's position changes to a more streamlined position, and the water's flow becomes more concentrated, ensuring that there is no residue left behind.
- Reference: Over the sequence of images, the utensils being rinsed transition from a knife, to a brush, to a spoon, reflecting a progression in the cleaning process. The knife, with its pointed tip and elongated shape, is first to undergo the rinse, likely following a scrub to remove any food remnants. Next, the brush appears, its bristles undergoing what appears to be a thorough rinse, perhaps after being used to scrub other dishes or utensils. Finally, the spoon is held delicately and purposefully under the water, ensuring a complete rinse. This progression not only shows a variety of kitchen tools being cleaned but also suggests a methodical and systematic approach to the task, moving from one type of utensil to the next, each requiring a different handling technique to achieve optimal cleanliness.

#### Sample 180 — Transition

- Similarity: 0.4952
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the cheese. Initially, it's in a state of disarray, with the cheese separating from the other ingredients. As the frames progress, the cheese becomes more evenly distributed, indicating that the cheese has been properly incorporated into the dish. By the final frame, however, there is no discernible change in the cheese's state, implying that it has been removed from the dish and replaced with a smoother, more uniform texture.
- Reference: The progression of the tomato sauce's state from the first frame to the last indicates a process of manual spreading with a spoon. Initially, the sauce is concentrated in the center with an unrefined application. As we progress, the sauce is spread outwards, with the spoon's path creating a swirl pattern that becomes more complex and expansive. By the final frame, the sauce covers most of the flatbread's surface, the chunks of tomato are more dispersed, and the spoon has been set aside, signaling the end of this phase of food preparation. The transformation is from a concentrated dollop to a widely spread layer, ready for additional toppings and further preparation steps.

#### Sample 182 — Transition

- Similarity: 0.3699
- Prediction: Over the course of these three frames, there's a clear progression in the state of the oven. Initially, it's in a state of disarray, with no visible signs of activity. As the sequence progresses, the oven's surface is blurred, indicating a lack of movement. By the final frame, it appears to have been swept away, and the person's actions seem to have taken a positive turn. This progression suggests a change in the oven setting, which is likely a result of a cleaning action.
- Reference: The series of images collectively narrate the progression of a laundry routine. Initially, the preparatory action of dispensing detergent is suggested, though the actual liquid is not seen, possibly due to the timing of the snapshot. As the sequence advances, there is an interlude marked by a lone sock on the floor, which points to a common mishap during laundry tasks. The final frame resolves into the act of removing the clothes from the washing machine, indicating the completion of the washing cycle. The clothes' journey from being washed to being ready for drying is depicted subtly through these snapshots, highlighting the ordinary yet essential chore of laundry management.

#### Sample 187 — Transition

- Similarity: 0.4318
- Prediction: Over the course of these three frames, there's a clear progression in the handling of the pot. Initially, it's in a state of rest, but as the frames progress, the pot's surface becomes more exposed, indicating that the pot is being handled. As the frames move forward, the lid's position changes, suggesting that the lid has been removed from the pot, possibly to prevent the pot from being used. By the final frame, however, the container's state is blurred, with the lid still firmly placed on the pot and the pot still visible. Throughout the sequence, the process of handling the pot evolves into a
- Reference: The chicken has undergone a minimal change in state across these frames, primarily being the person's interaction with it. Initially, it is presented as having been recently sliced, with no further processing. Subsequently, there is a transition to hand washing, which indicates the chicken handling is momentarily paused. Finally, the person dries their hands, preparing to resume interaction with the chicken. The chicken's state remains constant as a raw, roughly cut ingredient, awaiting further preparation such as seasoning or cooking. Throughout these frames, the focus is not so much on the transformation of the chicken itself, but rather on the hygienic practices surrounding its preparation.

#### Sample 189 — Transition

- Similarity: 0.4830
- Prediction: Over the course of these frames, there's a noticeable progression in the state of the cheese. Initially, the cheese is untouched, but as the hands move closer to the cheese, the knife's action becomes more deliberate. As the knife is used to cut the cheese into pieces, it becomes more pronounced, indicating that the cheese has been sliced. By the final frame, there is a clear transition in the cheese's state, with the knife separating the cheese from the slices, highlighting the process of preparing the cheese for cooking.
- Reference: Over the course of the three frames, the cake sees a gradual decrease in its volume, as slices are methodically cut from it. Starting with a single slice removed, the cake then has additional portions taken away, revealing more of its rich and moist interior with each cut. The crumbly texture of the cake's surface remains a constant, as does the contrast between its golden-brown topping and its darker core. The changes across the frames tell a story of a delicious treat being enjoyed slice by slice.

#### Sample 192 — Transition

- Similarity: 0.4774
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the oven. Initially, the oven is in a state of disrepair. As the frames progress, the person's interaction with the oven becomes more visible, indicating that the oven has been fully cooled. By the third frame, the hand is engaged in the action of removing the oven from its position, implying that the door has been partially opened. This progression suggests a gradual change in the oven's settings, suggesting that there is a significant shift in the kitchen's setting.
- Reference: Across the sequence of frames, the microwave's role evolves subtly yet remains central to the narrative of meal preparation. Initially, it stands by, seemingly awaiting activation, which is anticipated by the user's poised hand. The narrative then diverts temporarily to a parallel task—the making of a pancake—before returning to the microwave, where the lack of active engagement implies a pause in its use. Throughout this progression, the microwave remains a silent participant in the kitchen's morning routine, its state of readiness a constant amidst the flurry of culinary activity.

#### Sample 203 — Transition

- Similarity: 0.4807
- Prediction: Over the course of these three frames, the bottle undergoes a clear transition from a state of rest to a moment of action. Initially, it is resting in a position where it can be easily accessed. As the sequence progresses, it becomes more and more agitated, indicating a gradual movement of the bottle. By the final frame, the lid is removed from the bottle, and the bottle's contents are retrieved. Throughout the sequence, the container's state is blurred, suggesting that the bottle may have been placed in an appropriate position. This sequence captures the progression of a bottle
- Reference: Throughout the three frames, the squash undergoes a subtle yet noticeable transition. Initially, it is cradled gently, indicating either a preliminary check for quality or the beginning of a motion to move it. As the frames progress, the hand’s grip shifts, reflecting a change in position or the intent to use the squash. The steady elevation and increasingly secure grip suggest that the person is preparing to place the squash into a cooking vessel or onto a cutting surface, with the movement executed with care to keep the squash intact. The sequence captures a deliberate and attentive handling, characteristic of someone who is possibly experienced in food preparation or mindful of preserving the vegetable’s condition for cooking.

#### Sample 210 — Transition

- Similarity: 0.4895
- Prediction: Over the course of these three frames, the chopping board undergoes a noticeable transformation. Initially, it's in a state of disarray, with no visible or visible debris. As the frame progresses, the board's surface is progressively sanitized, indicating a thorough cleaning. By the final frame, it appears to have been thoroughly washed away, with only a few drops of soap and water remaining. The consistency of the board is consistent with the cleaning process, highlighting a methodical approach to preparing the board for scrubbing.
- Reference: Observing the sequence of images, the soap transitions from being moderately lathered to heavily frothed with suds, and then back to a less sudsy state. This progression indicates a thorough washing process, with the soap being scrubbed, lathered, and finally rinsed. Throughout the frames, the soap diminishes slightly in size due to the abrasion against the cutting board. The suds' lifecycle—from creation to dissolution—parallels the soap's usage, reflecting a dynamic cleaning process. The person’s hands adapt their hold and motion to facilitate the soap's effective application, suggesting an attentive and methodical approach to the task.

#### Sample 211 — Transition

- Similarity: 0.4636
- Prediction: Over the progression of these frames, the cloth undergoes a noticeable transformation. Initially, it's in a state of disarray, with no visible signs of water or soap. As the frame progresses, it becomes more and more agitated, indicating that there's been a change in the water's state. By the final frame, it appears to be more hydrated, with less water and less soap on the cloth, suggesting that the water has been absorbed into the cloth. The cloth's transition from a wet state to a dry state is indicative of a thorough cleaning process.
- Reference: The progression of the sink's state from the first to the third frame narrates a short story of kitchen clean-up. Initially, we see the sink area with splashes of water and a single piece of vegetable debris, hinting at prior use. As time progresses, there's evidence of active cleaning—the presence of water streaks, and cleaning implements suggest the person is midway through the task. By the third frame, the cleaning appears nearly complete; the sink is wetter, the debris has been removed, and the person's hands are together in a gesture that often signifies a job well done. Throughout these frames, the state of the sink transitions from used and in need of attention to clean and orderly, reflecting the mindful efforts of the individual tending to the kitchen's cleanliness.

#### Sample 215 — Transition

- Similarity: 0.3232
- Prediction: Throughout the progression of these frames, there is a clear progression in the state of the fish. Initially, the fish is in a state of disarray, with no visible signs of internalization. As the process progresses, it becomes more and more difficult to remove the fish's skin, indicating that the fish has been thoroughly rinsed. By the final frame, the process is complete, with the fish being removed from the skin and the skin still present. This progression is indicative of the methodical nature of the fishing process, which is characterized by the use of a variety of tools and techniques.
- Reference: The progression of the chicken thigh from its initial whole state to being shredded is evident through the sequence of frames. Initially, the thigh appears untouched and plump, sitting on a plate. As the hands begin to work on it, the meat's structure starts to break down, with strands becoming visible and the skin stretching to accommodate the pulling motion. By the last frame, the thigh is no longer a single piece but a collection of stringy, uneven chunks of meat, demonstrating the physical change that occurs when chicken is shredded manually. This process is critical in culinary preparations where the texture and increased surface area of shredded chicken allow for better absorption of flavors and integration into dishes.

#### Sample 225 — Transition

- Similarity: 0.3950
- Prediction: Over the course of these three frames, there's a clear progression in the use of a blender. Initially, the user's hand is resting on the blender's lid, indicating that the blender is about to turn on. As the frames progress, the hand's grip becomes more relaxed, suggesting a gradual change in the action of the blender. By the final frame, the blender appears to be fully engaged and ready for use. The consistency of the blend remains consistent throughout the sequence, with the user still holding the blender in one hand and the blender still in motion.
- Reference: The mixture undergoes a noticeable transformation through the frames. Initially, it starts with a lumpy and uneven texture, a common state before ingredients are fully mixed. As the blending proceeds, there's a clear transition from this coarse start to a smoother consistency. By the end, the mixture evolves into a homogenous, airy, and glossy batter, reflecting the thorough integration of all ingredients. This progression is typical for mixtures where air incorporation is essential, often seen in recipes for cakes, muffins, or other baked goods, where aeration contributes to a light and tender final product.
Frame_1:
The mixture presents a vivid yellow hue, likely indicative of egg-based ingredients, with visible streaks of white and patches of different consistencies, suggesting the initial incorporation of ingredients. There is a discernible unevenness, with some areas appearing more liquid and others showing soft peaks, possibly from an uneven mixing speed or the starting phase of ingredient integration. The surface reveals air bubbles being folded into the blend, a sign of the mechanical action from the beaters beginning to aerate the mixture.

Frame_2:
There is a notable reduction in the streaking of the mixture, indicating a progression toward uniformity. The color is now more consistent throughout, without the distinct white areas seen previously, implying a better combination of ingredients. The texture is creamier, and the previous soft peaks have started to settle into a more cohesive batter. The beaters are well-coated, and the mixture exhibits a sheen, suggesting the development of a silky structure, characteristic of a well-emulsified blend.

Frame_3:
The mixture has reached a homogenously creamy state with a uniform yellow coloration and a smooth, glossy finish, consistent with a well-blended batter. The surface is free of any lumps or unincorporated patches, and the mixture now holds a ribbon-like trail from the beaters, which indicates good viscosity and structure. The overall volume appears to have increased, and the mixture maintains its shape around the beaters, demonstrating that sufficient air has been incorporated to give it a light, airy texture.

State_change_caption:
Throughout the frames, the mixture evolves significantly. Initially, the mixture is rough and variegated, with distinct colors and textures indicating the beginning of the blending process. As the blending continues, there's a clear progression toward a more homogeneous state, with the texture smoothing out and the color becoming uniform. By the final frame, the mixture has transformed into a creamy, airy, and smooth batter, a sign of proper technique and the readiness for the next step in the recipe. This transformation is critical for achieving the desired end product in baking, where the consistency of the batter can greatly influence the texture and rise of the baked good.

#### Sample 231 — Transition

- Similarity: 0.3802
- Prediction: Over the course of these three frames, there's a clear progression in the state of the onion. Initially, it's partially open, with the onion's skin exposed. As the sequence progresses, the person's hand moves closer to the onion, indicating that the onion has been partially opened. By the final frame, the onion is almost fully open, and the hand's movements are evident. This progression marks the beginning of a transitional phase in the process of preparing the onion for cooking.
- Reference: The plastic bag undergoes a clear transformation across the three frames, starting from a sealed and taut condition to an increasingly open state. Initially, the plastic shows tension and resistance, but as the fingers work to open it, this tension gives way to a more relaxed and malleable form. The opening action results in the gradual revelation of the bag’s contents, changing the plastic’s shape and the distribution of the items inside. The process of opening alters the bag from a closed container to one ready for the retrieval of its contents, with visible changes in the plastic's texture and form.

#### Sample 234 — Transition

- Similarity: 0.3028
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the oven. Initially, it's in a state of disrepair, but as the frames progress, the oven's surface becomes more exposed, indicating that the oven has been removed. As the frame progresses, it becomes more open, with the oven still partially closed. By the final frame, it appears to have been removed, and the oven is now fully open. This progression is indicative of the process of a kitchen
- Reference: The sequence reveals a dynamic transition of the mat from flat and undisturbed to a state of structured order. Initially, only slightly disturbed, the mat soon undergoes a transformation with a crease slicing through its center, manifesting the hand's intent to tidy. As the frames progress, the mat's identity shifts from a mere surface protector to a neatly folded object, its color and texture becoming more pronounced with each turn. This orderly metamorphosis reflects a moment of domestic routine, an ephemeral dance between utility and order captured in a fleeting blur.

#### Sample 235 — Transition

- Similarity: 0.4701
- Prediction: Over the course of these three frames, there's a clear progression in the state of the stovetop. Initially, it's in a state of disarray, with no visible signs of activity. As the frames progress, the kitchen appears to be in re-ordering, with the stove's lid positioned in the middle of the room. By the final frame, the stove appears to have been placed in the center of the kitchen, indicating that the kitchen is ready for cooking. This progression suggests a gradual shift in the kitchen's focus, with a focus on the kitchen and the stove itself.
- Reference: Over the sequence of the three frames, the grater experiences a gradual shift to the right and a rotation that alters its orientation from lying flat on its side to a more angled position with the handle nearest to the camera. The incremental movements imply human interaction, likely a rearrangement to accommodate use or to clear space on the counter. Throughout these transitions, the grater remains clean and unobstructed by food, which indicates that it is in a pre- or post-use state rather than actively being used. The surrounding environment maintains its consistency, with the grater’s movement being the primary change in the domestic kitchen landscape.

#### Sample 236 — Transition

- Similarity: 0.3461
- Prediction: Over the course of these frames, the cheese undergoes a transformation from a pristine state to a state of disintegration. Initially, it is untouched, but as the frames progress, the knife begins to cut through the cheese. As the knife is inserted into the cheese, there is a noticeable change in the cheese's texture and texture. By the final frame, it's almost ready to be sliced, indicating that the cheese has been thoroughly sliced. The knife'
- Reference: Over the course of these frames, the butter transitions from a freshly unwrapped, solid state to a more spreadable consistency as it warms slightly from room temperature and the heat of the hands. Initially, the butter's resistance to spreading creates a rough, textured surface on the bread. As the spreading progresses, the butter starts to give way, becoming more malleable, which is evidenced by the increasing coverage on the bread. The unevenness of the spread throughout suggests a battle against the butter's firmness, a common scenario when butter has not been given time to soften adequately before use.

#### Sample 238 — Transition

- Similarity: 0.3228
- Prediction: Over the course of these three frames, there's a clear progression in the state of the bottle. Initially, the bottle is fully open, with the lid partially closed. As the frames progress, the person's hand moves closer to the bottle, indicating that the bottle has been fully opened. By the final frame, the lid is fully closed, and the bottle's contents are visible. This progression is indicative of the process of preparing the bottle for use.
- Reference: The flour undergoes a dynamic transition across the three frames, starting with a gentle introduction into the bowl, increasing to a swift pour, and culminating in a substantial deposit of flour. The initial light dusting evolves into a significant mound, reflecting the increasing volume and momentum of the pour. The flour's consistency remains constant, fine and powdery, but its behavior changes from a delicate stream to a more forceful waterfall. This progression is marked by the growing cloud of flour dust, the rising mound within the bowl, and the change in the flour's surface from scattered to smooth and peaked. The action captures the careful control yielding to the forces of gravity and volume as the contents of the jar deplete.

#### Sample 240 — Transition

- Similarity: 0.4563
- Prediction: Over the course of these three frames, the rice undergoes a noticeable transformation. Initially, it's in a state of disintegration, but as the stirring progresses, it becomes more and more agitated, indicating that the rice is being stirred. By the final frame, it appears to be fully absorbed, with the water separating the rice from the water. The consistency of the rice remains consistent throughout the sequence, suggesting that the cooking process is a
- Reference: From the first to the third frame, there is a noticeable transformation in the state of the curry. Initially starting as a lighter, broth-like mixture with distinct floating ingredients, it transitions into a denser, more cohesive dish. As the cooking progresses, the liquid content reduces, and the curry takes on a richer hue, signifying the melding of flavors and ingredients. By the third frame, the curry exhibits a thick, integrated consistency, with the ingredients softened and fully incorporated, indicating its near completion in the cooking process.

#### Sample 241 — Transition

- Similarity: 0.4624
- Prediction: Over the course of these three frames, the icing board undergoes a subtle transformation. Initially, it's in a state of disarray, with no visible signs of activity. As the frames progress, it becomes more and more agitated, indicating a more deliberate action. By the final frame, it appears to have been re-engaged, suggesting a gradual change in its position. This progression is indicative of a person's intent to use the board as a tool for cooking.
- Reference: Between the three frames, the primary change involves the red ladle's position as it is manipulated by an unseen diner. Initially, it rests within the white bowl; then, it's in mid-air, indicating a motion of being placed down; and finally, it comes to rest on the white paper plate. The motion is deliberate and careful, ensuring the ladle does not contact other items on the table. Throughout this sequence, the rest of the setting remains static, highlighting the singular action of the ladle being moved after a meal. This action is part of the post-meal cleanup process, as the utensil is being set aside, possibly in preparation for washing.

#### Sample 245 — Transition

- Similarity: 0.4955
- Prediction: Over the progression of these three frames, the sugar undergoes a noticeable transformation. Initially, it's in a state of disarray, with no clear indication of its existence. As time progresses, the spoon's motion becomes more deliberate, indicating that the sugar has been incorporated into the bowl. By the final frame, the stirring is complete, and the spoon is now positioned in the correct position to serve as a serving vessel for the meal.
- Reference: The egg’s state changes visibly across these frames, showcasing the process of blending the yolks and whites together. Initially, the egg lies undisturbed with clear delineation between components. As the fork is introduced and the mixture is agitated, the yolks break apart and the whites begin to cloud with streaks of yellow. With continued whisking, the mixture transitions into an increasingly uniform color, indicating that the ingredients are becoming well integrated. The progression from separation to amalgamation reflects the careful, deliberate action of whisking, preparing the egg for cooking with each stroke of the fork.

#### Sample 248 — Transition

- Similarity: 0.4546
- Prediction: Across the three frames, there's a clear progression in the state of the oven. Initially, the oven's light is dimmed, but as the frame progresses, the light becomes more visible. By the final frame, the door is fully open, indicating that the oven is ready for use. The hand's motions are evident throughout the sequence, suggesting a gradual change in the oven setting. This progression suggests a transition from a closed oven to a fully open oven.
- Reference: The progression of frames shows the hand interacting with a light switch, moving from a state of non-engagement to actively pressing a button. Despite this interaction, the anticipated increase in light within the room is not evident. This suggests a delay or issue in the lighting system or possibly a timing issue with the camera's capture of the event. The consistent shadows across the frames imply that the light source has not changed its intensity or position throughout this sequence.
Frame_1:
The lighting environment is subdued, with a gentle, diffuse glow suggesting an external light source, perhaps natural light filtering in or an artificial light elsewhere in the room. The wall switch with multiple buttons is at rest, and none of the buttons are depressed, signaling an off position for the connected light fixtures. The hand is poised just before engagement with the switch, implying an intent to alter the lighting state. The shadows cast are soft and indicate that the primary light source is not directly overhead but rather coming from a side angle, contributing to the overall muted lighting conditions.

Frame_2:
The hand now interacts with the switch, and a finger is captured in the motion of pressing one of the buttons, which typically would initiate an electrical connection to illuminate a room. However, the lighting in the room remains unchanged, with the ambient light continuing to cast broad, indistinct shadows. This could suggest a momentary lapse between the action of pressing the switch and the activation of the light, or it may be that the light source requires a noticeable duration to reach full brightness.

Frame_3:
After the actuation of the switch, the lighting condition persists as before, with no discernible enhancement in brightness. The switch shows one button engaged, suggesting the circuit is complete and should theoretically result in a lit environment. Yet, the persistent shadowing and the absence of stark contrasts or bright reflections that would accompany an active artificial light source, denote that the anticipated illumination has not occurred, or that the light source is not within the frame's view.

State_change_caption:
The sequence of interactions with the light switch suggests an attempt to modify the lighting condition within the room, moving from inaction to a deliberate act of switching. Despite the physical engagement with the switch, the anticipated transition from dim to bright lighting does not transpire within these frames. The unchanged shadow patterns and the continuity of the ambient light's intensity through the sequence indicate that either the light source has not yet responded to the switch's activation, or the change is too gradual to be discerned in the captured moments.

#### Sample 252 — Transition

- Similarity: 0.4919
- Prediction: Over the sequence of frames, the sandwich undergoes a visible transformation from a state of rest to a pristine state. Initially, it's untouched, but as the frame progresses, the knife's action becomes more deliberate, with the knife slicing through the sandwich's surface. As the frames progress, the bread's texture becomes more uniform, indicating that the knife is engaged in a deliberate action. By the final frame, there is a noticeable change in the sandwich’s appearance, with a crisper, more slick appearance and a more uniformly-shaped surface.
- Reference: The sequence of frames chronicles the progressive serving of a bundt cake. Initially, a single slice is cut and replaced to show that the cake has been sliced into. Subsequently, this slice is removed entirely, leaving behind a void that marks its absence. As the frames advance, another slice is taken, furthering the cake's transition from a complete ring to a more fragmented form. The serving of the cake is methodical, with each slice cleanly cut and removed, suggesting a careful and considerate serving process. Throughout this progression, the visual characteristics of the cake, like its color and texture, remain constant, reinforcing the cake's quality and the uniformity of its baking.

#### Sample 253 — Transition

- Similarity: 0.4120
- Prediction: Over the course of these three frames, the sponge undergoes a noticeable transformation from a state of wilting to a fully saturated state. Initially, it's in a pre-cooking state, with the sponge's surface exposed. As the frames progress, it becomes more fully saturated, indicating that the sponge has been thoroughly soaked. By the final frame, it appears to be fully saturated and ready to be used again. The consistency of the sponge remains consistent throughout the sequence, suggesting a gradual change in its state of being soaked,
- Reference: Throughout the three frames, there's a notable progression in the rag's movement and use. Initially, it's captured mid-motion, actively cleaning, with its wetness prominently displayed. As we progress, the rag's details become more pronounced, hinting at the varying pressure and angles it's being used at. By the third frame, the rag's positioning and the hand's grip indicate a potential shift in cleaning direction or a momentary pause, yet the purpose - cleaning - remains evident. The consistent moisture level across the frames underscores its primary role in this setting.

#### Sample 255 — Transition

- Similarity: 0.4528
- Prediction: Over the progression of these three frames, the microwave undergoes a clear transition from a partially open state to a fully open state. Initially, it appears to be in a state of rest, but as the frame progresses, it becomes more and more agitated, indicating that the microwave has been fully opened. As the frames progress, there is a noticeable change in the microwave's position, suggesting that it has been partially opened. By the final frame, it seems to have been fully closed, with the microwave still partially open. This progression suggests a gradual process of adjusting the microwave to its proper position, possibly to make the microwave more responsive to the user's needs.
- Reference: Across the progression of the three frames, there's a palpable transition in the interaction with the switch. Initially, the hand moves in with intent, hinting at an upcoming action. As the sequence evolves, the hand's position in the subsequent frame indicates a direct interaction with the switch. By the third frame, it becomes evident that the action has been completed, with the switch likely being toggled. The narrative spun by these images tells a story of a deliberate action initiated, executed, and concluded on a switch in a domestic kitchen setting.

#### Sample 256 — Transition

- Similarity: 0.4501
- Prediction: Over the course of the three frames, there's a clear progression in the state of the stovetop. Initially, the stove is in a state of disarray, with no visible signs of cooking or cooking. As the frames progress, there is a noticeable change in the position of the burners, indicating a gradual shift in the direction of the cooking process. By the final frame, there appears to have been a significant shift from a static position to a more active position, suggesting a shift in cooking activity. The consistent lighting throughout the frame suggests a methodical approach to cooking.
- Reference: Over the course of these frames, the state of the grill transitions from untouched to the commencement of an interaction, specifically the removal of one of the grates. The hand, initially poised for action, advances towards the grate, eventually making contact and beginning to lift it from its resting position. This sequence captures the initial phase of what could be a cleaning process or the prelude to maintenance work. The grill itself retains its cleanliness throughout, with no visible debris being disturbed, indicating a careful and precise approach by the individual interacting with it.

#### Sample 258 — Transition

- Similarity: 0.4896
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the peeler. Initially, it's in a state of disarray, with no visible water or debris. As the frame progresses, the person's hands move from one hand to the other, indicating a thorough cleaning process. By the final frame, the peelers are fully rinsed and ready to be rinsed, with the person indicating that they're ready for the next step.
- Reference: The dish undergoes a notable transformation through the three frames, from a dirty, residue-laden state to a nearly fully cleansed condition. Initially presenting stubborn, burnt-on food remnants, the dish receives a thorough scrubbing that gradually reduces the visible residue. The process involves soaking, application of soap, and physical scrubbing, which are effective in loosening and removing the baked-on materials. The progression demonstrates the effectiveness of the cleaning method, with the final frame showing the dish nearly ready for rinsing or a final wash, highlighting the transition from dirty to clean through the stages of manual dishwashing.

#### Sample 267 — Transition

- Similarity: 0.4748
- Prediction: Over the course of these frames, there's a clear progression in the state of the onion. Initially, it's still intact, but by the final frame, the onion has been partially removed. The hand's action is evident, and the onion's surface is exposed, indicating that the onion is ready to be sliced. By the third frame, however, the process is complete, with the onion almost completely removed from the slice, highlighting the action's significance. This progression is indicative of the process of preparing the onion for cooking.
- Reference: The sequence of frames captures the gradual unveiling of the sweetcorn, beginning with its concealed state within a sealed can and transitioning towards its exposure as an ingredient ready for use. Initially, the can sits dormant, the sweetcorn hidden from view, its potential as a pizza topping only implied. The narrative then shifts as the can opener engages, piercing the metal lid and commencing its journey around the rim, revealing more of the sweetcorn with each twist. By the final frame, the transformation is nearly complete, with the sweetcorn almost fully exposed, transitioning from a contained food product to an active participant in the cooking process, its golden kernels ready to join the array of pizza toppings.

#### Sample 269 — Transition

- Similarity: 0.4553
- Prediction: Over the course of these frames, the pak cho
- Reference: Over the course of these three frames, there's a clear progression in the preparation of the choi pak. Starting from the initial stage where only a small portion has been chopped, the vegetable undergoes a methodical breakdown. With each subsequent frame, the quantity of cut choi pak increases, showcasing a steady and systematic approach to the cutting process. By the end, almost all of the choi pak has been transformed into neatly chopped pieces, ready for the next step in the cooking or serving process.

#### Sample 278 — Transition

- Similarity: 0.4456
- Prediction: Over the progression of these frames, the dough undergoes a noticeable transformation. Initially, it's unflattering, but as it becomes more firm, the texture becomes more pronounced. As the frames progress, the rolling action becomes more deliberate, indicating that the dough has been kneaded to a smoother texture. By the final frame, the shape has become more uniform, and the dough's texture has improved.
- Reference: Over the progression of these three frames, the cling film evolves from being mostly contained within its box to being widely spread out and manipulated by the user. Initially, only a small portion is visible, displaying minor wrinkles. As the frames advance, the film is extended more and more, showing an increase in creases and overlaps, likely due to the force of extraction and the manual handling. This transition underscores the film's flexible nature and its responsiveness to human touch and movement.

#### Sample 280 — Transition

- Similarity: 0.4813
- Prediction: Over the course of the three frames, the table undergoes a transformation from a static position to a dynamic one. Initially, it appears to be in a state of disarray, but as the frames progress, it becomes more and more agitated, indicating a shift in the table's position. By the third frame, it's more or less a stationary position, suggesting a change in the direction of the table. The hand's movements are evident throughout the frame, suggesting that the table is in motion, with the person's actions indicating that they are engaged in some sort of action. The consistent movement across the frames
- Reference: Over the course of these three frames, the toaster undergoes a transformation from being an object of focus to becoming a background element in a flurry of activity. The initial frame captures a moment of action centered around the toaster, while the subsequent images document a shift in attention and activity towards other areas of the kitchen. The consistent motion blur throughout the frames suggests a continuous, rapid movement, with the toaster's role diminishing as the scene progresses. This sequence captures the chaotic essence of a moment, likely in the middle of a multitasking kitchen endeavor.

#### Sample 281 — Transition

- Similarity: 0.3966
- Prediction: Over the progression of the three frames, the table undergoes a noticeable transformation. Initially, it's in a state of disarray, with no visible signs of wear or discoloration. As the frames progress, there is a clear shift in the position of the table, indicating a more thorough cleaning. By the final frame, there's an apparent change in the table's position, suggesting a gradual cleaning process. The hand's movements are evident throughout the sequence, suggesting that the table is being thoroughly cleaned,
- Reference: From the initial application of the detergent in a fine mist, there is a transition to spreading and then actively wiping the liquid across the surface. The droplets first seen are no longer distinguishable as individual particles but have merged into streaks and then into a more homogenous layer of moisture. The cleaning action evolves from a gentle application to a more forceful movement, indicating a progression from the distribution of the cleaning agent to the actual cleaning process, with the aim of leaving the surface clean and streak-free. The change in the cloth's appearance, from being relatively dry to becoming damp and heavy with detergent, marks the stages of cleaning.

#### Sample 282 — Transition

- Similarity: 0.3993
- Prediction: Over the course of these frames, there's a clear progression in the state of the garlic clove. Initially, it's mostly intact, but by the third frame, the clove is almost completely removed. By the final frame, however, the skin has been partially removed, indicating that the process has been completed. The process is evident in the subsequent frames, with the clove becoming more and more dispersed, revealing a variety of different parts of the clove. This progression is indicative of the methodical nature of the preparation process, with each frame highlighting a different part of the culinary process.
- Reference: As the sequence progresses, the onion skin undergoes a subtle transformation in response to the hands' movements. Initially laid out loosely on the cutting board, it becomes a secondary participant in the dance of meal prep, its position shifting with each new action. The texture of the skin changes from being slightly pliable and glossy to drier and more curled, echoing the natural progression of being separated from its original form. This progression showcases the interplay between the food preparer and the ingredients, with the onion skin serving as a delicate reminder of the ongoing preparation process.

#### Sample 285 — Transition

- Similarity: 0.3686
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the sieve. Initially, it's in a state of disrepair, with no soap or soap residue. As the sequence progresses, the knife's surface is progressively sanitized, indicating a thorough cleaning. By the final frame, the blade's state is more streamlined, with less soap and less suds, suggesting a more thorough cleaning of the knife. This sequence exemplifies the process of rinsing the knife,
- Reference: Over the course of these three frames, the lemon squeezer transitions from being initially submerged for soaking to being scrubbed and finally rinsed. The progression shows a meticulous cleaning effort, where the hand's grip and movement reflect the different stages of washing—soaking, scrubbing, and rinsing. The squeezer's cleanliness improves visibly, as evidenced by the increased reflection and absence of debris, demonstrating a thorough and effective cleaning process.

#### Sample 288 — Transition

- Similarity: 0.4739
- Prediction: Over the course of these three frames, the frying pan undergoes a noticeable transformation. Initially, it's in a state of disrepair, with no visible food or debris. As the sequence progresses, the pan's surface appears to be scrubbing, indicating a thorough cleaning. By the final frame, there is a visible reduction in the amount of food and debris on the pan, suggesting a more thorough cleaning of the entire surface. The constant movement of the pan from one position to the next shows a clear progression in the cleaning process.
- Reference: Over the sequence of frames, the plate transitions from being actively washed under a vigorous stream to being rinsed in a pool of soapy water, and finally to experiencing a gentle overflow rinse. Initially, the direct impact of the water stream dislodges debris and creates a dynamic interaction with the suds, indicating the initial wash. As the plate is submerged, the suds indicate a soapy bath likely following a scrubbing action. In the final frame, the subtle flow and the clear water in the plate signify the concluding phase of the cleaning process, where the objective is to remove any remaining soap rather than dislodge food particles. The entire sequence reflects a systematic approach to dishwashing, focusing on cleaning efficacy and thorough rinsing.

#### Sample 294 — Transition

- Similarity: 0.4057
- Prediction: Over the course of these three frames, the cooker undergoes a noticeable transformation. Initially, it's in a state of disarray, with no visible signs of cooking. As the frames progress, there is a clear progression in the cleaning process, with a focus on the surface of the cooker's surface. By the final frame, there's an apparent reduction in the amount of soap and water on the cooker, indicating a more thorough cleaning process. The consistency of the cooking surface, as well as the presence of the cleaning agent, are indicative of a methodical cleaning approach.
- Reference: The progression of the towel's state indicates a series of cleaning actions. Initially presented as a recently used but still serviceable item, it then becomes absent from view, presumably set aside for a moment where the cleaning focus shifts to another object. Upon its return, the towel is employed with more intent and vigor, now visibly dirtier, having absorbed more residues from the cleaning surface. This evolution illustrates a typical cleaning process, where a towel is used, evaluated, and reused with increasing intensity until the task is complete or the towel requires laundering.

#### Sample 295 — Transition

- Similarity: 0.4126
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the sieve. Initially, it's in a state of disrepair, with no visible or visible debris. As the frames progress, the siege becomes more and more agitated, indicating a thorough cleaning. By the final frame, it appears to have been sanitized, suggesting that it has been thoroughly washed and is ready to be rinsing. Throughout the sequence, the dish's state of cleanliness is evident, with the hand's emphasis on a clean surface and a clear focus on the cleaning process.
- Reference: The strainer has undergone a visible transformation across the three frames. Initially, it was only being rinsed, with food particles stubbornly clinging to its surface. As the cleaning progressed, the introduction of the blue sponge and detergent facilitated a deeper clean, dislodging and reducing visible debris. In the final frame, the application of the white cloth and a resumption of the water flow indicate a final rinse and wipe-down, leaving the strainer looking refreshed and markedly cleaner. This sequence illustrates a methodical approach to cleaning kitchen utensils, starting with a rinse, followed by scrubbing with a sponge and detergent, and concluding with a thorough wipe and final rinse.

#### Sample 297 — Transition

- Similarity: 0.3857
- Prediction: Over the course of these three frames, the chicken undergoes a clear transformation from a whole chicken to a fully sliced piece of meat. Initially, it's in a state of disintegration, but as the sequence progresses, it becomes more and more fragmented, indicating that the meat has been removed from the chicken. By the final frame, the meat is being sliced into pieces, with the skin still present. The methodical nature of the chicken's preparation suggests that the chicken is being prepared to serve as a meal preparation tool.
- Reference: The progression of these frames shows the process of preparing and cooking garlic. Initially, we see the clove intact, indicating the starting point of the culinary action. As we move to the next frame, the garlic has been crushed into a paste, reflecting the transformation from raw ingredient to a form that can be easily mixed with other components of the dish. Finally, the garlic is transferred into the pan, completing its journey from a solid clove to a cooking element that will infuse the dish with flavor. The careful manipulation of the knife and board by the cook's hands underscores the attention to detail and the methodical approach to incorporating the garlic into the meal.

#### Sample 298 — Transition

- Similarity: 0.4378
- Prediction: Over the course of these three frames, the pan undergoes a visible transformation from a state of rest to a process of cooking. Initially, it's positioned in a position that's being used for cooking. As the frames progress, there is a noticeable change in the pan's position, indicating that the cooking process has been completed. By the final frame, it appears to be fully seated, with the pan still partially drained and ready to be served. The consistent movement of the pan, the constant movement of its surface, and the constant motion of its handling are indicative of a deliberate cooking process.
- Reference: The sequence of images captures the progressive movement of a pair of yellow rubber gloves engaged in kitchen tasks. Initially, the left glove is seen gripping a white bowl, suggesting the commencement of a washing or cleaning action. Moving to the second image, both hands are occupied, with one hand stabilizing a pot and the other in motion, indicative of a multitasking scenario. By the third frame, there's a distinct change, as the gloves are now repositioned to handle a frying pan, suggesting the completion of one task and the beginning of another. Throughout the sequence, the gloves remain taut and appear well-fitted to the user's hands, their bright yellow color standing out against the backdrop of kitchen utensils and appliances. The gloves’ texture and sheen alter slightly with the changing angles and actions, reflecting their flexible and water-resistant nature.

#### Sample 304 — Transition

- Similarity: 0.4096
- Prediction: Over the progression of these three frames, the tupperware undergoes a clear transition from being placed in a sink to being washed. Initially, it's agitated, but as the sequence progresses, it becomes more and more motion-free, indicating a thorough cleaning process. By the final frame, it appears to have been sanitized, suggesting that it has been thoroughly rinsed. This progression is indicative of a
- Reference: The tin's journey through these frames is a visual narrative of restoration. Initially, it stands as a testament to its robust utility, bearing the marks of many uses. As water is introduced, it takes on a dynamic role, actively engaging with the tin to begin a transformation. The water's force is evident in the way it interacts with the seasoned surface, and finally, the tin sits with water pooled within, a temporary reservoir that hints at the potential for renewal. This progression is not just physical but symbolic, echoing the cycle of use, wear, and rejuvenation inherent in the life of a well-loved kitchen implement.

#### Sample 305 — Transition

- Similarity: 0.3172
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the chili. Initially, it's still in a state of disarray, with no visible signs of cooking. As the sequence progresses, the chili becomes more agitated, indicating that it is ready to be served. By the final frame, the chilli has been fully incorporated into the dish, suggesting that the chef is preparing to serve it.
- Reference: As the sequence progresses, there is a clear transition from a static, somewhat disordered countertop to one that is the focus of active tidying. Initially, the countertop appears merely wiped down with residual moisture, then transitions to a state of active cleaning with the person's hands and sponge in motion. By the third frame, the cleanliness is maintained despite the ongoing meal preparation, showcasing the individual's diligence in keeping the space orderly. The consistent presence of the person's hands and the movement of the sponge indicate a methodical cleaning process, maintaining order amidst the culinary activity.

#### Sample 308 — Transition

- Similarity: 0.4799
- Prediction: Over the course of these frames, there's a noticeable progression in the rinsing of the bowl. Initially, the bowl is being rinsed with water. As the sequence progresses, the water's flow becomes more concentrated, indicating a more thorough rinse. By the final frame, it's becoming more and more agitated, with the water sprinkling on the bowl's surface. The consistency of the water, as well as the hand's grip, are indicative of a thorough rinse, ensuring that the bowl will be thoroughly rinsed.
- Reference: The progression of cleaning the baking tray is quite evident across the three frames. Initially, the tray was being rinsed, with the water pressure aimed at dislodging the large particles and debris. Moving on, it was tilted to facilitate the removal of these particles, allowing a more targeted rinse. Finally, the application of soap and active scrubbing suggests a meticulous cleaning process is underway. Throughout these stages, the tray transitions from heavily soiled to being covered in soap suds, which marks the midway point of the washing cycle, leading towards a fully cleaned state. The person's consistent handling and methodical cleaning process indicate an effective and routine approach to dishwashing.

#### Sample 309 — Transition

- Similarity: 0.4575
- Prediction: Over the course of these three frames, the chicken undergoes a clear transformation from a state of being partially soaked in water to being thoroughly rinsed. Initially, there is a noticeable transition from being fully soaked to being fully rinsed, indicating a thorough cleaning process. As the frames progress, it becomes more and more evident that the chicken is being thoroughly washe
- Reference: Over the course of these frames, the tap undergoes a clear transition in its functionality. Initially, it's in a dormant state with no water flow. However, as time progresses, water begins to stream out, and by the third frame, the intensity of this flow has increased substantially. This progression indicates the tap being turned on and adjusted to release water at a faster rate. The entire scene captures the tap's transition from a static state to one of full operation, showcasing the simple yet essential function of such a household fixture.

#### Sample 312 — Transition

- Similarity: 0.4788
- Prediction: Throughout the progression of these frames, the onion undergoes a clear transformation from being untouched to being discarded. Initially, it's still intact, but by the third frame, it has been partially removed, indicating that the onion has been thoroughly cleaned and is ready for use. As the frames progress, the person's actions become more deliberate, suggesting that they are preparing the onion for cooking. By the final frame, there is a noticeable change in the onion's state, with the peeler removing the outer layer of the onion,
- Reference: Throughout the three frames, there is a clear progression in the state of the green beans. Initially, we see the early stages of preparation, with just a few beans trimmed. As time moves forward, more beans are processed and the evidence of work accumulates on the countertop. The person's methodical process of trimming, evident in the consistent size and shape of the beans in the colander, speaks to their attention to detail. The gradual transition from unprepared to prepared beans, along with the increasing number of discarded ends, paints a picture of the ongoing task, with the person's hands in constant motion, refining the vegetables for cooking. The sequence captures the meticulous care taken in preparing the beans, a routine yet intimate part of meal preparation.

#### Sample 315 — Transition

- Similarity: 0.4598
- Prediction: Over the course of these three frames, the onion undergoes a transformation from a whole onion to a fully sliced piece. Initially, it's untouched, but as the sequence progresses, it becomes more and more intertwined with the onion. As the frames progress, the person's actions become more deliberate, indicating that the onion is being prepared for cooking. By the final frame, there is a noticeable change in the onion's state, suggesting a gradual change in its state of preparation.
- Reference: The peeler transitions from a state of rest to active use and back to rest again over the course of these frames. Initially, it is seen with evidence of recent use, marked by the piece of cucumber skin attached to its blade. In the following moment, it is captured in the midst of peeling, with a visible strip of cucumber skin being removed, illustrating its function and the action of the user. Finally, the peeler returns to a stationary position, now clean and reflecting the change in the cucumber's appearance, which now bears a larger peeled area. The progression shows a typical use cycle during a peeling task in a kitchen environment.

#### Sample 320 — Transition

- Similarity: 0.3702
- Prediction: Over the course of these three frames, the chicken undergoes a noticeable transformation. Initially, it is untouched, with no visible signs of cooking. As the frame progresses, the meat begins to become more tender, with the skin separating from the meat. By the final frame, the hands are engaged in the process of removing the meat from the chicken, indicating a gradual change in the meat's state. This progression is indicative of the chicken's preparation for cooking.
- Reference: Over the course of these frames, the sweet potato skin transitions from freshly cut to completely separated. Initially, the skin is freshly peeled, with vibrant colors and moisture that highlight its recent contact with the flesh. As the peeling continues, more of the flesh is exposed, and the skin's texture and color change slightly due to air exposure. In the final frame, there is a substantial amount of peel removed, evidencing the work done, and the skin that remains on the sweet potato shows signs of drying out. The process reflects a meticulous peeling technique aimed at preserving as much of the sweet potato flesh as possible while removing the skin.
Frame_1:
The skin of the sweet potato is mid-peel, with a segment hanging off the edge of the vegetable, poised to be removed. It exhibits a rich, deep orange hue indicative of its freshness and nutritional content. The texture of the recently cut skin appears slightly moist and shiny, contrasting with the dry, matte outer surface. The peeling action has produced a few errant strands of skin that have curled away from the starchy interior, creating a small pile on the edge of the cutting board, which is speckled with moisture and small flecks of the sweet potato flesh.

Frame_2:
The sweet potato now reveals more of its vibrant orange flesh as the skin has been further peeled back. The skin itself is thinner and more fragmented than before, indicative of the peeling process becoming more refined as it progresses. Pieces of the skin are now strewn across the cutting board in a more dispersed pattern, and some have fallen to the stovetop, suggesting a rapid peeling motion. The knife, still held firmly, continues to work closely against the flesh, ensuring minimal wastage of the vegetable, while the brightness of the skin has begun to wane as it dries out.

Frame_3:
Here, the sweet potato skin has been almost entirely removed, with only a small portion left at the tip. The collection of peeled skin has grown substantially, covering a significant area of the cutting board. The skin's color has dulled slightly, losing some of its initial vibrancy as it succumbs to the air's oxidizing effects. The knife and fork are now at rest beside the pile of peelings, and the skin's moisture has visibly reduced, appearing drier and starting to curl at the edges.

State_change_caption:
Observing the state of the sweet potato skin across these frames shows a clear progression in the peeling process. The initial frame displays a just-begun peel with a skin rich in color and moisture. Moving to the next, there is a noticeable increase in the quantity of skin removed, with evidence of technique refinement and speed. By the final frame, the skin has mostly been stripped away, leaving behind a more extensive and drier collection of peelings. The transformation is marked by a gradual loss of moisture and color in the skin, as well as a shift from a few large pieces to many smaller, drier fragments.

#### Sample 328 — Transition

- Similarity: 0.4706
- Prediction: Over the course of these three frames, there's a clear progression in the state of the bag. Initially, the bag is resting on its side, indicating a state of rest. As the sequence progresses, the person's hand moves closer to the bag's side, suggesting a gradual movement. By the final frame, the man's hands are engaged in the process of removing the bag from its upright position, implying a shift in the action. This progression is indicative of a
- Reference: The sequence captures a simple yet ubiquitous kitchen ritual: the toasting of a slice of bread. Initially presented in hand, the bread slice is a static object, yet full of potential. As it is inserted into the toaster, there is a transition from potential to process—the bread begins its transformation. The final frame culminates in the bread's disappearance inside the toaster, a visual cue that the physical state of the bread is changing from soft to toasted, even though the process is hidden from view. This sequence is a snapshot of everyday life, a familiar action paused in time and broken down into the individual steps that lead to the satisfying crunch of a freshly toasted slice of bread.

#### Sample 332 — Transition

- Similarity: 0.4853
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the oven door. Initially, the door is partially open, with the person's hand resting on it. As the frames progress, the oven's surface becomes more exposed, indicating that the oven has been fully opened. By the final frame, there is a noticeable change in the position of the door, suggesting that the door has been partially opened. This progression is indicative of the process of preparing the oven for use.
- Reference: Over the progression of these frames, the freezer drawer transitions from being partially open to fully closed. The motion is rapid, as evidenced by the blurring in the first two frames and the quickly diminishing gap. The closing action seems smooth, with no visible obstructions or misalignment, implying an efficient and possibly habitual motion by the individual. The final frame confirms the cessation of movement, with the drawer securely in place, ensuring the preservation of the freezer's cold environment and its contents.

#### Sample 335 — Transition

- Similarity: 0.2282
- Prediction: Over the progression of these frames, the table undergoes a noticeable transformation. Initially, it's in a state of disarray, with no visible signs of wear or tear. As the frames progress, the person's hands move from one hand to the other, indicating a deliberate action. By the final frame, the hand's movements become more deliberate, suggesting that the table is being rearranged and ready for use. This progression marks a transition from a static state to a more dynamic one, with the hand demonstrating a shift in the direction of the table's movement.
- Reference: Over the course of these frames, the degreaser transitions from a freshly sprayed mist to a settled layer of cleaning agent on the countertop. Initially, the liquid is airborne, caught in the act of being dispensed. As the spray continues, the droplets begin to fall and spread across the surface, moving from a state of suspension to contact. By the final frame, the spray action has stopped, and the degreaser has formed an even layer across the countertop, indicating the completion of the application phase and the beginning of its cleaning action. The progression shows an effective dispersion method, covering the targeted area thoroughly with the cleaning agent.

#### Sample 338 — Transition

- Similarity: 0.3908
- Prediction: Over the course of these three frames, the meat undergoes a noticeable transformation. Initially, it's in a state of disintegration, with no visible signs of cooking or cooking. As time progresses, it becomes more and more pronounced, indicating that the cooking process has been completed. By the final frame, it appears to be fully absorbed, with the meat forming a smooth, charred, and ready to eat.
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

- Similarity: 0.3650
- Prediction: Over the course of these three frames, the chopping board undergoes a visible transformation. Initially, the board is being rinsed with water, indicating a thorough cleaning process. As the frames progress, the water's movement changes to a more gentle action, implying that the board has been sanitized. By the final frame, the hand's motion shifts to rinsing the board, ensuring that there is no residue left on the board.
- Reference: The tablecloth transitions from a static, artistically displayed kitchen item to an object in the midst of washing. Initially laid out with a prominent apple design, it is subjected to a cascade of water, which introduces a new texture and sheen, altering its appearance and form. As the cleaning progresses, the tablecloth takes on a more functional role, its aesthetic momentarily set aside for practicality. The water's impact is evident in the evolving state of the fabric, from dry and smooth to wet and contoured, highlighting the cloth's transition through the stages of cleaning.

#### Sample 351 — Transition

- Similarity: 0.3907
- Prediction: Over the course of these three frames, there's a clear progression in the state of the bag. Initially, it's in a state of disarray, with the bag's contents scattered across the surface. As the frames progress, the person's actions become more deliberate, indicating that the bag is being handled. By the final frame, the bag appears to be fully open, with no visible signs of damage. This progression is indicative of the process of preparing the bag for use.
- Reference: Over the course of the three frames, the olive oil bottle undergoes a transition from being open to being sealed. Initially, the cap is resting independently on the stovetop, separated from the bottle. Moving to the second frame, the cap is picked up and aligned with the bottle for recapping. By the third frame, the action is nearly complete, with the cap being twisted onto the bottle to form an airtight seal. This sequence captures a common yet precise task, requiring fine motor skills to ensure the cap is correctly threaded and the contents of the bottle are preserved. The process is a small but integral part of kitchen activities, reflecting both the use and storage aspects of cooking ingredients.

#### Sample 353 — Transition

- Similarity: 0.4753
- Prediction: Over the course of these three frames, there's a clear progression in the state of the machine. Initially, it's in a state of disengagement, with the user's hand indicating that the machine is ready for use. As the frames progress, the hand's interaction with the machine becomes more evident, implying that the user is engaged in the process of adjusting the machine's settings. By the final frame, the user appears to have withdrawn the machine from its position, indicating a change in its state of engagement. This sequence captures the progression of a machine
- Reference: The transition of the button from its initial unpressed state to being fully pressed is a smooth progression. Initially at rest, the button begins to depress under the force of the finger, altering its reflective qualities and shifting the angle of its surface. As the finger continues to exert pressure, the button moves downward until it reaches its maximum range of motion. Throughout this sequence, the surrounding area remains largely unaffected, with only the light and shadows dancing across the button's surface indicating the dynamic action taking place.

#### Sample 354 — Transition

- Similarity: 0.4686
- Prediction: Over the course of these three frames, there's a clear progression in the state of the kettle. Initially, it's in a state of disrepair, with no visible signs of use. As the frames progress, the kettle's surface becomes more exposed, indicating a gradual change in its position. By the final frame, it appears to be fully withdrawn from the water, with the lid still firmly attached to the pot.
- Reference: The sequence of frames depicts the motion of a ladle being handled in a kitchen setting. Initially, the ladle is gripped firmly and is being moved with purpose, likely transitioning from one part of a cooking task to another. As the frames progress, there is a fluid movement, a rotation captured by the change in the ladle's orientation and the user's grip. By the final frame, the ladle has been placed down, signifying the end of its immediate use. The surrounding kitchen items like the rolling water bottle and the wooden spoon provide a static backdrop to the ladle's journey from active use to rest.

#### Sample 355 — Transition

- Similarity: 0.4796
- Prediction: Over the course of these frames, the halibut undergoes a noticeable transformation. Initially, it's whole and ready to be sliced, but as the frame progresses, it becomes more and more shredded, indicating a gradual process. As the frames progress, there is a clear progression in the preparation of the vegetable, with the initial stages indicating the final stages of the cooking process. By the final frame, the vegetable is being prepared for cooking, demonstrating a methodical approach to the preparation process.
- Reference: The pak choi leaf undergoes a clear transformation across the three frames. Initially whole and just touched by the knife, it is then seen mid-slice with the knife cutting through its fibrous stem and delicate leaf. By the final frame, the leaf is transformed into neatly cut sections. The process reflects a careful and purposeful effort to prepare the pak choi for cooking, maintaining the integrity of the leafy greens while creating bite-sized pieces suitable for a dish. The slicing is methodical, maintaining the freshness and structure of the pak choi throughout the process.

#### Sample 356 — Transition

- Similarity: 0.4336
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the stovetop. Initially, it's in a state of disarray, with no visible signs of activity or activity. As the frames progress, however, there is a clear transition in the direction of the burner, with the burner positioned in the middle of the frame. By the final frame, the burner's position is blurred, indicating that the burner has been removed from the burner and replaced with a new one. Throughout the sequence, the kitchen appears to be undergoing a transformation in the kitchen's settings, with fewer and fewer items being placed on the burner.
- Reference: Over the course of these three frames, the mixture in the pan undergoes a clear transformation. It begins with a brighter, fresher-looking assortment of green ingredients floating in a clear, thin liquid with a light sheen of oil. As time progresses, the liquid gradually reduces, the green components wilt and darken in color, and the overall consistency of the mixture thickens. By the final frame, there is a noticeable reduction in volume, the ingredients have melded together more cohesively, and there is a glossy sheen that suggests the formation of a sauce. This visual progression is indicative of the sautéing and simmering process, where heat gradually breaks down the ingredients, evaporates water content, and concentrates flavors.

#### Sample 359 — Transition

- Similarity: 0.4380
- Prediction: Over the course of these three frames, the cloth undergoes a noticeable transformation from a partially wetted area to a fully soaked area. Initially, it's in a state of disarray, with no visible signs of rinsing or wringing. As the final frame progresses, it becomes more and more soaked, indicating that the water has been drained out of the cloth. By the third frame, there is a visible change in the amount of water in the cloth, with a gradual increase in the volume of the water's contents. The cloth's transition from wet to wet is indicative of a thorough cleaning process, demonstrating a
- Reference: Analyzing the bin across the three frames, its state remains consistently full, with the contents reaching above its rim throughout. There is a subtle implication of additional waste being added, as indicated by the human interaction in frames two and three. However, there is no significant visible change to the volume of waste in the bin, suggesting that if something was added, it was small. The environment around the bin stays static, with no observable adjustments to the items on the countertop or within the dish rack. The plastic liner shows a slight bulge in the last frame, which might be a result of the bin being further filled or simply from the movement of the bag as waste was added.

#### Sample 361 — Transition

- Similarity: 0.3818
- Prediction: Over the course of these three frames, there's a clear progression in the state of the chicken. Initially, it's fully intact, with no visible signs of cooking. As the frames progress, the hands are engaged in the process of removing the chicken from its packaging. By the final frame, the chicken is almost completely removed, indicating that the action is complete. The hand's movements are evident throughout the process, demonstrating a willingness to engage in the action. The consistency of the hands' movements is indicative of a methodical approach to preparing the chicken for cooking.
- Reference: The sequence of images captures a moment-by-moment transformation of the red pepper from its packaged state to being prepped for cooking. Initially, the pepper sits undisturbed, secure in its plastic wrap with other colorful companions. As the moments pass, human interaction introduces change; the hand selects the red pepper, repositions it, and the knife is poised to cut. Finally, the knife slices through the plastic, an act that converts the pepper from a packaged good to a ready-to-use ingredient. This progression not only depicts the physical state change of the pepper but also the methodical approach taken to prepare it for inclusion in a meal.

#### Sample 364 — Transition

- Similarity: 0.2037
- Prediction: Over the progression of these three frames, the jar undergoes a clear transition from a static state to a dynamic state. Initially, it's in a state of disarray, but as it moves closer to the surface, it becomes more agitated, indicating a change in its position. As the frames progress, the hand's movements become more deliberate, suggesting a shift in the direction of the action. By the final frame, the lid's position is blurred, suggesting that the lid has been removed from the container.
- Reference: Over the span of these frames, the sweet potato undergoes a captivating transformation. Initially, it sits in its whole, untouched state, exuding natural freshness and earthly charm. As we progress, the tuber is carefully dissected, revealing its juicy, vibrant core, and setting the stage for its culinary destiny. By the end, the sweet potato, having been cooked or baked, has transformed into a tantalizing dish, with textures and colors enhanced, promising a delightful taste and aroma to whoever is about to enjoy it. The journey showcases not just a physical change, but a sensory evolution, inviting onlookers to appreciate the culinary art and nature's bounty.

#### Sample 365 — Transition

- Similarity: 0.2994
- Prediction: Over the course of these three frames, there's a clear progression in the state of the stovetop. Initially, it's in a state of disarray, with no visible signs of cooking or cooking. As the sequence progresses, the person's hands move from one side to the other, indicating a thorough cleaning. By the final frame, there is a noticeable shift in the position of the burners, with a gradual change in the direction of the cooking process. The consistent movement of the blades, as well as the hand's motions, suggest a methodical approach to the task.
- Reference: Throughout the progression of these frames, the state of the hob surface has undergone a significant transformation. Starting with a noticeable amount of spilled substance and moisture, there has been a systematic reduction in the residue and sheen with each frame. The presence and action of the blue cloth have been instrumental in this change. From the initial spotting of the spill to the near completion of the cleaning process, the hob's state has shifted from messy to mostly clean, showcasing the effectiveness of the cleaning effort.

#### Sample 367 — Transition

- Similarity: 0.3976
- Prediction: Over the course of these three frames, there's a clear progression in the state of the oil. Initially, it's in a state of disarray, but as the frame progresses, it becomes more and more agitated, indicating a gradual release of oil. As the frames progress, the oil's surface becomes more undisturbed, suggesting that the oil has been removed from the surface. By the final frame, it appears to have been poured into the oil, with the oil still present. This sequence captures the action of a
- Reference: Over the course of the three frames, the cap undergoes subtle changes in its position and visibility. Initially obscured and in the periphery, it gradually moves to a more central position in the viewer's field of vision. The illumination improves slightly across the frames, revealing more of the cap's details. Throughout the progression, the cap seems to be in a state of rest amidst a disorderly setting, but its prominence becomes more pronounced with each successive frame.

#### Sample 368 — Transition

- Similarity: 0.4548
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the bag. Initially, it's partially open, with the person's hand guiding it. As the frames progress, the bag's contents are revealed, indicating that the person is preparing to use it. By the final frame, the man's hands are engaged in the action, demonstrating that the bag is fully opened. This progression is indicative of the process of preparing the bag for use.
- Reference: Over the course of these three frames, the chopped tomatoes transition from being freshly opened in their can to being absent from the visible area, indicating their progression in the cooking process. Initially, the tomatoes are presented in their raw, canned state, ready for use. As the frames advance, the tomatoes themselves are not directly shown, but the surrounding evidence of cooking activity suggests that they have been set aside or added to a dish that's being prepared. The progression of the ingredients from packaged to being part of a meal preparation is subtly indicated by the changing state of the kitchen countertop, from the organized beginning to a more active cooking stage.

#### Sample 370 — Transition

- Similarity: 0.4843
- Prediction: The sequence of frames captures a clear progression in the state of the tea towel. Initially, it's in a state of disarray, with no visible signs of movement. As the sequence progresses, the towel's surface becomes more cluttered, indicating a deliberate action. By the final frame, the hand's actions become more deliberate, with the towel now positioned in the middle of the table. The transition from a static state to a more dynamic state is indicative of a transformation in the towel, which is a shift in the direction of the action.
- Reference: The sequence of the frames illustrates the dynamic process of tearing paper from a roll. Initially, the roll is intact, with only the anticipation of movement. Progressing to the next frame, the action commences, disrupting the roll's uniformity as the paper begins to separate. By the final frame, the paper's detachment is evident, and the manner in which it has been torn—upward and away from the roll—is clear. This progression captures the interplay of force and resistance inherent in the act of tearing paper, where each frame represents a distinct phase of the transition from potential to kinetic energy and finally to the alteration of the paper's form.

#### Sample 371 — Transition

- Similarity: 0.4824
- Prediction: Over the course of these three frames, the courgette undergoes a noticeable transformation. Initially, it's fresh and crisp, with a distinctive shape and texture. As the cooking process progresses, the vegetables begin to cook more evenly, indicating that they're ready for cooking. By the final frame, they've become more charred and browned, demonstrating a more gradual cooking process. This transition is indicative of the chef's intent to ensure that the vegetables are cooked to their fullest potential.
- Reference: The spatula's journey begins with anticipation, held ready above the pan, then it dives into the action, pressing into the chopped vegetables, stirring them around. This motion is purposeful, ensuring an even sauté. Finally, the utensil is lifted, pausing in the air, completing the cycle of cooking action. Throughout these frames, the spatula's role is pivotal in the manipulation of the food, working in harmony with the cook's movements to achieve the culinary goal. The sequence shows a progression from readiness to action to a brief rest, reflecting the rhythm of cooking.

#### Sample 372 — Transition

- Similarity: 0.4335
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the trash can. Initially, it's partially open, with no visible obstructions. As the frames progress, the person's movements become more deliberate, indicating that they're engaged in a routine activity. By the final frame, the trashcan is almost fully open, suggesting that the person is attempting to remove the trash from the container. This progression is indicative of a more deliberate action, with the person likely removing the trash, implying that the trash has been removed.
- Reference: The progression across the frames captures a dynamic sequence involving the basket: from being in rapid motion, to the absence of the basket in the frame focusing on the movement of the person, to a final frame where the action culminates in the person engaging directly with the basket's contents. The sequence depicts a swift transition from motion to stability, with the final frame suggesting a resolution to the action, where the person is likely sorting or retrieving items from the basket. The change in the basket's state from blurred to stable, coupled with the person's changing position, narrates a brief story of an everyday activity captured in fragments of continuous motion.

#### Sample 373 — Transition

- Similarity: 0.4827
- Prediction: Over the course of these three frames, there's a clear progression in the state of the cheese. Initially, it's in a state of disarray, with no visible signs of activity. As the sequence progresses, the cheese appears to have been removed from its packaging, indicating a deliberate action. By the final frame, the person's actions are evident, with the cheese firmly placed in the hands of the person who is preparing the meal.
- Reference: Starting from an untouched state, the sandwich undergoes a transformation as it is being sliced. Initially, the bread appears whole and uncut, with its contents hidden. As the knife begins its descent, the sandwich's structure is disturbed, revealing a peek of its inside ingredients. By the third frame, the knife has made a significant cut, leading to a clear distinction between the two halves of the sandwich, showcasing the sandwich's interior more prominently. The transition from whole to being sliced captures the meticulous process of preparing the sandwich for consumption.

#### Sample 378 — Transition

- Similarity: 0.4506
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the vegetables. Initially, they're still a little wilted, but by the third frame, they become more agitated and ready for cooking. By the fourth frame, however, the vegetables are no longer fully cooked, indicating a gradual change in their state of cooking. The changes in the vegetables' appearance, texture, and flavor are indicative of a deliberate cooking process.
- Reference: Over the sequence, the hob's state transitions from active cooking to an implied pause. Initially, the hob is the center of activity with vegetables being sautéed on a lit burner. As the scene moves to the countertop, the focus on the hob is momentarily lost, suggesting a brief intermission in its use, with the user's attention diverted to other preparatory tasks or to the oven. Finally, the user's attention seems entirely redirected from the hob towards the oven, indicating a progression in the cooking process or a multitasking scenario where the hob's contents require less immediate supervision. Throughout these frames, the hob remains in a consistent state of use, with one burner visibly operational.

#### Sample 379 — Transition

- Similarity: 0.4755
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the pot. Initially, it's in a state of disrepair, but as the frame progresses, the pot's surface becomes more exposed, indicating a gradual change in its position. As the frames progress, the lid's position becomes more prominent, suggesting that the pot has been partially removed from the burner. By the final frame, it appears to have been fully removed, with the lid still firmly attached to the stovetop. This progression is reminiscent of a kitchen scene where the lid is removed and the pot is placed on a counter.
- Reference: Across the progression of the three frames, the tray undergoes a clear transition from a state of rest to being in motion. Initially, it sits undisturbed on the scales. As the frames progress, there is an evident gradual disturbance in its positioning, transitioning from a subtle tilt to a full lift-off from the scales. By the final frame, the tray has been lifted to a degree that it no longer maintains any contact with the scales, suggesting the act of someone picking it up or removing it from its original position. The surrounding objects provide a static backdrop against which the tray's movement becomes even more noticeable.

#### Sample 390 — Transition

- Similarity: 0.4548
- Prediction: Over the course of the three frames, there is a clear progression in the state of the oven. Initially, the oven's light is dimmed, but as the frame progresses, the light becomes more visible. By the third frame, it's almost fully illuminated, indicating that the oven has been switched on. As the frames progress, there's a noticeable shift in the light's state, implying that the light has been turned off, and the oven is now almost fully lit. This transition suggests a gradual change in the lighting conditions, with the light intensifying and bringing the oven to a more natural state.
- Reference: The progression of the images shows a distinct transformation in the lighting conditions of the room. Initially, the light was diffused, casting a faint and formless glow. As adjustments were made, the light became more focused, with the second frame revealing a clearer shadow and the third demonstrating a marked increase in both intensity and definition. This sequence illustrates the dynamic nature of light and its ability to dramatically alter the visual ambiance of a space, as manipulated by the unseen individual interacting with the room's lighting.

#### Sample 392 — Transition

- Similarity: 0.3782
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the oven door. Initially, it's partially open, with the door's contents concealed. As the frames progress, the door is progressively opened, revealing the contents. By the final frame, the doors are fully open, and the person's hand is engaged in the process of opening the door. This progression marks the beginning of a transitional phase in the kitchen
- Reference: Throughout the sequence, the tea towel transitions from a loosely placed item in the drawer to one that's actively being manipulated. Initially, it lies casually draped, its vivid stripes providing a pop of color against the wooden backdrop. As the hand intervenes, the fabric gathers and folds, with the direction and intent of the movement becoming more apparent. By the final frame, the tea towel's state reflects the consequences of this interaction—a more crumpled presence, embodying the dynamic nature of household tasks and the temporary disorder that often precedes tidiness.

#### Sample 398 — Transition

- Similarity: 0.4134
- Prediction: Over the course of these frames, there's a clear progression in the handling of a can
- Reference: Throughout the three frames, there's a consistent evolution in the interaction with the jar's clip top. Initially, it's in a semi-open state, with a preliminary exploration by the hands. As the frames progress, the clip top is manipulated into a fully open position, enabling a closer examination of its components. This transition underlines a systematic process of inspecting or cleaning the jar's sealing mechanism, ensuring its readiness for future use or confirming its operational status. The hands' movements highlight the importance of the clip top's integrity in preserving the jar's contents.

#### Sample 401 — Transition

- Similarity: 0.3294
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the kitchen sink. Initially, it's partially open, with no visible signs of life or activity. As the frames progress, the person's hand moves closer to the sink, revealing more of the sink's contents. By the final frame, the sink appears to be fully open, indicating that the sink has been removed from the sink. This progression is indicative of a gradual change in the kitchen's state of being, with the sink becoming more open and revealing less of its contents.
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

- Similarity: 0.4775
- Prediction: Over the course of these three frames, the bacon undergoes a clear transition from being untouched to being sliced. Initially, it's untouched, but as the hands move closer to the bacon, the action becomes more deliberate, indicating that the bacon is being cut. As the final frame progresses, the knife's movements become more precise, suggesting that the bread has been sliced and is ready to be sliced again. This progression is indicative of the bread's transformation from a single piece of bread to a complete meal.
- Reference: Over the course of these three frames, the onion undergoes a transition from being a stand-alone prepared ingredient to becoming an integral component of a more complex dish. Initially, it's presented in its sliced form, clearly showcased on a plate. As the scenes progress, the onion becomes a part of a layered culinary creation, suggesting an evolving recipe. By the third frame, the onion, while still recognizable, is now harmoniously combined with other ingredients, ready for the next steps in the cooking process. This progression highlights the versatility of the onion and its role in enhancing the flavors of a dish.

#### Sample 406 — Transition

- Similarity: 0.4720
- Prediction: Over the progression of these three frames, the trash can undergoes a dynamic change in its state of being. Initially, it's partially open, with no visible obstructions. As the frames progress, the person's hand moves closer to the lid, indicating that the trash has been removed from the container. The final frame captures the action of removing the trash from the bin, with the lid still partially closed. This progression represents a progressive change in the way the trash is handled, with a focus on the user's interaction with the trashcan.
- Reference: As we traverse through the frames, there's a pronounced evolution in the state of the strainer. Beginning with a substantial amount of orange-yellow liquid, there's a clear progression of this liquid being drained or poured out. The liquid's presence diminishes considerably from the first to the third frame, with the strainer transitioning from being nearly full to almost entirely empty. This sequence paints a picture of an action being carried out methodically, showcasing the draining process in its different stages, from initiation to near completion.

#### Sample 410 — Transition

- Similarity: 0.4380
- Prediction: Over the course of these three frames, there's a clear progression in the state of the cheese. Initially, it's resting in a state of disintegration, but as the frames progress, the cheese begins to become more fully incorporated. By the final frame, however, the person's hand is engaged in the action, indicating that the cheese has been removed from the container. This progression is indicative of a gradual change in the cheese's state of being, with the hand's motion indicating the process of removing the cheese from its container.
- Reference: The progression of sweetcorn from can to pizza captures a brief narrative of pizza preparation in these frames. Initially, the sweetcorn is introduced to the pizza, finding a home among the stripes of sauce. As we move to the next scene, there is an active engagement, a deliberate scattering that increases the sweetcorn's presence across the pizza's canvas. By the final frame, the act of sprinkling sweetcorn reaches a crescendo, culminating in a more uniform distribution, filling the space with color and texture. The narrative is one of addition and integration, with each frame representing a moment in the transformation of raw ingredients into a pre-baked culinary creation.

#### Sample 412 — Transition

- Similarity: 0.4475
- Prediction: Over the course of these three frames, the chopping board undergoes a visible transformation. Initially, it's in a state of rinsing, with the water running through the board's surface. As the frames progress, the water's flow becomes more concentrated, indicating that the board is being rinsed. By the final frame, the board appears to be fully rinsed, and the water has been drained away. This sequence exemplifies a methodical approach to preparing the board for the next step in its cleaning process.
- Reference: The progression observed in the spring onion's state from the first to the third frame demonstrates a systematic cleaning process. Initially presented in a dry state, the onion is then subjected to a rinse, evidenced by the water droplets forming on its surface. As the frames advance, the onion is held more securely, and the water pressure increases, causing the stalks to bend and reveal their fresh and crisp quality. The final frame encapsulates the conclusion of the rinsing, with the onion fully saturated and its roots drenched, signifying readiness for subsequent culinary use.

#### Sample 419 — Transition

- Similarity: 0.4917
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the water in the sink. Initially, it's in a state of disrepair, indicating that the water has been drained out. As the frames progress, the water's state changes to a more active state, suggesting that the sink has been partially emptied. By the final frame, the sink is fully empty and ready to be rinsed. This progression is indicative of a thorough cleaning process, with a clear emphasis on the cleanliness of the sink and the surrounding area.
- Reference: Over the span of these three frames, the kettle undergoes a notable transformation in its state and positioning. Initially, it is actively being tilted to pour out its contents, evident from the water splashes and the hand's positioning. As we progress, the pouring action slows down or pauses, with the kettle becoming more upright and stationary by the third frame. Throughout this sequence, the open lid remains a constant, but the dynamics of the hand's grip and the kettle's orientation depict a story of a task – likely emptying or cleaning – nearing its completion.

#### Sample 427 — Transition

- Similarity: 0.3646
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the cheese. Initially, it's in a state of disarray, but as it moves closer to the surface, the cheese becomes more noticeable. As the frames progress, the hand's movements become more deliberate, indicating that the cheese has been placed on the surface. By the final frame, the person's interaction with the cheese is evident, and the cheese's contents are clearly visible. This progression is indicative of a gradual change in the cheese
- Reference: Initially, the refrigerator appears partially stocked with eggs and possibly vegetables, and the door is slightly open with the interior unlit. As the door opens fully, more contents become visible, including fruits on the door and condiments on the lower shelf, yet the light remains off throughout, which is atypical for an operating refrigerator. In the progression of the frames, the focus shifts from the upper to the lower part of the refrigerator, revealing a consistent state of the appliance being unlit and the door moving from slightly to fully open, suggesting someone is either searching for something or organizing the contents.

#### Sample 433 — Transition

- Similarity: 0.3521
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the kitchen sink. Initially, it's partially open, with no visible obstructions. As the frames progress, the sink's surface becomes more exposed, indicating a gradual change in its position. By the final frame, it appears to be partially closed, with the sink still partially open. This progression is indicative of a transition in the kitchen's state of being, with a focus on the kitchen as a whole.
- Reference: Throughout the frames, the cloth undergoes a clear transformation associated with the act of squeezing out liquid. Initially held in a preparatory grip, it is then firmly wrung, which is evident from the twisting and compacting of the material. As the sequence progresses, the intensity of the squeeze lessens, and the cloth begins to unfold and relax. This indicates the end of the active wringing phase, transitioning towards the cloth being unfurled to either be used again or to dry out completely. The fabric's moisture content seems to have decreased, judging by the less saturated appearance in the final frame, which suggests that the squeezing action effectively expelled liquid from the cloth.

#### Sample 437 — Transition

- Similarity: 0.2843
- Prediction: Over the progression of these three frames, there's a noticeable progression in the state of the sieve. Initially, it's in a state of disrepair, with no visible signs of food or water. As the frames progress, it becomes more and more agitated, indicating that there is a significant amount of water or food in it. By the final frame, the siege has been fully emptied, and the water level has been reduced to a level that is conducive to rinsing.
- Reference: Over the course of the three frames, the pepper pieces undergo subtle yet noticeable shifts in their position on the chopping board. Initially scattered haphazardly, they experience a minor rearrangement, possibly due to external forces or preparatory actions for the next step in the cooking process. By the third frame, human intervention is evident as a hand enters the frame, poised to pick up or move the pepper pieces, indicating the progression from preparation to active utilization of the ingredients. This sequence portrays a typical kitchen scene where ingredients are prepared and then used in the cooking process.

#### Sample 447 — Transition

- Similarity: 0.4255
- Prediction: Over the course of these three frames, there's a clear progression in the state of the pan. Initially, it's in a state of disrepair, with the pan's lid still partially open. As the frames progress, the person's hand moves closer to the pan, indicating a more active action. By the final frame, the pan is almost fully open, with its lid still slightly open. This progression is indicative of a deliberate handling of the pot, which is likely a step in the kitchen's preparation for cooking.
- Reference: The progression of the food processor's state unfolds in a meticulous cleaning routine. Initially, it is presented as a freshly washed item inside the dishwasher, surrounded by other clean dishes. The subsequent frame captures a moment of additional rinsing, indicating a personal touch to the standard cleaning process. Finally, the processor is seen being settled back into the dishwasher, not for another wash cycle, but rather for orderly storage. This sequence of actions not only emphasizes cleanliness but also the care taken in maintaining kitchen appliances, ensuring they are ready for their next use.

#### Sample 448 — Transition

- Similarity: 0.4668
- Prediction: Over the course of these three frames, there's a clear progression in the state of the washing machine. Initially, it's in a state of disengagement, with the user's hand resting on the machine's side. As the sequence progresses, the hand's movements become more pronounced, indicating that the machine has been fully engaged. By the final frame, the person's interaction with the machine becomes more evident, implying that the hand is engaged in the process of washing the machine.
- Reference: Over the course of these frames, the coffee machine transitions from an idle state to the beginning of a brewing cycle. Initially dormant, with no indication of activity, it moves into an active state under the guidance of a human hand. The engagement of a button and the accompanying green light serve as clear signals of this transition. Despite the activation, the brewing process has not visibly commenced, likely due to the carafe’s absence, which is a necessary component for most machines to start brewing. There's an anticipation of action, suggested by the hand's presence and the machine's readiness, but the sequence does not yet culminate in the actual brewing of coffee.

#### Sample 453 — Transition

- Similarity: 0.4815
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the sink. Initially, it's in a state of disarray, with no visible or visible debris. As the frames progress, the sink's surface appears to be progressively scrubbing and reorganizing. By the final frame, there is a clear shift in the direction of the cleaning process, indicating that the water has been drained out and the sink is clean. The consistency of the water's suds, as well as the movement of the hand, are indicative of a thorough cleaning process.
- Reference: As the frames progress, the counter undergoes a dramatic transformation. What begins as a surface layered with imperfections, dust, and remnants, soon witnesses a division, a split between the cleaned and the cluttered. The dance of the cloth, dampened with intent, choreographs this change. By the final frame, the counter has shrugged off its prior state, embracing cleanliness and uniformity, telling a silent tale of care and maintenance.

#### Sample 456 — Transition

- Similarity: 0.4397
- Prediction: Over the course of these three frames, there's a noticeable progression in the cleaning process of a pot
- Reference: Throughout the three frames, the decorative coffee machine undergoes subtle changes in its positioning and interaction. Initially presented in full view, the machine gets partly obscured in the second frame by a hand, hinting at some movement or interaction. By the third frame, the machine seems to have been repositioned, and the hand is no longer in sight. These changes suggest that someone was likely adjusting or moving the coffee machine during this sequence. The lighting alterations between the frames also indicate varying environmental conditions or camera adjustments.

#### Sample 458 — Transition

- Similarity: 0.3834
- Prediction: Over the course of these three frames, the pan undergoes a noticeable transformation. Initially, it's in a state of disrepair, with no visible food or debris. As the sequence progresses, it becomes more and more agitated, indicating that there's been a significant change in the pan's state of cleanliness. By the final frame, it appears to be fully sanitized and ready to be washed, suggesting that the cleaning process is complete.
- Reference: Over the course of the three frames, the tap's state transitions from off to on. Initially, the lever is parallel to the countertop, indicating a closed position with no water flow. There is no change in the tap's status between the first and second frames, but by the third frame, the lever has been tilted downwards, which is a common position for allowing water to flow. The progression shows a deliberate action to turn the tap on, although the actual flow of water is not captured within these still frames.

#### Sample 459 — Transition

- Similarity: 0.3640
- Prediction: Over the progression of these three frames, the chopping board undergoes a noticeable change in its state. Initially, it's in a state of disrepair, but as it moves closer to the edge of the board, it becomes more and more agitated. As the frames progress, the person's movements become more deliberate, indicating that they are engaged in some sort of action. By the final frame, the hand's motions become more pronounced, suggesting that the person is preparing for a meal or other activity.
- Reference: Transitioning from the first to the last frame, the can undergoes a series of changes. Initially, it is at rest on the countertop, with the lid partially opened, revealing a static glimpse of its contents. As the sequence progresses, the can is picked up, its lid further retracted to display the peas or corn more clearly. In the final frame, the can is in swift motion, likely being disposed of or transferred to another area. Throughout this transition, the contents remain consistent, but their visibility increases as the lid is peeled back, and finally, the motion likely causes a disturbance of the contents, hinting at a change in their arrangement.

#### Sample 460 — Transition

- Similarity: 0.3009
- Prediction: Over the course of these frames, there's a noticeable progression in the state of the stovetop. Initially, it's in a state of disarray, with no visible signs of cooking or cooking. As the frames progress, there is a clear transition in the direction of the burners, with a focus on the surface of the pan. By the final frame, the pan's surface appears to have been cleaned, indicating a thorough cleaning process. The consistency of the surface and the consistent movement of the blades suggest a methodical approach to preparing the surface for cooking.
- Reference: Transitioning from the initial frame to the last, the sequence displays a rapid deceleration of both hand movement and water flow. Initially, the blur and lack of clear water stream suggest a tap being swiftly turned off. As the sequence progresses, the reduction in motion blur and hand retreat reflect the decreasing flow of water, culminating in the final frame where stillness prevails. The tap, once engaged in delivering water, now stands idle, having completed the transition from active to inactive, evidenced by the absence of water flow and the calm state of the surrounding area.

#### Sample 463 — Transition

- Similarity: 0.3935
- Prediction: Over the course of these three frames, there's a clear progression in the state of the pot. Initially, it's in a state of disarray, with no visible signs of cooking. As the frame progresses, the pot appears to be a little more agitated, suggesting a change in the pot's position. By the final frame, however, there is a noticeable increase in the amount of water on the pot, indicating that the pot is being used for cooking. This progression is indicative of a more active cooking process, with the pot likely to be ready for use within a few minutes.
- Reference: Over the course of the three frames, there's a perceptible sense of progression and movement, especially around the switch area. The images give an impression that the hand is reaching for, interacting with, or moving away from the switch. The exact transition from the "on" to "off" state (or vice versa) is not explicitly captured, but the sequence implies a deliberate action concerning the switch. The blurriness and rapid movement suggest that there might be a swift change in the state of the switch, but the specific details of that transition remain inconclusive based on the provided frames.

#### Sample 469 — Transition

- Similarity: 0.4313
- Prediction: Over the course of these three frames, there's a clear progression in the state of the chicken. Initially, it's in a state of disarray, with no visible signs of activity. As the sequence progresses, the chicken's movements become more deliberate, indicating that the action is taking place. By the final frame, it appears to have been agitated, with the chicken poised to be ready for cooking. The hand's motions are consistent, suggesting that the chicken has been preparing for cooking, and the chicken is ready to be cooked.
- Reference: Starting from its initial state where it rests on the appliance, there is a gradual and evident progression in the cover's movement across the frames. Initially, slight elevation suggests the beginning of the lift. As we move to the next frame, there's clear interaction with hands surrounding and tilting it, indicating an active and deliberate action of removal. By the final frame, the cover is almost entirely lifted, showcasing the culmination of the removal process, with the motion and environment around it capturing the rapidity and fluidity of the action. The entire sequence demonstrates a steady progression from a static state to dynamic motion.

#### Sample 470 — Transition

- Similarity: 0.3900
- Prediction: Over the progression of these three frames, the bottle undergoes a clear transition from a state of rest to an active action. Initially, it's in a steady state, with no noticeable change in its state. As the frames progress, the person's actions become more deliberate, indicating that the bottle has been agitated. By the final frame, there is a noticeable shift in the position of the bottle, suggesting that the action has taken place. This progression is indicative of a
- Reference: Over the course of the three frames, the plug undergoes a clear transition from being partially inserted in the power outlet to almost completely removed. Initially, the plug is seen in a semi-attached state, with the person’s hands positioned to start the unplugging process. As the sequence progresses, the hands are observed pulling the plug out, demonstrating more of the metal prongs in the process. By the final frame, the plug is nearly detached, signifying the end of the action. This sequence showcases a careful and deliberate movement, likely performed to disconnect the appliance without causing damage to the plug or the outlet.

#### Sample 476 — Transition

- Similarity: 0.3434
- Prediction: Over the course of these three frames, there's a clear progression in the state of the cheese. Initially, it's in a state of disarray, with no discernible markings. As the sequence progresses, the cheese begins to become more pronounced, indicating a gradual change in the cheese's composition. By the final frame, the pizza's surface appears to have been rearranged, with a smoother surface and a more uniform appearance. This progression is indicative of the chef's intent to ensure that the cheese is properly distributed, ensuring that the finished product is ready for use.
- Reference: The progression of the salt from the shaker to the flatbread reveals a deliberate and methodical seasoning process. Initially, the salt shaker is poised to begin the action, with no salt visible in the air. As the hand commences shaking, we observe a subtle start, gradually intensifying into a more vigorous motion by the second frame, where the salt begins to emerge. By the third frame, the hand has carried out a series of shakes, evidenced by the visible grains of salt mid-descent. The sequence captures the dynamic nature of seasoning, with the shaker's angle and the hand's motion suggesting a rhythmic and controlled dispensing of the salt.

#### Sample 477 — Transition

- Similarity: 0.2517
- Prediction: Over the course of these three frames, the rice undergoes a noticeable transformation. Initially, it's in a state of disarray, with a few pieces of rice separated from the rest of the rice. As time progresses, the water's action becomes more active, resulting in the rice turning into a smoother, more uniform texture. By the final frame, the spoon's motion becomes more deliberate, indicating that the rice has been thoroughly stirred and is ready to be served.
- Reference: Observing the progression of the light in these frames depicts the ignition and stabilization of a gas burner's flame. Initially, a magenta glow indicates the initial light-up, followed by a transition to a bright blue as the flame becomes more intense and the gas combustion reaches a higher efficiency. Finally, the flame settles into a steady state, with a strong blue core and a constant outer flame, signifying a sustained and even heat source. This progression is typical for gas burners, as the color and intensity of the flame can indicate the stage of heating and the efficiency of the fuel being burned.

#### Sample 482 — Transition

- Similarity: 0.4767
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the aluminum foil. Initially, the foil is untouched, with no visible signs of damage. As the frames progress, the person's hands are engaged in the process of removing the foil from the foil. By the final frame, it's evident that the foil has been partially removed, with the foil still firmly attached to the foil, indicating that the action has taken place. This progression is indicative of a gradual change in the foil's state of being exposed to the elements, with a focus on the individual's ability to use the foil as a source of sustenance.
- Reference: Throughout the progression of these frames, there's a clear transition in the state of the meat packaging. Initially, both packages of meat were untouched and intact. As the frames progress, the lighter meat's package becomes the focus of interaction, starting from a subtle pinch or pry at its corner to a more evident attempt at opening it by the third frame. By the end of this sequence, the original sealed state of the packaging is altered, revealing a part of its contents and signifying the commencement of the unboxing process.

#### Sample 490 — Transition

- Similarity: 0.3617
- Prediction: Over the progression of these three frames, there's a clear progression in the state of the packaging. Initially, the packaging is fully open, with no visible signs of damage. As the sequence progresses, the person's hands are engaged in the process of removing the packaging, indicating that the action is complete. By the final frame, the package is almost fully opened, with the hand's fingers firmly pressed against the plastic. This progression is indicative of a more deliberate handling of the package, with a focus on minimizing the risk of contamination.
- Reference: The tortilla undergoes a noticeable transition across the three frames, driven by the careful manipulation of the hand. Initially presented as a flat, supple disc, it begins a journey back to its pack, its shape and texture remaining relatively intact. As the motion progresses, the tortilla succumbs to the forces exerted by the hand and gravity, bending and folding, altering its form. This evolution from a flat entity to a conforming, folded object encapsulates a simple, yet precise action of returning the tortilla to its storage, a mundane task executed with an everyday grace and necessity.

#### Sample 491 — Transition

- Similarity: 0.1002
- Prediction: Over the course of these frames, the pak cho
- Reference: Starting from a fresh and untouched state, the coriander undergoes a transformation across the three frames. Initially presented in a whole and unprocessed form, the herb is gradually dissected, with leaves and stems becoming increasingly separated and chopped. As the frames progress, there's a noticeable increase in the distribution of cut coriander pieces on the board, showcasing the stages of the herb being prepared for a culinary purpose. The evolution of the coriander's state is evident in the increasing fragmentation and dispersion of its components.

#### Sample 495 — Transition

- Similarity: 0.3481
- Prediction: Over the progression of these three frames, the icing paper undergoes a subtle transformation. Initially, it's in a state of disarray, but as it moves closer to the surface, it becomes more and more agitated. As the frames progress, the hand's movements become more deliberate, indicating that the paper has been placed on the surface. By the final frame, the person's actions become more intentional, implying that they're preparing for a meal or other activity. This progression is indicative of a
- Reference: Throughout the sequence of images, there is a clear progression in the state of the plug as it transitions from being fully inserted to partially removed from the wall socket. Initially, the plug is firmly in place, but as the sequence progresses, a pulling force acts upon it, evidenced by the change in the angle and tension of the cord. By the final frame, the plug is only halfway engaged with the socket, and the movement suggests a deliberate action to disconnect the plug. The unplugging appears to be done with some haste or urgency, as the cord is taut and the action swift. This sequence captures the very moment of electrical disconnection, a commonplace yet crucial action in daily life.

#### Sample 496 — Transition

- Similarity: 0.4291
- Prediction: Over the progression of these three frames, the paper towel undergoes a transformation from a static state to a dynamic state. Initially, it's in a state of disarray, with no visible signs of movement. As the sequence progresses, the person's actions become more deliberate, indicating that the towel is being used for a purpose. By the final frame, the towel's position is blurred, with the hand's movements indicating a shift in the direction of the action.
- Reference: Across these frames, the package undergoes a visible transformation from a blurred object in motion to a stilled and focused item, indicating the transition from shaking to a pause. The bag inflates progressively, as evidenced by the increasing puffiness, which is a tell-tale sign of the popcorn being heated and popped inside. The person's interaction with the package evolves from vigorous shaking to a careful examination, and finally, to a display and preparation to open, following the instructions for a presumably hot and ready-to-eat snack.


## Interpretation Notes

- BLEU and ROUGE-L measure lexical overlap with reference captions.
- Semantic similarity measures embedding-based caption similarity.
- Temporal alignment aggregates semantic similarity across the four stages.
- Low-similarity cases are candidates for manual review, not confirmed factual errors.
