# YOLOv3 - CS5990_Project

CS5990 Deep Learning project to detect custom objects [using pre-trained weights and/or training a model with a specific dataset]

## Getting Started

These instructions will giude to get a copy of the project running and provide information on how to customize your run for custom object detection.

### Prerequisites

In order to run or train a model below packages are required* (Additional pagkage may required based on your current system configuration). Additionally to create labeled dataset on image for custom object detection, [LabelImage](https://github.com/tzutalin/labelImg) will be a useful repository.

```
Python3
Keras
matplotlib
opencv-python
pip
tensorflow (>= 1.12.0)
```

### One time setup

First, clone this repository.

```
git clone https://github.com/nambvp03/yolov3_keras.git
```

Download pre-trained weights with COCO dataset available on official [YOLO](https://pjreddie.com/darknet/yolo/) website.

```
#YOLOv3
wget https://pjreddie.com/media/files/yolov3.weights

#YOLOv3 tiny
wget https://pjreddie.com/media/files/yolov3-tiny.weights
```


## Running YOLOv3 object detection algorithm

As in this project we are using Keras, so before running algorithm to detect object we need to generate keras model based on darknet model.

### Generate Keras model.

YOLOv3 version model
```
python3 convert.py yolov3.cfg yolov3.weights model_data/yolov3.h5
```
YOLOv3 tiny version model
```
python3 convert.py yolov3-tiny.cfg yolov3-tiny.weights model_data/yolov3-tiny.h5
```

### Running object detection

Based on your requirement update 'model_path' param in [yolo.py](yolo.py) with path of original model or tiny model. Also update 'anchor_path' too before running object detection. There are two varient to execute object detection -- one for image and othe for video input.

```
#Image input
python3 yolo_video.py --image

#Image input
python3 yolo_video.py --input test_vdo.mp4
```

## Train a model on custom dataset

Add additional notes about how to deploy this on a live system

## Output

* Tested using a model trained on COCO dataset.
![Laptop](test_laptop_1_res.jpg)
* Tested using a model trained on custom dataset of fire extinguisher.
![Fire Extinguisher](test_fire_2_res.jpg)

## Authors

* [**Bhargav Parekh**](https://github.com/nambvp03) CS5990 Deep Learning project


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [pjreddie](https://github.com/pjreddie/darknet) for algorithm in darknet
* [LabelImage](https://github.com/tzutalin/labelImg) for amazing image labeling software
* [qqwweee](https://github.com/qqwweee/keras-yolo3) for converting cfg to model in python
