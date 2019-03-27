import socket
from abc import abstractmethod, ABC


class UI(ABC):  # pragma: no cover

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


class ConsoleUI(UI):  # pragma: no cover

    def __init__(self):
        super().__init__()

    def initialize_ui(self):
        print("Initializing console UI")

    def input(self, message: str) -> str:
        return input(f"{message}: ")

    def output(self, message: str):
        print(message)


class DummyUI(UI):  # pragma: no cover
    """
    A dummy UI that doesn't do anything and is mostly used by AIPlayers
    """
    def initialize_ui(self):
        pass

    def input(self, message: str) -> str:
        pass

    def output(self, message: str):
        pass


class RemoteUI(UI):  # pragma: no cover
    """
    A UI to be used by a server to communicate with remote network players

    """
    def __init__(self, connection: socket):
        self.connection = connection
        super().__init__()

    def initialize_ui(self):
        print("Initializing Remote UI")

        if not self.connection:
            raise ConnectionError("Connection for RemoteUI didn't start properly!")

    def input(self, message: str) -> str:
        self.output(f"{message}")
        recv_input = self.connection.recv(1024).decode()
        return recv_input

    def output(self, message: str):
        self.connection.send(message.encode())
