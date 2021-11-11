# TFW: Annotated Thermal Faces in the Wild Dataset
The dataset contains thermal images acquired in indoor (controlled) and outdoor (uncontrolled) environments. The indoor dataset was constructed using our previously  published [SpeakingFaces dataset](https://github.com/IS2AI/SpeakingFaces). The outdoor dataset was collected using the same FLIR T540 thermal camera with a resolution of 464x348 pixels, a wave-band of 7.5–14 μm, the field of view 24, and an iron colour palette. The dataset was manually annotated with face bounding boxes and five point facial landmarks (the centre of the right eye, the centre of the left eye, the tip of the nose, the right outer corner of the mouth, the left outer corner of the mouth).

| Environment  | # subjects | # images | # labelled faces | 
|  ---:| :---: | :---: | :---: | 
| Indoor  | 142  | 5,112  | 5,112  |
| Outdoor  | 15  | 4,090  | 8,950  |
| Total  | 145  | 9,202  | 14,062  |

Examples of annotated images:

<img src="https://github.com/IS2AI/TFW/blob/main/figures/example.png">

## Setup and Requirements

## Downloading the dataset 
The dataset can be downloaded after signing a consent form.

## Data visualization 
- To visualize the `outdoor` dataset:
```
python visualize_dataset.py --dataset dataset/TFW/train/ --set outdoor
```
```
python visualize_dataset.py --dataset dataset/TFW/test/ --set outdoor
```
```
python visualize_dataset.py --dataset dataset/TFW/val/ --set outdoor
```
- To visualize the `indoor` dataset:
```
python visualize_dataset.py --dataset dataset/TFW/train/ --set indoor
```
```
python visualize_dataset.py --dataset dataset/TFW/test/ --set indoor
```
```
python visualize_dataset.py --dataset dataset/TFW/val/ --set indoor
```
## Training

## Pre-trained YOLOv5 and YOLO5Face models
