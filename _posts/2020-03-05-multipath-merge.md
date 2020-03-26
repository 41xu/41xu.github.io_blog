---
title:	多路归并、败者树、置换选择的C++及golang实现
tags:	算法 数据结构
---

> background: PingCAP的[TiDB Online Courses, Section 1](https://university.pingcap.com/talent-plan/)
> 
> 是我不会的问题呢🤔今天才学的Go..还要用Go写
> 
> 学[数据结构](http://xusy2333.cn/2019/09/17/kaoyan-DS/)的时候就并没有把它实现过，现在可以写写试试。

## 问题是什么

> 用Go实现一个多路归并的Merge Sort：内存中有一个无序的int64数组，数组有16M个整数，要求使用多个goroutine对这个无序数组进行排序，使得有元素按照从小到大的顺序排列，并且排序的性能需要比单线程的Quick Sort快。
> 
> 根据框架完成demo，跑通测试程序，并使用go profile工具分析性能瓶颈 (课程还要有文档、单元测试、性能瓶颈分析，这些好像go都可以自动帮你执行？不过第一天接触Go不是很了解，所以以后写了文档会补上的)

## 分析一下问题

int64->8B,16M个整数->16x8=128MB(不过题里给的这个M是我理解的那个M吗..1024x1024？)

## reference

介绍了[大文件排序时的几个可以考虑的方法：内部归并、位图、多路归并](https://www.jianshu.com/p/dce6a43d4678)我觉得讲得还挺好的

介绍了[多路归并、败者树并附代码实现](https://blog.csdn.net/u010367506/article/details/23565421)

