---
title:	《推荐系统实战》笔记
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

> 《推荐系统实战》笔记，个人认为这本书只能算作科普读物，不是很推荐

## Chap1 好的推荐系统

推荐系统：根据用户的个性化需求推荐。

推荐方法：

1. 社会化推荐：你的好朋友给你推荐。你的沙雕网友给你推荐

2. 基于内容的推荐：以看电影为例，推荐系统通过你看过的电影，找到你喜欢的演员和导演，然后推荐这些他们的其他电影

3. 基于协同过滤的推荐：找到和自己历史兴趣相似的一群用户，然后根据他们最近在看啥给你推荐啥


​		

## Chap2 基于用户行为推荐

以电影推荐为例，我们是要推荐给用户他想看的电影，而不是预测评分，因此top-N问题比较合适

- 评价指标：Recall, Precision, Coverage, 新颖度
- 相似度计算：Jaccard, 余弦相似度, 加入物品流行度考虑

Jaccard公式：

$$w_{uv}=\frac{|N(u)\cap N(v)|}{|N(u)\cup N(v)|}$$

余弦相似度：

$$w_{uv}=\frac{|N(u)\cap N(v)|}{\sqrt{|N(u)||N(v)|}}$$

$cos\theta \in [-1,1]$一般情况相似度在$[0,1]$所以要对余弦值进行归一化，因此得到 $cos\_similarity=0.5+0.5*cos\theta$

```python
# 余弦相似度计算
from numpy import linalg as la
def cosSim(inA, inB): // inA, inB两个列向量
  num = float(inA.T * inB)
  denom = la.norm(inA) * la.norm(inB)
  return 0.5 + 0.5 * (num/denom)
```

计算余弦相似度时可以引入U-T-rating的倒排索引加快计算，但是numpy已经很快了所以我觉得没必要。

改进的根据用户行为计算用户兴趣相似度: 

$$w_{uv}=\frac{\sum_{i \in N(u) \cap N(v)} \frac{1}{log1+|N(i)|}}{\sqrt{|N(u)||N(v)|}}$$

 通过 $\frac{1}{log+|N(i)|}$ 惩罚了用户 $u,v$ 共同兴趣列表中热门物品对他们相似度的影响，即将物品对流行度（比如说近期热门排行榜topxxx这种就是流行度）计入考虑，可以提升推荐结果的质量

ps: 可以将用户评分数据划分成train和test之后再做个k折交叉验证

- 基于物品的协同过滤 `ItemCF` ：并不是利用物品内容属性计算物品相似度，而是通过分析用户的行为记录计算物品相似度。比如说喜欢A的用户也喜欢B所以A和B的相似度就很高

  - 计算物品相似度:

     $$w_{ij}=\frac{|N(i) \cap N(j)|}{|N(i)|}$$

    即喜欢物品$i$的用户有多少也喜欢$j$. $N(i),N(j)$为喜欢物品$i,j$的用户数. 同样的这个公式没有考虑到热门物品的影响因素，比说《流浪地球》这个2019蛮热门的电影，几乎人人都看过（夸张了）然后你计算发现《四个春天》和他的相似度很高，接近1，于是这么推荐了，那肯定不对啊！那任何物品都和热门物品有很高的相似度了！

  - 所以物品相似度计算可以这样改进：

    $$w_{ij}=\frac{|N(i)\cap N(j)|}{\sqrt{|N(i)||N(j)|}}$$ 

    惩罚了物品j的权重 -> 不就是余弦相似度Orz

  - 简单🌰: ![](/img/rs-example.png)

  - 得到物品间相似度后，可用如下公式计算用户u对物品j的感兴趣程度：

    $$p_{uj}=\sum_{i \in N(u) \cap S(j,K)} w_{ji}r_{ui}$$

- Inverse User Frequency: 用户活跃度对数的倒数，IUF认为活跃用户对物品相似度贡献应小于不活跃用户贡献，因此提出IUF用于修正物品相似度：

  $$w_{ij}=\frac{\sum_{u \in N(i) \cap N(j)} \frac{1}{log1+|N(u)|}}{\sqrt{|N(i)||N(j)|}}$$

   IUF提高哦了推荐结果的覆盖率，降低了流行度，改进了综合性能

- ItemCF的相似度矩阵按最大值归一化也可以提高推荐结果的准确率：

  $$w_{ij}=\frac{w_{ij}}{max_{j} w_{ij}}$$

   归一化提高了推荐的准确率，覆盖率和多样性

- 