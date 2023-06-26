---
title: "Automatic Configuration of Deep Neural Networks with Parallel Efficient Global Optimization"
collection: talks
type: "Talk"
permalink: /talks/2019-07-02-talk-cnn-ijcnn
venue: "IJCNN 2019"
date: 2019-07-02
location: "Budapest, Hungary"
---

[More information here](https://ieeexplore.ieee.org/abstract/document/8851720?casa_token=W7U_7pA_Ad8AAAAA:7rq1Z4nAqShtzp_-5AffRG-h0e12dq4qClDmI6i05_4V7GXv_m23EAVvqhapyh25tio9XMIoBRA0)

Designing the architecture for an artificial neural network is a cumbersome task because of the numerous parameters to configure, including activation functions, layer types, and hyper-parameters. With the large number of parameters for most networks nowadays, it is intractable to find a good configuration for a given task by hand. In this paper the Mixed Integer Parallel Efficient Global Optimization (MIP-EGO) algorithm is proposed to automatically configure convolutional neural network architectures. It is shown that on several image classification tasks this approach is able to find competitive network architectures in terms of prediction accuracy, compared to the best hand-crafted ones in literature, when using only a fraction of the number of training epochs. Moreover, instead of the standard sequential evaluation in EGO, several candidate architectures are proposed and evaluated in parallel, which reduces the execution overhead significantly and leads to an efficient automation for deep neural network design.
