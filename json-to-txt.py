import json
import os
import argparse
import shutil

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
def read_name_file(name_path):
    names= []
    with open(name_path, "r") as name_file:
        for name in name_file:
            names.append(name.replace("\n", "").strip())
    return names

def json_to_txt(args):
    list_path = read_name_file(args.list_dataset_file)
    names = read_name_file(args.name_file_path)
    is_move = args.move_json
    if is_move:
        if os.path.exists("./json_backup/"):
            shutil.rmtree("./json_backup/")
        os.mkdir("./json_backup/")
        json_backup = "./json_backup/"
        
    for path in list_path:
        flag = False
        for f in (os.listdir(path)):
            if (f.split('.')[-1] in ["json"]):
                flag = True
                txt_name = f.rstrip(".json") + ".txt"
                txt_outpath = os.path.join(path, txt_name)
                txt_outfile = open(txt_outpath, "a")

                js = json.load(open(os.path.join(path, f)))

                for item in js["shapes"]:
                    label = item["label"]
                    for i, name in enumerate(names):
                        if label == name:
                            cls = str(i)

                    point = item["points"]
                    x1 = point[0][0]
                    y1 = point[0][1]
                    x2 = point[1][0]
                    y2 = point[1][1]

                    xmin = min(x1,x2)
                    xmax = max(x1,x2)
                    ymin = min(y1,y2)
                    ymax = max(y1,y2)

                    height = js["imageHeight"]
                    width = js["imageWidth"]
                    b = (xmin, xmax, ymin, ymax)
                    bb = convert((width,height), b)

                    txt_outfile.write(cls + " " + " ".join([str(a) for a in bb]) + '\n')
                
                if flag and is_move:
                    os.rename(os.path.join(path, f), os.path.join(json_backup,f))	#move json file to backup folder   

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--list_dataset_file', default='./dataset.txt',help='input dataset paths with annotated files',type=str,)
    parser.add_argument('--name_file_path', default='./obj.names',help='input the object name file path',type=str,)
    parser.add_argument("--move_json", default=True, help = "move json file to json backup folder", type=bool)
    args = parser.parse_args()

    json_to_txt(args)

if __name__ == '__main__':
    main()