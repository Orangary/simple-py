# -*- coding: utf-8 -*-
from enum import Enum, unique
# Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,number in Month.__members__.items():
#     print(name,'=>',number,',',number.value)

@unique
class Gender(Enum):
    Male = 0 # Sun的value被设定为0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')