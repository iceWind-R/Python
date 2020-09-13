import numpy as np
import collections as c

data1 = [
    [154,1],
    [126,2],
    [70,2],
    [196,2],
    [161,2],
    [371,4]
]

print("普通切片：",data1[0][0])


data2 = np.array( # numpy的创建数组，比起默认数组分片更容易
    [
        [154,1],
        [126,2],
        [70,2],
        [196,2],
        [161,2],
        [371,4]
    ]
)

print("numpy切片：",data2[1,0])

# 输入值
feature = data2[:,0] # numpy提取所有

# 结果rebel
label = data2[:, -1] # 从后面取倒数第一列

# 设置预测点
predictPoint = 200

# 利用map()映射函数，和lambda表达式，求得feature中每个元素与200的绝对值
distance = list(map(lambda x : abs(predictPoint - x), feature))

# 排序
# np.sort(distance) # 不合适，直接在原数组中排序

# 选用下列排序方法，得到的结果是位置的序列
sortIndex = np.argsort(distance) # [3 4 0 1 2 5]

# 用排序的下标来操作label集合
sortedLabel = label[sortIndex] # 直接在[]中写入下标，即可得到结果 [2 2 1 2 2 4]
# knn算法的 k 取 最近的 3 个邻居
k = 3

#           最受欢迎的 1 个，得到以（元素，次数）为元素的列表，第 0 个元素，得到元组
print(c.Counter(sortedLabel[0:k]).most_common(1)[0][0])


# 封装函数
def knn(k, predictPoint, feature, label):
    distance = list(map(lambda x: abs(predictPoint - x), feature))
    sortIndex = np.argsort(distance)
    sortedLabel = label[sortIndex]
    return c.Counter(sortedLabel[0:k]).most_common(1)[0][0]

if __name__ == '__main__':
    print('函数执行knn:',end='')
    print(knn(k, predictPoint, feature, label))

    # 读取文件内的数据 data0.csv (注意：此文件名为逗号分隔值文件)
    data = np.loadtxt("data0.csv",delimiter=",",encoding='UTF-8') # 加载文件，第二参数为分隔符为 ','
    feature = data[:, 0]  # numpy提取所有

    # 结果rebel
    label = data[:, -1]  # 从后面取倒数第一列
    print(data)
    print(knn(k, predictPoint, feature, label))