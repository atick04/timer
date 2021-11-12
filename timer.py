from multiple_inheritance import Moto1


timeDesk = float(input("Enter time in seconds:"))
day = timeDesk // (24 * 3600)
timeDesk = timeDesk % (24 * 3600)
hour = timeDesk // 3600
timeDesk %= 3600

min = timeDesk // 60
timeDesk %= 60
seconds = timeDesk
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, min, seconds))

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class MOTIKI:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    @property
    def general(self):
        flowers = self.name + '' + self.brand
        return  MOTIKI

    @general.setter
    def general(self, motiki):
        self.name, self.color = motiki.split()

    @general.deleter
    def general(self):
        self.name = None
        print('Name delete')

    def __str__(self):
        return f'motiki: {self.name}  {self.brand}'

    @staticmethod
    def for_all(cost):
        if cost > 0:
            return True
        else:
            return False

Moto1 = MOTIKI(name='honda', brand='cbr1000rr')
print(Moto1)
print(Moto1.general)

Moto1.name = 'ducati'
print(Moto1.general)

del Moto1.general
print(Moto1.general)

print(Moto1.for_all(67))




