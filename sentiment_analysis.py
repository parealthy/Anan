import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
file_path = 'D://Download//用户评论（高中低端）-约26w-高端.csv'
data = pd.read_csv(file_path)

# 确保 '描述' 列没有缺失值
data = data.dropna(subset=['描述'])

# 确保所有的描述都是字符串类型
data['描述'] = data['描述'].astype(str)

# 定义情感分析函数
def analyze_sentiment_cn(text):
    s = SnowNLP(text)
    return 'Positive' if s.sentiments > 0.5 else 'Negative'

# 应用情感分析函数
data['Sentiment'] = data['描述'].apply(analyze_sentiment_cn)

# 保存更新后的数据到新的 CSV 文件
output_file_path = 'D://Download//用户评论（高中低端）-约26w-高端-分析结果.csv'
data.to_csv(output_file_path, index=False)

# 提示操作完成
print("Updated CSV file saved as:", output_file_path)

# 可视化情感分析结果
sentiment_counts = data['Sentiment'].value_counts()
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Analysis of User Comments')
plt.show()
