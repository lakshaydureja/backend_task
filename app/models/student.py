from bson.objectid import ObjectId

class StudentModel:
    def __init__(self, name: str, age: int, address: dict):
        self.name = name
        self.age = age
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
        }

    @staticmethod
    def from_dict(data: dict):
        return StudentModel(
            name=data["name"],
            age=data["age"],
            address=data["address"],
        )