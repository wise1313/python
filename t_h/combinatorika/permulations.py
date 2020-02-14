def gen_permulations(n, prefix=''):
    """генерация перестановки чисел n < 10
    """
    print("prefix =======", prefix)
    if len(prefix) == n:
        print("***")
        print(prefix)
        print("***")
    else:
        for digit in range(0, n):
            digit = str(digit)
            if digit not in prefix:
                gen_permulations(n, prefix + digit)
    



n = int(input("Введите n :"))
gen_permulations(n)
