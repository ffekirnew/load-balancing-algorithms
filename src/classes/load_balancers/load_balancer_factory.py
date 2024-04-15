from random import choice
from typing import List

from classes.load_balancers.load_balancer import LoadBalancer
from classes.load_balancers.round_robin_load_balancer import  classes.servers.server import Server
from classes.servers.simple_server import SimpleServer


class LoadBalancerFactory:
    @staticmethod
    def create_servers(number_of_servers: int) -> List[Server]:
        servers = []
        for i in range(number_of_servers):
            servers.append(SimpleServer(f"Server {i}", choice(Server.power_levels)))

        return servers

    @staticmethod
    def create_load_balancer(
        load_balancer_type: str, number_of_servers: int
    ) -> LoadBalancer:
        servers = LoadBalancerFactory.create_servers(number_of_servers)

        if load_balancer_type == "round_robin":
            return RoundRobinLoadBalancer(servers)

        raise ValueError(f"Invalid load balancer type: {load_balancer_type}")
