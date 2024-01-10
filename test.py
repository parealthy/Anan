
from snownlp import SnowNLP

text = ["手机发热发烫那么严重，一点散热都不做是吧，无语死了",
        "房间很冷，冬天根本没法住",
        "房间很凉爽",
        "质量不太好",
        "真是漂亮极了"]


for sentence in text:
    print("正面" if SnowNLP(sentence).sentiments > 0.5 else "负面")



