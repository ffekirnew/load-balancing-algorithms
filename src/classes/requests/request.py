class Request:
    def __init__(self, request_id: int, request_expensiveness: int) -> None:
        """
        :param request_id: Unique identifier for the request
        :param request_expensiveness: Level identifier for the expensiveness of the request
        different servers can handle different levels of expensiveness. Level 1 is the least expensive and level 5 is the most expensive

        This class represents a simple request with a unique identifier and an arrival time
        """
        self.request_id = request_id
        self.request_expensiveness = request_expensiveness

    @property
    def request_expensiveness(self) -> int:
        return self._request_expensiveness

    @request_expensiveness.setter
    def request_expensiveness(self, value: int) -> None:
        if value < 1 or value > 5:
            raise ValueError("Request expensiveness must be between 1 and 5")
        self._request_expensiveness = value

    def __str__(self) -> str:
        return f"Request {self.request_id}, Expensiveness: {self.request_expensiveness}"
