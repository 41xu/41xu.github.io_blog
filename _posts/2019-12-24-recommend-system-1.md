---
title:	Recommender Systems Handbook -- 基于邻域的推荐
tags:	Recommend-System
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

> 《推荐系统》基于邻域的推荐方法综述 
>
> 书是图书馆随便借的，本博是Note+可能会有的代码吧Orz，可能会长期更新，善于挖坑不填坑的我也说不准233333

本篇博客讲的是**基于邻域**的推荐方法，简单介绍一下几个推荐方法。
## 概述：物品推荐方法

物品推荐方法可以分为两类：个性化和非个性化

### 个性化

- 基于内容的推荐：对某个用户已经评分过的物品分析其共同特点，然后将含有这些特点的新物品推荐给用户。只依赖内容信息，有`受限内容分析`和`过度专业化`的局限
- 协同过滤：利用系统中其他用户对物品的评分信息，找到和目标用户在一些物品上评分相似的用户，那么目标用户对新物品的评分和相似用户的评分也是相似的。
- 两者混合

上面提到的`受限内容分析`是指：系统只包含有限的用户信息或物品信息。`过度专业化`是指：只推荐与用户以评分物品高度相似的物品，实际的应用当中我们还是希望系统能推荐点有差异性并且仍然感兴趣的东西的，所以只推荐类似的东西就不太好！但是协同过滤可以推荐出来内容差异很大的物品。

### 协同过滤

协同过滤又可分成：

- 基于邻域的方法：根据用户对物品的历史评分预测用户对新物品的评分。基于邻域的推荐中有两种著名的方法：`基于用户的推荐`和`基于物品的推荐`
- 基于模型的方法：一般使用评分信息来学习预测模型。主要思想是使用属性构建用户和物品之间的联系，属性代表系统中物品和用户的潜在特征，如用户喜爱类别和物品所属的类别。常用方法: `Bayesian Clustering 贝叶斯聚类`, `Latent Semantic Analysis 潜在语义分析`, `Latent Dirichlet Allocation 潜在狄利克雷分布`, `Maximum Entropy 最大熵`, `Boltzmann Machines 玻尔兹曼机`, `Support Vector Machines 支持向量机`, `Singular Value Decomposition 奇异值分解`

`基于用户的推荐`：目标用户对某一物品的感兴趣程度是利用对该物品已评过分，并且和目标用户有相似评分模式的其他用户（近邻）来估计的

`基于物品的推荐`：根据某一用户对<u>相似于目标物品</u>（就是指被同一组用户评分且评分值相近的物品）的评分来预测该用户对目标物品的评分 

### 基于邻域

评价一个推荐系统的好坏可以通过预测分数来体现，在预测分数上，基于模型的要好于基于邻域的。但仅有预测的高精度不能保证用户的高效和满意的体验，推荐系统中影响用户体验因素的一个评判指标是：`serendipity 惊喜度`,即帮助用户找到感兴趣但本不可能发现的物品，是新颖性概念的一个扩展。

基于模型的方法在刻画用户爱好的潜在因素上有突出优势，但基于模型的可以断定用户是喜剧和浪漫电影的影迷，可以推荐给用户他不知道的浪漫喜剧，但是无法推荐给用户题材没有那么高度一致的电影，如恐怖恶搞喜剧。而基于邻域的方法可以捕捉到这些关联，（就是说恐怖恶搞喜剧和浪漫喜剧有什么关系啊模型很难推荐到因为模型觉得他们没什么关系，但是基于邻域的就可以通过近邻用户的打分来发现这些电影间的关联）。

基于邻域的优势主要有：简单性、合理性、高效性、稳定性。但是也存在着：覆盖度受限的问题，造成一部分物品一直得不到推荐。同时也存在：对评分的稀疏性和冷启动的问题较敏感，即系统中仅有很少评分或没用任何评分的新用户核心物品）

## 基于邻域的推荐

了解完推荐系统的一些分类和概念之后，接下来我们首先谈谈基于邻域的推荐。

### 符号定义

| 说明                                                       | 符号               |
| ---------------------------------------------------------- | ------------------ |
| 用户集合                                                   | $\mathcal{U}$      |
| 物品集合                                                   | $\mathcal{T}$      |
| 系统评分集合                                               | $\mathcal{R}$      |
| 评分可选的分数集合                                         | $\mathcal{S}$      |
| 用户$u\in \mathcal{U} $ 对物品$i\in\mathcal{T}$ 的评分     | $r_{ui}$           |
| 用户$\mathcal{U}$中已对物品$i$进行评分的用户集合           | $\mathcal{U_i}$    |
| 被用户$\mathcal{U}$评分的物品集合                          | $\mathcal{T_u}$    |
| 用户$u$和$v$评分的物品集合$\mathcal{T_u}\cap\mathcal{T_v}$ | $\mathcal{T_{uv}}$ |
| 同时对于物品$i$和$j$都进行评分的用户集合                   | $\mathcal{U_{ij}}$ |

