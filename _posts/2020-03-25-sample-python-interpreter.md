---
title:	Sample Python Interpreter (1)
tags:	编译原理
---

> write my own sampel python interpreter.

# Lexer

lexer实现词法分析，将读入的字符串转成合法的标记输出。

lexer也可以说成一个scanner，这个版本实现的是读入字符串之后对字符进行匹配处理。如果参考[qcx大佬的写法](https://medioqrity.github.io/2019/12/15/%E4%BB%8E%E9%9B%B6%E5%86%99%E4%B8%80%E4%B8%AA%E7%BC%96%E8%AF%91%E5%99%A8-Lexer%E4%B8%8EParser/)，以及创建丰富点的语法的话，使用进行正则匹配应该会更好一点。anyway先让他work起来再写别的版本优化吧。

ver-0.1中定义的token类型有：`int, float, +, -, *, /, (, )`

目前版本的构造`int/float`时还不能识别负数。**待改进**

# Parser

parser解释器，将输入的token转换成parsing tree。在这之前我们应该先定义好sample python的grammer

```
expr:	term((PLUS|MINUS) term)*
term:	factor((MUL|DIV)factor)* 
factor:	INT|FLOAT
```

有点像手动定义了优先级？