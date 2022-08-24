#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.*,'hello', -87.8,-,/,+,6
# 
# 

# Ans: There are a total of 4 Operators and 3 Expressions, They are:
# Operators: *,-,/,+
# Expressions: & values'hello', 87.8, 6
# 
# 

# 2. What is the difference between string and variable?

# Ans: A Variable is used to store of information, and a String is a type of information you would store in a Variable. A String is a group of characters or a single character usually enclosed in Double quotes " " or single quotes ' '

# 3. Describe three different Data Types ?

# Ans: Three fundamental Data types in python are int, float, complex.

# int = contain only (integral values)
# float = contain only (decimal value)
# string = contain only(charcter value like "hello")

# Ans: Three fundamental Data types in python are int, float, complex.
# 
# int = contain only (integral values) float = contain only (decimal value) string = contain only(charcter value like "hello")

# 4. What is an expression made up of? What do all expressions do?

# Ans: An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If we ask Python to print an expression, the interpreter evaluates the expression and displays the result.

# In[4]:


4*5+20-50 # Is an Expression, The Python Interpreter Evaluates it to -10


# 5.This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# Ans: An expression is a combination of values, variables, and operators.When we type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression.
# 
# eg: 4*5+20-40 is an example of a statement
# 
# A statement is a unit of code that has an effect, like creating a variable or displaying a value.When we type a statement, the interpreter executes it, which means that it does whatever the statement says. In general, statements don’t have values.
# 
# eg: variable declaration and assignment are statements because they do not return a value

# In[5]:


#Example:
4*5+20-50 # Is a Expression
saurabh = 'INeuron FullStack DataScience' # Is a Statement
print("Hello World !") # Is a Expression Statement


# 6.After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# In[6]:


bacon = 22
bacon + 1
print(bacon)


# The variable bacon is set to 22 .The expression bacon + 1 does not reassign the value in bacon (that would the case if the expression is like bacon = bacon + 1 instead of bacon + 1)

# In[8]:


#Example Case#2
bacon=22
bacon=bacon+1 
print(bacon)


# 7.What should the values of the following two terms be?
# 'spam'+'spamspam'
# 'spam'*3
# 
# 

# In[10]:


print('spam'+'spamspam') # string concatenation
print('spam'*3) # string multiplication


# 8. Why is eggs a valid variable name while 100 is invalid?
# 

# Ans: As per python,Variable names cannot begin with a number. The python rules for naming a variable are :-
# 
# Variable name must start with a letter or the underscore character.
# Variable name cannot start with a number.
# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, & _ ).
# Variable names are case-sensitive (name, INEURON and ineuron are three different variables).
# The reserved words(keywords) cannot be used naming the variable.
# eg

# 9.What three functions can be used to get the integer,floating-point number,or string version of a value?

# Ans: The int(),float(),and str() functions will evaluate to the integer,floating-point number,string version of the value passed to them.

# 10.Why does this expression cause an error? how can you fix it?
# 'I have eaten ' + 99 + 'burritos.'

# In[16]:


#Ans: This cause of error is 99.because 99 is not a string. 99 must be typecasted to a string to fix this error. the correct way is:
print('I have eaten '+str(99)+' burritos')


# In[ ]:




