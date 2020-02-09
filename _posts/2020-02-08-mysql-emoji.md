---
title:	字符串中的emoji插入mysql时引发的错误❌
tags:	mysql
---

> 很多条emoji引发的插入错误的血案（不是
>
> 这里记录一下避免以后踩坑。mysql真的好多坑。

## 问题描述

当数据的字符串中含有emoji时，在我想把他插入到mysql数据库中时，发现报错插不进去，导致数据少了一些。debug的过程排查的恐慌仔细审视俺的爬虫等过程就略去不说了。

最终得到的结论：emoji的编码格式和数据库里的编码格式不相符所以插不进去（废话）emoji是`utf8mb4` 数据库里是`utf8`格式（应该吧。我也不知道。还是说character_set_server的编码格式是utf8，表中的编码为utf6mb4所以插不进去..怎么乱七八糟的）

## 解决方案

摆在眼前的解决方案其实也很好想，有两个：

1. 将爬好的含emoji的数据转成utf8写入数据库，在将数据从数据库中导出为csv时再进行一个转换🤔

2. 将数据库的字符编码格式修改一下，从`utf8`->`utf8mb4`(这里表述的可能有些不准确

这个代码之后还要运行在朋友的PC上，考虑到这个其实方案1应该最合适（但是看起来好像有点复杂呢。方案2好像直接修改数据库配置就可以了呀。）那么两个都试一试吧。

### 方案二：改数据库编码

> 我记得我的mysql安装是homebrew安装的，但不管怎么装之前都没有查看过配置文件。而且之前没用过配置文件所以电脑里是绝对没有这个cnf的。难搞哦。

首先用命令查看`my.cnf`的位置

```
192:~ xusy$ mysql --verbose --help | grep my.cnf
                      order of preference, my.cnf, $MYSQL_TCP_PORT,
/etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf 
192:~ xusy$ 
```
可以看到电脑里有三个位置，但是之前根本没用过配置文件因此电脑里不存在这个文件，所以我们可以到[这里](https://www.fromdual.com/mysql-configuration-file-sample)下载到这个配置文件。之后

```
cd /etc
sudo vi my.cnf
```
创建my.cnf之后把刚刚的配置文件复制过来就可以了。

紧接着在刚刚的配置文件中把下面这个注释解除掉就可以了
```
# character_set_server           = utf8mb4                             # For modern applications, default in MySQL 8.0
```
之后重启mysql
```
brew services restart mysql
```

这样通过修改数据库的字符编码格式就可以将emoji插入到数据库中了。解决了解决了！！！

> 但是俺的小兄弟之后要在PC上跑这个代码呀，小兄弟并不是CS专业的电脑上连mysql也没装，更别提改数据库设置啦！而且电脑环境也不一样这篇博客小兄弟也参考不了。那么就试试第二个方法吧！

### 方法一：将emoji的编码转换成utf8后写入，导出时再转回去

算了emoji的编码转换好像很麻烦算了算了。先这样吧。

> PS：记录一下homebrew安装的mysql的启动、重启、进入等的命令。
```
# 启动 mysql, 并设置为开机启动
brew services start mysql
# 关闭 mysql
brew services stop mysql
# 重启 mysql
brew services restart mysql
# 进入mysql
192:~ xusy$ mysql -uroot -p
```