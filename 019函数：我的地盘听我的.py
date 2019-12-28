# 函数和过程
# 函数(function):有返回值
# 过程(procedure):简单的特殊的并且没有返回值的
# python严格来说只有函数没有过程




# 返回值  
# 返回值可以是一个int类型，可以返回一个列表，可以返回一个元组


# 局部变量(local variable)
# 全局变量(Global variable)

# 函数中的定义的变量均为局部变量
# 函数外定义的变量都是全局变量
# 可以在函数里调用全局变量(不会改变全局变量,如果再函数中修改全局变量会创建一个同名的局部变量)
# 不可以再函数外调用局部变量




我的回文联
def hwl(i):
	sum=0
	for x in range (len(i)//2):  #回文联计算相同的字符有几对 迭代
		if i[x]==i[-(x+1)]:      #从第一个开始和最后一个开始对比
			sum+=1               #每一对相同加一
			if sum==len(i)//2:   #把对比出的相同的对数和回文联相同的对数对比
				print(i,'是回文联')
			else:
				print(i,'不是回文联')


# 网上的
# def palindrome(string):
#     list1 = list(string)  #把字符串变成列表
#     list2 = reversed(list1) #将列表翻转
#     if list1 == list(list2):  #如果翻转的列表等于原来字符串生成的列表
#         return '是回文联'
#     else:
#         return '不是回文联'

# print(palindrome('1234abcdedcba4321'))


def coonunt(*st1):
	changdu=len(st1)  #收集参数序列长度
	for x in range (changdu): #从收集参数序列列第一个开始迭代
		zimu=0 
		kong=0
		shuzi=0
		null=0
		for srt in st1[x]: #从收集参数序列的第一个字符开始迭代
			if srt.isalpha(): #如果是字母字母变量+1
				zimu+=1
			elif srt.isspace(): #如果是空kong变量加一
				kong+=1
			elif srt.isnumeric(): #如果是数字shuzi变量加一
				shuzi+=1
			else:                 #都不是其他字符加一
				null+=1
		print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个'%(x+1,zimu,shuzi,kong,null)) #第一个for迭代一次打印一次