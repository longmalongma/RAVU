import torch
import pickle
import json

# 递归转换Tensor为可序列化格式
def convert_to_serializable(obj):
    if isinstance(obj, torch.Tensor):
        return obj.tolist()  # Tensor 转换为列表
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    else:
        return obj  # 对于其他类型，直接返回

# 加载.pkl文件
with open('E:\Desktop\processed_action_memory.pkl', 'rb') as f:
    data = pickle.load(f)

# 将复杂类型转换为可序列化格式
data_serialized = convert_to_serializable(data)

# 将数据写入txt文件
with open('E:\Desktop\processed_action_memory.txt', 'w') as f:
    json.dump(data_serialized, f, indent=4)  # 使用 JSON 格式保存，增加可读性

print("数据已成功转化为 txt 格式并保存！")
