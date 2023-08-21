from typing import Any

from modules.trade.strategy.strategy_abstract import StrategyAbstract


class SimpleSqzMomStrategy(StrategyAbstract):
    name = 'simple_sqz_mom_strategy'

    def __init__(self, strategy_input: Any):
        # Doi voi moi mot strategy thi cac config filters, signals, actions la hard code
        super().__init__(strategy_input, filters=[], signals=[], actions=[])

    def _load_input(self):
        pass

    def get_input_description(self):
        return {}
