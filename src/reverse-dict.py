# 反转字典
# 当我们想要反转字典的建和值的时候应该怎么做呢？

myDict = {
  'Izuku Midoriya': 'One for All',
  'Katsuki Bakugo': 'Explosion',
  'All Might': 'One for All',
  'Ochaco Uraraka': 'Zero Gravity'
}

# 1、用于反转具有唯一值的字典
# 方法思路：使用dict.item()方法将字段转为dict_items类型，可以理解为元素为元组的列表
# 而元组的项就是(key, value),通过map方法经过reversed函数，将dict_items的元组反转为(value, key)
# 最后再转为dict
myInvertedDict = dict(map(reversed, myDict.items()))
print(myInvertedDict)

# 2、用于反转具有唯一值的字典
# 方法思路：zip方法可以理解为矩阵的旋转，通过dict.values()，dict.keys()获得一个矩阵
#   [key1, key2, key3]
#   [value1, value2, value3]
# 经过zip变为
#    [value1, key1]
#    [value2, key2]
#    [value3, key3]
# 最后再转为dict
myInvertedDict2 = dict(zip(myDict.values(), myDict.keys()))
print(myInvertedDict2)


# 3、用于反转具有唯一值的字典
# 方法思路：使用推导式的方式遍历myDict.items(),获取到了key、value，构造{value:key}即可。
myInvertedDict3 = {
  value: key for key, value in myDict.items()
}
print(myInvertedDict3)

# 4、用于反转具有非唯一值的字典
# 方法思路: 使用defaultdict方法创建dict，设置dict的value的默认值为list，
# 使用推导式将值相同的key会被放在list里
from collections import defaultdict
myInvertedDict4 = defaultdict(list)
{
  myInvertedDict4[value].append(key) for key, value in myDict.items()
}
print(myInvertedDict4)

# 5、用于反转具有非唯一值的字典
# 方法思路：与4思路相同，只不过没有用到库，使用dict的setdefault方法
myInvertedDict5 = dict()
for key, value in myDict.items():
    myInvertedDict5.setdefault(value, list()).append(key)

print(myInvertedDict5)


# 6、用于反转value是列表的字典
# 方法思路：推导式一把梭，先推出key，然后通过key获取到values数组
# 然后遍历values得到每一个value，将每一个value做key，key做value
myInvertedDict6 = {
  value: key for key in myDict for value in myDict[key]
}
print(myInvertedDict6)
