#!/usr/bin/env python
# coding: utf-8

# #Q 1 What exactly is []?

#  ans it is a list with empty
# Q 2 In a list of values stored in a variable called spam, how would you assign the value hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# In[3]:


spam =[2, 4, 6, 8, 10]


# In[4]:


spam[2] = "hello"


# In[5]:


spam

#Q 3 Lets pretend the spam includes the list ['a', 'b','c','d'] for the next three queries.
# In[15]:


spam = ["a","b","c","d"]


# In[ ]:


# Q 4 What is the value of spam[int(int(3 * 2) / 11)]?


# In[98]:


spam[int(int('3' * 2) / 11)]


# In[ ]:


# Q 5 What is the value of spam[-1]?


# In[19]:


spam[-1]


# In[ ]:


# Q 6 What is the value of spam[:2]?


# In[22]:


spam[:2]


# In[ ]:


#Q 7 Let's pretend bacon has the list [3.14, 'cat' 11, 'cat' True] for the next three questions.


# In[24]:


bacon.index("cat")


# In[23]:


bacon = [3.14,"cat",11,"cat","true"]


# In[ ]:


# Q 8How does bacon.append(99) change the look of the list value in bacon?


# In[25]:


bacon.append(99)


# In[26]:


bacon


# In[29]:


# Q 9How does bacon.remove('cat') change the look of the list in bacon?


# In[30]:


bacon.remove("cat")


# In[31]:


bacon


# In[32]:


#Q 10 What are the list concatenation and list replication operators?


# In[33]:


a= [1,2,3,4]


# In[34]:


b=[3,4,5,6]


# In[35]:


a+b


# In[36]:


lst  = [3,4,5]
lst1 = lst*4


# In[37]:


lst1


# In[38]:


Q 11 What is difference between the list methods append() and insert()?


# In[39]:


# list insert value at last of list


# In[40]:


a= [1,2,3,4,5]


# In[41]:


a.append(9)


# In[42]:


a


# In[43]:


# insert function insert value by indexes


# In[44]:


a= [1,2,3,4]


# In[46]:


a.insert(2,12)


# In[47]:


a


# In[48]:


# Q 12What are the two methods for removing items from a list?


# In[56]:


a= ["top",2,3,4,5]


# In[57]:


a.remove(3)


# In[58]:


a # it will remove 3 by math 3 is present in list or not


# In[61]:


a.pop() # it will  remove the last element from list


# In[63]:





# In[64]:


#13. Describe how list values and string values are identical.


# In[69]:


'''both are iterabel 
      both are mutable 
    can be replaced by other element
    can be sum to simler'''
    


# In[70]:


get_ipython().set_next_input('Q 14 Whatt is  the difference between tuples and lists');get_ipython().run_line_magic('pinfo', 'lists')


# In[71]:


'''tuple define by ()
but list define by []
tuple immutable 
list is mutable '''


# In[ ]:


#15. How do you type a tuple value that only contains the integer 42?


# In[74]:


tup = (42)


# In[75]:


tup


# In[ ]:


# Q 16 How do you get a list value's tuple form? How do you get a tuple value's list form?


# In[76]:


lis = [2,3,6]


# In[78]:


t = tuple(lis)


# In[79]:


t


# In[80]:


type(t)


# In[81]:


tp = (1,6,8)


# In[82]:


b =list(tp)


# In[83]:


b


# In[84]:


type(b)


# In[85]:


# Q 17 Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?


# In[86]:


#thay can contain dynamicly  as per requirment
a= [1,2,3,4,"foo"]


# In[87]:


a = 34


# In[88]:


a= "str"


# In[89]:


a=(4,5,6,7)


# In[90]:


# Q 18 How do you distinguish between copy.copy() and copy.deepcopy()?


# In[95]:


# ANS The copy.copy() function will do a shallow copy of a list,


# In[96]:


#The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the list


# In[ ]:




