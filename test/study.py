import copy

defa = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}

over = {
    'db': {
        'host': '192.168.0.100',
        'db11': {
            'host': 'i444'
        }
    }
}


def merge_dict(default, override):
    result = copy.deepcopy(default)

    def merge(l_result, l_override):
        for k, v in l_override.items():
            if k in l_result:
                if isinstance(v, dict):
                    merge(l_result[k], v)
                else:
                    l_result[k] = v
            else:
                l_result[k] = v

    merge(result, override)
    return result


result = merge_dict(defa, over)

print(defa)
print(over)
print(result)
