# 4) Реализовать функцию bank, которая приннимает следующие аргументы:
# сумма депозита (pv), кол-во лет (r), и процент (n). 
# Результатом выполнения должна быть сумма по истечению депозита

#PV = 1 000 UAH
#r = 0,12 (12% годовых)
#n = 5 (лет)


def deposit_yesr(pv, n, r):
    return round((pv * (1 + r) ** n), 2)


def deposit_mos(pv, n, r):
    result = pv

    for _ in range(n):
        result = result + (result * r)
    return round(result, 2)

print(deposit_yesr(1000, 5, 0.12))

print(deposit_mos(1000, 5, 0.12))