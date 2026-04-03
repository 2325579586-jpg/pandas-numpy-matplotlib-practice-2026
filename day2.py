"""
Day 2（索引与布尔选择）
使用Day1的df（重新运行一次）。
练习题：
	1	用iloc取df第2行第1列的值。
	2	用loc取“score”列。
	3	用布尔索引选出score > 85的所有行。
	4	用NumPy创建一个5x5的随机数组（rand），打印其ndim和size。
	5	用Matplotlib画柱状图：x=姓名，y=年龄。
	6	把df中age列所有值+5，生成新列age_new并打印df。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {'name':['小明','小红','小刚','小李'], 'age':[23,25,22,24], 'score':[85,92,78,88]}
df = pd.DataFrame(data)

#	1	用iloc取df第2行第1列的值。
print(df.iloc[1,0])

print("\n\n\n")
#	2	用loc取“score”列。
print(df.loc[:, 'score'])

print("\n\n\n")
#	3用布尔索引选出score > 85的所有行。
print(df[df['score'] > 85])

print("\n\n\n")
#	4	用NumPy创建一个5x5的随机数组（rand），打印其ndim和size。
a = np.random.rand(5,5)
print("矩阵：\n",a)
print("维度",a.ndim)
print("元素总数：",a.size)

print("\n\n\n")

#	5	用Matplotlib画柱状图：x=姓名，y=年龄。

#设中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.bar(df['name'], df['age'],color = 'skyblue')
plt.show()

#水平柱状图
plt.barh(df['name'], df['age'],color = 'skyblue')
plt.show()



# 6  把df中age列所有值+5，生成新列age_new并打印df。

df['age_new'] = df['age'] + 5
print(df)