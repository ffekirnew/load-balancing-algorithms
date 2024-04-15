from typing import override

from classes.load_balancers.load_balancer import LoadBalancer
from classes.requests.request import Request


class RoundRobinLoadBalancer(LoadBalancer):
    def __init__(self, servers):
        super().__init__("Round Robin", servers)
        self.index = 0

    @override
    def process_request(self, request: Request):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)

        server = self.servers[self.index]
        if server.is_busy:
            print("Server is busy, request is dropped")
        else:
            self.servers[self.index].process_request(request)
            print(f"Processing request on {server}")
