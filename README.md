# LabelMe json to yolo txt converter
Convert LabelMe JSON format to YOLO text file format

This tool helps you:
- Convert from LabelMe json annotation file to Yolo text file format for training darknet.
- Visualize the bounding box from Yolo text file (txt) to image.

## 1. LabelMe json to txt:
The json format:

![plot](https://github.com/VoNhatVinh/LabelMe-Json-To-Yolo-txt-converter-/blob/main/utils/json.jpg)


The txt format:

![plot](https://github.com/VoNhatVinh/LabelMe-Json-To-Yolo-txt-converter-/blob/main/utils/txt.PNG)


### How to run
`python3 json-to-txt.py --list_dataset_file [file txt contains dataset paths] 
                        --name_file_path [file obj.names] 
                        --move_json [move json file to backup folder]`

Example: 
`python3 json-to-txt.py --list_dataset_file ./list_path.txt --name_file_path ./obj.names --move_json True`


## 2. Visualize bounding box on image from Yolo txt file:

`python3 visualize_txt_to_bbox.py --data_folder [folder contain txt and jpg] --output_folder [visualize folder]`

Example:
`python3 visualize_txt_to_bbox.py --data_folder ./data_yolo --output_folder ./visualize`
