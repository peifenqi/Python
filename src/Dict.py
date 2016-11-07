# encoding: utf-8

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

# 创建
# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})
# f = a.copy()
# g = f.copy()

h= {'one', 'two', 'three'}
g = a.fromkeys(h, d.get('two'))
print h
print g


# 赋值 & 增加值
# a['one'] = 5
# a['four'] = 4 

# 删除
#del d['one']
#f.clear()


# 取值
# print a['two'], b['one'], c['three']
# print a.get('Java', 0)
# print a.items()


# 按关键词key查询
#print 'three' in e
#print 'four' not in e


# 判断长度
#print len(a)


