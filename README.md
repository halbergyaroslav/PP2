## Quiz 1

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
