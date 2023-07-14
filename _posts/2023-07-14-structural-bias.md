---
title: 'Gecco 2023 - DoE2Vec'
date: 2023-07-14
permalink: /posts/2023/07/structural-bias/
teaser: "teasers/biastoolbox.png"
tags:
  - bias
  - structural-bias
  - optimization
  - heuristics
  - deep-learning
  - explainable-AI
---


Structural Bias, what is it and why do we care?
====

## What is Structural Bias?

SB is,..

{: .notice} Watch the [video](https://youtu.be/tVBM56y-lU0){:target="_blank"} of our Hot-off-the-press talk on Gecco 2023.


### Why is it important to detect structural bias?


### What can we do when an algorithm exhibits structural bias?

In the case that we detect or suspect that a heuristical search algorithm shows structural biased behaviour, the first thing we can do is verify and inspect the type of structural bias.

One way to do this is by visual inspection of the behaviour of the algorithm in the search space. By running the optimizer on a special function called `f0`, which is  a function that returns a uniform random number between 0 and 1, we can de-couple the algorithm behaviour from the objective function. A better and more robust way to verify if the algorithm exhibits structural biased behaviour is by using the statistical functions and deep-learning framework of our [BIAS Toolbox](https://github.com/Dvermetten/BIAS){:target="_blank"}.
Using the BIAS Toolbox we can verify the existance, strength and type of structural bias. This can give insights into the cause of the bias. For example, an algorithm with boundary bias (exploring the boundaries more than the rest of the search space) can be caused by biased boundary correction mechanisms. 
Once the type of structural bias is known, we can perform abblation studies to vary the hyper-parameters and modules of an algorithm. Each variant of the algorithm can then be verified using the BIAS toolbox.
Correlations can then be observed between the hyper-parameters and the presense of structural bias. Using this information we can pick hyper-parameters that do not suffer from structural bias, or improve certain algorithmic components.

### How does structural bias affect algorithm performance?

Structural bias can affect the performance of an algorithm on a specific problem, or even on a benchmark set, both positively and negatively. It depends on the location of local and global optima in the problems whether the biased algorithm performs well or not. In general, for a set of functions where the global optimum can be anywhere in the search space, structural bias is always a disadvantage.
The strength of the bias (how much the algorithm is attracted to certain parts of the search space) determines how much the performance is affected.
If the strength of the bias is relatively low compared to the (wanted) bias caused by the objective function, the performance might not be affected at all.

### How to design bias-free optimization algorithms?

When developing algorithms it is important to understand what Structural Bias is and how it can affect the performance and evaluation of your algorithms.
Be wary of algorithm components that steer into a direction in the search space indepdent of the objective function. For example, a mutation operator for an evolutionary algorithm, that is more likely to increase a dimension than decrease it, or a mutation operator that puts an individual on the boundary when it overpasses the boundary, are both clearly cases of structurally biased algorithm components.
It is not always easy however to detect what parts of an algorithm can induce bias, it is therefore always advised to inspect the performance of your algorithms using the [BIAS Toolbox](https://github.com/Dvermetten/BIAS){:target="_blank"}.

## Using the BIAS Toolbox

Installing and using the BIAS toolbox is super easy. All you need is python 3 and R installed on your system.
Once R and Python are properly installed, you can install the BIAS toolbox using pip and test your algorithm using the example below.

#### Install the structural BIAS toolbox

```sh
pip install struct-bias
```

#### Test your algorithm

```python
#example of using the BIAS toolbox to test a Differential Evolution algorithm

from scipy.optimize import differential_evolution
import numpy as np
from BIAS import BIAS, f0, install_r_packages

#run first time to install required R packages
install_r_packages()

#In this example we use a 5 dimensional search space.
#We recommend to do the test with at least 2 dimensions.
dim = 5
bounds = [(0,1)] * dim

#do 30 independent runs (5 dimensions), 
samples = []
print("Performing optimization method 30 times on f0 as objective.")
for i in np.arange(30):
    result = differential_evolution(f0, bounds, maxiter=1000)
    samples.append(result.x)

samples = np.array(samples)

test = BIAS()
print(test.predict(samples, show_figure=True))

#Use the deep-learning module of the toolbox to verify results
#  and predict the type of SB
y, preds = test.predict_deep(samples)
test.explain(samples, preds, filename="explanation-de.png")
```
We advise to us a large enough evaluation budget for your algorithm, the tests from our paper uses 10.000 evaluations, however, 1.000 evaluations is generally enough to discover any structural bias.
The number of runs should be either 30, 50, 100 or 600. We advise to use 100 individual runs.

See for more details the [Github repository](https://github.com/Dvermetten/BIAS){:target="_blank"}.


### How biased are popular optimization algorithms?

Using the BIAS toolbox we have tested over 3000 popular (and less popular) optimization heuristics and their variants.

A few interesting cases are:

- list examples TODO

See also our paper [Emergence of structural bias in differential evolution](https://scholar.google.com/scholar?q=Emergence+of+structural+bias+in+differential+evolution){:target="_blank"} for an in-depth analysis of different DE variants.

---

See also our the blog post about [Deep-Bias](https://nikivanstein.nl/..), the deep-learning extension of our Structural BIAS toolbox.