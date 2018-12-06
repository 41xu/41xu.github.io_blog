---
title:	Hadoop Installation on MacOS 10.14
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

#### hadoop-env.sh

这个配置文件网上找到的大部分教程都要修改..但是..我看完我下载完之后打开的默认配置感觉不用改..于是没改..

---更新---

在这个配置文件中删掉了一些export前的注释, 关于JAVA_HOME, JSVC_HOME, HADOOP_HOME, HADOOP_HEAPSIZE=1000(或者2000), HADOOP_OPTS一些的注释都被去掉了，无需添加啥别的东西


#### core-site.xml
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

#### mapred-site.xml
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

#### hdfs-site.xml
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


#### yarn-site.xml

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

### 添加Hadoop环境变量

在~/.bash_profile中添加
```
# Setting path for Hadoop
HADOOP_HOME="/Users/xusy/Documents/Hadoop/hadoop-2.8.5"
export HADOOP_HOME
export PATH=$PATH:HADOOP_HOME/sbin:$HADOOP_HOME/bin

export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native/
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native:$HADOOP_COMMON_LIB_NATIVE_DIR"
```
具体路径根据hadoop的安装目录决定

下半部分的配置可以在上面提到的一些


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
格式化文件系统（对namenode进行初始化)（好像是只要初始化一次就好了就是最开始建系统的时候..之后如果每次启动你都初始化..那么是会有问题的！）

---
更新
---

在启动Hadoop，jps之后可能会出现你的namenode没起来的这个问题，这个时候就得格式化一下namenode，具体的话👇🏿

这里的namenode format的问题：由于namenode的信息是存在了系统的tmp文件夹下的，如果你到这里看的话是能看见这些的：

![tmp](/img/tmp.png)

每次启动的话tmp是会清空的，我也不知道咋回事反正，虽然我在core-site.xml文件里明明定义的是tmp存在了Hadoop文件夹下...但还是有这个问题..所以就重新在我的xusy用户下面新建了一个hadoop_tmp文件夹，把上面core-site.xml里存temp的那个文件夹路径改成了
```
	<property>
		<name>hadoop.tmp.dir</name>
		<value>/Users/xusy/hadoop_tmp</value> 
```
然后重新format就可以了..不知道再重新启动我的电脑的时候还会不会有这个问题..如果有那就再更新一下..		


接下来启动namenode & datanode （感觉就是启动dfs文件系统)
```
./sbin/start-dfs.sh
```
中间会有一个询问yes/no的我们输入yes就好了..
启动yarn
```
./sbin/start-yarn.sh
```
启动日志管理log的histroyserver
```
./mr-jobhistory-daemon.sh start histroyserver
```

当然以上的命令都是在hadoop-2.8.5下面运行的

想要关闭的话..
```
./sbin/stop-all.sh
# stop-dfs.sh stop-yarn.sh
```

查看当前的hadoop运行情况:
```
xushiyaodeMacBook-Pro:sbin xusy$ jps
39696 SecondaryNameNode
39809 ResourceManager
49810 JobHistoryServer
39891 NodeManager
39507 NameNode
69306 
39595 DataNode
73471 Jps
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


### 继续启动！！！

由于我们刚刚到配置..这里的namenode1对应的就是我们本机localhost啦～(所以下面的web查看正常输入的URL应该是namenode1+端口的)

overview查看！

查看HDFS：

http://localhost:50070

查看YARN：

http://localhost:8088

查看MR启动JobHistory Server(这里暂时出了问题..让我研究一下..)

http://localhost:19888


----

在启动的时候网上还找到了其他版本的启动但是我没成功感觉就很迷不知道为啥..

比如说我们可以进入到libexec这个文件夹里执行hdfs/jps/start/等等操作

> 最后的最后按照惯例..这个教程应该是有点点问题的..那么有问题/我哪里写错了欢迎下方评论区(得科学上网才能看见)/wx:xsy9915/email:xu_sy11111@mail.dlut.edu.cn 联系我！
> 写这个教程只是因为..这门课学校老师给的安装教程是Windows+ubuntu+centos7安装的..得有虚拟机我觉得好麻烦..而且macOS明明巨好用！！！ 后续会更新Spark课程相关内容以及Scala相关内容！欢迎收藏本站持续更新！如需引用请标明出处！





