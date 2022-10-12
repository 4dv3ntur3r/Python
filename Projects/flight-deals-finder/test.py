

def print_all_codes(n, m):
    UPPER_BOUNT = 0
    print("a")
    def print_01_codes(current, num_digits):
        if num_digits == 0:
            print(current)
        else:
            print_01_codes('0' + current, num_digits - 1)
            print_01_codes('1' + current, num_digits - 1)


    while True:


        for i in range(UPPER_BOUNT):
            print("b")
            print_01_codes('', n)
            if UPPER_BOUNT > m:
                break
            UPPER_BOUNT += 1
            print("b")
            print(UPPER_BOUNT)



print_all_codes(4, 5)