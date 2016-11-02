
def test_1():
    test = True
    test = not test
    if not test:
        print("Hello")
    else:
        print("Welcome")


def test_2(a,b,c):
    if a==2:
        print(b)
    elif c==1:
        print(a)
    else:
        print(c)

def test_3():
    t = (1,2,3)
    l = [1,2,3]
    d = {1:2, 3:4}
    print(type(t))
    print(type(l))
    print(type(d))

    print(t[0])

test_3()

# Invoke from here
# test_1()
# test_2(1,2,3)
