import torch
import pickle

# 假设你已经加载了pkl文件中的数据
with open('E:\\Desktop\\action_memory.pkl', 'rb') as f:
    data = pickle.load(f)

# 创建一个标签列表，长度与数据列表相同
labels = ['shooting_basketball', 'shooting_basketball', 'shooting_basketball', 'shooting_basketball', 'shooting_basketball', 
          'running', 'running', 'running', 'running', 'running', 
          'swimming', 'swimming', 'swimming', 'swimming', 'swimming', 
          'jumping', 'jumping', 'jumping', 'jumping', 'jumping']

# 将所有数据转换为tensor（假设每个数据是一个一维数组，长度固定）
tensor_data = [torch.tensor(sublist) for sublist in data]

# 将tensor数据按要求转换成一个整体的tensor对象
tensor_stack = torch.stack(tensor_data)

# 输出最终结果：一个包含tensor数据和标签的格式
result = [tensor_stack, labels]

# 打印结果
print(result)

# 将结果保存为新的pkl文件
with open('E:\\Desktop\\processed_action_memory.pkl', 'wb') as f:
    pickle.dump(result, f)
