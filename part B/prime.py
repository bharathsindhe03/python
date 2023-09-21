num = int(input("enter num"))
flag = False
if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               flag = True

if (flag):
    print("is not a prime")
else:
    print("is a prime")                