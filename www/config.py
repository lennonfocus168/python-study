from heapq import merge

from www import config_default

configs = config_default.configs

try:
    import config_override

    configs = merge(configs, config_override.configs)

    print(configs)
except ImportError:
    pass
