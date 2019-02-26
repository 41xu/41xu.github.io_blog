---
title:	Perceptron 感知机
tags:	统计学习方法 机器学习
---
<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

> 本文介绍感知机模型，叙述感知机的学习策略、损失函数。后介绍感知机学习算法，包括原始形式和对偶形式，并证明算法的收敛性。文末附相关代码

## 感知机简单介绍

感知机是Frank Rosenblatt 在Cornell Aeronautical Laboratory发明的一种人工神经网络，它可被视为一种最简单形式的前馈神经网络，是一种**二元线性分类器**。Frank Rosenblatt给出了相应的感知机学习算法，常用的有：感知机学习、最小二乘法、梯度下降。（相信看过CS229的朋友们对这个一定不陌生，我当时看的时候感知机看的是挺混乱的..那么在这里理清一下吧）感知机利用梯度下降法对损失函数进行极小化，求出可将训练数据进行线性划分的分离超平面，从而求得感知机模型。

🤔那感知机是怎么工作的呢？

感知机的输入是一些二进制$x_1, x_2, ...$，输出是$0,1$这样的单独一个的二进制。

![感知机图片](/img/统计学习方法/1.png)

这个例子里的感知机有三个输入：$x_1, x_2, x_3$。Rosenblatt提出了一种简单的计算输出(output)的规则：他引入了权重(weight)$w_1, w_2, ...$等实数来表示各个输入对于输出的重要程度。output到底是0还是1，由加权和$\sum_j w_j x_j$是否大于某一阈值(threshold value)决定。阈值也是一个实数，同时是神经元的一个参数。我们可以使用这样的一个式子来表示上面的过程
$$\begin{eqnarray} \mbox{output} & = & \left\{ \begin{array}{ll} 0 & \mbox{if } \sum_j w_j x_j \leq \mbox{ threshold} \\ 1 & \mbox{if } \sum_j w_j x_j > \mbox{ threshold} \end{array} \right. \tag{1}\end{eqnarray}$$

👆🏿看起来还有点笨重，通过这样的变换我们可以让他看起来更简单些。
- 用点乘代替$\sum_j w_j x_j$，即$w \cdot x \equiv \sum_j w_j x_j$ 其中$w$和$x$是向量，分别代表了权重和输入。
- 使用偏置(bias)来代替阈值threshold，即$b \equiv -\mbox{threshold}$
上面的式子就可以被重写为
$$\begin{eqnarray} \mbox{output} = \left\{ \begin{array}{ll} 0 & \mbox{if } w\cdot x + b \leq 0 \\ 1 & \mbox{if } w\cdot x + b > 0 \end{array} \right. \tag{2}\end{eqnarray}$$

这里的偏置可理解为感知机为得到输出为1的容易度。

这就是感知机的工作方式了🤔

让我们再来重复一次：感知机是一个二元线性分类器。尽管结构简单但是感知机能够学习并解决相当复杂的问题。然而感知机的主要本质缺陷是它不能处理线性不可分问题。

有了上面对感知机的了解接下来让我们来好好看看感知机定义和一些细节🤔。

## 感知机定义

假设输入空间（特征空间）是$\mathcal{X} \subseteq \mathbf{R^{n}}$，输出空间是$\mathcal{Y} = \{+1, -1\}$. 输入$x\in\mathcal{X}$表示实例的特征向量，对应于输入空间（特征空间）的点；输出$y\in\mathcal{Y}$表示实例的类别. 由输入空间到输出空间到如下函数

$$f(x)=sign(w \cdot x+b)$$

称为感知机.其中$w$和$b$为感知机模型参数，$w \in \mathbf{R^{n}}$叫做权值weight或权值向量，$b \in \mathbf{R^{n}}$叫做偏置bias，$w \cdot x$表示$w$和$x$的内积. sign是符号函数，
$$\begin{equation}sign(x)=\begin{cases}+1& \text{x \geq 0}\\-1& \text{x < 0}\end{cases}\end{equation}$$

感知机是一种线性分类模型，属于判别模型. 模型的假设空间是定义在特征空间中的所有线性分类模型或线性分类器. 

## 感知机的几何解释

对于线性方程 $w \cdot x+b=0$ 对应于特征空间$\mathbf{R^{n}}$中的一个超平面$S$，其中$w$是超平面的法向量，$b$是超平面的截距，这个超平面将特征空间划分为两个部分，位于两部分的点（特征向量）分别被分为正负两类，因此超平面$S$称为分离超平面.

![几何解释图片](/img/统计学习方法/2.png)

这里涉及到了几个概念：**超平面**、**超平面的法向量**，为啥$w$就是超平面的法向量了呢🤔，让我们来解释一哈

### 特征空间的超平面

平面是三维空间中定义的面如$Ax+By+Cz+D=0$，而超平面就是多维空间中定义的面. d维空间中的超平面有下面的方程确定：$w^Tx+b=0$. 其中$w$,$x$都是**d维列向量**，$x=(x_1,x_2,…,x_d)^T$为平面上的点，$w=(w_1,w_2,…,w_d)^T$为平面的法向量. $b$是一个实数，代表平面与原点之间的距离.

我们可以看到这个超平面的定义中就是涉及到了法向量的问题，而这个定义和我们的方程有非常像几乎是一模一样，所以接下来让我们探索一哈法向量到底是个啥。

### 超平面的法向量

在空间里，向量可以看作一个点（原点为起始点的向量），对于分离超平面方程里的向量$x$可以看作由坐标原点到超平面任意“点”的向量

## Reference

- [wikipedia](https://zh.wikipedia.org/wiki/%E6%84%9F%E7%9F%A5%E5%99%A8)
- [统计学习方法pdf](http://www.dgt-factory.com/uploads/2018/07/0725/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95.pdf)
- [Neural Networks and Deep Learning, Chap1](https://hit-scir.gitbooks.io/neural-networks-and-deep-learning-zh_cn/content/chap1/c1s1.html)
- [一个博客](https://www.cnblogs.com/OldPanda/archive/2013/04/12/3017100.html)
- [还是一个博客](https://blog.csdn.net/dream_angel_z/article/details/48915561)


> 转载需征得作者我本人同意并注明出处。
> 
> 联系我：📧: xu_sy11111@mail.dlut.edu.cn or wx: xsy9915
>
> 或经科学上网后在下方评论区留言即可
>
> 如有问题，欢迎指正。
