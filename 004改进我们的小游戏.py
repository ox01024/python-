# 004改进我们的小游戏
# 添加提示
# 添加多次机会
# 添加随机答案
# 条件分支  ==等于 ！=不等于 true真  False假 
# if 条件:
# 	条件为真(true)执行的操作
# else :
# 	条件为假(False)执行的操作

# 添加提示
# print('---------------小甲鱼大傻逼----------------')  #
# temp= input('小甲鱼心里面的逼数是多少:')
# guess= int(temp)
# if guess == 8:
# 	print('你是小甲鱼他爹吧')
# else :
# 	if guess > 8:
# 		print('大了大了')
# 	else:
# 		print('小了小了')
# print('886小甲鱼')

#添加多次机会
# while 条件:
# 	条件为真(true)时执行的操作
# print('---------------小甲鱼大傻逼----------------')  #
# temp= input('小甲鱼心里面的逼数是多少:')
# guess= int(temp)
# while guess !=8:
# 	temp = input('输错了重新输吧')
# 	guess = int(temp)
# 	if guess == 8:
# 		print('你是小甲鱼他爹吧')
# 	else :
# 		if guess > 8:
# 			print('大了大了')
# 		else:
# 			print('小了小了')
# print('886小甲鱼')

# 添加固定多次机会
# while 条件:
# 	条件为真(true)时执行的操作
# print('---------------小甲鱼大傻逼----------------')  #
# temp= input('小甲鱼心里面的逼数是多少:')
# guess= int(temp)
# i = 3
# while guess !=8 and i:
# 	temp = input('输错了重新输吧,你还有'+str(i)+'次机会')
# 	guess = int(temp)
# 	if guess == 8:
# 		print('你是小甲鱼他爹吧')
# 	else :
# 		if guess > 8:
# 			print('大了大了')
# 			i=i-1
# 		else:
# 			print('小了小了')
# 			i=i-1
# print('886小甲鱼')


# 添加随机答案
# 使用random模块里的randint()函数可以返回一个随机的整数
# import random
# secret = random.randint(1,10) #生成一个1到10的随机整数 赋值给secret
# print('---------------小甲鱼大傻逼----------------')  
# temp= input('小甲鱼心里面的逼数是多少:')
# guess= int(temp)
# while guess !=secret:
# 	temp = input('输错了重新输吧')
# 	guess = int(temp)
# 	if guess == secret:
# 		print('你是小甲鱼他爹吧')
# 	else :
# 		if guess > secret:
# 			print('大了大了')
# 		else:
# 			print('小了小了')
# print('886小甲鱼')

#改进
# import random
# secret = random.randint(1,10) #生成一个1到10的随机整数 赋值给secret
# print('---------------小甲鱼大傻逼----------------')  #
# temp= input('小甲鱼心里面的逼数是多少:')
# guess= int(temp)
# while guess !=secret:
# 	if guess < secret:
# 		print('小了小了')
# 		temp = input('输错了重新输吧')
# 		guess = int(temp)
# 	else :
# 		if guess > secret:
# 			print('大了大了')
# 			temp = input('输错了重新输吧')
# 			guess = int(temp)
# 		else:
# 			print('猜对了')
# print('你是小甲鱼他爹吧')
# print('886小甲鱼')

#不完美版
# import random
# secret = random.randint(1,10) #生成一个1到10的随机整数 赋值给secret
# print('---------------小甲鱼大傻逼----------------')  #
# temp= input('小甲鱼心里面的逼数是多少:')
# guess= int(temp)
# i=3
# while guess !=secret and i:
# 	if guess < secret:
# 		print('小了小了')
# 		temp = input('输错了重新输吧，你还有'+str(i)+'次机会')
# 		i=i-1
# 		if i==0:
# 			print('这都猜不中回家玩泥巴去吧')
# 		guess = int(temp)
# 	else :
# 		if guess > secret:
# 			print('大了大了')
# 			temp = input('输错了重新输吧，你还有'+str(i)+'次机会')
# 			i=i-1
# 			if i==0:
# 				print('这都猜不中回家玩泥巴去吧')
# 			guess = int(temp)
# 		else:
# 			print('猜对了')
# 			print('你是小甲鱼他爹吧')
# 			print('886小甲鱼')

# 听说过“短路逻辑（short-circuit logic）”吗？
# python短路逻辑 表达式 x and y 
# 当两个数进行比较时只有两个值都为真时结果才为真
# 所以一方为假(False)时结果自动为假
# 这种叫做短路逻辑，又叫惰性求值 and与or操作符相同

# 课后习题输出
# 1
# 2
# 3
# 4
# 5
# temp=input('请输入一个整数') 
# num=int(temp)
# i=1
# while num:  #如果num>0则循环 true 
# 	print(i)
# 	i=i+1 #i自增
# 	num=num-1 #i自增则num自减 当num-1等于0时循环终止


# 请输入一个整数:5
#     *****
#    ****
#   ***
#  **
# *


# temp=input('输入一个整数')
# num=int(temp)
# while num:
# 	print(" "*num+num*"*")
# 	num=num-1

#自制
# import random
# secret = random.randint(1,10) #生成一个1到10的随机整数 赋值给secret
# i = 3
# guess = 0
# print('---------------小甲鱼大傻逼----------------')  
# while guess != secret and i :
# 	guess=int(input('请输入小甲鱼心中想的数字，你还有'+str(i)+'次机会'))
# 	if guess>secret :
# 		i=i-1
# 		print('大了大了，你还有'+str(i)+'次机会')
# 	else:
# 		if guess<secret :
# 			i=i-1
# 			print('小了小了，你还有'+str(i)+'次机会')
# 		else :
# 			print('猜对了，哈哈哈')
# 		


#模仿小甲鱼
import random
secret=random.randint(1,10)
i=3
guess=0
print('---------------小甲鱼大傻逼----------------')  
while guess!=secret and i:
	guess=int(input('请输入小甲鱼心中想的数字：'+ ' '))
	if guess==secret:
		print('猜对了，你时小甲鱼他爹吧')
	else:
		if guess>secret:
			i=i-1
			print('大了大了，哥')
		else:
			if guess<secret:
				i=i-1
				print('小了小了，哥')
		if i>1:
			print('你还有'+str(i)+'次机会，请好好珍惜')
		else:
			if i==1:
				print('你就剩一次机会了哦')
			else:
				print('机会用光了下次再来吧！')
print('游戏结束了')
					
#小甲鱼版本
# import random
# times = 3
# secret = random.randint(1,10)
# print('------------------我爱鱼C工作室------------------')
# # 这里先给guess赋值（赋一个绝对不等于secret的值）
# guess = 0
# # print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# # 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
# print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
# while (guess != secret) and (times > 0):
#     temp = input()
#     guess = int(temp)
#     times = times - 1 # 用户每输入一次，可用机会就-1
#     if guess == secret:
#         print("我草，你是小甲鱼心里的蛔虫吗？！")
#         print("哼，猜中了也没有奖励！")
#     else:
#         if guess > secret:
#             print("哥，大了大了~~~")
#         else:
#             print("嘿，小了，小了~~~")
#         if times > 0:
#             print("再试一次吧：", end=" ")
#         else:
#             print("机会用光咯T_T")
# print("游戏结束，不玩啦^_^")