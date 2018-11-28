---
title:	Hadoop简单介绍
tags:	Hadoop
---

> 你是否像我一样对Hadoop这个东西感觉比较迷..？
>
> 你是否像我一样上课不听课甚至翘课于是现在感觉自己有点凉..？
>
> 那么..希望本篇文章及接下来的系列文章会对你有帮助(:D

首先照例[官网](http://hadoop.apache.org/docs/r1.0.4/cn/quickstart.html)是最好的教程！

## Hadoop概述

### Hadoop到底是个啥？

官方介绍：Hadoop是一个由Apache基金会所开发的，可靠的、可扩展的、用于分布式计算的分布式系统基础架构和开发开源软件。简单的说Hadoop软件库就是一个框架，通过这个框架你可以在计算机集群中对大规模的数据集进行分布式处理，可以理解成和操作系统的多线程并行有点像的一个东西。但是这个东西非常稳定，如果一个节点上的数据宕掉了还有神奇的机制可以保证数据备份在其他节点上，可以继续运行。


Hadoop架构核心包括: 
- 分布式文件系统 HDFS(Hadoop Distributed File System)
- 分布式计算系统 MapReduce
- 分布式资源管理系统 YARN

等下我们分别介绍一下这三个东西，先对他们有个大概的了解就好了

### Hadoop特点

-  高可靠性：数据存储有多个备份，集群设置在不同的机器上，可以防止一个节点宕机造成集群损坏。当数据处理请求失败后，Hadoop会自动重新部署计算任务，对出现问题的部分进行修复或通过快照方式还原到之前的时间点。

- 高扩展性：Hadoop在可用的计算机集群见分配数据并完成计算任务的，在集群中添加新的节点是很容易的，所以集群可以容易的进行节点的拓展完成集群的扩大。

- 高效性：Hadoop可以在节点间动态的移动数据，数据可在节点间进行并发处理，并保证节点的动态平衡，因此处理速度非常快。

- 高容错性：和前面的高可靠性差不多，文件系统HDFS存储文件时如果某台机器宕机了或者读取文档出错，系统调用其他节点上的备份文件保证程序顺利运行。如果启动的任务失败，Hadoop会重新运行该任务或启用其他任务完成这个任务未完成的部分。

- 低成本

- Hadoop基本框架用Java编写

## HDFS概述

### HDFS又是个啥？

HDFS是以分布式进行存储的文件系统，主要负责集群数据的存储和读取。是一个Master/Slave体系结构的分布式文件系统，HDFS实际上是运行在已有文件系统之上的一个文件系统，某种程度上你就理解成和你计算机的传统的文件系统差不多的一个东西就好了。同样的基本上面的Hadoop有什么特点HDFS就有这些特点。

歪一个楼我们可以顺便来回忆一下文件系统：

（以下内容来自屁屁踢）👇🏿 传统文件系统们

操作系统 | 文件系统
--- | ---:
Windows | FAT32,NTFS,exFAT
Linux/Android | ext3,ext4,xfs
macOS/iOS | HFS+,APFS
UNIX | JFS,JFS2,CDRFS,UDFS

分布式文件系统(Distributed File System):

文件系统管理的物理存储资源不一定直接挂载在本地节点上，而是通过计算机网络与节点相连。

常见类型：

- NFS (Network FileSystem): 比如说我们在做网安实验互相通过共享的网络文件夹里拷文件拷数字签名的时候可以把那个东西看成NFS，那种文件的组织形式和NFS我觉着有点像

- GFS (Google Filesystem)

- HDFS (Hadoop Distribute FileSystem): 就是我们这里的HDFS

话题再扯回来...！！！

### HDFS包括啥呢？

主要包括一个NameNode, 一个Secondary NameNode, 多个DataNode

首先我们要了解一下这几个概念:

#### 元数据

####


> 既然这篇001只是一个简单介绍..那么我就不讲太多啦！想看剩下的[HDFS更详细的介绍](http://hadoop.apache.org/docs/r1.0.4/cn/hdfs_design.html)可以到官网👈🏿去看看呢！这篇博只是想让我们后续的学习能更加顺利知道这是在讲什么想干嘛的一个东西..






