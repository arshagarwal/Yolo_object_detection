pip uninstall tensorflow
pip install tensorflow=={1.2.0rc0}
wget -P weights https://pjreddie.com/media/files/yolov3.weights
python detect.py $1
