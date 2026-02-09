filename = input("Enter the filname:")

try:
    file = open(filename,"r")
    content = file.read()
    print("\nFile content:\n")
    print(content)
    file.close()

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")

except Exception as e:
    print("Something went wrong:",e)