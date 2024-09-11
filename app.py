import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")
st.title("2024 Olympic Medlists Birth Locations")

df = pd.read_csv('2024_medalists_all.csv')
df_filtered = df.dropna(subset=['lat', 'lon'])

medal_colours = {
    'Gold': 'yellow',
    'Silver':'silver',
    'Bronze': 'brown"
}

df_filtered['representing_country'] = "Representing: " + df_filtered["country_medal"]

fig = px.scatter_geo(
    df_filtered,
    lat="lat",
    lon="lon",
    hover_name='medalist_name',
    hover_data={'lat': False, 'lon': False, 'place_of_birth': True, 'Representing': True, 'event_name': True},
    colour='medal',
    color_discrete_map=medal_colours,
    title="2024 Olympic Medlists Birth Locations",
    projection="natural earth",
    template="plotly_dark"
)

fig.update_traces(marker=dict(size=12))

fig.update_geos(
    showcoastlines=True,
    coastlinecolor='white',
    showland=True,
    landcolor="black",
    showocean=True,
    oceancolor="darkgrey",
    showlakes=True,
    lakecolor="darkgrey",
    showcountries=True,
    countrycolor="white",
    bgcolor='black'
)

fig.update_layout(
    height=700,
    margin={"r": 0, "t": 50, "l": 0, "b":0},
    plot_bgcolor = 'black',
    paper_bgcolor='black',
    font_color="white",
)

st.plotly_chart(fig, use_container_width=True)
