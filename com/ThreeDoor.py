import random

temp = [0, 0, 1]

n = 100000  # 实验进行次数
size = 3  # 步长
result = 0  # 原来结果
rev = 0  # 换后结果

for i in range(n):
    data = temp
    random.shuffle(data)
    k = random.randint(0, size - 1)
    # 寻找data[j]==0 且j!=k 找到那只羊
    result += data[k]
    for j in range(size):
        if j == k:
            continue

        if data[j] == 0:
            break
    # 换门
    for jj in range(size):
        if jj != j and jj != k:
            break

    rev += data[jj]

print(result)
print(rev)  # 接近三分二
