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

然后修改core-site.xml, mapred-site.xml(这里是mapred-site.xml.template修改成.xml)

1. hadoop-env.sh

这个配置文件网上找到的大部分教程都要修改..但是..我看完我下载完之后打开的默认配置感觉不用改..于是没改..

---

2. core-site.xml
```
<configuration>
	<property>
		<name>fs.default.name</name>
		<value>hdfs://localhost:9000</value>
	</property>
	<property>
		<name>hadoop.tmp.dir</name>
		<value>/Users/xusy/Documents/Hadoop</value>  👈🏿是自定义的放hdfs文件的目录这里我就直接放在了我的Hadoop目录里
	</property>
</configuration>
```

---

3. mapred-site.xml
这个文件实际上我下载完的后缀是.xml.template(还是啥玩意反正是后面有个后缀，被我直接修改成了.xml)
```
<configuration>
  <property>
    <name>mapred.job.tracker</name>
    <value>localhost:9010</value>
  </property>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```

---

4. hdfs-site.xml
```
<configuration>
	<!--伪分布式-->
	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>
</configuration>
```
这里的变量dfs.replication指定了每个HDFS数据库的复制次数，通常为3，而我们要在本机建立一个伪分布式的DataNode所以这个值改成了1

---

5. yarn-site.xml

```
<configuration>
	<property>
		<name>yarn.nodemanager.aux-services</name>
		<value>mapreduce_shuffle</value>
	</property>

<!-- Site specific YARN configuration properties -->

<!-- 集群配置-->
  <!--      <property>
      <name>yarn.resourcemanager.hostname</name>
      <value>master</value>
      </property> -->

</configuration>
```


### 启动Hadoop

> 每次操作的时候都要进入这个Hadoop文件夹哦（当然我觉得如果把这个添加到环境变量里会不会好点..我也不知道我瞎说的

终端进入到Hadoop的文件夹下
我这里的文件夹就是
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

想要关闭的话..
```
./sbin/stop-all.sh
# stop-dfs.sh stop-yarn.sh
```

查看当前的hadoop运行情况:
```
xushiyaodeMacBook-Pro:libexec xusy$ jps
39696 SecondaryNameNode
39809 ResourceManager
39891 NodeManager
39507 NameNode
14375 
40267 Jps
39595 DataNode
```
测试一下我们能不能进入到overview界面呢！

NameNode - http://localhost:50070

ps:这里有一个Hadoop2和Hadoop3对应端口修改的表在下面：

NameNode端口

Hadoop2 | Hadoop3
--: | --:
50470 | 9871
50070 | 9870
8020 | 9820

Secondary NN端口

Hadoop2 | Hadoop3
--: | --:
50091 | 9869
50090 | 9868

DataNode端口

Hadoop2 | Hadoop3
--: | --:
50020 | 9867
50010 | 9866
50475 | 9865
50075 | 9864


----

在启动的时候网上还找到了其他版本的启动但是我没成功感觉就很迷不知道为啥..

比如说我们可以进入到libexec这个文件夹里执行hdfs/jps/start/等等操作

---



