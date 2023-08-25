from modules.core.logging.logger import Logger
from modules.trade.generator.predefined_strategy_generator import PredefinedStrategyGenerator
import sys

try:
    generator = PredefinedStrategyGenerator(
        predefined_input="fixture/trade/predefined_inputs/generator/simple_sqz_mom_v1.json"
    )

    generator.generate()
except Exception as e:
    Logger().error("An error occurred: %s", e, exc_info=True)
finally:
    sys.exit(1)
