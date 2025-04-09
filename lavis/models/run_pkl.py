import torch
import pickle

with open('E:\\Desktop\\action_memory.pkl', 'rb') as f:
    data = pickle.load(f)

labels = ['shooting_basketball', 'shooting_basketball', 'shooting_basketball', 'shooting_basketball', 'shooting_basketball', 
          'running', 'running', 'running', 'running', 'running', 
          'swimming', 'swimming', 'swimming', 'swimming', 'swimming', 
          'jumping', 'jumping', 'jumping', 'jumping', 'jumping']

tensor_data = [torch.tensor(sublist) for sublist in data]

tensor_stack = torch.stack(tensor_data)

result = [tensor_stack, labels]

print(result)

with open('E:\\Desktop\\processed_action_memory.pkl', 'wb') as f:
    pickle.dump(result, f)
