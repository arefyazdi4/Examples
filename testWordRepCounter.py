# strA = input("Enter words")
if __name__ == '__main__':

    strA = "Hellow world python world"
    listA = strA.split(" ")
    dicA = {word:listA.count(word)  for word in listA}

    print(dicA.items())