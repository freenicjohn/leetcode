def my_sqrt(x):
    l, r = 1, x

    # x = 64
    # 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16
    # l                    m                       r
    # l        m           r
    # l  m     r
    #      lm  r
    # 1, 4, 9 = product
    # l  m  r

    while l < r:
        m = (l + r) // 2

        if m*m >= x:
            r = m
        else:
            l = m + 1

    return l
    

if __name__ == "__main__":
    print(my_sqrt(16))
    print(my_sqrt(64))
    
