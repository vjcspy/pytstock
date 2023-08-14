import logging

from modules.core.logging.custom_formatter import CustomFormatter

_log_instances = {}


def Logger(name: str = "root") -> logging.Logger:
    cached = _log_instances.get(name)
    if cached:
        return cached
    else:
        l = logging.getLogger(name)
        l.setLevel(level=logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        ch.setFormatter(CustomFormatter())
        l.addHandler(ch)
        _log_instances[name] = l
        return _log_instances[name]
