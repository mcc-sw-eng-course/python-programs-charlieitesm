import json


# Exercise 14
class MyPowerList:

    def __init__(self):
        self._backend = []

    # Exercise 14
    def read_from_text_file(self, filename: str) -> bool:

        if not filename.endswith(".json"):
            filename += ".json"

        with open(filename, "r") as file:
            self._backend = json.load(file)
        return True

    # This will allow us to print the representation of this object as a str that can be concatenated
    def __str__(self):
        return f"[{', '.join([str(x) for x in self._backend])}]"
