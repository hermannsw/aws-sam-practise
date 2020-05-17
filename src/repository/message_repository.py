from pynamodb.exceptions import DoesNotExist


class Repository:
    def __init__(self, model):
        self.model = model

    def get(self, pk, sk):
        res = [e for e in self.model.query(pk, self.model.user_id == sk)]
        if len(res) == 0:
            return DoesNotExist()
        return res[0]

    def save(self, data):
        try:
            message = self.model(**data)
            message.save()
        except Exception as e:
            return e
        return message

    def delete(self, data):
        self.model = data
        try:
            res = self.model.delete()
        except Exception as e:
            return e
        if res.get('ConsumedCapacity'):
            return self.model
