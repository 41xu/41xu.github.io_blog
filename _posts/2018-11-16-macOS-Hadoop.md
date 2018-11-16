---
title:	macOS下尝试搭建伪分布式Hadoop
tags:	Hadoop
---

首先照例[官网](http://hadoop.apache.org/docs/r1.0.4/cn/quickstart.html)是最好的教程！

## 环境准备

本机macOS Mojave 10.14.1 尝试在本地搭建伪分布式Hadoop

### jdk下载

到官网下载了jdk8 jdk-8u191-macosx-x64.dmg安装jdk 之后配置环境变量如下：
```
JAVA_HOME="Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home"
export JAVA_HOME
CLASS_PATH="$JAVA_HOME/lib"
PATH=".$PATH:$JAVA_HOME/bin"
export PATH="$HOME/.yarn/bin:$PATH"
```

> 根据[这个教程](https://zhuanlan.zhihu.com/p/31162356)装好了java

### ssh配置
先把系统偏好设置-共享-远程登录打开
```
ssh localhost
```
显示需要密码，实际上就是本机密码，这样不是很ok（具体到底哪里不ok我也不是很清楚

terminal中修改ssh设置
```
ssh-keygen -t rsa
[这里有啥输入的东西反正我们就按回车就完事]
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod og-wx ~/.ssh.authorized_keys
```
这时候我们再执行
```
ssh localhost
```
就会发现不需要密码ssh登陆了～就可以下载Hadoop了呢！

## Hadoop下载安装

### 官网下载

[官网提供的下载地址](https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-2.8.5/hadoop-2.8.5.tar.gz)我下载了2.8.5

下载完之后我把这个tar.gz放到了/Documents/Hadoop 文件夹里 
```
cd Hadoop
tar -zxvf hadoop-2.8.5.tar.gz
```
（实际上就是我们在终端里解压的2333）
接下来可以进入到我们的Hadoop目录里:

/hadoop-2.8.5/etc/hadoop/

然后修改core-site.xml, mapred-site.xml(这里是mapred-site.xml.templete修改成.xml),

### 启动Hadoop

终端进入到Hadoop的文件夹下
我这里就是
```
/Users/xusy/Documents/Hadoop/hadoop-2.8.5
```
执行
```
./bin/hdfs namenode -format
```
格式化文件系统（对namenode进行初始化)

接下来启动namenode & datanode （感觉就是启动dfs文件系统)
```
./sbin/start-dfs.sh
```
中间会有一个询问yes/no的我们输入yes就好了..
启动yarn
```
./sbin/start-yarn.sh
```
当然以上的命令都是在hadoop-2.8.5下面运行的

----

在启动的时候网上还找到了其他版本的启动但是我没成功感觉就很迷不知道为啥..




