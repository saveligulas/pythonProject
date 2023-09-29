from MyCollection import MyCollection

myList = MyCollection()
for i in range(10):
    myList.add(i)
myList.add_end(999)
for i in range(5):
    myList.remove_index(0)
myList.remove_object(999)
print(myList.__str__())

