import torch
import pickle

# 假设你已经有一个原始的 pkl 文件（ext_path）
# 读取原始数据
with open('E:\Desktop\processed_action_memory.pkl', 'rb') as f:
    data, labels = pickle.load(f)

# data 的形状是 [n, 32, 768]
# 我们将对第二维（32）进行平均
data_tensor = torch.tensor(data)  
mean_data = data_tensor.mean(dim=1)  # 对 32 维度进行平均，得到 [20, 768]

# 确保新的数据与标签配对
# 假设 labels 是一个包含 20 个标签的列表，例如 ["shooting_basketball", ...]
new_data = mean_data.numpy()  # 转换为 numpy 数组，方便保存
new_labels = labels  # 标签不变

# 保存到新的 pkl 文件
with open('E:\\Desktop\\3_action_memory.pkl', 'wb') as f:#这里的名字需要改，改成其他的文件名，防止重复
    pickle.dump((new_data, new_labels), f)

print("New data has been saved to 'your_output_file.pkl'")

