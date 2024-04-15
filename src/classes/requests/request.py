class Request:
    expensiveness_levels = [1, 2, 3, 4, 5]

    def __init__(self, request_id: int, expensiveness: int) -> None:
        """
        :param request_id: Unique identifier for the request
        :param expensiveness: Level identifier for the expensiveness of the request
        different servers can handle different levels of expensiveness. Level 1 is the least expensive and level 5 is the most expensive

        This class represents a simple request with a unique identifier and an arrival time
        """
        self.request_id = request_id
        self.expensiveness = expensiveness

    @property
    def expensiveness(self) -> int:
        return self._expensiveness

    @expensiveness.setter
    def expensiveness(self, value: int) -> None:
        if value < 1 or value > 5:
            raise ValueError("Request expensiveness must be between 1 and 5")
        self._expensiveness = value

    def __str__(self) -> str:
        return f"Request {self.request_id}, Expensiveness: {self.expensiveness}"
