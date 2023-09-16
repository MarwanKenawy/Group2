# You Only Look Once
> Creating Object detection model using ***YOLOv8 ultralytics framework***
1. Step 1:
    ## Dataset collection
    > The team members collaborated in collecting data set by taking photos of coins (one, half, quart) in different environments and states
2. Step 2:
    ## Labeling
    > Each coin in the photos is labeled according to its type using **labelimg** framework and saved in *YOLO* format to be prepared for model training
3. Step 3:
    ## Model Training
    > Dataset is divided into **Training** part and **Testing** part
    >
    >Training part is used to train the model using ***YOLOv8 ultralytics framework*** an d getting *best.pt* and *last.pt* (weights) as output model
    >
    >And the Testing part is used to test the model, check on the accuracy, and validate the results