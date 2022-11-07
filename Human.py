class Human:
    default_name = 'Alex'
    default_age = 33

    def __init__(self, money, house, name = default_name, age = default_age,):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        return "Имя - {},\nВозраст - {},\nНаличие денег - {},\nНаличие дома - {}".format(self.name,self.age,self.__money,self.__house)

    def __str__(name = default_name, age = default_age):
        return "Имя по умолчанию - {},\nВозрст по умолчанию - {}".format(name, age)


human_object = Human( 20000, 'Yes', 'Asder')

if __name__ == '__main__':
    print(human_object.info())
    print(human_object.__str__())
    # print(dir(human_object))
    # print(dir(Human))