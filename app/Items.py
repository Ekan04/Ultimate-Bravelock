import os  # import os module
import random

directory = 'app/Icons'  # set directory path

itemList = []

for entry in os.scandir(directory):  
    if entry.is_file():  # check if it's a file
        #print(entry.name.removesuffix('.png'))
        itemList.append(entry.name.removesuffix('.png'))


def randomizeItems():
    itemsLeft = itemList.copy()
    inventory_size = 12
    selectedItems = []
    while inventory_size >= 1:
        item = random.choice(itemsLeft)
        selectedItems.append(item)
        itemsLeft.remove(item)
        inventory_size -= 1
    return selectedItems
        

hero1 = randomizeItems()
print(hero1)