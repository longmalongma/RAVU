
from packaging import version
import numpy as np
import torch
#from torch.cuda.amp import autocast as autocast
import torch.nn as nn
'''
import pickle
import faiss
import re
import transformers
'''
from PIL import Image
from torchvision import transforms

#import requests
#from io import BytesIO

def load_and_preprocess_image(image_path, img_size=224):
    image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = preprocess(image).unsqueeze(0)  # 增加batch维度
    return image.to(device)

image_path = "path_to_your_image.jpg"  # 替换为实际路径
image_tensor = load_and_preprocess_image(image_path)

print("image_embeds shape:", image_tensor.shape)
'''
def save_tensor_to_txt(tensor, filename):
    # 将 tensor 转换为 numpy 数组，方便写入到文本文件
    np_array = tensor.cpu().numpy()  # 转换为 CPU 上的 numpy 数组（避免在 GPU 上操作）
    
    with open(filename, 'w') as f:
        # 将 numpy 数组的每行写入到文本文件
        for row in np_array.reshape(-1, np_array.shape[-1]):  # 将高维张量扁平化成二维
            # 写入每一行，使用空格分隔
            f.write(' '.join(map(str, row)) + '\n')

# 保存 tensor 到 txt 文件
save_tensor_to_txt(image_tensor, 'image_embeds.txt')
print("Tensor has been saved to image_embeds.txt")
'''