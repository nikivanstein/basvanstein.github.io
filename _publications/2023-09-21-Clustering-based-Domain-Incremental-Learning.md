---
title: "Clustering-based Domain-Incremental Learning"
collection: publications
permalink: /publication/2023-09-21-Clustering-based-Domain-Incremental-Learning
date: 2023-09-21
venue: 'IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)'
citation: ' Christiaan Lamers,  René Vidal,  Nabil Belbachir,  Niki van Stein,  Thomas Bäck,  Paris Giampouras, &quot;Clustering-based Domain-Incremental Learning.&quot; IEEE/CVF International Conference on Computer Vision Workshops (ICCVW), 2023.'
authors:
- Christiaan Lamers
- René Vidal
- Nabil Belbachir
- Niki van Stein
- Thomas Bäck
- Paris Giampouras
doi: 10.1109/iccvw60793.2023.00363
paperurl: https://doi.org/10.1109/iccvw60793.2023.00363
arxiv: '2309.12078'
pdf: https://arxiv.org/pdf/2309.12078
venue_type: conference
abstract: >-
  We consider the problem of learning multiple tasks in a continual learning setting in which data
  from different tasks is presented to the learner in a streaming fashion. A key challenge in this
  setting is the so-called "catastrophic forgetting problem", in which the performance of the learner
  in an "old task" decreases when subsequently trained on a "new task". Existing continual learning
  methods, such as Averaged Gradient Episodic Memory (A-GEM) and Orthogonal Gradient Descent (OGD),
  address catastrophic forgetting by minimizing the loss for the current task without increasing the
  loss for previous tasks. However, these methods assume the learner knows when the task changes,
  which is unrealistic in practice. In this paper, we alleviate the need to provide the algorithm with
  information about task changes by using an online clustering-based approach on a dynamically updated
  finite pool of samples or gradients. We thereby successfully counteract catastrophic forgetting in
  one of the hardest settings, namely: domain-incremental learning, a setting for which the problem
  was previously unsolved. We showcase the benefits of our approach by applying these ideas to
  projection-based methods, such as A-GEM and OGD, which lead to task-agnostic versions of them.
  Experiments on real datasets demonstrate the effectiveness of the proposed strategy and its
  promising performance compared to state-of-the-art methods.
---
