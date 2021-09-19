import os
import cv2
import numpy as np
import argparse
import shutil

def visualize_annotation(args):
    input_folder = args.data_folder
    output_folder = args.output_folder

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.mkdir(output_folder)

    for file in os.listdir(input_folder):
        if file.split(".")[-1] in "txt":
            txt_file = open(os.path.join(input_folder, file),'r')
            lines = txt_file.readlines()
            img = cv2.imread(os.path.join(input_folder, file[:-3]+'jpg'))
            img_hei, img_wid = img.shape[:2]

            for line in lines:
                sample = line.split(' ')
                if len(sample) < 1:
                    break

                data = np.array(list(map(float,sample)),dtype= float)
                class_ID = data[0]
                x_center = data[1] * img_wid 
                y_center = data[2] * img_hei
                wid = data[3] * img_wid 
                hei = data[4] * img_hei
                x1, x2 = x_center - wid/2, x_center + wid//2
                y1, y2 = y_center - hei//2, y_center +hei//2

                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
                cv2.putText(img, str(int(class_ID)), (int(x1),int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), lineType=cv2.LINE_AA) 
            cv2.imwrite(os.path.join(output_folder, file[:-3]+'png'),img)



def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data_folder', default='./dataset', help='dataset folder',type=str,)
    parser.add_argument('--output_folder', default='./visualize', help="output image folder")
    args = parser.parse_args()

    visualize_annotation(args)
    print("Visualize Successfully")

if __name__ == '__main__':
    main()