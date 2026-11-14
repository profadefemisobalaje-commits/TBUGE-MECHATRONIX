# Preface

There is a moment in every machine learning project when the model reports a number and the team celebrates. The celebration is usually premature, and the reason is almost never the mathematics. It is that nobody asked what the number measured, on which data, chosen by whom, compared with what.

This volume is about that question. It teaches the standard methods of supervised and unsupervised learning — regression, classification, nearest neighbours, trees, ensembles — and it teaches them in the company of the discipline that decides whether any of them are worth deploying: splitting, validation, calibration, cost-sensitive evaluation and monitoring. The methods are the easy part. Every library will run them for you. The discipline is what distinguishes an engineer from someone who can call a function.

## The order of learning

The chapters follow the order in which understanding arrives, not the order of a syllabus.

We begin with the shape of a learning problem: what it means to learn from examples, and what you are assuming when you do. Then data, because a model is a claim about data and the claim is only as good as the sample. Then error, because the choice of what to minimise decides what the model becomes.

The middle of the volume builds four methods that are simple enough to compute by hand and useful enough to deploy: linear regression, logistic regression, nearest neighbours, and trees with their ensembles. Each is introduced with numbers, worked through on a small dataset, and examined for the way it fails. A reader who can fit a line by hand, work a logistic model at a single point, and split a small table by hand has the intuition that later volumes will formalise.

The last part is the part that gets skipped in courses and costs money in practice: feature pipelines, validation under leakage, metrics that respect costs, deployment, drift, retraining, and the question of whether machine learning is the right tool at all.

## What you need

A pencil, paper, and a calculator. Python helps from Chapter 4 onwards, and the examples are written so that they can be followed by typing them in rather than by understanding a framework. No mathematics beyond arithmetic, percentages and the idea of a graph is assumed. Where a formula appears, it is followed by a sentence saying what it does, and usually by a worked number.

## A warning that is also a promise

Machine learning is the part of artificial intelligence where it is easiest to fool yourself and hardest to notice. A model can be beautiful, fast, accurate on its test set and useless in the world, and no error message will appear. The promise of this volume is that you will learn to see the difference before the deployment, rather than after it.
