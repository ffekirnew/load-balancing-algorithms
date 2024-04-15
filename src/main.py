from classes.load_balancers.round_robin_load_balancer import RoundRobinLoadBalancer
from classes.requests.request import Request

request = Request(1, 1)
round_robin_load_balancer = RoundRobinLoadBalancer([])
print(request)
print(round_robin_load_balancer)
