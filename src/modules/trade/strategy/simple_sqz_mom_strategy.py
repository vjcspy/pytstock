from typing import Any

from modules.trade.strategy.strategy_abstract import StrategyAbstract


class SimpleSqzMomStrategy(StrategyAbstract):
    name = 'simple_sqz_mom_strategy'

    def __init__(self, strategy_input: Any):
        super().__init__(strategy_input, filters=[], signals=[], actions=[], analysis=[])

    def get_input_description(self):
        return {}
