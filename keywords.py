import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常用的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

file_path = 'D://Download//用户评论（高中低端）-约26w-高端.csv'  # 替换为您的文件路径
data = pd.read_csv(file_path)
comments = data['描述'].fillna("")  # 替换NaN为空字符串

def extract_keywords(comments, keyword):
    return sum(keyword in comment for comment in comments)

keywords = ['卡顿', '延迟', '发热', '耗电', '壁纸', '主题','漂亮','好看']
keyword_counts = {keyword: extract_keywords(comments, keyword) for keyword in keywords}

plt.figure(figsize=(10, 6))
plt.bar(keyword_counts.keys(), keyword_counts.values(), color='skyblue')
plt.title('用户评论中关键词出现次数')
plt.xlabel('关键词')
plt.ylabel('出现次数')
plt.xticks(rotation=45)
plt.show()
