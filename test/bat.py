from superhero import Superhero
from human import Human

class Bat:
    species = "Baty"

    def __init__(self, can_fly = True):
        self.fly = can_fly
    
    def say(self, msg):
        msg = "... ... ..."
        return msg
    
    def sonar(self):
        return '))) ... ((('
    
if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)


class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        Superhero.__init__(self, 'anonymous', movie=True, superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        self.name = "Sad Affleck"
    
    def sing(slef):
        return 'nan nan nan batman!'

if __name__ == '__main__':
    sup = Batman()

    # 获取方法解析顺序 MRO，MRO 被用于 getattr() 和 super()
    # 这个字段是动态的，并且可以被修改
    print(Batman.__mro__)       # => (<class '__main__.Batman'>,
                                # => <class 'superhero.Superhero'>,
                                # => <class 'human.Human'>,
                                # => <class 'bat.Bat'>, <class 'object'>)

    # 调用父类的方法并且使用子类的属性
    print(sup.get_species())    # => Superhuman

    # 调用被重写的类
    print(sup.sing())           # => nan nan nan nan nan batman!

    # 调用 Human 上的方法，(之所以是 Human 而不是 Bat)，是因为继承顺序起了作用
    sup.say('I agree')          # => Sad Affleck: I agree

    # 调用仅存在于第二个继承的父类的方法
    print(sup.sonar())          # => ))) ... (((

    # 继承类的属性
    sup.age = 100
    print(sup.age)              # => 100

    # 从第二个类上继承字段，并且其默认值被重写
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False
