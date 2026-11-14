## these are used to store mutiple items in a single variable.
myList = ["Apple", "Banana", "Cherry"];
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(myList)
print(list1)
print(type(list1))
thisList = list(("Mangoes", "Apples","Kiwi"))
print(thisList)
print(thisList[2])
print(thisList[-1])


## chcking if something exists
if "Apples" in thisList:
    print("Yes, 'apples' is in this list")

### Changing item in the list
thisList[1] = "Black currant"
print(thisList)