import streamlit as st
from modules.data_loader import load_data
import pydeck as pdk

def sample_data(data, fraction=0.5):
    """Sample a cross-section of the data"""
    return data.sample(frac=fraction, random_state=1)

def app():
    st.title("Explore Neighborhoods")
    st.write("**Note:** This represents only a portion of the available data. For full access, contact [darnel.m@distinctlymktg.com](mailto:darnel.m@distinctlymktg.com).")

    # Load and sample data
    data = load_data('data/neighborhood_viewr_data.parquet')
    data_sampled = sample_data(data, fraction=0.5)
    
    st.sidebar.header("I want to understand People")
    
    kind_of_person = st.sidebar.multiselect("Kind of Person", data_sampled['Kind_of_Person'].dropna().unique(), help="Who they are - Kind of Person")
    people_standard = st.sidebar.multiselect("People Standard", data_sampled['People_Standard'].dropna().unique(), help="Who they are - People Standard")
    true_colors = st.sidebar.multiselect("True Colors", data_sampled['True_Colors'].dropna().unique(), help="What they think - True Colors")
    their_reactions = st.sidebar.multiselect("Their Reactions", data_sampled['Their_Reactions'].dropna().unique(), help="What they think - Their Reactions")
    how_to_connect = st.sidebar.multiselect("How to Connect", data_sampled['How_to_Connect'].dropna().unique(), help="What's their value - How to Connect")
    what_theyre_into = st.sidebar.multiselect("What they’re into", data_sampled['What_theyre_into'].dropna().unique(), help="What's their value - What they’re into")
    how_they_feel = st.sidebar.multiselect("How They Feel", data_sampled['How_They_Feel'].dropna().unique(), help="What's their value - How They Feel")
    make_them_loyal = st.sidebar.multiselect("Make Them Loyal", data_sampled['Make_Them_Loyal'].dropna().unique(), help="What's their value - Make Them Loyal")

    filtered_data = data_sampled.copy()
    
    if kind_of_person:
        filtered_data = filtered_data[filtered_data['Kind_of_Person'].isin(kind_of_person)]
    if people_standard:
        filtered_data = filtered_data[filtered_data['People_Standard'].isin(people_standard)]
    if true_colors:
        filtered_data = filtered_data[filtered_data['True_Colors'].isin(true_colors)]
    if their_reactions:
        filtered_data = filtered_data[filtered_data['Their_Reactions'].isin(their_reactions)]
    if how_to_connect:
        filtered_data = filtered_data[filtered_data['How_to_Connect'].isin(how_to_connect)]
    if what_theyre_into:
        filtered_data = filtered_data[filtered_data['What_theyre_into'].isin(what_theyre_into)]
    if how_they_feel:
        filtered_data = filtered_data[filtered_data['How_They_Feel'].isin(how_they_feel)]
    if make_them_loyal:
        filtered_data = filtered_data[filtered_data['Make_Them_Loyal'].isin(make_them_loyal)]
    
    # Ensure the latitude and longitude columns are correctly named
    filtered_data = filtered_data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
    
    # Map visualization with tooltips
    tooltip = {
        "html": "<b>Neighborhood:</b> {Neighborhood_}<br/>"
                "<b>City:</b> {City}<br/>"
                "<b>State:</b> {State_Name}<br/>"
                "<b>Kind of Person:</b> {Kind_of_Person}<br/>"
                "<b>True Colors:</b> {True_Colors}<br/>"
                "<b>Their Reactions:</b> {Their_Reactions}<br/>"
                "<b>How to Connect:</b> {How_to_Connect}<br/>"
                "<b>What they’re into:</b> {What_theyre_into}<br/>"
                "<b>How They Feel:</b> {How_They_Feel}<br/>"
                "<b>Make Them Loyal:</b> {Make_Them_Loyal}<br/>",
        "style": {
            "backgroundColor": "steelblue",
            "color": "white"
        }
    }
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        filtered_data,
        pickable=True,
        opacity=0.8,
        filled=True,
        radius_scale=10,
        radius_min_pixels=5,
        radius_max_pixels=100,
        get_position=["lon", "lat"],
        get_fill_color=[255, 0, 0],
        get_radius=200,
    )

    view_state = pdk.ViewState(
        latitude=filtered_data["lat"].mean(),
        longitude=filtered_data["lon"].mean(),
        zoom=8,
        pitch=0,
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip
    )

    st.pydeck_chart(r)

if __name__ == "__main__":
    app()
