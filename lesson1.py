''''
class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print("哈哈， {0} 会比 {1} 大吗？".format(self._name, obj._name))
        return self._name > obj._name


# 作业：
# 字符串的比较是按什么规则
stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)
'''

class Person:
    # 实例方法
    def eat(self):
        print(self)
        print("Eating.....")

    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.....")

    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying....")


yueyue = Person()

# 实例方法
yueyue.eat()
#名称是 person object
# 类方法
Person.play()
#名称是Person
yueyue.play()
# 静态方法
Person.say()
yueyue.say()