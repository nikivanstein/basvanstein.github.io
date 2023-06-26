---
title: "A Novel Uncertainty Quantification Method for Efficient Global Optimization"
collection: talks
type: "Talk"
permalink: /talks/2018-06-06-talk-uq-ipmu
venue: "IPMU 2018"
date: 2018-06-06
location: "Cádiz, Spain"
---

[More information here](https://link.springer.com/chapter/10.1007/978-3-319-91479-4_40)

For most regression models, their overall accuracy can be estimated with help of various error measures. However, in some applications it is important to provide not only point predictions, but also to estimate the “uncertainty” of the prediction, e.g., in terms of confidence intervals, variances, or interquartile ranges. There are very few statistical modeling techniques able to achieve this. For instance, the Kriging/Gaussian Process method is equipped with a theoretical mean squared error. In this paper we address this problem by introducing a heuristic method to estimate the uncertainty of the prediction, based on the error information from the k-nearest neighbours. This heuristic, called the k-NN uncertainty measure, is computationally much cheaper than other approaches (e.g., bootstrapping) and can be applied regardless of the underlying regression model. To validate and demonstrate the usefulness of the proposed heuristic, it is combined with various models and plugged into the well-known Efficient Global Optimization algorithm (EGO). Results demonstrate that using different models with the proposed heuristic can improve the convergence of EGO significantly.
