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
