import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = "D://Download//用户评论（高中低端）-约26w-中端.csv"
data = pd.read_csv(file_path)

# 计算每个类别的出现次数
category_counts = data['类别'].value_counts()

# 只保留占比最高的前5个类别
top_categories = category_counts.head(5)

# 绘制这些类别的分布图
plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.index, y=top_categories.values)
plt.xticks(rotation=45)
plt.xlabel('类别')
plt.ylabel('数量')
plt.title('低端产品用户反馈类别分布')
plt.tight_layout()

# 显示图表
plt.show()