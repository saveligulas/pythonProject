from MyCollection import MyCollection

myList = MyCollection()
for i in range(10):
    myList.add(i)
myList.remove_index(1)
print(myList.__str__())

