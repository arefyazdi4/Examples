from datetime import datetime


class Characters:
    __doc__ = "this class is abstract class (virtual)"
    T_POSE = True   # capital name is const attribute and its global class attribute (not 4 object)

    def __init__(self, hit_box=40):
        self.__speed = 10  # contract that __ is private and have have no access out of class
        self._hit_box = hit_box  # contract _ is semi private attribute u can access out of class

    def get_speed(self) -> int:  # specify the output type of methode
        return self.__speed

    def __set_speed(self, new_speed: int):  # specify the input type of methode
        self.__speed = new_speed


class Legends(Characters):  # inheriting from base class
    counter = 0  # static attribute

    def __init__(self, name, ability=None, ult=None, passive=None, speed=40):
        Characters.__init__(self, speed)  # over writing super class init function super().__init__(speed)
        self.__name: str = name
        self.__ability = ability
        self.__ult = ult
        self.__passive = passive
        Legends.counter += 1
        # print(self.__speed)  # __speed is private so it has no access to it

    @property  # decorator lt function be used as str -> print(obj.name)
    def name(self):
        return self.__name

    @name.setter  # decorator lt function be used as attribute -> obj.name = str
    def name(self, new_name):
        self.__name = new_name

    @name.deleter  # decorator lt function be used as attribute -> del obj.name
    def name(self):
        del self.__name

    @staticmethod
    def show_legend_number():  # static methode that can be used without class instance
        return Legends.counter

    @classmethod
    def factory_methode(cls, name, speed):
        if 100 > speed > 0:
            return cls(name=name, speed=speed)

    def address(self):  # if u don't over load the repr method in will return identity od obj
        # in case that u over load repr method
        identity = '<%s.%s object at %s>' % (
            self.__class__.__module__,
            self.__class__.__name__,
            hex(id(self))
        )
        return identity
        # return self.__repr__()  # showing the called methods

    # def __repr__(self):  # secondary return the str instant of memory location for debug
    #     return "Hero ({} , {} , {})".format(self.__name, self.__ability, self.__passive)

    def __str__(self):  # primary return the str instant of memory location
        return "Hero ({} , {})".format(self.__name, self.__ability)


if __name__ == '__main__':
    wrath = Legends("wrath")
    print(wrath.name)
    wrath.name = "mirage"
    print(wrath.name)
    print(wrath)
    print(wrath.address())
    del wrath.name
    # print(wrath.name)
    print(Legends.show_legend_number())
    print("***************'*'******")
    today = datetime.now()
    print(today)
    print(today.__str__())
    print(today.__repr__())  # magic tundther
    Legends.__init__()

