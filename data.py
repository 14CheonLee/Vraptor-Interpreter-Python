"""
 Created by IntelliJ IDEA.
 Project: Vraptor-Interpreter
 ===========================================
 User: ByeongGil Jung
 Date: 2019-03-16
 Time: 오후 5:17
"""


class DataFrame(object):
    def __init__(self, name: str):
        self.name = name
        self.data = dict()

    def __str__(self):
        return "{}[{}] : {}".format(self.__class__.__name__, self.name, self.data.__repr__())

    def __repr__(self):
        return self.data.__repr__()


class Data(DataFrame):
    def __init__(self, name):
        super().__init__(name=name)

    def add(self, key: str = None, value: str = None, dataobj: DataFrame = None, **kwargs) -> None:
        if key is not None and value is not None:
            self.data[key] = value

        if dataobj is not None:
            self.data[self.name] = dataobj.data

        # If it has kwargs
        for key, value in kwargs.items():
            if type(value) == dict:
                self.data[key] = value
