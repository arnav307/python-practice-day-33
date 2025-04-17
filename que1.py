def stringconverter():
    try:
        user=input("Enter a string: ")
        convert=int(user)
        return convert
    except ValueError:
        print("String cannot be convert to integer")
        return 0
result=stringconverter()
print(result)

