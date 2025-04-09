import json
import os

#file_path = "/home/longma/MA-LMM/data/lvu/annotation/val.json"
file_path = "/home/longma/MA-LMM/data/msrvtt/annotation/qa_val.json"
#file_path = "/home/longma/MA-LMM/data/msvd/annotation/cap_val.json"
#file_path = "/home/longma/MA-LMM/data/msvd/annotation/qa_val.json"
#file_path = "/home/longma/MA-LMM/data/breakfast/annotation/val.json"

#base = "/home/data1/lvu_frames/"
base = "/home/data1/msrvtt_frames/"
#base = "/home/data1/breakfast"
#base = "/home/data1/msvd/"

with open(file_path, 'r') as file:
    data = json.load(file)

empty = []

for item in data:
    name = data[item]['video']
    #name = item
    if os.path.exists(os.path.join(base, name)): 
        length = len(os.listdir(os.path.join(base, name)))
        if length == 0:
            empty.append(item)
        #data[item]['num_frames'] = length
        data[item]['frame_length'] = length
    else:
        print(name)
        empty.append(item)
    
for v in empty:
    del data[v]

with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
 