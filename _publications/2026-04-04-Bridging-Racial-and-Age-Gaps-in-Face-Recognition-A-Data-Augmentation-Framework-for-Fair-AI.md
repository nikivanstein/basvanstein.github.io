---
title: "Bridging Racial and Age Gaps in Face Recognition: A Data-Augmentation Framework for Fair AI"
collection: publications
permalink: /publication/2026-04-04-Bridging-Racial-and-Age-Gaps-in-Face-Recognition-A-Data-Augmentation-Framework-for-Fair-AI
date: 2026-04-04
venue: 'SN Computer Science'
citation: ' Sofoklis Kitharidis,  Anthonie Schaap,  Thomas Bäck,  Niki van Stein, &quot;Bridging Racial and Age Gaps in Face Recognition: A Data-Augmentation Framework for Fair AI.&quot; SN Computer Science, 2026.'
authors:
- Sofoklis Kitharidis
- Anthonie Schaap
- Thomas Bäck
- Niki van Stein
doi: 10.1007/s42979-026-04885-x
paperurl: https://doi.org/10.1007/s42979-026-04885-x
pdf: https://link.springer.com/content/pdf/10.1007/s42979-026-04885-x.pdf
venue_type: journal
abstract: >-
  This work addresses both race- and age-based imbalances in facial recognition, aiming to mitigate
  disparate error rates across underrepresented demographics. We refine our original framework through
  iterative data augmentation, combining standard transformations and GAN-based synthesis while
  introducing an embedding-based filter to discard artifacts or near-duplicates. Fairness is measured
  using per-subgroup Equalized Odds and F1-scores, comparing incremental retraining strategies,
  targeting the worst-performing age-ethnicity subgroups, to larger static merges of UTKFace and
  FairFace. Results show that boosting a single subgroup can yield local gains but often triggers a
  cyclical “whack-a-mole” pattern, wherein new disparities emerge elsewhere. Although
  StyleGAN-generated samples can narrow bias for specific subgroups, they sometimes inherit generative
  limitations and may not stabilize global performance. In contrast, merging balanced datasets or
  introducing large, diverse synthetic sets leads to more consistent fairness gains, though complete
  parity remains elusive. Overall, our findings demonstrate that while targeted data injections can
  alleviate certain imbalances, true equity requires broader measures such as robust data balancing
  and refined generation techniques. Future work should further explore adversarial debiasing,
  conditional GAN training, and dynamic reweighting to sustain fairness improvements across varied
  demographic settings.
---
