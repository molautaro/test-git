import amazing_function as af

if __name__ == "__main__":
    print("Please follow me on instagram")
    print("https://www.instagram.com/amazing_function")
    print("https://github.com/amazing_function")
    print("https://twitter.com/amazing_function")
    print("https://www.linkedin.com/in/amazing_function")
    x= int(input("Enter the first number"))
    y= int(input("Enter the second number"))
    power = int(input("Enter the power"))
    result = af.amazing_function(x,y,power)
    print(result)
else:
    print("Hello world, again!")