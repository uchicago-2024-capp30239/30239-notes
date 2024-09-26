# Grammar of Graphics with Altair

## CAPP 30239

---

## Today

- Grammar of Graphics
- Types of Data
- Intro to Altair

---

## Grammar of Graphics

Hadley Wickham, creator of `ggplot2` and `tidyverse`, ["A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf).

Key Idea: move beyond pre-defined composites like "scatter plot" and "bar chart" into a composable grammar from which we can construct a wide variety of visualizations.

---

## Wickham's Components:

1. data and aesthetic mappings,
2. one or more layers, each with

    - a geometric object (line, point, etc.)
    - (optional) statistical transformation
    - (optional) position adjustment

3. one scale per aesthetic mapping (color, size, etc.)
4. a coordinate system
5. facet specification

---

## Types of Data

### **N** - Nominal

"strings" with no **order** (alphabetical does not count)

Species
States
Countries

### **O** - Ordered

- Grades: A, B, C, D, E, F
- Rankings: 1st, 2nd, 3rd

---

## Types of Data (Quantitative)

### **Q** - Interval (arbitrary zero)

- Dates (1 CE, Jan 1 1970, or...)
- Location (lat, lon)

Only differences matter, can't compare ratios.
_(What is 2024 / 1990?)_

### **T**emporal

Some systems (like Altair) will also offer this option specifically for dates and times.

### **Q** - Ratio (zero fixed)

Physical measurements, counts, amounts.

"4 km is _twice as far_ as 2 km"

---

## Types of Data (Operations)

|          | =, != | <, >, <=, >= | +, - | ÷   |
| -------- | ----- | ------------ | ---- | --- |
| Nominal  | ✓     |              |      |     |
| Ordered  | ✓     | ✓            |      |     |
| Interval | ✓     | ✓            | ✓    |     |
| Ratio    | ✓     | ✓            | ✓    | ✓   |

---

## Data Model to N, O, Q

- string?
- bool?
- float/int?

Possible exceptions?

---

## Data Model to N, O, Q

_Typically:_

- string - nominal or ordered
- bool - nominal
- float/int - interval or ratio

Possible Exceptions?

- Numeric IDs
- ZIP Codes
- ratio data stored with units (e.g. "10km")

---

## Mapping of Variables to Aesthetics

- position (X, Y, Z)
- length
- angle
- slope
- area
- volume
- density
- hue
- saturation
- texture
- connection
- containment/grouping
- shape

---

### Mackinlay's "effectiveness"

![width:800px](effectiveness.png)

---

## Altair's Grammar

Altair condenses several of the different pieces of the grammar to _"encoding channels"_.

We've seen X, Y, and color, let's take a look at some examples of other encoding channels.

---
