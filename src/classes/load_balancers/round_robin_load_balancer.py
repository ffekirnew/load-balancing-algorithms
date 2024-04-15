from typing import override

from classes.load_balancers.load_balancer import LoadBalancer
from classes.requests.request import Request


class RoundRobinLoadBalancer(LoadBalancer):
    def __init__(self, servers):
        super().__init__("Round Robin", [])
        self.index = 0

    @override
    def process_request(self, request: Request):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        print(f"Processing request on {server}")
