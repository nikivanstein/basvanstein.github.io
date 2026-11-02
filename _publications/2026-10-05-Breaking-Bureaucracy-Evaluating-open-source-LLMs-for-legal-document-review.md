---
title: "Breaking Bureaucracy: Evaluating open-source LLMs for legal document review"
collection: publications
permalink: /publication/2026-10-05-Breaking-Bureaucracy-Evaluating-open-source-LLMs-for-legal-document-review
date: 2026-10-05
venue: 'arXiv preprint arXiv:2610.06345'
citation: ' Farrukh Baratov,  Niki van Stein,  Suzan Verberne, &quot;Breaking Bureaucracy: Evaluating open-source LLMs for legal document review.&quot; arXiv preprint arXiv:2610.06345, 2026.'
authors:
- Farrukh Baratov
- Niki van Stein
- Suzan Verberne
paperurl: https://arxiv.org/abs/2610.06345
arxiv: '2610.06345'
pdf: https://arxiv.org/pdf/2610.06345
venue_type: preprint
abstract: >-
  In this paper, we evaluate open-source generative LLMs on legal Natural Language Inference (NLI).
  Legal inspectorial processes take place in specific domains and often deal with confidential data.
  This creates a need for working with local models that do not require labeled training data. We
  evaluate our models on the ContractNLI benchmark and two NLI4Wills datasets. We successfully
  reproduce the baseline for the task (Span NLI BERT) and we evaluate multiple open-source LLMs on the
  same task. We analyze the invalid rate of the models, and their stability across temperature
  settings and domains. Among the generative models, Gemma-4 26B performs the best, reaching an
  accuracy of 81.2%, even outperforming the supervised model on one metric. On accuracy, it is not
  possible to beat the supervised model with zero-shot approaches. Qwen-3.6 35B performs well on both
  ContractNLI and additional datasets in the legal wills domain. Our findings indicate that zero-shot,
  open-source, generative LLMs are a viable alternative for real-world legal NLI when no supervised
  data is available. Our code is available at https://github.com/fbaratov/contractnli-llms.
---
