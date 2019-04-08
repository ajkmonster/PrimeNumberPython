for x in range(1,11,1):
    if x==2 or x==3:
        print(x,' is a prime number')
    elif x==1:
        print(x, 'is not a prime number')
    elif x%2 == 0 or x%3 == 0:
        print(x,' is not a prime number')
    else:
        print(x,' is a prime number')
