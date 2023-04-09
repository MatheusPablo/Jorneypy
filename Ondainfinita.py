import time
while True:
    a = "-"
    b = "-"
    c = 37
    while True:
        print(a)
        a = a + "-"
        time.sleep(0.0001)
        if a == "-------------------------------------":
            break
    while True:
        print(b*c)
        c = c - 1 
        time.sleep(0.0001)
        if b*c == "-":
            break



