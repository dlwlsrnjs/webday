a, b = input().split()
a = float(a)
b = float(b)


def sum(x, y):
    resultsum_1 = x + y
    resultsum_2 = y + x
    if (resultsum_1 > resultsum_2):
        return resultsum_1
    else:
        return resultsum_2


def miner(x, y):
    resultmi_1 = x - y
    resultmi_2 = y - x
    if (resultmi_1 > resultmi_2):
        return resultmi_1
        print(resultmi_1)
    else:
        return resultmi_2


def asam(x, y):
    resultas_1 = x * y
    resultas_2 = y * x
    if (resultas_1 > resultas_2):
        return resultas_1
    else:
        return resultas_2


def sep(x, y):
    resultsep_1 = x / y
    resultsep_2 = y / x
    if (resultsep_1 > resultsep_2):
        return resultsep_1
    else:
        return resultsep_2


def toto(x, y):
    result_1 = x ** y
    result_2 = y ** x
    if (result_1 > result_2):
        return result_1
    else:
        return result_2


l = sum(a, b)
r = miner(a, b)
c = asam(a, b)
d = sep(a, b)
e = toto(a, b)
p = l, r, c, d, e
print('%.6f'%max(p))
