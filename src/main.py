from classes.load_balancers.load_balancer_factory import LoadBalancerFactory
from classes.load_balancers.round_robin_load_balancer import RoundRobinLoadBalancer
from classes.requests.request_config import RequestConfig
from classes.requests.requests_factory import RequestsFactory


class Program:
    def __init__(self) -> None:
        self.load_balancer = LoadBalancerFactory.create_load_balancer("round_robin", 5)
        requests_configuration = RequestConfig(200)
        self.requests_factory = RequestsFactory(requests_configuration)

    def run(self) -> None:
        for request in self.requests_factory.generate_requests():
            self.load_balancer.process_request(request)


if __name__ == "__main__":
    program = Program()
    program.run()
