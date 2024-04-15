from abc import ABCMeta, abstractmethod

from classes.requests.request import Request


class Server(metaclass=ABCMeta):
    power_levels = [1, 2, 3, 4, 5]

    def __init__(self, name: str, power: int) -> None:
        """
        :param name: Name of the server
        :param request_processing_time: Time taken (in milliseconds) by the server to process a request

        This class represents a simple server with a name and a request processing time
        """
        self.name = name
        self.power = power
        self.is_busy = False

    def __str__(self) -> str:
        return f"{self.name} - {self.power} Level Server"

    @abstractmethod
    def process_request(self, request: Request) -> None:
        pass
