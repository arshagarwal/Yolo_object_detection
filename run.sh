pip uninstall tensorflow
pip install tensorflow=={1.14}
cd /content/Yolo_object_detection
wget -P weights https://pjreddie.com/media/files/yolov3.weights
python detect.py $1
