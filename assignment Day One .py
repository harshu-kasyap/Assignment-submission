def cal_simple_interest(p, t, r):
    # Calculate simple interest
    h = (p * t * r) / 100

    print('The Simple Interest is : ', h)
    return h



p = float(input("Enter the principal amount : "))
t = float(input("Enter the number of years : "))
r = float(input("Enter the rate of interest : "))

cal_simple_interest(p, t, r)