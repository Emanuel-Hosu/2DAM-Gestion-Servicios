user = ""
numbers = []
while (user != exit):
    print("insert number and type exit for exit")
    user = input()
    
    if (user != "exit"):
        numbers.append(int(user))