
def gen_bin(prefix, digits):
    if digits == 0:
        print(prefix, '|', 'HEX-->', hex(int(prefix, 2))[2:], '|', 'DEC-->', int(prefix, 2))
    else:
        gen_bin(prefix + '0', digits - 1)
        gen_bin(prefix + '1', digits - 1)
    
n = int(input("Введите n разрядов двоичного числа :"))
gen_bin('', n)