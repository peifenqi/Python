
# coding: utf-8

# # Dict 学习

# ## 初始环境

# In[77]:




# In[78]:

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})


# ## 创建

# * ### 用dict函数构建

# In[79]:

a = dict(one=1, two=2, three=3)
a


# * ### 用{key: value}创建

# In[80]:

b = {'one': 1, 'two': 2, 'three': 3}
b


# * ### 用dict函数加zip数组方式构建

# In[81]:

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
c


# * ### 用dict函数加数组方式构建

# In[82]:

d = dict([('two', 2), ('one', 1), ('three', 3)])
d


# * ### 3,2,1和1,2,3其实一样

# In[83]:

e = dict({'three': 3, 'one': 1, 'two': 2})
e


# * ### 也可以用Dict的copy()函数复制一份

# In[84]:

f = a.copy()
f


# * ### 也可以用Dict的copy()函数复制一份

# In[85]:

h= {'one', 'two', 'three'}
g = a.fromkeys(h, d.get('two'))
h, g


# ## 赋值

# In[86]:

a['one'] = 5
a


# ## 增加一个值

# * ### 1

# In[87]:

a['four'] = 4
a


# ## 取值

# * ### 可以直接用[key]来引用值

# In[88]:

a['two'], b['one'], c['three']


# * ### 可以直接用values()来取所有的值

# In[89]:

d.values()


# * ### get函数可以按某个Key查询值，并赋予未查到后的默认值

# In[90]:

a.get('one', 0)


# * ### 描述dict中的元素

# In[91]:

a.items()


# ## 删除

# * ### 删除单个值

# In[92]:

del d['one']
d


# * ### 全清

# In[93]:

f.clear()
f


# ## 判断长度

# In[94]:

len(a)


# ## 判断是否有某个关键词

# In[95]:

'three' in e


# In[96]:

'four' not in e

