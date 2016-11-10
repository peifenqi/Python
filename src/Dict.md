
# Dict 学习

## 初始环境


```python
# encoding: utf-8
```


```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
```

## 创建

* ### 用dict函数构建


```python
a = dict(one=1, two=2, three=3)
a
```




    {'one': 1, 'three': 3, 'two': 2}



* ### 用{key: value}创建


```python
b = {'one': 1, 'two': 2, 'three': 3}
b
```




    {'one': 1, 'three': 3, 'two': 2}



* ### 用dict函数加zip数组方式构建


```python
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
c
```




    {'one': 1, 'three': 3, 'two': 2}



* ### 用dict函数加数组方式构建


```python
d = dict([('two', 2), ('one', 1), ('three', 3)])
d
```




    {'one': 1, 'three': 3, 'two': 2}



* ### 3,2,1和1,2,3其实一样


```python
e = dict({'three': 3, 'one': 1, 'two': 2})
e
```




    {'one': 1, 'three': 3, 'two': 2}



* ### 也可以用Dict的copy()函数复制一份


```python
f = a.copy()
f
```




    {'one': 1, 'three': 3, 'two': 2}



* ### 也可以用Dict的copy()函数复制一份


```python
h= {'one', 'two', 'three'}
g = a.fromkeys(h, d.get('two'))
h, g
```




    ({'one', 'three', 'two'}, {'one': 2, 'three': 2, 'two': 2})



## 赋值


```python
a['one'] = 5
a
```




    {'one': 5, 'three': 3, 'two': 2}



## 增加一个值

* ### 1


```python
a['four'] = 4
a
```




    {'four': 4, 'one': 5, 'three': 3, 'two': 2}



## 取值

* ### 可以直接用[key]来引用值


```python
a['two'], b['one'], c['three']
```




    (2, 1, 3)



* ### 可以直接用values()来取所有的值


```python
d.values()
```




    dict_values([3, 1, 2])



* ### get函数可以按某个Key查询值，并赋予未查到后的默认值


```python
a.get('one', 0)
```




    5



* ### 描述dict中的元素


```python
a.items()
```




    dict_items([('four', 4), ('three', 3), ('one', 5), ('two', 2)])



## 删除

* ### 删除单个值


```python
del d['one']
d
```




    {'three': 3, 'two': 2}



* ### 全清


```python
f.clear()
f
```




    {}



## 判断长度


```python
len(a)
```




    4



## 判断是否有某个关键词


```python
'three' in e
```




    True




```python
'four' not in e
```




    True


