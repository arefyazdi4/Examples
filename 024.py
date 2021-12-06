# strA = input("Enter words")
strA = "Hellow world python world"
listA = strA.split(" ")
dicA = {word:listA.count(word)  for word in listA}

print(dicA.items())