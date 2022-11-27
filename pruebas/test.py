def myfunc(*args):
    my_list = []
    for n in args:
        if n%2 == 0:
            my_list.append(n)
        else:
            pass
    
    return my_list

print(myfunc(1,2,3,4))

