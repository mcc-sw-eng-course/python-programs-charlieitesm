import json


# Exercise 15
class User:

    NEXT_ID = 1

    def __init__(self, name: str, address: str, phone: str, email: str):
        self.user_id = User.generate_id()
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    @staticmethod
    def generate_id() -> int:
        new_id = User.NEXT_ID
        User.NEXT_ID += 1

        return new_id

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}"


# This class will allow us to serialize the User objects to JSON easily
class UserJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class UsersDatabase:

    def __init__(self):
        self.users = {}

    def new_user(self, name: str, address: str, phone: str, email: str):
        new_record = User(name, address, phone, email)
        new_record_id = new_record.user_id
        self.users[str(new_record_id)] = new_record
        return new_record_id

    def search(self, user_id):
        return self.users.get(str(user_id), None)

    def save_to_text_file(self, filename: str):
        if not filename:
            raise ValueError("The filename can't be None nor empty")

        if not filename.endswith(".json"):
            filename += ".json"

        with open(filename, "w") as file:
            json.dump(self.users, file, cls=UserJsonEncoder)

        return True

    def load_from_file(self, filename: str):
        self.users = {}

        if not filename.endswith(".json"):
            filename += ".json"

        with open(filename, "r") as file:
            data = json.load(file)

        max_id = -1

        for k in data.keys():
            record = data[k]
            deserialized_user = User(record["name"], record["address"],
                                     record["phone"], record["email"])
            deserialized_user_id = int(k)
            max_id = deserialized_user_id if deserialized_user_id > max_id else max_id
            deserialized_user.user_id = deserialized_user_id
            self.users[str(k)] = deserialized_user

        # This will prevent ID collisions from the deserialized data
        User.NEXT_ID = max_id + 1

        return True

