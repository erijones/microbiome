---
title: $0^{\text {th}}$ order model for competing microbes
author: Eric Jones
format: beamer
header-includes:
- \usepackage[]{algorithm2e}
...


Background
==========

+ Derived from the plankton-rotifer trait-based predator-prey model
  (\texttt{http://dx.doi.org/10.1016/j.ecolmodel.2009.05.005})
  by Agostino Merico
+ $n$ and $m$ types of microbes A and B; each of the A-type microbes share the
  same death rate $\mu_A$, but has a stochastic growth rate which provides
  variety within a given microbe
+ In addition, of the $1 - \kappa$ energy available for the microbe, a
  proportion $\delta_{A_i}$ goes to defense and $\alpha_{A_i}$ goes to nutrient
  allocation
+ This model assumes that the microbes compete for nutrients, but otherwise do
  not interact with each other (hence a 0$^\text{th}$ order model)
+ When microbes die, we assume their biomass is returned into the existing
  nutrients, $N$
+ Next steps: fit the model to data (***which constants?***), add in
  intermicrobe interaction, add in immune system interaction

Model
=====
\begin{align*}
    \frac{\diff A_1}{\diff t} &= \left[ {\red \gamma_A} \left(
    \frac{N}{N + \frac{\color{red} K_{A}}{\alpha_{A_1}}}\right) - {\red \mu_A}
    \right]A_1\\ \vdots & \\
    \frac{\diff A_n}{\diff t} &= \left[ {\red \gamma_A} \left( \frac{N}{N +
    \frac{\color{red} K_{A}}{\alpha_{A_n}}}\right) - {\red \mu_A} \right]A_n\\
    \frac{\diff B_1}{\diff t} &= \left[ {\red \gamma_B} \left(
    \frac{N}{N + \frac{\color{red} K_{B}}{\alpha_{B_i}}}\right) - {\red \mu_B}
    \right]B_1\\ \vdots & \\
    \frac{\diff B_m}{\diff t} &= \left[ {\red \gamma_B} \left(
    \frac{N}{N + \frac{\color{red} K_{B}}{\alpha_{B_m}}}\right) - {\red \mu_B}
    \right]B_m\\ \frac{\diff N}{\diff t} &= - \sum_i \left( \frac{\diff
    A_i}{\diff t} + \frac{\diff B_i}{\diff t}  \right) + \beta(N_0 - N)
\end{align*}

Fitting Data
============
+ Initially, we try to fit parameters for just one species of microbe
\begin{align*}
    \frac{\diff A}{\diff t} &= \left[ {\red \gamma} \left( \frac{N}{N +
    {\color{red} K}}\right) - {\red \mu} \right]A \\
    \frac{\diff N}{\diff t} &= - \frac{\diff A}{\diff t} + 
    \beta(N_0 - N)
\end{align*}
+ From the experimental design, we should know $\beta$ and $N_0$
+ We need to fit ${\red \gamma, \ K}$, and ${\red \mu}$ from data

"Experimental" Data
===================
![Data from model with random fluctuations](one_microbe.pdf)

Univariate Bayesian Parameter Estimation
==========================================
\KwData{$\hat{y}$ dependent on $\theta_\text{true}$ at $n$ time-steps, with
model $y(\theta_\text{guess})$ at any time-steps}
set range for possible $\theta$ values ($[\theta] = [\theta_\text{min}, \ldots,
\theta_\text{max}]$)\; \
\For{each $\theta[i]$}{
    \textit{set initial uniform prior:}\; \\
    probability[i,0] = 1\; \\
    \For{each timestep $j$}{
        $y_{i,j} = y(\theta[i])|_{t=j}$\; \\
        \textit{compare data to proposed $\theta$ value}:\; \\
        distance$[i,j]$ = \texttt{normalpdf}($\hat{y}(t=j), \mu=y_{i,j},
        \sigma^2 = 1 )$\; \\
        probability$[i,j]$ = probability$[i,j-1]$*distance$[i,j]$
    }
}
normalize probabilities;

**As the number of time steps increases, the probability distributions over
$\theta$ should approach $\theta_\text{true}$**

