---
title:	重置服务器之后..的相关设置
tags:	centos 踩过的坑

---

### 重置服务器之后的解决ssh登陆failed的问题

![failed!](/img/hosts-linked-failed.png)

今天晚上重置服务器之后..

ssh -p 22 root@****失败了..

具体的失败及解决方法如上图

由于使用ssh登陆时，在你当前的本地主机会有相应的记录生成，当你重置服务器后，可能就会出现登录记录不匹配的情况，因此就不能成功登陆。
在本地主机上执行以下操作

下面是**Host key verfication failed**的解决办法：
```
cd ~/.ssh/
ls
会显示：>know_hosts
rm know_hosts
ssh root@**** # 这里就是你的域名/IP
然后会弹出yes/no的选项，我们根据提示yes然后输入你的服务器的密码就完成啦！
```
实际上..如果我们好好读报错信息的话..也是可以读出来这是现实的某个文件夹中的keys不匹配了我们把known hosts删除重置就好了

### 修改centos里root@XXXX 艾特后面的名字问题
```
cd /etc/
vi hostname
```
然后在hostname里添加上你想要的名字即可！一般好像都是添加自己的域名就可以了～
！！！当然还要记得重启服务器！！！

### centos上装python

[链接在这里，讲得挺好的](https://www.cnblogs.com/chenweixuan/p/6133929.html)

> 以上 简单的重置服务器中的踩坑存档，欢迎留言评论～

