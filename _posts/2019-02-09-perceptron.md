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



## 感知机简单介绍

感知机是Frank Rosenblatt 在Cornell Aeronautical Laboratory发明的一种人工神经网络，它可被视为一种最简单形式的前馈神经网络，是一种**二元线性分类器**。Frank Rosenblatt给出了相应的感知机学习算法，常用的有：感知机学习、最小二乘法、梯度下降。（相信看过CS229的朋友们对这个一定不陌生，我当时看的时候感知机看的是挺混乱的..那么在这里理清一下吧）感知机利用梯度下降法对损失函数进行极小化，求出可将训练数据进行线性划分的分离超平面，从而求得感知机模型。

🤔那感知机是怎么工作的呢？

感知机的输入是一些二进制`x1,x2,...`，输出是`0/1`这样的单独一个的二进制。

![感知机图片](/img/统计学习方法/1.png)

这个例子里的感知机有三个输入：`x1,x2,x3`。Rosenblatt提出了一种简单的计算输出(output)的规则：他引入了权重(weight)`w1,w2,...`等实数来表示各个输入对于输出的重要程度。output到底是0还是1，由加权和$\sum_j w_j x_j$是否大于某一阈值(threshold value)决定。阈值也是一个实数，同时是神经元的一个参数。我们可以使用这样的一个式子来表示上面的过程
$\begin{eqnarray} \mbox{output} & = & \left\{ \begin{array}{ll} 0 & \mbox{if } \sum_j w_j x_j \leq \mbox{ threshold} \\ 1 & \mbox{if } \sum_j w_j x_j > \mbox{ threshold} \end{array} \right. \tag{1}\end{eqnarray}$

让我们再来重复一次：感知机是一个二元线性分类器。尽管结构简单但是感知机能够学习并解决相当复杂的问题。然而感知机的主要本质缺陷是它不能处理线性不可分问题。

有了上面对感知机的了解接下来让我们来好好看看感知机定义和一些细节🤔。

## 


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
