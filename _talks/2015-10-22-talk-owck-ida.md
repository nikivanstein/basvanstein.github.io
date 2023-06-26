---
title: "Optimally Weighted Cluster Kriging"
collection: talks
type: "talk"
permalink: /talks/2015-10-22-talk-owck-ida
venue: "IDA 2015"
date: 2015-10-22
location: "Saint-Etienne, France"
---

In business and academia we are continuously trying to model and analyze complex processes in order to gain insight and optimize. One of the most popular modeling algorithms is Kriging, or Gaussian Processes. A major bottleneck with Kriging is the amount of processing time of at least O(n3)  and memory required O(n2)  when applying this algorithm on medium to big data sets. With big data sets, that are more and more available these days, Kriging is not computationally feasible. As a solution to this problem we introduce a hybrid approach in which a number of Kriging models built on disjoint subsets of the data are properly weighted for the predictions. The proposed model is both in processing time and memory much more efficient than standard Global Kriging and performs equally well in terms of accuracy. The proposed algorithm is better scalable, and well suited for parallelization.
