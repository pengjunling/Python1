info = {
    'stu01': 'wangwu',
    'stu02':'lisi'

}
b  = {1:2,3:4}
#stu01就是key  最好不用中文
#info key-values
#字典是无序的
print(info['stu01'])   #查  最好不用这种查找，没有就报错
print(info.get('stu01'))  #查找，哪怕没有也不报错
print('stu01' in info)   #判断是不是在字典里，返回布尔值
info['stu01'] = "武藤兰"  #改
print(info['stu01'])
info['stu03'] = '杀阡陌' #存在就修改，不存在就增加
print(info)
del info['stu01']  #删除
print(info)
info.pop('stu02')  #也是删除
print(info)
info.popitem()  #随机删除
print(info)
info['stu03'] = '杀阡陌'
info['stu01'] = '杀阡'
print(info.values())  #.values 打印除了第一层key的其他所有值
print(info.keys())   #只打印第一层key的值
print(info.setdefault(1,2))   #如果不存在key就增加，如果存在就不修改
print(info.update(b))    #有两个字典，加个其他字典的参数，两个字典合并，中间有交叉的部分更新
print(info)
print(info.items())  #把一个字典变为列表
c = dict.fromkeys([6,7,8],['test',{'name':'oldboy'}])   #初始化一个值，给他们临时赋值，只手第一层永久生效，其他不是永久生效
print(c)
c[6][1]['name'] = 'jack chen'
print(c)
print(info)

for i in info:          #循环
    print(i,info[i])

for k,v in info.items():
    print(k,v)

