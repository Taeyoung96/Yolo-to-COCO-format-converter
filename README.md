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

<p align="center"><img src="https://user-images.githubusercontent.com/41863759/100314803-cfd36800-2ffa-11eb-90ed-bf821ba2de4f.png" width="400px"></p>  

#### 2. Check the absolute path in `train.txt`.  
Make sure that it points to the absolute path to the folder where the image and text files are located.  
You can easily change the path with `Text Editor`(Ubuntu 18.04) or `NotePad` (Window 10).  

<p align="center"><img src="https://user-images.githubusercontent.com/41863759/100314808-d366ef00-2ffa-11eb-96fe-f4a2d5ffadb0.png" width="600px"></p>  

#### 3. Just run the code.  
You need to provide 2 argments(essential) & 1 argments(optional).  
- path : Absolute path of train.txt  
- output : Name of the json file  
- debug : If you want to check the bounding boxes or annotation information.

When you want to make json file,  
- `python main.py --path [Absolute Path of train.txt] --output [Name of the json file]`  
- (For example)`python main.py --path /home/taeyoungkim/Desktop/Yolo-to-COCO-format-converter/tutorial/train.txt --output train`  

Or when you want to check the bounding boxes,  
- `python main.py --path [Absolute Path of train.txt] --output [Name of the json file] --debug`
- (For example)`python main.py --path /home/taeyoungkim/Desktop/Yolo-to-COCO-format-converter/tutorial/train.txt --output train --debug`  

#### Tips  
If you want to read json files more clearly, you should use `JQ`!  
- [JQ Manual](https://stedolan.github.io/jq/manual/)
- (For example) `cd output`
- `jq . train.json > train_jq.json`

## Results  

<p align="center"><img src="https://user-images.githubusercontent.com/41863759/100314819-d8c43980-2ffa-11eb-9b9b-ecadc411544a.png" width="200px"></p>  

<p align="center">Result of Json file</p>  

<p align="center"><img src="https://user-images.githubusercontent.com/41863759/100314966-217bf280-2ffb-11eb-95fc-156131d4a38e.png" width="350px"></p>  

<p align="center">On debug mode, you can check bounding boxes</p>  

<p align="center"><img src="https://user-images.githubusercontent.com/41863759/100314970-250f7980-2ffb-11eb-88e6-3c11613a69c3.png" width="700px"></p>  

<p align="center">On debug mode, you can check annotation information on terminal</p> 

## Contributors
- I created a repository by referring to [chrise96/image-to-coco-json-converter](https://github.com/chrise96/image-to-coco-json-converter).  
- **GeeJae Lee** helped to make it.

  
