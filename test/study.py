set_zh = list()

with open(r'zh.txt', 'rb') as fzh:
    list_zh = fzh.readlines()

for zh in list_zh:
    tmp = zh.decode("utf-8").strip()
    temp = tmp[0:tmp.find("=")]
    if len(temp) > 0:
        set_zh.append(temp)

dict_en = dict()
with open(r'en.txt', 'rb') as fen:
    list_en = fen.readlines()

for en in list_en:
    tmp = en.decode("utf-8").strip()

    if len(tmp) <= 0:
        continue
    key, value = tmp.split('=')
    dict_en[key] = value

for zh in set_zh:
    print(zh + "=" + dict_en.get(zh, ""))
