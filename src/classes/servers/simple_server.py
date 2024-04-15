import time

from classes.requests.request import Request
from classes.servers.server import Server


class SimpleServer(Server):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name, power)

    def process_request(self, request: Request) -> None:
        self.is_busy = True
        time.sleep(0.5 * (Server.power_levels[-1] - self.power))
        time.sleep(0.5 * (Request.expensiveness_levels[-1] - request.expensiveness))

        self.is_busy = False

        return
