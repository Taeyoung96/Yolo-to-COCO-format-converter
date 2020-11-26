# Yolo-to-COCO-format-converter

When you use **Yolo-model**, you might create annotation labels with [Yolo-mark](https://github.com/AlexeyAB/Yolo_mark).  
For example,  
- `obj.names` - example of list with object names  
- `train.txt` - example with list of image filenames for training Yolo model  
- `train/` - example of folder that contain images and labels
> - *.jpg : example of list of image  
> - *.txt : example of list of label  

**But, when you want to use another model(ex. efficientdet), you need another annotation format! :disappointed_relieved:**  
### This code will help you make a COCO format annotations with Yolo format!  

## How to use
### Requirements
- numpy
- OpenCV  

You can make same environment with anaconda environment.  
- `conda create -n Yolo-to-COCO python=3.8`  
- `conda activate Yolo-to-COCO`  
- `pip install numpy`  
- `pip install opencv`  

Just clone this repository.  
- `git clone https://github.com/Taeyoung96/Yolo-to-COCO-format-converter.git`  
- `cd Yolo-to-COCO-format-converter`  

### It will be easy to understand if you refer to the tutorial folder.  

When you have your own Yolo annotation format, just change a little bit!  
#### 1. Change `classes` with your own dataset.  
In `main.py`, there is a code that declare the classes. You will change this with your `obj.names`.  

<p align="center"><img src="" width="500px"></p>  

#### 2. Check the absolute path in `train.txt`.  
Make sure that it points to the absolute path to the folder where the image and text files are located.  
You can easily change the path with `Text Editor`(Ubuntu 18.04) or `NotePad` (Window 10).  

<p align="center"><img src="" width="500px"></p>  

#### 3. Just run the code.  
You need to provide 2 argments(essential) & 1 argments(optional).  
- path : Absolute ㅔath of train.txt  
- output : Name of the json file  
- debug : If you want to check the bounding boxes or annotation information.

When you want to make json file,  
`python main.py --path [Absolute Path of train.txt] --output [Name of the json file]`  
(For example)`python main.py --path /home/taeyoungkim/Desktop/Yolo-to-COCO-format-converter/tutorial/train.txt --output train`  

Or when you want to check the bounding boxes,  
`python main.py --path [Absolute Path of train.txt] --output [Name of the json file] --debug True`
`python main.py --path /home/taeyoungkim/Desktop/Yolo-to-COCO-format-converter/tutorial/train.txt --output train --debug True`  

## Results  

<p align="center"><img src="" width="500px"></p>  
<p align="center"> <Result of Json file> </p>  

<p align="center"><img src="" width="500px"></p>  
<p align="center"> <On debug mode, you can check bounding boxes> </p>  

<p align="center"><img src="" width="500px"></p>  
<p align="center"> <On debug mode, you can check annotation information on terminal> </p> 

  
