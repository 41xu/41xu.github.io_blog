---
title:	Generator in python
tags:	python 机器学习课产物
---

> 机器学习及python课的辣鸡产物
> 
> 生产的连学术垃圾都算不上...只能算是写作业顺手写的辣鸡介绍..
> 大家姑且随便一看，有啥问题欢迎下方评论区使用Disqus给我评论留言，评论区的加载可能需要科学上网
>
> 或者可以使用网站内我的其他社交网站的链接，欢迎发私信和邮件给我～

# Generators(生成器)

## 直接调用generator及generator的实现

官网对他的定义是：**Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.**

我们可以看出，生成器就是一个一边循环一遍计算的函数。生成器非常强大，当推算的算法比较复杂，用类似列表生成式的for循环无法实现时，可以用函数实现。

想要生成一个generators时，只需把生成列表的那个表达式的[]换成()即可
```
l=[x*x for x in range(10)]
# l is a list
g=(x*x for x in range(5))
# g is a generator
```
上式的输出结果
```
print(l)
print(g)
 >>> 
 <generator object <genexpr> at 0x10af1ac50>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
可以看出generator这个对象只有在你对他进行调用时才会有输出，我们直接print结果只是存放生成器这个对象的地址，而对比之下的list就是在我们还没调用时就已经生成好了的这么一个东西，比较占内存,生成list的时间也比较大，下面是一个对比：
```
import time

start=time.time()
nums=[i for i in range(1000000)]
end=time.time()
print(end-start)

start1=time.time()
numbers=(i for i in range(1000000))
end1=time.time()
print(end1-start1)
if end1-start1 < end-start:
    print("哇generator真的好快！")
```
输出：
```
0.07283806800842285
6.9141387939453125e-06
哇generator真的好快！
```
其他的关于generator的本文所涉及到的代码见[这个链接](https://github.com/41xu/41xu.github.io/blob/master/code_in_posts/generator-iterator.py)

## 函数中使用generator和yield关键字

### yield关键字

stackoverflow中关于yield&generator的最高票回答中是这样解释yield关键字的： **it is a keyword used like return, except the function will return a generator**

举个简单栗子：
```
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i

mygenerator = create_generator()
print(mygenerator)
# 这个的print结果和直接定义一个generator g=(i*i for i in range(3)) 结果是一样的
# 直接输出generator的内存地址

print(next(mygenerator))
print(next(mygenerator))
print("next over!")
for i in mygenerator:
    print(i)
```
结果
```
<generator object create_generator at 0x109cd3b48>
0
1
next over!
4
```
It is handy when you know your function will return a huge set of values that you will only need to read once.

### 函数和generator
> 一句话概括就是当你在函数中使用了yield时这个函数就变成了一个generator

当你使用yield时，yield所在函数的主体并不会被执行也不会被返回，而是返回一个定义里用了这个函数的generator，接下来就当成普普通通的generator使用即可。
变成了generator之后的函数，和generator一样，每次调用next()执行，遇到yield返回。下次调用的时候从上次返回的yield之后执行。

下面还是一个例子：
```
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(10)
print(f)
print(next(f))
print(next(f))
for i in f:
    print(i)
```
输出
```
<generator object fib at 0x10b388c50>
1
1
2
3
5
8
13
21
34
55
```
### 一些使用tips(待更新)


- **id()**函数： 用于获取对象的内存地址
```
id([object])
```

- tuple定义后不可被修改

- ‘+’加法可以实现对两个list/tuple的拼接

- tuple通过sorted()排序之后返回的结果是list


> 最后：[可真是个好东西！](https://wiki.python.org/moin)