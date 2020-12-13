# 将两个list转为dict

columnNames = ['id', 'color', 'style']
columnValues = [1, 'red', 'bold']

# 1.使用zip函数和dict构造函数
nameToValueDict = dict(zip(columnNames, columnValues))
print('nameToValueDict', nameToValueDict)

# 2. 使用zip函数和字典推导式
nameToValueDict1 = {
    key: value for key, value in zip(columnNames, columnValues)
}
print('nameToValueDict1', nameToValueDict1)


# 3. 使用循环
nameToValueDict2 = {}
for idx in range(len(columnNames)):
    if columnNames[idx] in nameToValueDict2:
        pass
    else:
        nameToValueDict2[columnNames[idx]] = columnValues[idx]

print('nameToValueDict2', nameToValueDict2)
