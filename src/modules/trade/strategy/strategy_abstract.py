from abc import abstractmethod, ABC
from typing import Any, Self


class StrategyAbstract(ABC):
    def __init__(self, strategy_input: Any, filters: list, signals: list, actions: list, analysis: list):
        self._for_only_symbol = None
        self.strategy_input = strategy_input

    @abstractmethod
    def get_input_description(self):
        """
        Mỗi một strategy sẽ mô tả cách mà config của nó có thể được dynamic config như thế nào.

        Mục đích của việc này là để strategy generator có thể dynamic generate input trong tất cả các trường hợp.
        Từ đó chạy strategy này trong một phạm vi nào đó để tìm ra best input config

        Returns:
            TBD
        """
        pass

    def set_for_only(self, symbol: str) -> Self:
        """
        Sets the value of the _for_only_symbol attribute to the specified symbol.

        Args:
            symbol (str): The symbol to be set.

        Returns:
            Self: The modified instance of the class.

        """
        self._for_only_symbol = symbol

        return self

    def get_for_only(self):
        """
        Retrieves the value of the '_for_only_symbol' attribute.

        Returns:
            The value of the '_for_only_symbol' attribute.

        """
        return self._for_only_symbol
