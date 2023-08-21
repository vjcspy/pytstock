from abc import abstractmethod
from typing import Any

from modules.trade.strategy.strategy_abstract import StrategyAbstract


class StrategyGeneratorAbstract:
    @abstractmethod
    def generate(self):
        pass
