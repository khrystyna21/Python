import worker_class


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.__id_ = id_
        self.__name = name
        self.__company = company
        self.__workers = []

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
    def workers(self):
        return self.__workers.copy()

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

    @workers.setter
    def workers(self, workers):
        self.__workers = workers

    # _______________to string_____________________________

    def __str__(self):
        return 'id: {}, name: {}, company: {}'.format(self.__id_, self.__name, self.__company)

    # _______________methods_____________________________

    @staticmethod
    def validate_worker_type(worker):
        if not isinstance(worker, worker_class.Worker):
            raise Exception("Wrong worker type")

    def new_worker(self, worker):
        self.validate_worker_type(worker)
        self.__workers.append(worker)
        return worker

    def remove_worker(self, worker):
        self.__workers.remove(worker)
