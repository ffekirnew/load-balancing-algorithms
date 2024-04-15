from abc import ABCMeta, abstractmethod

from classes.requests.request import Request


class Server(metaclass=ABCMeta):
    def __init__(self, name: str, request_processing_time: int) -> None:
        """
        :param name: Name of the server
        :param request_processing_time: Time taken (in milliseconds) by the server to process a request

        This class represents a simple server with a name and a request processing time
        """
        self.name = name
        self.request_processing_time = request_processing_time

    def __str__(self) -> str:
        return f"{self.name} - {self.request_processing_time}ms"

    @abstractmethod
    def process_request(self, request: Request) -> None:
        pass
