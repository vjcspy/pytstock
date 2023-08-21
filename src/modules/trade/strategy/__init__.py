from modules.trade.strategy.simple_sqz_mom_strategy import SimpleSqzMomStrategy
from modules.trade.strategy.strategy_manager import StrategyManager

STRATEGIES = {
    SimpleSqzMomStrategy.name: {
        "class": SimpleSqzMomStrategy
    }
}

for key, value in STRATEGIES.items():
    StrategyManager.define_strategy(key, value)
