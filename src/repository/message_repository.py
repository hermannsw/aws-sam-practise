from pynamodb.exceptions import DoesNotExist


class Repository:
    def __init__(self, model):
        self.model = model

    def get(self, pk, sk):
        res = [e for e in self.model.query(pk, self.model.user_id == sk)]
        if len(res) == 0:
            return DoesNotExist()
        return res

    def save(self, data):
        try:
            message = self.model(**data)
            message.save()
        except Exception as e:
            return e
        return message

    def delete(self):
        pass
