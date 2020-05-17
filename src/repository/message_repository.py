class Repository:
    def __init__(self, model):
        self.model = model

    def get(self):
        pass

    def save(self, data):
        try:
            message = self.model(**data)
            message.save()
        except Exception as e:
            return e
        return message

    def delete(self):
        pass
