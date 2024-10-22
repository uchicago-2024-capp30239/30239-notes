# Visualizing Uncertainty

## CAPP 30239

---

![bg fit](climate1.png)

<!--
What is this trying to show?
source: https://www.ipcc.ch/report/ar6/wg1/figures/chapter-3/figure-3-4/
-->

---

![bg fit](climate2.png)

<!--
These are showing essentially the same thing, one shows individual models and the other uses some aggregates with confidence intervals.
These are from the same page of the IPCC report.
-->

---

## What causes uncertainty?

1) **measurement error** - An instrument used has some non-perfect degree of accuracy. In a survey, this could be a poorly-worded question.
2) **model uncertainty** - Models make assumptions and simplifications, different assumptions lead to different outcomes.
3) **sampling variability** - Differences between sample & population.
4) **missing data** - How missing data is accounted for & represented.

The result is that we have a range or distribution, where we want a number to use with one of our channels (Hue, X, Y, etc.).

---

## Challenges of Uncertainty

Often left out, in part due to being hard to understand, and even harder to visualize.

Omission however misleads audiences, especially where a lot of significant figures are included.

![width:100%](clock.png)

*Global Population Uncertainty: ±160 million people (2%)*

---

## Challenges of Uncertainty

Uncertainty estimates are simplified, often out of necessity.

![](weather.png)

30% chance of rain: "A 30% chance that at least 0.01" of rain will fall somewhere within a given area over a 12 hour period."

**Do I bring an umbrella?**

---

## Challenges of Uncertainty

Complexity of visualization can overwhelm audience, obscure other meaning.

![](matplotlib.png)

From a data-ink ratio perspective, it is understandable why if the error bars do  not seem relevant to a narrative, that they would be omitted.

---

## Including Uncertainty

If omitting uncertainty misleads, it violates our prime directive of **graphical integrity**.

The job then, is to find ways that are **audience appropriate** & **don't obfuscate the meaning**.

The difficulty will be in resolving this tension.

---

## Common Techniques

- Uncertainty as Probability
- Error Bars
- Confidence Bands

---

## Uncertainty As Probability


![width:100%](probability-waffle.png)

Random waffle chart: works for cases with discrete outcomes.

---

## Uncertainty As Probability

In practice, we often care about more than boolean outcome.
![](election-prediction.png)

---

![bg fit](election-quantile.png)

<!--

We can convert this to discrete measurements: quantile dot plot.

-->


---

![bg fit](biden-trump.webp)

<!-- source: fivethirtyeight -->

---

## Uncertainty of Point Estimates

These work when we're focused on uncertainty around a particular outcome.

Sometimes we need to show uncertainty around discrete measurements, or projections.

---

### Error Bars

![](data-ci.png)

---

### Error Bands

![bg left](altair-errorband.png)

```python
line = alt.Chart(source).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)'
)

band = alt.Chart(source).mark_errorband(extent='ci').encode(
    x='Year',
    y=alt.Y('Miles_per_Gallon').title('Miles/Gallon'),
)

band + line
```

---

### Issues with Error Bars & Confidence Bands

1) There is no pre-defined meaning of these intervals.
  **If error bars or bands are included, the legend must include information on the meaning.**
2) Error bars are common in scientific & academic literature, other audiences cannot be assumed to understand them.
3) Restricted to 1D/2D dots. If variable being expressed is mapped to color, area, etc. then alternative presentations needed.

---

![bg fit](2016.jpg)

---

### Variations on Error Bars & Intervals

![](ci-2.png)

<!-- when appropriate, can also be used to show multiple intervals -->

---

![bg fit](ci-3.png)

<!--care should be taken that distribution is indeed normal if curves/etc. chosen  -->

---

![](2d-bars.png)

---

### Regression Uncertainty

![width:900px](multiple-reg.png)

---

### Regression Uncertainty

![width:900px](translucent-band.png)

---

## Other Approaches

---
### Showing Multiple Futures

![](multiple-outcomes.webp)

---

![width:900px](climate1.png)

---

### Hurricane Uncertainty

<div class="container">
<div class="col">

![width:450](hurricane2.png)

</div>
<div class="col">

![width:450px](hurricane1.png)

  </div>
</div>

<!-- source: https://tamucoa.b-cdn.net/app/uploads/2021/10/House2011TrackUncertaintyVisualization.pdf -->

---
### On Maps

![bg fit](map-uncertainity.png)

<!-- source: https://www.e-education.psu.edu/geog486/sites/www.e-education.psu.edu.geog486/files/Lesson_07/Images/ex_vs_ont.PNG --> 

---
### "Sketchiness"

![](sketchy.gif)

---
### Animating Uncertainty

- <https://www.nytimes.com/interactive/2018/03/27/upshot/make-your-own-mobility-animation.html>
- HOP Plot: <https://vallandingham.me/animating_uncertainty.html>

---
## References & Acknowledgements

- <https://mucollective.co/uncertainty_collection/>
- <https://clauswilke.com/dataviz/visualizing-uncertainty.html>
- <https://www.mjskay.com/presentations/aalto2020-uncertainty.pdf>
- <https://nightingaledvs.com/dark-sky-weather-data-viz/>
