# list+list1
# 两个列表可以用+号拼接
# list>list1 
# 只对比第一个元素 如果成立返回Ture反之亦然
# list*3  赋值并改变list*=3
# 列表中元素*三

# 123 in list 当123在list列表里为真反之亦然
# 123 not in list 当123不在list列表里为真反之亦然
# 列表中的列表中的值
# 123 in list[0] 当列表list里的列表索引0的值为123 则返回为True 反之亦然

# list[3][0] 当列表第三个元素是列表时 索引列表中的列表的第一个元素


# dir() 列举
#  list.conunt(123) 统计元素123在列表中出现的次数
#  list.index(123)  查看元素123第一个出现的位置的索引
#  list.reverse()   反转列表
#  list.sort()  使用指定方式对元素进行排序 默认为从大到小 首字母排序
#  list.sort(reverse=True)  反向为真则通过首字母倒着排序

# list.clear() 清除列表 
# list2=list.copy()  将列表copy并赋值给list2

# 列表推导式（List comprehensions）也叫列表解析
# i*i for i in range(10) i在range(10)中i*=i

# >>> list1 = [x**2 for x in range(10)] #在range(10)中x**2  
# >>> list1
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> 


# 问题：请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。
# list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]

# list1=[]
# for x in range(10):
# 	for y in range(10):
# 		if x%2==0:
# 			if y%2!=0:
# 				list1.append(x,y)


# list3=(name,kouhao)for name in list2 for kouhao in list1 if list[0]==list2[0]

# 列表的常用操作符：
# 比较：如果有多个元素，默认从第一个元素开始比较，比较对应的ASCII码值大小；
# 逻辑（and or）：
# 连接（+）：[1, 2, 3] + [4, 5, 6] 结果是 [1, 2, 3, 4, 5, 6]
# 重复（*）：['Hi!'] * 4 结果是 ['Hi!', 'Hi!', 'Hi!', 'Hi!']
# 成员关系（in 和 not in）：3 in [1, 2, 3] 结果是 True

# 列表的方法：dir(list)
# append()：在列表末尾添加新的对象
# extend()：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# count()：统计出现的次数
# index(目标，起始位置，截止位置)：返回参数在列表中的位置
# insert()：将对象插入到列表指定位置
# pop()：移除列表中的一个元素（默认最后一个元素，可指定其他的位置），并且返回该元素的值
# remove()：移除列表中某个值的第一个匹配项（不能指定位置删除）
# reverse()：翻转列表
# sort()：按照指定的方式对列表成员排序，默认则从小到大排列
# 特别的：sort(reverse=True)表示从大到小，默认为False

# 列表的内置函数：
# 比较两个列表的元素：operator.eq(list1,list2）（前提需import operator）
# 计算列表元素个数：len(list1)
# 返回列表中元素最大值：max(list1)
# 返回列表中元素最小值：min(list1)
# 将元组转换为列表：list(tuple1)
