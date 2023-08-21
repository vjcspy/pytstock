from typing import Any

from modules.core.logging.logger import Logger
from modules.trade.error import TradeFileNotFoundError
from modules.trade.generator.strategy_generator_abstract import StrategyGeneratorAbstract
import simplejson as json
import os
import jsonschema

PRE_DEFINED_INPUT_SCHEMA_V1 = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "api": {"type": "string"},
        "strategy": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "input": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "data": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["type", "data"]
                }
            },
            "required": ["name", "input"]
        }
    },
    "required": ["strategy"]
}


class PredefinedStrategyGenerator(StrategyGeneratorAbstract):
    logger = Logger()

    def __init__(self, predefined_input: str):
        super().__init__()
        self.predefined_input = predefined_input
        self._load_input()

    def _load_input(self):
        # Lấy đường dẫn của thư mục project. Giả sử thư mục project của bạn là thư mục cha của thư mục 'src'
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), self.predefined_input))
        self.logger.info(f"Load input by path: {file_path}")
        if not os.path.exists(file_path):
            raise TradeFileNotFoundError()

        with open(file_path, 'r') as file:
            data = json.load(file)

        if data is not None:
            api = data['api']
            match api:
                case '@predefined_input/generator/v1':
                    return self._load_input_v1(data)

    def _load_input_v1(self, data: Any):
        # Validate input
        jsonschema.validate(data, PRE_DEFINED_INPUT_SCHEMA_V1)

        self.strategy = data['strategy']['name']

        if data['strategy']['input']['type'] == 'files':
            self.strategy_inputs = data['strategy']['input']['data']

    def generate(self):
        self.logger.info(f"Process generate with strategy '{self.strategy}' and input: {self.strategy_inputs}")
