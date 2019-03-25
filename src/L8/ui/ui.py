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
        self.output(f"{message}: ")
        recv_input = self.connection.recv(32)
        return recv_input

    def output(self, message: str):
        self.connection.send(message.encode())


class ClientUI(RemoteUI):
    """
    A UI to be used by ClientPlayers connecting to a ServerGame. It inverts the flow of the RemoteUI
    so that the input flow is correctly simulated by the server, i.e., the input in a client calls
    the output of the RemoteUI and the output of the client calls the input of the RemoteUI
    """
    def __init__(self, connection: socket):
        super().__init__(connection)

    def initialize_ui(self):
        print("Initializing ClientUI...")

        if not self.connection:
            raise ConnectionError("Connection for ClientUI didn't start properly!")

    def input(self, message: str) -> str:
        user_input = input(f"{message}: ")
        super().output(user_input)
        return user_input

    def output(self, message: str):
        recv_message = super().input("Receiving from server...")
        print(recv_message)
