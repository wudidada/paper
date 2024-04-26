import random
from collections import Counter

import matplotlib
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'


def test(key, title, size=1024*1024):
    cipher = ChaCha20.new(key=key)
    data = bytearray(size)

    encrypted = cipher.encrypt(data)

    # 使用Counter来计数每个值的出现次数
    byte_counts = Counter(encrypted)

    # 准备数据用于绘图
    values = range(256)
    counts = [byte_counts[val] for val in values]

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(values, counts, width=1.0, edgecolor='black')
    plt.xlabel('字节值')
    plt.ylabel('出现频率')
    plt.title(title)
    plt.xlim(-0.5, 255.5)  # 设置x轴范围以覆盖所有可能的字节值
    plt.grid(axis='y', linestyle='--')

    plt.savefig(title + '.png')


    # 显示图像
    plt.show()
    return encrypted

    # 保存图像


key = bytearray(32)
data1 = test(key, '密钥1生成的字节流分布')

# 生成末尾为1的密钥
key[-1] = 1
data2 = test(key, '密钥2生成的字节流分布')

# 测试两个字节流数据相同的比率
same = sum([1 for i in range(len(data1)) if data1[i] == data2[i]]) / len(data1)
print('两个字节流数据相同的比率:', same)
