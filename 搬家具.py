# 家具类
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

# 房子类
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面加
        self.area = area
        # 剩余面加
        self.free_area = area
        # 家具列表
        self.furnitures = []

    def __str__(self):
        return f'房子地理位置：{self.address},房子的面加：{self.area},房子的剩余面积：{self.free_area},房子的家具列表：{self.furnitures}'

    def add_furniture(self, item):
        if item.area <= self.free_area:
            self.furnitures.append(item.name)
            self.free_area -= item.area
        else:
            print(f'家具太大，无法装下，该家具占地面积{item.area},房子剩余面积{self.free_area}')


bed = Furniture('双人床',60)
sofa = Furniture('沙发',5)

home1 = Home('北京',100)
print(home1)
home1.add_furniture(bed)
print(home1)
home1.add_furniture(sofa)
print(home1)