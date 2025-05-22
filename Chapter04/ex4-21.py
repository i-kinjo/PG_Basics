try:
    a = input("type a num:")
    b = input("tupe anoeher:")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError,ValueError):
    print("Invalid input.")
