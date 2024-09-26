import marimo

__generated_with = "0.8.20"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import altair as alt
    import polars as pl
    from pathlib import Path
    return Path, alt, mo, pl


@app.cell
def __(mo):
    mo.md(
        """
        ## Tidy Data

        Altair expects our data to be [tidy](http://vita.had.co.nz/papers/tidy-data.html).

        - Each variable is a column.
        - Each observation is a row. 
        - Each type of observational unit is a table.

        You can use `pandas` or `polars` DataFrames.
        """
    )
    return


@app.cell
def __(Path, __file__, pl):
    # first let's load and look at a dataframe with three columns
    #  there is an observation for each state legislature, showing how many bills they introduced in a given year
    df = pl.read_csv(Path(__file__).parent / "midwest_bills.csv")
    # (having a dataframe or chart as the last line in a notebook cell will automatically display it)
    df
    return (df,)


@app.cell
def __(alt, df):
    # Let's make our own charts of this dat, first we bind the data to a new chart object
    chart = alt.Chart(df)
    return (chart,)


@app.cell
def __(chart):
    # we add a geometry, we'll start with a point (at this point *something* can be displayed, but it won't be useful)
    chart.mark_point()
    return


@app.cell
def __(chart):
    # We use encodings to map our data to particular dimensions.
    # Altair will make then make appropriate choices based upon the type of data.
    chart.mark_point().encode(
        y="state",
        x="num_bills"
    )
    return


@app.cell
def __():
    return


@app.cell
def __(alt, chart):
    # what happens when we try to add color?
    chart.mark_point().encode(
        alt.Y("state"),
        alt.X("num_bills"),
        alt.Color("session_start_year"),
    )
    return


@app.cell
def __(alt, chart):
    # the prior example treated year as an Ordinal because it was numeric
    # instead we would treat it as Nominal for this data
    # we can use :Q, :O, :N, :T to mark the type that should be used
    by_year = chart.mark_point().encode(
        alt.Y("state:N"),
        alt.X("num_bills:Q"),
        alt.Color("session_start_year:N"),
    )
    # we're saving this one for later
    by_year
    return (by_year,)


@app.cell
def __(alt, chart):
    # Here we make a different chart from the same base data 
    # by re-using our `chart` variable.
    #
    # We choose a different shape (parameters that don't need to vary can be passed into the mark_* functions)
    # We also use an aggregate function average(num_bills)
    avgs = chart.mark_point(shape="wedge", color="black").encode(
        alt.Y("state"),
        alt.X("average(num_bills)"),
    )
    avgs
    return (avgs,)


@app.cell
def __(avgs, by_year):
    # two charts with compatible data can be layered with +
    by_year + avgs
    return


@app.cell
def __(alt, by_year, chart):
    # perhaps we don't want to use mark_point anymore, maybe a bar?
    bar_avgs = chart.mark_bar(color="#ccc").encode(
        alt.Y("state"),
        alt.X("average(num_bills)"),
    )
    bar_avgs + by_year
    return (bar_avgs,)


@app.cell
def __(alt, chart):
    # We can customize titles and other details by using `.title` and `.properties`
    # the latter sets chart-wide properties.
    final = chart.mark_point(shape="diamond").encode(
        alt.Y("state:N"),
        alt.X("num_bills:Q"),
        alt.Color("session_start_year:N").title("Session Year"),
    ) + chart.mark_bar(color="#70905050").encode(
        alt.Y("state"),
        alt.X("average(num_bills)").title("Number of Bills Introduced"),
    )
    final.properties(
        title='Midwest Bills by State',
        background='#f5f5dc'
    )
    return (final,)


@app.cell
def __(alt, chart):
    # Let's say we instead want to see if there are trends by year.
    # create a new chart object with year on the X-axis, and bills on the Y-axis
    # Also, make the chart print/colorblind friendly by encoding state in multiple ways.
    new_chart = chart.mark_point().encode(
        alt.Y("num_bills"),
        alt.X("session_start_year:N"),
        alt.Color("state"),
        alt.Shape("state"),
    )
    new_chart.properties(
        title='Midwest Bills by Year',
        background='#f5f5dc'
    )
    return (new_chart,)


@app.cell
def __(mo):
    mo.md(
        """
        ### Recommended Reading

        Altair Tutorial

        - Specifying Data (you can stop when you hit 'Generated Data')
        - Encodings
        - Encodings -> Channels (skim Channel Options)
        - Marks (skim a few of the mark guides, including Bar & Point)
        - Data Transformations (skim a few, including Regression)
        - Layered and Multi-View Charts
        - Customizing Visualizations

        Once you've read the above you have the core ideas of Altair.
        The remaining sections are useful as reference, and as you use Altair you will find your way to them as you ask yourself questions like "how do I work with geospatial data" or "how can I combine these axes"?

        The other common thing you will use the documentation for is "what arguments can I pass to this?"

        For that, use the [API Reference](https://altair-viz.github.io/user_guide/api.html) and find the class you're working with.

        Example: 

        - Let's say we want to adjust the color scheme, start with <https://altair-viz.github.io/user_guide/generated/channels/altair.Color.html>
        - Note that it can take a scale, and click to <https://altair-viz.github.io/user_guide/generated/core/altair.Scale.html#altair.Scale>
        """
    )
    return


@app.cell
def __(alt, chart):
    color_scheme = alt.Scale(scheme="set2")
    chart.mark_line().encode(
        alt.Y("num_bills"),
        alt.X("session_start_year:N"),
        alt.Color("state", scale=color_scheme),
    ) + chart.mark_point().encode(
        alt.Y("num_bills").title("Bills Introduced"),
        alt.X("session_start_year:N").title("Session Year"),
        alt.Color("state", scale=color_scheme),
        alt.Shape("state"),
    ).properties(
        title='Midwest Bills by Session',
    )
    return (color_scheme,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
