class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0
    def say(self, msg):
        print(f"{self.name}: {msg}")

    def sing(self):
        return 'yo... yo... microphone check... one two ... one two...'
    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def set_species(cls, species):
        cls.species = species

    @staticmethod
    def grunt():
        return '*grunt*'
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    @age.deleter
    def age(self):
        del self._age


# 当 Python 解释器在读取源文件的时候，就会执行文件中所有的代码
# 对 __name__ 的检查可以保证这块代码只会在这个模块是主程序的情况下被运行（而不是在引用时运行）
if __name__ == '__main__':
    # 
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i 和 j 都是 Human 实例化后的对象，换一句话说，它们都是 Human 实例

    # 运行类方法 (classmethod)
    i.say(i.get_species())          # "Ian: H. sapiens"
    # 修改共享的类属性
    Human.species = "H. neanderthalensis"
    i.species = "test"
    i.set_species("test2")
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # 运行静态方法 (staticmethod)
    print(Human.grunt())            # => "*grunt*"

    # 实例上也可以执行静态方法
    print(i.grunt())                # => "*grunt*"

    # 更新实例的属性
    i.age = 42
    # 访问实例的属性
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # 删除实例的属性
    del i.age
    # i.age                         # => 这会抛出一个错误: AttributeError