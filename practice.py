# # declare a list with numbers 1 to 5 and add 6 at the end of list
# num_list = [1, 2, 3, 4, 5]
# print(num_list)
# num_list.append(6)
# print(num_list)

# 2 Create a tuple with values 1 - 5
# num_tuple = {1, 2, 3, 4, 5}
# num_list = list(num_tuple)
# print(num_list[:3])
# # You cannot append this
#
# # 3 declare a dictionary of a shopping list
# shopping_list = {
#     'fruits': 5.00,
#     'eggs' : 2.50,
#     'veg' : 8.99
# }
# print(type(shopping_list))
#
# print(shopping_list['eggs'])
#
# # 4 replace a value in a dictionary
# shopping_list['fruits'] = 6
#
# print(shopping_list)
#
#
# # 5 declare a method that adds two given arguments
# def add(num1, num2):
#     return num1 + num2
#
# print(add(3, 5))

# 6 Create a class called person with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
test = Person('Dono', 14)
print(test.name)
print(test.age)

# 7
class Student(Person):
    def __init__(self, name, age, studentID, course):
        super().__init__(name, age)
        self.studentID = studentID
        self.course = course
student_test = Student('Dono', 18, 1, 'DevOps')
print(f'{student_test.name}, {student_test.age}, {student_test.studentID}')

# 8 create a dictionsary with 4 items and prices and get total cost
q8_dict = {'eggs': 2.58, 'paint': 4.99, 'pork': 3.49, 'cheese': 700}
# total_cost = sum(q8_dict.values())
# print(total_cost)

# 9 create function to do it
def total(dict):
    return sum(dict.values())

print(total(q8_dict))

# 10 have a shopping list and add kiwis to it
q10_dict = q8_dict
q10_dict['kiwis'] = 3.49
print(q10_dict)

# 11
q10_list = list(q10_dict.keys())
for item in q10_list:
    if item == 'pork':
        break
