# TFW: Annotated Thermal Faces in the Wild Dataset
The dataset contains thermal images acquired in a  controlled indoor (`c-indoor`), semi-controlled indoor (`s-indoor`), and uncontrolled outdoor (`u-outdoor`) environments. The `c-indoor` dataset was constructed using our previously  published [SpeakingFaces dataset](https://github.com/IS2AI/SpeakingFaces). The `s-indoor` and `u-outdoor` datasets were collected using the same FLIR T540 thermal camera with a resolution of 464x348 pixels, a wave-band of 7.5–14 μm, the field of view 24, and an iron color palette. The dataset was manually annotated with face bounding boxes and five point facial landmarks (the center of the right eye, the center of the left eye, the tip of the nose, the right outer corner of the mouth, the left outer corner of the mouth).

| Environment  | Subjects | Images | Labeled faces | 
|  ---:| :---: | :---: | :---: | 
| c-indoor  | 142  | 5,112  | 5,112  |
| s-indoor  | 9  | 780  | 1,748  |
| u-outdoor  | 15  | 4,090  | 9,649  |
| combined  | 147  | 9,982  | 16,509  |

Examples of annotated images:

<img src="https://github.com/IS2AI/TFW/blob/main/figures/example.png">

## Preprint
[TFW: Annotated Thermal Faces in the Wild Dataset](https://www.techrxiv.org/articles/preprint/TFW_Annotated_Thermal_Faces_in_the_Wild_Dataset/17004538)

## Video on YouTube
[TFW: Annotated Thermal Faces in the Wild Dataset](https://www.youtube.com/watch?v=YWCy_WmFNW0)

## Dowloading the repository:
```
$ git clone https://github.com/IS2AI/TFW.git
```

## Downloading the dataset 
You can download the dataset directly from [Google Drive](https://drive.google.com/file/d/1q8jfnDdCe3e-YOnoL5PIpSlkt0vamPMV/view?usp=sharing) or send a [request](https://issai.nu.edu.kz/tfw-annotated-thermal-faces-in-the-wild-dataset/) to get the access to our server. 

## Data visualization 
- To visualize the `outdoor` dataset:
```
python visualize_dataset.py --dataset PATH_TO_DATASET/TFW/train/ --set outdoor
```
```
python visualize_dataset.py --dataset PATH_TO_DATASET/TFW/test/ --set outdoor
```
```
python visualize_dataset.py --dataset PATH_TO_DATASET/TFW/val/ --set outdoor
```
- To visualize the `indoor` dataset:
```
python visualize_dataset.py --dataset PATH_TO_DATASET/TFW/train/ --set indoor
```
```
python visualize_dataset.py --dataset PATH_TO_DATASET/TFW/test/ --set indoor
```
```
python visualize_dataset.py --dataset PATH_TO_DATASET/TFW/val/ --set indoor
```
## Training
First, convert the dataset to the yolo format using the `dataset2yolo.ipynb` notebook.
Then, follow these steps to train the [YOLOv5](https://github.com/ultralytics/yolov5) models on our TFW dataset: 
1. Download the YOLOv5 repository and install the necessary packages:
```
$ git clone https://github.com/ultralytics/yolov5
$ cd yolov5
$ pip install -r requirements.txt
```
2. Download the latest models:
``` 
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
```
3. Copy our `yolov5_tfw.yaml` file into `/yolov5/data` and update paths to the training and validation sets.
4. Start the training on the TFW dataset (change the --img_size to 832 for models with the P6 output block):
```
python train.py --data data/yolov5_tfw.yaml  --cfg models/yolov5s.yaml --weights 'pretrained weights' --batch-size 64 --epochs 250 --img-size 800 
```

To train the [YOLO5Face](https://github.com/deepcam-cn/yolov5-face) models on our TFW dataset:
1. Download the YOLO5Face repository:
```
$ git clone https://github.com/deepcam-cn/yolov5-face.git
$ cd yolov5-face
```
2. If you haven't installed the necessary packages for the `YOLOv5` in the previous step, please install them.
3. Copy our `yolov5_tfw.yaml` file into `/yolov5-face/data` and update paths to the training and validation sets.
4. Start the training on the TFW dataset (change the --img_size to 832 for models with the P6 output block):
```
python train.py --data data/yolov5_tfw.yaml  --cfg models/yolov5s.yaml --weights 'pretrained weights' --batch-size 64 --epochs 250 --img-size 800 
```

## Pre-trained YOLOv5 and YOLO5Face thermal face detection models
| Model  | Backbone | c-indoor<br>AP<sub>50 | u-outdoor<br>AP<sub>50 | Speed (ms)<br>V100 b1|Params (M)|Flops (G)<br>@512x384|
|  ---:| :---: | :---: | :---: | :---: | :---: | :---: | 
| [YOLOv5n](https://drive.google.com/file/d/1PLUq7WbOWS7Ve2VKW7_WBkC3Uksje8Fx/view?usp=sharing) | CSPNet  | 100  | 97.29 | 6.16  | 1.76  | 0.99 |  
| [YOLOv5n6](https://drive.google.com/file/d/1wV9t5uH_eiy7WaHdQdWnbeEIijuDAdKI/view?usp=sharing)| CSPNet  | 100  | 95.79 | 8.18  | 3.09  | 1.02 |  
| [YOLOv5s](https://drive.google.com/file/d/1IdsdR1-qUeRo5EKQJzGQmRDi2SrMXJG5/view?usp=sharing) | CSPNet  | 100  | 96.82 | 7.20  | 7.05  | 3.91 |  
| [YOLOv5s6](https://drive.google.com/file/d/1YZX3t7cSPnWWoic7oJo86ljBQgE5PPb2/view?usp=sharing)| CSPNet  | 100  | 96.83 | 9.05  | 12.31 | 3.88 |  
| [YOLOv5m](https://drive.google.com/file/d/16TlHaA28_FBrRT8BuVPuvYp-XTzjRdOC/view?usp=sharing) | CSPNet  | 100  | 97.16 | 9.59  | 21.04 | 12.07|  
| [YOLOv5m6](https://drive.google.com/file/d/1zK51YBu1Whet7-XahQpdoQyJ8eyBn2pB/view?usp=sharing)| CSPNet  | 100  | 97.10 | 12.11 | 35.25 | 11.76|  
| [YOLOv5l](https://drive.google.com/file/d/1uBAgzmIMdKVlpO_ky9nGP0mTurRg8ADG/view?usp=sharing) | CSPNet  | 100  | 96.68 | 12.39 | 46.60 | 27.38|  
| [YOLOv5l6](https://drive.google.com/file/d/16MiFjGA_RAKDQ4U25kuz8LUqTmDn0uIq/view?usp=sharing)| CSPNet  | 100  | 96.29 | 15.73 | 76.16 | 110.2| 
| [YOLOv5n-Face](https://drive.google.com/file/d/1vXk9P3CfhUtRBGI44SqWbuiTJ7rAI4hP/view?usp=sharing) |ShuffleNetv2| 100  | 95.93 | 10.12 | 1.72 |1.36|  
| [YOLOv5n6-Face](https://drive.google.com/file/d/1B7JQkNBg598HAeL80rKV712Gy-iPnGn2/view?usp=sharing)|ShuffleNetv2| 100  | 95.59 | 13.30 | 2.54 |1.38|  
| [YOLOv5s-Face](https://drive.google.com/file/d/1mBg-nV94fDLaWJK1q9dMEaykRmLjMN4o/view?usp=sharing) | CSPNet  | 100  | 96.73 | 8.29  | 7.06  | 3.67 |  
| [YOLOv5s6-Face](https://drive.google.com/file/d/16v3Kb5omSai0pBiJv4ZoL2y5gFWloswt/view?usp=sharing)| CSPNet  | 100  | 96.36 | 10.86 | 12.37 | 3.75 |  
| [YOLOv5m-Face](https://drive.google.com/file/d/1x7fQWvlLJiH4ZoeQHNtG5MZQrPTEoCbq/view?usp=sharing) | CSPNet  | 100  | 95.32 | 11.01 | 21.04 | 11.58|  
| [YOLOv5m6-Face](https://drive.google.com/file/d/10JWlXAWDjBBWODxF3U3bLCLe-3-mmMsm/view?usp=sharing)| CSPNet  | 100  | 96.32 | 13.97 | 35.45 | 11.84|
| [YOLOv5l-Face](https://drive.google.com/file/d/1DbWZJ8awdi6QCR1gH5Tn4-tRiY_KCXIP/view?usp=sharing) | CSPNet  | 100  | 96.18 | 13.57 | 46.59 | 25.59|
| [YOLOv5l6-Face](https://drive.google.com/file/d/1TMoa2GYfMM1ptySmntN7HBPNJG5oMWnP/view?usp=sharing)| CSPNet  | 100  | 95.76 | 17.29 | 76.67 | 113.2| 

To use the pre-trained `YOLOv5` models:
  1. Download the pre-trained models from [Google Drive](https://drive.google.com/drive/folders/10ToqjavIlk5bj63zV4xgibE1L-jTEzxN?usp=sharing) and unzip inside the `yolov5` repository folder.
  2. Copy the `yolov5_tfw.ipynb` notebook into the `yolov5` repostiory folder.
  3. Open the notebook and run cells.
  
<img src="https://github.com/IS2AI/TFW/blob/main/figures/yolov5.png">  

To use the pre-trained `YOLO5Face` models:
  1. Download the pre-trained models from [Google Drive](https://drive.google.com/drive/folders/12ub57wP1hZ4tL2WH7TrUpmbvXXIdi3NU?usp=sharing) and unzip inside the `yolov5-face` repository folder.
  2. Copy the `yolo5face_tfw.ipynb` notebook into the `yolov5-face` repostiory folder.
  3. Open the notebook and run cells.
  
<img src="https://github.com/IS2AI/TFW/blob/main/figures/yolov5_face.png">  
  
## Demo
  <img src="https://github.com/IS2AI/TFW/blob/main/figures/demo.gif">  
  
## In case of using our dataset and/or pre-trained models, please cite our work:
  ```
@article{Kuzdeuov2021,
author = "Askat Kuzdeuov and Dana Aubakirova and Darina Koishigarina and Hüseyin Atakan Varol",
title = "{TFW: Annotated Thermal Faces in the Wild Dataset}",
year = "2021",
month = "11",
url = "https://www.techrxiv.org/articles/preprint/TFW_Annotated_Thermal_Faces_in_the_Wild_Dataset/17004538",
doi = "10.36227/techrxiv.17004538.v1"
}
  ```
