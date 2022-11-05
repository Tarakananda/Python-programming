def fun(a):
    if a<4:
        b=a/(a-3)
    print(b)
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("Zero Division Error Occured and handled")
except NameError:
    print("Name error occured and handled")