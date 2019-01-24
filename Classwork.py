def main():
    # prob1()
    prob2()


def prob1():
    test = []
    while 1 == 1:
        word = input("Enter a word: ")
        if word == "q" or word == "Q":
            print(test)
            break
        else:
            test.append(word)


def prob2():
    myList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Alex",
            "age": 21
        },
        {
            "name": "Bob",
            "age": 50
        }
    ]
    print(myList)
    while 1==1:
        setup = input("Sort by name or age: ")
        if setup.lower() == "q":
            break
        elif setup.lower() == "name":
            x = "name"
            def listFun(e):
                return e[x]
            myList.sort(key=listFun)
            print(myList)
        elif setup.lower() == "age":
            x = "age"
            def listFun(e):
                return e[x]
            myList.sort(key=listFun)
            print(myList)
        else:
            print("ERROR, Try Again!")

if __name__ == '__main__':
    main()
