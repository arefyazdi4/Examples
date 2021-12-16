import sys
import math

# add new path to ur variables
# sys.path.append(r"c:\\Users")
# print(sys.path)

# show every thing in module
print(dir(math))
print("*************")
import Game.Level
print('#############')
import Game.Level.Start
Game.Level.Start.select_difficulty()

from Game.Level import Start as St
St.select_difficulty()
print('&&&&&&&&&')
if __name__ == '__main__':
    print(__name__)
    print(math.__name__)
    print("it runs ad main module")

else:
    print("it runs from module")

