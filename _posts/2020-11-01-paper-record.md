---
title:	generation/transfer文章整理
tags:	CV paper
---

> 整理的一些领域文章

## Basic Model

- PredRNN NIPS 2017
- Flow Grounded Video Prediction ECCV 2018
- *Non-Station* Texture Synthesis using Adversial Expansions SIGGRAPH 2018
- *Animating Langscape* SIGGRAPH 2019
- *SinGAN* ICCV 2019
- Structural-analogy from a Single Image Pair arxiv 2020, 感觉就是把SinGAN和Cycle GAN结合加了loss进行image-to-image translation
- *pix2pix_Conditional GAN* 一个image-to-image translation问题
- Cycle GAN
- pix2pixHD
- Bicycle GAN 
- Star GAN
- Multi-Content GAN
- SPADE
- Style GAN
- AdaIn
- Perceptural Loss
- Texture GAN: Controlling Deep Image Synthesis with Texture Patches

> TextureGAN也被拿出来做baseline比较过

---

## Text Effect Transfer

- Awesome Typography: Statistics-Based Text Effects Transfer -- Shuai Yang, Jiaying Liu, Zhouhui Lian, Zongming Guo. CVPR 2017

- A Common Framework for Interactive Texture Transfer -- Yifang Men. CVPR 2018 Spotlight 这个就是SATT，之后有一个SATT的 Neural based 版本

- DynTypo: Example-based Dynamic Text Effects Transfer -- Yifang Men. CVPR 2019

- Context-Aware Text-Based Binary Image Stylization and Synthesis -- Shuai Yang. ACM MM 2018 Oral, TIP 2019 

- Context-Aware Unsupervised Text Stylization -- Shuai Yang. ACM MM （好像和上面那个差不多

- Controllable Artistic Text Style Transfer via Shape-Matching GAN -- Shuai Yang. ICCV 2019 Oral 

- TET-GAN: Text Effects Transfer via Stylization annd Destylizaion -- Shuai Yang. AAAI 2019, TPAMI 2020

- TET141K: Artistic Text Benchmark for Text Effect Transfer -- Shuai Yang. TPAMI 2020

### Local patch

- Image Analogy. replace unstylized image patches with the corresponding stylized ones 

- Image Quilting. 根据content的梯度把style patch rearrange到content中

- CNNMRF. 这个还没看过不做评判

- Neural Doodles. semantic map 作为guidance还是要做patch match

- pix2pix

- Bicycle GAN 

- StarGAN

- Multi-Content GAN





