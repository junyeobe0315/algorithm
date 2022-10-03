# this is Karatsuba's algorithm in python

def Karatsuba(a : int, b : int):
    a_size = len(str(a))
    b_size = len(str(b))
    assert a_size == b_size

    a = [i for i in str(a)]
    b = [i for i in str(b)]

    a0_ = str()
    b0_ = str()
    a1_ = str()
    b1_ = str()

    for i in range(a_size):
        if (i < a_size/2):
            a1_ += a[i]
            b1_ += b[i]
        else:
            a0_ += a[i]
            b0_ += b[i]
    
    a1 = int(a1_)
    a0 = int(a0_)
    b1 = int(b1_)
    b0 = int(b0_)

    print("a1 = {}, a0 = {}".format(a1, a0))
    print("b1 = {}, b0 = {}".format(b1, b0))

    z0 = a0 * b0
    z2 = a1 * b1
    z1 = (a0 + a1) * (b0 + b1) - z0 - z2
    print("z0 = {}, z1 = {}, z2 = {}".format(z0, z1, z2))
    
    output = z2*(10**a_size) + z1*(10**int(a_size/2)) + z0
    return output

if __name__ == "__main__":
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    output = Karatsuba(a,b)
    print("output : ",output)