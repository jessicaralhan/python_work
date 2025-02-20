def simple_interest(p,t,r):
    print("principal is",p)
    print("time period is", t)
    print("rate of interest is", r)

    si = (p * r * t)/100
    print("simple interest is ", si)
    return si

simple_interest(3,4,9)


