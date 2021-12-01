#### Variables  

A variable is like a box in the computer’s memory where you can store a single value.  
If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.  
  
* variable names cannot have 3 in the starting, and they are alphanumeric 
* For example
* 342var = 69 # this is not a valid variable
* Variables can't also have special symbols like + - < > 
* Variables can either start with _ or any letter but not numbers
  
Variables can store data of different types, and different types can do different things.  
The data types which are built into python by default are as follows :
1. String
2. Int
3. Float
4. Boolean



## Data types in Python  

A data type is a category for ­values, and every value belongs to exactly one data type. The most common data types in Python are Strings, floats, Integers and Boolean

* String  
    Textual data in python is handled by string variables. 
    Strings are written in a variety of ways that is We can wrap the text content around a single quote( ' ) or a double quote ( " )
    to Assign a variable string value we use the `=` operator like below:  
    `variable = "Your text here"`

    Strings are a type of sequence, which means we can index into the strings like 
    ``` 
        babu = 'babu'
        print(babu[0])
    ```
    This will print the first character of the string variable babu

* Integers:  
    Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    We can create an Int variable using the following code:
    `myNum = 3242`

* Floats  
    Floats or floating point numbers are numbers which have a decimal point in it. for example 2.34 or 3.14159 are considered as floating point numbers or Floats



    We can also perform basic arithmetic on Int and float like 
    Addition,   Subtraction, Multiplication, Division, Modulus and Power  
    All the operators and syntax is given in the below table  

    
|Operator|Description|Syntax|
|--- |--- |--- |
|+|Addition: adds two operands|x + y|
|–|Subtraction: subtracts two operands|x – y|
|*|Multiplication: multiplies two operands|x * y|
|/|Division (float): divides the first operand by the second|x / y|
|//|Division (floor): divides the first operand by the second|x // y|
|%|Modulus: returns the remainder when first operand is divided by the second|x % y|
|**|Power : Returns first raised to power second|x ** y|

##### type() function 
to get the type of any variable use type() function  
eg.
```python
area = 324
print(type(area))
```

###### print() function
The print function prints data to the screen

##### variable names
* variable names cannot start with a number and they are alphanumeric
* For example
* 342var = 69 # this is not a valid variable
* Variables can only contain letters, numbers, and underscores. Variable names can start with a letter or an underscore, but can not start with a number.
* Spaces are not allowed in variable names, so we use underscores instead of spaces. For example, use student_name instead of "student name".
* You cannot use Python keywords as variable names.
* python variable are case sensitive which means babu is not equal to BABU

#### taking user input in python
We can take user input in python using the input() function  
the input() function asks the user for input and when the user hits enter it returns that input as a string, the input() function takes an optional argument which is prompt, Prompt is displayed when asking the user input

#### Type casting
The process of converting one data type to another data type is called Typecasting or Type Coercion or Type Conversion.
we can use the functions int() float() or str() to convert any object into another object
for example we can convert the integer 2322 to a string using the below code  
```python
int_value = 2322
str_of_int = int(int_value)

print(type(str_of_int))

```
The above code will print :
`<class 'str'>`

##### round() function
The round() function returns a  number that is a rounded version of the specified number


### If else and elif in python

##### if block
The if statement is used for conditional execution: i.e executing certain block of code based on certain conditions. Only if the condition in the if block is true the code inside is executed.
An "if statement" is written by using the if keyword.
the syntax of an if block is like below:
```python
if (condition):
    code_block
    # do something
```
Eg.

```python
a = 33
b = 200
if b > a:
print("b is greater than a")
```
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".  

##### Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.  
an If statement without indention will will raise an error 



##### elif block
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".  
it extends an if statement to execute a different statement in case the original if expression evaluates to false .
The syntax of elif block is the same as if block
```python
elif (condition):
    # code to be executed if condition is true

```

Example  
```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

#### else block
if all the conditions in if and elif blocks failed the control will transfer to the else block
the syntax of else block is pretty simple :

```python
else:
    # condition to be executed
```
There can be zero or more elif parts, and the else part is optional.

#### comparision operators
comparision operators are used to compare two values in python  
here is a list of operators that you can use in python

##### Assume variable a holds 10 and variable b holds 20, then −
|Operator|Description|Example|
|--- |--- |--- |
|==| If the values of two operands are equal, then the condition becomes true. |(a == b) is not true.|
|!=| If values of two operands are not equal, then condition becomes true. |(a != b) is true.|
|<>| If values of two operands are not equal, then condition becomes true. |(a <> b) is true. This is similar to != operator.|
|>| If the value of left operand is greater than the value of right operand, then condition becomes true. |(a > b) is not true.|
|<| If the value of left operand is less than the value of right operand, then condition becomes true. |(a < b) is true.|
|>=| If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. |(a >= b) is not true.|
|<=| If the value of left operand is less than or equal to the value of right operand, then condition becomes true. |(a <= b) is true.|

#### String indexing
Strings are ordered sequences of character data. Indexing allows you to access individual characters in a string directly by using a numeric value. String indexing is zero-based: the first character in the string has index 0, the next is 1, and so on.
The syntax for string indexing is : `string_variable\[index\]`

```python
string_variable = "this is a string"
# example of indexing
print(string_variable[0]) # this will print the first character

# string index can be also a negative number
# If a negative index is supplised it will start conting from the end of the string
# for example
print(string_variable[-1]) # this will print the last character of the string
```

##### string slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.

syntax `string_variable\[start_index:end_index\] `
Remember that the substring string will start at the start_index and will not include the end_index (not included)

Example
Get the characters from position 2 to position 5 (not included):
```python
b = "Hello, World!"
print(b\[2:5\])
```
###### Slice From the Start
By leaving out the start index, the range will start at the first character:
eg. ` print(b\[:5\])  `

###### Slice To the End
By leaving out the end index, the range will go to the end:
eg. ` print(b\[2:\]) `


##### String concatenation
To concatenate, or combine, two strings you can use the + operator.
eg. `print("hello" + " world")`

##### String multiplication
if we use the multiply operator on strings it will multiply the string times the number
we can only multiply an integer with a string anything else will result in an error
eg `print("hello " * 5)`  
the above line will print hello 5 times


#### String function and methods

len() ==> Return the length (the number of items) of a given sequence (such as a string, list, or range) 
for eg. len("hello") will return 5

##### String methods:
\[stringVariable\].replace(find,replace) ==> Replaces every occurences of \[find\] with \[replace\]  
  
\[stringVariable\].split(\[seperator\])==> splits the string into the list based on the \[seperator\]  
  
\[stringVariable\].lower()==> Converts the \[stringVariable\] to lowercase  
  
\[stringVariable\].upper() ==> Converts the \[stringVariable\] to uppercase  
  
\[stringVariable\].isalpha() ==> Return True if all characters in the string are alphabetic and there is at least one character   

\[stringVariable\].find(sub\[, start\[, end\]\]) ==> Return the lowest index in the string where substring sub is found within the slice s\[start:end\]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.    

\[stringVariable\].isnumeric() ==> Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise.  

\[stringVariable\].isdigit() ==> Return True if all characters in the string are digits and there is at least one character, False otherwise.  