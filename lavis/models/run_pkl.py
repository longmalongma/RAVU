import torch
import pickle
import json


def convert_to_serializable(obj):
    if isinstance(obj, torch.Tensor):
        return obj.tolist()  
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    else:
        return obj  


with open('E:\Desktop\processed_action_memory.pkl', 'rb') as f:
    data = pickle.load(f)


data_serialized = convert_to_serializable(data)


with open('E:\Desktop\processed_action_memory.txt', 'w') as f:
    json.dump(data_serialized, f, indent=4)  

print("Finish！")
