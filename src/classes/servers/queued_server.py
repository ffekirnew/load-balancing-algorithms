import time
from collections import deque
from typing import override

from classes.requests.request import Request
from classes.servers.server import Server


class QueuedServer(Server):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name, power)
        self.queue = deque([])

    @property
    def is_busy(self) -> bool:
        return len(self.queue) > 3

    @override
    def process_request(self, request: Request) -> None:
        if self.is_busy:
            print("Server is busy, request is dropped")
            return

        self.queue.append(request)
        request = self.queue.popleft()

        time.sleep(0.5 * (Server.power_levels[-1] - self.power))
        time.sleep(0.5 * (Request.expensiveness_levels[-1] - request.expensiveness))

        return
