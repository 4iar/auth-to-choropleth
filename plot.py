import plotly
from iso3166 import countries
from sys import argv

def plot_chloropleth(data):

    data = [dict(
            type='choropleth',
            locations=list(data.keys()),
            z=list(data.values()),
            text=[countries.get(c).name for c in data.keys()],
            colorscale = [[0, 'rgb(255,248,245)'], [0.35, 'rgb(252,187,161)'], [0.5, 'rgb(252,146,114)'], [0.6, 'rgb(251,106,74)'], [0.7, 'rgb(222,45,38)'], [1, 'rgb(165,15,21)']],
            autocolorscale=False,
            reversescale=False,
            marker=dict(
                    line=dict (
                            color='rgb(180,180,180)',
                            width=0.5
                    )
            ),
            colorbar=dict(
                    autotick = False,
                    tickprefix='',
                    title='Login attempts'
            ),
    )]

    layout = dict(
            title='',
            geo=dict(
                    showframe=False,
                    showcoastlines=False,
                    projection=dict(
                            type='Mercator'
                    )
            )
    )

    fig = dict(data=data, layout=layout)
    filename = "{}_chloropleth.html".format(argv[1])
    url = plotly.offline.plot(fig, validate=False, filename=filename)
