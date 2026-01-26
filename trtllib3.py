# Activity 1 
lst = ['apple', 'banana', 'fig', 'grape', 'cherry', 'elderberry']
print("Original list:", lst)
print("Length of the list:", len(lst))

print('The first element is:', lst[0])
print('The last element is:', lst[-1])
print('The last element of this list is :', lst[5])

lst.append('kiwi')
print('The list after appending kiwi:', lst)

lst.remove('fig')
print('The list after removing fig:', lst)

lst.sort()
print('The sorted list is:', lst)

lst.reverse()
print('The reversed list is:', lst)

lst.clear()
print('The list after clearing all elements:', lst)
print(lst)

# Activity 2
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA',
    'email': 'john@example.com',
    'phone': '123-456-7890'
}

print('Original dictionary:', my_dict)
print('The value of key name us:', my_dict['name'])
print('The value of key age is:', my_dict['age'])

my_dict['state'] = 'New York'
print('The dictionary after adding state:', my_dict)

# Activity 3
def test(lst1):
    result = {}
    for item in lst1:
        result[item[0]] = item[1]
    return result

student_list = [('John', 25, 'New York'), ('Jane', 30, 'Los Angeles'), ('Jack', 28, 'Chicago')]

print(test(student_list))
print('nOrignal list of list :', student_list)
print('Convert the said list of list to a distionary :', test(student_list))