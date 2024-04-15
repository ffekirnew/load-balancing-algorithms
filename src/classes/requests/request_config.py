class RequestConfig:
    cost_variance_levels = [0, 1, 2, 3, 4, 5]
    rps_variance_levels = [0, 1, 2, 3, 4, 5]

    def __init__(self, rps: int, rps_variance: int = 0, cost_variance: int = 0) -> None:
        """
        :param rps: Requests per second
        :param rps_variance: Variance in the requests per second
        :param cost_variance: Variance in the cost of the requests

        This class represents the configuration for generating requests.
        """
        self.rps = rps
        self.rps_variance = rps_variance
        self.cost_variance = cost_variance

    @property
    def cost_variance(self) -> int:
        return self._cost_variance

    @cost_variance.setter
    def cost_variance(self, value: int) -> None:
        if value not in RequestConfig.cost_variance_levels:
            raise ValueError("Cost variance must be between 0 and 5")

        self._cost_variance = value

    @property
    def rps_variance(self) -> int:
        return self._rps_variance

    @rps_variance.setter
    def rps_variance(self, value: int) -> None:
        if value not in RequestConfig.rps_variance_levels:
            raise ValueError("RPS variance must be between 0 and 5")

        self._rps_variance = value
