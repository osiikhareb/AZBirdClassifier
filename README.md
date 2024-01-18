# AZBirdClassifier
Classification of avian species in Arizona (WIP)


***All information below is subject to change but the structure remains the same

Phase 1: Scrape

Phase 2: Organize

Phase 3: Model

Phase 4: Train

Phase 5: Deploy

Phase 6: Prettify

Phase 7: Expand




Phase 1: Scrape
- Build labeled training data set
	- Use Selenium scraper to obtain images from eBird
	- Start with select birds in Arizona; include difficult cases e.g. Falcon vs Red-Tailed Hawk, 
	Red-Tailed Hawk vs Swainsons Hawk, Crow vs Raven, etc.
	- Include static side profiles, in-flight, etc.

Phase 2: Organize
- Data cleaning possibly with FastDup or some other tool
- Perform necessary steps (transformations) beyond just obtaining images such as resizing, padding, reflecting, decolorizing, 
standardizing/scaling, etc.
- Create object-oriented classes and label images
- Program outline and pseudo code

Phase 3: Model
- Create ConvNNet model(s)
- Create Tree based ConvNNet approach if possible

Phase 4: Train
- Run model on data

Phase 5: Deploy
- Containerize program and store training data in SQL database
- Create a front end application to drag and drop images, run model, and spit out a result

Phase 6: Prettify
- OpenCV and other CV models such as YOLOv8 to extract information from videos e.g. detection, classification, and segmentation 
as well as per instance segmentation
- Use YOLOv8 or some other application to track and count objects (birds) from a video

Phase 7: Expand
- Expand training dataset to all birds of North America
