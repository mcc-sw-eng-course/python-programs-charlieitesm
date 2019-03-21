from abc import abstractmethod, ABC


class UI(ABC): # pragma: no cover

    def __init__(self):
        self.initialize_ui()

    @abstractmethod
    def initialize_ui(self):
        raise NotImplementedError

    @abstractmethod
    def input(self, message: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def output(self, message: str):
        raise NotImplementedError


class ConsoleUI(UI): # pragma: no cover

    def __init__(self):
        super().__init__()

    def initialize_ui(self):
        print("Initializing console UI")

    def input(self, message: str) -> str:
        return input(f"{message}: ")

    def output(self, message: str):
        print(message)


class DummyUI(UI): # pragma: no cover
    """
    A dummy UI that doesn't do anything and is mostly used by AIPlayers
    """
    def initialize_ui(self):
        pass

    def input(self, message: str) -> str:
        pass

    def output(self, message: str):
        pass
