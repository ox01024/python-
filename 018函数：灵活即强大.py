# 函数的参数
# 形参(parameter)形式参数
# 实参(argument)实际参数
# 定义参数的变量叫形参
# 传入的参数叫实参
 
#  函数文档 
# def function(name):
# 	'这是一个函数文档'
# 	#这是一个注释
# 	print('传进来的是'name)
# function._doc_ 查看函数文档
# help(function)  help()访问也可以看到函数文档


# 关键字参数  关键字索引
# def function(x,y):
# 	print(x,y)
# function(x=1,y=2)

# 默认参数
# def function(x=1,y=2):
# 	print(x,y)
# function(x,y)
# function(x=1,y=2)
# 如果有默认参数当不传参进去也不会报错
# 也可以指定关键字参数或者顺序传参


# 收集参数    在形参前加*就成为一个收集参数
# def test(*x，y=2):
# 	print(x,y)
# 如果不加关键字传入的参数都会被收集参数收集
# 建议其他参数添加上默认参数 不容易出错
# >>> def test(*x,y=2):
# 	print(x,y)

# >>> test(5)
# (5,) 2
# >>> test(5,6,7,8)
# (5, 6, 7, 8) 2
# >>> test(5,y=6)
# (5,) 6
# >>> 

# a) 计算打印所有参数的和乘以基数（base=3）的结果
# b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。
# 答
# def Sum(*y,base=3):
# 	for i in y:
# 		Sum+=i
# 	Sum*=base
# 	print('结果是',Sum)
# 	





# for sxh in range(100,1000):
# 	b=str(sxh)[0]
# 	s=str(sxh)[1]
# 	g=str(sxh)[2]
# 	if int(b)**3+int(s)**3+int(g)**3==sxh:
# 		print('水仙花数是:',sxh)



# 统计字符串2在字符串1中出现的次数
# def findstr(str1,str2): 
# 	list1=[]  #先创建一个空列表
# 	for i in range(len(str1)): #统计字符串1一共有多长从第一个开始切片
# 		if str1[i:i+len(str2)]==str2: #统计字符串2有多长,加上第一个的索引值把字符串一切成和字符串二相同大小的片
# 			list1.append(i)           #将字符串二出现的位置索引添加到列表1里面,列表一有多长字符串二就出现了多少次
# 	print('字符串2在字符串1中出现的次数是:',len(list1))