注：1. $\mathcal{S}=\{1, 5\} 或 \mathcal{S}=\{喜欢，不喜欢\}$

​		2. $r_{ui}$取值不多于一个

### rating prediction & top-N

#### rating prediction

`rating prediction` 是为了预测某个用户对他未评价过的物品$i$的评分，当评分值存在时，很容易把这个问题变成一个回归/多分类的问题。

目标是用学习函数$f: \mathcal{U}\times\mathcal{T}\to\mathcal{S}$预测$u$对$i$的评分$f(u,i)$，$\mathcal{R}$可被分为$\mathcal{R_{train}}, \mathcal{R_{test}}$

评估预测准确性的标准：MAE(平均绝对误差), RMAE(均方根误差)

$$\mathrm{MAE(\mathit{f})}=\frac{1}{|\mathcal{R}_{test}|} \sum_{r_{ui}\in \mathcal{R_{test}}}|f(u,i)-r_{ui}|$$

$$\mathrm{RMAE(\mathit{f})}=\sqrt{\frac{1}{|\mathcal{R}_{test}|} \sum_{r_{ui}\in \mathcal{R_{test}}}(f(u,i)-r_{ui})^2}$$

#### top-N

当没有可用评分信息$\mathcal{R}$时，如仅有用户购买商品的列表，那么评估预测分数的准确性很明显是不可能的。这时对于寻找最优项问题就转换为向用户推荐感兴趣列表：列表$L(u_a)$包含用户$u_a$最感兴趣的$N$项物品，即 `top-N`.

评估`top-N`的质量也是将 $\mathcal{T}$ 分成用于训练函数$L$的训练集$\mathcal{T_{train}}$和测试集$\mathcal{T_{test}}$

令$T(u)\subset\mathcal{T}\cap\mathcal{T_{test}}$ 表$\mathcal{T_{test}}$中$u$认为相关的物品子集，如果用户的反馈是二元反馈，那么$T(u)$就是$u$所给评分为正的，如果$L(u_a)$中仅出现了用户购买或浏览过的物品，那么这些物品可直接用于表示$T (u)$

评估标准：precision(准确率), recall(召回率)

$$\mathrm{Precision(\mathit{L})}=\frac{1}{|\mathcal{U}|}\sum_{u\in\mathcal{U}}|L(u)\cap T(u)|/|L(u)|$$

$$\mathrm{Recall(\mathit{L})}=\frac{1}{|\mathcal{U}|}\sum_{u\in \mathcal{U}} |L(u) \cap T(u)|/|T(u)|$$

`top-N`的缺点是用户对$L(u)$中所有物品的感兴趣程度（权重）都被认为是等同的，解决办法：构造函数$L$可以使$u$对应的$L(u)$中包含的物品是根据$u$的感兴趣程度排列好的。如果测试集是随机划分的，对于每个$u$，其对应的$\mathcal{T_u}$中一个项可以表示为$i_u$，那么评估函数$L$的效果可以通过`Average Reciprocal Hit Rank, ARHR`平均逆命中率来衡量

$$\mathrm{ARHR(\mathit{L})}=\frac{1}{|\mathcal{U}|}\sum_{u\in \mathcal{U}}\frac{1}{\mathrm{rank}(i_u,L(u))}$$

 $rank(i_u,L(u))$表示$i_u$在$L(u)$中排名，如果$i_u \notin L(u),rank(i_u,L(u))=∞$

### 基于用户的评分预测 

基于用户的评分预测$r_{ui}$是利用$u$的对$i$做了评分的近邻，我们用$w_{uv} (u ≠v)$ 表示用户$u$和用户$v$的相似程度，用户$u$的$k$近邻表示为$\mathcal{N(u)}$, 在这些近邻中只有对$i$做评分的近邻可以用于预测$r_{ui}$，因此$k$近邻更进一步的应该是$N_i(u)$. 综上预测$r_{ui}$的评分策略可以为：

$$\hat{r}_{ui}=\frac{1}{|\mathcal{N_i(u)}|}\sum_{v \in \mathcal{N_i(u)}} r_{vi}$$

然而$u$和每个近邻的相似程度是不同的，因此我们可以将上面的东西标准化：

$$\hat{r}_{ui}=\frac{\sum_{v \in \mathcal{N_i(u)}} w_{uv}r_{vi}}{\sum_{v \in \mathcal{N_i(u)}} |w_{uv}|}$$

这里的分母其实可以再优化，用$w_{ui}^\alpha$代替，其中$\alpha>0$为放大因子，$\alpha>1$时，与$u$越接近的用户评分越重要



### 基于用户的分类预测





常用推荐系统数据集link

- [一个汉化版博客](https://www.cnblogs.com/lijinze-tsinghua/p/10768033.html)
- [又一个汉化版博客](https://blog.csdn.net/hellozhxy/article/details/81275133)
- [GroupLen](https://grouplens.org/datasets/movielens/)
- [推荐系统的专栏](https://www.jianshu.com/nb/21403842)

