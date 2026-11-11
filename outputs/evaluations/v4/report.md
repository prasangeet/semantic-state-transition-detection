# OSCaR-Lite Evaluation Report

- Generated: 2026-11-11T16:59:17.741819+00:00
- Samples evaluated: 500

## Temporal Stage Metrics

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic Similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.3430 | 0.1743 | 0.0908 | 0.0484 | 0.2252 | 0.6167 |
| During | 0.3217 | 0.1738 | 0.0912 | 0.0496 | 0.2340 | 0.6185 |
| After | 0.3170 | 0.1715 | 0.0922 | 0.0502 | 0.2322 | 0.6092 |
| Transition | 0.3857 | 0.2104 | 0.1164 | 0.0705 | 0.2593 | 0.6583 |

## Temporal Alignment

- Overall temporal score: 0.6257

| Stage | Semantic Alignment |
|---|---:|
| Before | 0.6167 |
| During | 0.6185 |
| After | 0.6092 |
| Transition | 0.6583 |

## Qualitative Error Analysis

- Similarity threshold: 0.5000
- Low-similarity cases: 462

| Stage | Low-Similarity Cases | Rate | Mean Similarity |
|---|---:|---:|---:|
| Before | 133 | 0.2660 | 0.6167 |
| During | 114 | 0.2280 | 0.6185 |
| After | 122 | 0.2440 | 0.6092 |
| Transition | 93 | 0.1860 | 0.6583 |

### Cases for Manual Inspection

#### Sample 5 — Before

- Similarity: 0.3246
- Prediction: The countertop is cluttered with a variety of items, including a dish towel, a towel, and a plastic container. The counter appears to be in a state of disorganization, possibly due to a recent cleaning or a spill
- Reference: The floor is comprised of square, mustard-yellow tiles with slightly darker grout lines that create a grid-like pattern across the surface. In this scene, a few small, dark specks and light smudges are scattered across the tiles, indicating either bits of dirt or minor stains. The floor's glossy finish reflects some of the overhead lighting, which highlights the imperfections and the wear of the tiles, such as faint scratches and slight discoloration in places, suggesting this is a well-used area.

#### Sample 12 — Before

- Similarity: 0.4265
- Prediction: The trash can appears to be in a position where it's being handled by a person who's holding a white towel or a rag. It's positioned on a counter-top, with a handle attached, suggesting that the person is holding the item. The area around the trash can is cluttered with various items, including dishes, dishes, and utensils. The surrounding area is dimly lit, suggesting a dark ambient.
- Reference: The basket appears to be partially open with some items inside, although the exact content is not entirely discernible due to the oblique angle of the shot. Adjacent to the basket, there's a surface with a blurry orange and red pattern, perhaps a textile or a rug. A portion of a purple object, likely related to the basket or its contents, is visible to the left. The surrounding environment includes a floor with tiles, suggesting an indoor setting.

#### Sample 20 — Before

- Similarity: 0.3626
- Prediction: The package appears to be in the hands of a person who is holding the package. The person's hands are positioned on the side of the package, indicating that the package has been opened. The package's contents are not visible, but it appears to contain a variety of items, such as a toothbrush, toothpaste, and a toothpaste bottle.
- Reference: The yogurt in this frame appears to be in a state of being intentionally arranged. One can observe that a hand is positioning a yogurt container, which is upright and has a lid depicting some form of fruit, likely indicating the flavor. The placement is precise and seems to be part of an organized pattern, with two other yogurt containers already placed in proximity: one upright and another on its side, possibly to showcase the brand or variety. The environment suggests that the action is taking place in a kitchen, given the presence of a microwave, stove, and various kitchen items in the background.

#### Sample 24 — Before

- Similarity: 0.4392
- Prediction: The plastic bag appears to be a thin, rectangular piece of paper, with a slightly curved edge. The paper is positioned on a flat surface, with the edges of the paper overlapping each other, indicating that the paper has been inserted into the bag. The person's fingers grasp the paper, which appears to have been partially pressed against the edge of the bag, suggesting that it has not been fully inserted.
- Reference: A pair of scissors is opened and inserted into a notch of a blue plastic clip, which is mounted on the edge of a packet labeled "Funghi Porcini". The scissors' handles are blue, and the blades silver, with one blade partially inserted into the clip's opening. The person holding the scissors appears to be right-handed, as inferred by the thumb and fingers' positioning. The clip is halfway along the length of the packet, suggesting the intention to either open or reseal it. Surrounding the scene are various kitchen items, including dishes in an orange drying rack, a roll of paper towels, and a white napkin.

#### Sample 31 — Before

- Similarity: 0.3647
- Prediction: The surface of the countertop appears to have been wiped down with a damp cloth, indicating that the surface has been cleaned. The surface appears to be in a state of disorganization, possibly due to a spill or a scrubbing
- Reference: The glass, appearing to be a standard pint-size, is situated upside down on the tabletop, its opening facing down. The translucent material suggests it's made of a typical glass composition, possibly indicating recent usage as there are no visible residues on its inner surface. The base of the glass, now at the top, reflects a smidgen of light, hinting at a relatively clean and glossy finish. The glass is positioned slightly off-center to the left in the viewer's perspective, with ample space around it, undisturbed and static in its placement.

#### Sample 32 — Before

- Similarity: 0.4247
- Prediction: The tomato appears to be in the hands of a person, with a slight hint of movement. The tomato's surface is blurry, suggesting that it's not necessarily fresh, but may be ripe or stale. It's surrounded by a variety of fruits and vegetables, including tomatoes, cucumbers, and greens. The camera's focus is on the tomato itself, which is positioned in a kitchen setting, implying that the tomato has been placed in the refrigerator or freezer for a long period of time.
- Reference: The lettuce is enveloped in a clear, plastic wrap, appearing crisp and fresh with a bright green color that suggests it has been recently purchased or harvested. The leaves are tightly packed, indicating the lettuce is likely a head of iceberg or a similar variety, known for its dense, rounded shape. The plastic wrap is intact, with no visible tears or openings, preserving the lettuce's moisture and freshness. The surrounding area is cluttered with kitchen items, but the lettuce is the focal point, resting on a white, rectangular container with grooves, which may be a lid to another container or a cutting board.

#### Sample 33 — Before

- Similarity: 0.4088
- Prediction: The holder of the utensil appears to be in a position where it's positioned on a flat surface. It's slightly tilted, indicating that the holder is positioned in the middle of a kitchen or counter. The handles are slightly angled, suggesting that they're positioned at the edge of the counter. There's no indication of any obstructions or obstructions, implying that there's been any movement.
- Reference: The cabinet appears to be slightly ajar with the door swung open to a small degree, allowing a glimpse of its contents. On the lower shelf, there are visible stacks of cans that seem to be in a neat order, with labels facing forward, making them easily identifiable. Above, on the upper shelf, the blur obstructs a clear view, but it suggests the presence of additional items, possibly more cans or containers, hinting at a well-stocked and organized space. The edge of the cabinet door shows a handle, indicating the manner in which it is meant to be opened further.

#### Sample 36 — Before

- Similarity: 0.3076
- Prediction: The cheese appears to have been removed from its packaging. The cheese has a slightly smoky appearance, suggesting that it has not been fully removed from the packaging, indicating that it is still in its original state. The sandwich's exterior remains unmarked, with no visible markings or markings on the surface of the cheese, which indicates that the cheese has not yet been opened.
- Reference: The butter is encased in a rectangular plastic tub with a bright blue lid, prominently featuring the brand "FLORA" and a sunflower image indicating a light, sunflower-based spread. The lid is securely attached, showing no signs of having been opened. The spread inside is unseen, implying a fresh, untouched state. The tub rests on a kitchen counter, held firmly by a left hand, with the right hand holding a butter knife poised to lift the lid, indicating an imminent action of usage.

#### Sample 38 — Before

- Similarity: 0.4725
- Prediction: The freshly-scooped carrot appears to have been sliced off its stem, indicating that it has been cut off. The carrot remains intact, with the skin still visible, suggesting that the knife has been used to cut it. The knife's edge is slightly curved, suggesting a sharper edge, and the carrot's flesh appears to be ripe.
- Reference: The aubergine lies on a bright green cutting board, its dark purple skin exhibiting a glossy sheen indicative of freshness. The stem end, where it was once attached to the plant, is facing the person handling it, and the opposite end has been cleanly sliced, revealing the creamy, seeded interior. The knife, positioned at the center, is pressed down into the flesh, suggesting the beginning of a longitudinal cut. The person's hand is in mid-motion, steadying the vegetable, with the thumb positioned on one side and fingers on the other, indicating a secure grip.

#### Sample 41 — Before

- Similarity: 0.4381
- Prediction: The stainless-steel sink appears to be in a state of transition, indicating that the sink has been removed from its packaging. The sink's surface is cluttered with a variety of kitchen items, including utensils, kitchenware, and kitchenware. The surrounding area is dimly lit, suggesting that there may be a slight movement in the sink.
- Reference: The milk bottle, with a classic white and yellow design suggesting a standard pasteurized variety, rests on its side near the kitchen sink's edge. Its cap, a vibrant red that contrasts starkly with the bottle's muted tones, is partially obscured from view, suggesting it may not be fully secured. Shadows cast across the bottle indicate ambient lighting from above, and a slight reflection hints at the bottle's glossy surface, likely plastic. The positioning of the bottle, coupled with nearby kitchen items, gives the impression of a hurried or cluttered setting.

#### Sample 45 — Before

- Similarity: 0.3582
- Prediction: The liquid appears to have been poured into a glass container, indicating that it has been placed in a well-ventilated position. The surface of the glass appears to be slightly damp, suggesting that the liquid has not yet been stirred. The liquid's surface is smooth, suggesting a smooth surface, with a slight haze, suggesting the presence of a liquid in the glass container.
- Reference: The jam appears as a concentrated, viscous mass, clinging persistently to the fork's tines, indicating its thick, gelatinous consistency. A prominent dollop of jam rests atop the tines, with its deep red hue and glossy sheen suggesting a fruit-based composition, likely berry. The surface tension of the jam is evident, with the mass not yet succumbing to gravity, hinting at the presence of pectin which is common in jams to give them structure.

#### Sample 51 — Before

- Similarity: 0.4514
- Prediction: The trash can appears to be in a dark, cluttered environment, with a lid and a plastic lid, indicating that it has been removed. The contents of the trash can are scattered around the room, including dishes, dishes, and utensils. The surrounding area is dimly lit, suggesting that there is a person or a group of people in the vicinity.
- Reference: The image captures a cylindrical filter component, partially obscured by the person's hand as they are in the midst of removing or inspecting it. The filter's exterior is predominantly white, with some areas of discoloration, suggesting it may have accumulated dust or other particulate matter. The top portion of the filter appears to be a semi-transparent material, possibly a fine mesh designed to trap contaminants. The texture of the surface suggests a fibrous material, commonly used in filters to enhance their trapping capability. There is visible debris collected on the filter's surface, indicating it has been in use and is performing its function of purifying the air or water it is designed for.

#### Sample 54 — Before

- Similarity: 0.4184
- Prediction: The marble is submerged under a stream of water, indicating that it is in the process of being rinsed. Its interior is cluttered with soapy suds, suggesting that it has been soiled or washed. The glass appears to be partially submerged in the water, suggesting the presence of a detergent solution. The surrounding area is saturated with water, which suggests that it may be time to rinse the marble.
- Reference: The mug appears partially obscured by a yellow-gloved hand holding a sponge. Its interior is not visible, indicating it is facing downwards. Water droplets and suds are present on the surface, suggesting it has been subject to washing. The mug's handle is visible and points to the left, slightly upward, indicating its position as resting on the sink's edge or possibly in the hand of the individual washing it. The surrounding environment is cluttered with dishes and washing paraphernalia, such as a bottle of Fairy dish soap and a blue dish brush nearby, which adds to the sense that the mug is in the midst of a cleaning process.

#### Sample 56 — Before

- Similarity: 0.3262
- Prediction: The jar appears to be in a kitchen setting, with a lid positioned near the edge of the kitchen counter. It is positioned on a countertop, with the lid facing downwards, indicating that the jar is in the kitchen. The surrounding area is cluttered with various kitchen items, such as utensils and kitchenware, and a variety of kitchen items such as pots, pans, and other household items are visible, including a stove, oven, microwave, and refrigerator.
- Reference: The packaging appears largely intact but slightly compressed at the top, suggesting the initial stages of crumpling. The shiny blue and silver hues reflect light, indicating its metallic nature, likely aluminum. A human hand with a fair complexion is visible, with fingers gently curving around the top part of the packaging. This crumpling action has not yet deformed the original cylindrical shape significantly, leaving the majority of the packaging still resembling its original form.

#### Sample 63 — Before

- Similarity: 0.4996
- Prediction: The jar appears to be in the hands of a chef, with a large bowl containing a variety of ingredients. It is positioned on a kitchen counter, surrounded by a mixture of white and yellow liquids, which are scattered around the jar, indicating that the ingredients have been added to it. The contents of the bowl are scattered across the counter, suggesting that they have been incorporated into a recipe.
- Reference: A bowl sits on a countertop cluttered with various kitchen appliances and items, holding a mixture that appears to be in the initial stages of preparation. In the bowl, there is a raw egg, its yolk intact and sunny, surrounded by a clear viscous albumen, with flecks of black pepper scattered throughout, providing a stark contrast to the pale yellow and translucent whites. The egg has been cracked open recently, as suggested by the lack of disturbance in the albumen and the yolk's domed shape, indicating minimal interaction with the fork lying beside it.

#### Sample 71 — Before

- Similarity: 0.4963
- Prediction: The bottle appears to be in the hands of a young woman, with her hands clasped in the palm of her hand. The bottle is positioned in a kitchen setting, with a bottle in the middle of the room, indicating that it is ready to be used. The scene's focus is on the bottle, which appears to have been opened, and the bottle's contents, such as milk, vinegar, and sugar, appear to be dispensed.
- Reference: The degreaser in question appears to be in a state of rest, positioned on a clean, off-white tabletop. The bottle is upright, with its nozzle directed upwards, and no visible spray is being emitted. Its label is facing away from the viewer, obscuring any brand or usage instructions that may be present. The cap seems to be firmly attached, and the trigger is in a neutral position, suggesting it hasn't been recently pressed. The surrounding area is free of any visible residue or signs of degreaser application, indicating that the cleaning action has yet to commence.

#### Sample 72 — Before

- Similarity: 0.4770
- Prediction: The jar appears to be in the hands of a person who has just finished preparing a meal. It's placed in a kitchen sink, with a lid and a handle, suggesting that it's being handled by someone who's not yet finished. The kitchen sink appears to have a removable cover, which suggests that the jar may have been used as a dishwashing solution. The sink's interior is cluttered with various items, including dishes, dishes, and utensils, indicating that there's a lot of work to be done.
- Reference: A saucepan lid with a convex, metallic surface is being grasped by a person's hands, which are wrapped in a white cloth, likely to prevent direct contact with heat or to provide a better grip. The lid's underside is partially visible, showing a concentric circular design characteristic of such lids, where the central part often holds a knob or handle. The surrounding kitchen environment is slightly blurred, with stacked dishes and kitchen utensils nearby, suggesting the midst of kitchen activity, possibly during or after meal preparation.

#### Sample 74 — Before

- Similarity: 0.3396
- Prediction: In this frame, the amount of sugar in the mixture appears to be a little less than a teaspoon, suggesting that the sugar has been incorporated into the mixture. The spoon-like texture of the sugar is reminiscent of a powdered sugar paste, with a slight smoky hue to it, indicating that it has been stirred or poured into a bowl.
- Reference: The scale is a compact, digital model with a clear glass platform, resting on a black granite countertop. It is positioned to the right side of the bowl filled with a white powdery substance, presumed to be flour. The scale appears to be turned off, as no digital numbers or lights are visible on its display. It is situated next to an open notebook, with its top edge aligned with the spiral binding, suggesting that it might be used for recording measurements. Surrounding the scale are scattered ingredients and kitchen tools, indicating an ongoing cooking or baking process.

#### Sample 86 — Before

- Similarity: 0.3699
- Prediction: The plastic bag appears to be in the hands of a person, with its contents being placed in a plastic bag. The bag is partially open, with the contents of the bag being placed on a counter, indicating that the bag has been opened. The camera's focus is on the bag's interior, which is cluttered with a variety of items, such as a toothbrush, toothpaste, and a mug.
- Reference: The leek, freshly uprooted from its packaging, appears in the process of being transferred, likely from a shopping bag onto a household surface, possibly in preparation for storage or cooking. It's held at one end, with the root tip facing downwards, suspended mid-air, showcasing its full length and firm, layered structure. The white base transitions into a deep green, with the tightly wrapped, flat leaves that are characteristic of leeks. The plastic wrap encasing it is slightly puckered, indicating the initial grip that preceded the motion captured.

#### Sample 88 — Before

- Similarity: 0.4933
- Prediction: The lid of the jar appears to be open, suggesting that the lid has been opened. The lid is positioned on a kitchen counter, with a lid in the middle of the container, indicating that it's ready for use. The contents of the lid are clearly visible, with the lid positioned in a position that allows the lid to be fully opened.
- Reference: The food container in view is semi-transparent with a blue rimmed lid, partially ajar, revealing its contents. Inside, a layered arrangement of cheese, discernible by its yellow-white hues and distinctive edging, is stacked with precision. Each slice is partially overlapped by the next, creating an ordered appearance. The container is held by a pair of hands, with the lid being gently lifted, indicating the initial stage of unveiling the contents.

#### Sample 89 — Before

- Similarity: 0.2821
- Prediction: The kitchen sink appears to be in a position where it's positioned on a counter or counter, with a few items scattered around it. The sink's surface is cluttered with various items, such as utensils, napkins, and other household items, indicating that the sink has been used for a long period of time. It's not visible from a distance, but it appears to have been placed in the middle of a kitchen counter, implying that it is a sink or a countertop sink.
- Reference: The squash container, predominantly white with touches of blue, rests atop a gray counter. It stands upright, showcasing its slender and elongated design. The label, although not entirely discernible, carries hints of blue and green graphics, likely illustrating the flavor or variety of the squash. Adjacently, a white cap lies on the counter, suggesting it's been recently removed or will be placed back on the container.

#### Sample 95 — Before

- Similarity: 0.4411
- Prediction: The plastic bag appears to be partially open, with a portion of the bag positioned in front of the person. The bag's contents are clearly visible, as well as the contents of a plastic bag, which has been placed in a hands-free position. The person's hands are holding the bag, indicating that the bag has been opened, allowing the person to grasp the bag and place it in the hands of another person.
- Reference: The lettuce is partially visible through the translucent packaging, appearing fresh and green, with leaves that look crisp. The package seems to be a standard pre-washed mixed lettuce bag, often found in grocery stores, with a printed label showing nutritional information and branding. The person's hand grasping the bag indicates it has just been taken out of the refrigerator, as suggested by the cold storage ambiance and surrounding items like bottles and other kitchen paraphernalia.

#### Sample 100 — Before

- Similarity: 0.3852
- Prediction: The tea kettle appears to be positioned in a horizontal position, with a slightly tilted position, suggesting that it's positioned close to the edge of a kitchen counter or counter. The kettle's interior is cluttered with various items, including dishes, pots, and utensils, which are likely to be in use for a variety of purposes. The surrounding area is dimly lit, indicating that the kettle isn't in use, and there's no indication of any obstructions or obstructions. The camera's focus is on the kettle, which appears to
- Reference: The image captures an illuminated environment where light diffuses softly across various surfaces, indicating an active light source within the room. The light reflects off the tiled flooring, creating a pattern of highlights and shadows that suggest a glossy finish on the tiles. The countertop to the right also catches the light, indicating its polished surface, and various kitchenware items reflect the light differently, from the metallic sheen of pots and pans to the more subdued reflection of ceramic dishes. The light appears to be emanating from a point above the scene, casting a consistent glow across the room.

#### Sample 101 — Before

- Similarity: 0.3782
- Prediction: The granules of the pesto appear to have been scooped out of a container, indicating that they have been placed in a single layer. The contents are scattered across the surface of the container, suggesting that there is a large amount of pesto in the container. The spoon appears to be holding a small portion of the mixture, which appears to contain a variety of nuts, such as walnuts, almonds, and pistachios.
- Reference: The milk in the container appears to be in an initial stage of stirring, with the surface showing a mild disturbance. There is a visible swirl starting to form, indicating the motion of a spoon or a stirrer recently having passed through it. The consistency of the milk seems uniform and no significant mixing of any added ingredient is apparent yet. The color is a uniform creamy white, and the viscosity appears to be typical of milk, without any signs of thickening or curdling.

#### Sample 102 — Before

- Similarity: 0.3486
- Prediction: The granule of the sugar cane is positioned on a kitchen counter, with a hand in the palm of the hand, indicating that the sugar has been added to the sugar. The sugar is placed on top of a bowl, with the lid firmly closed, suggesting that it is ready to be poured into a container. The contents of the bowl are visible, as well as a handful of sugar, which appears to have been poured onto the sugarcane.
- Reference: The hand blender rests inert in a clear mixing bowl containing a yellowish mixture, possibly a batter or purée. The blender's blue motor housing, with a digital display and silver power button, suggests a modern and perhaps sophisticated appliance. The electrical cord dangles casually over the bowl's rim, and a blue cap, likely a protective cover for the blender's blade, is held in one hand. The ambient lighting reflects off the kitchenware around, and the hand holding the cap appears relaxed, indicating that the blending action has yet to commence.

#### Sample 107 — Before

- Similarity: 0.4603
- Prediction: The mixture appears to be in the hands of a hand mixer, with a small amount of flour and a little bit of water present. The texture of the mixture seems to be a mixture of flour, milk, and water, with the consistency of clumps of dough forming a single layer. The ingredients are scattered across the surface of the mixing bowl, indicating that they have not yet been fully combined. The consistency of the dough appears to have been incorporated into the mixture, suggesting that it has not been fully incorporated. The presence of the flour in the mixture suggests that the flour has not
- Reference: The biscuit appears to be in its initial stage of being pressed, with its texture still visible, suggesting that it has just begun to be mixed or crushed. It's surrounded by an assortment of kitchen appliances and utensils, indicating that preparation is underway. The area looks cluttered, with a glass of something powdery next to the bowl, possibly an ingredient yet to be added. The biscuits retain their integrity to some extent, as the pressing has seemingly just commenced.

#### Sample 108 — Before

- Similarity: 0.4739
- Prediction: The stalk of the broccoli appears to be in a well-grooved state, indicating that it has been thoroughly rinsed. The leaves are held by a person's hand, which indicates that they have been rinsing the broccoli for a few minutes. The water droplets appear to be dripping from the stems, suggesting that the water has been drained out of the leaves. The leaf appears to have been washed under a gentle watering motion, implying that it is still wet.
- Reference: The salad is being held under a running tap, the water cascading over the green leaves and into the stainless steel sink. The leaves appear fresh and vibrant, with a bright green hue indicating their freshness. Droplets of water cling to the surface of the leaves, highlighting their crisp texture. A person's hands are visible, with one hand holding a piece of the salad under the stream of water, suggesting the rinsing process is actively underway. The surrounding area is relatively tidy, with a clear distinction between the washed and unwashed leaves, as the rinsed salad is being separated from the rest.

#### Sample 110 — Before

- Similarity: 0.3221
- Prediction: The cabinet appears to be in a state of transition, with the door open and its contents scattered around the room. The cabinet's interior is cluttered, with a variety of items on the wall, such as pots and pans, utensils, and other household items. There is a slight contrast between the cabinet and the surrounding area, which suggests that the cabinet is not fully occupied.
- Reference: The chair appears in a position where it is partially tucked under a table. The tablecloth is colorful with a pattern, resting on a table with a light-colored surface. The chair itself has a cushioned seat with a light fabric, and the backrest is not visible in this angle. The floor is tiled, reflecting the chair's shadow and some light. The chair is angled such that one leg is closer to the camera, suggesting it may have been in motion or is about to be moved.

#### Sample 112 — Before

- Similarity: 0.4739
- Prediction: The jar appears to be in the hands of a person who is holding the lid. The surrounding area is blurred, suggesting that the jar is not being properly handled. The lid's surface is slightly exposed, suggesting it's being handled by someone who hasn't opened the lid yet. The contents of the bottle appear to be a variety of items, such as condiments, fruit, and spices. The image suggests that the lid is being handled in a kitchen setting, implying that it is likely to be used for a recipe.
- Reference: The image captures a blur of movement, likely due to the camera's swift motion. Amidst this swirl of colors and shapes, the focus is on a partially visible bag of coffee. The bag is not clearly discernible, but the slight crinkling texture suggests it may have been recently handled or is in the process of being moved. The surrounding environment is a jumble of kitchenware and appliances, all blending into the scene's dynamic and hasty vibe.

#### Sample 116 — Before

- Similarity: 0.4709
- Prediction: The carrot is positioned on a cutting board with a sharp edge, suggesting that it has just been removed from the cutting board. It is surrounded by a handful of vegetables, indicating that they are ready to be picked. The carrot's stems appear to be ripe, suggesting they may be ready for harvest. The knife's surface is brightly lit, suggesting a bright green color, implying that the carrot is in the process of being chopped.
- Reference: The ingredients appear to be in the early stages of preparation. A variety of food items are visible, most notably diced sweet potatoes that are collected inside a white bowl. On the countertop, there's evidence of fresh preparation with discarded peels and cut-offs from what seems like vegetables and fruits. To the side, there's a knife resting on a chopping board, indicating recent use. Some other ingredients, like canned goods and possibly some spices or seasonings, are also present nearby.

#### Sample 118 — Before

- Similarity: 0.4736
- Prediction: The image shows a kitchen with a variety of vegetables, including carrots, broccoli, and cauliflower. There is a pot of water on the stove, which appears to be agitating, suggesting that the vegetable has been added to the pan. The surface of the pot appears to have been harmed by a hand-held device, possibly a chopping board or a cutting board.
- Reference: The hob presents a white stove with four gas burners of varying sizes, organized in a traditional layout with two rows and two columns. The burners are capped with black grates, suitable for holding cookware securely. In this scene, a wok is placed on the front right burner, filled with a mix of vegetables that appear to be in the early stages of cooking, indicated by their vibrant colors and rigid textures. The knobs for gas control are aligned on the front panel, each corresponding to one of the burners. The control knob for the wok's burner is turned on, suggesting an active flame heating the pan. A spoon rest lies empty next to the hob, and the wooden countertop that surrounds the stove is clear of any other kitchen utensils or ingredients.

#### Sample 123 — Before

- Similarity: 0.4726
- Prediction: The camera's focus is on the water, which appears to be in a downward motion, indicating that the water has been drained from the tap. The water's surface is slightly blurred, suggesting that there is no water on the surface of the tap, implying that the tap is not functioning properly. There is a slight movement in the direction of the water flow, which suggests that there may be a significant amount of water present in the water.
- Reference: The image captures a blurry motion of a hand submerged under running water from a stainless steel sink faucet, suggesting a vigorous hand-washing action. The hand is oriented palm down, with fingers slightly splayed, and water droplets can be seen splashing around, some catching the light and creating a shimmering effect. The movement of the hand and the water creates a dynamic interplay of light and shadow across the hand's surface, indicating a swift motion typically involved in rubbing or cleansing.

#### Sample 124 — Before

- Similarity: 0.3692
- Prediction: The pasta appears to have been stirred, indicating that it has been added to the dish. The ingredients are scattered across the surface of the pasta, which suggests that the pasta has been placed in a pre-mixed state. The pasta's texture is slightly different from that of other pastas, suggesting that it's not yet ready to be added to a dish.
- Reference: The wooden spoon in view exhibits a clean and unused appearance with a smooth, glossy finish indicative of minimal prior usage. The utensil is grasped firmly in the person’s right hand, its bowl facing downwards towards the plate below. The positioning of the spoon, coupled with the direction of the individual's grip, suggests an impending action, likely to involve contact with the plate's contents. The spoon's handle extends towards the edge of the frame, slightly tilted, enhancing the sense of anticipated movement.

#### Sample 142 — Before

- Similarity: 0.4785
- Prediction: The plate appears to be in the hands of a person, with a hand in the middle of the action. The surface of the plate is blurred, suggesting that it's being handled by someone who hasn't yet done so. The camera's focus is on the plate's surface, which appears to have been placed on a flat surface, possibly a table or a countertop. The plate is positioned in a horizontal position, indicating that the person is holding the plate.
- Reference: In this frame, the sausage is not immediately visible, suggesting it may be obscured or hidden beneath other objects on the countertop. Various items, including a bottle, a knife, and a plate, are scattered around the area, which could be potentially concealing the sausage. The dominant visual elements are a person's hands, which appear to be in the midst of handling or interacting with an item, possibly the plate, implying that the sausage might be under it or being prepared for covering.

#### Sample 146 — Before

- Similarity: 0.4996
- Prediction: The saucepan appears to be in a kitchen setting, with a lid and a handle, suggesting that it's a microwave-safe one. The lid is positioned on top of a countertop, with the lid pointing downwards, indicating that the saucepan has been removed from the kitchen. The saucepan's interior is dimly lit, suggesting a low-level view of the kitchen, which suggests that it may be preparing for a meal or a quick meal.
- Reference: The tupperware in the frame is partially visible, with its open side facing downwards toward the counter. It appears to be a rectangular container made of a translucent, frosted plastic that diffuses the view of its interior. The lid is not attached, suggesting that the tupperware has either been recently used or is about to be used. Light reflects off its smooth surface, and the container's textured sides indicate it may have a grip-friendly design. The container is positioned next to a stack of plates and appears to be in motion, as indicated by the slight blur around the edges.

#### Sample 150 — Before

- Similarity: 0.4073
- Prediction: The soap bottle appears to be in a position where it's positioned on a counter or counter, with a hand in the palm of the hand. It's slightly tilted away from the viewer, suggesting that the soap has been swung into the position of the bottle. The bottle's contents are scattered around the room, and there's no indication of the soap's origins.
- Reference: The spice is initially placed in a relatively hidden position within the cupboard, surrounded by various other items such as bottles, jars, and containers of varying sizes and shapes. The visibility of the spice is partially obscured due to its placement and other items around it. There is a sense of stillness, with the spice resting comfortably, untouched and undisturbed in its familiar environment.

#### Sample 153 — Before

- Similarity: 0.3608
- Prediction: The countertop appears to be in a state of disrepair, with a thin, glossy surface and a smattering of dust and debris scattered around it. The area around the counter appears to have been cleaned, and there is a noticeable amount of debris on the floor, suggesting a recent cleaning effort. The counter is positioned on a flat surface, which is likely a reflection of a person's hand or a hand-held device, implying a presence of some type of cleaning action.
- Reference: The pepper mill appears to be in motion, falling towards the ground. The motion blur present in the image suggests rapid movement, and the position of the pepper mill, tilted at an angle, indicates it has just been knocked or is slipping from its standing position. The proximity of the hand and the cloth suggest an attempt to catch or stabilize the falling object. There's a dynamic interaction between the hand, the cloth, and the pepper mill, captured in the midst of an unexpected shift from stability to motion.

#### Sample 158 — Before

- Similarity: 0.4506
- Prediction: The dish appears to be in the hands of a chef, with a slicing knife in the middle of the dish. It is surrounded by a variety of fruits and vegetables, such as bananas, oranges, pineapples, and peaches. The dish is positioned on a plate or counter, with its contents scattered around the table. The menu appears to contain a wide variety of foods and beverages, including ice cream, fruit juices, yoghurt, and ice cubes. There is a slight contrast between the dish and the kitchen, suggesting that the dish
- Reference: The orange rests on a smooth, matte surface, likely a wooden table. Its glossy skin reflects a muted light, emphasizing the deep, sun-kissed hue typical of ripe oranges. There are slight imperfections visible on its skin, perhaps a small scar or two, and minute, pitted details, reminding the viewer of its organic nature.

#### Sample 161 — Before

- Similarity: 0.4586
- Prediction: The strainer appears to be in the hands of a person, with its contents scattered across the surface, indicating that the strainer has been placed in a position where it is likely to be used for a variety of purposes, such as cooking, cleaning, or preparing food.
- Reference: The image reveals the interior of a cylindrical bin, which appears to be a washing machine drum, with a textured white exterior and a dark, shadowy interior. The rim of the drum is partially illuminated by a striking pink and white light source, creating a stark contrast with the darkness inside. A pair of hands, protected by bright yellow rubber gloves, reaches into the drum, suggesting the commencement of a task. The reflection on the drum's surface indicates a nearby metallic object, possibly a utility that is within the vicinity of the bin.

#### Sample 165 — Before

- Similarity: 0.4455
- Prediction: The sponge appears to be in the hands of a person who has just been rinsing, indicating that it has been thoroughly washed. The person's fingernails are visible, suggesting that the sponge is being used for a specific purpose, such as removing a lint or soap residue. The sponge's surface is saturated with water, implying that the water has been drained from the sponge. The water droplets appear to be concentrated on the sponge, which appears to have been squeezed out of the water.
- Reference: The cloth is firmly gripped by both hands, appearing to be undergoing a wringing or squeezing action. Its surface texture indicates it is damp, with the uneven, darker shades suggesting retained moisture. The fabric looks compressed, with creases and folds accentuating the action being performed on it, signifying a focused effort to expel water.

#### Sample 166 — Before

- Similarity: 0.3881
- Prediction: The hand-held image of a kitchen sink appears to be in the hands of someone who has just finished preparing a meal. The kitchen sink is positioned on a counter, with a white countertop and a stainless steel sink, indicating a sink or dish. The sink's faucet is located near the sink, and there is a water bottle nearby, suggesting that the sink may have been used for a quick rinse.
- Reference: The bottle appears almost centrally placed on a wooden surface, lying on its side with the cap partially obscured by the hand of a person. This person's hand is also grasping a sponge or cloth, hinting at a cleaning activity possibly having just occurred. The bright red cap of the bottle is not fully tightened, suggesting either recent use or preparation for use. Surrounding the bottle are various other cleaning supplies, including a clear plastic bottle and a green bottle with a label, creating a cluttered but utilitarian atmosphere.

#### Sample 170 — Before

- Similarity: 0.4817
- Prediction: The salt appears to be in the hands of a young girl, whose fingers are firmly grasped, indicating that she is about to eat it. The salt has a slightly smoky hue, suggesting that it's ripe and ready to be used. The rim of the salt container is slightly curved, suggesting a slight downward movement, implying that the salt has just been added to the brine. The olives appear to be freshly squeezed, suggesting they've been soaked in brine for at least a few minutes. The
- Reference: A hand is captured in the midst of a dynamic action, positioned above a plate of freshly sliced tomatoes, holding a dual-sectioned spice shaker with a clear body, revealing two separate compartments containing white and darker granules, presumably salt and pepper. The motion is frozen in time, with a small mound of the darker spice poised on the edge of the shaker, suggesting that some of the contents have already been dispensed onto the tomatoes. The scene is indicative of seasoning in progress, with the intent to enhance the flavor of the tomatoes.

#### Sample 183 — Before

- Similarity: 0.4491
- Prediction: The stovetop appears to be in a state of disrepair, with a smattering of grime and grime on the surface. The burner appears to have been recently cleaned, and there is a noticeable amount of grease on the bottom of the burner, suggesting that it may be time to clean the burners. A hand-held camera captures a person's movements, indicating that he or she has just finished cleaning the stovetop.
- Reference: The table appears to be a part of a kitchen counter. On its surface, there are multiple objects: a set of stove burners, a dish rack filled with clean dishes, and a sink next to the dish rack. There is also a piece of meat, possibly ham, placed on a green cutting board. Adjacent to these items, a person's hand can be seen holding a cloth, indicating an action, possibly wiping or cleaning. There's a water bottle near the stove and some other objects near the sink. The table appears to be made of a white material, possibly a type of stone or laminate, and has a smooth surface.

#### Sample 185 — Before

- Similarity: 0.4512
- Prediction: The timer is positioned on a white background, with a blue screen surrounding it, suggesting that it is in the middle of a busy kitchen or kitchen setting. The display's interior is cluttered with various items, including a microwave, a toaster, and a kitchen sink. The camera's focus is on the control panel, which appears to be positioned in a horizontal position, indicating that the timer has been turned on. The surrounding area is dimly lit, suggesting a dark ambient.
- Reference: The oven’s digital display is highlighted in bright red, showing a temperature setting of 180 degrees, likely in Celsius given the context. This specific reading indicates a moderate baking temperature, commonly used for a wide range of dishes, from baked goods to casseroles. The reflective glass surface of the oven door mirrors the interior racks and elements, hinting at a clean and possibly recently unutilized state. The user's hand, adorned with a fitness tracker, suggests an attention to detail and precision, pressing a button on the control panel likely to adjust the temperature, as indicated by the finger's position.

#### Sample 187 — Before

- Similarity: 0.2213
- Prediction: The hand appears to be positioned in a circular motion, indicating that the hand is currently in motion. The hand is positioned on a table or counter, with a few other objects in the background, such as a dish or a pot of soup. The hands are in close proximity to each other, suggesting that they are engaged in some sort of activity. The camera's focus is on the hand's surface, which suggests that it's positioned at the edge of a kitchen counter or counter.
- Reference: The chicken appears to be in the initial stages of preparation, with a few pieces lying irregularly on a wooden chopping board. The pieces are uneven in size and shape, suggesting they have been roughly chopped, and the texture looks somewhat ragged, indicating a less than smooth cut, possibly due to the use of a non-professional or slightly blunt kitchen knife. The board itself has a few stray chicken pieces scattered about, and there is no sign of any seasoning or marinade on the meat, implying the chicken is plain and possibly recently removed from its packaging.

#### Sample 193 — Before

- Similarity: 0.3467
- Prediction: The potato appears to be in a state of transition, indicating that it has just been cooked and is ready to be served. The knife's surface is slightly uneven, suggesting that the meat has been removed from the pan, which indicates that it's time to slice it. The texture of the potato is reminiscent of a slicing board, with a sharp edge and a smooth surface, suggesting a well-balanced cooking process. It's a medium-sized piece of meat, weighing between 1 to 2 lb., with an average thickness of about 1 to
- Reference: A wooden cutting board is positioned over the edge of a stovetop, featuring several freshly cut, irregularly shaped pieces of tofu, each exhibiting a spongy texture and a pale cream color, indicative of firm tofu that has not yet been cooked or seasoned. The tofu appears moist, likely from being recently pressed or cut, with small beads of water visible on its surface. The board shows remnants of moisture and small bits of tofu residue, suggesting it has been used to cut the tofu into these sizable chunks.

#### Sample 197 — Before

- Similarity: 0.4202
- Prediction: The paper rests on a flat surface, with a slight crease in the middle, suggesting that the paper has been placed in a position where it is likely to be used for a recipe. The paper appears to be positioned in the center of the room, indicating that it's being used to make a dish or to cook a meal.
- Reference: A pot with a steamy lid sits atop a gas stove, indicating something is being cooked. The stovetop is stainless steel and reflects the surrounding items, including another pot and a grater. The kitchen counter appears messy with a spill near the stovetop, and various kitchen tools are strewn about, including a grater, a pair of tongs, and a bottle, possibly of oil or vinegar. A person's arm is in motion, wiping the counter with a white paper towel, suggesting an attempt to tidy up. The blurred motion of the hand implies swift movement, likely in the midst of cleaning.

#### Sample 210 — Before

- Similarity: 0.3588
- Prediction: The board appears to be in a state of disrepair, indicating that it has been thoroughly cleaned. The surface of the board is cluttered with debris, including leaves, leaves, and debris, suggesting that it may be in need of a thorough cleaning. The board's surface appears to have been soiled, with a smattering of food particles clinging to the surface, implying that it was recently washed.
- Reference: The image captures a partially translucent bar of soap that has been used to some extent, evident from the smoothed edges and rounded corners. It rests against the vivid green surface of a plastic cutting board, with suds and water droplets scattered across the board's surface, indicating recent or ongoing washing activity. The bar of soap appears slick and wet, reflecting the light in the room, which enhances its glossy appearance. It's held firmly by a person's hand, suggesting a deliberate action of cleaning or scrubbing is taking place.

#### Sample 211 — Before

- Similarity: 0.4762
- Prediction: The cloth appears to be in the hands of a person who has just been rinsing, indicating that he or she has just finished a thorough cleaning. The cloth's surface is slightly damp, suggesting that it's still wet, and there's a noticeable amount of moisture on the surface of the cloth, which suggests that it may be wet or damp. The person's fingers are pointing at the fabric, which appears to have a slight wrinkly appearance, possibly due to the presence of water.
- Reference: The sink is in a state of disarray with a single carrot peel resting on the wooden counter, indicating recent use. Water splashes and droplets are scattered around the sink area, and on the metallic surface, signifying that it has been recently rinsed or used. The sink itself is a stainless steel dual-basin with the right side featuring a garbage disposal cover. The basin is dry, and there are no dishes, soap, or sponges within it, suggesting that a cleaning activity may have just commenced or concluded. A person's hands are visible, one holding a damp rag, which is poised as if in the middle of a wiping motion, suggesting that cleaning is underway.

#### Sample 220 — Before

- Similarity: 0.3449
- Prediction: The image of a freshly washed kitchen sink appears to be being held by a person who has just started to rinse it. The water droplets appear to be dripping from the sink's faucet, indicating that the water has been sucked out of the sink. The person's hand is holding the sink, which is positioned in a horizontal position, with a water droplet in the center of the hand, pointing toward the sink and a sprinkling of water on top of it.
- Reference: The cucumber appears to be partially washed, with beads of water dotting its surface, reflecting the overhead light. It's held firmly in one hand while the other hand grips a kitchen knife, poised as if in the midst of slicing. The cucumber's dark green skin shows slight variations in hue and a fresh, firm texture. The hand holding the cucumber has visible knuckles and fingers, suggesting a gentle but steady grip, indicative of a task performed with care.

#### Sample 223 — Before

- Similarity: 0.4839
- Prediction: The jar appears to be in the hands of a person, with the lid open, suggesting that the contents of the jar have been removed. The lid is positioned on a kitchen counter, indicating that it has been opened, and a hand is grasping the lid, revealing a portion of the contents inside. The fingers of the hand are holding the lid in place, suggesting the contents are being removed from the container. The bottle's contents are not visible to the naked eye, implying that the person has not yet opened it.
- Reference: The tuna can appears to be sealed, indicating that it has not yet been opened. The individual's fingers grip the can's edges, while the other hand seems poised to interact with it, possibly preparing to use an implement or just beginning the process of opening. The aluminum lid of the can reflects the ambient light, showing no signs of puncture or any openings.

#### Sample 225 — Before

- Similarity: 0.4336
- Prediction: The hand-held blender is positioned on a kitchen counter, with a bowl in the center, indicating that it has been placed on the counter. The blender's handle is visible, suggesting that the user is holding the blender in a hand. The surrounding area is cluttered with various tools, including a broom, a blender, and a handful of kitchen tools. The camera's focus is on the blender, which appears to be in motion, displaying a well-balanced mixture of white and blue, suggesting a smoother operation.
- Reference: The mixture presents a vivid yellow hue, likely indicative of egg-based ingredients, with visible streaks of white and patches of different consistencies, suggesting the initial incorporation of ingredients. There is a discernible unevenness, with some areas appearing more liquid and others showing soft peaks, possibly from an uneven mixing speed or the starting phase of ingredient integration. The surface reveals air bubbles being folded into the blend, a sign of the mechanical action from the beaters beginning to aerate the mixture.

#### Sample 226 — Before

- Similarity: 0.4808
- Prediction: The packaging of a plastic bag appears to be in a state of transition, indicating that the bag has been placed in the hands of someone who is preparing to use it. The packaging is positioned on a flat surface, with a single hand holding the bag, suggesting that the person is engaged in the process of removing the plastic bag from its packaging. The bag is a clear plastic container, which indicates that it is being handled by a person or a family member. The contents of the bag appear to be a variety of different foods, such as fruits, vegetables, and dairy products,
- Reference: The wrap is shown partially unrolled across the kitchen counter, with a length of it stretched out over the edge. The hand holds a pair of blue scissors, positioned midway on the wrap, suggesting the intention to cut. The wrap exhibits a degree of static cling, sticking to itself slightly, and has a translucent sheen under the kitchen lights. It is placed over a foil-lined tray, indicating a step in a food preparation process. The serrated edge of the box is visible, indicating that the roll was likely tugged from its container with some force.

#### Sample 228 — Before

- Similarity: 0.4506
- Prediction: The lemon squeezer is held in a hand-held position, with a sprinkling of soap suds and a drop of water nearby. The person's fingernail appears to be slicing the lemon under the faucet, indicating that the lemon has been washed or is still wet. The lemon's surface appears to have been rinsing with soap and water, suggesting that it may have been rinsed. The water droplets on the side of the lemon indicate that the water has been sprayed or is being rinsed, implying that
- Reference: The saucepan lid is gripped firmly with a yellow and green sponge, its surface covered with soap suds, indicating the initial stage of the cleaning process. The lid appears to be positioned upside down, as the knob, usually on the top, is not visible, suggesting that the underside is being scrubbed. The surrounding area is cluttered with various other washed items, and the faucet above is off, focusing the scene on the cleaning action at hand.

#### Sample 235 — Before

- Similarity: 0.4820
- Prediction: The holder of the oven mitt appears to be in a kitchen setting, with a handful of food items scattered around it. It is positioned on a counter, near a microwave, and appears to have been removed from the kitchen counter, possibly due to a recent meal or cooking session. The oven's interior is cluttered with various items, including utensils, dishes, and other household items, and the oven is visible from a distance, indicating that the oven hasn't been fully emptied.
- Reference: The grater is positioned almost centrally in the scene, lying flat on its side with its shredding surface visible. It's resting on the kitchen counter, with its handle extending towards the bottom right corner of the frame. The metallic surface appears to be clean with no visible residue, suggesting it may have been recently used or is about to be used. Surrounding the grater are various kitchen utensils and containers, creating a busy but common kitchen countertop scene.

#### Sample 238 — Before

- Similarity: 0.4891
- Prediction: The sugar jar is positioned in a kitchen setting, with a lid and a sprinkling of food on the counter. The jar's contents are visible from a distance, indicating that the sugar has been added to the jar. The container's interior is dimly lit, suggesting that it is not yet ready to be used. The sugar bottle is placed on a counter, with its contents scattered around it, implying that it has not yet been removed from the kitchen.
- Reference: A glass jar, nearly full of white flour, is being tilted over a large mixing bowl, allowing a gentle cascade of flour to fall into the bowl. The flour appears fine and powdery, suggesting a soft, sifted texture. It forms a small mound within the bowl, and there's a visible dusting of flour escaping into the air, reflecting the light and creating a soft haze around the jar's opening. The flow from the jar is steady but controlled, indicating a careful pouring motion by the person handling the ingredients.

#### Sample 241 — Before

- Similarity: 0.2786
- Prediction: The slice of bread appears to be in the hands of a young woman, with her hands firmly pressed against the edge of the bread. It is surrounded by a variety of fruits and vegetables, including bananas, strawberries, and oranges. The texture of the slice is slightly different from that of other slices of bread, but it appears to have a slight hint of freshness, suggesting that it may be a fruit or vegetable.
- Reference: A red soup ladle with a long handle is resting inside a deep, circular white bowl. The bowl is placed on a white paper plate that shows remnants of food particles, suggesting a meal was recently consumed. Adjacent to the bowl is a clear glass, about a quarter full with a yellowish liquid, possibly a beverage. The table setting includes a folded yellow napkin under the bowl and a portion of a white paper plate visible in the foreground, suggesting the presence of another dining space opposite the viewer.

#### Sample 245 — Before

- Similarity: 0.3779
- Prediction: The tomato appears to have been sliced and placed on a cutting board, indicating that it has been removed from its packaging. The texture of the tomato is reminiscent of a freshly-blended salad, with a vibrant orange hue, contrasting with the rest of the ingredients. The tomato's surface is a mixture of white and yellow, suggesting that it may have been used as a preservative or a seasoning.
- Reference: The egg in this frame is intact and appears freshly cracked into the white bowl, with both yolks whole and centrally located, untouched by the fork lying next to the bowl. The translucent albumen encases the deep orange yolks, which are uniform and undisturbed, suggesting that the egg has not been manipulated since being opened. The stark contrast between the bright yellow yolks and the white bowl accentuates the egg's freshness and the stillness of this initial stage of preparation.

#### Sample 248 — Before

- Similarity: 0.3625
- Prediction: The button on the control panel appears to be in motion, indicating that the button has been pressed. The button is in a horizontal position, suggesting that it is in the position of a button. The surrounding area is cluttered, with a white surface and a blueish-blue color scheme. The buttons appear to be placed on the side of the door, suggesting they are being used for a specific purpose, such as a washing machine.
- Reference: The light switch appears to be in an inactive state, with the toggle buttons in a neutral position, not pressed down. The ambient lighting in the room remains dim, indicating that the electrical circuit connected to the light source is incomplete. The shadow cast on the wall by the hand and the switch assembly suggests a faint light source elsewhere in the room, not from the intended fixture, and the overall atmosphere is one of low illumination.

#### Sample 252 — Before

- Similarity: 0.2501
- Prediction: The cheese appears to be freshly sliced, with a thin layer of cheese surrounding it, suggesting that the cheese has been placed in a single layer. The cheese is positioned on a white plate, indicating that it has been sliced and placed on the plate. The sandwich appears to have been placed on top of a slice of bread, with the bread resting on the edge of the plate, suggesting the bread has been removed from the plate and placed onto a plate.
- Reference: The cake presents as an almost complete ring, set against a decorative lace doily. It appears to be a dense, golden-brown bundt cake with a moist-looking crumb, suggesting a rich and buttery composition. A single slice has been neatly removed, placed back in its original position, slightly askew to indicate it has been cut. Crumbs dot the doily around the cake's base, and the inner circle of the bundt shape is clear, revealing the doily's intricate pattern.

#### Sample 253 — Before

- Similarity: 0.4740
- Prediction: The pan appears to be sprinkling with soap and water, indicating that it has been thoroughly rinsed. The soap's surface is slightly damp, suggesting that the soap has been dipped in soapy water. The pan's handle is positioned at a 45-degree angle, pointing downwards, implying that it's being handled by a person who's just started cleaning.
- Reference: The rag, mostly blurred due to motion, is clutched by a hand and seems to be in the process of wiping or cleaning. The fabric appears to be somewhat damp, reflecting light in certain areas, indicating moisture. There's a sense of dynamic movement in the rag's position, with the fabric bunching up slightly under the pressure of the hand.

#### Sample 258 — Before

- Similarity: 0.2232
- Prediction: The can opener appears to be in the hands of a person who is attempting to remove the contents of the can. The person's fingernails appear to be pointing at the can, indicating that the can has been removed from its packaging. The man's fingers are positioned against the can's edge, implying that they are engaged in the process of removing the contents.
- Reference: The rectangular dish, positioned in the lower left quadrant, displays a well-used appearance with burnt-on residues covering its inner surface. A smattering of droplets surrounds the pan, suggesting recent attempts at cleaning or soaking. The wear and stains indicate that the dish has likely been through a cooking process that involved high heat, such as roasting or baking, which has resulted in the caramelization of food remnants adhering persistently to the metal.

#### Sample 260 — Before

- Similarity: 0.4137
- Prediction: The countertop appears to be in a state of disrepair, with a smattering of crumbs and debris scattered around the surface. The surface is cluttered with crumbs, which appear to have been strewn onto the countertop, resulting in clumps of food or other items on the countertop. The area around the countertop is mostly unoccupied, with no visible signs of use or activity, suggesting that there may be a lack of a proper cleaning solution or cleaning solution. The counter's surface appears to contain a variety of items, including paper towels,
- Reference: The frame captures a moment within a kitchen environment, where it seems that a recent spill has occurred. There's a visible wetness on the countertop, possibly indicating the initial application or spillage of the detergent. The image doesn't show a direct spray action, but there's an implication of a recent spray given the freshly wet appearance. Adjacent to the spill, there's a hand that appears to be preparing to wipe or clean up the liquid.

#### Sample 265 — Before

- Similarity: 0.4053
- Prediction: The cheese is in a sealed plastic container, with a tangerine-yellow color that contrasts with the rest of the packaging. The cheese has a slightly frothy appearance, indicating that it has not been fully opened. The package's contents are not visible, but the contents of the plastic are visible. The person's fingers grasp the cheese's surface, which indicates that the cheese has been properly sliced.
- Reference: A bag of coffee is positioned in the center of the frame, placed on a well-used wooden cutting board. The bag appears to be sealed, with no visible tears or openings. It is oriented such that the top of the bag, presumably where the resealable track runs, is facing directly upwards. The person's hands are just beginning to interact with the bag, fingers positioned on the sides, indicating an intention to open it. Surrounding the bag are various kitchen items, but the coffee bag is the clear focal point, untouched and intact.

#### Sample 267 — Before

- Similarity: 0.4996
- Prediction: The jar's lid is positioned on a kitchen counter, indicating that it has been opened, and the contents of the jar are being poured into the container. The hand grasping the lid appears to be holding the lid open, suggesting that the contents have been poured from the can. The lid's shape is reminiscent of a jar opener, with a sharp edge pointing downwards, suggesting the contents may have been squeezed out of the can's contents.
- Reference: The sweetcorn is sealed within a can, the top of which is intact and unopened. It sits on a white cutting board, surrounded by the remnants of previously chopped red onions. The can's label faces upwards, displaying its contents to the viewer, and no tools are present to suggest the beginning of an opening process. The environment suggests the preparation of a meal, likely involving the sweetcorn as a topping, indicated by the presence of two pizzas in the background awaiting further ingredients.

#### Sample 275 — Before

- Similarity: 0.4732
- Prediction: The coffee pot appears to be in a hand-held position, with a handle pointing downwards, indicating that it has been inserted into the pot. The camera's focus is on the pot's interior, which appears to have a slightly tilted angle, suggesting that the pot is positioned at a slight angle. The surrounding area seems to be a kitchen setting, implying that it is likely to be used for cooking or brewing.
- Reference: The cap burner in this frame is positioned amidst other objects within the vicinity. It seems to be resting securely on the burner base. The reflection and shadow patterns on its surface suggest ambient lighting from above. The cap's edges are distinct, and the inner section shows slight color variations, possibly from usage or lighting effects. The immediate surroundings have other kitchen items, but the cap burner is the focal point.

#### Sample 277 — Before

- Similarity: 0.4471
- Prediction: The sponge appears to be in the hands of a person who has just been rinsing its contents. The water droplets on the surface of the sponge are visible, indicating that it has been thoroughly washed. The sponge's surface is saturated with water, suggesting that the water has been drained from the sponge. The hand is holding the sponge in its hands, with the fingers firmly gripping it, implying that the sponge is in the process of being rinsed.
- Reference: The cloth is being held tightly in a person's hands, with the fingers clenching a section of it, causing it to bunch up and form wrinkles. Water from the faucet cascades down onto the cloth, which appears saturated, as indicated by the darker coloration of the blue fabric and the visible water droplets on its surface. The force of the water creates a small splash zone around the area where the stream hits, with tiny droplets visible in the air just above the cloth.

#### Sample 281 — Before

- Similarity: 0.2942
- Prediction: The table appears to be in a state of disrepair, with a smattering of dust and debris on the surface of the table. A hand-held camera captures a person's movements, indicating that he or she is cleaning a table. The table's surface appears to have been wiped down, suggesting that it has been scrubbing or washed, and the area around the table appears slightly damp, suggesting a presence of dust or debris.
- Reference: A hand is pressing the nozzle of a spray bottle, emitting a fine mist of detergent onto a white surface. The detergent disperses in small, glistening droplets, creating a slightly irregular pattern due to the angle and pressure of the spray. The light reflects off the droplets, highlighting their presence against the matte finish of the surface. The shadow of the person holding the bottle is cast over the area, suggesting an indoor setting with a light source above.

#### Sample 282 — Before

- Similarity: 0.4327
- Prediction: The garlic clove is in the hands of a person, whose fingers are firmly pressed against the skin of the clove. The clove's skin appears to be partially detached from the skin, suggesting that the clove has been removed from its natural state. The garlic's cloves are scattered around the clove, indicating that they've been partially peeled.
- Reference: A translucent, slightly crumpled piece of onion skin rests precariously on the edge of a white cutting board. The board is sprinkled with flecks of freshly chopped green herbs and minute pieces of onion, indicating recent use. A person's hand is caught in motion, with fingers partially open, as they have just released the onion skin. The skin itself catches the light, giving it a slightly glossy appearance amidst the otherwise matte surroundings of the kitchen counter.

#### Sample 289 — Before

- Similarity: 0.4845
- Prediction: The jar is held under a faucet with a stream of water, displacing a small amount of soap and water. The water flows into the jar's interior, creating a flow of soap suds, resulting in a foam-like consistency. The glass is held at a 45-degree angle to the water's surface, exposing a thin layer of water that appears to be clinging to the bottom of the glass, causing it to become brittle and sticky.
- Reference: The tupperware appears as a clear plastic container with a frosted texture, indicating that it has been used and is undergoing the process of cleaning. Water is running from the tap, actively splashing against the interior surfaces, causing bubbles and a dynamic water flow visible inside the container. The person cleaning it, clad in bright yellow rubber gloves, holds the tupperware firmly under the stream, with one hand at the bottom and the other gripping the side, ensuring thorough exposure to the cleansing water.

#### Sample 294 — Before

- Similarity: 0.3134
- Prediction: The stovetop appears to be in a state of flux, with no visible signs of use or maintenance. The surface of the burner appears to have been soiled, with a smattering of grime and grime on the surface, suggesting that the burner is not working properly. A hand-held camera captures a man's movements, indicating that he has started cleaning the stovetop.
- Reference: The towel appears to be a crumpled mass of white fabric, lightly soiled with what could be remnants of food or grease, suggesting recent use in wiping or cleaning. It's held loosely in the hand, with fingers slightly curled around it, indicating a casual or in-between action moment. The texture of the towel seems soft and pliable, showing no signs of stiffness, and the stains are not overly pronounced, indicating that the towel might still be in a usable condition for further cleaning tasks.

#### Sample 295 — Before

- Similarity: 0.4746
- Prediction: The dish appears to be in the hands of a person who has just washed it. The surface of the dish is covered in soapy suds, suggesting that the dish has been thoroughly rinsed. The hand is holding the dish in its hands, pointing to a circular motion, indicating that it has been sprayed with soapy water.
- Reference: The strainer is held firmly in one hand, positioned under a running tap with water cascading through its numerous vertical slits. Its white plastic surface is dotted with remnants of food particles, particularly concentrated at the base where they seem to resist the rinse. The wear on the strainer's surface suggests frequent use, highlighted by the contrast of clean water flowing over less pristine areas. The strainer's grid-like interior is clearly visible, acting as a barrier to the larger debris while allowing water to pass through.

#### Sample 297 — Before

- Similarity: 0.4353
- Prediction: The chicken appears to have been removed from the kitchen, with no visible signs of cooking. The chicken is positioned on a cutting board, with a knife in hand, indicating that it has been placed on the cutting board. The knife's surface is slightly uneven, suggesting that the meat has not yet been fully cooked. The kitchen appears to be engaged in a process of removing the chicken from its packaging, which suggests that the chicken has not been properly cooked.
- Reference: The cutting board is held at an angle, with the edge slightly elevated over a pan filled with other ingredients. A single garlic clove rests on the board, and it appears partially crushed, with its papery skin still attached but flayed open, indicating that it has been prepared for mincing or crushing. The garlic’s yellowish hue suggests it's fresh, and there's a visible moistness on the clove, possibly from the garlic juice being released due to the pressure applied. The person's hand is positioned as if they have just finished or are about to continue the crushing process.

#### Sample 298 — Before

- Similarity: 0.3478
- Prediction: The utensil appears to have been removed from the pan, indicating that it has been placed in a position where it is likely to be used for cooking. The surface of the pan appears to be covered in crumbs, suggesting that it may have been used for a quick meal. The pan's interior is cluttered with a variety of food items, such as bread, soup, and condiments, and there is a sprinkling of grease on the surface, implying that the pan has been used recently.
- Reference: The gloves appear to be durable rubber kitchen gloves, commonly used for washing dishes or cleaning to protect the hands from water and detergents. They are bright yellow, a standard color which suggests their use in household chores. The gloves extend to the mid-forearm, providing ample coverage. In this frame, the glove on the left hand is gripping a white bowl near the sink, fingers curved around the edge, indicating a firm grip. The texture of the gloves seems slightly wrinkled, a characteristic that often occurs when the material is flexed.

#### Sample 303 — Before

- Similarity: 0.4845
- Prediction: The milk bottle appears to be in a position where the hand is holding the cap, indicating that it has been properly inserted into the bottle. The hand's grip on the bottle is firm, suggesting that the cap is still in its proper position. The bottle's contents are clearly visible, with a single hand grasping the bottle, implying that the person is attempting to remove the cap.
- Reference: The aluminum beverage can is captured in a near-upright position on a wooden table. A person's hand, adorned with a metallic watch, is gently grasping the can from its side, with fingers wrapped around its circumference. There is another circular object on the table, possibly a glass coaster or the can's lid. The table surface has a rich wood grain, with visible streaks and knots, and there's a black mat adjacent to the can.

#### Sample 305 — Before

- Similarity: 0.4236
- Prediction: The stove appears to be in motion, with a pan containing a variety of items, including a pot, a burner, and a stovetop. The surface of the stove is cluttered with various items, such as pots and pans, which are likely to be used for cooking. The stovetop appears to have been turned on, with the burners still visible, suggesting that there may have been a recent change in the stove's settings.
- Reference: The countertop is partially visible, composed of a light-colored, solid surface with few distinct features. To the left, there's a stainless steel double sink with one basin empty and the other holding a plastic dish rack filled with kitchen utensils and plates. A solitary, well-used sponge rests on the divider between the sinks. The countertop adjacent to the sink appears wet, possibly from recent cleaning or dishwashing activities, with water droplets scattered across the surface. Visible in the lower right corner is an individual's forearm, lending a sense of scale and human presence to the scene.

#### Sample 308 — Before

- Similarity: 0.3747
- Prediction: The stainless-steel is held under a faucet with a stream of water, indicating that it has been rinsed or washed. The water droplets on the surface of the stainless steel sink are visible, suggesting that the water has been drained from the sink. The faucet's handle is positioned over the sink's edge, pointing downwards, implying that it is in the process of being rinsed.
- Reference: The baking tray in the image is a large, rectangular, dark-colored vessel, possibly made of metal with a non-stick surface, placed under running water from a white tap. The tray appears quite dirty, with patches of grime and food residue clinging to its interior surfaces, indicating recent use. It’s being held by a person with a silver bracelet on their left wrist, suggesting that they are in the midst of cleaning it. The contrast between the dark tray and the bright yellow tiles of the kitchen adds to the visibility of the soiling.

#### Sample 309 — Before

- Similarity: 0.3681
- Prediction: The knife appears to be in the hands of a person, with its handle pointing downwards. The knife's surface is slightly wet, suggesting that it's being washed, and there's a small amount of water on the surface of the knife, indicating that the knife is still in the process of being rinsed. The kitchen sink appears to have a sprinkling of soapy water on it, implying that the water has been drained from the sink.
- Reference: In this frame, the metallic tap over the kitchen sink is positioned in a downward angle. The faucet appears to be turned off, as there is no visible flow of water emanating from it. The surface of the tap is reflective, and a chain-like apparatus is attached near its base, possibly serving as a plug mechanism for the sink.

#### Sample 310 — Before

- Similarity: 0.4549
- Prediction: The cake appears to be in a pre-heated oven, with a sprinkling of flour and a small amount of baking powder scattered across the surface. The cake is positioned on a parchment-lined baking sheet, indicating that it has been heated to a medium-high temperature, possibly for a few minutes or more. It's surrounded by a thin layer of flour, which appears to have been incorporated into the cake batter, suggesting that the batter has been placed in the oven.
- Reference: The tray appears to be a standard kitchen baking tray with a dull metallic finish, showing signs of wear such as scratches and residual oil coating, which gives it a slightly glossy appearance in spots. On the tray, three balls of dough are placed towards the upper left side, spaced evenly apart from each other. They are formed into rough, rounded shapes, indicating they have been hand-shaped and are perhaps in the initial stages of proofing. The surrounding area of the tray is clear, though small bits of dough and oil streaks are visible, suggesting recent activity of dough being worked on.

#### Sample 313 — Before

- Similarity: 0.4687
- Prediction: The sauce appears to have been stirred, indicating that it has been simmered for a long period of time. The texture of the sauce is reminiscent of a thick sauce, with chunks of meat forming a prominent part of the surface. The sauce's consistency is pronounced, suggesting that the sauce has been added to the pot, resulting in a smooth, creamy texture.
- Reference: The soup appears thick with a hearty consistency, showing a mix of ingredients that include discernible chunks of what seems to be meat and vegetables. Its color is a rich, golden yellow, indicating a possible base of chicken or vegetable broth infused with herbs and spices. As the spoon scoops through the soup, it leaves a trail, revealing the soup's viscous nature and the generous amount of solid components it contains.

#### Sample 316 — Before

- Similarity: 0.4873
- Prediction: The skillet appears to be positioned in the middle of a busy kitchen, with a person's hand near the edge of the pan, indicating that he or she is preparing a meal. The skillet is positioned on the counter, with the handle facing downwards, suggesting that the person is holding a knife or a fork. The cooking surface of the skillet appears uniformly clean, with no visible marks or markings.
- Reference: The hob displays a well-used condition with four burner areas, of which only the front-right burner is active, its red indicator light glowing. A stainless-steel frying pan rests on this active burner, containing several circular slices of food, possibly vegetables like courgettes or eggplants, sizzling as they cook. The adjacent burners remain unused, and a wooden cutting board to the right of the hob holds a variety of spice jars, suggesting preparatory or concurrent seasoning of the food. The control knobs for the burners are all in the off position except for the one controlling the active burner, implying a focused cooking activity on one element.

#### Sample 320 — Before

- Similarity: 0.2695
- Prediction: The mushroom appears to have been partially removed from its packaging, indicating that it has not yet been fully cooked. The texture of the meat appears to be a mixture of white and yellow, with a slight hint of browning, suggesting that the meat is still a medium-sized piece of meat.
- Reference: The sweet potato skin appears freshly sliced, revealing a bright orange interior, indicative of a recent cut. The peel segments are irregular in shape and size, scattered haphazardly on the wooden cutting board, some still attached to chunks of the sweet potato flesh. The edges of the skin are slightly curled up, a natural response to being separated from the dense, moist flesh. One can observe the contrast between the rough, textured outer surface of the peel and the smooth, moist inner surface that was against the sweet potato flesh.

#### Sample 328 — Before

- Similarity: 0.4033
- Prediction: The grocery bag appears to be in the hands of a single person, with its contents scattered around the room. The bag's contents are not visible, but the contents of the bag appear to be a variety of foods, such as cereals, fruits, and vegetables. The packaging appears to contain a wide variety of ingredients, including sugar, salt, and spices, suggesting that the bag is likely to be prepared in a kitchen setting.
- Reference: The slice of bread is being held by a person's hand, captured mid-motion as it's moved towards a toaster. The bread appears to be a piece of wholegrain or multigrain toast, with visible seeds and grains throughout its surface, suggesting a health-conscious choice. The hand gripping it seems to be in the midst of an action, likely having just retrieved it from the bread bag resting on the counter. The bread itself is in focus, with the background slightly blurred due to the movement, emphasizing the slice as the central element of the frame.

#### Sample 329 — Before

- Similarity: 0.3869
- Prediction: The coffee machine is positioned on a countertop, with a coffee maker in the middle of the room. The coffee drips into the coffee grounds, indicating that the coffee has not been properly brewed, and there is no indication that the machine has been fully emptied. The machine's interior is dimly lit, suggesting that it is not yet ready to be used. The surrounding area is cluttered with various items, including mugs, utensils, and other household items.
- Reference: The bag appears to be partially opened, exposing a small section of its contents which look like bread. The bag is of a transparent nature with an orange label, suggesting it could be store-bought bread. The surrounding area includes other household items, but the main focus is the bag with a person's hand reaching towards it, hinting at the intention to open it further or take out its contents.

#### Sample 335 — Before

- Similarity: 0.2964
- Prediction: The mat rests on a flat surface, with a slightly curved edge and a slight crease in the middle, suggesting a smoother surface. The mat's surface is positioned against a white background, indicating it's being used for a variety of purposes, such as a recipe or to make a quick meal.
- Reference: The degreaser appears as a white mist, consisting of fine droplets in mid-air, captured as they disperse across the surface in the upper right quadrant of the frame. The motion of the degreaser is dynamic, indicating that it has just been sprayed from the bottle, which is held in the right hand of the individual. The droplets are densest nearest the nozzle, indicating the recent activation of the spray mechanism. Below the area of the spray, the countertop remains visibly dry, reflecting the light from above, suggesting that the degreaser has not yet had time to settle or spread across the surface.

#### Sample 336 — Before

- Similarity: 0.4889
- Prediction: The canister is held at a height of the kitchen sink, with a water droplet dangling from its handle. The water droplets fall on the inside of the canister, indicating that the water has been drained out of the sink. The tap's handle is held by a person's hand, implying that it's being used for a quick rinse.
- Reference: A hand is gripping a piece of cutlery, a fork, under a stream of water flowing from a silver-colored faucet with a slight curvature. The tines of the fork are positioned downwards, perpendicular to the stream, suggesting the initial action of rinsing. Soap bubbles cling to the base of the tines and handle, indicating recent scrubbing activity. The surrounding area is cluttered, with other kitchen items and a purple sponge visible, and a bottle of liquid soap prominently in the background, contributing to the domestic cleaning context.

#### Sample 338 — Before

- Similarity: 0.4184
- Prediction: The pan appears to be in the middle of a cooking process, with a sprinkling of oil on the surface of the pan, indicating that the pan has been heated to a medium-high temperature. The pan's surface is slightly uneven, suggesting that there may be a small amount of oil left on the pan. The skillet appears to have been placed on a burner, allowing the oil to circulate around the pan while the pan is being cooked.
- Reference: The extractor fan situated above the stove is in a visibly used state, with a distinct pattern of grease and vapor deposits concentrated in the center, spreading outwards to the edges. The coloration of these deposits varies from dark brown at the center to a lighter, amber-like hue towards the periphery, indicating a combination of both recent use and an accumulation over time. The fan's surface has a matte finish, which suggests it is not currently in operation, as an active fan would likely reflect some of the ambient light from the surrounding area.

#### Sample 341 — Before

- Similarity: 0.3568
- Prediction: The stainless-steel dish appears to be in the hands of a person who has just been rinsing the dish. The dish's surface is cluttered with a variety of food items, such as fruit, vegetables, and fruit. The kitchen sink appears to have been soiled, and there is a visible stream of water nearby, indicating that the dish has been thoroughly washed.
- Reference: The tablecloth appears predominantly white with a large, vivid green apple design in the center, suggesting a fresh, crisp theme. It is stretched out across the surface, occupying a significant portion of the frame, with an emphasis on the apple's detailed depiction that includes a spectrum of green shades and visible brush strokes, adding a textured, artistic touch. The tablecloth's edges are not visible, indicating it is fully spread out, and the surface wrinkles suggest it has been used rather than freshly laundered or ironed.

#### Sample 348 — Before

- Similarity: 0.4373
- Prediction: The camera's focus is on the contents of the container, which are a variety of different foods, such as yogurt, ice cream, and fruit juices. The interior is cluttered with various items, including condiments, fruits, and condiments. A person's hand grasps the lid, revealing a small portion of a yogurt container with a lid.
- Reference: The image shows a blurry close-up of a kitchen counter with a spice jar in a state of motion, likely in the midst of being handled. Due to the motion blur, specific details about the spice jar, such as brand or content, are indiscernible. The surrounding environment suggests a domestic kitchen with a stainless-steel appliance, possibly a dishwasher, and a cabinet above filled with an assortment of other spice jars and items.

#### Sample 351 — Before

- Similarity: 0.4442
- Prediction: The cheese is in a sealed plastic container with a lid, which is partially open, indicating that the cheese has been removed from the container. The packaging is clearly visible, with no visible markings or markings on the surface of the cheese, suggesting that it is not being used for any purpose other than to serve as a condiment.
- Reference: The olive oil bottle appears to be a standard size, with a metallic cap that is placed adjacent to the bottle on a black, glossy stovetop surface, reflecting the ambient light. The bottle itself is not in view, suggesting it may be upright and out of the frame or placed elsewhere. The cap is positioned with its open end facing upwards, indicating it has just been removed and set aside temporarily. Nearby, there are scattered items on the stovetop, including a paper bag and what appears to be a packet of food, contributing to a sense of ongoing kitchen activity.

#### Sample 353 — Before

- Similarity: 0.3012
- Prediction: The food processor is positioned on a countertop, with a lid and a bowl in the middle, indicating that the food processor has been placed on the counter. The operator's hand is engaged in the process of removing the lid from the machine, which is currently in motion, and the contents of the bowl are being poured into the bowl. The surrounding area is cluttered with various items, including a food processor, a blender, or a juicer.
- Reference: The button appears to be in a neutral state, unpressed and intact, showing no signs of deformation or displacement. It is situated among a cluster of other buttons, all of which seem to be similarly at rest. The surface of the button reflects a certain amount of ambient light, indicating a smooth, possibly plastic material. Its color blends with the surrounding buttons, suggesting a user interface designed for uniformity. The finger is positioned above the button, casting a slight shadow, but not yet exerting any pressure that would indicate activation.

#### Sample 354 — Before

- Similarity: 0.4799
- Prediction: The rinsed spoon appears to be positioned in a kitchen setting, with the spoon positioned at the edge of the kitchen counter. The spoon's handle is positioned on a counter, indicating that the spoon has been removed from the kitchen and is still in its proper place. Its contents are scattered around the spoon, which suggests that it has been placed in the kitchen, implying that it is being used for a specific purpose.
- Reference: A ladle with a bright yellow handle and a reflective, stainless steel scoop is held mid-air, seemingly captured in the midst of an action. Its position is off-center towards the lower part of the frame, pointing diagonally upwards, suggesting an upward or forward motion. The ladle's handle appears sturdy and ergonomic, with a slight curvature that fits comfortably in a grip, as indicated by the fingers wrapped securely around it. The scene is domestic, with a kitchen countertop visible, and various items such as a wooden spoon resting in a white spoon rest, a clear glass with a green motif, and a plastic water bottle in motion, caught mid-roll towards the edge of the counter.

#### Sample 356 — Before

- Similarity: 0.2536
- Prediction: The timer is positioned in a kitchen, with a microwave on the side, indicating that the timer has been set. The kitchen is cluttered with dishes, dishes, and other kitchen items, including utensils and dishes, which are scattered around the kitchen. The camera's focus is on the kitchen, which appears to be occupied by a handful of people, presumably busy with their daily routines.
- Reference: The mixture in the pan appears to be in the initial stages of cooking, with a moderate amount of clear liquid pooling around the ingredients. Scattered throughout the liquid are green components, which resemble sliced green parts of spring onions or possibly green bell peppers, not yet softened by the heat. Their shapes are irregular, and they float separately in the liquid without clumping together. There is a visible sheen on the surface, indicating the presence of oil or another cooking fat, aiding in the sautéing process. The edges of the mixture are not sticking to the pan, suggesting that it is being stirred frequently or that the heat is appropriately moderated.

#### Sample 359 — Before

- Similarity: 0.4456
- Prediction: The sink appears to have been recently washed, and there is a noticeable amount of water on the bottom of the sink, suggesting that the water has been drained from the sink. The sink's surface appears to be in a slightly damp state, possibly due to the presence of a small amount of soap or water on it. There are a number of items on the counter, such as a sponge, a cloth, or a paper towel, indicating that the sink has been thoroughly rinsed. The area around the sink seems to be cluttered with a variety of items, including
- Reference: The bin is situated in the lower right corner of the image, just beside a white dish rack that houses various kitchen utensils. It appears slightly overfilled, with its contents reaching above the rim, indicating a pressing need for emptying. A clear plastic bag lines the bin, and items within seem to be a mix of food waste and other household refuse, suggesting recent kitchen activity. The positioning of the bin, tucked away under the counter, implies an efficient use of space in a kitchen where activities are underway.

#### Sample 361 — Before

- Similarity: 0.4162
- Prediction: The chicken appears to have been removed from its packaging, revealing a portion of the chicken's skin, which appears to be intact, with no visible signs of cooking or cooking. The fingers of the hand are positioned on the cutting board, indicating that the chicken is still in its packaging. The knife's surface is slightly exposed, suggesting that it is not yet fully sliced, and there is no indication of the contents of the container.
- Reference: The pepper is fully encapsulated in a clear plastic wrap, presenting a vivid contrast against the yellow cutting board. It's nestled between a green and a yellow pepper, suggesting they are part of a multi-colored pack. The untouched plastic suggests the initial stage of the culinary preparation process. The individual's hand is positioned over the green pepper, implying an imminent action, perhaps to commence the unwrapping or cutting. The surrounding area is littered with onion skins and garlic cloves, indicating ongoing cooking activity.

#### Sample 364 — Before

- Similarity: 0.2586
- Prediction: The stainless-steel appliance is positioned on a kitchen counter, with a handful of kitchen supplies scattered around it. The appliance's interior is dimly lit, indicating that the appliance has not been used in a long time. The kitchen sink appears to be positioned at the edge of the appliance, suggesting that there is a lot of work to be done on the appliance.
- Reference: The sweet potato in this frame exudes a fresh and robust appearance. Its skin, mostly smooth with a few natural blemishes, holds a rich orange-brown hue, hinting at its natural earthy origins. The oblong shape of the tuber is accentuated by subtle curves and a slightly tapered end. There's a faint glisten on its surface, perhaps from being freshly washed or due to ambient light. One can almost sense its starchy texture and sweet aroma just by looking at it.

#### Sample 365 — Before

- Similarity: 0.4443
- Prediction: The stovetop appears to be inactive, with no visible signs of use. The burners are positioned on a flat surface, with a few spots of grease and grime, suggesting that the burners have been used for a long period of time. The surface of the burner appears to have been cleaned, with some residue still on the surface, possibly due to a recent cleaning. The area around the stove appears to contain a large amount of grease, possibly from a previous cleaning session. There is a visible handmark on the burner's surface, indicating that it has been cleaned. The
- Reference: The hob surface in this frame appears to have a somewhat creamy-textured substance spread across it. The consistency of the substance gives the impression of a sauce or liquid that has been spilled or is in the process of being cleaned. There's an evident sheen on the surface, indicating the presence of moisture. On the right side of the hob, we can see some containers and kitchen items, and on the left, there appears to be a hand with a blue cloth, presumably in the act of cleaning.

#### Sample 367 — Before

- Similarity: 0.4792
- Prediction: The pot appears to be in the hands of a person, with the lid open, indicating that the liquid has been poured into the pot. The contents of the pot are clearly visible, suggesting that it is being handled by someone. The surrounding area is cluttered with a variety of objects, including a spoon, a mug, and a coffee grinder.
- Reference: The cap appears to be in a dimly lit setting, making the details slightly obscured. From the visible portion, it seems to be situated amidst various household items. The angle at which the cap is positioned does not offer a full view, providing only a partial glimpse of it. The surrounding environment has a chaotic appearance with multiple objects scattered around, drawing attention away from the cap itself.

#### Sample 368 — Before

- Similarity: 0.4279
- Prediction: The package appears to be partially thawed, indicating that the contents of the package have been removed. The package's contents are not visible, but the contents are still visible. The packaging is slightly open, suggesting that the package has been opened, revealing a portion of the contents. The person's hands seem to be holding the package in their hands, implying that they are preparing to eat.
- Reference: The tomatoes appear freshly opened from a sealed, rectangular plastic can, with the lid being peeled back by a pair of hands. The contents are vibrant red chopped tomatoes, steeped in their own juice, with a noticeable gleam that suggests a high moisture content. Small bits of tomato pulp and seeds are visible, indicating a coarse chop. The can's label, facing downwards, is not fully visible, but the color and texture are unmistakably those of canned chopped tomatoes.

#### Sample 371 — Before

- Similarity: 0.4551
- Prediction: The courgette appears to be freshly chopped, indicating that it's ready to be added to the pan. It's surrounded by bright green leaves, suggesting that they've been slicing for a long period of time. The leaves appear to be ripe, suggesting they're ready to use. They're arranged in a single layer, with a handful of the vegetables scattered around them. They appear to have been chopping, implying that there's been a bit of cooking going on.
- Reference: The spatula is held at a slightly angled position, hovering over a pan that contains diced vegetables, presumably being sautéed. The hand grasping it appears to be mid-stir, suggesting a gentle but firm motion. The utensil itself looks to be made of a dark material, possibly non-stick plastic or silicone, suited to the task of cooking without scratching the pan's surface. Its flat edge and slotted design indicate that it's meant for flipping or turning food items while allowing excess oil or liquid to drain through the openings.

#### Sample 376 — Before

- Similarity: 0.3893
- Prediction: The vegetable appears to be in the hands of a person, with a sharp knife in hand, pointing downwards at the stem. The camera's focus is on the vegetable, which is positioned on a flat surface, revealing a bright green color and a well-grooved stem, suggesting that it has been slicing for a long period of time.
- Reference: The cucumber appears to be relatively dry and untouched by water. The person's hands are not yet interacting with the cucumber directly. The cucumber's skin looks smooth with a shiny green hue, indicative of its freshness. There are no apparent blemishes or imperfections on the visible part of the cucumber, and it rests against the side of the sink, yet to be cleaned.

#### Sample 378 — Before

- Similarity: 0.4998
- Prediction: The chopping board appears to be in a kitchen setting, with a variety of ingredients scattered around it. The surface of the cutting board is brightly lit, suggesting that the cooking process has been completed, and there is a large amount of food on the board. The cooking surface appears to have been huddled around a wooden cutting board, indicating that there has been a significant amount of cooking done. There are a number of vegetables scattered around the board, including carrots, celery, broccoli, and cauliflower.
- Reference: A gas hob displays a single black pan centered on the front right burner, which is alight, suggesting cooking is in progress. The pan contains diced vegetables, primarily zucchini and carrots, being sautéed, as evidenced by the glossy sheen, possibly from oil. Cooking utensils — a spatula and a spoon — rest on the counter, within easy reach. To the left, a plate with remnants of food and a white spatula suggest a meal is being prepared or has recently been consumed. The hob appears to be clean, and the knobs on the hob front are in an undisturbed position, indicating a single burner in use.

#### Sample 379 — Before

- Similarity: 0.3544
- Prediction: The lid of the jar appears to be positioned on a kitchen counter, with its contents scattered around it. The lid is positioned against a wall, with a handful of food in the background, indicating that the lid has been removed from the kitchen counter. The contents of the lid appear to be in the kitchen, with the lid positioned at a 45-degree angle, suggesting that it has been placed on the counter.
- Reference: The tray is situated on the scales, appearing relatively stationary. The tray itself has a clean and shiny surface with an almost reflective quality. It sits flush against the scale's surface, suggesting that it's resting firmly and has not yet been disturbed.

#### Sample 389 — Before

- Similarity: 0.3833
- Prediction: The coffee maker appears to be positioned in a horizontal position, with a single hand in the middle of the frame. The camera's focus is on the coffee maker's interior, which is cluttered with various items, such as mugs, utensils, and other household items. The surrounding area is dimly lit, suggesting a view of a kitchen or kitchen setting.
- Reference: The locker appears to be a wooden cabinet situated in a domestic setting, most likely a kitchen. It's opened slightly, revealing its contents which consist of various household items. There's a white container with a lid positioned centrally, and to its right, we can see multiple food items, including some packets and perhaps some bottles. The interior wall of the locker showcases a wood grain pattern, and the door has vertical paneling.

#### Sample 391 — Before

- Similarity: 0.3587
- Prediction: The glove appears to be in the hands of a child, with its fingers pointing downwards, indicating that it has just been swung into the water. The glove is positioned in the middle of the kitchen sink, where it's likely being washed, and the gloves are positioned near the sink's edge, implying that the gloves have just been used. It's surrounded by yellow, yellow, and blue towels, suggesting that it may be time to wash them. The surrounding area is well-lit, with a steady stream of water enveloping the glove
- Reference: The chopping board appears to be wet with visible droplets of water scattered across its surface. The water seems to have been splashed or poured recently, as the droplets are dispersed unevenly, suggesting movement. The shade of the board appears darker in the watered sections, contrasting with the drier areas that display a lighter hue of blue.

#### Sample 392 — Before

- Similarity: 0.3871
- Prediction: The drawer appears to be partially open, indicating that the contents are in a sealed container. The drawer's interior is cluttered with various items, such as utensils, kitchenware, and other household items. The camera's focus is on the contents of the drawer, which appear to contain a variety of items, including food, beverages, and personal items.
- Reference: A tea towel is partially draped over the edge of an open drawer. The towel exhibits a vibrant stripe pattern with bold colors—yellow, pink, blue, green, and white—creating a lively contrast against the wooden tones of the drawer. It appears to be a linen material, given its texture and slight wrinkles, indicative of recent use or hasty storage. The tea towel is positioned such that it could easily slip off the drawer's edge, suggesting that it wasn't placed with long-term storage in mind.

#### Sample 397 — Before

- Similarity: 0.4063
- Prediction: The hand appears to be in motion, indicating that it's at a slow or slow pace. It's positioned on a kitchen counter, with a few items in the background, such as a utensil or a pot of soup. The camera's focus is on the kitchen area, which is cluttered with items such as food or cooking tools. The hand is positioned in the middle of the kitchen, with the kitchen sink and kitchen counter in focus, suggesting that the hand is near the kitchen counter.
- Reference: The salt appears to be contained within a typical cylindrical container with a white cap, likely designed with a flip-top for easy pouring or shaking. The container rests among an array of other kitchen items, and the immediate surroundings give no clear indication of any recent interaction or disturbance involving the salt. The placement and orientation of the salt container suggest that it has been set down after use or it's awaiting its turn for inclusion in the culinary process.

#### Sample 403 — Before

- Similarity: 0.4243
- Prediction: The cheese appears to be freshly cut, with a thin layer of dough on the surface of the cheese. The dough's surface is slightly uneven, suggesting that the cheese has not yet been fully cooked. The cheese's texture is reminiscent of a freshly-baked pizza crust, indicating that it has not been properly seasoned. The texture of the dough seems to be a mixture of flour and water, which suggests that the dough has not had time to fully cook.
- Reference: The onion appears to be in the initial stages of preparation. It is sliced into semi-circular or crescent-shaped pieces, with the pieces neatly arranged on a plate. The thickness of each slice is relatively consistent, suggesting that the onion has been methodically and carefully prepared. Around the plate, other ingredients, such as olives, are visible, implying that the onion might be an integral part of a broader recipe. The vibrant, off-white to pale yellow coloration of the onion slices indicates freshness.

#### Sample 406 — Before

- Similarity: 0.3646
- Prediction: The trash bin appears to be in a state of collapse, with a slack, indicating that the contents of the bin have been emptied. The bin's interior is cluttered with various items, including dishes, dishes, and utensils, suggesting that the bin is being used for a variety of purposes, such as cleaning or preparing food. The surrounding area is dimly lit, suggesting a dark ambient, implying a lack of natural lighting.
- Reference: The strainer appears to be held at an angle, capturing the viewer's immediate attention. It contains a vivid, possibly viscous, orange-yellow liquid that seems to be either being poured into or is about to be drained from the strainer. The liquid's bright hue contrasts with the white of the strainer, and there are several distinct streams and drops evident, suggesting a dynamic moment of motion or transition.

#### Sample 408 — Before

- Similarity: 0.3055
- Prediction: The dough in this frame has a slightly uneven surface, indicating that it has not yet been spread out. The texture of the dough appears to be smooth, with a thin, uniform consistency, suggesting that the dough has not been evenly spread out, resulting in a smoother surface. The dough's surface is uneven, suggesting it hasn't yet been fully incorporated into the dough, implying that it's not yet ready for use.
- Reference: The bottle appears to be in a closed state, with the cap securely fastened atop. The person's hand is holding the bottle at its base, positioning it over a flat, beige-colored surface, likely a tortilla or wrap. It's noticeable that no content from the bottle has been dispensed on the tortilla yet, and the surroundings include an array of spices and ingredients indicating meal preparation.

#### Sample 410 — Before

- Similarity: 0.4635
- Prediction: The corn appears to be acorn-shaped, with a thin layer of kernels covering the surface of the corn kernels. The kernels appear to be in the middle of a corn kernel, indicating that the corn has been thoroughly minced. The corn is placed in a jar, with the lid open, suggesting that it's ready for use.
- Reference: A partially completed pizza with a base of dough prominently displays a smattering of sweetcorn kernels. These golden nuggets of corn are scattered across the pizza in a casual, seemingly haphazard fashion, dotting the surface with their sunny hues. The sweetcorn appears to have been freshly sprinkled, with some kernels resting atop streaks of tomato sauce, while others find themselves nestled between the creamy white of the dough. There’s a sense of motion, perhaps captured mid-action, as if the sweetcorn has just tumbled from the can and landed in a random array on the pizza.

#### Sample 412 — Before

- Similarity: 0.3801
- Prediction: The peeler appears to be in the hands of a person, with a water droplet dangling from its stem, indicating that it has been thoroughly rinsed. The water droplets appear to be squeezing from the bottom of the peeler's stem, suggesting that the water has been drained from the stem and the peel has been properly rinsed, implying that the peel is still wet. The potato's surface is slightly damp, suggesting it may be a bit wet or damp, and it appears to have been thoroughly washed.
- Reference: The spring onion appears freshly introduced into a kitchen sink area, its roots still intact, suggesting recent procurement, possibly from a garden or market. The onion's white bulbous end displays a healthy sheen, indicative of moisture retention, while the green stalks exhibit a vibrant color, with no visible wilting, indicating freshness. The onion is held at a slight angle, with fingers gripping firmly around the lower green stalks, preparing for a rinse or a cut.

#### Sample 422 — Before

- Similarity: 0.2334
- Prediction: The timer is placed on a flat surface, with a kitchen counter in the background, indicating that the timer has been turned on. There are no other items on the stovetop, including a pot or pan, which are likely to be used for cooking. The stovetop appears to be in a dark room, with no windows or doors, suggesting that it's not occupied.
- Reference: The oven glove appears to be partially on the person's hand, with the fingers not fully inserted into the glove's finger compartments, indicating a hurried or in-process action of putting it on. The glove itself is a light color, possibly white or a light shade of grey, and shows signs of wear such as slight discoloration or stains. The thumb of the glove seems to be properly worn, but the rest of the fingers are yet to be snugly fitted. The overall position of the hand and the glove suggests the individual is either about to engage with something hot or has just completed a task requiring thermal protection.

#### Sample 433 — Before

- Similarity: 0.4549
- Prediction: The hand appears to be in the middle of a busy kitchen, with a handful of food and a few items on the floor. Its surface is blurred, suggesting a lack of movement or movement. The hand's position is blurry, indicating that the hand is in a slow motion motion. The camera's focus is on the object, which appears to have been placed on a table or counter.
- Reference: The cloth appears to be partially scrunched in the person's hand, showing signs of having been twisted or wrung out. Its texture looks damp and heavy, suggesting it has absorbed a significant amount of water or another liquid. The cloth's color is not fully discernible due to the motion blur and lighting, but it seems to have a light tone, possibly white or cream. The person's grip on the cloth is firm, as indicated by the tautness on the visible portion, indicating that the squeezing action has just been performed or is about to be initiated.

#### Sample 437 — Before

- Similarity: 0.4084
- Prediction: The stainless-steel is positioned on a cutting board, with a sharp edge and a sprinkling of food particles, indicating that it has been removed from the cutting board. The surface of the knife appears to have been coiled, suggesting that the knife has been used in a recent action. The knife's surface is cluttered with crumbs and debris, and the knife itself appears to be clinging to the blade, implying that it may have been used for a previous task. The kitchen sink appears to contain a variety of dishes, including
- Reference: The pieces of pepper are strewn about on a wooden chopping board. Their fresh, vibrant yellow hue contrasts starkly with the brown backdrop of the board. They appear to be freshly chopped, with a few seeds evident among the pieces, and the wetness of the freshly cut vegetable glistening in the ambient light.

#### Sample 439 — Before

- Similarity: 0.4505
- Prediction: In this frame, the rag appears to be in the hands of a person who has just started rinsing it. The rag seems to be clinging to the edge of the cloth, indicating that it has been thoroughly washed. The water droplets appear to be coming from the bottom of the fabric, suggesting that the water has been drained from the fabric.
- Reference: The towel appears to be a standard kitchen towel with a predominantly yellow hue, featuring a red pattern, which suggests a possible decorative or functional design. It is being held by a person whose hand and forearm are visible in the image. The towel is partially crumpled and in motion, which blurs the details of its design and exact shape, as the person seems to be in the process of either picking it up or beginning to use it. The background reveals a typical kitchen countertop with various items scattered around, indicating that cleaning or cooking activities may be taking place.

#### Sample 446 — Before

- Similarity: 0.3189
- Prediction: The moka pot appears to be in the hands of a person who has just started using it. The pot is positioned on a stovetop, with a lid and a handle, suggesting that the pot is being used for brewing. The stovetop appears to have a removable lid, which indicates that it has been placed in a kitchen setting. The surrounding area is cluttered with various items, including utensils, mugs, and other household items.
- Reference: The bottle of oil is gripped by a hand, slightly tilted, with its cap being held nearby, ready to be placed back onto the bottle. The cap appears to be in motion, with a tissue wrapped around it, likely for better grip or to clean excess oil. The angle of the bottle suggests the oil has just been poured, and the action of closing it is in process. The surrounding environment is a kitchen, with various cooking ingredients and utensils scattered around, indicating a meal preparation scenario.

#### Sample 450 — Before

- Similarity: 0.4617
- Prediction: The pizza appears to have been sliced and placed on a cutting board, indicating that it has been removed from the oven. The pizza's surface is slightly uneven, suggesting that it may have been left in the oven for a few minutes. The toppings of the pizza appear to be a mixture of cheese, olive oil, and tomato paste, with a slight hint of salt and pepper.
- Reference: Chopped green chili peppers are scattered across the surface of a pizza base. Their vibrant green hue stands out against the reds and yellows of the tomato sauce and corn kernels. Each piece of chili varies in size, suggesting they were hand-cut, with edges that are slightly curled from the knife's pressure, indicating they are fresh. The distribution is somewhat concentrated towards the center, hinting that they were likely dropped from a small height, allowing for a clustered effect rather than an even spread.

#### Sample 456 — Before

- Similarity: 0.4505
- Prediction: The cup appears to be in the hands of a person who has just been rinsing it. It is held under a faucet, with a water droplet dangling from its handle, indicating that it has been washed. The water droplets are visible, suggesting that the cup is being rinsed.
- Reference: The coffee machine is adorned with vibrant blue and gold patterns, presenting an ornate and decorative appearance. Its main body has a curved design, with the base being somewhat cylindrical, leading to an open top. The spout of the machine is not visible, suggesting it's either turned away or the machine doesn't have one. There's a prominently featured label or marking on the front, but the exact details or brand are not discernible.

#### Sample 457 — Before

- Similarity: 0.4922
- Prediction: The bowl appears to be in the hands of a person, with its contents scattered across its surface. The bowl is positioned on a countertop, with a handful of ingredients scattered around it, indicating that it has been used to make a variety of food preparations. It is surrounded by a mixture of flour, baking powder, sugar, and salt, suggesting that it is likely to be used as a preservative or a flavor enhancer.
- Reference: The mixture appears to be in the initial stages of mixing. It exhibits a vivid yellow hue, indicative of the presence of eggs or a similar binding ingredient, interspersed with dark green specks, likely herbs or finely chopped vegetable matter. The texture is somewhat lumpy and uneven, suggesting that the ingredients have just begun to be incorporated. The surface shows the beginning of streaks and swirls, a sign that it has been stirred but not yet fully homogenized, with visible peaks and valleys of mixture indicating a recent entry of the spoon.

#### Sample 459 — Before

- Similarity: 0.3148
- Prediction: The glove appears to be in motion, indicating that it has been placed in a position where it is likely to be used as a hand-washing tool. The gloves are positioned in the middle of a kitchen, suggesting that they are near a sink or counter, possibly a microwave or oven. The glove's surface is cluttered with various items, such as utensils and kitchenware, which indicate that the gloves are in motion. The contrast between the gloves and the surrounding area is blurred, suggesting a busy kitchen environment.
- Reference: The image reveals a standard-sized, cylindrical can positioned near the edge of a countertop, partially opened with a lid attached. The pull-tab of the can has been engaged and is bent at an angle, indicating the lid has been partially peeled back. The metallic interior surface of the can reflects the ambient light, highlighting the exposed content which appears to be a type of food, possibly a canned fruit or vegetable, showing a glimpse of small, rounded items consistent with peas or corn.

#### Sample 460 — Before

- Similarity: 0.4710
- Prediction: The utensil appears to be in the hands of a person, indicating that he or she is preparing a meal or a recipe for a specific type of food. The object's surface is cluttered with a variety of objects, including a pot, a sink, and a dishware container. The camera's focus is on a kitchen sink, which is positioned near a stove, possibly a microwave oven, or an oven. The user's fingernails appear to be positioned on the surface of the sink, suggesting that the user
- Reference: The image captures a motion-blurred scene where the water tap appears to be at a critical transition point. The blurred state of the hand and the tap suggest a dynamic interaction, with the tap likely in the process of being turned off. The water flow is not clearly visible, indicating either a rapid movement that the camera could not freeze or a very thin stream of water that blends into the surrounding blur. Drops of water can be inferred to be present, possibly splashing or just ceasing to fall, reflecting the hurried action taking place.

#### Sample 469 — Before

- Similarity: 0.3797
- Prediction: The garlic clove appears in a dimly lit frame, revealing a portion of the clove's interior. The clove itself appears to be partially detached from the surrounding area, indicating that the clove has been removed from its packaging. The surrounding area is cluttered with various items, including a plastic bag, a kitchen towel, and a handful of kitchen paper.
- Reference: The cover appears to be initially situated atop a cooking appliance, with only a small portion of the object being captured in this frame. From what's discernible, the cover's surface appears glossy, possibly indicating it's made of a material like glass or polished metal. There's also a reflection on its surface, hinting at overhead lighting in the room. The edges of the cover seem to be slightly elevated, suggesting that the person might be starting the process of lifting it or that it's not entirely sealed on the appliance.

#### Sample 470 — Before

- Similarity: 0.3467
- Prediction: The bottle appears to be in the hands of a person who is holding it. The bottle is positioned in a position where it's being handled, with the fingers pointing downwards, indicating that the bottle is still in the position of its upright position.
- Reference: The plug appears to be partially inserted into a power outlet, which is located close to a cluttered area, possibly a kitchen counter, given the presence of various kitchen items and food packages. The outlet itself is standard, likely designed for two-pronged plugs, and the plug is white, contrasting with the cream-colored wall. The person's hands are gloved in yellow, suggesting the maintenance of hygiene or protection from dirt. The plug is captured in the midst of an action, with the person's hands positioned as if they are in the process of gently pulling or manipulating the plug.

#### Sample 476 — Before

- Similarity: 0.3795
- Prediction: In this frame, a person is holding a container of a liquid, which is being poured into a glass container. The container's contents are clearly visible, with a single finger grasping the container, indicating that the liquid has been poured onto it. The fingernail appears to be grasping a small amount of the liquid, implying that the container has been placed in a position where it is likely to be used to make a fresh batch of food. The person's fingers appear to be holding the container in their hands, suggesting that they are engaged in
- Reference: The salt shaker is inverted, with its opening directed towards a mound of shredded cheese on a round flatbread. It's being held by a hand mid-motion, implying that the action of shaking has just begun or is about to begin. The shaker's lid is white, suggesting a contrast with the surrounding ingredients and the warm tones of the kitchen. There's no visible salt coming out yet, indicating this is the initial stage of seasoning. The hand looks to be giving a slight shake, with salt potentially starting to disperse.

#### Sample 480 — Before

- Similarity: 0.3564
- Prediction: The plastic bag appears to be in the hands of a person, with its contents being placed in the palm of the hand. The bag's interior is cluttered with a variety of items, including a toothbrush, toothbrush, and toothpaste. It is positioned on a flat surface, indicating that the bag has been fully inserted into the container. The packaging appears to have a sleeve, which indicates that the contents of the bag have been removed from the container, implying that it is being used for a specific purpose.
- Reference: The liquid washing up is yet to be dispensed from its container, which is being held in a poised position over a sponge. The sponge, appearing dry and ready to absorb, waits to receive the liquid. There is an anticipation in the scene as the liquid remains enclosed in its container, suggesting that the act of dispensing is imminent.

#### Sample 482 — Before

- Similarity: 0.3266
- Prediction: The film has a slightly distorted image of a man holding a tray of shredded plastic. The film appears to be in the hands of the person who is attempting to remove the film from the tray, indicating that it has been removed from its packaging. The man's hand is positioned on the tray's edge, grasping the film with one hand, revealing a portion of the film, which appears to have been ripped open and placed onto a cutting board.
- Reference: The packaging, in this frame, is intact with no apparent tampering or alterations. A package of red meat rests on the countertop, untouched and in its original state. Adjacently, there's a package of chicken or some lighter meat. The package has a label attached to it, displaying some information, potentially related to its weight and price, but the exact details cannot be discerned. The plastic seal around both these meat packages is undisturbed, signaling that the items have not been accessed yet.

#### Sample 485 — Before

- Similarity: 0.3988
- Prediction: The package appears to be in the hands of a person who has just opened it. The contents of the package are clearly visible, as well as the packaging's contents. The package is positioned on a counter-top, with a single hand holding it, indicating that the package has been opened. The person's hands are engaged, suggesting that they are attempting to open the package.
- Reference: The milk carton appears to be in a person's hand, which is in motion, likely towards a surface or a designated storage area. The carton is predominantly green with visible text and imagery, suggesting it is a branded product with some sort of label design. The positioning of the hand and the blurred background suggest a swift movement, with the focus being on placing the milk carton down. The surrounding area is cluttered with various kitchen items, indicating the setting might be a kitchen counter or a similar domestic space.

#### Sample 487 — Before

- Similarity: 0.3257
- Prediction: In this frame, the kitchen sink appears to be in a different state, indicating that it has been removed from the cabinet. The kitchen's interior is still cluttered, with a few items on the counter, including a bowl, a pot, and a dish towel. The camera's focus is now focused on the sink, which appears to have been placed in the kitchen, implying that the sink has been emptied.
- Reference: The stove top appears cluttered and in the midst of a cleaning process. A kettle and a pan with a striped base sit on the stove, indicating recent or pending use. To the right, a microwave door is ajar, while various items, including a tea box and an assortment of spice containers, occupy the counter space. The hand of the person cleaning is in motion, suggesting an ongoing task, and the blurred movement of the sponge in their hand implies vigorous scrubbing. The sponge's yellow hue stands out against the white microwave, suggesting the presence of cleaning agent or accumulated grime.

#### Sample 490 — Before

- Similarity: 0.4480
- Prediction: The package appears to be in the hands of a person, with its contents being placed in a sealed container. The package is positioned on a kitchen counter, with the lid open, indicating that the package has been opened. The contents of the package are clearly visible, as well as the packaging's contents. The packaging appears to contain a variety of ingredients, such as salt, sugar, and spices, which are likely to be used to prepare foods.
- Reference: The tortilla appears freshly lifted from the stack, held by a hand wearing a checkered shirt, indicating the beginning of an action. It exhibits slight flexing at the edges, a common characteristic of a pliable, room-temperature tortilla. The smooth, pale surface of the tortilla contrasts with the more textured and vibrant packaging from which it was taken, and the surrounding kitchen paraphernalia—like the bag of chips and container of sugar in the background—provides a casual, domestic setting.

#### Sample 494 — Before

- Similarity: 0.4832
- Prediction: The kitchen appears to be in the middle of a busy kitchen, with a kitchen sink, a microwave, and a stove. The kitchen's lighting is dim, suggesting that there is no lighting, and the kitchen is not visible from afar. The ambient lighting provides a contrast to the surrounding environment, which suggests that the kitchen may be in a state of transition.
- Reference: In this frame, the door is almost entirely closed. The door's handle, located on the right side, appears to be in its resting position, suggesting that it hasn't been fully engaged yet. Shadows cast from the door onto the adjacent surfaces indicate that ambient light is coming from the left side of the frame. The door seamlessly blends into the cabinetry, making it difficult to discern any clear boundaries at first glance.

#### Sample 495 — Before

- Similarity: 0.2039
- Prediction: The drawer appears to be in the middle of a kitchen or dining area, with a variety of items scattered around it, including utensils, kitchenware, and other household items. The drawer's surface is cluttered with various items, such as dishes, pots, pans, and bowls, indicating that there is a large amount of food on the counter or in the drawer.
- Reference: The electrical plug, white in color with two prongs, is securely inserted into a wall socket. The plug's cord extends towards the bottom right corner of the image, indicating that it is under some tension, possibly from the device it is connected to or from the act of being pulled. The wall socket is situated close to the corner of two walls meeting, and the plug itself is partially obscured by a wooden chair leg, hinting at a domestic setting. The flooring is tiled in a warm yellow hue, and the skirting is white, matching the plug and socket.

#### Sample 497 — Before

- Similarity: 0.3109
- Prediction: The kitchen sink appears to be in a state of disrepair, indicating that the sink has been recently cleaned. The sink's surface appears to have been wiped with a damp cloth, suggesting that it is still wet, possibly from a recent cleaning process. The area around the sink is cluttered with stains, which indicate that there is a significant amount of grime on the surface of the sink, implying that there may be a clog or a spill.
- Reference: The glove in this frame appears to be bright yellow in color and covers the entirety of the person's hand, extending past the wrist. Its surface texture is smooth, suggesting it might be made of rubber or a similar waterproof material. The individual wearing the glove is holding a kitchen utensil, which suggests that the glove is designed for tasks that require dexterity, like cooking or cleaning. The environment around the glove indicates a kitchen setting with various utensils and dishes present.

#### Sample 5 — During

- Similarity: 0.3476
- Prediction: In this frame, there is a noticeable increase in the number of items on the counter, indicating a shift in the direction of the cleaning process. The countertop remains in the same position, but there are a few more items, such as a dish towel or a utensil, in the center of the frame. The kitchen sink appears to be in a state of transition, possibly due to a recent cleaning.
- Reference: The floor appears to remain consistently colored with the same mustard-yellow tiles, but the angle of the shot reveals more of the tile area. Additional small debris and smudges are present, and a damp streak is now visible, likely from the wiping motion. The streak has a darker shade than the rest of the floor, indicating that the floor may have been somewhat dirty before being wiped, and the wetness is bringing out the contrast in the tile's coloration.

#### Sample 7 — During

- Similarity: 0.4925
- Prediction: In this frame, the contents of the cupboard are more visible, indicating that the person is now engaged in some sort of action, such as removing the lid or opening the door.
- Reference: The jar is now in motion, caught mid-air with its label oriented towards the camera. Its trajectory appears to be downwards, indicating it has been dropped. The lid remains firmly affixed, and no contents are visible escaping from the jar. The blurred background due to the motion suggests a rapid descent. The person’s foot and the striped sock are prominent in the frame, possibly the inadvertent catalysts for the jar’s sudden journey towards the floor.

#### Sample 8 — During

- Similarity: 0.3894
- Prediction: In this frame, the button has been pressed into place, indicating that it is ready to be turned on. The button remains in the same position as before, suggesting that the button is still operational. The surrounding area of the button remains unchanged, with no visible signs of pressing the button, implying that the switch has been activated.
- Reference: The same toaster now displays subtle differences. The lever has been slightly pushed downwards, but not entirely, hinting at the beginning of the toasting process. The slots still appear vacant, and there isn't any visible toasted bread. However, there's a soft glow starting to emanate from the slots, suggesting that the heating elements are beginning to activate. The power indicator light has a dim glow, further affirming the initial stages of the toasting process.

#### Sample 20 — During

- Similarity: 0.4974
- Prediction: In this frame, the package is now in a new position, with the person's hands firmly engaged in the action. The packaging remains in the same position as before, but the hands are now able to grasp the contents of the package, indicating that they have been removed from the packaging.
- Reference: In this frame, the action has progressed, with the hand now holding a yogurt container mid-air, suggesting movement. The container appears to have been recently moved, as indicated by its orientation and the slight blur conveying motion. The backdrop remains consistent with the kitchen setting, and the previously mentioned items remain static, reinforcing that the yogurt's movement is the focal point of the activity. The hand's grip is firm, suggesting purpose in the movement of the yogurt container.

#### Sample 31 — During

- Similarity: 0.3420
- Prediction: In this frame, there is a noticeable increase in the amount of food left on the table. The surface of the table now has a slightly different appearance, indicating that it has been thoroughly cleaned. The cleaning solution remains the same as before, and there are still a few drops of the cleaning solution on the surface.
- Reference: In this instance, the glass maintains its upside-down orientation, but there is a noticeable shift in its position on the tabletop. The person's hand is in motion, with fingers and thumb appropriately placed to apply force to the glass's base. The movement suggests a slide across the wooden surface, as evidenced by the change in the light reflection pattern on the glass's base, which now has a slightly blurred appearance due to the motion.

#### Sample 32 — During

- Similarity: 0.3988
- Prediction: In this frame, the tomato has been moved closer to the camera, indicating that it has been placed in the hands of the person who is holding it. The tomato remains in the same state as before, but it's now positioned in a slightly different position, implying that the person is holding the tomato. The proximity of the tomato to the person's hand indicates that the tomato is being handled, possibly by a friend or family member.
- Reference: The lettuce is in the process of being unveiled; the plastic wrap has been partially removed, revealing the top of the lettuce head. The leaves at the crown appear slightly more relaxed than before, likely due to the removal of the constraining wrap. The green hue of the leaves is consistent, displaying no signs of wilting or discoloration, which emphasizes the freshness of the produce. The person handling the lettuce has initiated the unwrapping from the top, peeling the plastic down and away from the lettuce, indicating a preparation to use the lettuce imminently.

#### Sample 33 — During

- Similarity: 0.3314
- Prediction: In this frame, the knife has been moved to a new position, indicating that it is no longer in its original position. The hand's grip remains stationary, and the knife's handle is now positioned slightly away from the viewer's eye. The image of the knife appears to have been taken from a previous frame, suggesting that the knife may have been placed in a different position.
- Reference: The cabinet door is now open wider than in the previous frame, revealing more of its contents. The lower shelf still displays the orderly arrangement of cans, and now, the upper shelf's contents become partially visible, featuring what appears to be a row of upright standing bottles or jars. The arrangement suggests a systematic approach to organizing the items by size or type. The cabinet's interior is bathed in the ambient light of the room, which casts soft shadows and gives a homely atmosphere to the kitchen storage space.

#### Sample 36 — During

- Similarity: 0.4390
- Prediction: In this frame, the cheese has been removed from its packaging. The cheese remains in the same state as before, but is now positioned in a slightly different position. The butter's surface remains unchanged, and the bread's texture remains unchanged. The sandwich's shape remains unchanged in the previous frame, with the bread still retaining its original shape.
- Reference: The scene is largely unchanged with the same blue-lidded butter tub in view. However, there's a subtle shift in the positioning of the hands and the butter knife. The right hand still grips the knife, now slightly repositioned, suggesting movement. The butter tub remains closed, and there is no additional evidence of the contents being disturbed. The anticipation of the spread's use is still present, reflected in the slight adjustment of the hands, preparing for the opening of the tub.

#### Sample 41 — During

- Similarity: 0.2711
- Prediction: In this frame, the tray appears to have been removed from its original position, indicating that it has been placed in a different position. The tray's surface is still visible, but it's still slightly tilted away from the viewer's perspective, implying that the tray has been removed.
- Reference: Here, the milk bottle appears more prominently in the foreground, its label more visible, confirming its identity as a household dairy product. The red cap now seems more defined and appears to be partially twisted open, indicating recent or imminent use. The angle of the bottle suggests that it has been nudged or moved, possibly by the person whose hands are in view. The surrounding area remains cluttered, with kitchen utensils and containers in close proximity to the bottle, further emphasizing the dynamic nature of this domestic scene.

#### Sample 45 — During

- Similarity: 0.4635
- Prediction: In this frame, the liquid has been poured into the glass. The surface of the glass appears to have been dampened, indicating that the liquid is now being stirred. The liquid's surface is still visible, with a slight movement in the direction of the pouring motion. The volume of the liquid appears to be more or less constant, suggesting that there may be a sprinkling of liquid particles.
- Reference: In this scene, the jam is in the process of being transferred from the jar to the mixing bowl. It is stretched between its container and the fork, creating a slender, slightly curved bridge of jam. The elasticity of this bridge shows the jam's sticky and pliable nature, and the sheen on its surface reflects the light, further accentuating its smooth texture. This intermediate state between the jar and the bowl shows the jam's ability to retain its shape even when being moved.

#### Sample 56 — During

- Similarity: 0.4516
- Prediction: In this frame, the jar appears to be in the hands of a person, indicating that he or she is engaged in the process of removing it from the kitchen counter. The jar is now in a state of transition, with the lid still firmly in place. The surrounding area is blurry, implying that the person has just stepped into the kitchen and is preparing to eat.
- Reference: In this frame, the packaging is further crumpled, with more pronounced deformations. The hand actively pinches the packaging near its center, causing creases and folds to form. The metallic material shows increased signs of manipulation, with the reflective surface now marred by irregularities from the pressure being applied. The crumpling action is more evident here, as the hand's grip tightens to compact the material further.

#### Sample 57 — During

- Similarity: 0.3701
- Prediction: In this frame, the foil has been placed in the hands of the person who is holding the bag. The person's fingers are firmly grasped, indicating that the foil is still in its original state. The foil remains in the same state as before, but the grip of the hand is now more firm.
- Reference: In this view, the filter is captured mid-removal, slightly lifted from the coffee maker's well. The moist coffee grounds cling together, exhibiting the filter's effectiveness in maintaining the grounds' mass without spillage. The filter shows a slight deformation, likely from the weight of the wet grounds, and the hand's grip has tightened, causing the filter edges to crinkle. The positioning of the hand suggests the intention to dispose of the contents, as it is held away from the body to prevent spillage on clothing.

#### Sample 63 — During

- Similarity: 0.4662
- Prediction: In this frame, the jar has been removed from the kitchen, indicating that it has been moved to a new location. The jar remains in the same position as before, and the rim of the bowl appears to have been removed, suggesting that the bowl has been placed in a different location.
- Reference: The contents of the bowl show signs of being mixed, as the egg's yolk now presents a disrupted surface, with strands of the albumen beginning to blend into the yolk. The pepper specks are more widely distributed, some sinking into the depths of the egg mixture, while others cling to the emerging strands of egg white. The fork's position has changed, implying it has been used to stir the ingredients together, but the mixture remains only partially combined with clear distinctions between the yolk and the whites still visible.

#### Sample 73 — During

- Similarity: 0.4184
- Prediction: In this frame, the cleaner's residue is still present, indicating that it's time to clean the grid again. The grid's surface is now cleaner and cleaner than before, suggesting that there's still a lot of residue left on the surface. The cleaning solution is still wet, but the residue appears to have been removed.
- Reference: In this instance, the grid is more level, held steadily in place by the right hand gripping the top edge. The left hand comes into play, with fingers positioned on the lower left corner, possibly exerting a slight force to maintain the grid's balance or to manipulate it further. The sink appears wet, and the grid itself shows evidence of water exposure, as indicated by the water droplets clinging to the metal bars and reflecting the ambient light.

#### Sample 79 — During

- Similarity: 0.4235
- Prediction: In this frame, the scourer's cup is in a slightly different position, indicating that it has been moved from its original position. The cup's position remains the same, and it's now viewed from a different angle, implying that the cup has been placed in the hands of someone else.
- Reference: Here, the colander is being held over a drying rack adjacent to the sink. It is tilted slightly, allowing any residual water or particles to escape. The reflective light on its surface indicates that it's possibly wet or has recently been rinsed. Its metallic structure shines through, showing its sturdy build. The positioning of the hand holding it suggests an intent to either place it down or shake it.

#### Sample 82 — During

- Similarity: 0.3679
- Prediction: In this frame, the tap's water flow has been reduced to a minimum, indicating that the tap has been fully withdrawn from the water source. The faucet's handle is now slightly tilted, suggesting that the water has been sucked out of the sink. The water flow appears to be slowed down, with a slight increase in the flow of water.
- Reference: Here, the cloth is grasped between both hands, with the fingers of one hand seemingly applying pressure or motion to the fabric. The cloth seems to be undergoing a more thorough rinsing or wringing action, as evidenced by the positioning of the hands and the appearance of the water flowing off of it. It's more spread out than before, allowing the water to flush out any soap or debris. The cloth's texture is more discernible, implying that it has been opened up compared to the previous state.

#### Sample 86 — During

- Similarity: 0.3171
- Prediction: In this frame, the contents of the plastic bag are now visible, indicating that the bag has been opened. The bag is now in a new state, with the handles still in place, suggesting that the contents have been removed from the bag. The person's hands seem to be holding the bag in their hands, implying that they are trying to open it.
- Reference: In this snapshot, the leek is in the midst of a dynamic, albeit unintended, journey as it descends towards the floor. The white end, previously pointing downwards, now inclines towards the camera, hinting at a flipping motion. The plastic wrap has loosened in places, a testament to the forces at play, and the leek's green tops appear more splayed, no longer neatly aligned due to the movement. The blurring of its edges suggests a swift motion, further highlighting the unexpected descent.

#### Sample 89 — During

- Similarity: 0.4903
- Prediction: In this frame, the holder of the sink has been moved to a new position, indicating that the sink is now in a different position. The sink's position remains the same, and it is now positioned in the same position as the sink. The kitchen sink appears to have been moved from the previous position, suggesting that it is no longer in the position it was in.
- Reference: The container appears to be at a slightly different angle, giving an impression of being either moved or possibly tilted. It continues to reveal its label, with the blue and green graphics more prominent in this frame. The white cap remains off, placed close to the base of the container. Nearby objects and the counter’s surface indicate that the location remains consistent with the previous frame.

#### Sample 96 — During

- Similarity: 0.4960
- Prediction: In this frame, the person's hands are engaged in the process of removing the package from its packaging. The package's contents are still present, but the hands are now able to grasp the contents of the package with their fingers, ensuring that the contents remain intact.
- Reference: In this moment, the person has partially peeled back the top layer of the plastic seal, starting the process of opening. The opening is at the initial stage, with just the corner of the packaging being lifted. The seal's detachment is most noticeable at the top left corner where the individual's fingers are pulling the material away, revealing a glimpse of the salmon's surface beneath. The packaging still retains its original shape, but the airtight seal has been compromised.

#### Sample 97 — During

- Similarity: 0.4126
- Prediction: In this frame, the plastic bag is now firmly grasped by the hand, indicating that the bag has been inserted into the bag. The hand's grip is more firm, suggesting that the seal has been closed. The bag's contents remain the same, but the hands are now engaged in the process of removing it.
- Reference: In this moment, the cereal is in the process of being poured. A stream of small, flaky, tan-colored cereal pieces cascades from the bag into a bowl held below with the same hand that was holding the bag open in the previous frame. The flow of the cereal is steady, indicating that the bag has been tilted sufficiently to allow the contents to exit freely. The flakes catch the light as they fall, suggesting a light, crispy texture, and they accumulate in the bowl, already containing a modest amount of cereal.

#### Sample 100 — During

- Similarity: 0.2351
- Prediction: In this frame, the tea kettle appears to be in motion, indicating that the hand is engaged. The hand's position remains unchanged, suggesting that the kettle is still in motion. The camera's focus is on the kettle's exterior, which suggests that it's positioned in a horizontal position, implying that the person is engaged in some sort of action. The contrast between the kettle and the surrounding environment is blurred, suggesting a shift in the direction of the action.
- Reference: In this image, the environment has transitioned into a state of semi-darkness, with the light source significantly reduced. The glow that previously brightened the entire room is now subdued, with shadows beginning to dominate the space. The reflective surfaces that once gleamed under the light now present muted reflections, and the overall visibility in the room has decreased. It appears as though the light source is in the process of being extinguished, capturing the room in an intermediate stage between light and dark.

#### Sample 110 — During

- Similarity: 0.3853
- Prediction: In this frame, the cabinet's position is slightly different from the previous frame, indicating that the door has been moved. The cabinet'd location remains the same, and the area around the door appears to be a little more open, suggesting that there may be some movement in the area. The overall state of the cabinet is still consistent with its previous state, but there is a slight change in the position of the door. The absence of a noticeable difference in the space between the two frames suggests that the cabinet may have been moved a step further.
- Reference: The chair is now seen at a different angle and slightly further away from its original position under the table. The cushion is still visible, and the chair's wooden frame has come into clearer view, indicating that it has been pulled back or to the side. The tablecloth and table surface are no longer in the immediate vicinity of the chair, emphasizing its movement. The lighting conditions remain consistent with the first frame, and the shadow cast by the chair has shifted accordingly.

#### Sample 112 — During

- Similarity: 0.3746
- Prediction: In this frame, the holder of the teapot appears to be in motion, indicating that it has been removed from its position. The surrounding area is blurred, suggesting that the tea pot has been placed in a position where it is likely to be used as a condiment or a decorative item. The teapot's exterior is more reflective, implying that it is being handled with utmost care.
- Reference: Here, the coffee bag is now the central element, with hands actively engaging with it. The fingers are pinching the top corners, preparing to seal the bag. The bag appears to be made of a flexible, possibly foil material that has a reflective sheen, indicating its lightweight and pliable nature. The backdrop consists of a kitchen counter cluttered with various items, including a coffee mug and kettle, setting the scene for a routine coffee-making process.

#### Sample 116 — During

- Similarity: 0.4539
- Prediction: In this scene, the carrots have been removed from the cutting board, indicating that they have been placed on a cutting board. The carrots are now in the hands of a chef, demonstrating that they are ready to be cooked. The vegetables are still in the kitchen, and the pot appears to be chopping, implying that they will be ready for the next batch of cooking.
- Reference: The focal point in this scene continues to be the white bowl with diced sweet potatoes. They seem to be soaking in a liquid, possibly water or a marinade. This liquid gives the sweet potatoes a slightly glossy appearance. Surrounding the bowl are other ingredients, including a clear container holding what looks like a slice of lemon, two cans that seem to contain some sort of sauce or preparation, and a packaged item with indistinct labeling. The area appears slightly tidier compared to the previous frame.

#### Sample 123 — During

- Similarity: 0.4957
- Prediction: In this frame, there is a slight movement in the direction of the sink, suggesting that the sink is in a downward motion. The sink's surface appears to be slightly tilted, indicating that the water has been dripping into the sink basin. The water's flow seems to be slowed down, and the sink appears to have been agitated.
- Reference: Here, the hand appears to be in the midst of a hand-washing routine, with a wet and possibly soapy texture visible on the skin. The fingers are spread apart, and the hand is again captured in a motion blur, suggesting a scrubbing action. The hand is slightly more elevated from the sink compared to the previous frame, and water can be seen cascading off the fingers, reflecting the indoor lighting with a glossy sheen that highlights the contours of the hand and the fluid dynamics of the water.

#### Sample 124 — During

- Similarity: 0.4676
- Prediction: In this frame, there is a noticeable increase in the amount of ingredients on the pasta, indicating that the ingredients have been added to the bowl. The ingredients are now more evenly distributed, with the remaining ingredients still present. The bowl appears to have been removed from the pan, suggesting that the pasta has been thoroughly stirred.
- Reference: In this instance, the spoon's orientation has shifted; it now rests within the confines of the plate, cradling a small portion of the meal's remnants. The bowl of the spoon is partially obscured by food particles, indicating it has been actively used. The utensil's handle reflects a secure hold within the individual's grasp, and the angle of the spoon suggests a motion of scooping or scraping the plate. The wooden texture remains visible, though slightly less pronounced due to the overlay of food.

#### Sample 129 — During

- Similarity: 0.4678
- Prediction: In this frame, the contents of the container are now more visible, indicating that the person has moved to the next step in the process. The camera's focus now shifts to the side of the fridge, which is still a bit blurred, possibly due to the movement of the hand. The items on the counter are still in the same position, but the contents are still visible, suggesting that they may have been placed in a different location.
- Reference: The drawer is now further ajar, allowing a clearer view of its contents. The variety of greens becomes more evident, with at least two different types distinguishable by their leaves. One bag has a distinctive red and blue label, perhaps indicating brand information or product type. The milk container on the right is more visible, alongside a blue-lidded container, which may hold leftover food or additional ingredients. The individual's hands are more visible in this frame, with one hand steadying the drawer and the other beginning to reach towards the contents.

#### Sample 142 — During

- Similarity: 0.4801
- Prediction: In this frame, the surface of the plate is now blurred, indicating that the plate has been removed from the kitchen. The camera's focus is now on the plate, which is now in a state of transition, possibly due to the presence of a new layer of paper.
- Reference: The frame offers a clearer view of the kitchen setting, but the sausage remains elusive. While the person's hands dominate the frame, drawing attention to the plate they're holding, the sausage is not directly visible. It's plausible that the sausage is now beneath the plate, given the positioning and movement of the hands, indicating an action related to covering or unveiling.

#### Sample 147 — During

- Similarity: 0.4863
- Prediction: In this frame, the hand is engaged in the action of removing the lid from the cooker, indicating that the cooker has been turned on. The kitchen remains unchanged, with the kitchen still cluttered with items such as pots and pans, utensils, and other household items. The surrounding area is still uncluttered, with a focus on the kitchen's main features, such as the stove and oven.
- Reference: In this frame, the mixer remains in a similar position as before but seems to be slightly tilted or in the process of being adjusted. The same hand is still in contact with the blender's base, firmly gripping it. The scene shows a more dynamic interaction between the user and the appliance, as if preparing or making a subtle adjustment for its next operation.

#### Sample 150 — During

- Similarity: 0.4059
- Prediction: In this frame, the hand is engaged in the action of removing the soap bottle from its original position, indicating that it has been removed from its proper position. The hand's position is now blurred, suggesting that the soap has been placed in a more upright position.
- Reference: The spice is now more visible, suggesting that some items have been moved or repositioned. The surroundings still include various kitchen items, but the focus is increasingly on the spice. The proximity of a hand to the spice indicates imminent interaction or the possibility that the spice will be picked up or moved shortly. The spice has not yet been completely taken out, but it's clear that it's in the process of being accessed.

#### Sample 153 — During

- Similarity: 0.3472
- Prediction: In this frame, there is a person sweeping the counter, indicating that he's done with the cleaning process. The person's hand appears to be holding a paper towel, possibly a cloth or a rag, and the surface of the counter is still damp, suggesting that the person is cleaning the counter. The countertop is now a darker color, with a lighter hue to it, suggesting a deeper cleaning.
- Reference: In this instance, the pepper mill is grasped firmly in the hand, suggesting that the previous state of falling has been arrested. The hand's grip is tight around the pepper mill's middle section, which is often designed to be ergonomically suitable for such a hold. The other hand remains in contact with the cloth, possibly stabilizing the situation or preparing to resume cleaning. The orientation of the pepper mill is now more vertical, indicating control has been re-established over its movement.

#### Sample 158 — During

- Similarity: 0.4462
- Prediction: In this frame, there is a slight change in the position of the banana, which is still in its original position. The banana's position remains the same, and the surrounding area is no longer visible, indicating that the banana has been moved away from the perspective of the camera. The surrounding area remains unchanged, with the banana still positioned in the same position as it was in the previous frame.
- Reference: Now, the orange has begun to move, evident from a slight blurring on one side, indicating the direction of the push. The previously highlighted scars and details are somewhat distorted due to the motion. The area of the table now occupied by the orange is darker, suggesting that the light source is constant, and the orange's position has indeed changed.

#### Sample 161 — During

- Similarity: 0.1751
- Prediction: In this frame, the strainer is now in motion, indicating that it has been removed from the container. The strainer's contents are still visible, but there is still a slight movement in the direction of the sink, suggesting that the liquid has been drained. The sink's surface appears to be a bit damper, with a few drops of water spilled onto the bottom of the container, implying that it may have been clogged or soiled.
- Reference: This frame is nearly identical to the first, maintaining the focus on the bin's interior. The hands in yellow gloves continue to reach inside the drum, which remains dark and devoid of any visible contents. The lighting conditions are unchanged, with the pink and white glow casting a soft hue on the drum's edge and the surrounding environment. The angle and position of the hands seem consistent, implying a continued action or perhaps a momentary pause in movement.

#### Sample 162 — During

- Similarity: 0.4635
- Prediction: In this frame, the utensil has been moved away from its original position, indicating that it is now in a new position. The kitchen sink remains in the same position as before, and the sink's handle is still visible, suggesting that it may have been moved.
- Reference: The focus of this scene shifts to a transparent blue plastic measuring jug with white markings, which indicate measurements. The jug, which is now the central object being handled, is being retrieved from the same dish rack, revealing its storage alongside everyday kitchen items. It's positioned next to stacked white plates and near a colorful silicone lid, emphasizing the jug's functional role in cooking or baking. The jug’s clear plastic material contrasts with the other opaque items, highlighting its purpose for measuring liquids with precision.

#### Sample 170 — During

- Similarity: 0.4542
- Prediction: In this frame, the hand is engaged in the action of slicing the garlic. The garlic is still present, but there is still a slight movement in the direction of the hand, indicating that the garlic has been incorporated into the garlic's composition. The hand's movements are more deliberate, implying that they are preparing the garlic to be used as a condiment, rather than just a garnish.
- Reference: The hand appears to have completed the action of seasoning, as evidenced by the change in the positioning of the spice shaker, now held with a more relaxed grip. The distribution of the spices on the tomatoes is more apparent, with individual grains of the darker spice visible against the vibrant red of the sliced tomatoes. The tomatoes exhibit a glistening surface, likely due to the freshly applied seasoning interacting with the tomato juices, enhancing the visual appeal and suggesting a readiness for the next step in preparation or consumption.

#### Sample 185 — During

- Similarity: 0.3695
- Prediction: In this frame, the microwave remains in the same position as before, but the hands are now engaged in the action. The person's hand is still positioned on the side of the counter, indicating that the microwave has been turned on. The camera's focus remains on the microwave, which is still in motion, and the surrounding area is still blurred, suggesting that there may be a physical connection between the microwave and the oven.
- Reference: In this scene, the temperature display reads a much higher value of 556, an unusual and likely erroneous display since conventional ovens typically don’t reach such extreme temperatures. This could indicate that the user is in the process of setting or adjusting the temperature and has possibly overshot the desired temperature setting. The user’s action of turning a knob, usually associated with increasing or decreasing the oven's temperature, supports this. The digits are bright and unambiguous against the dark background of the oven’s control panel.

#### Sample 189 — During

- Similarity: 0.4358
- Prediction: In this frame, the pizza has been removed from the cutting board, revealing a more detailed slice of the pizza. The knife's edge is still visible, indicating that the slice has been cut and the knife has been inserted into the pizza's crust. The slice of pizza remains in the same state as before, with the knife still pointing downwards. The slices of pizza are now viewed from a different angle, demonstrating that the knife was inserted in the middle of the slice.
- Reference: The cake, still maintaining its crumbly texture on the surface, has now been further reduced in size. An additional portion has been sliced away, and this new slice showcases the cake's uniform interior, which is noticeably darker than its topping. The golden topping creates a stark contrast against the darker, moist center. Now, more than half of the cake remains on the plate, with its exposed interior providing a glimpse into its delectable consistency.

#### Sample 192 — During

- Similarity: 0.4488
- Prediction: In this frame, the microwave remains in the same state as the previous frame, but the microwave's position remains unchanged, indicating that the microwave has been placed in a different state. The microwave remains unoccupied, and there is no indication of the person's presence, implying that they are engaged in any activity.
- Reference: The scene shifts to showcase a stovetop with a frying pan, within which a single pancake cooks; this suggests a breakfast setting. The microwave is out of direct view in this instance, but its proximity to the cooking area implies it plays a part in the meal preparation. In the foreground, hands are engaged in the process of tearing a piece of kitchen towel, likely for use in the cooking or serving process. The countertop is adorned with various breakfast ingredients and utensils, such as a jar of spread, a cut lime, and a glass of a golden-hued liquid, further reinforcing the meal prep context.

#### Sample 194 — During

- Similarity: 0.3920
- Prediction: In this frame, the liquid has a more pronounced presence, indicating that it has been stirred into the water. The liquid is now in the same state as before, forming a syringe-like structure with a smooth surface. The surface of the liquid is still a bit wet, but there is a slight movement in the direction of the water's movement. The movement of the stirring action causes the liquid to become more and more agitated, resulting in a gradual increase in the liquid's volume.
- Reference: The saucepan now sits more squarely in the sink, and it is filled with soapy water, creating a bubbly mixture that obscures the bottom and sides. The water is less turbulent, suggesting that the initial vigorous rinsing has ceased. There appears to be a slight reduction in the food residue as the cleaning agent has had some time to work on the leftover contents. The individual's hand is on the handle, stabilizing the pan as the cleaning continues.

#### Sample 197 — During

- Similarity: 0.4671
- Prediction: In this frame, the paper has been placed in a new position, indicating that it has been moved from its original position. The paper's position remains the same, and the position of the hand indicates that the paper is now positioned in the same position as it was before.
- Reference: The scene shows continuity in the action of wiping the counter. The paper towel is now more crumpled, signifying its use in cleaning up the spill. The kitchen items remain in place: the pot continues to simmer on the stove, and the kitchen tools are untouched from their previous positions. The person's arm is extended further across the counter, reaching to clean more of the surface. The dynamic of cleaning is apparent through the positioning of the paper towel and the person's arm across the counter space.

#### Sample 210 — During

- Similarity: 0.3260
- Prediction: In this frame, the board has been re-sealed, revealing a more streamlined appearance. The board's surface is now more cluttered, indicating that it has been thoroughly cleaned, and there are still a few drops of water on the board, suggesting a deeper cleaning. The kitchen sink appears to be in a state of disarray, suggesting that the board may have been soiled or washed. The blue-green color of the board is reminiscent of a scrubbing motion, implying that a thorough cleaning is taking place. The
- Reference: In this perspective, the soap appears more foamy and sudsy, with a thicker layer of soap suds on its surface. The surrounding area is more cluttered, and the soap is now at an angle, which implies a vigorous scrubbing motion has been applied. The increased number of soap bubbles suggests that the soap has been more actively used, possibly with more water added to generate lather. The grip on the soap has shifted, indicating a different angle or approach to washing has been taken.

#### Sample 211 — During

- Similarity: 0.4816
- Prediction: In this frame, the cloth seems to be wringing out of the water, indicating that the water has been drained. The cloth's surface is still wet, suggesting that it has been thoroughly rinsing. The person's hands are more visible, implying that the cloth is being wrung out.
- Reference: The sink now displays evidence of cleaning activity. There are streaks of moisture across the basin, particularly around the drain, indicative of a wiping action. To the right of the sink, cleaning implements including a sponge and a metallic scrubber can be seen, along with a spray bottle, likely containing a cleaning agent. A black-handled frying pan and other kitchen utensils are drying in a white dish rack. The individual's hands are still present, with the right hand grasping a carrot peel, possibly preparing to discard it, while the left hand rests on the counter, not actively engaged in the cleaning process.

#### Sample 218 — During

- Similarity: 0.4812
- Prediction: In this frame, the pitta has been partially removed from the hummus, indicating that it has been thoroughly soaked. The pittat's surface is now slightly exposed, suggesting that the pit has been dipped in a thin layer of pita. The humus is now embedded in the pit, revealing a sprinkling of the pita's contents, implying that it may have been discarded.
- Reference: The same piece of pitta bread now exhibits a noticeable change; it is torn with a portion of it missing, indicating that a piece has been broken off. The hand, still with the smartwatch visible, is in the process of pulling away a fragment of the bread, with fingers pinched together holding the small torn piece. The texture of the bread's interior is visible, revealing a soft, fluffy crumb that contrasts with the darker, crispier edges. This action is fluid and seems to be done with ease, suggesting the bread's delicate texture.

#### Sample 220 — During

- Similarity: 0.4091
- Prediction: In this frame, the scissors are still held in the hands of the person who is rinsing the dish, indicating that the water has been drained from the sink. The hand's grip is still firm, suggesting that the blades have been thoroughly rinsed. The water droplets appear to be clinging to the paper's surface, implying that the paper has been washed away.
- Reference: Here, the cucumber is positioned under a running tap, with a stream of water cascading over its curved surface, which suggests the washing process is ongoing. The hand gripping the cucumber adjusts its hold, now supporting it from underneath to allow the water to run along its entire length. The pressure of the water causes slight ripples along the skin of the cucumber, and droplets bounce off, creating a dynamic scene where the focus is on ensuring the vegetable is thoroughly cleansed.

#### Sample 225 — During

- Similarity: 0.3921
- Prediction: In this moment, the hand blender remains in the same position as before, indicating that the blender is still on its way to the desired setting. The blender's handle is still visible, suggesting that the user is still using it. The surrounding area of the blender remains unchanged, with a mixture of white and blue hues contrasting against a blue background. The user's hand appears to be holding the blender in a more upright position, implying that they are preparing a new batch.
- Reference: There is a notable reduction in the streaking of the mixture, indicating a progression toward uniformity. The color is now more consistent throughout, without the distinct white areas seen previously, implying a better combination of ingredients. The texture is creamier, and the previous soft peaks have started to settle into a more cohesive batter. The beaters are well-coated, and the mixture exhibits a sheen, suggesting the development of a silky structure, characteristic of a well-emulsified blend.

#### Sample 226 — During

- Similarity: 0.2716
- Prediction: In this frame, the packaging has been placed in the hands of the person who is holding the package. The packaging is still in its original packaging state, but the hand is now engaged in the action of removing it from the packaging.
- Reference: Here, the scissors have made contact with the wrap, capturing the moment where the blades begin to slice through the material. The wrap's tension appears uneven, with a slight ruffling near the point of contact with the scissors. The person's grip on the wrap and scissors is steady and firm, providing control over the cutting action. The surrounding kitchen items remain unchanged, maintaining the focus on the task at hand. The wrap itself has a slight wrinkle near the cutting area, a common trait when handling such materials.

#### Sample 237 — During

- Similarity: 0.4713
- Prediction: In this frame, the salmon remains in a slightly different state, exhibiting a more pronounced bite of the fish. The fish's surface is still slightly exposed, suggesting that the fish has been handled more carefully. The salmon's skin appears to be a little more exposed, indicating that it's still not fully cooked. The chef's hands are now engaged in the process of removing the salmon from the pan, implying that they've been preparing the salmon for a long time.
- Reference: The fish now appears partially submerged in the water, with only its dorsal fin and upper part of the body visible. Water droplets can be seen cascading off its scales, hinting at the recent force exerted on it. Its glistening eyes hint at a sense of urgency, while its body appears slightly curved due to the downward motion.

#### Sample 238 — During

- Similarity: 0.4157
- Prediction: In this frame, the sugar container has been removed from the kitchen counter, revealing a hand-held display of the contents of the sugar cane. The hand's grip on the container is still present, indicating that the sugar has been poured into the container. The spoon's position is still visible, suggesting that the contents are being poured from the container, implying the presence of a large amount of sugar to be added.
- Reference: The jar of flour is now inverted completely, positioned directly above the bowl to maximize the flow of flour. The powdery substance seems to be pouring out more quickly, as evidenced by a thicker stream forming a more substantial pile on top of the previously deposited flour. The white mound in the bowl has grown noticeably, and a cloud of flour dust is more pronounced around the rim of the jar, signifying a brisk pouring action.

#### Sample 241 — During

- Similarity: 0.4107
- Prediction: In this frame, there is a noticeable increase in the number of slices of bread, indicating that the bread has been removed from the plate. The bread remains in the same state as before, suggesting that the slice has been placed in a different place. The spinach remains in its original state, but it appears to have been discarded.
- Reference: The ladle appears to have been lifted from the bowl and is now hovering above the plate, with its bowl-end pointing downwards, poised to be placed down. The liquid in the glass remains at the same level, and the surrounding items on the table, such as the remote control, the blue bowl with green beans, and the yellow-lidded container, remain unmoved. The table's surface is visible, showing more of the texture and the edge of the white paper plate in the foreground.

#### Sample 252 — During

- Similarity: 0.4356
- Prediction: In this frame, the cheese has been partially removed from the plate, revealing a more pronounced slice of the cheese. The knife's edge is still visible, indicating that the knife has been used to slice the cheese, which is now in the hands of the person who cut it.
- Reference: In this frame, the cake remains largely the same, still maintaining its ringed bundt form. The slice that was previously cut and replaced askew is now absent, removed from the frame entirely. This subtraction leaves a clear demarcation where the slice once was, disrupting the cake's continuity. The doily beneath remains visible, and there are no additional crumbs or changes in the cake's texture or coloration.

#### Sample 253 — During

- Similarity: 0.4356
- Prediction: In this frame, the pan's surface appears to be slightly damp, indicating that the water has been drained from the pan. The water droplets appear to be dripping from the bottom of the pan, suggesting that the soap has been thoroughly rinsed. The pan is now positioned in a downward motion, implying that it's been sprayed with soap and water.
- Reference: In this frame, the rag is more distinctly visible, showing its textured surface more clearly. It's still being held firmly, emphasizing its utilitarian function in cleaning. The wetness of the rag is evident, with certain portions appearing more saturated than others. Its edges are splayed out a bit, showcasing its length and breadth.

#### Sample 256 — During

- Similarity: 0.4345
- Prediction: In this frame, the stove remains in the same position as the previous frame, with the stove still in motion, indicating that the burner has been turned on. The stove's burner remains stationary, and there is no indication of the person's presence, implying that he or she is engaged in a cooking activity. The kitchen remains uncluttered, and the kitchen's focus remains on the stove.
- Reference: In this snapshot, the hand is in closer proximity to the grill, specifically targeting the grate over one of the burners. The thumb appears to be tucked underneath the grate, indicating that the person is preparing to lift or remove it. The condition of the grill remains unchanged from the previous frame, retaining its clean and maintained appearance. The hand's shadow is cast over the cooktop, altering the reflection and metallic sheen of the surface. No other objects or materials are in direct contact with the grill, maintaining a focus on the imminent action of the hand.

#### Sample 258 — During

- Similarity: 0.2403
- Prediction: In this frame, the person's hand is engaged in the process of removing the can'tin from its packaging, which is now firmly grasped by the fingers of the person who is holding the can. The handles of the canister are still in place, suggesting that the contents have been removed from the container. The man's hands seem to be reversing their actions, indicating that the canin is now being handled more carefully.
- Reference: The dish now appears closer to the center of the frame, reflecting a slight shift in focus during the cleaning process. Water droplets and suds cling to its surface, evidencing the use of soap or detergent for cleansing. The presence of a blue scrubbing brush in the sink basin implies that a manual scrubbing action has been or will be applied to the dish. There is less visible residue on the pan's surface compared to the previous state, suggesting that some cleaning has already taken place.

#### Sample 260 — During

- Similarity: 0.4413
- Prediction: In this frame, there is a noticeable movement in the kitchen, indicating that the stove has been turned on. The kitchen counter is now cluttered with a variety of items, including dishes, dishes, and utensils. The counter's surface is still a bit blurry, but it's still visible from a distance, suggesting that there may be a gap between the countertop and the counter. The countertop is now more cluttered, and there's a slight change in the color of the counter, possibly due to a shift in lighting or a change in temperature. The
- Reference: In this snapshot, the kitchen counter continues to hold the focal point with a clear sign of the detergent's presence. The wet area on the counter appears more spread out, indicating it has either been smeared or that more detergent has been applied. A hand is more actively involved in the frame, possibly in the midst of wiping or spreading the detergent. Additionally, a bottle, presumably containing the detergent, is in closer proximity, suggesting it might have been used recently.

#### Sample 269 — During

- Similarity: 0.4958
- Prediction: In this frame, the chopping board has been removed from the cutting board. The knife is now in the middle of the slicing board, with the knife's edge still visible. The pieces of sliced clementia are now scattered across the board, indicating that they have been thoroughly chopped. The leaves are now arranged in a downward-sloping fashion, revealing a more uniform distribution of cactus and stems.
- Reference: The cutting process seems to be more advanced in this frame. There are now more pieces of choi pak arranged on the wooden cutting board. The slices appear to be more uniform in size, suggesting a methodical chopping approach. The green leaves and white stems are more distinguishable now, as the choi pak is being broken down further. The bowl, which previously contained choi pak, is now fuller, indicating that more of the vegetable has been prepped.

#### Sample 275 — During

- Similarity: 0.4557
- Prediction: In this frame, the pot appears to be tilted downwards, indicating that it has been removed from its original position. The pot is now in a more upright position, with the lid still pointing downwards. The kitchen sink appears to have been removed, implying that the pot has been placed in the correct position.
- Reference: In this frame, the cap burner is being grasped by a hand. The fingers envelop its sides, exerting a slight pressure, which can be inferred from the positioning of the thumb and the fingers. The top surface of the cap burner remains largely visible, displaying some wear marks and shadows. It appears to have been lifted slightly from its original position, with an evident gap between the cap burner and the stove base.

#### Sample 279 — During

- Similarity: 0.3684
- Prediction: In this frame, the hand is still motionless, indicating that the microwave has been placed on the counter. The surrounding area is still blurred, suggesting that there are no other objects in the vicinity of the microwave, such as a paper towel or a utensil.
- Reference: In this frame, the cabinet door is still ajar but appears to be more closed than in the previous frame, suggesting a continued motion towards closing. The items inside the cabinet remain the same, and there is no significant change in the organization or arrangement of the contents. The blur is still present, reinforcing the idea of movement. The angle of the door compared to the previous frame suggests it has been moved slightly but is not yet fully closed.

#### Sample 280 — During

- Similarity: 0.4789
- Prediction: In this frame, there is a noticeable movement in the direction of the kitchen or the counter, indicating that the kitchen has been moved. The kitchen is now more cluttered, and there are more items in the kitchen, such as utensils, dishes, and other household items.
- Reference: In this snapshot, the toaster is again partially visible, caught mid-motion. A hand is grasping a drawer handle, possibly searching for an item or in the process of storing something. The motion blur permeates the scene, creating an effect that implies swift, perhaps frantic, activity. The cabinet's wood grain and the handle's details are smeared across the image due to the motion, suggesting that the focus of the action has quickly shifted from the toaster to the drawer.

#### Sample 286 — During

- Similarity: 0.3868
- Prediction: In this frame, the ingredients are more evenly distributed, indicating that they've been thoroughly stirred. The consistency of the sauce appears to be more consistent, with a slight increase in the consistency. The texture of the pasta is more uniform, suggesting that the ingredients have been evenly stirred together.
- Reference: The hand is steadier in this frame, indicating a pause in the action of pouring the mixture into the pan. The mixture is more distributed across the pan but still concentrated towards the center. It gives the impression that the heat has started to permeate through the vegetables, likely causing them to start softening. The colors remain bright and there's a sheen that reflects the heat interacting with the oil, but no significant change in the texture or color of the vegetables can be observed yet.

#### Sample 289 — During

- Similarity: 0.4722
- Prediction: In this frame, the rinsing of the jar appears to have been done in a circular motion, with the water running from the top to the bottom. The water is now dripping into the glass, allowing the water to seep through the glass and into the interior. The hand's grip is still firm, indicating that the water has been drained out of the glass.
- Reference: In this instance, the tupperware is held at a slightly different angle under the running water, allowing for the stream to rinse off any soap suds that may have been on the sides. The container shows less bubbling, suggesting that the washing action is progressing. The hand position remains strategic, with fingers spread out to cover more surface area, possibly to check for any residual food particles or to ensure that all soap is washed away.

#### Sample 294 — During

- Similarity: 0.4038
- Prediction: In this frame, the person's hands are positioned on the stovetop, indicating that they have started cleaning the burners. The stovetop is still in the same state as the previous frame, but there is a slight change in the lighting, possibly due to the presence of a cleaner on the surface.
- Reference: In this instance, the towel is not immediately visible; instead, the focus is on the hands, one of which is holding a clear glass object while the other is manipulating a smaller, bluish-white object that could be a cap or a lid. This suggests that the towel may have been set aside or is being held in a manner that is not captured by the frame. The absence of the towel from direct view implies a shift in the cleaning process or a transition to a different cleaning task.

#### Sample 295 — During

- Similarity: 0.4435
- Prediction: In this frame, the plate is being rinsled with soap suds, indicating that the dish has been washed. The person's hand is holding the plate, pointing to the surface of the dish, which appears to be scrubbing with a cloth or a sponge. The plate's surface is still wet, suggesting that it may have been soiled.
- Reference: The strainer now cradles a vibrant blue sponge, its rough texture indicating its abrasive capabilities for cleaning. Water no longer flows through it; instead, the focus has shifted to the manual scrubbing action, which is suggested by the positioning of the hands and the sponge. Small bubbles from detergent residues cling to the inner walls of the strainer, and the previously visible food particles appear diminished, a result of the ongoing cleaning effort.

#### Sample 297 — During

- Similarity: 0.3709
- Prediction: In this frame, the chicken has been placed in the hands of a person who is preparing to eat it. The chicken remains in the same state as before, and the fingers are now engaged in the process of removing it from the kitchen. The hand's grip on the chicken remains firm, indicating that the chicken is still being handled.
- Reference: In this moment, the person's hands show motion, with the fingers of one hand holding the board steady and the other using the flat side of a knife blade to scrape the garlic off the board. The garlic is no longer in a solid clove form but is now a smeared, pasty consistency, spread thinly across the board. This indicates that the garlic has been crushed to a degree that it's almost paste-like, ready to be added to the pan for cooking. The action of scraping suggests that the person is transferring the garlic into the pan, as the garlic paste is gathered towards the edge of the board.

#### Sample 298 — During

- Similarity: 0.2257
- Prediction: In this frame, the utensil has been removed from the kitchen counter and replaced with a stainless-steel one. The surface of the pan appears to have been removed, indicating that it has been placed on the counter. The kitchen sink appears to be in a state of disrepair, possibly due to a recent cleaning. The sink's surface is still visible, suggesting that it may have been used for cooking.
- Reference: Here, the gloves are again in focus, with the left hand visibly holding onto a pot's edge and the right hand slightly raised, suggesting a moment of transition or the performance of a task requiring a two-handed approach. The bright yellow rubber material of the gloves continues to be prominent, and they maintain a sheen that could either be from the material's natural finish or a slight dampness, possibly from exposure to water.

#### Sample 303 — During

- Similarity: 0.4510
- Prediction: In this frame, the cap has been completely retracted from the bottle, indicating that the cap is no longer in its original state. The hand's grip is still firm, suggesting that the bottle is still in its proper position. The bottle's contents remain the same, but the cap appears to be a bit looser. The cap's position is now slightly different from the previous frame, implying that there is a slight change in the position of the cap.
- Reference: In this snapshot, the same aluminum beverage can is now slightly tilted. The person's hand, identifiable from the same metallic wrist accessory, appears to be pouring liquid from the can into a transparent glass that already has some fluid. The glass exhibits a hint of condensation, indicating the chilliness of its content. The table retains its wooden aesthetic, and the black mat and a fork are visible nearby.

#### Sample 304 — During

- Similarity: 0.4280
- Prediction: In this frame, the tiniest part of the sink appears to be in motion, indicating that it has been agitated. The sink's surface is blurred, suggesting that the sink is still agitating. The water level is slightly higher than usual, suggesting the sink may be clinging to the surface of the water.
- Reference: In this moment, the tin is captured mid-transition, the focus of a simple yet crucial kitchen task. Water is being poured into the tin, producing a dynamic interplay of fluidity against the rigid, stained background of the tin's interior. The stream of water appears forceful, suggesting a vigorous pour, and its impact on the tin’s surface creates a scattering of water droplets and rivulets that momentarily disturb the residual patterns of baked-on remnants.

#### Sample 305 — During

- Similarity: 0.3240
- Prediction: In this frame, there is a noticeable increase in the number of ingredients on the stove, indicating that the stove has been turned on. The stove remains in the same state as before, and the stove's burners are still visible, suggesting that there may be a change in the direction of the cooking process.
- Reference: The perspective shifts to show more of the countertop's expanse, revealing a clean, clutter-free surface that extends towards a cooking area. An array of beer bottles of various sizes and labels stands in an irregular formation near the edge, alongside a pair of clear glasses, one upright and the other tipped over. A wooden spoon lies on a white spoon rest, next to a skillet on the stove filled with a sautéed mixture, indicating a meal preparation in progress. The person's hands are now in view, one holding a sponge, suggesting active cleaning.

#### Sample 309 — During

- Similarity: 0.3107
- Prediction: In this frame, the tomato has been placed in the hands of a person, indicating that it has been thoroughly rinsed. The tomato's surface is still slightly damp, suggesting that the water has been sprayed on the surface of the tomato. The palm of the person holding the tomato appears to be engaged in a downward motion, implying that the tomato is now being rubbed with soap and water.
- Reference: Here, the tap remains in its downward position, but there is a notable change as water starts to flow from its spout. The stream of water is clear, consistent, and seems to be at a moderate flow rate. Droplets of water can be seen splashing around the sink's basin as the stream hits its surface.

#### Sample 310 — During

- Similarity: 0.4542
- Prediction: In this frame, the cake has been removed from the kitchen, revealing a more streamlined appearance. The surface of the cake is now more exposed, indicating that the batter has been placed on the cake. The cake's surface is still a bit damp, suggesting that it has not been fully incorporated into the cake, which is likely due to the time it took to bake.
- Reference: In this scene, the tray is shown in a similar state to the first, maintaining its worn appearance with streaks and spots of oil glistening lightly across its surface. The placement of the three dough balls remains unchanged; however, the perspective is slightly different, indicating a shift in the camera angle or the tray's position. The dough balls appear untouched and consistent in their shape and size with the previous frame, reinforcing the notion that they are in a static state of rest.

#### Sample 328 — During

- Similarity: 0.2589
- Prediction: In this frame, the hand is engaged in the action of removing the bag from the kitchen counter, indicating that the contents of the bag have been removed from the tray. The bag's contents are still visible, but there is a slight movement in the direction of the hand, implying that the bag has been placed in the hands of the person who is holding it.
- Reference: Here, the slice of bread is partially inside the toaster, with only a small portion protruding above the slot. It sits within a gray toaster that seems to be of a modern design, with the red light on the control panel indicating that the toaster is on and actively toasting. The bread has begun its transformation from a soft, pliable state to one that will become crispy and golden-brown, the anticipation of that textural change implicit in the image.

#### Sample 329 — During

- Similarity: 0.4589
- Prediction: In this frame, the hand is engaged in the action of removing the lid from the machine, indicating that the machine has been removed from the coffee grounds. The coffee machine remains in the same state as before, but there is a slight change in the position of the hand, suggesting that the hand may have stepped into the machine's coffee chamber. The hand's position is still unchanged, with the machine still positioned on the counter and the surrounding area still unoccupied.
- Reference: The bag now seems more exposed as compared to the previous frame. The hand appears to be actively engaging with the bag, either adjusting or opening it. The bread inside is more clearly visible, showing its texture and confirming that it is indeed a bread bag. The orange label on the bag is also clearer, and the overall placement of the bag has slightly shifted, implying some interaction has taken place.

#### Sample 335 — During

- Similarity: 0.2955
- Prediction: In this frame, the place mat has been repositioned, indicating that it has been moved to a new position. The position of the mat remains the same as before, but now appears to be in a slightly different position, possibly due to the presence of a hand-held device. The mat's position is now more pronounced, suggesting that the person has moved the mat to another position.
- Reference: The degreaser now shows a different stage of application. The mist has settled slightly, with fewer droplets suspended in mid-air, and more visible accumulation on the surface, forming irregular patterns where the liquid has begun to settle. The hand holding the bottle has moved marginally to the right, indicating the continuation of the spraying action. The countertop reflects less light where the degreaser has settled, indicating the surface is now moistened by the liquid. The spread of the degreaser is more widespread, covering a larger area than in the previous frame.

#### Sample 338 — During

- Similarity: 0.2317
- Prediction: In this frame, the skillet remains in the same state as before, indicating that the pan has been removed from the burners. The pan's surface remains unchanged, suggesting that the skillet has been placed on the stove, allowing the steam to continue to cook. The skillet's temperature remains the same, suggesting a gradual increase in the temperature, which could indicate a change in the cooking process.
- Reference: Upon closer inspection, the extractor fan presents a consistent appearance of wear, with no discernible changes in the distribution or intensity of the grease marks compared to the previous state. The uniformity of the discoloration suggests that the fan has been subjected to a steady amount of heat and airborne particles over a considerable duration. There is no evidence of any cleaning attempts, as the patterns of grease remain uninterrupted and widespread across the entire surface of the fan.

#### Sample 351 — During

- Similarity: 0.3652
- Prediction: In this frame, the cheese has been completely removed from the banana, revealing a more pronounced slice of the cheese. The cheese's skin is still present, and the knife's grip remains firm, indicating that the cheese is still in the hands of the person who grabbed it.
- Reference: Here, the olive oil bottle's cap is being handled by a person, whose hands are the focal point of the image. The cap is grasped firmly between fingers, showing the action of capping in progress. The individual appears to be in the midst of securing the cap back onto the bottle, indicated by the positioning of the hands and the slight squeeze of the fingers, which are attempting to align the cap with the threads of the bottle. This frame captures the motion and intent to seal the bottle after use, ensuring the olive oil's freshness.

#### Sample 353 — During

- Similarity: 0.2987
- Prediction: In this frame, the lid of the food processor appears to have been removed from the machine, indicating that the operator is now engaged in the process of removing the food from the bowl. The user's hand is still holding the control panel in place, suggesting that he or she is preparing to start the process. The surrounding area is still unoccupied, with no visible signs of activity.
- Reference: In this instance, the button is captured in the midst of being pressed. One can discern the initial stages of depression as the button yields to the finger's force. The top surface of the button, which was previously flush with the console, now shows a slight angle indicative of the pressing action, and the shadow around the finger's contact point has deepened, reflecting the change in distance between the finger and the button surface. The light reflection on the button's surface has altered slightly, conforming to the new shape as the button is pushed inward.

#### Sample 356 — During

- Similarity: 0.3834
- Prediction: In this frame, the timer appears to be in motion, indicating that the time has been taken. The timer's position remains the same, suggesting that it is still in motion. The kitchen remains unoccupied, and the kitchen's focus is on the cooking process.
- Reference: In this scene, the pan contains a similar mixture, but the quantity of the liquid appears slightly reduced, indicating that some of the water content has evaporated due to heat. The green elements have a more wilted and cooked appearance, taking on a darker, more olive-like shade. The liquid has a few more visible bubbles, showing signs of gentle simmering, and the mixture is beginning to cling lightly to the wooden spoon, suggesting a slight thickening of the sauce or reduction in volume. The stirring motion seems to be gentle and consistent, maintaining an even cooking process.

#### Sample 359 — During

- Similarity: 0.4454
- Prediction: In this frame, there is a more noticeable presence of a hand, indicating that the sink has been cleaned. The person's hand appears to be engaged in a hands-off action, implying that he or she is cleaning the sink. The sink's surface is still wet, suggesting that the water has been drained out of the sink basin. The water droplets appear to have been sucked from the sink, possibly due to a spill or a clogged drain.
- Reference: The bin is now partially obstructed by a person's forearm, suggesting action in the process of discarding waste. The contents of the bin remain the same, densely packed and unaltered in the brief time lapse between the frames. There is no visible movement of the bin itself, indicating that the person's focus might be on another task, possibly related to cleaning or preparing to dispose of waste. The surrounding area, including the dish rack and countertop, appears unchanged, maintaining the context of ongoing kitchen use.

#### Sample 360 — During

- Similarity: 0.3898
- Prediction: In this frame, the lid has been moved to a new position, indicating that the container has been removed from its original position. The lid remains in the same position as before, but it's now slightly tilted away from the edge of the container. The object's focus is now on the container, which is now positioned in the hands of the person who's grasped it.
- Reference: The fridge door seems slightly more closed compared to the previous frame but is still not completely shut. The LED indicators remain visible and illuminated. The door handle has moved a bit towards its resting position, yet the black interior of the fridge is still partly visible. The reflections on the fridge surface appear slightly different, suggesting a subtle shift in the surroundings or lighting.

#### Sample 361 — During

- Similarity: 0.3482
- Prediction: In this frame, the mozzarella cheese has been fully removed from its packaging. The mozzarella is now in a new state, and the fingers are now able to grasp it with their fingers, ensuring that the cheese remains intact. The cheese's consistency remains the same, but there is a slight change in the way the cheese is being handled. The hands are now engaged in the process of removing the cheese, revealing a slightly different texture to the mozzarella.
- Reference: Now, the hand has shifted focus to the red pepper, which remains partially sheathed in the plastic wrap, hinting at the progression of the unwrapping process. The other peppers are out of sight, possibly set aside for later use. The hand holds the red pepper firmly while the other hand wields the knife, positioned to make a cut. This suggests that the preparatory phase is progressing, moving from unwrapping to cutting. The presence of the knife blade close to the plastic indicates that the cutting is about to begin.

#### Sample 362 — During

- Similarity: 0.4813
- Prediction: In this frame, the cloth is being pulled out of the water, indicating that it has been washed away. The hands are holding the cloth in one hand and the fingers are firmly squeezing it, implying that the cloth has been rinsing. The cloth's surface is still wet, suggesting that the water has gotten into the fabric, resulting in a more pronounced pull.
- Reference: Here, the water tap appears in a similar state as before, with water flowing from its spout. However, there's a subtle change in the positioning of the hands and the tap, indicating an interaction has occurred. The hands are now closer to the tap, implying an action in progress. The stream of water seems uninterrupted, with the liquid's surface tension visible as it flows and splashes into the basin, reflecting the kitchen's ambient light.

#### Sample 363 — During

- Similarity: 0.4307
- Prediction: In this frame, the kitchen sink appears to be in a state of transition, indicating that there is a noticeable movement in the kitchen. The kitchen sink's interior is now blurred, suggesting that the sink has been removed from the cabinet. The surrounding area is still cluttered, with a few items scattered around the kitchen counter, including a pot and a bowl. The cabinet's contents are still visible, but there are still a number of items on the counter, such as utensils, dishes, and other items.
- Reference: The locker in this frame is more obscured than in the previous one, though it remains open. It's challenging to make out specific items due to the angle and blurriness of the image, but it seems that the contents remain unchanged from the previous glimpse. The focus is slightly shifted towards the countertop, yet the open door still captures a significant portion of the frame.

#### Sample 364 — During

- Similarity: 0.1875
- Prediction: In this frame, the toaster is positioned in a slightly different position than before, indicating that it has been stepped on. The kitchen sink appears to be positioned on the kitchen counter, and there is no indication of a hand-over, implying that the hand is engaged in the process of preparing food or cooking.
- Reference: In this frame, the sweet potato shows visible signs of being prepared for consumption. Slices or sections have been neatly cut, revealing its vibrant orange interior. The flesh looks soft, moist, and inviting, contrasting beautifully with the outer skin. The cuts are clean, indicating a sharp knife was used, and the edges of the slices glisten slightly, catching the light in a way that accentuates their fresh, juicy appearance.

#### Sample 368 — During

- Similarity: 0.4041
- Prediction: In this frame, the wrapper is positioned in the hands of a person who is preparing to eat it. The wrapper's surface is slightly exposed, indicating that it has been fully inserted into the container. The contents of the wrap are still present, but there is a slight movement in the direction of the person's hand, implying that the wrap has been partially opened.
- Reference: In this scene, there is no direct view of the tomatoes as the can is absent from the visible countertop. However, the preparation for incorporating the tomatoes into a meal is ongoing. The countertop shows evidence of cooking activity with various items scattered around, such as a toaster, a crumpled plastic bag, and what appears to be the card of recipes or instructions. Without the presence of the tomato can, there's an implication that the tomatoes have been or are in the process of being transferred to another stage of the cooking process.

#### Sample 372 — During

- Similarity: 0.4425
- Prediction: In this frame, the trash can is now in motion, indicating that it has been placed in a position where it isn't being used, implying that it's not being used. The surrounding area is blurred, suggesting that there is a noticeable movement in the direction of the basket, which could be a sign of a recent change in the way the container is being handled. The camera's focus is on the basket's contents, which are more likely to be in the hands of someone or a family member.
- Reference: In this moment, the basket is not visible; the focus is on a person's lower body in motion, with the legs partially seen at the edge of the frame. The feet are clad in sandals, firmly planted on an orange-tiled floor that contributes to the warm color palette of the scene. The person's shadow and the floor tiles suggest a quick, perhaps downward movement, as if stepping or crouching, in the midst of an action that is not fully captured within this particular frame.

#### Sample 389 — During

- Similarity: 0.4691
- Prediction: In this frame, the hand is positioned in front of the coffee maker, indicating that it has been placed in a position where it is likely to be used for brewing. The surrounding area is blurred, suggesting that there is a slight movement in the direction of the hand, implying that the hand may have moved away from the machine. The camera's focus is now focused on the kitchen counter, which appears to be occupied with a variety of items, including a pot, a kettle, and a coffee grinder.
- Reference: This frame shows a different angle of the wooden locker, with more emphasis on the lower part of the cabinet. The door seems to be more ajar compared to the previous frame. Below the locker, there's a countertop which houses several kitchen appliances, including a kettle, toaster, and possibly a mixer. The user's hand is visible, reaching out to the door handle, indicating an intention to open or adjust the door's position. Above the appliances, the bottom edge of the locker has a slight overhang, with handle cut-outs for ease of opening.

#### Sample 391 — During

- Similarity: 0.3368
- Prediction: In this frame, the glove is in a slightly altered state, indicating that it has been removed from its original position. The glove's surface is still wet, but it appears to be clinging to the soapy water, implying that the gloves have been removed. The fingers of the glove are still visible, suggesting that the glove has been placed in the water for a few minutes.
- Reference: In this frame, the chopping board's surface has significantly more water on it, with larger puddles forming in certain areas. The water droplets have spread further, covering more of the board's area. The color distinction between the wet and dry areas remains noticeable, with the wet sections showcasing a deeper shade of blue, possibly indicating that more water has been added or that the existing water has spread.

#### Sample 397 — During

- Similarity: 0.4547
- Prediction: In this frame, there is a slight shift in the direction of the hand, indicating that the hand has moved away from the kitchen or counter. The hand's position remains unchanged, with the hand still pointing toward the kitchen counter, and the kitchen sink still visible.
- Reference: The salt container seems to have been repositioned slightly. While it remains amidst other kitchen items, the shift in its placement suggests that it might have been moved or nudged. The cap appears to remain closed, indicating that the salt inside hasn't been dispensed recently in this frame. The scene appears busier than in the previous frame, perhaps indicating progression in the cooking or preparation process.

#### Sample 403 — During

- Similarity: 0.3314
- Prediction: In this frame, there is a noticeable movement in the direction of the cheese, indicating that the cheese has been thoroughly incorporated into the dough. The cheese's surface is still slightly damp, suggesting that it may have been squished or melted before being placed on the cutting board.
- Reference: The onion slices have been further processed in this frame. They are now laid out on what appears to be a piece of bread or perhaps a base for a pizza or flatbread. The slices are arranged to cover most of the surface area of the bread, slightly overlapping in places. The arrangement is deliberate, ensuring even distribution and coverage. The onions still retain their fresh appearance, with the edges looking slightly translucent, a characteristic feature when onions are thinly sliced.

#### Sample 406 — During

- Similarity: 0.4368
- Prediction: In this frame, the bin has been fully emptied, with the lid still in place. The bin's contents remain the same, and there is no noticeable movement in the room, suggesting that the bin is now empty. The person's hand appears to be holding the bin, indicating that he or she has removed the trash from the bin.
- Reference: In this frame, the strainer is still held, but now its bottom faces more towards the ground. The orange-yellow liquid that was once prominent in the strainer has lessened considerably, and the strainer appears more vacant. While traces of the liquid remain, it's evident that a substantial amount has already been poured out or drained. The strainer's white surface now contrasts with the remnants of the liquid, highlighting the empty spaces between the fine mesh.

#### Sample 408 — During

- Similarity: 0.3178
- Prediction: In this frame, the oil has started to spread across the surface of the dough, indicating that it has been incorporated into the dough's composition. The texture of the oil appears to be more uniform, with a slight change in the direction of the spread. The oil's consistency is more consistent, suggesting that it's being spread more evenly, rather than spreading at a slower pace.
- Reference: In this frame, the person's hand has made progress in opening the bottle. The cap seems to have been slightly loosened, allowing for the content within the bottle to be accessed soon. The fingers grasp around the neck of the bottle, exerting a gentle pressure indicating the act of unscrewing the lid. The base of the bottle remains firmly over the tortilla, poised to dispense its contents.

#### Sample 410 — During

- Similarity: 0.4734
- Prediction: In this frame, the corn kernels appear to have been removed from the corn, indicating that the corn has been thoroughly incorporated into the corn. The corn is now more evenly distributed, with the kernels spreading out across the corn's surface, resulting in a more even distribution of the corncorns.
- Reference: The scene shifts slightly to show a hand actively engaged in the act of sprinkling sweetcorn onto the pizza. The kernels are in a state of descent, some possibly caught in the very moment of leaving the can, while others are likely just making contact with the saucy surface below. The sweetcorn's distribution is uneven, with a cluster gathering more densely in one area, indicating the initial point of contact from the can. The act of sprinkling is captured dynamically, with the potential for motion blur on some kernels indicating their rapid journey onto the pizza.

#### Sample 411 — During

- Similarity: 0.4562
- Prediction: In this frame, the container has been moved to a new position, with the lid still in place. The contents of the container remain in the same position as before, indicating that the container is now in a different state. The container's position remains the same, but the contents are now more visible.
- Reference: In this scene, the pot is absent, indicating that it has been picked up from the sink. The absence of the pot reveals more of the sink's basin, highlighting the used state of the kitchen. The scene includes a chopping board with a red-handled knife and a metal spoon resting on it, which suggests that food preparation or another cooking task was recently undertaken. The blurry foreground implies a swift movement, either of the pot being moved out of the frame or the camera itself moving.

#### Sample 412 — During

- Similarity: 0.4830
- Prediction: In this frame, the peeler appears to be in a slightly different state, with a more streamlined appearance. The peeler's surface is still slightly wet, but the water droplets are still present, indicating that the water has been drained out. The waterdrops appear to be clinging to the bottom of the stalks, implying that they have been rinsing or washed. The hand-held camera captures a steady stream of water, which indicates that there is still a lot of water on the stalk.
- Reference: The grip on the spring onion has shifted slightly, indicating motion. The fingers are now closer to the white bulb, possibly to provide better control during the cleaning process. The onion is now positioned directly under the faucet, and the water droplets on its surface reflect the onset of rinsing. The green tops are now slightly more splayed, likely due to the water's pressure, and there is a more pronounced curvature in the stalks, suggesting flexibility and crispness.

#### Sample 415 — During

- Similarity: 0.3762
- Prediction: In this frame, there is a noticeable shift in the position of the pan. The pan's position is now blurred, indicating that the pan has been moved, possibly to a different location. The area around the pan is now more cluttered, suggesting that it may have been moved or placed in a new location.
- Reference: The lunch box is now opened slightly, revealing more of its interior. Through the opened part, it's noticeable that there is a light-colored content, which might be a type of food, possibly a sandwich or wrap given its layered appearance. The label on the transparent lid is more apparent in this frame, and the red hue of the box is still visible.

#### Sample 433 — During

- Similarity: 0.3506
- Prediction: In this frame, the bin's position is blurred, indicating that the bin has been removed from the scene. The bin remains in the same position, with the lid still in place, suggesting that it has been moved. The camera's focus is on the bin, which appears to be in a state of transition, possibly due to a change in the direction of the bin or the movement of the hand.
- Reference: Here, the cloth seems to be in a state of being actively squeezed. The fingers are pressing into the material, which is gathered and twisted to wring out the liquid. This action has created darkened wet patches on the cloth's surface, implying that the moisture is being expelled. The cloth's twisted sections are tightly compressed, and the surrounding area suggests a more vigorous motion compared to the previous state, reflecting a more dynamic phase of the wringing process.

#### Sample 436 — During

- Similarity: 0.3615
- Prediction: In this frame, the kitchen knife is now in motion, indicating that the knife has been removed from the kitchen counter. The kitchen knife remains in the same state as before, but the knife's position remains unchanged, implying that the hand is now engaged in the process of removing the knife.
- Reference: In this snapshot, the peeler has been set down on the cutting board, its handle extending towards the bottom edge of the frame. It lies adjacent to a vividly colored eggplant peel, showcasing the contrast between the peeler's utilitarian design and the organic curvature of the peel. The blade end of the peeler is slightly obscured by the discarded peel, indicating that it has been recently used. The surrounding area is sparsely littered with small flecks of peel and moisture, possibly from the eggplant, suggesting a scene of ongoing food preparation.

#### Sample 437 — During

- Similarity: 0.4902
- Prediction: In this frame, the knife has been removed from the cutting board, revealing a sharper edge. The knife's grip remains firm, suggesting that the knife is now in the position it was in during the previous step. The surface of the knife remains untouched, indicating that there is still a lot of work to be done on the knife.
- Reference: The pepper pieces remain on the wooden chopping board, but they have been slightly rearranged or shifted, possibly due to some movement or external interference. They seem to be closer to the edge of the board, hinting at a potential transition in their placement. Their bright yellow color still stands out prominently, showcasing their freshness.

#### Sample 446 — During

- Similarity: 0.3599
- Prediction: In this frame, the moka pot appears to be in motion, indicating that the pot has been removed from the burner. The pot's handle is still stationary, suggesting that the person is engaged in the process of removing the pot from the stove. The moka's contents are still present, but the pot is still tilted slightly away from the flame, implying that the liquid has been added to the pot.
- Reference: The bottle of oil is now in an upright position, secured by the same hand, which has moved closer to the bottle’s opening, suggesting that the process of closing the bottle has advanced. The cap, still enveloped in the tissue, is closer to the top of the bottle, indicating an imminent action of resealing the bottle. The hand's positioning is more relaxed, suggesting a smoother process than before, possibly because of the tissue absorbing the slipperiness of the oil.

#### Sample 450 — During

- Similarity: 0.3068
- Prediction: In this frame, the ingredients have been added to the pan, indicating that they have been removed from the oven. The ingredients appear to have been incorporated into the pan's surface, revealing a slightly different texture and texture. The cooking process appears to have started, with the ingredients being placed in a single layer on the bottom of the pan.
- Reference: The hands of the person preparing the pizza are in motion, indicating the action of sprinkling the chili pieces. It appears that the individual is in the process of evenly distributing the chilis, as evidenced by the placement of the pieces across the entirety of the pizza base. The motion blur of the hands suggests a gentle shaking movement, helping to disperse the chili pieces more broadly across the pizza. There is a slight accumulation of chilis on one side, which may be due to the manner in which the person has directed their sprinkle.

#### Sample 457 — During

- Similarity: 0.3122
- Prediction: In this frame, the bowl has been removed from its original position, indicating that it has been moved to a new location. The bowl remains in the same position as the previous frame, but there is a slight movement in the direction of the hand, which indicates that the hand is now engaged in the process of removing the bowl.
- Reference: The mixture now presents a smoother consistency, with fewer visible lumps, indicating that it has been stirred more thoroughly since the last frame. The color remains consistently yellow with green flecks, but the specks are more evenly distributed throughout the mixture. It has a glossy sheen, which could suggest the incorporation of a fat component, like oil or butter. The surface has a more uniform texture, with the swirls from stirring being tighter and more integrated, showing a progression in the mixing process.

#### Sample 459 — During

- Similarity: 0.2546
- Prediction: In this frame, there is a noticeable shift in the direction of the hand, suggesting that the hand is engaged in some sort of action. The hand appears to be in a downward motion, implying that it's been agitated, possibly by a hand-held device, or a chopping action.
- Reference: In this scene, the can is now held aloft by a human hand, gripped firmly around its body. The lid is in a further state of detachment, peeled back to expose more of the contents within, which are indeed small, spherical, and uniformly sized, corroborating the initial presumption of peas or corn. The opening of the can now allows for a clear view into the interior where the contents are packed in liquid, likely brine or syrup, which is typical of canned produce.

#### Sample 463 — During

- Similarity: 0.4816
- Prediction: In this frame, the pot remains in the same position as before, with the pot still positioned on the counter. The surrounding area is no longer visible, indicating that the pot has been turned off. The kitchen sink remains unoccupied, and there is no indication of the pot's presence.
- Reference: In the second frame, the surroundings of the switch become slightly more discernible, but the state of the switch is still not entirely clear. The image features a hand near what appears to be the kitchen countertop or appliance interface, suggesting some interaction might be occurring. There's an indication that the hand might be grasping or reaching for something, possibly the switch. However, the exact state, whether it's turned on or off, remains ambiguous due to the blurriness.

#### Sample 469 — During

- Similarity: 0.4716
- Prediction: In this frame, there is a noticeable movement in the direction of the kitchen, indicating that the food is being prepared. The kitchen is now cluttered with a variety of items, including utensils, dishes, and other household items. The focus is now on the kitchen area, which appears to be occupied by a handful of kitchen items, such as bread or a pot of soup.
- Reference: In this frame, the cover is noticeably being interacted with, as evidenced by the hand positioning around its sides. The cover's surface still displays a sheen, reinforcing the notion that it could be a reflective material. The curvature of the cover is more prominent here, hinting at its domed shape. It appears to be slightly tilted or in motion, possibly due to the person's actions. Adjacent to the cover, one can identify a stove's burner, indicating the cover's position relative to the cooking surface.

#### Sample 470 — During

- Similarity: 0.3407
- Prediction: In this frame, the hand is engaged in the process of removing the bottle from its original position, implying that the bottle is now in a new position. The hand's grip remains firm, indicating that the liquid has been removed from the bottle. The bottle's contents are still present, and the hand appears to have grasped the bottle with one hand, allowing the liquid to fall into the hands of another person.
- Reference: In this moment, the plug is further removed from the outlet compared to the previous frame. The individual's grip on the plug is firm, indicated by the slight compression of the yellow rubber gloves around their fingers. This suggests a deliberate action, likely the act of unplugging. The plug's prongs are more visible now, and it appears to be a standard, non-grounded two-prong plug. The background remains unchanged, crowded with kitchenware and items, which are out of focus.

#### Sample 480 — During

- Similarity: 0.1690
- Prediction: In this frame, the plastic bottle has been re-opened, revealing a more streamlined appearance. The packaging is now positioned in a slightly different position, indicating that the contents have been removed from the container. The hand's grip on the bottle is still firm, suggesting that the plastic has been handled with care.
- Reference: Now, the liquid washing up is being actively applied onto the sponge. The stream of the liquid can be discerned as it makes contact with the sponge, creating a wet spot. This wet spot reflects light differently than the rest of the sponge, indicating that the sponge is beginning to absorb the liquid.

#### Sample 481 — During

- Similarity: 0.4698
- Prediction: In this frame, the person is holding the utensil and rinsing the ricotta in a downward motion, indicating that the water has been drained from the rim of the sink. The water droplets appear to be clinging to the bottom of the receptacle, implying that they are being rinsed. The camera's focus is on the sink's surface, which appears to be tilted away from the water, suggesting that the sink may have been clung to the water's edge.
- Reference: Now the jug begins to fulfill its purpose, with a steady stream of clear water cascading into it from the faucet above. The flow is centralized, targeting the heart of the jug’s basin, causing a swirl of bubbles to form on the surface as air is displaced by the incoming water. The hand adjusts slightly to stabilize the jug against the force of the water, while the level of the liquid rises visibly, indicating the jug's capacity is being tested.

#### Sample 482 — During

- Similarity: 0.3624
- Prediction: In this frame, the film has been removed from the tray. The film's surface is now more exposed, with the center of the film separating from the peel. The person's hands are now able to grasp the film with their fingers, ensuring that the film remains intact.
- Reference: In this frame, the packaging of the lighter meat, possibly chicken, is being interacted with. A pair of hands can be seen grasping the package, where one hand holds the body of the package while the fingers of the other hand appear to be prying or pinching at a corner of the seal. Despite this, the plastic wrapping remains mostly undisturbed, and the meat inside the package is still concealed. There's no sign of the seal being fully breached at this point.

#### Sample 485 — During

- Similarity: 0.4536
- Prediction: In this frame, the contents of the package have been removed from the box. The person's hands are now firmly grasped, indicating that the package has been placed in a new position. The packaging is now positioned in the hands of the person who opened it, implying that the bag has been opened.
- Reference: In this scene, the milk carton has been released from the person's grasp and is captured in mid-descent towards the floor. The green carton with its label is in a vertical orientation, with the top side facing downward, suggesting it may not have been securely closed. The background is less cluttered here, featuring a broom and a dustpan against a wall, and what appears to be a container lid on the floor, indicating that the carton is likely falling in an area adjacent to the kitchen or a utility space.

#### Sample 487 — During

- Similarity: 0.4644
- Prediction: The camera pans through a window, revealing a kitchen area with a white countertop, a sink, and a counter top. The kitchen area is cluttered with utensils, dishes, and other household items, indicating that there is a variety of items on the counter. The countertop appears to be in a state of deterioration, possibly due to the use of a microwave oven or oven.
- Reference: The perspective has shifted closer to the microwave, which dominates the frame, now fully opened. The person's hand is more prominently featured, moving rapidly, as indicated by the motion blur of the sponge. This closer view reveals a clearer sight of the sponge's texture and the cleaning action it's engaged in. The stove top is out of view, but the continued presence of the kettle to the left and the microwave's control panel hints at the kitchen's functional use. The cleanliness of the microwave's interior contrasts with the task at hand, focusing on the appliance's exterior.

#### Sample 488 — During

- Similarity: 0.4989
- Prediction: In this frame, the lettuce has been re-rinsing again, with the water still dripping from the bottom of the bowl, indicating that it has been thoroughly rinsed. The leaves are now more exposed to the water, suggesting that the water has gotten deeper into the leaves. The water is still running through the leaves, which may indicate that they have been washed.
- Reference: Here, the leaf is still subject to the cleansing process, with water continuing to flow over its surface. It appears to be slightly more saturated with water, causing the leaf to adhere to the person's fingers due to the increased weight and surface tension of the water. The central rib of the leaf is more prominent, indicating the leaf may be slightly more pliant from the water absorption. This suggests that the washing has been thorough, reaching deep into the crevices and folds of the leaf.

#### Sample 490 — During

- Similarity: 0.3159
- Prediction: In this frame, the person is removing the plastic wrap from the bottom of the container, revealing a portion of the contents. The person's hands are now engaged in the process of opening the package, indicating that the contents have been removed from the container.
- Reference: In this moment, the tortilla is being maneuvered back towards its original packaging. The hand's grip has shifted, now supporting the tortilla more from beneath, with the fingers curving upwards, cradling its base. The tortilla's flexibility is evident as it displays a gentle droop, arching downwards due to gravity. Its surface is still unblemished, and it retains the circular shape characteristic of a classic tortilla, highlighting its apparent softness and readiness for use.

#### Sample 495 — During

- Similarity: 0.3103
- Prediction: In this frame, the drawer's position remains unchanged, indicating that it has been moved to a new position. The drawer is in a slightly different position from the previous frame, which suggests that the drawer has been removed from its original position.
- Reference: The plug remains in a similar position, but now it appears to be slightly askew, suggesting that a pulling force has been applied. The prongs are still engaged with the socket, but the angle at which the cord extends has shifted, becoming more pronounced towards the right, indicating movement. The environment is consistent with the previous frame, with the wooden chair leg, white skirting, and yellow tiling composing the surroundings. The plug's facade is more visible, and the socket looks standard with no distinct features or damage.

#### Sample 496 — During

- Similarity: 0.4101
- Prediction: In this frame, the paper appears to be in a different state than before, indicating that it has been handled differently. The paper's surface is slightly different from the previous frame, suggesting that it may have been handled more carefully. The person's hands seem to be grasping the paper, implying that they are holding it in their hands.
- Reference: In this scene, the popcorn bag is held steadily, likely immediately after being shaken, as the hand and the bag are less blurred compared to the previous frame. The text and graphics on the bag are now legible, showing icons and instructions for proper microwave use. The top of the bag appears slightly inflated, a sign that the popping process has occurred or is nearing completion. The person's grip on the bag is firm, their thumb pressing down on the front face, possibly feeling for the consistency of the popped kernels inside.

#### Sample 497 — During

- Similarity: 0.2789
- Prediction: In this frame, the kitchen sink appears to have been wiped down with a damp cloth, indicating that the sink has been thoroughly cleaned. The surface of the sink is now more cluttered, with the sink's surface still slightly damp, and there is a noticeable movement in the direction of the person's movements. The hand's hands are now engaged in a downward motion, implying that they've been slicing away at the sink.
- Reference: In this subsequent image, the same yellow glove is depicted, but this time, the hand's posture has changed, showcasing the glove's flexibility. It seems the wearer is engaged in a different task as the hand is positioned near a stove, handling another object. The glove appears to be well-fitted to the hand, as there aren't any noticeable wrinkles or sagging areas, emphasizing its functional design.

#### Sample 2 — After

- Similarity: 0.4916
- Prediction: In this frame, the water has been removed from the glass, indicating that the glass has been fully emptied. The glass remains in the same state as before, and the water is still visible in the glass's rim. The water level remains unchanged, and there is no indication of the presence of any liquid in the water.
- Reference: In this frame, the bottle maintains its upright position, and there is no visible change in the liquid level. The cap has made contact with the bottle's opening, as evidenced by the position of the hand, which has shifted slightly to apply downward pressure, suggesting the beginning of the sealing process. The fingers appear to be closing in, preparing to twist the cap, and the thumb is positioned for leverage. The cap is angled slightly, indicating that it has not yet been properly aligned with the threads of the bottle's neck.

#### Sample 7 — After

- Similarity: 0.4074
- Prediction: In this frame, the contents of the cupboard are more visible, indicating that the person is now engaged in the action of removing the contents from the cabinet.
- Reference: In this final frame, the jar has landed on the wooden floor, its positioning now horizontal. The lid still appears to be tightly sealed, with no visible breakage or spillage from the jar itself. The shadow it casts is elongated and to the side, indicating the presence of a light source to the upper right of the scene. The jar's placement, close to the open dishwasher, suggests that the fall was not far, and the wooden flooring may have somewhat cushioned the impact.

#### Sample 8 — After

- Similarity: 0.3488
- Prediction: In this frame, the button has been fully pressed, indicating that it is ready to be turned on. The button's position remains unchanged, suggesting that the button is still in its current position. The surrounding area of the button appears to be positioned in the same position as before, implying that it has been pressed into the desired position.
- Reference: The toaster's lever is now completely depressed, with the slots wholly accommodating the bread for toasting. A radiant, warm orange glow emanates from within the slots, indicative of the fully active heating elements. The surrounding countertop captures the gentle light spill, creating a cozy ambiance. The power indicator light is now brightly illuminated, confirming that the toaster is in full operation. A slight hint of steam or heat waves can be seen rising, testifying to the toasting in progress.

#### Sample 20 — After

- Similarity: 0.3259
- Prediction: In this frame, the package has been placed in the hands of the person who is holding it. The person's hands are now engaged in the process of removing the package, indicating that the contents have been removed from the package. The packaging is still in its original packaging state, but the hands have been able to grasp the contents with their fingers, implying that the package may have been opened.
- Reference: Here, the yogurt's state has further evolved. It has been placed down with the hand retracting from the action, implying that the positioning of the yogurt container has been completed. The container rests at an angle, distinct from its previous upright position, which contributes to a sense of completion or finality in the sequence of arranging the containers. The kitchen setting serves as a passive backdrop, with the light reflecting off the surface indicating a well-lit environment.

#### Sample 30 — After

- Similarity: 0.4874
- Prediction: In this frame, the pot has been lowered into the water, indicating that the water has reached the bottom of the pot. The water is now dripping from the pot, resulting in a sprinkling of bubbles. The sink's surface is still damp, but there are still a few drops of water on the surface, suggesting that there may be a slight movement in the water's flow.
- Reference: In this frame, the colander has been moved further to the side, and the rice grains are dispersing more evenly across its surface. The tilt is more pronounced, and water can be seen dripping from the bottom, indicating that the shaking motion has effectively encouraged the drainage of water. The hand continues to hold the colander steadily, and the rice grains look more separate from each other, which is typically desired after washing to prevent over-clumping during cooking.

#### Sample 31 — After

- Similarity: 0.3265
- Prediction: In this frame, the surface of the table has been wiped with a damp cloth, indicating that it has been thoroughly cleaned. The wiper remains stationary, and there are no visible streaks of dirt or grime on the surface. The surface is now cleaner and more uniformly arranged, suggesting that the cleaning process has been completed.
- Reference: The glass has been repositioned further to the right, confirming the continuous movement from the previous frame. The person's hand has moved along with the glass, indicating a controlled slide. The blurred reflection on the base of the glass is more pronounced, showing a consistent movement. There's a dynamic interaction between the hand and the object, where the hand's steadiness and the glass's balance appear synchronized in the action of sliding.

#### Sample 32 — After

- Similarity: 0.4131
- Prediction: In this frame, the tomato has been moved closer to the camera, indicating that it has been placed in the hands of the person who is handling it. The tomato's position remains unchanged, suggesting that the person is engaged in some sort of action, such as removing it from the kitchen or placing it in a container.
- Reference: The plastic wrap has been drawn further back, exposing a larger portion of the lettuce head. The leaves now have more space to fan out, and they exhibit a mixture of light and dark green shades, characteristic of the leafy layers of the head. It's evident that the lettuce is still quite fresh, with the leaves showing a healthy, plump appearance. The person's hands are more engaged in the unwrapping process, suggesting an eagerness or readiness to prepare the lettuce for consumption or use in a dish.

#### Sample 33 — After

- Similarity: 0.2985
- Prediction: In this frame, the knife has been moved to a new position, indicating that it has been placed in the same position as the previous frame. The knife's position remains unchanged, and the hand's movements have been reversibly redirected to the next frame.
- Reference: In this frame, the cabinet door has been pulled open even more, almost to its fullest extent, allowing a full view of the shelves. The lower shelf's orderly array of cans is completely visible now, and the upper shelf reveals a collection of various-sized items that seem to be jars and other containers, some with identifiable labels, others obscured by the angle. The items on the upper shelf are less uniformly arranged than the cans below, suggesting a more casual approach to placing frequently used items within easy reach.

#### Sample 36 — After

- Similarity: 0.4379
- Prediction: In this frame, the cheese has been progressively removed from its original position. The butter remains in the same state as before, but the bread's surface remains slightly exposed, indicating that it has been thoroughly removed. The sandwich's interior remains unchanged, with no noticeable changes in the shape or color of the cheese.
- Reference: The tub has been opened, revealing the golden buttery spread inside, which has a smooth surface except for a slight disturbance where a portion has been skimmed off, most likely by the knife previously seen in the right hand. The lid has been neatly flipped open and placed back onto the tub, but slightly ajar, indicating recent use. The consistency of the butter appears soft, as is common with spreads of this type, and a small portion adheres to the knife's edge, showing it has just been used.

#### Sample 41 — After

- Similarity: 0.3391
- Prediction: In this frame, the tray has been placed in a new position, indicating that it has been removed from its original position. The tray's surface is still visible, but there is a slight movement in the direction of the sink, implying that the tray is now in its current position.
- Reference: In this final frame, the milk bottle maintains its central position in the scene, with the cap clearly in a different state compared to earlier images. The hands seen in the periphery are positioned as though they are in the process of closing or have just finished closing the bottle. The cap appears to be settled more securely on the bottle, suggesting the action of sealing the bottle is either complete or nearly so. The lighting and reflections remain consistent, highlighting the bottle's curves and the cap's smooth, round shape.

#### Sample 45 — After

- Similarity: 0.3024
- Prediction: In this frame, the liquid has been poured into the glass, revealing a smoother surface. The surface of the glass is now more pronounced, indicating that the water has been removed from the glass. The glass's surface is now slightly softer, suggesting that the liquid is still a bit damp. The liquid's texture is more consistent, exhibiting a more rounded appearance.
- Reference: The jam is now in a more disheveled state, with some of it smeared on the side of the bowl and a smaller quantity adhering to the fork. It has lost its initial compact shape, becoming more spread out and less uniform. The strands that once connected the jam to the jar have been broken, leaving behind only a thin, tapering trail from the fork to the last of the jam's body, suggesting the completion of the transfer process.

#### Sample 56 — After

- Similarity: 0.4031
- Prediction: In this frame, the holder of the jar appears to be engaged in the process of removing it from its original position. The jar's contents are still visible, but there is a slight movement in the direction of the hand, indicating that the action has taken place.
- Reference: The packaging is now in an advanced state of crumpling. The hand has shifted position, now grasping the lower part, indicating a progression in the crumpling process. The once cylindrical shape of the packaging is significantly distorted, with multiple folds and creases compacting it into a smaller, irregular form. The reflective surface is mostly crinkled, losing much of its initial luster and now exhibits a matte finish due to the extensive manipulation.

#### Sample 57 — After

- Similarity: 0.4056
- Prediction: In this frame, the foil has been removed from the inside of the bag, revealing a more streamlined appearance. The hand's grip remains firm, indicating that the bag has been properly removed from its packaging. The bag's contents remain in the same state as before, but there is a slight change in the position of the foil, reversing the previous position.
- Reference: The filter is now held at a more pronounced angle, with the coffee maker slightly out of immediate reach below. The hand's grip has shifted to support the filter's base, likely to provide stability as the weight of the grounds could cause tearing or spillage if not handled carefully. The radial structure of the filter's base is more pronounced, possibly due to the changing grip and angle at which the filter is held. There's a clear intent to transport the used filter, possibly to a trash receptacle.

#### Sample 61 — After

- Similarity: 0.3554
- Prediction: In this frame, the table has been rearranged in a slightly different manner. The table's position remains the same as before, but now it's positioned closer to the center of the table, indicating that the table is now positioned in the same position as before. The napper's hand appears to have moved the table from the previous position, implying a shift in the position of the napper.
- Reference: In this frame, the crumb has been decisively moved from its original position, now closer to the vacuum cleaner's nozzle. The disturbance in the fabric of the tablecloth around the crumb is more pronounced, with folds and creases leading towards the nozzle, visually narrating the path of movement. The crumb itself is more obscured by the shadow of the vacuum cleaner, highlighting the imminent action of it being picked up. The proximity to the nozzle and the altered lighting condition suggest the crumb's journey is nearing its end.

#### Sample 74 — After

- Similarity: 0.4994
- Prediction: In this frame, the flour has been incorporated into the mixing bowl, indicating that it has been thoroughly stirred. The flour's consistency is more consistent, with a smoother texture and a more homogeneous texture. The movement of the hand is more deliberate, implying the presence of a larger portion of the flour, which is likely to be used for the preparation of the meal.
- Reference: In this frame, the scale has been relocated further to the left, with the person's hand grasping its right edge, indicating movement. The display remains inactive, confirming that the scale has not been utilized for any weighing task up to this point. The glass platform of the scale now partially overlaps with the notebook, while the left hand steadies the bowl, ready to receive ingredients. This repositioning signals a transition from preparing to actively using the scale for the intended measuring task.

#### Sample 82 — After

- Similarity: 0.3653
- Prediction: In this frame, the tap's water flow has been reduced to a minimum, indicating that the tap has been fully emptied. The faucet's surface is still slightly damp, suggesting that the water has not been dripping from the tap. The tap has a slight flow of water, implying that it has been turned off.
- Reference: The cloth now appears to be almost fully extended between the hands, reaching the final phase of the rinsing process. One can see the clear delineation of its edges, and the cloth seems to be more uniformly wet, lacking any dry spots. The hands are positioned in a way that suggests a final wringing or shaking out, prepping the cloth to be possibly hung up to dry. The water stream impacts the cloth directly, indicating the rinse is still actively ongoing.

#### Sample 86 — After

- Similarity: 0.2351
- Prediction: In this frame, the contents of the plastic bag have been retrieved from the freezer. The bag is now in a new position, indicating that the contents have been fully incorporated into the bag. The person's grip on the bag appears to be more firm, suggesting that the bag may have been handled more quickly.
- Reference: The leek's trajectory continues its unwelcome descent, now even closer to the ground. The motion blur has intensified, especially around the green leafy ends, indicating an acceleration of its fall. The plastic sheath appears more disheveled, possibly due to air resistance and the leek's own motion. The leek's base end, once pristine white, is now almost out of view, implying it may have rotated slightly as it fell, with the possibility of impact becoming more imminent.

#### Sample 88 — After

- Similarity: 0.4118
- Prediction: In this frame, the lid has been removed from the container, indicating that the lid is no longer in its original position. The lid remains in the same position as the previous frame, but the lid appears to have been opened. The person's hands are now engaged in the action of removing the lid, implying that the container is now in its proper position.
- Reference: In this frame, the hands grasp the container more securely, and a notable shift in the arrangement of the cheese slices can be observed. The top slice has been disturbed from its previously neat stack, now protruding at an angle indicative of potential selection or preparation for use. This slight disarray contrasts with the earlier orderly presentation, conveying a sense of imminent consumption or culinary application.

#### Sample 89 — After

- Similarity: 0.2842
- Prediction: In this frame, the knife has been moved away from the table, indicating that it has been removed from the workspace. The knife's position remains unchanged, suggesting that the knife is no longer in the position it was in before. The kitchen sink appears to be positioned in the same position as the knife, implying that it is now in the hands of the kitchen staff.
- Reference: In this frame, the squash container seems to retain its position from the second frame, with minimal to no noticeable difference. The label graphics remain visible, reiterating its blue and green hues. The proximity of the white cap to the container is consistent with the second frame, emphasizing that the cap has not been replaced.

#### Sample 100 — After

- Similarity: 0.1423
- Prediction: In this frame, the tea kettle is in a more upright position, indicating that the hand is engaged with the kettle's handle. The hand's position remains unchanged, suggesting that the kettle is still in the position it was when it was first placed. The camera's focus shifts to the action of the kettle, implying that it is now positioned in the hands of the user. The overall state of the teakettle's surroundings is more consistent with the previous frame, which suggests that it has been placed in the same position as the kettle.
- Reference: The scene has now been enveloped in darkness, with the light source seemingly turned off. The absence of light has rendered the room's details nearly indiscernible, with only vague shapes and forms distinguishable in the deep shadows. What were once reflective surfaces have now blended into the obscurity, losing the luster they exhibited when illuminated. The environment exudes a sense of stillness and quiet, typical of a space where the light has been switched off and night has fallen.

#### Sample 110 — After

- Similarity: 0.4308
- Prediction: In this frame, the cabinet's position remains unchanged, indicating that it has been moved. The absence of any visible obstructions suggests that the cabinet is now in a state of disrepair. The overall state of the cabinet remains the same, suggesting that there are no signs of progress.
- Reference: In this frame, the chair has been moved further from the table, and its orientation has changed noticeably. The distance between the chair and the table has increased, which is evident by the larger expanse of tiled floor now visible between them. The chair's shadow stretches out on the floor, altered by the movement and the angle of the light source. The chair's position relative to the camera has shifted, suggesting continued movement.

#### Sample 111 — After

- Similarity: 0.3612
- Prediction: In this frame, the sink's surface appears to be in a downward motion, indicating that the water has been drained. The person's hands are still present, suggesting that the sink has been thoroughly cleaned. The sink is now more cluttered, and there are no visible traces of soap or water on the surface. The hand's movements are more deliberate, implying that they've been scrubbing the sink with a cloth or paper towel.
- Reference: The cloth now appears to be in a more relaxed state compared to the previous frame. Its texture and spread suggest that it has been released or lessened from the squeezed position it was in earlier. While it still retains numerous folds and creases, it looks more spread out, indicating the release of pressure. The cloth continues to display signs of dampness, and its positioning suggests it's still being held or manipulated, albeit with less force than before.

#### Sample 112 — After

- Similarity: 0.1705
- Prediction: In this frame, there is a noticeable shift in the direction of the stove, indicating that the stove is no longer in use. The stove's interior is now more cluttered, suggesting that it may have been used for a purpose other than cooking. The kitchen sink appears to be in a state of disrepair, implying that the kitchen sink has been removed or replaced. The lighting in the kitchen seems to be dim, suggesting the stove may be in need of a refresh.
- Reference: In this final frame, the action of sealing the bag is near completion. The fingers have rolled the top of the bag tightly, indicating an effort to preserve the coffee's freshness. The bag’s texture shows the crinkles and folds resulting from the rolling process, and it's being held just above the counter, where a coffee mug with a used filter sitting beside it suggests that coffee has just been brewed. The bag's placement and handling convey a sense of care and routine.

#### Sample 116 — After

- Similarity: 0.3167
- Prediction: In this frame, the carrots have been removed from the cutting board, indicating that they are ready to be used. The carrots are now placed on a cutting board in the same position as the pot, implying that they have been inserted into the pot. The kitchen is now cluttered with utensils and potpourrins, suggesting that they may be ready for use.
- Reference: Here, a person's hands are actively engaged with the ingredients, signaling a step forward in the preparation process. One hand holds the white bowl, tilting it slightly, while the other hand stirs or mixes the sweet potatoes inside. The act of mixing suggests the integration of flavors or ingredients, and there's a sense of urgency or momentum in the person's movements. The surrounding area remains consistent with the previous frame, with the various ingredients and utensils present on the countertop.

#### Sample 117 — After

- Similarity: 0.4780
- Prediction: In this frame, the bowl is held in the hands of a person, indicating that the water has been drained from the tap. The hand's grip is firm, suggesting that the bowl has been properly rinsled. The water flows through the bowl, resulting in a stream of bubbles forming on the surface of the bowl.
- Reference: The plate is again in a different position, now held horizontally with both hands, with fingers extended and palms facing downwards, suggesting a gentle scrubbing or wiping motion. The running water envelopes the plate, suggesting thorough rinsing. The proximity to the camera gives a clear view of the water interacting with the plate's surface, and the individual's wristwatch is now visible, hinting at the passage of time. The surrounding environment remains consistent with the previous frames, filled with dishwashing paraphernalia.

#### Sample 124 — After

- Similarity: 0.4761
- Prediction: In this frame, the ingredients have been added to the pasta, indicating that the pasta has been thoroughly stirred. The pasta is now in a more evenly distributed state, with the remaining ingredients still in the bowl. The ingredients are now evenly distributed across the surface of the pasta. The bowl appears to have been thoroughly incorporated into the pasta's surface, implying that there has been a significant amount of mixing.
- Reference: The wooden spoon appears once more in a different stage of use, its bowl now exhibiting clear signs of interaction with the food. Food residue clings to the inner surface, and the spoon is positioned at a near-vertical angle, indicating the completion of a scraping or gathering action. The handle of the spoon, consistent with the prior images, is held steadily, and the utensil is poised just above the plate, likely having just been lifted following contact with the food.

#### Sample 127 — After

- Similarity: 0.4708
- Prediction: In this frame, the cloth is held in a downward motion, indicating that the water has been drained out. The hand's grip is still firm, suggesting that the cloth has been thoroughly rinsled. The cloth's surface appears to be squeaking, with the fingers pointing toward the edge of the cloth, implying that it has been washed.
- Reference: In this final frame, the tap is completely turned off, as evidenced by the absence of water flow. The handle is now positioned parallel to the sink's surface, in alignment with the faucet's design, indicating the closure of the valve. The stillness of the water surface confirms that the tap has been shut off, and the lack of water motion allows for a clearer reflection of the surrounding area on the wet basin surface.

#### Sample 147 — After

- Similarity: 0.4824
- Prediction: In this frame, the hand is engaged in the action of removing the lid from the pan, indicating that the pot has been removed from the burner. The kitchen remains unoccupied, with no visible signs of activity, and the kitchen's contents are still present. The blender remains in the same state as the previous frame, but there is no indication that the lid has been placed on the pan.
- Reference: The environment around the mixer now appears more blurred, suggesting rapid movement or a swift action taking place. The mixer, while still recognizable, seems to be in the midst of a quick rotation or shift, likely guided by the user's hand. The lid on the mixer is firmly in place, ensuring the contents inside remain secure despite the rapid movement.

#### Sample 150 — After

- Similarity: 0.4777
- Prediction: In this frame, the hand has stepped into the position of the kettle, implying that it is now in its final position. The hand's position remains unchanged, suggesting that the kettle has been placed in a position where it is not yet ready to be used. The bottle is still in its original position, but the hand is now engaged in the action of removing it from the position it was in before.
- Reference: The hand is now in direct contact with the spice, suggesting that the spice has been actively selected and is being removed from its original position. The other surrounding items have become secondary as the primary interaction is between the hand and the spice. The gesture of the hand indicates a firm grip, and it's evident that the spice will be used or inspected, taking it out of its passive state in the cupboard.

#### Sample 153 — After

- Similarity: 0.2923
- Prediction: In this frame, the counter appears to have been thoroughly cleaned, indicating that it has been thoroughly sanitized. The surface of the counter is still damp, suggesting that there is still a lot of work to be done. The person's hand appears to be holding a cloth or paper towel, implying that he or she has been cleaning the counter for a long period of time.
- Reference: The scene has evolved into one where the pepper mill is being maneuvered with intention, as indicated by the hand's confident grip and the blurred motion of the mill and the hand together. This motion blur indicates a swift, directed movement, likely an action to place the pepper mill back into its rightful position or to continue with its intended use. The hand's position at the top of the mill suggests a more stabilized and deliberate control, contrasting with the previous frames.

#### Sample 158 — After

- Similarity: 0.3625
- Prediction: In this frame, the banana appears to have been removed from its packaging, indicating that it is no longer in its original state. The position of the banana remains the same, and the surrounding area remains unchanged. The banana's contents are still present, but there is a slight change in its position, suggesting that it may have been placed in a different position.
- Reference: The orange has travelled further from its original position. It's almost at the edge of the table, with increased motion blur indicating its consistent movement. The reflection of the light source on the orange's skin has shifted towards the opposite side, now highlighting different surface imperfections and presenting a dynamic change in its overall visual perception.

#### Sample 161 — After

- Similarity: 0.3992
- Prediction: In this frame, the strainer has been removed from the container, indicating that the contents of the container have been thoroughly emptied. The strainer is now in a more streamlined state, and the contents are no longer visible, implying that there is still a significant amount of residue left on the bottom of the bowl.
- Reference: The third frame is again similar to the previous two, with no significant alterations in the scene. The hands in yellow gloves remain inside the drum, and the position of the person appears unchanged. The lighting still accentuates the bin's rim, and the lack of visible contents inside the drum suggests that the task at hand may involve removing items, although no items are seen being extracted at this moment.

#### Sample 162 — After

- Similarity: 0.3938
- Prediction: In this frame, the utensil has been moved away from its original position, indicating that it is now in the hands of a new person. The hand's grip remains firm, and the knife's edge is still visible, suggesting that the knife may have been moved. The kitchen sink is now positioned in the same position as the kitchen sink, and there is a slight movement in the direction of the knife, implying that the hand is now engaged in the process of removing it.
- Reference: The measuring jug is now being held aloft, providing a clearer view of its design and scale. The white measurement markings are visible, suggesting that the jug can measure significant volumes, suitable for a variety of kitchen tasks. The action of lifting the jug implies that it has been selected for use, and the person’s task progression is evident as the hand grips it firmly, ready to measure ingredients. The surrounding environment remains a backdrop of kitchenware and utensils, unchanged from the previous activities.

#### Sample 170 — After

- Similarity: 0.4106
- Prediction: In this frame, the hand is engaged in the action of slicing the garlic. The hand's fingers are still present, suggesting that the garlic has been thoroughly incorporated into the dish. The garlic's consistency is more consistent, indicating that the salt has been added to the brining brine. The salt's surface is still slightly damp, suggesting a slight movement in the direction of the garlic, which may indicate a change in the course of the process.
- Reference: In this frame, the hand and the shaker are no longer directly over the tomatoes, indicating the conclusion of the seasoning process. The focus has shifted, and the spice shaker is now oriented towards a different part of the kitchen counter. The tomatoes rest undisturbed on the plate, their seasoned surface untouched since the last action. The background contains elements such as a knife, an empty plate, and packaged food items, suggesting that the preparation of a meal is underway, with the seasoning of the tomatoes being one of the steps in the culinary process.

#### Sample 174 — After

- Similarity: 0.4523
- Prediction: In this frame, the colander has been removed from the pot, revealing a more streamlined appearance. The colander's surface appears to be a bit looser, indicating that it has been placed on the counter, rather than being placed on top of the rice cooker. The kitchen sink appears to have been removed, suggesting that there is still a large amount of rice to be added to it. The rice cooker's interior is now cluttered with a variety of items, such as utensils, napkins, and other household items.
- Reference: In this frame, the colander is now positioned over the sink, as if the person is preparing to drain excess water or give the beans another rinse. The beans are settled at the bottom, still wet and shimmering under the light. The person's other hand is visible, wearing a yellow glove, possibly to protect against hot water or to keep hands clean. Below the colander, the shiny sink basin reflects the beans' colors, and the overall atmosphere suggests a diligent and thorough cooking process.

#### Sample 187 — After

- Similarity: 0.4360
- Prediction: In this frame, the hand appears to be in the hands of a person who has just finished cleaning the kitchen sink. The hand is still motionless, indicating that the water has been drained from the sink, and the hand is now in motion. The camera's focus shifts to the palm of the hand, suggesting that the hand has been removed from the water source.
- Reference: The chicken now seems to be momentarily set aside, as the individual has completed the hand washing and is drying their hands with what appears to be a yellow kitchen cloth. The chicken remains on the cutting board as in the first frame, with no additional preparation evident. This suggests that the process of cutting the chicken has been momentarily halted while the person attends to personal cleanliness, maintaining good kitchen hygiene practices.

#### Sample 193 — After

- Similarity: 0.4792
- Prediction: In this frame, the chef's knife has been removed from the cutting board. The knife's position remains unchanged, indicating that the knife is still in the process of cutting the onion. The slices of onion remain in the same position as before, but they are now positioned in a slightly different position. The kitchen's focus is now on the preparation of the next slice of the vegetable, which is likely to be ready in the next few minutes.
- Reference: The knife is seen completing a cut, with a piece of tofu having just been severed, demonstrating the ease with which the knife glides through the soft material. The tofu pieces that have been cut are notably uniform in size, suggesting a meticulous approach to cutting for even cooking. One can see that the tofu is still uncooked, maintaining its raw texture and color, as it awaits the heat of the wok to transform its flavor and texture.

#### Sample 197 — After

- Similarity: 0.4051
- Prediction: In this frame, the paper has been placed in a new position, indicating that it has been removed from its original position. The position of the paper remains the same, suggesting that the paper is now positioned in the same position as the previous frame. The paper's position is now more consistent with the current position, suggesting a shift in the direction of the action.
- Reference: In this frame, the action of cleaning has progressed. The paper towel, more crumpled and possibly saturated, is placed further along the counter, suggesting the area initially wiped is now cleaner. The pot on the stove is now accompanied by a pot of yellow substance, likely a starch-based food, perhaps pasta or rice. The position of the kitchen tools has not changed, and the shadow of the person suggests they are leaning over the counter to ensure a thorough clean. The overall state of the kitchen remains busy with cooking and cleaning happening simultaneously.

#### Sample 211 — After

- Similarity: 0.4660
- Prediction: In this frame, the cloth is more wavy, suggesting that it has been rinsing or washed. The person's hand appears to be holding the cloth in one hand, indicating that the cloth has been thoroughly rinsed.
- Reference: In this view, the sink appears to be in the final stages of being wiped down. The person's clasped hands convey a sense of completion or a pause in the activity. The stainless steel surface of the sink is now visibly wetter than in the previous frames, with water covering a greater area of the basin and reflecting light, suggesting a more thorough cleaning has taken place. The counter has been cleared of the carrot peel seen earlier, and the rag previously held in the person's hand is no longer visible, possibly set aside after finishing the wiping.

#### Sample 220 — After

- Similarity: 0.4362
- Prediction: In this frame, the fingernails are still held in the hands of the person who's been rinsing them, indicating that they've been thoroughly rinsed. The hand's grip is still firm, suggesting that it's time for the next step in the process.
- Reference: In this frame, the cucumber is still under the faucet, but now it's angled differently, allowing the water to wash over another side of it. The hand has shifted position, cradling the cucumber more towards its end, which could indicate a rotation for an even wash. The other hand, previously holding a knife, is now absent from the scene, possibly set aside to facilitate better handling of the vegetable during the washing process.

#### Sample 223 — After

- Similarity: 0.4109
- Prediction: In this frame, the lid has been removed from the jar, revealing a portion of the contents inside. The lid is now in a more upright position, indicating that the contents have been removed. The person's grip on the lid remains firm, suggesting that the lid is still firmly in place.
- Reference: The can is now more extensively opened. A greater portion of the aluminum lid has been pulled back, revealing the moist, chunky content of the tuna inside. The texture of the tuna is uneven, suggesting it may be in chunks or flakes. One can deduce from the partial view that it's possibly preserved in some form of liquid, possibly oil or brine, as it glistens slightly.

#### Sample 225 — After

- Similarity: 0.4466
- Prediction: In this frame, the hand blender remains in the same position as before, indicating that the blender has been removed from the user's workspace. The hand blender's grip remains unchanged, suggesting that the user is still holding the blender in place. The mixture appears to be blending smoothly, with no noticeable changes in the settings.
- Reference: The mixture has reached a homogenously creamy state with a uniform yellow coloration and a smooth, glossy finish, consistent with a well-blended batter. The surface is free of any lumps or unincorporated patches, and the mixture now holds a ribbon-like trail from the beaters, which indicates good viscosity and structure. The overall volume appears to have increased, and the mixture maintains its shape around the beaters, demonstrating that sufficient air has been incorporated to give it a light, airy texture.

#### Sample 226 — After

- Similarity: 0.4923
- Prediction: In this frame, the hand is engaged in the action of removing the plastic bag from the kitchen counter. The hand's hands are still present, indicating that the bag has been removed from its packaging. The packaging's shape remains the same, suggesting that it may have been placed in a freezer or refrigerator.
- Reference: The scissors are now absent, and the wrap has been cut, with the roll repositioned closer to the center of the counter. The cut edge of the wrap is not visible, suggesting that it has been neatly trimmed and possibly adhered to a dish or discarded. The layout of the kitchen counter shows a shift in focus towards other cooking activities, such as the microwave oven now entering the frame, hinting at the next steps in meal preparation. The wrap's previous tension is gone, indicating the cutting action is complete.

#### Sample 234 — After

- Similarity: 0.4423
- Prediction: In this frame, the mat has been moved to a new position, indicating that it is no longer in the position of its predecessor. The mat's position is now blurred, suggesting that the mat is now in a different position. The camera's focus remains on the mat, which appears to be positioned in the same position as the previous frame.
- Reference: The transformation of the mat is nearly complete. It presents itself with a sharp fold down the middle, the two halves nearly symmetrical, a sign of a deliberate and practiced movement. The orange tone of the mat now seems richer, the texture more evident as the lighting casts shadows within the folds, providing depth to the previously flat object. The mat's new shape is compact, hinting at the finality of the action, with just a corner lifted, poised for the last step in its folding sequence.

#### Sample 235 — After

- Similarity: 0.3746
- Prediction: In this frame, the thermometer remains in the same position as the previous frame, indicating that it has been removed from its original position. The kitchen counter is now positioned in a slightly different position, suggesting that the hand has moved away from the kitchen counter. The counter's position remains the same, and there is no discernible movement between the counter and the counter, implying that the timer has been moved.
- Reference: Here, the grater has been repositioned further to the right, and its orientation has changed such that the top, where the handle is affixed, is now closest to the camera. The grater's shredding surface is now partly obscured by the handle from this angle, and the background clutter seems unchanged. This shift in position makes the grater more prominent in the frame and suggests an active engagement with it, possibly in preparation for use.

#### Sample 238 — After

- Similarity: 0.4591
- Prediction: In this frame, the sugar container has been removed from the kitchen counter, indicating that the sugar has been poured into the container. The hand's grip on the container is still present, suggesting that the spoon has been used to pour the sugar into it. The spoon's position is still visible, with the palm of the hand resting on the side of the container, implying that it is now in the process of pouring the sugar.
- Reference: The pouring action has reached its peak, with the flour leaving the jar in a fuller, more rapid stream. The pile of flour in the bowl has risen significantly, nearly doubling in size from the initial pour, and the top of the mound has a smooth, undisturbed surface. The cloud of flour dust has dissipated slightly, suggesting a slowing of the pouring action. There's a slight over-pour on the rim of the bowl, indicative of the speed and volume of the flour being transferred.

#### Sample 241 — After

- Similarity: 0.4009
- Prediction: In this frame, there is a noticeable increase in the number of slices of bread, indicating that the bread has been removed from the plate. The bread remains in the same state as before, suggesting that it has been placed on the plate or placed in a bowl.
- Reference: The ladle has been set down onto the white paper plate, with the bowl of the ladle now resting on the plate's surface. The handle extends towards the top left of the frame, crossing over the edge of the plate. The scene is largely unchanged apart from the ladle's movement; the table still holds the same items, and the glass remains untouched, with the liquid level consistent with the previous frames.

#### Sample 245 — After

- Similarity: 0.4487
- Prediction: In this frame, the ingredients have been incorporated into a new dish. The mixing bowl appears to have been removed from the plate, indicating that the ingredients are still in the bowl. The color of the bowl is now more vibrant, suggesting that it may be time to add more ingredients to the recipe.
- Reference: Here, the whisking has progressed further. The fork is actively churning through the egg mixture, creating a more homogeneous yellow color as the yolks and whites combine more thoroughly. The motion of the fork is more evident, indicated by the trails and ripples in the mixture. There are fewer clear whites visible, and the yolks are no longer distinct entities, signifying a deliberate and continued mixing effort to achieve a consistent blend for cooking.

#### Sample 248 — After

- Similarity: 0.4762
- Prediction: In this frame, the hand is engaged in the action of pressing the button, indicating that the device has been turned on. The hand's position is still the same, suggesting that the button has been pressed, and the button is still in motion.
- Reference: The light switch now shows one button fully depressed, indicating that the switch has been activated. The lighting condition, however, does not show a noticeable change from the previous frames. This could mean that the light has yet to turn on, the bulb is non-functional, or the change in lighting is too subtle to be captured by the camera. The hand remains in contact with the switch, and the shadow on the wall is consistent with the previous lighting condition.

#### Sample 252 — After

- Similarity: 0.4506
- Prediction: In this frame, the knife has been inserted into the center of the sandwich. The knife's edge is still visible, indicating that the sandwich has been successfully removed from the plate. The sandwich's exterior remains unchanged, suggesting that the knife was used to slice the sandwich, preserving its shape and texture.
- Reference: Here, the cake's integrity is further reduced by the removal of an additional slice. This action has created a larger gap in the ring, with two segments now missing. The texture of the cake is consistent with the previous images, and it continues to sit on the same decorative doily. The absence of the slices highlights the consistent golden-brown color of the cake's crust and the moistness of the interior, as inferred from the newly exposed edges.

#### Sample 253 — After

- Similarity: 0.2509
- Prediction: In this frame, the sprinkling pan is in a slightly different state, indicating that the water has been drained out of the pan. The pan's surface is still wet, but the water's movement is still visible, suggesting that the pan has been thoroughly rinsed.
- Reference: The rag here has a slightly different posture, being maneuvered possibly to a different angle or direction. The grip on the rag seems firm, and its dampness is consistent with the previous frames. Some portions of the rag look more pressed down, likely from the cleaning motion and the force applied by the hand.

#### Sample 256 — After

- Similarity: 0.4227
- Prediction: In this frame, the stovetop remains in the same position as the previous frame, indicating that the burner has been removed from the burner. The kitchen remains unchanged, with the stove's burner still visible, and the kitchen's kitchen sink still in place, suggesting that the stove has been turned on. The stove remains unbroken, and there is no indication of the person's presence, implying that he or she is engaged in any activity.
- Reference: The progression of interaction is evident as the hand has now grasped the grill grate, with fingers curled securely around one of the bars. The grate is slightly lifted, suggesting the initial stage of removal. The rest of the grill remains static, its cleanliness and the unaltered positions of the other grates indicating that this is perhaps the first grate being manipulated. The surrounding area, including a countertop and various kitchen items, remains undisturbed by the action taking place.

#### Sample 258 — After

- Similarity: 0.4568
- Prediction: In this frame, the can opener has been fully re-emerging from its original position, indicating that the contents of the can have been removed. The person's hands are now engaged in the process of removing the can, implying that there is still a significant amount of residue left on the can's surface. The man's fingers appear to be holding the can in place, suggesting that there may be some residue left behind.
- Reference: In this frame, the dish has been turned to expose a different angle to the viewer, revealing that the previously seen residues are now substantially reduced. The upper surface is now the primary focus, gleaming with moisture and displaying streaks of water that reflect the overhead lighting, indicating a recent rinse. The surrounding area of the sink is splashed with water, and the dish appears to be in the final stages of being cleaned, with only minor remnants of residue left.

#### Sample 260 — After

- Similarity: 0.4533
- Prediction: In this frame, there is a clearer view of the kitchen counter, which is now cluttered with a variety of items, including a bowl, a pot, and a dish towel. The kitchen counter remains in a state of disrepair, and the surface of the counter appears to be a bit more cluttered.
- Reference: The final frame offers a perspective where the detergent has been further dispersed across the countertop. The once localized wetness now has a more spread-out appearance, showcasing a wider affected area. The hand in the image is actively holding a cloth, potentially in the process of cleaning or spreading the detergent further. The scene gives the impression of the cleaning process being in full swing, with a significant part of the countertop being addressed.

#### Sample 263 — After

- Similarity: 0.4123
- Prediction: In this frame, the hand is engaged in the action of putting the mug in the microwave, indicating that the microwave has been turned on. The hand remains stationary, and there is no indication of the person's presence, implying that he or she is using the microwave.
- Reference: The mixer reappears in the frame, still in an inverted position with its handle pointing upwards, resting against a container possibly used for mixing ingredients. The blue motor housing is prominent, and the electrical cord is loosely draped over the container, indicating a temporary placement, perhaps as the user prepares to clean the device or retrieve something else. The state of the kitchen remains unchanged from the first frame, with the spill still on the floor and the countertops cluttered.

#### Sample 265 — After

- Similarity: 0.2789
- Prediction: In this frame, the cheese has been fully removed from its packaging, revealing a new layer of the cheese. The hands are now able to grasp the cheese's core, which is now firmly encircling the top of the sandwich. The cheese has now been fully incorporated into the sandwich's surface, allowing it to be more easily accessed.
- Reference: The coffee bag now exhibits a more pronounced opening, with the top separated enough to reveal the inner seal and possibly some of the coffee product inside. The person's hands have adjusted their grip, indicating the opening process is nearly complete. One can infer that the aroma of the coffee may be starting to permeate the area, as opening the bag this much would release the scent. The bag maintains its central placement on the cutting board, even as it transitions from sealed to unsealed.

#### Sample 267 — After

- Similarity: 0.4034
- Prediction: In this frame, the jar has been tilted downwards, indicating that the lid has been removed from the pan. The jar is now in a more upright position, with the lid still firmly in place. The person's grip on the lid remains firm, suggesting that the contents of the can have been removed.
- Reference: Progress in the sweetcorn's reveal is evident as the can opener has now traversed a significant portion of the can's circumference. The lid is partially detached, with a noticeable gap indicating the path the opener has taken. Corn kernels are now visible, peeking through this gap, their yellow hue contrasting with the metallic sheen of the can's interior. The user's hands are actively engaged in the process, suggesting that the opening sequence is close to completion, and the sweetcorn will soon be fully accessible.

#### Sample 269 — After

- Similarity: 0.4330
- Prediction: In this frame, the chopping board has been moved to a new position, with the knife still in the middle of the cutting board. The knife's blade is now positioned in the same position as the previous one, and the knife is now in the process of slicing the stems. The pieces of coiled stems are now arranged in a more uniform pattern, indicating that they have been thoroughly chopped. The leaves appear to have been sliced into smaller pieces, revealing a larger portion of the stalks.
- Reference: By this stage, the choi pak has been extensively chopped, with nearly all of it being transformed into bite-sized pieces. The cutting board is more cluttered, with pieces of the vegetable spread out, revealing both the lush green of the leaves and the crisp white of the stems. The bowl is almost filled to the brim with choi pak, showcasing the quantity that has been prepared.

#### Sample 271 — After

- Similarity: 0.4306
- Prediction: In this frame, the spray bottle has been dipped in the water, indicating that it has been fully dispensed. The bottle's position is now more pronounced, suggesting that the liquid has been applied to the bottle. The hand's grip on the bottle is still firm, suggesting the action of the sprayer.
- Reference: The action of squeezing has resulted in a substantial amount of washing up liquid pooled at the base of the bowl, with the stream now thicker and more copious. The surface of the liquid pool is uneven, with ripples and bubbles indicating recent disturbance. Some liquid has started to spread out from the initial point of contact, with tendrils of green stretching outwards, showing the beginning stages of dispersion through the water present in the bowl.

#### Sample 279 — After

- Similarity: 0.3535
- Prediction: In this frame, the hand is engaged in the motion of the scale, indicating that it has been placed on the counter. The scale remains in the same position as before, suggesting that it is still in the position of its predecessor. The contrast between the hand and the scale remains blurred, with the focus shifting to the side of the kitchen counter, implying that the scale has been removed from the countertop.
- Reference: The cabinet door is now almost completely closed, with only a small gap remaining. The motion blur has decreased, implying that the speed of the closing action has reduced as the door nears its fully closed position. The contents of the cabinet are no longer visible due to the narrow opening, and the door is nearly flush with the cabinet frame, indicating that the action of closing the cabinet is almost complete.

#### Sample 280 — After

- Similarity: 0.3299
- Prediction: In this frame, the utensil has been moved away from its original position, indicating that the hand is still motion-free. The hand's movements are more pronounced, suggesting a more gradual movement in the direction of the hand or the hand itself.
- Reference: The scene remains a whirl of colors and shapes due to motion blur, with the toaster even less discernible than before. It's apparent that the camera or the person is moving quickly, creating an almost abstract composition of kitchen elements. The blur conveys a sense of urgency or haste. The toaster, while present in the scene, has become an element of the background, overshadowed by the blur of motion that dominates the frame.

#### Sample 282 — After

- Similarity: 0.4414
- Prediction: In this frame, the garlic cloves have been progressively removed from the skins, revealing a more pronounced and slouchy appearance. The cloves are now more exposed to the light, indicating that they've been thoroughly cleaned. The garlic's skins are still a little damp, but they're still able to retain some of their moisture. The skin's surface is still slightly damp, suggesting that it's time to remove the cloves.
- Reference: Here, the fingers hold the onion firmly, peeling back an additional layer. The onion skin, while not the focus, has shifted again, likely due to the movements of the hands and the objects on the board. It is now partially covered by the person’s hand, and the action suggests a continuation of the peeling process. The skin's texture seems drier, and it's beginning to resemble more of a shell discarded during the culinary preparation.

#### Sample 287 — After

- Similarity: 0.4496
- Prediction: In this frame, the potatoes have started to turn golden brown, indicating that they've been fully cooked. The edges of the potatoes are still slightly exposed, suggesting that they may have begun to turn their color. The potatoes are now a darker shade of brown, with a slight hint of browning. They've also started to show signs of being cooked longer.
- Reference: The wooden spatula continues its stirring motion, ensuring the even cooking of the potato slices. The slices appear slightly softer in texture, with some edges showing a bit more curl, indicating they're cooking and possibly getting crispier. The glossy coating of seasoning or marinade persists, suggesting that it's locking in the flavors while the potatoes cook. The overall arrangement is more uniform, indicating the continuous effort to ensure every slice is cooked thoroughly.

#### Sample 289 — After

- Similarity: 0.4244
- Prediction: In this frame, the rinsing of the jar appears to have been completed, with the water still flowing from the bottom of the glass. The water is now dripping into the glass, resulting in a clearer, more filtered stream of water.
- Reference: The tupperware now appears to be in the final stages of rinsing, with the water flowing smoothly over its edges, indicating the absence of soap suds. The positioning of the container under the tap is more tilted, likely directing the water flow to rinse off the last remaining droplets and soap traces. The handgrip has shifted, with the fingers now closer together, possibly signaling a gentler handling as the task nears completion.

#### Sample 295 — After

- Similarity: 0.4710
- Prediction: In this frame, the dish is still rinsing, with the water still displacing some of the soap suds, indicating that the dish has been washed. The person's hand appears to be holding the dish in one hand, implying that it has been rinsed, and the bowl is now in the hands of a professional. The surface of the plate is still wet, with a few drops of soap on the surface, suggesting that the solution has been thoroughly rinsed.
- Reference: The cleaning process seems to have progressed, as the strainer is now being wiped from the inside out with a white cloth that is likely absorbing moisture and dislodging any remaining particles. The sponge has been set aside, indicating that the scrubbing action has been completed. The water flow has resumed, suggesting a final rinse. The interior of the strainer looks significantly cleaner, with fewer visible food particles, and the white plastic appears to have regained some of its original brightness.

#### Sample 297 — After

- Similarity: 0.4054
- Prediction: In this frame, the chicken has been placed in the hands of the person who is preparing to eat it. The chicken remains in the same position as the previous frame, but the hands are now engaged in the process of removing it from the kitchen. The hand's grip on the chicken remains firm, indicating that the chicken is ready to be handled.
- Reference: The board is now tilted at a steeper angle towards the pan, and the garlic paste has been mostly scraped off, leaving only a slight residue on the surface. The person's grip on the knife has changed to a more precise and firm hold, focusing on ensuring that all of the garlic is removed from the board. The hand holding the board has adjusted its position to facilitate the transfer of the garlic into the pan, and the fingers are curled to avoid contact with the knife or the hot surface of the pan.

#### Sample 298 — After

- Similarity: 0.2891
- Prediction: In this frame, the utensil rack appears to have been removed, indicating that the pan has been removed from the kitchen. The kitchen sink appears to be in the same position as the sink, suggesting that the sink has been placed in a different position. The sink's surface is now slightly tilted away from the counter, implying that it has been wiped with a cloth or paper towel.
- Reference: The gloves in this frame are presented in a state of action. The left hand, clad in the yellow rubber glove, is actively engaged in holding a dark frying pan, while the right hand appears to be reaching towards or withdrawing from an interaction with the pan or another object just outside the frame. The gloves are more stretched across the palms and fingers compared to the previous frames, indicating a firmer grip and a dynamic movement.

#### Sample 303 — After

- Similarity: 0.4513
- Prediction: In this frame, the cap has been completely removed from the bottle, indicating that the cap is no longer in its original state. The hand's grip remains firm, suggesting that the bottle is still in its proper position. The bottle's contents are clearly visible, and the cap appears to have been fully withdrawn from its original position.
- Reference: The scene portrays the can in a more pronounced tilted angle, suggesting an active pour. The fluid is visible midway, cascading into the already partially filled glass. The glass captures the liquid's effervescence, with bubbles hinting at the carbonated nature of the drink. The person's grip has adjusted to facilitate the pour, and the wrist's metallic accessory shines under the ambient light.

#### Sample 304 — After

- Similarity: 0.2029
- Prediction: In this frame, there is a noticeable movement in the direction of the sink, indicating that the sink has been agitated. The sink's surface is blurred, suggesting that it may be clogged or soiled. The camera's focus is more on the sink than the sink itself, implying that it's not necessarily a sink, but rather a kitchen sink or a bathroom sink.
- Reference: The transformation of the tin reaches a new phase as it now holds a quantity of water, with its surface partially submerged. The water reflects the kitchen's ambient light and surroundings, introducing a glossy sheen that contrasts sharply with the matte and tarnished finish of the tin's unwetted interior surfaces. The water's presence introduces a visual softening of the tin's hardened deposits, implying a preliminary step in a cleansing process.

#### Sample 306 — After

- Similarity: 0.4327
- Prediction: In this frame, the knife is held in a circular motion, indicating that it has been rinsing or washed. The person's hand is holding the knife in the same position as the previous one, and the knife's surface is still wet, suggesting that the blade may have been soiled.
- Reference: The rolling pin now rests on the edge of the sink, with attention focused on cleansing a white plate. The pin is no longer the central object of cleaning but remains in the scene, possibly awaiting a final rinse or to dry. The soapy water on the pin has formed small puddles on the stainless steel sink, separating the cleaning zones between the plate and the pin. The pin's handles protrude outward, suggesting that it might be picked up again soon.

#### Sample 309 — After

- Similarity: 0.3422
- Prediction: In this frame, the fingernails have been removed from the potato, indicating that the water has been drained from the inside of the potato. The hand's grip is still firm, suggesting that the potato has been thoroughly washed. The water's droplets appear to be absorbed into the potato's surface, implying that it has been rinsed.
- Reference: The tap continues to be in its downward position over the sink. Water is gushing out from the spout with a higher intensity compared to the previous frame. The flow is forceful, resulting in more water splashes within the sink. The clarity and consistent nature of the water suggest it's likely at a cold temperature.

#### Sample 310 — After

- Similarity: 0.4872
- Prediction: In this frame, the cake has been placed in a new position, indicating that it has been removed from the pan. The surface of the cake appears to have been wiped with a damp cloth, suggesting that the cake is still in its original state. The cake's shape remains the same, with the center of the parchment paper and the edges of the baking sheet still visible.
- Reference: The tray in this image is consistent with the previous frames, with no significant changes to its condition. The three dough balls remain in the same positions, and there are no additional markings or changes to the surface of the tray that would suggest any interaction. The consistency of the tray's appearance across the frames reinforces the static nature of the scene, with the dough remaining in an undisturbed state, likely resting and undergoing proofing.

#### Sample 316 — After

- Similarity: 0.4773
- Prediction: In this frame, the hand has moved closer to the plate, indicating that it has been removed from the kitchen. The hand's position is still consistent with the previous frame, suggesting that the plate has been placed on the counter or in a drawer. The thumb and index finger appear to be pointing at the plate's edge, suggesting a slight change in the position of the hand.
- Reference: The scene on the hob is largely consistent with the previous moments, with the front-right burner staying lit and active. The frying pan and its contents remain the focus of the cooking process, with the hand and utensil now positioned as if the food has just been stirred or turned. The surrounding area is static, with the other burners untouched and the spice jars nearby, reinforcing the singular concentration on the dish at hand. The hob's surface reflects the common wear of cooking, with no additional elements introduced into the scene.

#### Sample 320 — After

- Similarity: 0.4054
- Prediction: In this frame, the cheese has been fully removed from the skin, revealing a more smoky, charred appearance. The knife's grip is still firm, suggesting that the meat has been thoroughly removed from its skin. The cheese's texture is more pronounced, indicating that it's ready to be sliced or grilled.
- Reference: The sweet potato skin here is mostly separated, with only a small portion still attached at the end of the vegetable. The accumulation of peelings on the cutting board has grown, and some peel segments have escaped onto the counter, showing the progression of the peeling task. The skin's moisture has begun to dull as exposure to the air has set in, and there is a noticeable decrease in the vibrancy of the orange color. The knife and fork are now lying on the cutting board, indicating a pause or the completion of peeling.

#### Sample 329 — After

- Similarity: 0.4680
- Prediction: In this frame, the hand is engaged in the action of removing the lid from the coffee machine, indicating that the machine has been removed from the kitchen counter. The coffee machine remains in the same state as before, but there is a slight change in the position of the hand, suggesting that the hand may have stepped into the machine.
- Reference: The bag is significantly more open in this frame, with a substantial portion of its contents now visible. The hand is holding onto the bread, indicating an intention to possibly take it out or examine it. The surrounding items remain in place, emphasizing the main action taking place with the bag and its contents. The transparency of the bag offers a clear view of the bread inside, revealing its shape, size, and texture.

#### Sample 335 — After

- Similarity: 0.2815
- Prediction: In this frame, the mat has been repositioned, indicating that it has been removed from its original position. The mat's position remains unchanged, and the surface of the mat is now positioned in a slightly different position, suggesting that it is now being used as a mat.
- Reference: In this frame, the degreaser's presence is evidenced by a layer of liquid across the surface, with a significant reduction in airborne droplets. The hand and bottle are now absent, indicating that the spraying action has ceased. The surface of the countertop shows a consistent wet sheen, highlighting the even distribution of the degreaser. The wet area has expanded further, showing the progression of the liquid as it moves outward from the point of initial contact. The pattern of the countertop is slightly obscured by the sheen of the degreaser, displaying the product's coverage.

#### Sample 338 — After

- Similarity: 0.2580
- Prediction: In this frame, the pan has been removed from the burner, indicating that it has been placed on the stove. The pan's surface remains unchanged, suggesting that the pan is still in the oven. The skillet appears to have been placed in a pre-heated position, implying that the heat has reached the pan.
- Reference: The extractor fan remains in the same state as before, maintaining its heavily used appearance with a stubborn layer of grime. The lack of light reflection on its surface reinforces the idea that the fan is not operational, and there seems to be a consistent lack of maintenance, which is evidenced by the undisturbed grease deposits. The fan's surroundings, including the wall tiles and the stovetop, also show signs of use, correlating with the condition of the fan, suggesting a kitchen that is frequently used but not frequently cleaned.

#### Sample 341 — After

- Similarity: 0.4225
- Prediction: In this frame, the dish appears to have been rinsing again, with the water still lingering on the surface of the dish, indicating that the water has been thoroughly drained. The hand's movements suggest that the dish has been washed, and the water is now running smoothly.
- Reference: The tablecloth is now draped over the sink's divider, its apple design partially obscured by the curvature of the fabric as it conforms to the sink's shape. Water droplets are scattered across the surface, some merging to create larger rivulets that travel along the cloth's folds and undulations. The image conveys a sense of motion and fluidity, with the previous crispness of the apple design softened by the water's influence.

#### Sample 343 — After

- Similarity: 0.4491
- Prediction: In this frame, the knife is in the hands of a person who has just finished scrubbing the blade. The person's hand appears to be engaged in a more thorough cleaning, indicating that the blade has been thoroughly washed. The blade's surface is still wet, suggesting that it may have been soiled, and the blade may have had a thorough cleaning.
- Reference: The spoon is still held by the hand, but the position has slightly changed. The bowl of the spoon is more exposed, and it looks much cleaner with fewer water droplets than the previous frame. The yellow sponge is in closer contact with the spoon, implying an ongoing cleaning process. The spoon reflects more of its surroundings, suggesting a cleaner and shinier surface.

#### Sample 351 — After

- Similarity: 0.3815
- Prediction: In this frame, the cheese has been completely removed from the foil, revealing a new layer of the cheese. The cheese's surface remains intact, indicating that it has been thoroughly removed from its packaging. The hands are now engaged in the process of removing the cheese from the sandwich, demonstrating that the cheese is still there and ready to be sliced.
- Reference: In this frame, the action of capping the olive oil bottle has progressed further. The cap is now partially obscured by the hand, suggesting that it has been placed over the bottle's opening and is likely in contact with the bottle's rim. The person's hand is stretched towards the bottle, which remains out of view, and the downward pressure indicates that the cap is being twisted to secure it in place. The cap appears slightly tilted, a common occurrence when initiating the twisting motion to seal a screw-top bottle.

#### Sample 353 — After

- Similarity: 0.3356
- Prediction: In this frame, the operator is engaged in the process of removing the lid from the food processor, indicating that he or she has left the machine. The food processor remains in the same state as before, and the contents of the bowl remain the same. The user's hand appears to be holding the control panel in place, suggesting that the device is still in use.
- Reference: The button now appears to be fully engaged, pressed down to its furthest extent. The change in elevation from its original position is apparent, with the finger firmly applying pressure. The shadow cast by the finger is now more pronounced and confined to a smaller area directly around the point of contact, indicating that the button is at its lowest position. The surface of the button that was once reflective is now mostly obscured by the finger, and the surrounding buttons remain static, undisturbed by the action of this single button being pressed.

#### Sample 356 — After

- Similarity: 0.3060
- Prediction: In this frame, the microwave oven has been moved away from the kitchen, indicating that the microwave is no longer in use. The kitchen's interior remains unchanged, with the kitchen sink and counter still visible, as well as the microwave's utensils. The absence of the microwave in this frame suggests that the kitchen is now occupied with cooking.
- Reference: At this point, the mixture shows further signs of cooking, with even less liquid visible. The green components now appear more thoroughly cooked, with a subdued green color and more pronounced softness. The reduced liquid has a glossier look, indicating that the flavors are concentrating and the oil is emulsifying with the water content to create a more cohesive sauce. The edges of the pan show small bits of the mixture, which could suggest some caramelization or simply remnants from stirring. The wooden spoon is now resting, which might indicate a momentary pause in stirring, perhaps to evaluate the state of the mixture.

#### Sample 359 — After

- Similarity: 0.4216
- Prediction: In this frame, the person's hand is positioned on the counter, indicating that he or she has started cleaning the sink. The sink's surface is still wet, but there is a slight movement in the direction of the sink, suggesting that the person is engaged in some sort of cleaning activity. The water level in the sink is still low, and there is no indication of a significant amount of water being drained from the basin.
- Reference: In this frame, the bin remains in the same location, but the person's hand is now retracting from the area, implying that an item may have been deposited into it. The fill level of the bin appears consistent with the previous images, maintaining its overfilled state. The plastic liner bulges slightly outward, a sign of the bin's capacity being maximized. The environment around the bin, particularly the dish rack and the countertop, shows no noticeable change, reinforcing the ongoing use of the space for kitchen activities.

#### Sample 360 — After

- Similarity: 0.3721
- Prediction: In this frame, the lid has been removed from the container, indicating that the container is no longer in its original state. The person's hand is still holding the lid, suggesting that the lid may have been removed.
- Reference: The fridge door now appears almost completely closed. The black interior is scarcely visible, and the door handle is nearing its resting position. The LED indicators are still on, but due to the door's position, they are more prominently visible. The reflections on the fridge surface have shifted again, hinting at the continuous motion during the closing process.

#### Sample 363 — After

- Similarity: 0.3868
- Prediction: In this frame, the kitchen sink appears to be in a state of slow motion, indicating that the sink has not been fully emptied. The kitchen sink's interior is still blurred, suggesting that there is a slight movement in the direction of the sink, possibly due to a sudden change in the position of the blades. The surrounding area seems to be cluttered, with a few items scattered around the sink.
- Reference: The perspective is similar to the second frame, with the locker still open and the contents unchanged. The blurriness continues, indicating ongoing motion, either of the locker door or the camera. Kitchenware is partially visible on the top shelf, and the door's position seems consistent with the previous frames, suggesting that it has been open throughout and that no significant interaction with the locker has occurred between the frames.

#### Sample 364 — After

- Similarity: 0.1649
- Prediction: In this frame, the toaster's handle is positioned in the same position as the previous frame, indicating that the hand has been removed from the kitchen counter. The hand's position is consistent with that of the earlier frame, suggesting that it has been placed in the kitchen or in a drawer. The kitchen sink appears to be positioned near the stove, and the sink's faucet appears to have been turned on. The stainless-steel surface of the kitchen sink is reminiscent of a kitchen sink, with a sprinkling of utensils and other household items
- Reference: Now, the sweet potato takes on a distinctly different form. It appears to be cooked or baked, with its exterior taking on a wrinkled, slightly crispy texture. The rich orange hue of its interior has deepened, becoming more caramelized and glossy. Steam rises gently from the potato, indicating its warmth, and the flesh seems to have softened further, suggesting it would easily yield to the slightest pressure from a fork.

#### Sample 365 — After

- Similarity: 0.4228
- Prediction: In this frame, the cleaning solution on the burners appears to have been removed, indicating that the cleaning action has taken place. The surface of the burner is still clean, with no visible streaks or streaks, as well as the overall appearance of the stove's surface. The hand's hand appears to be focusing on the stovetop, suggesting that it has been cleaned.
- Reference: The hob surface now appears much cleaner than in the previous frames. The creamy substance is noticeably diminished, and while there's still some sheen indicative of moisture, it's less pronounced. The cleaning action with the blue cloth seems to have been effective in removing the majority of the spill or residue. The surrounding area of the hob appears clearer, with fewer obstructions, hinting that the cleaning process is nearing completion.

#### Sample 367 — After

- Similarity: 0.4783
- Prediction: In this frame, the lid has been removed from the pot, indicating that the pot has been placed in a closed position. The cup's contents are still visible, but the lid appears to have been inserted into the pot's opening, implying that the liquid has been added to the pot. The glass's surface is slightly different from that of the previous frame, suggesting that the lid may have been removed.
- Reference: The cap is more discernible in this frame, offering a clearer view. It's positioned near some jars and containers, with its design and color more evident. The environment's lighting is slightly better, highlighting the cap's features. However, the surrounding objects continue to contribute to a sense of disarray in the frame.

#### Sample 368 — After

- Similarity: 0.3307
- Prediction: In this frame, the wrapper has been fully opened, revealing the contents of the package. The wrapper's surface appears to be more exposed, indicating that the contents have been incorporated into the wrap. The hands are now engaged in the process of removing the wrap from the container, implying that the wrap has been thoroughly removed.
- Reference: Here, the focus shifts slightly away from the preparation area, providing no direct view of the tomatoes. There's a clear indication that the cooking process is advancing with the presence of a knife and an empty plastic bag labeled with a reference to carrots, suggesting that the ingredients are being organized or prepped sequentially. The absence of the tomato can suggests that its contents have already been utilized in an earlier step, or are set aside, ready for the next stage of meal preparation.

#### Sample 371 — After

- Similarity: 0.2901
- Prediction: In this frame, the vegetables appear to be in the same state as before, indicating that they've been added to the dish. The greens are still slightly exposed, suggesting that there's still a lot of cooking going on. The overall feeling of the vegetables is more of a "cooking" action, implying that the vegetables have started to take on a more active role in the cooking process.
- Reference: The spatula is now out of the pan, held aloft, indicating the end of a stirring or flipping action. The utensil appears clean, with no visible food residue, which may suggest that the food did not stick to the surface during the stirring, or it could simply be due to the angle and the distance from the camera. The hand grips the handle closer to the body of the spatula, possibly for better control during the lifting motion.

#### Sample 379 — After

- Similarity: 0.3950
- Prediction: In this frame, the lid has been removed from the kitchen counter, indicating that the container has been placed in the kitchen. The lid remains in the same position as the previous frame, with the lid still positioned at the edge of the counter, suggesting that the lid may have been removed.
- Reference: The tray is now distinctly separated from the scales. It appears to be in mid-air, being actively lifted or removed. The angle of the tray is much steeper than before, and it is evident from the shadow beneath it that it is no longer in contact with the scale's surface. The tray's position suggests it's being held by someone, though the hand is barely visible.

#### Sample 384 — After

- Similarity: 0.4980
- Prediction: In this frame, there is a slight movement in the direction of the person's hand, indicating that he or she is preparing to eat. The camera's focus now shifts to the kitchen, suggesting that the person may be preparing food or preparing a meal.
- Reference: The jug is now outside the refrigerator, held by a person whose hand and lower arm are visible. The motion is more pronounced, with the background significantly more blurred due to the speed of the action. The milk's position in the person's hand has changed; it is now being transported to a new location, likely a countertop or table. The grip on the handle is tight, indicating that the milk is being moved quickly and with care to avoid spillage.

#### Sample 391 — After

- Similarity: 0.3973
- Prediction: In this frame, the kitchen sink appears to have been removed from the sink, and the sink's surface is now more exposed, indicating that the sink has been thoroughly cleaned. The sink is now in a downward-facing position, with the sink positioned in the middle of the sink. The kitchen sink is still in the same position as the sink in the previous frame, and there are no visible marks of water or debris on the sink surface, implying that it may have been clogged or soiled.
- Reference: The chopping board now appears to have even more water coverage, with nearly the entire surface gleaming with wetness. Puddles of water are more pronounced and seem to be joining together, giving the board a uniformly damp appearance. There are very few dry patches visible, and the entirety of the board has taken on the darker hue of blue seen in the wet sections from the previous frames.

#### Sample 397 — After

- Similarity: 0.4613
- Prediction: In this frame, the hand appears to be in a position where it's been a while since the last time you touched it. The hand's position is now blurred, suggesting that the hand is still in the position it was in before. The kitchen sink appears to have been moved, indicating that the kitchen sink has been removed. The camera's focus is now on the kitchen, with the kitchen counter and kitchen sink in the background. The menu appears to indicate that there's a variety of items on the table, including a pot, utensil, or other items. The
- Reference: In this frame, the salt container has been repositioned even more noticeably. It's apparent that there has been some interaction with it, potentially involving its use in the cooking process. However, the cap remains in its sealed position, suggesting that no salt has been dispensed during this specific moment captured in the frame. The nearby items and their arrangement further indicate continued progress in the kitchen activities.

#### Sample 403 — After

- Similarity: 0.3408
- Prediction: In this frame, there is a noticeable increase in the amount of cheese on the dough, indicating that the cheese has been thoroughly incorporated into the dough. The dough's surface is slightly uneven, suggesting that it may have been slicked or melted. The cheese's texture is more pronounced, with a slight tendency towards a smoother texture.
- Reference: In this frame, the onion seems to be part of a more elaborate culinary preparation. The slices are now combined with other ingredients on top of the bread or dough base. Specifically, there's an addition of what appears to be cheese or another dairy product intermingled with the onion slices. The layers suggest that the meal is being prepared with care, ensuring a blend of flavors. The presence of other ingredients along with the onion hints at a composite dish, possibly heading towards baking or cooking.

#### Sample 404 — After

- Similarity: 0.4996
- Prediction: In this frame, there is a noticeable increase in the number of pieces of lettuce, which are now scattered across the table, indicating that there has been a significant reduction in the amount of time it takes to peel the lettuce. The hands are more engaged in the task, suggesting that they are more likely to be focusing on a single piece of lettuce rather than a larger portion of the salad. The overall composition of the lettuce is more consistent with the previous frame, which suggests that the lettuce has been removed from the cutting board.
- Reference: The third frame presents a continuation of the garlic preparation, with a discernible increase in the number of discarded skins on the wooden board, which now harbors small clusters of the papery remnants. The hands, consistently the focal point, hold a nearly peeled garlic clove, with just a few fragments of skin still adhering to it. The knife, ever-present, has yet to be re-engaged in the process. The surrounding kitchen elements remain unchanged, underscoring the singular focus on the task at hand, while the bowl to the side holds the peeled cloves, signifying the progress made thus far.

#### Sample 406 — After

- Similarity: 0.4209
- Prediction: In this frame, the bin's contents are visible, indicating that the bin has been fully emptied. The person's hand is still holding the bin, suggesting that the contents of the bin have been removed from the bin. The bin is now in a more natural state, with the lid still firmly in place. The overall environment is more neutral, with no noticeable changes to the surrounding environment.
- Reference: The strainer is positioned over a receptacle, appearing almost directly above it. Very minimal traces of the orange-yellow liquid remain within the strainer, signifying that almost all of it has been emptied out. The strainer itself, mostly void of its contents, appears clean and almost pristine, with its mesh structure being more evident and discernible.

#### Sample 408 — After

- Similarity: 0.2913
- Prediction: In this frame, the spread of the dough has been completed, indicating that it has been evenly spread across the entire surface. The texture of the butter has improved, with a smoother surface and a more uniform distribution of the ingredients. The thickness of the oil has increased, suggesting that there is still a thin layer of dough to work with.
- Reference: The bottle is now in an open state, with the cap completely removed and set aside. The person's hand, still grasping the neck, tilts the bottle to a slight angle, signaling an intention to pour or spread the contents onto the tortilla. The immediate area around the bottle's mouth is clear, suggesting that the content hasn't been poured out yet or has been dispensed very minimally.

#### Sample 410 — After

- Similarity: 0.4437
- Prediction: In this frame, the corn kernels appear to have been scooped out of the can, indicating that the corn has been thoroughly removed from the can. The corn is now firmly in the can's center, with the kernels extending downwards, forming a downward-sloping pattern. The kernels are now more evenly distributed across the corn, suggesting that they've been evenly distributed. There's a slight movement in the direction of the corn's spread, implying that there's still a large amount of corn remaining.
- Reference: In this frame, the dispersal of sweetcorn across the pizza appears more complete. The kernels are spread out with a greater coverage, filling in previously bare patches of dough and sauce. The hand and can that were dispensing the sweetcorn are still present, implying the continuation of the action, yet there’s a sense that the sprinkling process is nearing its end. The kernels that have landed seem static, resting heavily upon the surface as if settling into their final position.

#### Sample 412 — After

- Similarity: 0.4703
- Prediction: In this frame, the peeler appears to be in a slightly different state, indicating that the water has been sucked out of the stem. The water droplets appear to be more concentrated, implying that they have been rinsing or washed away. The hand's grip is more firm, suggesting that there may be a slight movement in the water's direction, possibly due to a clogging or abrasive action.
- Reference: In this frame, the spring onion is undergoing a thorough rinse. The fingers have moved further up, near the middle of the stalks, ensuring a secure hold while the water cascades over the entire length of the onion. The stalks are bending gracefully under the stream of water, highlighting their fresh and pliable nature. The glistening droplets splash off the onion's surface, washing away any residual soil or debris, and the roots are now fully immersed, indicating a complete cleaning process.

#### Sample 415 — After

- Similarity: 0.3926
- Prediction: In this frame, there is a noticeable shift in the direction of the pan, indicating that the pan has moved closer or further away from the person's perspective. The pan's position is blurred, suggesting that the person is engaged in some sort of action, such as removing the pan from its position, or putting it in a different position.
- Reference: The lunch box appears to be opened even further compared to the second frame. The content inside the box is now more visible, but it remains hard to determine its exact nature. It continues to resemble layered food items like sandwiches or wraps. The transparent nature of the lid offers a clearer view into the contents, though precise details remain elusive.

#### Sample 422 — After

- Similarity: 0.2934
- Prediction: In this frame, the timer remains in the same position as in the previous frame, and the oven's knobs remain unchanged, suggesting that the oven has been turned on.
- Reference: The oven glove reappears in the scene, this time being worn correctly with the person's hand fully inserted into the glove. The fit appears snug and proper, covering the wrist and extending past the beginning of the forearm. The glove seems to be clean and in good condition, with no visible signs of wear or damage. This suggests that the individual is prepared to either handle something hot or is in the midst of doing so, with the glove serving its intended purpose of protecting the hand from high temperatures.

#### Sample 433 — After

- Similarity: 0.2985
- Prediction: In this frame, the hand is positioned in a horizontal position, with the hand resting on a table or counter. The hand's position is blurred, indicating that the hand has been removed from the table. The camera's focus is on the hand, which is now positioned on the table, pointing to the kitchen counter or the kitchen sink. The absence of a hand in the frame suggests a shift in the direction of the hand.
- Reference: The cloth now appears more loosely held, with the person's grip relaxed, suggesting the squeezing action may be complete. The cloth itself looks less twisted and more spread out than in the previous frames, with some parts hanging down, indicating that it is likely in the process of being opened up after wringing. The color of the cloth remains consistent with the earlier frames, light and uniform, without any visible patterns or designs that can be made out from this perspective.

#### Sample 436 — After

- Similarity: 0.4242
- Prediction: In this frame, the hand has moved closer to the kitchen counter, indicating that the oven has been removed from the kitchen. The hand's position remains unchanged, suggesting that the kitchen is now in a state of transition. The kitchen's interior is now more cluttered and cluttered, with fewer items on the counter and a sharper focus on the task at hand.
- Reference: The peeler now has been picked up again, and the hand that grips it exhibits a more dynamic tension, as if it is in the midst of peeling action. The peeler's blade is angled in such a way that it is ready to make contact with the eggplant, positioned to continue the peeling process. This frame captures the motion of food preparation, with the hand's positioning and the peeler's orientation suggesting a repetitive and rhythmic motion typical of peeling vegetables.

#### Sample 437 — After

- Similarity: 0.3851
- Prediction: In this frame, the knife has been removed from the bowl, indicating that it has been placed on the cutting board. The surface of the knife is still slightly damp, suggesting that the knife's position has been changed. The knife remains in the same position as before, but the knife now has a more pronounced presence, resembling a sprinkling of soapy water.
- Reference: A hand comes into the frame, moving towards the pepper pieces, suggesting an intention to pick them up or move them. The fingers are positioned in a way that they are about to grasp the pepper pieces, suggesting imminent action. The overall composition of the frame captures a moment of anticipation, as the viewer waits to see where the pepper pieces will be moved to next.

#### Sample 446 — After

- Similarity: 0.2181
- Prediction: In this frame, the moka pot appears to have been removed from the pot, indicating that the pot has been placed on the stove. The moka burner remains in the same state as before, but the pot is still tilted away from the stovetop, implying that it has been removed.
- Reference: In this frame, the hand has positioned the cap on top of the bottle, and it appears that the cap is being twisted on. The tissue is still wrapped around the cap, aiding in the final tightening of the cap. The hand's fingers have shifted to a more dynamic position, indicative of the twisting motion required to seal the bottle. The environment remains unchanged, with the focus solely on the action of closing the bottle.

#### Sample 456 — After

- Similarity: 0.4744
- Prediction: In this frame, the cup is still held in the hands of a person, indicating that it has been rinsing or washed. The cup's surface is still wet, but the water droplets are still visible, suggesting that the cup may have been soiled. The hand's grip on the cup appears to be more firm, suggesting a more gentle action. The water droplet's movement suggests that the water has saturated the surface of the cup, implying a thorough rinse.
- Reference: The coffee machine remains in the same decorative design with its distinct blue and gold patterns. However, its position appears to have slightly changed, indicating that it might have been shifted or rotated. The top part of the machine is more visible than in the previous frame, and the hand that was earlier interacting with it is no longer obstructing the view. The ambiance of the surroundings seems brighter, suggesting a slight change in lighting or camera exposure.

#### Sample 457 — After

- Similarity: 0.4417
- Prediction: In this frame, the bowl has been removed from the kitchen counter, indicating that it is no longer in the same position as the previous frame. The hand's movements are more consistent, suggesting that the bowl is now in a different state. The bowl's surface remains unchanged, and the surrounding area appears to be a bit damp. The spoon's hand is still holding the bowl, implying that he or she has been handling it for a while.
- Reference: In this frame, the mixture achieves a greater degree of homogeneity and appears even smoother and more cohesive than in the previous two frames. The consistency seems to have thickened slightly, which could be the result of the ingredients being well-combined or the mixture beginning to set or react chemically. The stirring pattern is very well-defined, with a clear spiral indicating vigorous and consistent mixing. The color is a more uniform yellow, suggesting a complete amalgamation of ingredients.

#### Sample 458 — After

- Similarity: 0.4637
- Prediction: In this frame, the rinsing of the board has been completed, indicating that the water has been drained from the bottom of the bowl. The hand's grip on the plate is still firm, suggesting that it's still a bit wet, but the water's presence is still visible. The sink's surface is still wet and there's a slight movement in the direction of the sink, implying that the board is now being rinsed.
- Reference: The tap's lever now shows a noticeable change, positioned at an angle that suggests the water has been turned on. The change in the lever's angle from parallel to the countertop to a downward tilt is a clear indication of activation. While water is not visibly flowing from the spout in the frame, the position of the lever is consistent with typical tap operation for initiating water flow.

#### Sample 459 — After

- Similarity: 0.4727
- Prediction: In this frame, the hand appears to be engaged in the action of removing the object from its position. The hand's focus is now on the kitchen counter, with the kitchen sink still visible, indicating that the hand has been removed from the kitchen. The kitchen sink appears to have been placed in the same position as the hand, implying the hand is now engaged in some sort of action, such as removing a piece of paper or a utensil.
- Reference: The can is now in motion, as evidenced by the blurred surroundings and the dynamic angle of the can itself, suggesting that it is being moved rapidly. The blurred hand position suggests a downward action, likely placing or dropping the can into a receptacle out of frame. The lid appears to be in the same state of opening as the previous frame, not further detached, but the rapid movement has caused the contents to shift, potentially leading to the spillage of the liquid and the spherical items within.

#### Sample 463 — After

- Similarity: 0.4745
- Prediction: In this frame, the pot has been turned off, indicating that the water has been removed from the burner. The surrounding area remains unchanged, with the stove still untouched and the kitchen still unoccupied. The absence of a pot indicates that the burner has not been turned on, implying that there is no need to turn the burner on.
- Reference: The third frame continues to showcase the kitchen environment and the hand in close proximity to the countertop or appliance interface. The specific state of the switch remains elusive, but there's a distinct impression of movement, potentially indicating the switch's activation or deactivation. The close-up nature of this frame in relation to the switch area suggests that there's an ongoing interaction, but the definitive state of the switch, either on or off, cannot be confidently ascertained.

#### Sample 469 — After

- Similarity: 0.2449
- Prediction: In this frame, there is a noticeable increase in the number of ingredients on the counter, indicating a shift in the direction of the cooking process. The kitchen is now cluttered with more items, such as utensils, paper towels, and other household items. The skin is now more exposed, suggesting a change in the way the food is being prepared.
- Reference: The cover seems to be in a more elevated position compared to the previous frames, with the lifting process appearing almost complete. The perspective shows a more pronounced view of its underside. Shadows under the cover suggest it's hovering above its initial position, which combined with the visible hand movement, implies it's being actively lifted. The surrounding area is slightly blurred, indicating swift motion, further emphasizing the dynamic state of the cover being removed.

#### Sample 470 — After

- Similarity: 0.3007
- Prediction: In this frame, the bottle has been completely re-opened, indicating that it has been removed from its original position. The hand's grip is still firmly in place, suggesting that the bottle is still in its original state of being. The bottle's surroundings are more reminiscent of the previous frame, implying that there is a slight change in the position of the bottle.
- Reference: The plug is now almost completely removed from the socket, with only the tips of the prongs still in contact with the outlet. The person’s hands, still sheathed in yellow gloves, show a relaxed grip, indicating the completion of the unplugging action. The background remains cluttered, and the shadow of the person’s hands and the plug is still visible on the wall, mirroring the action above.

#### Sample 477 — After

- Similarity: 0.4306
- Prediction: In this frame, the sauce has been reduced to a more uniform consistency, indicating that the ingredients have been thoroughly stirred. The color of the sauce is now more vibrant, with hints of a darker color, and the consistency is more consistent. The stirring is complete, suggesting that the sauce may be ready to serve.
- Reference: Here, the light maintains its vivid blue core but is surrounded by a broader, less intense outer flame, which hints at a stable and sustained heat source. The consistency of the flame's color and shape suggests that the burner is now in a steady state, providing a continuous and even heat. The light's reflection is consistent and widespread, indicating that the burner has reached an optimal operating condition, and the pot is fully enveloped in the heat, likely contributing to a steady cooking process.

#### Sample 480 — After

- Similarity: 0.3107
- Prediction: In this frame, the plastic bag has been placed in a new position, indicating that the contents of the container have been removed from its packaging. The hand's grip on the bag is still firm, suggesting that the container has been rinsing or washed. The bottle's surface is still slightly damp, suggesting the contents are still present. The packaging's interior appears to be a bit dampering, possibly due to the presence of more water.
- Reference: The dispensing action seems to have concluded, with a discernible portion of the sponge now saturated with the liquid washing up. The wetted area appears glossier and darker in contrast to the other parts of the sponge, suggesting that a significant amount of liquid has been absorbed.

#### Sample 482 — After

- Similarity: 0.3686
- Prediction: In this frame, the cling film has been removed from the tray. The film's surface is now more exposed, with the center of the film separating from the peel. The person's hands are holding the film in one hand, indicating that the film has reached the desired length.
- Reference: The packaging now shows clear signs of being tampered with. The hand continues its interaction with the lighter meat's package, and it appears that a portion of the seal is being lifted or pulled back. The action suggests that the individual is in the process of opening the packaging to access the meat inside. Although the seal isn't entirely removed, a partial view of the meat inside becomes visible, indicating that the package is no longer in its original, untouched state.

#### Sample 485 — After

- Similarity: 0.2585
- Prediction: In this frame, the contents of the package have been removed from the box. The packaging is now in a more open state, indicating that the contents are no longer visible. The hand's grip on the package is more firm, suggesting that the package may have been pushed open.
- Reference: The milk carton has now made contact with the floor, resting on its side with the top facing the wall. It is placed near a corner where the wall meets the floor, and the person’s hand is reaching towards it, possibly to pick it up or prevent spillage. The immediate vicinity is relatively bare, apart from a television and cleaning equipment, which implies that the carton might be in a transitional area such as a corridor leading away from the kitchen.

#### Sample 488 — After

- Similarity: 0.4156
- Prediction: In this frame, the lettuce has been re-rinsing again, with the water still dripping from the bottom of the bowl, indicating that it has been thoroughly rinsed. The leaves are now in a more streamlined state, and the water is still running through the leaves, implying that the water has gotten into the leaf's core.
- Reference: In this moment, the leaf appears to be at the final stages of being washed. The water's force seems to have unfurled the leaf more fully, revealing its broad surface area and the intricate vein pattern across its structure. The person's hands are placed in a way that indicates a final rinse, with fingers spread to allow any residual dirt or particles to be dislodged by the water stream. The leaf's texture looks uniformly wet, showcasing a consistent sheen that covers its entirety.

#### Sample 490 — After

- Similarity: 0.4265
- Prediction: In this frame, the hands are engaged in the process of removing the contents from the container, revealing a clearer view of the contents of the container. The hands are now positioned in the same position as before, indicating that the contents have been removed from the package. The packaging is now more visible, with the lid still slightly open, suggesting that the container may be ready for use.
- Reference: The tortilla is now partially folded, with the hand actively pinching one edge, guiding it into the confines of the plastic packaging. The tortilla has transformed from its previously flat and open state to a semi-crumpled form, bending to accommodate the reinsertion process. This action creates creases and wrinkles on its surface, a stark contrast to the previously smooth appearance. The tortilla is now interacting with its packaging, which bears bold colors and brand markings that suggest a commercial origin.

#### Sample 495 — After

- Similarity: 0.3078
- Prediction: The drawer's position remains unchanged, indicating that it has been moved to a new position. The drawer is now in the same position as the previous frame, and the hand's fingers are still present, suggesting that the hand is now engaged in some sort of action.
- Reference: In this frame, the plug is now half-out of the socket, with the prongs partially visible and the plug's body tilted downwards at an angle indicative of it being in motion. The motion seems to be a result of the pulling force applied to the cord, which is more taut and directed sharply to the bottom right. The plug's removal from the socket has not been completed yet, as the electrical connection appears to be still partially intact. The environment remains unchanged, continuing to suggest a domestic interior with minimalistic design elements.

#### Sample 496 — After

- Similarity: 0.4402
- Prediction: In this frame, the paper has been placed in a new position, indicating that it has been fully grasped by the hands. The paper's shape appears to be a bit looser than before, suggesting that the paper may have been pushed into the hands of someone or something else. The person's hands seem to be grasping the paper, implying that they are holding it in their hands.
- Reference: The focus here is closely on the bag, held outstretched in one hand, displaying the 'THIS SIDE UP' instruction clearly, signifying the correct orientation for microwave cooking. The bag appears more bloated than in the previous frame, suggesting the popcorn has fully popped. The text on the bag is sharp and readable, showing a caution for the contents being hot. The person's handling of the bag, with a single hand from the bottom, indicates confidence that the popping is complete and readiness to open the bag.

#### Sample 497 — After

- Similarity: 0.2441
- Prediction: In this frame, the sink's surface appears to be in a downward motion, indicating that the water has been drained from the sink. The person's hands are now positioned on the sink, implying that the sink has been thoroughly cleaned. The sink appears to have been wiped with a damp cloth, suggesting that it has been washed or was sanitized.
- Reference: The yellow glove continues to be the focal point in this frame. The hand wearing the glove has shifted its position once more, suggesting the wearer is moving quickly through various tasks. The glove remains intact without any visible wear or tear, suggesting it is durable. From this angle, a portion of the hand without the glove is also visible, juxtaposing the bare skin with the gloved hand and providing a clear demarcation of where the glove begins or ends.

#### Sample 20 — Transition

- Similarity: 0.4325
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the packaging. Initially, the package is in a state of disintegration, with the contents being exposed to the elements. As the frame progresses, the person's hands begin to engage in the action of opening the package. By the final frame, the packaging has been fully opened, indicating that the contents have been removed from the box. The packaging transitions from being open to being closed, suggesting that the package has been closed for a moment or two, and indicating a process of removing the contents
- Reference: Analyzing the state change of the yogurt across the three frames, one can observe a deliberate and sequential arrangement. Initially, the yogurt is being positioned as part of a set, with careful attention to the orientation and order. As the sequence progresses, the yogurt is moved with intention, showcased by the hand's secure grip and focused placement. By the final frame, the yogurt has been repositioned at a distinct angle, marking the conclusion of its movement. This deliberate progression indicates a methodical approach, possibly for an organizational or display purpose within the context of the kitchen environment.

#### Sample 27 — Transition

- Similarity: 0.4392
- Prediction: Over the sequence of frames, there is a noticeable progression in the state of the cereal box. Initially, the box is partially closed, with the hands attempting to open it. As the sequence progresses, the hand's action becomes more deliberate, focusing on the contents of the box. By the final frame, the person's actions become more deliberate and precise, resulting in a clearer picture of the contents.
- Reference: The sequence of images illustrates a gradual opening of a Twinings tea box over three stages. Initially, the box is intact, with the cellophane just beginning to be peeled back. In the second stage, the cellophane is removed, and one flap of the box is opened, revealing the silver foil bag inside. By the third stage, the opening process is near completion, with both flaps of the box opened wide and the contents almost ready to be fully revealed. The steady hands of the person indicate a careful and deliberate action, ensuring that the tea bag is not damaged during the unboxing.

#### Sample 28 — Transition

- Similarity: 0.3040
- Prediction: Over the course of these three frames, the roll transitions from a state of rest to a place of rest. Initially, it is in a position of rest, and then re-positioned. As the sequence progresses, the rolling tray emerges from its position, indicating that the roll is ready for use. The rolling tray's surface transitions between a resting position and a tilted position, suggesting the roll's transition from being a stand-alone roll to one that can be used as a pre-cooking tray. Finally, the
- Reference: The paper undergoes a visible transformation across the three frames: from an intact, untouched state to a partially torn state, and finally to a fully torn and separated state. The initial grip and force application result in a rough, uneven tear, highlighting the random nature of paper tearing by hand without a pre-folded line. The tearing process reveals the fibrous interior of the paper, a stark contrast to its initially smooth exterior. This sequence captures the progression of tearing, emphasizing the irreversible change from a whole to a separated state, demonstrating the physical properties of paper under stress.

#### Sample 33 — Transition

- Similarity: 0.4762
- Prediction: Over the course of these three frames, the utensil undergoes a transition from a stationary position to a moving object. Initially, it's positioned in a position that's likely to be used as a kitchen tool, and then re-arranged. As the frame progresses, the hand's motion becomes more apparent, indicating that the item has been moved. As a result, its state is blurred, suggesting that the hand is being used for another purpose. By the final frame, there's no sign of the hand in motion,
- Reference: The sequence of images captures the gradual opening of a kitchen cabinet. Initially, the cabinet is only slightly open, providing a limited view of its organized lower shelf. As the frames progress, the door swings wider with each successive image, revealing more of the interior. From a neatly arranged collection of cans on the lower shelf to a more assorted arrangement of jars and containers on the upper shelf, the opening door parallels an increasing reveal of the cabinet's contents. The movement appears smooth, indicating a well-used and familiar action in the domestic setting, perhaps preparing for meal preparation or the resumption of kitchen activities.

#### Sample 41 — Transition

- Similarity: 0.3710
- Prediction: Over the course of these three frames, the tray undergoes a transition from being a static state to a dynamic one. Initially, it is resting in its original position, indicating that the tray is ready for use. As the frame progresses, it becomes more and more visible, suggesting the tray has been placed in a state of transition. By the third frame, it appears to have been placed on the tray's surface, suggesting a gradual transition from a stationary state to an active one. The tray transitions into a more stable state, suggesting that it is likely to be
- Reference: The progression of these frames captures a small but telling narrative of domestic life. Initially, the milk bottle appears abandoned and potentially open, vulnerable to spilling or contamination. As the frames advance, human interaction becomes evident, with the bottle being given attention, likely to prevent wastage or for storage after use. The cap, initially ambiguous, moves towards a state of being firmly placed back on the bottle. This sequence reflects a moment of care or routine within the kitchen's daily rhythm, a choreography of use and maintenance often overlooked.

#### Sample 45 — Transition

- Similarity: 0.3746
- Prediction: Over the course of these three frames, the liquid undergoes a noticeable transformation from a static state to a dynamic one. Initially, it is a clear indication of the pouring process, but as time progresses, it becomes more and more agitated. By the final frame, the fluid is clearly displeasing itself, indicating that it is ready to be poured. This progression shows the fluid's transition from static to dynamic, with a gradual increase in the volume of the liquid, resulting in a smoother, more uniform liquid. The final frame captures the
- Reference: The jam's transition from the jar to the bowl showcases its sticky and thick properties. Initially, it forms a cohesive shape on the fork, resisting the pull of gravity. As the fork moves away from the jar, the jam stretches into a thin, resistant strand, demonstrating its adhesive quality. Finally, the jam is deposited into the bowl, leaving a trail and losing its defined shape, reflecting its semi-liquid state that allows it to be spread while still maintaining a degree of thickness that prevents immediate flattening.

#### Sample 61 — Transition

- Similarity: 0.3197
- Prediction: Over the course of these three frames, the chair undergoes a significant transformation from a static state to a dynamic one. Initially, it's tended to be in a state of disarray, but as the frame progresses, it shifts into a more dynamic state, indicating a change in the chair's state. By the final frame, there is a noticeable shift in the position of the chair, with the chair still positioned in the same position as the previous frame. This transition is reminiscent of a moment when the chair was placed in motion, and
- Reference: The journey of the crumb across these frames tells a story of displacement and cleaning. Initially stationary and almost camouflaged by the tablecloth's pattern, the crumb is subtly jostled by the unseen forces exerted by the approaching vacuum cleaner. As the cleaner moves closer, the crumb's environment becomes visibly disturbed, with the material of the tablecloth wrinkling and shifting. Finally, the crumb is drawn into the shadow of the vacuum cleaner, its final moments on the table marked by a dramatic change in light and position, signifying the crumb's inevitable conclusion of being vacuumed away.

#### Sample 63 — Transition

- Similarity: 0.4692
- Prediction: Over the course of these three frames, the bowl undergoes a transition from a static state to a dynamic one. Initially, it is in a state of rest, but as time progresses, it becomes more and more active. As the ingredients are added to the bowl, there is a noticeable shift in the bowl's position, indicating that the bowl is being used for cooking. By the final frame, there are no visible signs of the bowl being removed from the table, suggesting that it has been placed on the counter. This transition is indicative of a culinary process, with the bowl
- Reference: The egg mixture undergoes a visible transformation across these frames. Initially, the egg is in its raw, unaltered state with a distinct separation between yolk and whites. As we progress, the yolk is broken down and the whites begin to merge, with the pepper becoming more integrated. By the final frame, the action of mixing has created a uniform, airy mixture, indicative of a well-mixed scramble or omelette base. This progression reflects the methodical process of preparing eggs for cooking, where the initial stage of distinct components gradually evolves into a single, smooth preparation ready for the pan.

#### Sample 73 — Transition

- Similarity: 0.3953
- Prediction: Over the course of the three frames, there's a noticeable progression in the cleaning process. Initially, the surface is clean, with no visible residue. As the frames progress, we see a significant reduction in the amount of water on the surface. By the final frame, there is a visible improvement in the state of the staining, with a clearer and cleaner surface.
- Reference: Observing the grid across these frames shows a clear progression in its manipulation. Initially held at an angle, the grid is being adjusted, moved, or possibly cleaned. From the slanted hold, it transitions to a more balanced position, with both hands engaging to steady it. The final position is more settled, with a horizontal alignment that indicates a deliberate placement within the sink. Throughout this sequence, the presence of water droplets evolves from sparse to more dispersed, suggesting the grid has undergone a cleaning or rinsing process, with the hands' movements causing water to spread across its metallic surface.

#### Sample 74 — Transition

- Similarity: 0.4348
- Prediction: Over the course of these three frames, the flour undergoes a transformation from a static state to a dynamic one. Initially, it is in a state of disintegration, indicating a phase of mixing. As the process progresses, the batter becomes more and more agitated, leading to the formation of a clumping mixture. By the final frame, the dough has been fully incorporated and ready for use, with a smooth, uniform texture.
- Reference: Over the course of the three frames, the scale is systematically repositioned on the countertop, moving from the right-hand side towards the center, and then overlapping with the notebook to the left. The scale remains unused throughout, as indicated by the absence of a lit display or visible digits, implying a pre-weighing stage. The person's hands suggest a methodical process of setting up, first clearing the space and then positioning the scale for optimal use. This sequence of movements reflects a deliberate preparation for the accurate measurement of ingredients, a critical step in the culinary process.

#### Sample 83 — Transition

- Similarity: 0.4923
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the salsa. Initially, it's in a state of dismantination, but as the process progresses, it becomes more and more open. By the final frame, the salt has been removed from the container, indicating a gradual change in the way the salsa is handled. This progression is indicative of a phase in the process of preparing the salsa, with the addition of additional salt to the container. The final frame shows a clear progression in how the salsa interacts with the rest of the
- Reference: Over the course of these three frames, the pesto jar undergoes a noticeable transformation. Initially sealed and undisturbed, the jar maintains its freshness and pristine state. As we progress, the jar is opened, revealing its lush contents and inviting interaction. By the third frame, it's evident that someone has accessed the pesto, either stirring or extracting some of it, leaving behind traces of their interaction with the contents. The transformation captures a typical sequence of events when someone is about to use a condiment in their cooking, where the jar transitions from a sealed state to one that has been actively used.

#### Sample 86 — Transition

- Similarity: 0.4558
- Prediction: Over the progression of these three frames, there is a clear progression in the packaging's state of being. Initially, the packaging is positioned in a state of rest, with its contents still in its original state. As the frames progress, the contents of the bag are exposed to the elements, indicating a deliberate action. By the final frame, the bag has been fully opened, and the contents have been removed from the packaging. The packaging transitions from a resting state to a more stable state, with the packaging still firmly in place. This sequence captures a moment when a
- Reference: The leek, originally in a state of transition from bag to counter, has undergone a rapid and unscheduled descent to the floor. Initially held in a stable position, it has slipped from the person’s grasp, flipping end over end as it falls. The stages of its fall are marked by the increasing disarray of the plastic wrap and the blurring of its leaves, telling a story of motion and gravity at work. This sequence captures the leek's accidental journey from control to chaos, each frame depicting a further stage of its unintended flight towards the floor.

#### Sample 89 — Transition

- Similarity: 0.4762
- Prediction: Over the course of these three frames, the utensil basket undergoes a transition from a static position to a dynamic one. Initially, it is positioned in front of a kitchen sink, indicating a potential use, and then re-positioned as a part of the kitchen counter. As the sequence progresses, the basket becomes more and more cluttered and cluttered, resulting in a blurry, cluttered appearance. By the end of the frames, there is a noticeable shift in the basket's position, suggesting a deliberate use of the
- Reference: Throughout the progression of the three frames, the squash container undergoes subtle shifts in positioning. Initially, it stands upright in the first frame with the cap removed. As we transition to the second frame, a minor tilt or movement is evident, though the cap's position remains unchanged. By the third frame, the container seems to stabilize, reflecting a similar state as observed in the second frame. Throughout this progression, the container remains unsealed, implying a continuous phase of usage or preparation for consumption.

#### Sample 90 — Transition

- Similarity: 0.4615
- Prediction: Over the course of these frames, the lemon undergoes a transition from being a single ingredient to being part of a meal. Initially, it is presented as a whole, but as the sequence progresses, it becomes increasingly part of the kitchen. As the images progress, there is a shift in the position of the lemon, indicating that it is ready to be served. This progression suggests that the lemon is preparing for its next meal, and that it may be ready for another meal. The final frame, however, shows the lemon's transition from a raw fruit to a culinary
- Reference: The progression of the pepper's preparation reveals a methodical process. Initially, it is presented as a halved item with hidden seeds, then transitions to an open state with its core exposed, highlighting the natural partitioning of its flesh. Finally, it is cleanly segmented into even slices, seeds removed, and meticulously arranged. This sequence showcases not only the steps of preparing the pepper but also the care taken to maintain its aesthetic and structural integrity throughout the process. The change from a whole vegetable to a prepped ingredient is done with precision, preparing it for its final culinary destination.

#### Sample 100 — Transition

- Similarity: 0.3965
- Prediction: Over the course of these three frames, the kettle undergoes a series of changes in its state of operation. Initially, it is in a state of rest, with the handle positioned in the middle of the room. As the frame progresses, the person's hand interacts with the kettle, indicating that the kettle has been switched on or off. As a result, there is a noticeable shift in the kettle's state of function, from a static state to an active state. The progression of these images reflects the changing state of the kettle in the context of everyday life,
- Reference: Progressing through the frames, there is a clear transition from a well-lit space to one shrouded in darkness. Initially, the light bathes the room, highlighting textures and surfaces with its bright presence. As the sequence progresses, the light diminishes rapidly, giving way to creeping shadows that transform the room's atmosphere. The final state is one of complete darkness, a stark contrast to the initial frame, indicating that the light source has been effectively extinguished, capturing the essence of a room at rest after the light is turned off. The progression not only alters the visual aspects of the space but also suggests a change in ambience from the lively brightness of an active kitchen to the tranquil dimness of the same space at rest.

#### Sample 101 — Transition

- Similarity: 0.4757
- Prediction: Over the course of these three frames, there's a clear progression in the state of the shredded cheese. Initially, it's in a state of disintegration, but as time progresses, the cheese's appearance becomes more noticeable. As the cheese is removed from the container, the spoon's action becomes more deliberate, indicating that the cheese has been incorporated into the container. By the final frame, there are no visible signs of dissipation, and the crumbs are still present. This progression is indicative of a deliberate effort to separate the cheese from the rest of
- Reference: Over the course of these three frames, the milk undergoes a visible transformation from a calm, undisturbed state to one that is actively being mixed. Initially, the milk's surface shows the beginnings of a swirl pattern, evolving into a turbulent texture with ripples in the second frame, and culminating in a whirlpool effect with a frothy, aerated surface in the third. This progression highlights the stirring action's effect on the milk, which is not just a mixing of the liquid, but also an incorporation of air, leading to changes in the milk's surface texture and appearance.

#### Sample 110 — Transition

- Similarity: 0.4436
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the kitchen cabinet. Initially, the cabinet is in a state of rest, with no visible movement or movement. As the frames progress, the door appears to be open, indicating that it has been closed for a few seconds. By the third frame, the hinges have been repositioned, suggesting that the door has been opened. The transition between the frames suggests that the cabinet has been open for some time, and that there has been a significant change in the cabinet's state.
- Reference: The chair undergoes a transition from being partially tucked under the table to being pulled out and away from it. The shift in its shadow and the changing perspective of the chair's legs and seat in relation to the surrounding objects, like the table and the floor tiles, indicate the motion. Throughout the frames, the chair's position relative to the fixed elements in the room, such as the table and stove, highlights the trajectory of movement. The consistent lighting across the frames accentuates the changing angles and positions of the chair, marking the progress of its movement within the space.

#### Sample 116 — Transition

- Similarity: 0.4484
- Prediction: Over the course of these frames, there's a clear progression in the culinary process. Initially, the chicken is positioned in a pot of boiling water. As the sequence progresses, it becomes more and more involved in the cooking process. Finally, the carrot is placed in the pot of simmering water, indicating preparation for a meal. This progression suggests a deliberate step in culinary preparation, with a focus on the preparation of the ingredients. By the final frame, the cauliflower has become a focal point for culinary preparation.
- Reference: Over the course of these three frames, there's a clear progression in the preparation of the ingredients. Initially, the ingredients are laid out, with evidence of fresh chopping and dicing. As we move to the next frame, the ingredients are more organized, and the sweet potatoes appear to have been soaked or marinated. By the third frame, active engagement by the person is evident as they mix the sweet potatoes, indicating a move towards finalizing the preparation or integrating the flavors more thoroughly. The surrounding space also evolves, starting from a messy prep stage and gradually becoming more organized.

#### Sample 119 — Transition

- Similarity: 0.4864
- Prediction: Over the course of these three frames, there is a clear progression in the cleaning process of the cappuccino. Initially, it is being rinsed with soap and water, followed by rinsing it with a detergent solution. As the frame progresses, the person's hands are positioned to ensure that there is no residue left behind. Finally, the bottle is being washed to remove any remaining soapy suds, indicating a thorough cleaning process.
- Reference: Across the sequence, the V60's cleaning journey is evident. Initially nestled in the water for a soak, it is next examined and scrutinized for remaining impurities after being lifted from the water. This progression from soaking to inspection sets the stage for the final, vigorous scrubbing captured in the last frame. The transition from gentle rinsing to active scrubbing demonstrates a methodical approach to ensure the V60 is restored to a state befitting its use in brewing clean, untainted coffee. The careful handling throughout underscores the importance placed on maintaining the V60's condition.

#### Sample 150 — Transition

- Similarity: 0.3170
- Prediction: Over the course of these three frames, the bottle undergoes a
- Reference: Over the course of these three frames, the spice undergoes a transformation from a passive and partly concealed item within a cluttered cupboard to an object of focus and interaction. Initially nestled among various kitchen items, its importance becomes apparent as other objects are moved aside, allowing it clearer visibility. As the frames progress, the intention of interaction becomes clearer, culminating in the hand's direct contact and the spice's removal from its resting place, indicating its imminent use or inspection in the kitchen's activities.

#### Sample 153 — Transition

- Similarity: 0.4230
- Prediction: Over the course of the three frames, there is a noticeable progression in the state of the countertop. Initially, the surface appears to be in a state of disrepair. As the frames progress, the person's hand begins to shift from a scrubbing motion to a more thorough cleaning motion. By the final frame, the countertop appears to have been thoroughly cleaned, with no visible streaks or streaks. This progression is indicative of a thorough cleaning process, with a focus on the overall appearance of the surface.
- Reference: The sequence of images captures a dynamic progression: starting with the pepper mill in a state of uncontrolled descent, then being caught and held firmly, and finally being moved purposefully to a new location or state. The action begins with a state of disorder, indicated by the pepper mill's tilt and the hurried hand movements, then transitions to a controlled grasp that corrects the mill's trajectory, and culminates in a deliberate and controlled motion, likely to reposition the mill. This progression showcases a quick response to an unexpected situation, leading to the stabilization and purposeful handling of the kitchen utensil.

#### Sample 158 — Transition

- Similarity: 0.3771
- Prediction: Over the course of these three frames, the banana undergoes a remarkable transformation from a static state to a dynamic one. Initially, it's positioned in a position that's likely to be used as a source of food, but gradually becomes a focal point in the kitchen. As the sequence progresses, it becomes more apparent that the banana has been placed in the refrigerator, indicating that it is ready to be served. By the third frame, there's no discernible change in the banana's state, suggesting that it may be preparing for a meal, or
- Reference: From a position of rest, the orange has been subjected to an external force, setting it into motion across the table. The transition in its state is evident through the progressive distortion of details on its skin and the shift in reflected light. As it traverses the wooden expanse, it not only changes its position but also its interaction with the ambient environment, exemplified by varying highlights and shadows. This journey from stillness to movement showcases the orange's transient and dynamic nature when acted upon.

#### Sample 160 — Transition

- Similarity: 0.2297
- Prediction: Over the course of these frames, the tin undergoes a
- Reference: Throughout the three frames, there is a progression in the kitchen cleaning process. Initially, the focus is on the sink with the water running, indicating the start of cleaning. The scene then transitions to an overview of the dish rack, suggesting that the washing part may be nearing completion as no new items appear between the frames. By the third frame, the focus on the dish rack with no significant addition of dishes implies that the washing activity might be complete, with the emphasis now on drying and possibly organizing the cleaned items. The consistent presence of cleaning materials throughout the frames underscores the ongoing maintenance of the kitchen space.

#### Sample 188 — Transition

- Similarity: 0.4697
- Prediction: Over the course of these three frames, there's a clear progression in the state of the pan. Initially, the pan is in a state of static, with no movement or movement. As the frames progress, the person's hand begins to move, indicating that the pan has been placed on the table. The transition from a static position to a more dynamic position, suggests a gradual change in the pan's state. By the third frame, the man's hands begin to move around, suggesting that they're engaged in some sort of cooking activity.
- Reference: Throughout the progression of these images, there's a clear transition in the state of the heat, especially concerning the burner on the right. Initially, this burner was set to its maximum heat level, as evidenced by the '9' setting. However, as time advanced, the heat level was decreased to '8', marking a subtle reduction in temperature. This change might have been done to fine-tune the cooking process or to prevent overcooking. By the third frame, this burner was entirely turned off, indicating the end or a pause in that particular cooking process. Meanwhile, the burner on the left maintained a consistent low heat setting across all frames, providing a steady source of heat throughout the observed duration.

#### Sample 193 — Transition

- Similarity: 0.4189
- Prediction: Over the course of these three frames, the avocado undergoes a transformation from a static state to a dynamic one. Initially, it's anchored in a solid state, but as time progresses, it begins to move into a more dynamic state. As the avocado becomes more active, its surface becomes more exposed, indicating that the avocado is ready to be served. By the final frame, it has become a focal point for a variety of culinary endeavors, including the preparation of a dish, such as a soup or a salad. The avocado's transition from
- Reference: Over the sequence of images, the tofu transitions from a state of being prepped to cook-ready. Initially, it's presented as freshly cut chunks on a board. As the sequence progresses, the focus shifts to a single block being expertly scored and then sliced into individual pieces. The knife's journey through the tofu is smooth, reflecting a practiced hand at work. The transformation is purely physical, with the tofu's appearance changing from larger chunks to neatly divided portions, ready to be transferred into the heated wok where the cooking process will commence.

#### Sample 194 — Transition

- Similarity: 0.4865
- Prediction: Over the course of these frames, the soap undergoes a transformation from a static state to a dynamic one. Initially, it's anchored in a state of dispersión, indicating a phase of action. As the sequence progresses, the water's surface becomes more visible, revealing a vibrant contrast between the water and the surrounding environment. By the final frame, there is a clearer picture of the soap's transition from static to dynamic, with a gradual increase in the volume of the stream.
- Reference: Over the course of these frames, the saucepan transitions from having clear water and visible food residue to being filled with a foamy, soapy mixture that becomes increasingly murky, indicating the removal of food particles. The pan is manipulated from a tilted position to a more stable one, showing a methodical approach to the cleaning process. The constant presence of the individual's hand suggests an ongoing effort to clean the pan thoroughly, with the visible changes in the water's clarity and the reduction of residue reflecting the effectiveness of the cleaning.

#### Sample 197 — Transition

- Similarity: 0.4992
- Prediction: Over the course of these three frames, the paper undergoes a transition from a static state to a dynamic one. Initially, it is positioned on a flat surface, indicating a preparation for use. As the frame progresses, it becomes increasingly exposed to the action of a hand, suggesting that the paper is ready to be used. By the final frame, it appears to be in a state of disintegration, with the paper's surface exposed, suggesting a staged cleaning process. The transition from static to dynamic is marked by a change in the appearance of the
- Reference: Over the course of these frames, the kitchen undergoes a cleaning process. Initially, a spill is noticeable near the stovetop, which the individual is actively addressing by wiping with a white paper towel. As time progresses, the spill appears to be gradually cleaned up, indicated by the paper towel's movement and condition across the counter. While the focus is on cleaning, cooking continues as evidenced by the steam from the pots and the presence of food, suggesting a multi-tasking environment. The persistence of the individual's cleaning effort indicates an intention to maintain cleanliness during the cooking process.

#### Sample 210 — Transition

- Similarity: 0.4882
- Prediction: Over the course of these three frames, there is a noticeable progression in the cleanliness of the cutting board. Initially, it is bare, with no visible signs of cleaning. As the series progresses, the board becomes more and more soiled, indicating a gradual reduction in the amount of food left behind. By the final frame, there are visible signs that the board has been thoroughly washed, with a clear sign of the cleaning process underway. The chalkboard's transition from bare to clean is indicative of a time when the board is being cleaned, demonstrating the effectiveness of the
- Reference: Observing the sequence of images, the soap transitions from being moderately lathered to heavily frothed with suds, and then back to a less sudsy state. This progression indicates a thorough washing process, with the soap being scrubbed, lathered, and finally rinsed. Throughout the frames, the soap diminishes slightly in size due to the abrasion against the cutting board. The suds' lifecycle—from creation to dissolution—parallels the soap's usage, reflecting a dynamic cleaning process. The person’s hands adapt their hold and motion to facilitate the soap's effective application, suggesting an attentive and methodical approach to the task.

#### Sample 211 — Transition

- Similarity: 0.4939
- Prediction: Over the course of these three frames, the cloth undergoes a noticeable transformation from a wet state to a dry state. Initially, it is in a state of dissolving, indicating a cleaning process. As the frames progress, there is a visible increase in the amount of wetness on the cloth. By the final frame, there appears to be a significant decrease in the cloth's water content, suggesting that the cloth has been soaked for a prolonged period of time.
- Reference: The progression of the sink's state from the first to the third frame narrates a short story of kitchen clean-up. Initially, we see the sink area with splashes of water and a single piece of vegetable debris, hinting at prior use. As time progresses, there's evidence of active cleaning—the presence of water streaks, and cleaning implements suggest the person is midway through the task. By the third frame, the cleaning appears nearly complete; the sink is wetter, the debris has been removed, and the person's hands are together in a gesture that often signifies a job well done. Throughout these frames, the state of the sink transitions from used and in need of attention to clean and orderly, reflecting the mindful efforts of the individual tending to the kitchen's cleanliness.

#### Sample 225 — Transition

- Similarity: 0.3990
- Prediction: Over the course of these three frames, the blender undergoes a transition from a static state to a more active state. Initially, the user's hand is resting on the blender's handle, indicating that the blender is ready to be used. As the frames progress, there is a noticeable movement in the blender, suggesting that the user is preparing to use it. By the final frame, there appears to be a gradual deterioration in the blend's performance, with the blender still agitated and unable to fully blend.
- Reference: Throughout the frames, the mixture evolves significantly. Initially, the mixture is rough and variegated, with distinct colors and textures indicating the beginning of the blending process. As the blending continues, there's a clear progression toward a more homogeneous state, with the texture smoothing out and the color becoming uniform. By the final frame, the mixture has transformed into a creamy, airy, and smooth batter, a sign of proper technique and the readiness for the next step in the recipe. This transformation is critical for achieving the desired end product in baking, where the consistency of the batter can greatly influence the texture and rise of the baked good.

#### Sample 226 — Transition

- Similarity: 0.4949
- Prediction: Over the course of these three frames, the packaging undergoes a transformation from a static state to a dynamic state. Initially, the package is in a state of transition, indicating a moment of action. As the third frame progresses, the person's hand begins to interact with the packaging, suggesting a step in the process of removing it from its packaging. Finally, as the third frames progress, the bag's contents begin to move away from the packaging and become more visible. The packaging's transition from static to dynamic is reflected in the packaging itself, implying
- Reference: The wrap undergoes a transformation through these frames, from being an uncut piece draped over the counter's edge to being cut with precision. Initially, it is presented in a state of potential use, and through the frames, it encounters the shears that alter its form. The cutting process is deliberate, resulting in the wrap's detachment from its roll, and the aftermath shows a tidy work area, signifying the end of this particular task. The overall sequence captures a brief yet significant moment in the broader context of kitchen activities, from preparation to the eventual cooking phase.

#### Sample 227 — Transition

- Similarity: 0.3692
- Prediction: Over the course of these frames, there is a noticeable progression in the state of the sponge. Initially, the sponge is in a state of disrepair, with a visible amount of soap and water. As the frames progress, we see that the sponge has become more and more wet, indicating that the cleaning process is underway. By the final frame, we can see that there is still a significant amount of residue on the sponge, which represents a step in the process of cleaning.
- Reference: The sequence of frames captures the progression of repositioning a kitchen drying rack. Initially held at an angle, the rack is being maneuvered over the sink, likely after a cleaning activity given the presence of dish soap and water. As the frames advance, the rack is centered and then aligned with the sink, suggesting a deliberate and careful placement. The person's hands adjust their grip and position, ensuring stability and precision in the movement. This meticulous attention to the orientation of the rack indicates a level of care in maintaining the cleanliness and order within the kitchen space.

#### Sample 238 — Transition

- Similarity: 0.4907
- Prediction: Over the course of these three frames, the olive jar undergoes a transformation from a static state to a dynamic one. Initially, the jar is in a state of rest, but as the frame progresses, it begins to engage in action. By the final frame, the lid has been fully inflated, indicating that it is ready to be used. This sequence captures the moment when a person pours the olive oil into a pot, a moment when the kitchen is preparing to serve it, and a time when the lid is being poured into the pot
- Reference: The flour undergoes a dynamic transition across the three frames, starting with a gentle introduction into the bowl, increasing to a swift pour, and culminating in a substantial deposit of flour. The initial light dusting evolves into a significant mound, reflecting the increasing volume and momentum of the pour. The flour's consistency remains constant, fine and powdery, but its behavior changes from a delicate stream to a more forceful waterfall. This progression is marked by the growing cloud of flour dust, the rising mound within the bowl, and the change in the flour's surface from scattered to smooth and peaked. The action captures the careful control yielding to the forces of gravity and volume as the contents of the jar deplete.

#### Sample 241 — Transition

- Similarity: 0.4801
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the fruit. Initially, the fruit is positioned in a position that is likely to be used as a source of food. As the sequence progresses, it becomes increasingly apparent that the fruit has been placed in an area where it can be served. By the final frame, there appears to be a movement in the fruit's movement, indicating that it's ready for use.
- Reference: Between the three frames, the primary change involves the red ladle's position as it is manipulated by an unseen diner. Initially, it rests within the white bowl; then, it's in mid-air, indicating a motion of being placed down; and finally, it comes to rest on the white paper plate. The motion is deliberate and careful, ensuring the ladle does not contact other items on the table. Throughout this sequence, the rest of the setting remains static, highlighting the singular action of the ladle being moved after a meal. This action is part of the post-meal cleanup process, as the utensil is being set aside, possibly in preparation for washing.

#### Sample 252 — Transition

- Similarity: 0.4452
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the fruit. Initially, the fruit is untouched, with no visible signs of preparation. As the frame progresses, it becomes apparent that the fruit has been prepared and is ready to be devoured. By the final frame, the fruits are clearly visible, with the fruit's texture reflected in the knife's surface. This progression is indicative of a deliberate preparation, with a focus on preserving the fruit for future use.
- Reference: The sequence of frames chronicles the progressive serving of a bundt cake. Initially, a single slice is cut and replaced to show that the cake has been sliced into. Subsequently, this slice is removed entirely, leaving behind a void that marks its absence. As the frames advance, another slice is taken, furthering the cake's transition from a complete ring to a more fragmented form. The serving of the cake is methodical, with each slice cleanly cut and removed, suggesting a careful and considerate serving process. Throughout this progression, the visual characteristics of the cake, like its color and texture, remain constant, reinforcing the cake's quality and the uniformity of its baking.

#### Sample 258 — Transition

- Similarity: 0.4093
- Prediction: Over the course of these frames, there is a clear progression in the state of the jars. Initially, they are fully opened, with the lid partially closed. As the process progresses, the contents of the container are exposed to the elements, demonstrating the readiness to open them. By the final frame, there are visible signs of discharging, from the inside to the outside. This progression is reflected in the hands' motions, indicating a deliberate attempt to open the container.
- Reference: The dish undergoes a notable transformation through the three frames, from a dirty, residue-laden state to a nearly fully cleansed condition. Initially presenting stubborn, burnt-on food remnants, the dish receives a thorough scrubbing that gradually reduces the visible residue. The process involves soaking, application of soap, and physical scrubbing, which are effective in loosening and removing the baked-on materials. The progression demonstrates the effectiveness of the cleaning method, with the final frame showing the dish nearly ready for rinsing or a final wash, highlighting the transition from dirty to clean through the stages of manual dishwashing.

#### Sample 267 — Transition

- Similarity: 0.4795
- Prediction: Over the course of these frames, the jar undergoes a clear transition from being unopened to being opened. Initially, the lid is partially closed, with the lid still attached to the container. As the sequence progresses, the hand's grip becomes more engaged, indicating that the lid has been opened. By the final frame, there is no discernible change in the lid's state, suggesting that the container is being opened for the first time.
- Reference: The sequence of frames captures the gradual unveiling of the sweetcorn, beginning with its concealed state within a sealed can and transitioning towards its exposure as an ingredient ready for use. Initially, the can sits dormant, the sweetcorn hidden from view, its potential as a pizza topping only implied. The narrative then shifts as the can opener engages, piercing the metal lid and commencing its journey around the rim, revealing more of the sweetcorn with each twist. By the final frame, the transformation is nearly complete, with the sweetcorn almost fully exposed, transitioning from a contained food product to an active participant in the cooking process, its golden kernels ready to join the array of pizza toppings.

#### Sample 279 — Transition

- Similarity: 0.4648
- Prediction: Over the course of these three frames, the scale transitions from a static state to an active state. Initially, it is in a state of rest, but as the frame progresses, it becomes more and more visible. As the frames progress, there is a noticeable change in the scale's state of motion, indicating that the scale has been activated. By the third frame, however, it appears to be undergoing a phase of activation, with the hand hovering around the scale, suggesting that the shaker has been triggered. This sequence captures a moment when the scale
- Reference: The sequence of the three frames captures the progressive action of a cabinet door being closed. Initially, the door is wide open, exposing the contents within, and there is a noticeable blur indicating rapid movement. As time progresses, the door moves towards a closed position, with the gap narrowing significantly by the final frame and the motion blur diminishing. This suggests a deceleration in the movement as the door is gently eased to a close, nearly aligning with the frame of the cabinet. The process reflects a typical, careful attempt to close a kitchen cabinet, likely to avoid disturbing the contents or causing noise.

#### Sample 280 — Transition

- Similarity: 0.4730
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the wiper. Initially, it's in a state of static, with no movement or movement. As the frames progress, the blade appears to be in motion, indicating a deliberate action. By the end of the frames, however, there is a clear sign of a moment of action, with the hand positioned in front of the blade, suggesting a quick action. This progression is marked by a change in the position of the hand, suggesting that the blade is being used for a specific purpose
- Reference: Over the course of these three frames, the toaster undergoes a transformation from being an object of focus to becoming a background element in a flurry of activity. The initial frame captures a moment of action centered around the toaster, while the subsequent images document a shift in attention and activity towards other areas of the kitchen. The consistent motion blur throughout the frames suggests a continuous, rapid movement, with the toaster's role diminishing as the scene progresses. This sequence captures the chaotic essence of a moment, likely in the middle of a multitasking kitchen endeavor.

#### Sample 281 — Transition

- Similarity: 0.3618
- Prediction: Over the sequence of frames, there's a noticeable progression in the state of the table's surface. Initially, the table appears to be in a state of disrepair. As the frames progress, the surface appears to have been wiped down, indicating that the table has been thoroughly cleaned. By the final frame, the cleaning agent has been removed and the table is seen to be clean, suggesting that it's time to move on to the next stage of cleaning.
- Reference: From the initial application of the detergent in a fine mist, there is a transition to spreading and then actively wiping the liquid across the surface. The droplets first seen are no longer distinguishable as individual particles but have merged into streaks and then into a more homogenous layer of moisture. The cleaning action evolves from a gentle application to a more forceful movement, indicating a progression from the distribution of the cleaning agent to the actual cleaning process, with the aim of leaving the surface clean and streak-free. The change in the cloth's appearance, from being relatively dry to becoming damp and heavy with detergent, marks the stages of cleaning.

#### Sample 294 — Transition

- Similarity: 0.3887
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the oven. Initially, the oven is in a state of disrepair, with no visible signs of use or maintenance. As the frames progress, we see a gradual increase in the amount of residue on the surface of the burner, suggesting that the oven has been neglected or neglected. By the final frame, we can see that there is still a marked improvement in the oven's state of cleanliness. This progression is reflected in the presence of a person cleaning the oven, indicating that there has been a
- Reference: The progression of the towel's state indicates a series of cleaning actions. Initially presented as a recently used but still serviceable item, it then becomes absent from view, presumably set aside for a moment where the cleaning focus shifts to another object. Upon its return, the towel is employed with more intent and vigor, now visibly dirtier, having absorbed more residues from the cleaning surface. This evolution illustrates a typical cleaning process, where a towel is used, evaluated, and reused with increasing intensity until the task is complete or the towel requires laundering.

#### Sample 297 — Transition

- Similarity: 0.4077
- Prediction: Over the course of these three frames, the chicken undergoes a transition from being untouched to being part of the kitchen. Initially, it is positioned in a state of rest, but as the frame progresses, it begins to move away from the kitchen and onto the cutting board. As the frames progress, there is a noticeable shift in the chicken's state of being, indicating that it is ready to be used as a part of a meal preparation process. By the final frame, it's clear that the chicken is being prepared for use, and that the kitchen is preparing
- Reference: The progression of these frames shows the process of preparing and cooking garlic. Initially, we see the clove intact, indicating the starting point of the culinary action. As we move to the next frame, the garlic has been crushed into a paste, reflecting the transformation from raw ingredient to a form that can be easily mixed with other components of the dish. Finally, the garlic is transferred into the pan, completing its journey from a solid clove to a cooking element that will infuse the dish with flavor. The careful manipulation of the knife and board by the cook's hands underscores the attention to detail and the methodical approach to incorporating the garlic into the meal.

#### Sample 298 — Transition

- Similarity: 0.4576
- Prediction: Over the course of these three frames, the skillet undergoes a noticeable change in its state. Initially, it is positioned in a state of disrepair, indicating that the pan has been used for cooking. As the frames progress, the surface of the skillet becomes more exposed, suggesting that there is still a significant amount of food on the plate. As a result, the pan's state of rest is reflected in the skillet's surface, implying that there has been a shift in the state of the pan. Throughout the frames, there is a visible movement
- Reference: The sequence of images captures the progressive movement of a pair of yellow rubber gloves engaged in kitchen tasks. Initially, the left glove is seen gripping a white bowl, suggesting the commencement of a washing or cleaning action. Moving to the second image, both hands are occupied, with one hand stabilizing a pot and the other in motion, indicative of a multitasking scenario. By the third frame, there's a distinct change, as the gloves are now repositioned to handle a frying pan, suggesting the completion of one task and the beginning of another. Throughout the sequence, the gloves remain taut and appear well-fitted to the user's hands, their bright yellow color standing out against the backdrop of kitchen utensils and appliances. The gloves’ texture and sheen alter slightly with the changing angles and actions, reflecting their flexible and water-resistant nature.

#### Sample 304 — Transition

- Similarity: 0.4104
- Prediction: Over the course of these three frames, the taters undergo a clear transition from being in the kitchen to being washed out. Initially, they are positioned in a state of readiness for washing, with a focus on the task at hand. As the sequence progresses, they become more and more visible, indicating that the task has been completed. By the final frame, there is a noticeable shift in the state of the tea
- Reference: The tin's journey through these frames is a visual narrative of restoration. Initially, it stands as a testament to its robust utility, bearing the marks of many uses. As water is introduced, it takes on a dynamic role, actively engaging with the tin to begin a transformation. The water's force is evident in the way it interacts with the seasoned surface, and finally, the tin sits with water pooled within, a temporary reservoir that hints at the potential for renewal. This progression is not just physical but symbolic, echoing the cycle of use, wear, and rejuvenation inherent in the life of a well-loved kitchen implement.

#### Sample 308 — Transition

- Similarity: 0.4797
- Prediction: Over the course of these frames, there is a clear progression in the rinsing of the coffee maker. Initially, it is being rubbed with soap and water, with a focus on the cleaning process. As the frames progress, we see a gradual increase in the amount of water being rinsed out of the grinder. By the final frame, the water has been drained away from the grinding surface, indicating a thorough cleaning. This progression is indicative of a methodical approach to cleaning the coffee
- Reference: The progression of cleaning the baking tray is quite evident across the three frames. Initially, the tray was being rinsed, with the water pressure aimed at dislodging the large particles and debris. Moving on, it was tilted to facilitate the removal of these particles, allowing a more targeted rinse. Finally, the application of soap and active scrubbing suggests a meticulous cleaning process is underway. Throughout these stages, the tray transitions from heavily soiled to being covered in soap suds, which marks the midway point of the washing cycle, leading towards a fully cleaned state. The person's consistent handling and methodical cleaning process indicate an effective and routine approach to dishwashing.

#### Sample 309 — Transition

- Similarity: 0.4169
- Prediction: Over the course of these three frames, the carrot undergoes a noticeable transformation from a partially steamed state to a fully rinsed state. Initially, it is in a state of rest, but as the frame progresses, there is a visible change in the carrot's state of health. As the frames progress, the knife becomes more and more exposed to the water, indicating that the carrot is ready to be rinsed. By the final frame, there are visible signs of a thorough cleaning, with the carrot still holding a pristine appearance.
- Reference: Over the course of these frames, the tap undergoes a clear transition in its functionality. Initially, it's in a dormant state with no water flow. However, as time progresses, water begins to stream out, and by the third frame, the intensity of this flow has increased substantially. This progression indicates the tap being turned on and adjusted to release water at a faster rate. The entire scene captures the tap's transition from a static state to one of full operation, showcasing the simple yet essential function of such a household fixture.

#### Sample 310 — Transition

- Similarity: 0.4965
- Prediction: Over the course of these three frames, the cake undergoes a significant transformation from a static state to a dynamic one. Initially, it is a light-colored cake, with a slightly uneven surface. As the sequence progresses, it becomes more and more visible, indicating that the cake is being prepared for cooking. By the final frame, it appears to be preparing for a meal, with the cake still in its original state. The cake's transition from an adjined state to an active state is indicative of a culinary process.
- Reference: Throughout the three frames, the tray itself shows no notable changes in its state; it remains a passive element in the process of bread preparation. The three dough balls maintain their positions and shapes, indicating no active handling or shaping between the frames captured. The dough's stillness suggests a resting period necessary for proofing, where the yeast within the dough is allowed to work and cause the dough to rise. The only discernible change is in the camera's perspective, shifting the viewer's angle slightly but not affecting the state of the tray or its contents. The overall impression is one of a paused moment in a kitchen, capturing the quiet yet crucial phase of bread-making before the dough is ready to be baked.

#### Sample 320 — Transition

- Similarity: 0.4305
- Prediction: Over the course of these three frames, the chicken undergoes a significant transformation from being sliced to being fully sliced. Initially, it is a pristine state, but as time progresses, it becomes more and more exposed to the knife's action. By the end of these frames, there is no discernible difference in the quality of the chicken's skin or texture, which are indicative of the preparation process. Throughout this progression, the garlic has become a focal point for a variety of culinary uses, such as the preparation of a dish, or as a tool for
- Reference: Observing the state of the sweet potato skin across these frames shows a clear progression in the peeling process. The initial frame displays a just-begun peel with a skin rich in color and moisture. Moving to the next, there is a noticeable increase in the quantity of skin removed, with evidence of technique refinement and speed. By the final frame, the skin has mostly been stripped away, leaving behind a more extensive and drier collection of peelings. The transformation is marked by a gradual loss of moisture and color in the skin, as well as a shift from a few large pieces to many smaller, drier fragments.

#### Sample 335 — Transition

- Similarity: 0.3416
- Prediction: Over the course of these frames, the mat undergoes a significant transformation from a static state to a dynamic one. Initially, it is in a state of rest, but as the frame progresses, it begins to move away from its original state. As the frames progress, there is a noticeable shift in the position of the mat, indicating that the mat is being used for a cleaning purpose. By the final frame, it's clear that the space around the mat has been transformed into a place for the mat to be placed.
- Reference: Over the course of these frames, the degreaser transitions from a freshly sprayed mist to a settled layer of cleaning agent on the countertop. Initially, the liquid is airborne, caught in the act of being dispensed. As the spray continues, the droplets begin to fall and spread across the surface, moving from a state of suspension to contact. By the final frame, the spray action has stopped, and the degreaser has formed an even layer across the countertop, indicating the completion of the application phase and the beginning of its cleaning action. The progression shows an effective dispersion method, covering the targeted area thoroughly with the cleaning agent.

#### Sample 336 — Transition

- Similarity: 0.4723
- Prediction: Over the course of these three frames, the caner undergoes a noticeable change in its handling. Initially, the handle is tilted to allow the water to reach the bottom, indicating a thorough cleaning. As the frames progress, the hand's grip changes to a more relaxed position, ensuring that the water is able to reach all sides. By the final frame, there is a clear indication of a cleaning process, with the person's hand positioned to ensure that there is no residue left behind.
- Reference: Over the course of the three frames, there is a clear progression in the state of the cutlery from being soapy to becoming increasingly rinsed. The transition from the initial fork with noticeable soap suds to the knife, which shows a focused rinse down the blade, to another fork with reduced suds illustrates a methodical process of cleaning kitchen utensils. The consistent flow of water and the changing angles at which the cutlery is held under the faucet reflect an attentive approach to ensure that all remnants of soap and debris are removed from the items being washed.

#### Sample 338 — Transition

- Similarity: 0.3208
- Prediction: Over the course of these three frames, the omelette undergoes a significant transformation from a static state to a dynamic state. Initially, the surface of the plate appears to be untouched, with no visible signs of cooking. As the frames progress, there is a noticeable shift in the state of the oats, indicating a gradual change in the cooking process. By the final frame, there are no visible changes in the pan's temperature, suggesting a slowing of the meal's cooking process, or a change in its temperature. The omelet's transition
- Reference: Across the three frames, there is a conspicuous absence of any change in the state of the extractor fan. It remains consistently coated with a layer of grime that suggests significant elapsed time since its last cleaning. The fan shows no signs of recent operation, as there is no disturbance in the grease pattern that would indicate movement or airflow. The consistent lighting and lack of motion blur in and around the fan's environment further support the conclusion that it has not been turned on or interacted with during the time lapse these frames represent. The extractor's state is indicative of neglect both in terms of cleaning and in terms of usage, as it seemingly remains an inactive appliance amidst the kitchen's activities.

#### Sample 341 — Transition

- Similarity: 0.3956
- Prediction: Over the course of these frames, the lettuce undergoes a noticeable transformation. Initially, it appears to be in a state of flux, with water running everywhere. As the sequence progresses, the water's stream becomes more concentrated, indicating that the lettuce is being washed out. By the final frame, there is a clear sign of a rinsing-down process, with a visible increase in the amount of water in the lettuce.
- Reference: The tablecloth transitions from a static, artistically displayed kitchen item to an object in the midst of washing. Initially laid out with a prominent apple design, it is subjected to a cascade of water, which introduces a new texture and sheen, altering its appearance and form. As the cleaning progresses, the tablecloth takes on a more functional role, its aesthetic momentarily set aside for practicality. The water's impact is evident in the evolving state of the fabric, from dry and smooth to wet and contoured, highlighting the cloth's transition through the stages of cleaning.

#### Sample 351 — Transition

- Similarity: 0.4956
- Prediction: Over the course of these three frames, there is a clear progression in the state of the butter's preparation. Initially, it is untouched, untouched and untouched. As the frame progresses, the butter begins to crack open, revealing a protective layer of the cheese. As a result, the hand's action becomes more deliberate, indicating that the butter is ready to be used. By the final frame, there are no visible signs of damage, and the butter remains intact.
- Reference: Over the course of the three frames, the olive oil bottle undergoes a transition from being open to being sealed. Initially, the cap is resting independently on the stovetop, separated from the bottle. Moving to the second frame, the cap is picked up and aligned with the bottle for recapping. By the third frame, the action is nearly complete, with the cap being twisted onto the bottle to form an airtight seal. This sequence captures a common yet precise task, requiring fine motor skills to ensure the cap is correctly threaded and the contents of the bottle are preserved. The process is a small but integral part of kitchen activities, reflecting both the use and storage aspects of cooking ingredients.

#### Sample 353 — Transition

- Similarity: 0.4124
- Prediction: Over the course of these three frames, there's a clear progression in the state of the food processor. Initially, it's in a state of rest, with the lid open and the lid closed. As the frame progresses, the user's hand begins to interact with the processor, indicating that the processor is ready for use. By the final frame, the processor has been fully operational, with no noticeable change in its state or functionality.
- Reference: The transition of the button from its initial unpressed state to being fully pressed is a smooth progression. Initially at rest, the button begins to depress under the force of the finger, altering its reflective qualities and shifting the angle of its surface. As the finger continues to exert pressure, the button moves downward until it reaches its maximum range of motion. Throughout this sequence, the surrounding area remains largely unaffected, with only the light and shadows dancing across the button's surface indicating the dynamic action taking place.

#### Sample 356 — Transition

- Similarity: 0.3998
- Prediction: Over the course of these three frames, there is a clear progression in the state of the timer. Initially, it is in a state of rest, with no visible movement or movement. As the frames progress, there are no visible movements or movements in the kitchen, indicating a slowdown in the cooking process. By the end of the frames, however, there appears to be no sign of a timer, suggesting a delay in the preparation process.
- Reference: Over the course of these three frames, the mixture in the pan undergoes a clear transformation. It begins with a brighter, fresher-looking assortment of green ingredients floating in a clear, thin liquid with a light sheen of oil. As time progresses, the liquid gradually reduces, the green components wilt and darken in color, and the overall consistency of the mixture thickens. By the final frame, there is a noticeable reduction in volume, the ingredients have melded together more cohesively, and there is a glossy sheen that suggests the formation of a sauce. This visual progression is indicative of the sautéing and simmering process, where heat gradually breaks down the ingredients, evaporates water content, and concentrates flavors.

#### Sample 358 — Transition

- Similarity: 0.4439
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the burners. Initially, there is a clear focus on the cooking process, with the person's hand hovering over the burner, indicating that the burner has been thoroughly cleaned. As the frames progress, there appears to be a marked improvement in the burner's condition, with a visible reduction in the amount of residue on the burner. By the final frame, there are no visible residues, suggesting that there is still a significant amount of work to be done. This progression is indicative of a more
- Reference: Over the progression of these frames, the hob remains remarkably unchanged, indicating a state of cleanliness and non-use before and during the wiping process. The hand, methodically moving the cloth over the hob's surface, suggests a routine cleaning rather than a response to a recent cooking session. The consistency of the control knobs' positions throughout the frames confirms that the hob has not been used during this sequence. The main alteration is the movement of the cleaning cloth, which traces a path across the hob, likely picking up any unseen particles or smudges, ensuring the surface remains spotless.

#### Sample 359 — Transition

- Similarity: 0.4801
- Prediction: Over the course of the three frames, there's a noticeable progression in the state of the sink. Initially, the sink appears to be in a state of flux, with a visible amount of water in it. As the frames progress, the water level appears to have decreased, and the water content has increased. By the third frame, there are no visible changes in the sink's state, or the presence of a waterlogged area. Throughout the frames, the person's interaction with the sink remains consistent, suggesting that the person is preparing for a cleaning task.
- Reference: Analyzing the bin across the three frames, its state remains consistently full, with the contents reaching above its rim throughout. There is a subtle implication of additional waste being added, as indicated by the human interaction in frames two and three. However, there is no significant visible change to the volume of waste in the bin, suggesting that if something was added, it was small. The environment around the bin stays static, with no observable adjustments to the items on the countertop or within the dish rack. The plastic liner shows a slight bulge in the last frame, which might be a result of the bin being further filled or simply from the movement of the bag as waste was added.

#### Sample 361 — Transition

- Similarity: 0.3949
- Prediction: Over the course of these three frames, there is a clear progression in the state of the chicken. Initially, it's untouched, but as time progresses, the chicken is exposed to the elements. As the frames progress, the hands engage in a deliberate action to remove the chicken from its packaging. By the end of these frames, however, there's no discernible change in the chicken's state, either. Throughout the sequence, the hand's actions reveal a proactive approach to removing the chicken, indicating a readiness to use the chicken as a source of protein.
- Reference: The sequence of images captures a moment-by-moment transformation of the red pepper from its packaged state to being prepped for cooking. Initially, the pepper sits undisturbed, secure in its plastic wrap with other colorful companions. As the moments pass, human interaction introduces change; the hand selects the red pepper, repositions it, and the knife is poised to cut. Finally, the knife slices through the plastic, an act that converts the pepper from a packaged good to a ready-to-use ingredient. This progression not only depicts the physical state change of the pepper but also the methodical approach taken to prepare it for inclusion in a meal.

#### Sample 362 — Transition

- Similarity: 0.3891
- Prediction: Over the course of these frames, there's a clear progression in the wringing process. Initially, the cloth is soaking wet, with the water running through the fabric. As the frame progresses, the water's movement intensifies, resulting in a noticeable decrease in the amount of water in the cloth. By the final frame, the fabric has become less wet and less saturated, indicating that the water has been sucked out of the fabric, causing the cloth to become more wet. This progression is indicative of a thorough cleaning, with a focus on
- Reference: Across the sequence of these frames, there is a clear and deliberate progression from a full flow of water to almost none. The interaction with the tap begins with it fully open, allowing a strong stream of water. As the hands engage with the tap, turning it clockwise, the flow diminishes accordingly. By the last frame, the tap is almost completely turned off, with just a trickle of water left escaping. This sequence captures the concluding action of a routine task, likely the conservation of water after use. The change in flow is smooth and controlled, showing a common daily action of switching off a tap.

#### Sample 363 — Transition

- Similarity: 0.4965
- Prediction: Over the course of these three frames, there's a noticeable shift in the state of the kitchen cupboard. Initially, the cabinet is largely empty, with only a few items in view. As the frames progress, the cupboard becomes more and more visible, indicating that someone is likely to be using the cupboard. By the third frame, however, the kitchen appears to have been occupied, and the cupboard's contents are clearly visible.
- Reference: Over the course of the three frames, the locker’s state remains largely consistent, with the door staying open and the items inside unchanged. The persistent blurriness across the images indicates continuous motion, although the locker itself does not seem to be the primary subject of this motion. Instead, it appears that the camera or person is moving, while the locker remains static, with its contents on display. There is no clear evidence of the door being moved to a closed position or any items being rearranged or removed.

#### Sample 364 — Transition

- Similarity: 0.1870
- Prediction: Over the course of these three frames, the apron undergoes a transition from a static state to a dynamic one. Initially, it is resting in a stable position, indicating that the oven is ready for use. As the sequence progresses, the oven's handle is positioned in front of the oven, suggesting that it is likely to be used as a stand-alone item. By the final frame, it has been fully positioned, suggesting the oven has been set up for use, and indicating the oven
- Reference: Over the span of these frames, the sweet potato undergoes a captivating transformation. Initially, it sits in its whole, untouched state, exuding natural freshness and earthly charm. As we progress, the tuber is carefully dissected, revealing its juicy, vibrant core, and setting the stage for its culinary destiny. By the end, the sweet potato, having been cooked or baked, has transformed into a tantalizing dish, with textures and colors enhanced, promising a delightful taste and aroma to whoever is about to enjoy it. The journey showcases not just a physical change, but a sensory evolution, inviting onlookers to appreciate the culinary art and nature's bounty.

#### Sample 365 — Transition

- Similarity: 0.3742
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the stovetop. Initially, the stove is in a state of disrepair, with visible streaks of grime and grime. As the frames progress, the surface of the burner appears to be clean, with no visible residue. By the final frame, there is a visible improvement in the condition of the oven, with a clearer, cleaner surface and a more uniform appearance.
- Reference: Throughout the progression of these frames, the state of the hob surface has undergone a significant transformation. Starting with a noticeable amount of spilled substance and moisture, there has been a systematic reduction in the residue and sheen with each frame. The presence and action of the blue cloth have been instrumental in this change. From the initial spotting of the spill to the near completion of the cleaning process, the hob's state has shifted from messy to mostly clean, showcasing the effectiveness of the cleaning effort.

#### Sample 367 — Transition

- Similarity: 0.4817
- Prediction: Over the course of these three frames, there's a clear progression in the state of the coffee pot. Initially, the lid is open, indicating the action of removing the cap. As the frame progresses, the hand's motion becomes more apparent, suggesting that the person is engaged in the action. By the final frame, the man's hand appears to have stepped into the action, implying that he is attempting to remove the cap from the coffee maker. This progression suggests a deliberate action, with the person's actions reflected in the glass's surface,
- Reference: Over the course of the three frames, the cap undergoes subtle changes in its position and visibility. Initially obscured and in the periphery, it gradually moves to a more central position in the viewer's field of vision. The illumination improves slightly across the frames, revealing more of the cap's details. Throughout the progression, the cap seems to be in a state of rest amidst a disorderly setting, but its prominence becomes more pronounced with each successive frame.

#### Sample 368 — Transition

- Similarity: 0.3566
- Prediction: Over the course of these three frames, there's a clear progression in the state of the seal. Initially, the seal is in a state of dislodification. As the frame progresses, it becomes more apparent that the seal has been removed from the package. By the final frame, there are no visible signs of openness, and the seal's state is blurred, indicating a deliberate attempt to open the seal
- Reference: Over the course of these three frames, the chopped tomatoes transition from being freshly opened in their can to being absent from the visible area, indicating their progression in the cooking process. Initially, the tomatoes are presented in their raw, canned state, ready for use. As the frames advance, the tomatoes themselves are not directly shown, but the surrounding evidence of cooking activity suggests that they have been set aside or added to a dish that's being prepared. The progression of the ingredients from packaged to being part of a meal preparation is subtly indicated by the changing state of the kitchen countertop, from the organized beginning to a more active cooking stage.

#### Sample 371 — Transition

- Similarity: 0.4952
- Prediction: Over the course of these frames, the vegetable undergoes a transition from a static state to a more dynamic one. Initially, the vegetables are in a state of disintegration, but as they move through the frame, they begin to change color and texture. As the frame progresses, there is a noticeable shift in the vegetable's position, from its original position to its position on the cutting board. By the final frame, the veggies are no longer in their natural state, and the cooking process is complete, indicating that the vegetable is ready to be cooked.
- Reference: The spatula's journey begins with anticipation, held ready above the pan, then it dives into the action, pressing into the chopped vegetables, stirring them around. This motion is purposeful, ensuring an even sauté. Finally, the utensil is lifted, pausing in the air, completing the cycle of cooking action. Throughout these frames, the spatula's role is pivotal in the manipulation of the food, working in harmony with the cook's movements to achieve the culinary goal. The sequence shows a progression from readiness to action to a brief rest, reflecting the rhythm of cooking.

#### Sample 372 — Transition

- Similarity: 0.4661
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the trash can. Initially, the lid is partially open, and the person's hand is positioned in front of it. As the sequence progresses, the object appears to be moving, indicating a deliberate action. By the final frame, the bin has been fully closed, and there is no sign of the contents of the can. This sequence is reminiscent of a scene in which a trash can is being emptied out of the garbage can.
- Reference: The progression across the frames captures a dynamic sequence involving the basket: from being in rapid motion, to the absence of the basket in the frame focusing on the movement of the person, to a final frame where the action culminates in the person engaging directly with the basket's contents. The sequence depicts a swift transition from motion to stability, with the final frame suggesting a resolution to the action, where the person is likely sorting or retrieving items from the basket. The change in the basket's state from blurred to stable, coupled with the person's changing position, narrates a brief story of an everyday activity captured in fragments of continuous motion.

#### Sample 391 — Transition

- Similarity: 0.4467
- Prediction: Over the course of these three frames, the glove undergoes a noticeable transformation. Initially, it is resting in a state of disrepair, indicating that the cleaning process is underway. As the sequence progresses, the gloves become more and more exposed to the water, suggesting that the gloves are still wet. By the final frame, there is a clear transition between the glove's position and the water's flow, implying that the glove is being washed out. The glove transitions from a static state to a more active state, with the hand
- Reference: Over the span of these three frames, there's a noticeable progression in the wetness of the chopping board. Starting from scattered droplets in the initial frame, the water coverage intensifies, with the board transitioning from being partially wet to almost fully saturated by the third frame. This indicates that water is continuously being added or spread across the board's surface. The board's color evolves in tandem with this change, deepening in hue as more of its area becomes wet.

#### Sample 403 — Transition

- Similarity: 0.4271
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the pizza. Initially, the pizza is in a state of disintegration. As the frames progress, the cheese becomes more and more exposed to the knife's action, indicating that the cheese has been incorporated into the dough. By the final frame, there are no visible changes in the pizza's texture or appearance. Throughout these frames, the mozzarella becomes more exposed, suggesting that the pizza has been prepared for the first time.
- Reference: Over the course of these three frames, the onion undergoes a transition from being a stand-alone prepared ingredient to becoming an integral component of a more complex dish. Initially, it's presented in its sliced form, clearly showcased on a plate. As the scenes progress, the onion becomes a part of a layered culinary creation, suggesting an evolving recipe. By the third frame, the onion, while still recognizable, is now harmoniously combined with other ingredients, ready for the next steps in the cooking process. This progression highlights the versatility of the onion and its role in enhancing the flavors of a dish.

#### Sample 406 — Transition

- Similarity: 0.4523
- Prediction: Over the sequence of frames, there's a clear progression in the state of waste disposal. Initially, the trash bin is in a state of disrepair, with the lid open and the lid closed. As the sequence progresses, the bin's contents are removed from the bin, indicating that the waste has been disposed of properly. By the final frame, the lid has been removed, suggesting that the trash has been placed in the trash can for disposal. This progression suggests a deliberate disposal of the waste bin, with a focus on the process of disposal.
- Reference: As we traverse through the frames, there's a pronounced evolution in the state of the strainer. Beginning with a substantial amount of orange-yellow liquid, there's a clear progression of this liquid being drained or poured out. The liquid's presence diminishes considerably from the first to the third frame, with the strainer transitioning from being nearly full to almost entirely empty. This sequence paints a picture of an action being carried out methodically, showcasing the draining process in its different stages, from initiation to near completion.

#### Sample 408 — Transition

- Similarity: 0.4469
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the dough. Initially, the dough is a dense, clump-forming mass, with a smooth, uniform texture. As time progresses, the flour's texture becomes more uniform and uniform, resulting in a coarser, more uniform dough. By the final frame, there are visible signs of a dough's formation, from a thin layer of dough to a thicker, more evenly distributed layer. This progression is indicative of the process of preparing the dough, with the dough being
- Reference: Over the course of the three frames, there is a noticeable transition of the bottle from a closed state to an open one. Initially, the bottle is securely closed with the cap fastened tightly. As the frames progress, there is an evident effort to unscrew the lid, with the hand adjusting its grip around the bottle's neck. By the third frame, the cap has been entirely removed, and the bottle is positioned in a manner indicating an impending action of pouring or spreading its contents onto the underlying surface. Throughout this progression, the bottle remains over the tortilla, suggesting a deliberate intent to add its content to the meal being prepared.

#### Sample 410 — Transition

- Similarity: 0.2865
- Prediction: Over the course of these frames, there's a noticeable progression in the state of the corn. Initially, the corn is in a state of dispersion, with the kernels firmly inserted into the corn kernels. As the frames progress, it becomes apparent that the corn has been sprayed with pesticides. By the final frame, there is a clear indication of the pesticide's impact on the corn, indicating that it's ready to be used. This transition is marked by a gradual increase in the amount of pesticide residue that has been added to the corn
- Reference: The progression of sweetcorn from can to pizza captures a brief narrative of pizza preparation in these frames. Initially, the sweetcorn is introduced to the pizza, finding a home among the stripes of sauce. As we move to the next scene, there is an active engagement, a deliberate scattering that increases the sweetcorn's presence across the pizza's canvas. By the final frame, the act of sprinkling sweetcorn reaches a crescendo, culminating in a more uniform distribution, filling the space with color and texture. The narrative is one of addition and integration, with each frame representing a moment in the transformation of raw ingredients into a pre-baked culinary creation.

#### Sample 412 — Transition

- Similarity: 0.0883
- Prediction: Over the course of these frames, there is a noticeable progression in the state of the thawed polon
- Reference: The progression observed in the spring onion's state from the first to the third frame demonstrates a systematic cleaning process. Initially presented in a dry state, the onion is then subjected to a rinse, evidenced by the water droplets forming on its surface. As the frames advance, the onion is held more securely, and the water pressure increases, causing the stalks to bend and reveal their fresh and crisp quality. The final frame encapsulates the conclusion of the rinsing, with the onion fully saturated and its roots drenched, signifying readiness for subsequent culinary use.

#### Sample 415 — Transition

- Similarity: 0.4491
- Prediction: Over the course of these three frames, the tack undergoes a significant transformation from a static state to a dynamic one. Initially, it appears to be in a state of disrepair, but as the frame progresses, it becomes apparent that it is being used for something else. As the frames progress, there is a noticeable shift in the trays' position, indicating that the bag has been used for a specific purpose. By the final frame, there are no visible signs of the bag's movement, and no sign of the item's presence in the frame
- Reference: Throughout the progression of the three frames, there is a clear sequence of actions centered around the lunch box. Initially, it is securely closed, showing only a slight hint of its contents. As we move to the next frame, the box is gradually being opened, revealing a bit more about what's inside, although the exact nature of the food remains somewhat obscured. By the third frame, the box is opened even wider, displaying its contents more prominently. The transformation depicts a user unveiling their lunch, but the exact details of the meal remain a mystery, with only hints provided by the box's semi-transparent lid and its layered contents.

#### Sample 432 — Transition

- Similarity: 0.3855
- Prediction: Over the course of these three frames, there is a noticeable progression in the state of the light in the room. Initially, the room is largely unoccupied, with only a few lights visible. As the frame progresses, the light transitions to a more reflective state, indicating the presence of a light source. By the final frame, the lighting transition is complete, with the light coming out of the window and reflected back into the room's interior. This transition is marked by a gradual increase in the amount of light that enters the room, suggesting that the room has become more
- Reference: The transition from the first to the last frame captures a smooth and uninterrupted motion of the door being opened. The hand initially engages the door with a push at the edge, then repositions to apply more force, and finally presses flat against the door to achieve full openness. The handle remains stationary throughout, suggesting the door may not be latched or that the opener is using a push technique that doesn't require manipulating the handle. The widening gap reveals an increasing portion of the interior, and the consistency of the door's appearance throughout the motion conveys a fluid and effortless action.

#### Sample 433 — Transition

- Similarity: 0.4083
- Prediction: Over the course of these three frames, there's a clear progression in the state of the hand. Initially, the hand appears to be in a state of rest, with no visible movement. As the frame progresses, it becomes apparent that the hand is in motion, and the hand's motion is reflected in the object's surroundings. By the third frame, however, there is a noticeable shift in the hand position, with the hand still positioned in front of the object, indicating a deliberate action. This transition is marked by a gradual increase in the amount of time the hand
- Reference: Throughout the frames, the cloth undergoes a clear transformation associated with the act of squeezing out liquid. Initially held in a preparatory grip, it is then firmly wrung, which is evident from the twisting and compacting of the material. As the sequence progresses, the intensity of the squeeze lessens, and the cloth begins to unfold and relax. This indicates the end of the active wringing phase, transitioning towards the cloth being unfurled to either be used again or to dry out completely. The fabric's moisture content seems to have decreased, judging by the less saturated appearance in the final frame, which suggests that the squeezing action effectively expelled liquid from the cloth.

#### Sample 437 — Transition

- Similarity: 0.4235
- Prediction: Over the course of these three frames, the zucchini undergoes a transition from a static state to a dynamic state. Initially, it's in a state of rest, but as time progresses, it becomes more and more agitated. As the images progress, we see a change in the state of the zucchini, indicating that there's still a lot of work to be done. By the final frame, we can see that the zucchini is still in its state, and that there are still some parts of it that need to be cleaned. This transition is a reminder of
- Reference: Over the course of the three frames, the pepper pieces undergo subtle yet noticeable shifts in their position on the chopping board. Initially scattered haphazardly, they experience a minor rearrangement, possibly due to external forces or preparatory actions for the next step in the cooking process. By the third frame, human intervention is evident as a hand enters the frame, poised to pick up or move the pepper pieces, indicating the progression from preparation to active utilization of the ingredients. This sequence portrays a typical kitchen scene where ingredients are prepared and then used in the cooking process.

#### Sample 438 — Transition

- Similarity: 0.4016
- Prediction: Over the course of these three frames, there's a clear progression in the state of the stove's lighting. Initially, it's in a stable state, with no noticeable changes. As the frame progresses, the light becomes more visible, indicating that the stove has been switched on or off. By the third frame, however, there is no noticeable change in the lighting state, suggesting that there is still a noticeable difference in the setting. This progression suggests that the lighting has been turned off or switched on, implying that there has been a significant change in lighting conditions.
- Reference: The progression from the lid being firmly placed on the slow cooker to its removal indicates a series of actions typically associated with cooking. Initially, the lid rests securely, maintaining the cooking environment's temperature and pressure. As the frames advance, the lid is lifted, breaking the seal and potentially altering the cooking dynamics by releasing heat and steam. The removal of the lid signifies an interruption in the cooking process, perhaps to add ingredients, stir, or check doneness. The careful manner of the lid's removal suggests an attempt to preserve the internal cooking conditions as much as possible.

#### Sample 442 — Transition

- Similarity: 0.4676
- Prediction: Over the course of these frames, there's a clear progression in the state of the degreaser. Initially, it's in a state of repossi
- Reference: Across these frames, the degreaser transitions from a state of rest to active use and then towards rest again. Initially, the bottle is stationary, with the trigger untouched. As the frames progress, the user actuates the trigger, presumably dispensing the degreaser onto a surface. By the final frame, the motion concludes, with the trigger being released. This sequence captures the brief yet deliberate action of spraying, marked by the changing positions of the bottle and the user's finger on the trigger. Throughout this progression, the bottle remains firmly in the user's grasp, which reflects a controlled and purposeful application of the product.

#### Sample 446 — Transition

- Similarity: 0.3736
- Prediction: Over the course of these three frames, the moka pot undergoes a significant transformation from a state of rest to a functioning machine. Initially, the pot is positioned in a closed position, indicating a moment of action. As the frames progress, there is a noticeable shift in the position of the pot, suggesting a process of preparing the pot for use. By the final frame, the lid has been removed, suggesting that the pot has been placed on the stove. This transition indicates a deliberate step in the preparation of the coffee pot, which is likely a key component of
- Reference: The bottle of oil undergoes a clear transition across the three frames from being open and tilted, indicative of recent use, to being upright and in the process of being sealed. The cap, initially held aside, moves progressively closer to the bottle’s opening and finally appears to be twisted back on, with a tissue being used throughout to ensure a clean and firm grip. The hand's gestures reflect the stages of this process – from the initial alignment to the final sealing twist, portraying a routine yet careful operation of closing the bottle after use.

#### Sample 450 — Transition

- Similarity: 0.4493
- Prediction: Over the course of these frames, there's a noticeable progression in the state of the sauce. Initially, the sauce is presented as a single layer, but as the layers are spread out, it becomes more and more layered. As the frames progress, the ingredients begin to interact more closely with each other, resulting in a more cohesive whole. By the final frame, there are no discernible differences in the sauce's texture or flavor, but the overall state of its composition remains consistent throughout.
- Reference: Observing the sequence of these frames, one can trace the dynamic process of chili sprinkling. Initially, the chili pieces are densely gathered in the center, showing the starting point of the sprinkling. As the person shakes their hand, the chilis begin to disperse outward, creating a more balanced coverage over the pizza. By the final frame, the action has concluded, and there is a noticeable difference in the spread of the chilis, indicating a deliberate and careful distribution. This progression not only demonstrates the methodical application of toppings but also the ephemeral nature of the task, with the final distribution serving as a static testament to the motion that preceded it.

#### Sample 460 — Transition

- Similarity: 0.3911
- Prediction: Over the course of these three frames, there's a clear progression in the use of the kitchen utensil. Initially, it's placed in a position that's likely to be used for cooking. As the sequence progresses, the blade becomes more and more exposed to the elements, indicating that the cooking process is underway. By the end of the frames, the bristles have been removed from the blade, suggesting that the blade is still in use. This progression suggests that the kitchen is now being used as a tool for preparing food. The final frame shows a transition
- Reference: Transitioning from the initial frame to the last, the sequence displays a rapid deceleration of both hand movement and water flow. Initially, the blur and lack of clear water stream suggest a tap being swiftly turned off. As the sequence progresses, the reduction in motion blur and hand retreat reflect the decreasing flow of water, culminating in the final frame where stillness prevails. The tap, once engaged in delivering water, now stands idle, having completed the transition from active to inactive, evidenced by the absence of water flow and the calm state of the surrounding area.

#### Sample 469 — Transition

- Similarity: 0.2846
- Prediction: Over the course of these three frames, there's a clear progression in the state of the garlic cloves. Initially, they are in a state of rest, with the blades positioned on the counter. As the sequence progresses, they become more and more exposed to the action of removing them. By the final frame, the cloves have been removed from the table, indicating that they are ready to be used. This progression is a reminder of the importance of preserving food for the next step in the process.
- Reference: Starting from its initial state where it rests on the appliance, there is a gradual and evident progression in the cover's movement across the frames. Initially, slight elevation suggests the beginning of the lift. As we move to the next frame, there's clear interaction with hands surrounding and tilting it, indicating an active and deliberate action of removal. By the final frame, the cover is almost entirely lifted, showcasing the culmination of the removal process, with the motion and environment around it capturing the rapidity and fluidity of the action. The entire sequence demonstrates a steady progression from a static state to dynamic motion.

#### Sample 470 — Transition

- Similarity: 0.4234
- Prediction: Over the course of these frames, there is a clear progression in the state of the bottle. Initially, the bottle is in a state of repost, indicating a deliberate action. As the frame progresses, it becomes more apparent that the bottle has been detached from the surface and is now positioned on a flat surface. By the final frame, there appears to be a movement in the bottle's movement, suggesting a step in the process of removing it. This sequence captures a
- Reference: Over the course of the three frames, the plug undergoes a clear transition from being partially inserted in the power outlet to almost completely removed. Initially, the plug is seen in a semi-attached state, with the person’s hands positioned to start the unplugging process. As the sequence progresses, the hands are observed pulling the plug out, demonstrating more of the metal prongs in the process. By the final frame, the plug is nearly detached, signifying the end of the action. This sequence showcases a careful and deliberate movement, likely performed to disconnect the appliance without causing damage to the plug or the outlet.

#### Sample 471 — Transition

- Similarity: 0.4672
- Prediction: Over the course of these three frames, there is a clear progression in the state of the jar's packaging. Initially, it is partially sealed, with the lid closed and the contents uncovered. As the frames progress, the packaging changes to a more open state, indicating a step in the process of removing the seal. By the final frame, the seal has been removed, and the packaging is now fully sealed. The sequence captures a moment when the seal is being re-opened, with a focus on the seal's functionality.
- Reference: Over the sequence, the bag undergoes a visible transformation. Initially, it’s partially crumpled and held loosely, indicating the onset of compression. As we progress, the bag is momentarily rested on a surface, potentially to accommodate another action, and it’s more spread out, revealing its design and material. In the final stage, the bag is gripped more firmly, with the plastic material bunched together, highlighting the crumpling process nearing completion. Throughout these stages, the bag shifts from an object with a discernible pattern and shape to a more uniform, compacted form, ready for disposal.

#### Sample 476 — Transition

- Similarity: 0.4084
- Prediction: Over the progression of these three frames, there is a clear progression in the state of the cheese. Initially, the cheese is in a state of dissipation, with a tight grip on the lid. As the sequence progresses, the hand's grip changes to a more relaxed state, indicating that the cheese has been removed from the container. By the final frame, there are no discernible changes in the cheese's state, with the hand now firmly engaged in the process of discharging it. This progression is reminiscent of a phased process, where the cheese
- Reference: The progression of the salt from the shaker to the flatbread reveals a deliberate and methodical seasoning process. Initially, the salt shaker is poised to begin the action, with no salt visible in the air. As the hand commences shaking, we observe a subtle start, gradually intensifying into a more vigorous motion by the second frame, where the salt begins to emerge. By the third frame, the hand has carried out a series of shakes, evidenced by the visible grains of salt mid-descent. The sequence captures the dynamic nature of seasoning, with the shaker's angle and the hand's motion suggesting a rhythmic and controlled dispensing of the salt.

#### Sample 477 — Transition

- Similarity: 0.4209
- Prediction: Over the course of these frames, the sauce undergoes a noticeable transformation. Initially, it appears to be in a state of disintegration, but as time progresses, it becomes more and more combustible. By the final frame, there is no discernible difference in the consistency of the sauce, either in color or texture, from the first frame to the last, indicating that the sauce has been simmered for a longer period of time. This progression is indicative of a gradual change in the sauce's cooking process, with a clearer focus on the cooking process
- Reference: Observing the progression of the light in these frames depicts the ignition and stabilization of a gas burner's flame. Initially, a magenta glow indicates the initial light-up, followed by a transition to a bright blue as the flame becomes more intense and the gas combustion reaches a higher efficiency. Finally, the flame settles into a steady state, with a strong blue core and a constant outer flame, signifying a sustained and even heat source. This progression is typical for gas burners, as the color and intensity of the flame can indicate the stage of heating and the efficiency of the fuel being burned.

#### Sample 480 — Transition

- Similarity: 0.4140
- Prediction: Over the course of these three frames, there is a clear progression in the state of the contents of the bag. Initially, the bag is in a state of dislodishment, indicating that the contents are being emptied out. As the frames progress, the contents begin to appear to have been soiled, suggesting that the bag has been contaminated. By the final frame, the seal has been sealed and the contents have begun to settle. This progression is indicative of a thorough cleaning process, with the bag's contents deteriorating, suggesting the contents may have remained in the
- Reference: Over the course of the three frames, the liquid washing up undergoes a transition from containment to dispersion. Initially, it remains securely inside its container, showing no interaction with the external environment. As the moments progress, the liquid is actively dispensed, changing its state from static to dynamic, and interacts directly with the sponge. By the final frame, it has been transferred and absorbed, transforming the visual and textural state of the sponge from dry to damp. This progression showcases the utility of the liquid washing up and its intended purpose.

#### Sample 481 — Transition

- Similarity: 0.4695
- Prediction: Over the course of these three frames, there is a clear progression in the use of the utensil in the kitchen. Initially, it is being rinsed under running water, then re-rinsing, and finally, it's being washed again. The hand's motion is indicative of a thorough cleaning process, with a focus on removing any remaining residue. By the final frame, the person's hands are positioned in a circular motion, indicating that they've been thoroughly rinsed. This sequence suggests a methodical approach to rin
- Reference: The transformation of the jug across these frames is marked by the transition from emptiness to partial fulfillment. Initially poised and ready, the jug is transformed by the act of filling, its purpose gradually realized as the water level rises. The jug's role as a vessel is underscored by the visible increase in water, where each frame captures a snapshot of the sequential stages of filling, from anticipation to the action, then towards completion. The hands' subtle changes in positioning reflect a responsive and controlled approach to the task, ensuring the jug is filled efficiently and without spillage.

#### Sample 482 — Transition

- Similarity: 0.4893
- Prediction: Over the course of these three frames, the cling film undergoes a transformation from a partially untouched state to a fully-unsealed state. Initially, the film is in a state of deposition, but as it is unfolded, it begins to crack open. As the process progresses, the material becomes more and more exposed to the force of the hand, leading to the removal of the film. By the final frame, there is a clear indication that the film has been removed from its packaging, which is now fully intact and ready for use.
- Reference: Throughout the progression of these frames, there's a clear transition in the state of the meat packaging. Initially, both packages of meat were untouched and intact. As the frames progress, the lighter meat's package becomes the focus of interaction, starting from a subtle pinch or pry at its corner to a more evident attempt at opening it by the third frame. By the end of this sequence, the original sealed state of the packaging is altered, revealing a part of its contents and signifying the commencement of the unboxing process.

#### Sample 485 — Transition

- Similarity: 0.3971
- Prediction: Over the course of these three frames, the package undergoes a clear transition from being unlocked to being fully opened. Initially, the packaging is in a state of openness, but as the frame progresses, the contents begin to emerge. By the final frame, the bag has been fully opened, indicating that the package is ready to be opened. As the frames progress, there is a noticeable shift in the packaging's state of being, from a closed state to a more open state. The packaging transitions from being open to being opened, and this transition is reflected in the
- Reference: The progression of the milk's state from the first to the third frame illustrates an accidental drop. Initially, the milk is being transported, evidenced by the grip and motion blur. In the subsequent frame, it is airborne, indicating that it has been inadvertently released. By the third frame, the milk carton has landed on the floor, and the outstretched hand suggests an attempt to rectify the mistake. Throughout these frames, the milk carton's journey from a state of controlled movement to unintended release and eventual rest on the floor is captured, highlighting a brief narrative of domestic mishap.

#### Sample 490 — Transition

- Similarity: 0.4189
- Prediction: Over the course of these three frames, the package undergoes a clear transition from being untouched to being fully opened. Initially, the packaging is in a state of disintegration, but as the sequence progresses, the person's hands move and the package begins to open. By the final frame, there is no clear indication of how the package has been opened, or whether it has been properly sealed. The packaging transitions from being unopened to being partially opened, and the hand's motion indicates that the package is ready to be opened. This sequence captures the process of opening the package,
- Reference: The tortilla undergoes a noticeable transition across the three frames, driven by the careful manipulation of the hand. Initially presented as a flat, supple disc, it begins a journey back to its pack, its shape and texture remaining relatively intact. As the motion progresses, the tortilla succumbs to the forces exerted by the hand and gravity, bending and folding, altering its form. This evolution from a flat entity to a conforming, folded object encapsulates a simple, yet precise action of returning the tortilla to its storage, a mundane task executed with an everyday grace and necessity.

#### Sample 495 — Transition

- Similarity: 0.3125
- Prediction: Over the course of these three frames, there's a noticeable progression in the state of the kitchen utensil. Initially, it's in a state of partial rest, with the hand resting on the edge of the cabinet. As the frame progresses, the hand's position changes to a more relaxed position, indicating that the hand is engaged in some sort of activity. By the third frame, the knife's state is clearer and more stable, suggesting that the knife is being used for a longer period of time. The transition from a resting position to
- Reference: Throughout the sequence of images, there is a clear progression in the state of the plug as it transitions from being fully inserted to partially removed from the wall socket. Initially, the plug is firmly in place, but as the sequence progresses, a pulling force acts upon it, evidenced by the change in the angle and tension of the cord. By the final frame, the plug is only halfway engaged with the socket, and the movement suggests a deliberate action to disconnect the plug. The unplugging appears to be done with some haste or urgency, as the cord is taut and the action swift. This sequence captures the very moment of electrical disconnection, a commonplace yet crucial action in daily life.

#### Sample 497 — Transition

- Similarity: 0.3657
- Prediction: Over the course of these frames, the rolled-up taburra undergoes a noticeable change in its state. Initially, it appears to be in a state of disrepair, but as the frame progresses, it begins to show signs of cleaning. As the frames progress, it becomes apparent that the wringing cloth is being used for cleaning, and the creases in the cloth's surface are indicative of the cleaning process. By the final frame, there are no visible signs of the rinsing or drying process, and no sign of a
- Reference: Across the three frames, there's a clear progression of the glove's state in relation to the wearer's activities. Initially, the glove is engaged in holding a utensil, showcasing its dexterity. As we progress, the glove is seen interacting with different objects in the kitchen, illustrating its multifunctional use. The consistent appearance of the glove throughout the frames, without any visible degradation, emphasizes its resilience and suitability for the tasks being performed. Moreover, the changing hand positions across frames highlight the glove's flexibility and adaptability to various kitchen chores.


## Interpretation Notes

- BLEU and ROUGE-L measure lexical overlap with reference captions.
- Semantic similarity measures embedding-based caption similarity.
- Temporal alignment aggregates semantic similarity across the four stages.
- Low-similarity cases are candidates for manual review, not confirmed factual errors.
