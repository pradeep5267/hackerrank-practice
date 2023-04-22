def extraLongFactorials(n):
    # Write your code here
    s = 1
    for i in range(2, n+1):
        s*=i
    print(s)

extraLongFactorials(25)