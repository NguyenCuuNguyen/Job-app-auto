import os
import yaml


rootdir = r'C:\Users\nguyencuu\Downloads'
#os.listdir(os.path.abspath(folders))
mapper = {}
remove_list = ["ballon", "--", "---", "normal-person", "umberella"]

label_mapper = {'aeroplane': 0, 'animal': 1, 'ant': 2, 'apple': 3, 'arm': 4, 'arrow': 5, 'baby': 6, 'ball': 7, 'balloon': 8, 'bee': 9, 'bicycle': 10, 'big-eye': 11, 'bike': 12, 'bird': 13, 'birds': 14, 'black-eye': 15, 'blood': 16, 'boat': 17, 'body': 18, 'books': 19, 'bottle': 20, 'branch': 21, 'broken family': 22, 'broken heart': 23, 'brow': 24, 'building': 25, 'bus': 26, 'butterfly': 27, 'cake': 28, 'candle': 29, 'candy': 30, 'car': 31, 'carrot': 32, 'cartoon': 33, 'castle': 34, 'cat': 35, 'center': 36, 'chair': 37, 'chicken': 38, 'child': 39, 'chimney': 40, 'circle': 41, 'clock': 42, 'cloud': 43, 'cow': 44, 'crab': 45, 'dagger': 46, 'dead body': 47, 'deadbody': 48, 'diningtable': 49, 'dog': 50, 'door': 51, 'dotted-eye': 52, 'dotted-nose': 53, 'duck': 54, 'ear': 55, 'earth': 56, 'elephant': 57, 'emphasized-eye': 58, 'eye': 59, 'eyelash': 60, 'eyes': 61, 'face': 62, 'faces': 63, 'fence': 64, 'fire': 65, 'fire_truck': 66, 'fish': 67, 'flat-facial-feature': 68, 'flower': 69, 'fly': 70, 'food': 71, 'foot': 72, 'football': 73, 'front_facing': 74, 'fruit': 75, 'fruits': 76, 'garden': 77, 'gift': 78, 'grass': 79, 'gun': 80, 'hair': 81, 'hand': 82, 'happy': 83, 'happy kid': 84, 'head': 85, 'helico': 86, 'hen': 87, 'holdingtwohands': 88, 'home': 89, 'horse': 90, 'house': 91, 'house with doors': 92, 'house with no door and window': 93, 'house withdoor and window': 94, 'hut': 95, 'i-nose': 96, 'ice cream': 97, 'insect': 98, 'joker': 99, 'kite': 100, 'leaf': 101, 'leg': 102, 'light': 103, 'lighthouse': 104, 'lion': 105, 'lyingdown': 106, 'moon': 107, 'motorbike': 108, 'mountain': 109, 'mouth': 110, 'neck': 111, 'neutral': 112, 'nose': 113, 'open-mouth': 114, 'pencil': 115, 'person': 116, 'phantom': 117, 'pig-nose': 118, 'plane': 119, 'planet': 120, 'pottedplant': 121, 'rain': 122, 'rainbow': 123, 'red blood': 124, 'river': 125, 'road': 126, 'rocket': 127, 'rocks': 128, 'roof': 129, 'root': 130, 'run': 131, 'sad': 132, 'sad faces': 133, 'sad kid': 134, 'sad kids': 135, 'scarry thing': 136, 'scary thing': 137, 'sea': 138, 'sea horse': 139, 'seat': 140, 'sheep': 141, 'ship': 142, 'shrub': 143, 'side_facing': 144, 'sit': 145, 'smoke': 146, 'snail': 147, 'snowman': 148, 'sofa': 149, 'spider': 150, 'stairs': 151, 'star': 152, 'stars': 153, 'sun': 154, 'teeth': 155, 'tooth': 156, 'tortoise': 157, 'traffic_light': 158, 'trafic-signal': 159, 'train': 160, 'tree': 161, 'tree with leave': 162, 'tree with no leave': 163, 'tree with no leaves': 164, 'truck': 165, 'tvmonitor': 166, 'u-type-facial-feature': 167, 'umbrella': 168, 'upside-down-facial-feature': 169, 'vehicle': 170, 'walk': 171, 'wave': 172, 'weapon': 173, 'wind': 174, 'window': 175}

