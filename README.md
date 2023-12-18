## Quiz 1

### Syntax

Normal syntax

```python
if 5 > 2:
  print("Five is greater than two!")
```

Syntax error

```python
if 5 > 2:
print("Five is greater than two!")
```

Normal syntax

```python
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
```

Syntax error

```python
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
```

### Numerical data types

There are three numeric types in Python:

- int
- float
- complex

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Complex numbers are written with a "j" as the imaginary part.

Priority: complex > float > integer

### Sets

```python
a = set('abracadabra')
b = set('alacazam')

#union or sets
print(a | b)
print(a.union(b))

#intersection of sets
print(a & b)
print(a.intersection(b))
```

### Variable names

Officially, variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_). An additional restriction is that, although a variable name can contain digits, the first character of a variable name cannot be a digit.

```python
#Camel Case
var_name = 'numberOfCollegeGraduates

#Pascal Case 
var_name = 'NumberOfCollegeGraduates'

#Snake Case
var_name = 'number_of_college_graduates'
```

### Lambda function

A lambda function can take any number of arguments, but can only have one expression.

```python
x = lambda a : a + 10
print(x(5))
```

### Function arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly:

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

### Dictionaries

Dictionaries are used to store data values in key:value pairs.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```

The keys() method will return a list of all the keys in the dictionary.

The values() method will return a list of all the values in the dictionary.

The items() method will return each item in a dictionary, as tuples in a list.

```python
x = thisdict.keys()

x = thisdict.values()

x = thisdict.items()
```

Adding new value

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["color"] = "red"
print(thisdict)
```

Deleting value

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict["model"]
print(thisdict)
```

Sorting values

Sorting values without any extra parameters, sorts key values.

```python
>>> people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

>>> # Sort by key
>>> dict(sorted(people.items()))
{1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

>>> # Sort by value
>>> dict(sorted(people.items(), key=lambda item: item[1]))
{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
```

### Lists

Lists are used to store multiple items in a single variable.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

Add 

To add an item to the end of the list, use the append() method:

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

To insert a list item at a specified index, use the insert() method.

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

To append elements from another list to the current list, use the extend() method.

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

print(thislist)
```

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

```python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

print(thislist)
```

Remove elements 

The remove() method removes the specified item.

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

print(thislist)
```

The pop() method removes the specified index.

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)

print(thislist)
```

The del keyword also removes the specified index:

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]

print(thislist)
```

The clear() method empties the list.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()

print(thislist)
```

## Quiz 2

### Classes

A Class is like an object constructor, or a "blueprint" for creating objects.

To create a class, use the keyword class:

```python
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
```

To understand the meaning of classes we have to understand the built-in __init__() function. All classes have a function called __init__(), which is always executed when the class is being initiated. Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

The __str__() function controls what should be returned when the class object is represented as a string. If the __str__() function is not set, the string representation of the object is returned:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
```

Objects can also contain methods. Methods in objects are functions that belong to the object. Let us create a method in the Person class:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

```python
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```

Mdoify class objects

```python
p1.age = 40
```

Delete class objects

```python
del p1.age

del p1
```

### Inheritence

Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

Create a class named Student, which will inherit the properties and methods from the Person class:

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass
```

When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

```python
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

```python
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

Inherit methods of parents class:

```python
class ParentClass:
    def do_something(self):
        print("ParentClass is doing something")
class ChildClass(ParentClass):
    def do_something(self):
        super().do_something()
        print("ChildClass is doing something")
child = ChildClass()
child.do_something()
```
