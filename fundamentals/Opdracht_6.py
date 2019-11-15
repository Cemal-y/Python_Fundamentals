def list_manipulation(list, command, location, value=""):
    if command == "remove" and location == "end":
        return list.pop(-1)
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "beginning":
        list.insert(0, value)
        return list
    elif command == "add" and location == "end":
        list.append(value)
        return list


list1 = [1, 2, 3]

print(list_manipulation(list=list1, command="remove", location="beginning"))
print(list_manipulation(list=list1, command="remove", location="end"))
print(list_manipulation(list=list1, command="add", location="beginning", value=20))
print(list_manipulation(list=list1, command="add", location="end", value=30))
