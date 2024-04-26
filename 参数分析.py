from pathlib import Path

import matplotlib.pyplot as plt


def show_table(data):
    # 创建表格
    fig, ax = plt.subplots()

    # 关闭坐标轴
    ax.axis('off')

    # 绘制表格
    table = ax.table(cellText=data, loc='center')

    # 设置表格样式
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.5, 1.5)  # 调整表格大小

    plt.show()


dir = Path('M:\\out')

print(list(dir.glob('*.json')))

