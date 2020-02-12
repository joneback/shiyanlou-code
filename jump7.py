for i in range(1,101):
    if 0==i%7 or 7==i%10 or 7==i//10:
        continue;
    else:
        print(i)
