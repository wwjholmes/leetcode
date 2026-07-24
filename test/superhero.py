from human import Human

class Superhero(Human):
    species = 'Superhuman'

    def __init__(self, name, movie=False, superpowers=["super strength", "bulletproofing"]):
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers
        super().__init__(name)

    def sing(self):
        return 'Dun, dun, DUN!'
    
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {power}")

if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # 检查实例类型
    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a superhero')

    # 获取方法解析顺序 MRO，MRO 被用于 getattr() 和 super()
    # 这个字段是动态的，并且可以被修改
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # 调用父类的方法并且使用子类的属性
    print(sup.get_species())    # => Superhuman

    # 调用被重写的方法
    print(sup.sing())           # => Dun, dun, DUN!

    # 调用 Human 的方法
    sup.say('Spoon')            # => Tick: Spoon

    # 调用 Superhero 独有的方法
    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # 继承类的字段
    sup.age = 31
    print(sup.age)              # => 31

    # Superhero 独有的字段
    print('Am I Oscar eligible? ' + str(sup.movie))
