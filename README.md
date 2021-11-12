# TFW: Annotated Thermal Faces in the Wild Dataset
The dataset contains thermal images acquired in `indoor` (controlled) and `outdoor` (uncontrolled) environments. The indoor dataset was constructed using our previously  published [SpeakingFaces dataset](https://github.com/IS2AI/SpeakingFaces). The outdoor dataset was collected using the same FLIR T540 thermal camera with a resolution of 464x348 pixels, a wave-band of 7.5–14 μm, the field of view 24, and an iron color palette. The dataset was manually annotated with face bounding boxes and five point facial landmarks (the center of the right eye, the center of the left eye, the tip of the nose, the right outer corner of the mouth, the left outer corner of the mouth).

| Environment  | # unique subjects | # images | # labelled faces | 
|  ---:| :---: | :---: | :---: | 
| Indoor  | 142  | 5,112  | 5,112  |
| Outdoor  | 15  | 4,090  | 8,950  |
| Total  | 145  | 9,202  | 14,062  |

Examples of annotated images:

<img src="https://github.com/IS2AI/TFW/blob/main/figures/example.png">

## Dowloading the repository:
```
$ git clone https://github.com/IS2AI/TFW.git
```

## Downloading the dataset 
Please sign a consent form to download the dataset.

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
To train the [YOLOv5](https://github.com/ultralytics/yolov5) models on our TFW dataset: 
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
3. Copy our `yolov5_thermalface.yaml` file into `/yolov5/data` and update paths to the training and validation sets.
4. Start the training on the TFW dataset (change the --img_size to 832 for models with the P6 output block):
```
python train.py --data data/yolov5_thermalface.yaml  --cfg models/yolov5s.yaml --weights 'pretrained weights' --batch-size 64 --epochs 250 --img-size 800 
```

To train the [YOLO5Face](https://github.com/deepcam-cn/yolov5-face) models on our TFW dataset:
1. Download the YOLO5Face repository:
```
$ git clone https://github.com/deepcam-cn/yolov5-face.git
$ cd yolov5-face
```
2. If you haven't installed the necessary packages for the `YOLOv5` in the previous step, please install them.
3. Copy our `yolov5face_thermalface.yaml` file into `/yolov5-face/data` and update paths to the training and validation sets.
4. Start the training on the TFW dataset (change the --img_size to 832 for models with the P6 output block):
```
python train.py --data data/yolov5face_thermalface.yaml  --cfg models/yolov5s.yaml --weights 'pretrained weights' --batch-size 64 --epochs 250 --img-size 800 
```

## Pre-trained YOLOv5 and YOLO5Face thermal face detection models
| Model  | Backbone | Indoor<br>AP<sub>50 | Outdoor<br>AP<sub>50 | Speed (ms)<br>V100 b1|Params(M)|Flops(G)<br>512x384|
|  ---:| :---: | :---: | :---: | :---: | :---: | :---: | 
| [YOLOv5n](https://drive.google.com/file/d/1liLw59L1L56VJn7KQAHpWMIEuXdN62Yp/view?usp=sharing) | CSPNet  | 100  | 92.9 | 6.16  | 1.76  | 0.99 |  
| [YOLOv5n6](https://drive.google.com/file/d/1UpnnmCRP6rbszu5-sbbeOVTDrqbt1PPo/view?usp=sharing)| CSPNet  | 100  | 93.3 | 8.18  | 3.09  | 1.02 |  
| [YOLOv5s](https://drive.google.com/file/d/10CfN8-IkJhRC2TuPvTrQvA8VwkQupNn7/view?usp=sharing) | CSPNet  | 100  | 91.6 | 7.20  | 7.05  | 3.91 |  
| [YOLOv5s6](https://drive.google.com/file/d/1EP61OMgnAQZghfbOgxjKdcOkYrJyBmFK/view?usp=sharing)| CSPNet  | 100  | 92.6 | 9.05  | 12.31 | 3.88 |  
| [YOLOv5m](https://drive.google.com/file/d/1_4WbN7tCxwhiVgXw718ZBy-DhoxdZIay/view?usp=sharing) | CSPNet  | 100  | 90.9 | 9.59  | 21.04 | 12.07|  
| [YOLOv5m6](https://drive.google.com/file/d/1N8uDiFko_MlVUEGYYwS3VuJT9_5qQw6T/view?usp=sharing)| CSPNet  | 100  | 94.0 | 12.11 | 35.25 | 11.76|  
| [YOLOv5l](https://drive.google.com/file/d/163sCBcGbYNeekZ6KG6iSCDsHolajfu_B/view?usp=sharing) | CSPNet  | 100  | 91.3 | 12.39 | 46.60 | 27.38|  
| [YOLOv5l6](https://drive.google.com/file/d/1D_RvIdaBiqXpmtPRFglkbL5kYKY3dNfZ/view?usp=sharing)| CSPNet  | 100  | 92.7 | 15.73 | 76.16 | 110.2| 
| [YOLOv5n-Face](https://drive.google.com/file/d/1bYJWvI0OJ5evPCVmv0upOAsyld264jV_/view?usp=sharing) |ShuffleNetv2| 100  | 92.3 | 10.12 | 1.72 |1.36|  
| [YOLOv5n6-Face](https://drive.google.com/file/d/1fP0Wi9JQgSGxJDXckyrbAfTHHdFpbKT-/view?usp=sharing)|ShuffleNetv2| 100  | 91.5 | 13.30 | 2.54 |1.38|  
| [YOLOv5s-Face](https://drive.google.com/file/d/1MoUg4r1MCg2qCpnlW9CkTCZpLrBPnWEE/view?usp=sharing) | CSPNet  | 100  | 92.0 | 8.29  | 7.06  | 3.67 |  
| [YOLOv5s6-Face](https://drive.google.com/file/d/1qphk4AInYLhJktO6wlvgvL45XdS1YilE/view?usp=sharing)| CSPNet  | 100  | 94.1 | 10.86 | 12.37 | 3.75 |  
| [YOLOv5m-Face](https://drive.google.com/file/d/1TcbM9CbwsOVNdapFGrR4lHQ8J2s63_6z/view?usp=sharing) | CSPNet  | 100  | 92.2 | 11.01 | 21.04 | 11.58|  
| [YOLOv5m6-Face](https://drive.google.com/file/d/1aFzJoW_X03fN7NRRv1rZPkc4_cFwYUDI/view?usp=sharing)| CSPNet  | 100  | 94.4 | 13.97 | 35.45 | 11.84|
| [YOLOv5l-Face](https://drive.google.com/file/d/1bS_7ZTYDa6KJH1d6oLSZnumIfJU55ZMH/view?usp=sharing) | CSPNet  | 100  | 91.9 | 13.57 | 46.59 | 25.59|
| [YOLOv5l6-Face](https://drive.google.com/file/d/193sqIhipesvrcg1YN9G3_jSdFbjw4eJp/view?usp=sharing)| CSPNet  | 100  | 93.2 | 17.29 | 76.67 | 113.2| 

To use the pre-trained `YOLOv5` models:
  1. Download the pre-trained models from [Google Drive](https://drive.google.com/drive/folders/1W3UXstwJwyIBOJ4wfOgh4zW2G8qkqFzm?usp=sharing) and unzip inside the `yolov5` repository folder.
  2. Copy the `yolov5_tfw.ipynb` notebook into the `yolov5` repostiory folder.
  3. Open the notebook and run cells.
  
<img src="https://github.com/IS2AI/TFW/blob/main/figures/yolov5.png">  

To use the pre-trained `YOLO5Face` models:
  1. Download the pre-trained models from [Google Drive](https://drive.google.com/drive/folders/1FgtfBqMsydm7TugHFze9Bzd7Xc9kjOUp?usp=sharing) and unzip inside the `yolov5-face` repository folder.
  2. Copy the `yolo5face_tfw.ipynb` notebook into the `yolov5-face` repostiory folder.
  3. Open the notebook and run cells.
  
<img src="https://github.com/IS2AI/TFW/blob/main/figures/yolov5_face.png">  
  
## Demo
  <img src="https://github.com/IS2AI/TFW/blob/main/figures/demo.gif">  
  
## In case of using our dataset and/or pre-trained models, please cite our work:
  ```
  @misc{https://doi.org/10.48333/s13m-ca44,
  doi = {10.48333/S13M-CA44},
  url = {https://github.com/IS2AI/TFW},
  author = {Kuzdeuov, Askat and Aubakirova, Dana and Koishigarina, Darina and Varol, Huseyin Atakan},
  keywords = {FOS: Computer and information sciences},
  language = {en},
  title = {TFW: Annotated Thermal Faces in the Wild Dataset},
  publisher = {Institute of Smart Systems and Artificial Intelligence},
  year = {2021}
}
  ```
