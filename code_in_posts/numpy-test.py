import time

start = time.time()
nums = [i for i in range(1000000)]
end = time.time()
print(end - start)

start1 = time.time()
numbers = (i for i in range(1000000))
end1 = time.time()
print(end1 - start1)
if end1 - start1 < end - start:
    print("哇generator真的好快！")

# 一个没什么用的比较
g = (i for i in range(5))
l = [i for i in range(5)]
# print(sum(g))
print(sum(l))
print(next(g))
print(next(g))
print(sum(g))


# sum(g)直接放在前面就没办法调用next(g)这个函数因为g这个时候在内存里已经被全部生成出来了
# next(g)*2之后我们再调用sum(g)会发现输出结果是9，这个就和generator的实现方式有关系了！

# 官方对generator的实现
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()  # num>n抛出一个停止迭代的异常


sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
