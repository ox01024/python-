# 整型     整数 int()
# 浮点型   小数 float()
# 布尔型   true=1 Fales=0  bool 计算机二进制只认识01
# e计法    科学计数法  
# 字符串 str()
# 浮点数转整数会截断处理fload(5.55)=int(5)
# 取得变量类型 type(5.22) 
# 如何使fload()数转换成int()4舍5入 int(fload+0.5)就可以了 
# type() 直接返回一个输入的变量的类型
# ininstance() 返回变量与另一个变量的类型比较，如果是统一类型则返回TRUE,不同则返回FALSE
# s.isalnum() 所有字符都是数字或者字母，返回 True，否则返回 False
# s.isalpha() 所有字符都是字母，为真返回True,否则返回 False
# s.isdigit() 所有字符都是数字，为真返回True,否则返回 False
# s.islower() 所有字符都是小写，为真返回True,否则返回 False
# s.isupper() 所有字符都是大写，为真返回True,否则返回 False
# s.istitle(）所有单词都是首字母大写，为真返回True,否则返回 False
# s.isspace(）所有字符都是空白字符，为真返回True,否则返回 False
print('你好我是小爱同学，你可以告诉我你个年份我帮你判断是否是闰年哦！')
年份=input()
while not 年份.isdigit:
	print('人家说的是年份那讨厌')
year=int(年份)
if year/400==int(year/400):
	print('是世纪闰年哦')
else :
	if year/4==int(year/4) and year/100!=int(year/100):
		print('是普通闰年哦')
	else:
		print('不是闰年哦')