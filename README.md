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

