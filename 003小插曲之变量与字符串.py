# 变量(variable)
# python没有变量只有名字
# print(name) 输出name变量的值
# print('name') 输出字符串name
# last_name = ('jiao')
# fast_name = ('ao')
# name = last_name+fast_name 将两个变量的值拼接赋值给name
# print(name)                输出name变量的值jiaoao
#变量名可以包括字母下划线和数字但不可以以数字开头
# 如果你想在字符串中添加单引号或者双引号有两种方法
# print('let/’s go!')  转义符号（\）
# print("let's go !")  双引号包单引号或者单引号包双引号
# str = ("C:\now")
# print(str) 此时\n会被误认为换行
# str = (r"C:\now") # 此时我们使用原始字符串便可以解决
# str = (r"C:\now\") 原始字符串后不可以添加\
#  str = (r"C:\now""\")如果我们必须要添加\ 则需要将字符串分成两段
# 如果你希望得到一个跨越多行的字符串如
# 123
# 456
# 789
# 111
# 222
# 333
# 则需要使用三重引用字符串
# str = '''123
# 456
# 789
# 111
# 222
# 333'''
# print(str)
# 课后动手还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？
# 提示：可以以 DaysPerYear（每年天数），HoursPerDay（每天小时数），MinutesPerHour（每小时分钟数），SecondsPerMinute（每分钟秒数）为变量名。
DaysPerYear = 365
HoursPerDay = 24
MinutesPerHour = 60
SecondsPerMinute = 60
HoursSeconds = (MinutesPerHour*SecondsPerMinute) #每小时多少秒
DaysSeconds = (HoursPerDay*HoursSeconds)#每天多少秒
yearSeconds = (DaysPerYear*DaysSeconds)
print(yearSeconds)

