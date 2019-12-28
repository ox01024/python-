# 函数对象模块
# 定义一个函数
# def hanshu01():
# 	print('这是我创建的第一个函数')
# 	print('我一定要学会Python')
# 	print('加油加油')
# 调用一个函数 
# hanshu()
# 当调用一个函数，python会向上寻找函数的定义，然后执行函数过程的内容
# 参数
# >>> def hanshu02(name):
# 	print(name+'大傻逼！')

# >>> hanshu02('小甲鱼')
# 小甲鱼大傻逼！
# >>> 

# >>> def add(num1,num2):
# 	num=num1+num2
# 	print(num)

	
# >>> add(2,3)
# 5
# >>> 


# >>> def add(num1,num2):
# 	return(num1+num2)

# >>> add(1,2)
# 3
# 通过return返回值


# 1.  def MyFun():
# 2.      # 我是函数体
# 3.      # 我也是函数体
# 4.      # 我们都属于函数MyFun()
# 5.  
# 6.  # 噢，我不属于MyFun()函数的了
 


#  编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。  
# def power(x,y):
# 	return(x**y)
# print(power(2,3))


# 利用欧几里得算法求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。
# def gcd(x,y):
#     while y:
#         t = x % y
#         x = y
#         y = t
#     return x

 编写一个将十进制转换为二进制的函数，要求采用“除2取余”的方式，结果与调用bin()一样返回字符串形式。
def DectoBin(num):
    temp = []
    result = ''
    while num:
        x = num % 2  # 取余数，当做个位...十位...百位...以此类推
        num = num // 2  #取整数当做下一次的被除数
        temp.append(x)
    while temp:
        result += str(temp.pop())
    return result
