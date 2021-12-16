dataFile = open("A:\\Programming\\Python\\code training\\text.txt" , mode="r")

print("***************************")
dataFile.seek(0)
print(dataFile.read())
print("***************************")
dataFile.seek(0)
print(dataFile.readline())
print("***************************")
print(dataFile.readlines())

