class Dog(object):
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self, dog):
        dog.work()

ad = ArmyDog()
dd = DrugDog()
person1 = Person()
# 多态调用
person1.work_with_dog(ad) # 追击敌人
person1.work_with_dog(dd) # 追查毒品