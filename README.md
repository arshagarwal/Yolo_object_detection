# Yolo_object_detection
## Here are the results produced when you run the code on "Sample_dataset" provided in the repository.
![detected image](https://github.com/arshagarwal/Yolo_object_detection/blob/master/Sample_results/check.jpg)
![detected image 2](https://github.com/arshagarwal/Yolo_object_detection/blob/master/Sample_results/dog.jpg)
## Yolov3 in Tensorflow
This project is based on the algorithm proposed in the paper **Yolov3: An Incremental Improvement** [Yolov3](https://arxiv.org/abs/1804.02767).

## The code can be run locally to perform **Object detection** on custom dataset by performing the following steps:

1. Open terminal, and execute `git clone https://github.com/arshagarwal/Yolo_object_detection.git` or alternatively you can clone the repo by clicking the "code"button on the repositiory's main page.
2. Run the command `wget -P weights https://pjreddie.com/media/files/yolov3.weights` to download the official weights.
3. After cloning the directory navigate to the directory where the code is saved using the `cd` command.
4. Perform detection using `python detect.py data_path` where data_path is a string that gives the path to the directory which contains the images on which object detection is to be performed. For ex if you want to run the code on **Sample_dataset** provided in the repo, use the code `python detect.py Sample_dataset`.

#### Note: This might have thrown `AttributeError: module 'tensorflow' has no attribute 'placeholder'` this is because this code makes use of methods which are deprecated in tensorflow version 2.2.0.To fix this run `!pip uninstall tensorflow`,then run `!pip install tensorflow=={1.14}`.
5. The results obtained after performing **Object Detection** gets stored in **results** directory which in turn is in the same directory 
where your code was cloned.



## The code can also be run on google colab by performing the following steps:
0. `!pip uninstall tensorflow`, Then run `!pip install tensorflow=={1.14}`, to use tensorflow1.14 instead of tensorflow2.2.
1. Clone the repsoitory using `!git clone https://github.com/arshagarwal/Yolo_object_detection.git`.
2. Run `cd /content/Yolo_object_detection` to navigate to the project's working directory.
3. Run the command `!wget -P weights https://pjreddie.com/media/files/yolov3.weights` to download the official weights.
4. Run the command `!python detect.py data_path` where data_path is a string that gives the path to the directory which contains the images on which object detection is to be performed. For ex if you want to run the code on **Sample_dataset** provided in the repo, use the code `!python detect.py Sample_dataset`.
5. The results obtained after performing **Object Detection** gets stored in **results** directory which in turn is in the same directory 
where your code was cloned.

## The results can be saved locally on your computer by perfoming the following steps:
1. Create a zip file by running the code `Code to be added soon`
2. Download file by running `Code to be added soon`

## If this is too overwhelming run the following code in the terminal (Shortcut):
`bash run.sh data_path` where **data_path** is a string that denotes the path where the dataset on which **Object detection** is to be performed is stored.

## Shortcut for google colab
`!bash run.sh data_path` where **data_path** is a string that denotes the path where the dataset on which **Object detection** is to be performed is stored.

