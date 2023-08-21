from typing import Any


class StrategyManager:
    _strategy_map = {}

    @staticmethod
    def define_strategy(key: str, spec: Any):
        StrategyManager._strategy_map[key] = spec

    def get_strategy_map(self):
        return self._strategy_map
