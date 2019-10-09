name = 'oldboy \t is dog'
print(name.capitalize())    #大写
print(name.count('d'))
print(name.center(50,'-'))     #打印50个字符，name放在中间，其他用-补齐
print(name.encode())
print(name.endswith('dog'))  #判断是否以dog结尾。返回布尔值
print(name.expandtabs(tabsize=30)) #如果字符串中以\t   tab键转换为多少个空格
print(name.find('dog'))     #取查找的索引
print(name[12:15])
name = '{oldboy} is {dog}'
print(name.format(oldboy='alex',dog='big'))     #格式化,可以把{}里的变量赋值
print(name.format_map({'oldboy':'shabi','dog':12}))
print(name.index('s'))
print(name.isalnum())   #判断他是不是英文字符和阿拉伯数字，不能也特殊字符返回布尔值
print(name.isalpha())   #判断是不是纯英文字符，返回布尔值
print('1'.isdecimal())  #判断是不是十进制正整数
print(name.isdigit())   #判断是不是整数
print(name.isidentifier())  #判断是不是一个合法的标识符，是不是合法的变量名
print('b'.islower()) #判断是不是小写
print('1'.isnumeric())  #判断是不是一个数字，不能也其他字符，实际上就是正整数
print(' '.isspace())   #判断是不是一个空格
print('My Name'.istitle())   #每个首字母是不是大写
print(''.isprintable())   #判断是不是打印，除了tty，drive，file其他的大部分都能打印
print('A'.isupper())  #是不是都是大写
print('+'.join(['1','2','3']))  #把列表按字符串打印出来，可以添加区分号
print(name.ljust(50,'@'))   #打印50个字符，如果不够在末尾用@补齐
print(name.rjust(50,'$'))  #在前面赢$补齐
print('ABC'.lower())  #把大写变成小写
print('abc'.upper())  #把小写变大写
print('\n Oldboy\n'.lstrip())  #去除左边的空格和回车
print('\n Oldboy \n'.rstrip())   #去除右边的空格和回车
print('\n Oldboy \n'.strip())   #去除空格和换行
p = str.maketrans('abcdef','123456')
print(p)
print('oldboy lod'.translate(p))   #把p里面对应的数值替换
print('oldboy old'.replace('ol','OL',1))   #替换加个1就是只替换一个，要不然全部替换
print('oldboy old'.rfind('d'))     #从右边开始查找尾标
print('oldboy old'.split())    #安装空格把字符串变成列表
print('oldboy old'.split('l'))    #可以指定分隔符
print('oldboy \n old'.splitlines()) #== print('oldboy old'.split('\n')),以换行为分隔符，变成列表
print('oldboy old'.swapcase())    #全部变成大写
print('oldboy old'.title())    #首字母大写
print('oldboy old'.zfill(50))   #打印50个，不够用0补充




