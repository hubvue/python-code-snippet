# 检查list是否为空

# 1. 验证列表的长度是否为零
myList1 = list()
if len(myList1) == 0:
    print('list is empty')

# 2. 将列表直接与另外一个空列表进行比较
myList2 = list()
if myList2 == []:
    print('list is empty')


# 3. 通过类型灵活性检查列表是否为空(首选方法)
# 空列表的值为false
myList3 = list()
if not myList3:
    print('list is empty')
