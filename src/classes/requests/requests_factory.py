import time
from collections.abc import Generator
from random import choice
from typing import Any, Optional

from classes.requests.request import Request
from classes.requests.request_config import RequestConfig


class RequestsFactory:
    _instance = None

    def __new__(cls, config: Optional[RequestConfig] = None) -> "RequestsFactory":
        if cls._instance is None:
            cls._instance = super(RequestsFactory, cls).__new__(cls)
            cls._instance._config = config
            cls._instance._initialize_config()
        elif config is not None and config != cls._instance._config:
            raise ValueError(
                "RequestsFactory instance already exists with a different config."
            )

        return cls._instance

    def __init__(self, config: Optional[RequestConfig] = None):
        self._config = config
        pass

    def _initialize_config(self):
        # Initialize instance attributes using the config provided
        if self._config:
            self.rps = self._config.rps
            self.rps_variance = self._config.rps_variance
            self.cost_variance = self._config.cost_variance

    def generate_requests(self) -> Generator[Any, Any, Any]:
        request_id = 0
        while True:
            time.sleep(
                1
                / (self.rps + choice(range(-self.rps_variance, self.rps_variance + 1)))
            )
            yield Request(request_id, choice(Request.expensiveness_levels))
