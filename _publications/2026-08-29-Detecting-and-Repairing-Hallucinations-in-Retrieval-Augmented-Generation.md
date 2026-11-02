---
title: "Detecting and Repairing Hallucinations in Retrieval-Augmented Generation"
collection: publications
permalink: /publication/2026-08-29-Detecting-and-Repairing-Hallucinations-in-Retrieval-Augmented-Generation
date: 2026-08-29
venue: 'arXiv preprint arXiv:2608.29307'
citation: ' Sai Krishna Reddy Mulakkayala,  Niki van Stein,  Aske Plaat, &quot;Detecting and Repairing Hallucinations in Retrieval-Augmented Generation.&quot; arXiv preprint arXiv:2608.29307, 2026.'
authors:
- Sai Krishna Reddy Mulakkayala
- Niki van Stein
- Aske Plaat
paperurl: https://arxiv.org/abs/2608.29307
arxiv: '2608.29307'
pdf: https://arxiv.org/pdf/2608.29307
venue_type: preprint
abstract: >-
  Language models increasingly answer questions by consulting retrieved documents rather than memory
  alone, a design now common in search assistants and enterprise knowledge tools. Grounding a model in
  retrieved text reduces unsupported statements but does not eliminate them, and a reader cannot tell
  a grounded sentence from an invented one. Most research on this problem stops at detection, yet
  flagging a faulty answer changes nothing for the person reading it, and little is known about which
  action should follow. Using RAGTruth, a benchmark whose unsupported passages are annotated by hand,
  we split each flagged answer into individual factual claims, check each against the retrieved
  source, and compare leaving the answer untouched with three repair strategies of increasing
  richness: deleting an unsupported claim, replacing it with source text, and rewriting it. Three
  language models from different families judge the 916 repaired answers. Every strategy reduces the
  proportion of answers judged to contain unsupported content, and all three judges agree on the
  ordering. Deletion achieves the largest reduction while retaining least of the original answer, at
  64.3% of the text, whereas rewriting retains 80.1% and reduces least. Repair is not confined to
  faulty answers: 83.5% of answers annotated clean are edited too. The strategies occupy different
  points on a grounding preservation trade-off rather than forming a quality ranking, and choosing
  between them needs evidence about answer usefulness that automatic metrics cannot supply.
---
