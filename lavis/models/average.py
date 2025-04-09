import torch
import pickle


with open('E:\Desktop\processed_action_memory.pkl', 'rb') as f:
    data, labels = pickle.load(f)


data_tensor = torch.tensor(data)  
mean_data = data_tensor.mean(dim=1) 

.]
new_data = mean_data.numpy()
new_labels = labels 

with open('E:\\Desktop\\3_action_memory.pkl', 'wb') as f:
    pickle.dump((new_data, new_labels), f)

print("New data has been saved to 'your_output_file.pkl'")
