# Exception2.py
# Exception handling .. try-except-finally

def main():
    Ans = 0
    try:
        no1 = int(input("Input no1: "))
        no2 = int(input("Input no2: "))

        Ans = no1 / no2

    except ValueError as valError:
        print("Please enter numeric value:", valError)
    except ZeroDivisionError as zobj:
        print("No1 cannot be divided by zero: ", zobj)
    except Exception as exc:
        print("Exception occurred: ", exc)
    
    finally: # Resource de-allocate
        print("Inside finally block")

    print("Division is: ", Ans)

if __name__ == "__main__":
    main()