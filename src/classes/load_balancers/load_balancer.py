from abc import ABCMeta, abstractmethod
from typing import List

from classes.requests.request import Request
from classes.servers.server import Server


class LoadBalancer(metaclass=ABCMeta):
    def __init__(self, name: str, servers: List[Server]) -> None:
        """
        :param name: Name of the load balancer

        This class represents a base load balancer with a name
        """
        self.name: str = name
        self.servers: List[Server] = []

    def add_server(self, server: Server) -> None:
        """
        :param server: Server to add to the load balancer

        Adds a server to the load balancer
        """
        self.servers.append(server)

    def remove_server(self, server: Server) -> None:
        """
        :param server: Server to remove from the load balancer

        Removes a server from the load balancer
        """
        self.servers.remove(server)

    @abstractmethod
    def process_request(self, request: Request) -> None:
        """
        Processes a request by selecting a server and processing the request
        """
        pass

    def __str__(self) -> str:
        return f"{self.name} - {len(self.servers)} servers"
