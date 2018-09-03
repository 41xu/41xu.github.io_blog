---
title:  Mac上连接服务器并安装phantomjs的记录
tags:   日志 phantomjs 爬虫 centos
---

> 只是一篇普通的记录博客，防止以后连接服务器时候忘记把文件夹放哪里啦hhhhhh
>
> 或者可以理解为一个环境搭建的记录博 (:D

### Mac上连接服务器

```
sudo su -
输入你的电脑密码
ssh -p 22 root@**.***.**.***
# ssh -p 端口号（一般服务器都把22端口号打开用来连接SSH的）用户名（一般用root就可以了 或者你还有什么其他用户也可以用）@ip
输入该用户的密码
完事！你已经从终端连上你的服务器啦！
```
> 虽然这个命令很简单网上随随便便也能找到但是为了防止下次自己忘记连接命令的时候...那就在这里存个档吧！

![连接成功！](/img/2018-09-02-连接服务器成功.png)

### centos下安装phantomjs
> 其实只是纯粹的担心自己忘记把这坨东西装到哪去了所以存个档

```
mkdir ~/bin/
cd ~/bin/
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
```
到这里tar解压的时候有些问题..是这样的...
```
tar -xjvf phantomjs-1.9.7-linux-x86_64.tar.bz2
然后有这样的东西出来：
tar(child): bzip2: Cannot exec: No such file or directory
tar(child): Error is not recoverable: exiting now
tar: Child returned status 2
tar: Error is not recoverable: exiting now
```
⬆️原因嘛...就是我们的服务器实在是太新了...(没错当时买服务器的时候就是为了os课的上机可以直接用Linux不想安装虚拟机来着...然后该装的东西都没装Orz)（咦刚刚发现用有道云来写markdown来着不能显示emoji...emmmmm)

接下来安装
```
yum install bzip2
```
安好了让我们再来解压一次！

**成功！！！**

接下来就是要讲phantomjs的可执行文件放到系统路径里
```
sudo ln -s ~/bin/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
```
centos下就装好phantomjs啦！
现在你可以测试一下这个无头浏览器有没有装好到底怎么样啦！

### 测试phantomjs

> 在测试之前发现了一个关于phantomjs的博客讲得还不错[链接](https://www.jianshu.com/p/9d408e21dc3a)

开始测试

因为对phantomjs并不是很熟悉所以决定直接用pyhon测试一下！

> 这里插播一条消息：我的服务器在测试的时候发现...python3不能用了？？？pip3也不能用了？？？于是现在在重新装python3
>
> 以上 所以接下来我们从测试phantomjs转播到centos装python3.6.6
> centos下安装python3的时候是从网上找的教程参考的 链接在这里 当然你也可以用我的这个教程，就是废话太多了点hhhh[python3安装教程]（https://blog.csdn.net/u013332124/article/details/80643371）

```
在/文件夹下  wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
tar zxvf Python-3.6.6.tgz
cd Python-3.6.6
./configure prefix=/usr/local/python3
make && make install
```
实际上像上面的这些安装过程网上的教程一搜一大把的，这里只是简单的记录一下

安装后的python路径是/ 然后被我移到了/usr/lib/ 下 和python2 一样的目录

接下来继续装pip3

> 先待续好了...
>
> 感觉自己搞不好了是怎么回事？？？甚至打算重置一下服务器是怎么回事？？？于是先上课好了...或许重置服务器Orz...上课之后大概会更新...机器学习笔记？



