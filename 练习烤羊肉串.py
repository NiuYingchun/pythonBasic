class KQY:
    def __init__(self):
        '''初始化的参数'''
        self.cooking_time = 0
        self.cooking_status = '生的'
        self.cooking_zl = [] #保存作料

    def cooking(self , cooking_time):
        self.cooking_time += cooking_time
        if self.cooking_time >= 0 and self.cooking_time <= 3:
            self.cooking_status = '生的'
        elif self.cooking_time > 3 and self.cooking_time <=6:
            self.cooking_status = '半生不熟'
        elif self.cooking_time > 6 and self.cooking_time <=10:
            self.cooking_status = '熟了'
        else:
            self.cooking_status = '烤焦了'

    def add_zl(self , zl):
        self.cooking_zl.append(zl)

    def __str__(self):
        msg = '烤的时间{}, 目前状态{},添加的作料{}'.format(self.cooking_time , self.cooking_status, self.cooking_zl)
        return msg

chuan1 = KQY()
chuan1.cooking(3)
chuan1.add_zl('刷油')
print(chuan1)

chuan1.cooking(4)
chuan1.add_zl('孜然')
print(chuan1)

chuan1.cooking(3)
chuan1.add_zl('盐')
print(chuan1)



