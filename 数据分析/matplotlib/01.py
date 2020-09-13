from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

# 设置图片大小
plt.figure(figsize=(8,6),dpi=80)



# 绘图
plt.plot(x,y)

# 设置x轴的刻度
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::3]) # 当刻度太密集，使用切片的步长
plt.yticks(range(min(y),max(y)+1))

# 保存图片
plt.savefig("./t1.png") # 可以保存svg这种矢量图格式，放大不会有锯齿

# 展示
plt.show()