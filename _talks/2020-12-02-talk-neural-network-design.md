---
title: "Neural Network Design: Learning from Neural Architecture Search"
collection: talks
type: "Talk"
permalink: /talks/2020-12-02-talk-neural-network-design
venue: "SSCI 2020"
date: 2020-12-02
location: "Canberra, Australia"
---

[More information here](https://youtu.be/DnP05lbE7dM)

Neural Architecture Search (NAS) aims to optimize deep neural networks’ architecture for better accuracy or smaller computational cost and has recently gained more research interests. Despite various successful approaches proposed to solve the NAS task, the landscape of it, along with its properties, are rarely investigated. In this paper, we argue for the necessity of studying the landscape property thereof and propose to use the so-called Exploratory Landscape Analysis (ELA) techniques for this goal. Taking a broad set of designs of the deep convolutional network, we conduct extensive experimentation to obtain their performance. Based on our analysis of the experimental results, we observed high similarities between well-performing architecture designs, which is then used to significantly narrow the search space to improve the efficiency of any NAS algorithm. Moreover, we extract the ELA features over the NAS landscapes on three common image classification data sets, MNIST, Fashion, and CIFAR-10, which shows that the NAS landscape can be distinguished for those three data sets. Also, when comparing to the ELA features of the well-known Black-Box Optimization Benchmarking (BBOB) problem set, we found out that the NAS landscapes surprisingly form a new problem class on its own, which can be separated from all 24 BBOB problems. Given this interesting observation, we, therefore, state the importance of further investigation on selecting an efficient optimizer for the NAS landscape as well as the necessity of augmenting the current benchmark problem set.   *Keywords*: Neural Architecture Search, AutoML, Deep Learning, Exploratory Landscape Analysis
