from datetime import datetime


class BaseModel:
    def to_dict(self):
        rval = {}
        for key in self.attribute_values:
            if isinstance(self.__getattribute__(key), datetime):
                rval[key] = self.__getattribute__(key)
                rval[key] = rval[key].strftime("%Y-%m-%dT%H:%M")
            else:
                rval[key] = self.__getattribute__(key)
        return rval
