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

称为感知机.其中$w$和$b$为感知机模型参数，$w \subseteq \mathbf{R^{n}}$叫做权值weight或权值向量，$b \subseteq \mathbf{R^{n}}$叫做偏置bias，$w \cdot x$表示$w$和$x$的内积. sign是符号函数，
$$\begin{equation}sign(x)=\begin{cases}+1& \text{x \geq 0}\\-1& \text{x < 0}\end{cases}\end{equation}$$




## Reference

- [wikipedia](https://zh.wikipedia.org/wiki/%E6%84%9F%E7%9F%A5%E5%99%A8)
- [统计学习方法pdf](http://www.dgt-factory.com/uploads/2018/07/0725/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95.pdf)
- [Neural Networks and Deep Learning, Chap1](https://hit-scir.gitbooks.io/neural-networks-and-deep-learning-zh_cn/content/chap1/c1s1.html)

> 转载需征得作者我本人同意并注明出处。
> 
> 联系我：📧: xu_sy11111@mail.dlut.edu.cn or wx: xsy9915
>
> 或经科学上网后在下方评论区留言即可
>
> 如有问题，欢迎指正。
