# 01
class Cat():
    def __init__(self, colr, wight, agee):
        self.color = colr
        self.weight = wight
        self.age = agee

    def eat(self, food):
        print(f'{self.color}，{self.age}岁，体重{self.weight}kg的小猫{food}了')

    def __str__(self):
        return f'{self.color}，{self.age}岁，体重{self.weight}kg'


acat = Cat('三花', 1, 3)
print(acat)

acat.eat('吃鱼')


# 02
class People():
    def __init__(self):
        self.name = '小明'
        self.weight = 75

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步了，现在体重{self.weight}kg')

    def eat(self):
        self.weight += 1
        print(f'{self.name}吃东西了，现在体重{self.weight}kg')

    def __str__(self):
        return f'我叫{self.name},体重{self.weight}kg,我爱跑步,爱吃美食'


xming = People()
print(xming)
xming.run()
xming.eat()
xming.run()

xmei = People()
xmei.name = '小美'
xmei.weight = 45
print(xmei)
xmei.eat()
xmei.run()


# 03
class Home():
    def __init__(self, roms, tarea):
        self.rooms = roms
        self.area = tarea
        self.furn = []
        self.area_rest = self.area

    def add_furn(self, *furns):
        self.furn.extend(furns)
        for f in furns:
            if f == '床':
                self.area_rest -= 4
            if f == '衣柜':
                self.area_rest -= 2
            if f == '餐桌':
                self.area_rest -= 1.5

    def __str__(self):
        return f'{self.rooms}居室，总面积{self.area}m²，剩余面积{self.area_rest}m²，家具{self.furn}'


ahome = Home(5, 180)
print(ahome)
ahome.add_furn('床', '衣柜')
print(ahome)
ahome.add_furn('餐桌')
print(ahome)
print(ahome.area_rest)


# 04
class Solider():
    def __init__(self, namee, gun):
        self.name = namee
        self.gun = gun

    def shoot(self):
        self.gun.shoot()
        print(f'士兵{self.name}使用{self.gun.name}开火一次,当前子弹{self.gun.bullet}发')


class Gun():
    def __init__(self, name, bullet,bullet_max):
        self.name = name
        self.bullet = bullet
        self.bullet_max = bullet_max
    def shoot(self):
        if self.bullet == 0:
            print('请装子弹')
        else:
            self.bullet -=1
    def add_bullet(self,num):
        if self.bullet+num >= self.bullet_max:
            print(f'共装{self.bullet_max-self.bullet}颗子弹，已装满至{self.bullet_max}颗，')
            self.bullet = self.bullet_max
        else:
            self.bullet += num
            print(f'共装{num}颗子弹，当前子弹{self.bullet}颗')

    def __str__(self):
        return f'这是一把{self.name},当前子弹{self.bullet}发,共可装{self.bullet_max}发'

ak47 = Gun('ak47', 3,30)
print(ak47)
asolider = Solider('瑞恩',ak47)
asolider.shoot()
asolider.shoot()
ak47.add_bullet(29)
ak47.add_bullet(2)
asolider.shoot()
asolider.shoot()
ak47.add_bullet(2)