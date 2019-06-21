# 创建房子类：
# 房子的户型，面积，地址
class House:
    def __init__(self, info, area, addr):
        self.info = info
        self.area = area
        self.addr = addr
        self.furniture_lst = []  # 用来保存家具名称

    '''添加家具的方法'''

    def add_furniture(self, furniture):
        '''furniturn 接收传进来的对象'''
        # house面积剩余面积=house当前面积-家具面积
        self.area = self.area - furniture.area
        self.furniture_lst.append(furniture.name)  # 蒋家具的名称添加到家具列表中

    def __str__(self):
        msg = '剩余面积{}，户型{}，在{}买的房子,'.format(self.area, self.info, self.addr)
        msg1 = '新添的设备{}'.format(self.furniture_lst)
        return msg + msg1


# 创建床类:
class Bad:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = '{}面积是{}'.format(self.name, self.area)
        lst = []
        return msg


class Sofa:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = '{}的面积是{}'.format(self.name, self.area)


house = House('三室一厅', 130, '五方桥')
# print(house)
bad = Bad('上下铺', 2)
# print(bad)
house.add_furniture(bad)
print(house)
# 给房子再添家一个双人床
bad1 = Bad('双人床', 4)
house.add_furniture(bad1)
print(house)
sofa = Sofa('沙发', 3)
house.add_furniture(sofa)
print(house)
