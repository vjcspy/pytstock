class DateNotSetError(Exception):
    def __init__(self, message='Please set date before run get data', code='com_technical_indicator_000'):
        self.message = message
        self.code = code
        super().__init__(self.message)


class ConfigNotSetError(Exception):
    def __init__(self, message='Please set config before run get data', code='com_technical_indicator_000'):
        self.message = message
        self.code = code
        super().__init__(self.message)
