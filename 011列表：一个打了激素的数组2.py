# 从列表中获取索引值
# 列表[0] 索引从0开始
# temp=列表[0]  把列表索引值赋值给变量
# liebiao[0]=liebiao[1] 将索引0的值赋值给索引1
# liebiao[1]=temp 将temp的值赋值给列表索引1

# 从列表删除元素
# liebiao.remove('1') 删除列表中的1不需要索引
# del
# del liebiao[1] 删除列表中索引1的值(语句非函数或方法)
# del liebiao  删除整个列表
# pop()：弹栈
# liebiao.pop() 从列表取出最后一个元素并返回
# temp=liebiao.pop() 从列表取出最后一个元素并赋值给temp
# liebiao.pop(1) 从列表取出索引的值 同样可以赋值

# 列表分片[开始：结束]
# liebiao[1:3] 分片将列表索引值1到3 组成新的列表
# liebiao[:3] 从最前到3
# liebiao[1:]从一到最后一个元素
# liebiao[:]列表的拷贝
# liebiao[::-1]：完成原列表的反转

# 请问 list1[0] 和 list1[0:1] 一样吗？
# 不一样，list1[0] 返回第0个元素的值，list1[0:1] 返回一个只含有第0个元素的列表

#python支持倒数索引
# list[-3] 倒数第三个

# list[1:10] 步长默认为一
# list[0:9:2]：索引从2开始到索引8，跨步2取数
# list[::2] 不指定开始和结束分片只根据步长分片 步长不能为0 也就是不能原地踏步
# list[::-2]步长可以为负数则为倒着走

# list1=list[] 将列表赋值给list1
# list2=list   将list列表贴上list2的名字 如果列表list改变则list2也会改变

# 通过sort进行永久排序
# list.sort() 通过首字母对列表list进行排序
# list.sort(reverse=True)  反向为真则通过首字母倒着排序
