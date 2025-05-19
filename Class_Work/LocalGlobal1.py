# LocalGlobal.py

# you have to use "global" keyword if u have to use global variable in other methods

no = 11             # Global variable # try to avoid global variable

def fun():
    global no       # this is required if you have to modify the global variable
    # if you just want to access the global variable "global" keyword is not required
    # it is required only if you want to modify global variable's value

    print("FUN:: Inside fun()")
    x = 21                      # Local variable
    print("FUN:: Value of x is: ", x)
    print("FUN :: value of no: ", no)     # UnboundLocalError
    no = 12     
    print("FUN :: updated value of no: ", no)

def fun2(no):
    #global no   # "no" is assigned before global declaration
    print("FUN2 :: fun2(): ", no)

def sun():
    print("SUN :: Inside sun()")
    y = 51                      # Local variable
    print("SUN :: Value of y is: ", y)
    print("SUN :: value of no: ", no)

def main():
    print("MAIN :: Value of no before fun(): ", no)
    fun()
    fun2(21)
    print("MAIN :: Value of no after fun(): ", no)

    #sun()

if __name__ == "__main__":
    main()