# while 循环

# while 条件: 
# 	循环体

# 条件为真就会一直循环，我们可以在循环体内放入条件
# 如
# i=1
# while i>5:
# 	i+=1
# 如此循环5次条件i>5便会不成立为False 条件不成立循环终止

#for循环 (计数器循环) 迭代器
# 语法
# for 目标 in 表达式:
# 	循环体

##数组
# 数组=['小甲鱼','大甲鱼'，'老甲鱼','死甲鱼']

# len(i) 统计长度 

# range()
# 语法range([start,] stop [step=1]) step步进默认为一
# 默认从0开始
# range（1）start 从0开始不包括1
# range（1,2）start,stop 从一开始不包含2
# range(1,6,2) start,stop,step


# break 终止跳出循环
# continue 跳出本轮循环如果循环条件为真则继续循环
# 当continue 上方条件为真则跳过进行下一轮循环

# while 永远为真 是一个死循环 消息循环时刻接收消息 
# 可以随时用 break 来跳出循环！

# while i < len(string)):
# length = len(string)
# 相对于每次调用len()函数不如调用一次将值赋给变量

# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
# password='123456'
# i=3
# while i:
# 	p=input('请输入您的密码')
# 	if p==password:
# 		print('密码正确')
# 		break
# 	elif "*" in p:
# 		i-=1
# 		print('输入错误，密码中不允许有*。您还有%s次机会'%i)
# 		continue
# 	else:
# 		i-=1
# 		print('密码不对哦，您还有%s次机会'%i)

# 抄
# 编写一个程序，求 100~999 之间的所有水仙花数。
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# for i in range(100, 1000):
#     sum = 0
#     temp = i
#     while temp:  
#         sum = sum + (temp%10) ** 3 第一次取个位的3次幂赋值给sum 第二次取十位的三次幂加上个位的三次幂赋值给sum 第三次。。。。。
#         temp //= 10         # 注意这里要使用地板除哦~  第三次地板除以十 必然为0 temp为假则不再循环
#     if sum == i:
#         print(i)

for R in range(0,4):
	for Y in range(0,4):
		for G in range(2,7):
			if R+Y+G ==8:
				print(R,'\t',Y,'\t',G)