commodity_list = [['苹果',2000],['香蕉',300],['樱桃',400],['菠萝',3000]]
Wage = int(input('请输入你的工资:'))
shopping_list = []
Balance = Wage
while True:
    for index,imet in enumerate(commodity_list):
        print(index,imet)
    shopping_index = input('请输入你需要的商品编号 or q退出购物:')
    if shopping_index.isdigit():
        shopping_index = int(shopping_index)
        if shopping_index < int(len(commodity_list)) and shopping_index >= 0:
            shopping_list.append(commodity_list[shopping_index])
            Balance = Balance - commodity_list[shopping_index][1]
            print(shopping_list)
            print(Balance)
            if Balance < 0:
                print('Money not Enough')
                while True:
                    continue_shopping = int(input('删除购物车里的商品，请输入1，其他退出购物'))
                    if continue_shopping == 1:
                        for sp_index,sp_imet in enumerate(shopping_list):
                            print(sp_index,sp_imet,end=' ')
                        del_shopping = int(input('删除第几个商品:'))
                        if del_shopping < int(len(shopping_list)) and del_shopping >= 0:
                            Balance = Balance + shopping_list[del_shopping][1]
                            del shopping_list[del_shopping]
                            print('购买清单\n', shopping_list, '\n', '余额：', Balance)
                        else:
                            print('购买清单\n',shopping_list,'\n','余额：',Balance)
                            continue
                    else:
                        break
            else:
                print('购买清单\n \033[31:1m%s\033[0m' % shopping_list, '\n', '余额：\033[31:1m%s\033[0m' % Balance)
    elif shopping_index == 'q':
        if Balance >= 0:
            print('购买清单\n \033[31:1m%s\033[0m'%shopping_list, '\n', '余额：\033[31:1m%s\033[0m'%Balance)
            break
        else:
            shopping_list = []
            Balance = Wage
            print(shopping_list,Balance)
            break
    else:
        continue








