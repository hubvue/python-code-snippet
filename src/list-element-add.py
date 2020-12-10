# 两个列表的元素合并


# 1. 使用+运算符手动合并两个列表
# 方法思路：不用多说了
ethernetDevices = [1, [7], [2], [8374163], [84302738]]
usbDevices = [1, [7], [1], [2314567], [0]]

allDevices = [
  ethernetDevices[0] + usbDevices[0],
  ethernetDevices[1] + usbDevices[1],
  ethernetDevices[2] + usbDevices[2],
  ethernetDevices[3] + usbDevices[3],
  ethernetDevices[4] + usbDevices[4]
]

# 也可以这样写
allDevices1 = []

for i in range(len(ethernetDevices)):
  allDevices1.append(ethernetDevices[i] + usbDevices[i])

# 也可以使用推导式
allDevices2 = [ethernetDevices[i] + usbDevices[i] for i in range(len(ethernetDevices))]


# 2. 使用zip函数
allDevices3 = [x + y for x, y in zip(ethernetDevices, usbDevices)]

# 使用sum简化x + y
def sum(a: int, b: int):
  return a + b

allDevices4 = [sum(x, y) for x, y in zip(ethernetDevices, usbDevices)]


# 3. 使用map方法
import operator
allDevices5 = list(map(operator.add, ethernetDevices, usbDevices))
# print(allDevices5)



# change---实现merge方法，多个list相加

def merge(row1, row2, *rows):
  master = [x + y for x, y in zip(row1, row2)]
  for row in rows:
    master = [x + y for x, y in zip(master, row)]
  
  return master

print(merge(ethernetDevices,ethernetDevices,ethernetDevices,ethernetDevices,ethernetDevices))