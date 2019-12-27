元组不可更换元素的列表
yuanzu=(1,2,3,4,5,6,7) 创建元组也可以不用小括号
yuanzu[1] 查看元组第一个元素
yuanzu[5:]从第5个开始到最后一个
yuanzu[:5] 从第一个到第五个
yuanzu2=yuanzu[:] 拷贝
如果你需要创建一个只有一个元素的元组
你可以这样yuanzu=(1,)
如果你这样yuanzu=(1) 这不是一个元组
8*(8)  等于64
2*(1,) 等于(1,1) 

temp=1，2，3，4
temp=temp[:2]+('8，')+temp[2:] 一共4个元素前面两个加上新元素再加后面两个组成新元组，贴上temp  
当元组temp 被当作变量名贴在另一个元组上 原temp元组由于没有标签就会被回收
del temp 删除整个temp元组

当我们希望内容不被轻易改写的时候，我们使用元组（把权力关进牢笼）。
当我们需要频繁修改数据，我们使用列表


元组固然安全，但元组一定创建就无法修改（除非通过新建一个元组来间接修改，但这就带来了消耗）
而我们人是经常摇摆不定的，所以元组只有在特殊的情况才用到，平时还是列表用的多

元组可用的方法
count() 计算并返回指定元素的数量
index() 寻找并返回参数的索引值

元组的内置函数：
比较两个元组的元素：operator.eq(temp1,temp2）（前提需import operator）
计算元组元素个数：len(temp1)
返回元组中元素最大值：max(temp1)
返回元组中元素最小值：min(temp1)
将列表转换为元组：tuple(list1)
元组的方法：
index：这个方法返回某个参数在元组中的位置
count：这个方法用来计算某个参数在元组中出现的次数

