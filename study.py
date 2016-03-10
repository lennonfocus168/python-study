from types import MethodType


class Student(object):
    pass


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.name = 'afwef'

s1 = Student()
s1.step = 3

Student.set_age = MethodType(set_age, s)

s1.set_age(10)