def search_and_swap(str_row):
    sub = str_row.split(" ")
    if sub != ['']:
        print(f"r {r}")
        old_label = mapper[folders][int(sub[0])]
        print(f"mapper[folders] {mapper[folders]}")
        if old_label in label_mapper:
            new_index = label_mapper[old_label]
        else:
            if old_label == "ballon": #in ["--", "---"]:
                new_index = label_mapper["balloon"]
            elif old_label == "normal-person":
                new_index = label_mapper["person"]
            elif old_label == "umberella":
                new_index = label_mapper["umbrella"] 
    sub[0] = str(new_index)
    up_row = ' '.join(sub)
    return up_row


for folders in os.listdir(rootdir):
    if "input-" in folders:
        mapper[folders] = {}
        cur_path = os.path.join(rootdir, folders)
        for file in os.listdir(cur_path):
            sub_path = os.path.join(cur_path, file)
            if file.endswith('.yaml'):
                with open(sub_path) as f:
                    doc = yaml.safe_load(f)
                    for index, label in enumerate(doc['names']):
                        mapper[folders][index] = label 
            else:
                #get labels from Valid & train
                if os.path.isdir(sub_path):
                    for subfolder in os.listdir(sub_path):
                        if subfolder == "labels":
                            print(f"{sub_path}: {subfolder}")
                            for label in os.listdir(os.path.join(sub_path, subfolder)):
                                with open(os.path.join(sub_path, subfolder, label), "r+") as l:
                                    content = l.read()
                                    print(f"content {content}")
                                    row = content.split("\n")
                                    print(f"row {row}")

                                    for r in row:
                                        updated_row = search_and_swap(r)
                                        print(f"updated_row {updated_row}")
                                        content = content.replace(r, updated_row)
                                    print(f"updated_content {content}\n")
                                    
                                    l.seek(0)
                                    l.write(content)
                                    l.truncate()

                                    
                                        
                                                

                                            # print(f"mapper {mapper}\n--")
                                            # if "class" not in mapper[folders].keys():
                                            #     mapper[folders]["class"] = []
                                            #     mapper[folders]["x"] = []
                                            #     mapper[folders]["y"] = []
                                            #     mapper[folders]["width"] = []
                                            #     mapper[folders]["height"] = []
                                            # mapper[folders]["class"].append(sub[0])
                                            # mapper[folders]["x"].append(sub[1])
                                            # mapper[folders]["y"].append(sub[2])
                                            # mapper[folders]["width"].append(sub[3])
                                            # mapper[folders]["height"].append(sub[4])
    # print(f"final mapper {mapper}\n--")
    # if mapper != {}:
    #     exit()                    






def create_label_mapper(total_labels):
    print(f"total_labels {total_labels}")
    set_labels= [x for x in total_labels if x not in remove_list]
    set_labels = sorted(set(set_labels))
    label_mapper = {}
    for index, label in enumerate(set_labels):
        label_mapper[label] = index
    print(f"label_mapper {label_mapper}")
    return label_mapper





                    
    #         else:
    #             #get labels from Valid & train
    #             if os.path.isdir(sub_path):
    #                 for subfolder in os.listdir(sub_path):
    #                     if subfolder == "labels":
    #                         print(f"{sub_path}: {subfolder}")
    #                         for label in os.listdir(os.path.join(sub_path, subfolder)):
    #                             with open(os.path.join(sub_path, subfolder, label), "r") as l:
    #                                 content = l.read()
    #                                 row = content.split("\n")
    #                                 for r in row:
    #                                     sub = r.split(" ")
    #                                     if sub != ['']:
    #                                         print(f"mapper {mapper}\n--")
    #                                         if "class" not in mapper[folders].keys():
    #                                             mapper[folders]["class"] = []
    #                                             mapper[folders]["x"] = []
    #                                             mapper[folders]["y"] = []
    #                                             mapper[folders]["width"] = []
    #                                             mapper[folders]["height"] = []
    #                                         mapper[folders]["class"].append(sub[0])
    #                                         mapper[folders]["x"].append(sub[1])
    #                                         mapper[folders]["y"].append(sub[2])
    #                                         mapper[folders]["width"].append(sub[3])
    #                                         mapper[folders]["height"].append(sub[4])
    # print(f"final mapper {mapper}\n--")
    # if mapper != {}:
    #     exit()
