import copy

from www import config_default


# 这个类主要可以使dict对象，以object.key 形式来替代  object[key]来取值
class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D


def merge(loc_res, loc_override):
    for k, v in loc_override.items():
        if k in loc_res:
            if isinstance(v, dict):
                merge(loc_res[k], v)
            else:
                loc_res[k] = v
        else:
            loc_res[k] = v


# 交叉合并
def merge_dict(loc_def, loc_override):
    result = copy.deepcopy(loc_def)
    merge(result, loc_override)
    return result


default_configs = config_default.configs

# configs默认为默认配置
configs = default_configs

try:
    from main.www import config_override

    # 这里把自定义配置文件里的配置项覆盖了默认配置里的配置项，
    # 如果自定义配置里没有定义，默认配置定义了，则还是沿用默认配置
    configs = merge_dict(default_configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)
