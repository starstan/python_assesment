def sort():
    print "Please write 4 words"
    n = 0
    myList = []
    while (n < 4):
        word = raw_input("Enter a word here")
        myList.append(word)
        n = n + 1

        print sorted(myList)


sort()

