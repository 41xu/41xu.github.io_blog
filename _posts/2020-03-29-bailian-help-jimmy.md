---
title:  百练1661: Help Jimmy
tags:   算法
---

> 一个普普通通但是条件有点多好绕的dp

## 描述 

[题目链接](http://bailian.openjudge.cn/practice/1661)

Jimmy老鼠在时刻0从高于所有平台的某处开始下落，它的下落速度始终为1米/秒。当Jimmy落到某个平台上时，游戏者选择让它向左还是向右跑，它跑动的速度也是1米/秒。当Jimmy跑到平台的边缘时，开始继续下落。Jimmy每次下落的高度不能超过MAX米，不然就会摔死，游戏也会结束。

设计一个程序，计算Jimmy到底地面时可能的最早时间。

**输入**

第一行是测试数据的组数t（0 <= t <= 20）。每组测试数据的第一行是四个整数N，X，Y，MAX，用空格分隔。N是平台的数目（不包括地面），X和Y是Jimmy开始下落的位置的横竖坐标，MAX是一次下落的最大高度。接下来的N行每行描述一个平台，包括三个整数，X1[i]，X2[i]和H[i]。H[i]表示平台的高度，X1[i]和X2[i]表示平台左右端点的横坐标。1 <= N <= 1000，-20000 <= X, X1[i], X2[i] <= 20000，0 < H[i] < Y <= 20000（i = 1..N）。所有坐标的单位都是米。

Jimmy的大小和平台的厚度均忽略不计。如果Jimmy恰好落在某个平台的边缘，被视为落在平台上。所有的平台均不重叠或相连。测试数据保证问题一定有解。

**输出**

对输入的每组测试数据，输出一个整数，Jimmy到底地面时可能的最早时间。

**样例输入**

```
1
3 8 17 20
0 10 8
0 10 13
4 14 3
```

**样例输出**

```
23
```
## 分析

首先这个题目好像很麻烦的样子（因为要输入的东西很多）那么我们先定义一个struct让她表示的简单些。就有了`platform`，之后分析题目，好像没说输入是按照高度顺序输入的平台呀，那么我们还要先对平台按照高度排个序，这里就用到`sort()`函数。之后再想一下，如果我们从上往下计算时间，上面平台的时间受下面平台时间的影响，所以应该从下往上计算，因此排序的时候应该从小到大排序。

接下来开始核心状态转移的计算了！！！

一个平台p[i],下面紧邻着如果有平台p[j]，那么首先看看这两个平台的`p[i].h-p[j].h<=maxh`是否成立，成立了才能下跳不然不能跳并且时间应该为INF。接下来还要分从左边跳还是右边跳，（左右都类似就以从左边为例）如果从左边跳，那么lefttime[i]应该等于：高度差+跳下去往左边走的时间+lefttime[j] 或者 高度差+跳下去往右边走的时间+righttime[j] 这两个取小的。然后就可以得到下面的代码

## code

```c++
#include<bits/stdc++.h>

#define INF 1000000
using namespace std;

struct platform {
    int h, l, r;
} p[1005];

bool compare(platform a, platform b) {
    return a.h < b.h;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x, y, maxh;
        cin >> n >> x >> y >> maxh;
        p[0].h = y;
        p[0].l = p[0].r = x;
        for (int i = 0; i < n; i++)
            cin >> p[i + 1].l >> p[i + 1].r >> p[i + 1].h;
        sort(p, p + n + 1, compare); // 低到高排序
        vector<int> lefttime(n + 1, INF);
        vector<int> righttime(n + 1, INF);
        lefttime[0] = p[0].h <= maxh ? p[0].h : INF;
        righttime[0] = p[0].h <= maxh ? p[0].h : INF;
        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j >= 0; j--) { // 下层的
                if (p[j].l <= p[i].l && p[j].r >= p[i].l && p[i].h - p[j].h <= maxh) {
                    lefttime[i] =
                            min((lefttime[j] + p[i].l - p[j].l), (righttime[j] + p[j].r - p[i].l)) + p[i].h - p[j].h;
                    break;
                } else lefttime[i] = p[i].h <= maxh ? p[i].h : INF;
            }
            for (int j = i - 1; j >= 0; j--) {
                if (p[j].l <= p[i].r && p[j].r >= p[i].r && p[i].h - p[j].h <= maxh) {
                    righttime[i] =
                            min((lefttime[j] + p[i].r - p[j].l), (righttime[j] + p[j].r - p[i].r)) + p[i].h - p[j].h;
                    break;
                } else righttime[i] = p[i].h <= maxh ? p[i].h : INF;
            }
        }
        cout<<min(lefttime[n],righttime[n])<<endl;
    }
}
```