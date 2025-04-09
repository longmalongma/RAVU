import torch
import pickle

with open('/home/longma/MA-LMM/ext_data/ext_memory_lvis.pkl', 'rb') as f:
    data = pickle.load(f)

tensor, name = data

print(tensor.shape)
