pip uninstall tensorflow
pip install tensorflow=={1.14}
git clone https://github.com/arshagarwal/Yolo_object_detection.git
cd /content/Yolo_object_detection
wget -P weights https://pjreddie.com/media/files/yolov3.weights
python detect.py $1