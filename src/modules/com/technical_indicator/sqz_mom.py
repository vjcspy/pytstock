from modules.com.technical_indicator.technical_indicator_abstract import TechnicalIndicatorAbstract
from modules.com.util.price_history_helper import PriceHistoryHelper


class SqzMomConfig:
    length_bb: int
    mult_bb: int
    length_kc: int
    mult_kc: float

    def __init__(self, length_bb=20, mult_bb=2, length_kc=20, mult_kc=1.5, use_true_range=True,
                 cal_source_func=lambda row: row['close']):
        self.use_true_range = use_true_range
        self.cal_source_func = cal_source_func
        self.mult_kc = mult_kc
        self.length_kc = length_kc
        self.mult_bb = mult_bb
        self.length_bb = length_bb


class SqzMom(TechnicalIndicatorAbstract):
    def validate_input(self) -> bool:
        return True

    def set_config(self, config: SqzMomConfig):
        self._config = config

        # Check if input data is satisfied with config
        self.validate_input()

    def get_data(self):
        super().get_data()
        config: SqzMomConfig = self.get_config()
        price_helper: PriceHistoryHelper = self.get_price_history_helper()
        # Define date
        self.get_price_history_helper().set_date(self.get_date())

        # Calculate BB
        source = price_helper.get_row_data_by_source_func(config.cal_source_func)
        basic = price_helper.sma(config.length_bb)
        dev = config.mult_bb * price_helper.stdev(config.length_bb)
        upperBB = basic + dev
        lowerBB = basic - dev

        # Calculate KC
        ma = price_helper.sma_by_source_func(config.length_kc, config.cal_source_func)
