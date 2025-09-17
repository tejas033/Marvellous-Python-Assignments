# Recursion demo 7 print pattern * .. increase * by 1 up to 4

def RecursivePattern(counter):
    if(counter <= 4):
        print('*  ' * counter)
        RecursivePattern(counter + 1)

def main():
    RecursivePattern(1)

if __name__ == '__main__':
    main()