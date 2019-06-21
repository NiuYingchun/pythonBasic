# 商品列表
product_list = [
    ('Iphone8', 6888),
    ('MacPro', 14800),
    ('小米6', 2499),
    ('bike', 800),
    ('Coffee', 31),
    ('Nike Shoes', 799),
]
# 购物车
shopping_list = []
salary = input("输入您的薪水:")
if salary.isdigit():     # 检测字符串是否只由数字组成
    salary = int(salary)
    run_flag = True
    while run_flag:
         print(str.center('商品列表', 30, '-'))
         for k, v in enumerate(product_list):
             print('%s. %s     %s' % (k, v[0], v[1]))
         choice = input("请输入想买商品的编号,退出请输入q:")
         if choice.isdigit():
            choice = int(choice)
            print(choice)
            if choice >= 0 and choice < len(product_list):
                item_price = product_list[choice]
                if item_price[1] <= salary:  #买得起
                    shopping_list.append(item_price)  # 追加到购物车
                    salary -= item_price[1]
                    print("%s添加到购物车,您当前余额是:%d" % (item_price, salary))
                else:
                    print('您当前余额不足')
            else:
                print('商品不存在')
         elif choice == 'q' or choice == 'Q':
             if len(shopping_list) > 0:
                print(str.center('您已购买以下商品', 30, '-'))
                for k, v in enumerate(shopping_list):
                    print('%s. %s     %s' % (k, v[0], v[1]))
                print("您当前余额:%d" % salary)
             run_flag = False