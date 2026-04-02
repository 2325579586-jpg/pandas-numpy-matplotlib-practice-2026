"""
Day 1（基础创建与查看）
小数据集（复制运行）：
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {'name':['小明','小红','小刚','小李'], 'age':[23,25,22,24], 'score':[85,92,78,88]}
df = pd.DataFrame(data)
练习题：
	1	用NumPy创建一个3行4列全为7的数组，打印shape和mean。
	2	用Pandas查看df的前3行和整体info()。
	3	用NumPy把df[‘age’]列转成数组，计算其最大值和最小值。
	4	用Matplotlib画折线图：x=姓名，y=成绩，标题“学生成绩”。
	5	把df按照score从高到低排序，保存为day1_sorted.csv（不带索引）。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {'name':['小明','小红','小刚','小李'], 'age':[23,25,22,24], 'score':[85,92,78,88]}
df = pd.DataFrame(data)

#	1	用NumPy创建一个3行4列全为7的数组，打印shape和mean。
a = np.full((3,7),7)
print(a)
print(a.shape)
print(a.mean())

print("-"*23)

#	2	用Pandas查看df的前3行和整体info()。
df_3 = df.head(3)
print(df_3)
df.info()

print("-"*23)

#	3	用NumPy把df[‘age’]列转成数组，计算其最大值和最小值。
age = np.array(df['age'])
age_max = age.max()
age_min = age.min()
print("最大年龄：",age_max)
print("最小年龄：",age_min)

print("-"*23)

#4	用Matplotlib画折线图：x=姓名，y=成绩，标题“学生成绩”。

plt.rcParams['font.sans-serif'] = ['SimHei']     # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False       # 用来正常显示负号


plt.plot(df['name'],df['score'])
plt.title("学生成绩")
plt.show()

#5	把df按照score从高到低排序，保存为day1_sorted.csv（不带索引）。

sorted_list = df.sort_values(by='score',ascending=False)
sorted_list.to_csv('day1_sorted.csv',index=False)