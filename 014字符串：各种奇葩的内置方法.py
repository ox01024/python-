# 字符串
# str[:6] 切片前六个字符
# str=str[:6]+'字符串'+str[6:] 将字符串拼接并贴上str标签

# str.capitalize() 首字母大写
# str.casefold()    全部小写
# str.center(字符大小)   居中
# str.count(sub[start[end]]) 统计sub在字符串出现的次数 表示范围可选
# str.encode(encoding='utf-8',errors='strict') 以encoding指定的编码格式对字符进行编码
# str.endswith(sub[start[end]]) 检查字符串是否以sub字符串结束，是返回True否返回Fales 范围可选
# str.expandtabs([tabsize=8]) 将字符串中的tab符号(/t)转换成空格 空格数默认为8
# str.find(sub[start[end]])   搜索sub是否存在字符串中,有则返回索引值否则返回-1 范围可选
# str.index(sub[start[end]])  跟find方法一样，不过如果sub不在string中会产生一个异常
# str.isalnum()	如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
# str.isalpha()	如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
# str.isdecimal()	如果字符串只包含十进制数字则返回True，否则返回False
# str.isdigit()	如果字符串只包含数字则返回True，否则返回False
# str.islower()	如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True，否则返回False
# str.isnumeric()	如果字符串中只包含数字字符，则返回True，否则返回False
# str.isspace()	如果字符串中只包含空格，则返回True，否则返回False
# str.istitle()	如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回True，否则返回False
# str.isupper()	如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回True，否则返回False
# str.join(sub)	以字符串作为分隔符，插入到sub中所有的字符之间。>>> str5 = 'Fishc' >>> str5.join('12345') '1Fishc2Fishc3Fishc4Fishc5'
# str.ljust(width)	返回一个左对齐的字符串，并使用空格填充至长度为width的新字符串
# str.lower()	转换字符串中所有大写字符为小写
# str.lstrip()	去掉字符串左边的所有空格
# str.partition(sub)	找到子字符串sub，把字符串分成一个3元组（pre_sub,sub,fol_sub），如果字符串中不包含sub则返回(‘原字符串’, ’’, ’’)
# str.replace(old,new[,count])	把字符串中的old子字符串替换成new子字符串，如果count指定，则替换不超过count次。>>> str7 = 'i love fishdm and seven' >>> str7.replace('e','E',2) 输出'i lovE fishdm and sEven'
# str.rfind(sub[,start[,end]])	类似于find()方法，不过是从右边开始查找
# str.rindex(sub[,start[,end]])	类似于index()方法，不过是从右边开始
# str.rjust(width)	返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串
# str.rpartition(sub)	类似于partition()方法，不过是从右边开始查找
# str.rstrip()	删除字符串末尾的空格
# str.split(sep=None, maxsplit=-1)	不带参数默认是以空格为分隔符切片字符串，如果maxsplit参数有设置，则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表。>>> str7.split () ['i', 'love', 'fishdm', 'and', 'seven']
# str.splitlines(([keepends]))	按照‘\n’分隔，返回一个包含各行作为元素的列表，如果keepends参数指定，则返回前keepends行
# str.startswith(prefix[,start[,end]])	检查字符串是否以prefix开头，是则返回True，否则返回False。start和end参数可以指定范围检查，可选
# str.strip([chars])	删除字符串前边和后边所有的空格，chars参数可以定制删除的字符，可选
# str.swapcase()	翻转字符串中的大小写
# str.title()	返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串
# str.translate(table)	根据table的规则（可以由str.maketrans(‘a’,‘b’)定制）转换字符串中的字符。>>> str8 = 'aaasss sssaaa' >>> str8.translate(str.maketrans('s','b')) 'aaabbb bbbaaa'
# str.upper()	转换字符串中的所有小写字符为大写
# str.zfill(width)	返回长度为width的字符串，原字符串右对齐，前边用0填充

# '''这个
# 叫做
# 多行
# 注释'''

# file=open(r.'C:/user/2211/tmp/1.txt','r')  必须使用原始字符否则/t会被执行


str1 = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
has_str1 = 0
has_num = 0
has_alpha = 0
t = 'y'
while t == 'y':
        password = input("请输入需要检查的密码组合：")
        length = len(password)
        while(password.isspace() or length == 0):  # 有空格或者长度为零
                password = input('您输入的密码为空（或空格），请重新输入：')
        for i in password:
                if i in str1:
                        has_str1 = 1
                if i.isdigit():  # 所有字符都是数字
                        has_num = 1
                if i.isalpha():  # 所有字符都是字母
                        has_alpha = 1
        has =  has_str1 + has_num + has_alpha
        if length <= 8 or password.isalnum():
                level = "低"
        if length > 8 and has ==2:
                level = "中"
        if length >= 16 and has == 3 and password[0].isalnum():
                level = "高"
        print("您的密码安全等级评定为：%s"%level)
        if level == "高":
                print("请继续保持")
        else:
                print("""请按以下方式提升您的密码安全级别：
        1.密码必须由数字、字母及特殊字符三种组合
        2.密码只能由字母开头
        3.密码长度不能低于16位""")
        t = input("还要再测试么？（”y“继续，其他退出）")