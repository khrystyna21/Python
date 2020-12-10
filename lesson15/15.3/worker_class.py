import boss_class


class Worker:
    def __init__(self, id_, name, company, boss: boss_class):
        self.validate_boss_type(boss)
        self.__id_ = id_
        self.__name = name
        self.__company = company
        self.__boss = boss
        boss.new_worker(self)

    # _______________getters_____________________________

    @property
    def id_(self):
        return self.__id_

    @property
    def name(self):
        return self.__name

    @property
    def company(self):
        return self.__company

    @property
    def boss(self):
        return self.__boss

    # _______________setters_____________________________

    @id_.setter
    def id_(self, id_):
        self.__id_ = id_

    @name.setter
    def name(self, name):
        self.__name = name

    @company.setter
    def company(self, company):
        self.__company = company

    @boss.setter
    def boss(self, boss):
        self.validate_boss_type(boss)
        self.__boss.remove_worker(self)
        self.__boss = boss
        self.__boss.new_worker(self)


    # _______________to string_____________________________

    def __str__(self):
        return 'id: {}, name: {}, company: {}, boss: ({})'.format(self.__id_, self.__name, self.__company, self.__boss)

    # _______________methods_____________________________

    @staticmethod
    def validate_boss_type(boss):
        if not isinstance(boss, boss_class.Boss):
            raise Exception("Wrong boss type")




