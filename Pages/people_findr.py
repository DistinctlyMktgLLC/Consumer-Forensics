import streamlit as st
from modules.data_loader import load_data
import pydeck as pdk

def sample_data(data, fraction=0.5):
    """Sample a cross-section of the data"""
    return data.sample(frac=fraction, random_state=1)

def app():
    st.title("People Finder")
    st.write("**Note:** This represents only a portion of the available data. For full access, contact [darnel.m@distinctlymktg.com](mailto:darnel.m@distinctlymktg.com).")

    # Load and sample data
    data = load_data('data/people_findr_data.parquet')
    data_sampled = sample_data(data, fraction=0.5)
    
    st.sidebar.header("I want to understand People")
    
    kind_of_person = st.sidebar.multiselect("Kind of Person", data_sampled['Kind_of_Person'].dropna().unique(), help="Who they are - Kind of Person")
    true_colors = st.sidebar.multiselect("True Colors", data_sampled['True_Colors'].dropna().unique(), help="What they think - True Colors")
    their_reactions = st.sidebar.multiselect("Their Reactions", data_sampled['Their_Reactions'].dropna().unique(), help="What they think - Their Reactions")
    how_to_connect = st.sidebar.multiselect("How to Connect", data_sampled['How_to_Connect'].dropna().unique(), help="What's their value - How to Connect")
    what_theyre_into = st.sidebar.multiselect("What they’re into", data_sampled['What_theyre_into'].dropna().unique(), help="What's their value - What they’re into")
    how_they_feel = st.sidebar.multiselect("How They Feel", data_sampled['How_They_Feel'].dropna().unique(), help="What's their value - How They Feel")
    how_you_hook_them = st.sidebar.multiselect("How you hook them", data_sampled['How_you_hook_them_'].dropna().unique(), help="What's their value - How you hook them")

    sign = st.sidebar.multiselect("Sign", data_sampled['Sign'].dropna().unique(), help="Demographic - Sign")
    income = st.sidebar.multiselect("Income", data_sampled['Income'].dropna().unique(), help="Demographic - Income")
    race = st.sidebar.multiselect("Race", data_sampled['race'].dropna().unique(), help="Demographic - Race")
    marstat = st.sidebar.multiselect("Marital Status", data_sampled['marstat'].dropna().unique(), help="Demographic - Marital Status")
    educ = st.sidebar.multiselect("Education", data_sampled['educ'].dropna().unique(), help="Demographic - Education")
    employ = st.sidebar.multiselect("Employment", data_sampled['employ'].dropna().unique(), help="Demographic - Employment")
    gender = st.sidebar.multiselect("Gender", data_sampled['gender'].dropna().unique(), help="Demographic - Gender")

    filtered_data = data_sampled.copy()
    
    if kind_of_person:
        filtered_data = filtered_data[filtered_data['Kind_of_Person'].isin(kind_of_person)]
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
    if how_you_hook_them:
        filtered_data = filtered_data[filtered_data['How_you_hook_them_'].isin(how_you_hook_them)]
    if sign:
        filtered_data = filtered_data[filtered_data['Sign'].isin(sign)]
    if income:
        filtered_data = filtered_data[filtered_data['Income'].isin(income)]
    if race:
        filtered_data = filtered_data[filtered_data['race'].isin(race)]
    if marstat:
        filtered_data = filtered_data[filtered_data['marstat'].isin(marstat)]
    if educ:
        filtered_data = filtered_data[filtered_data['educ'].isin(educ)]
    if employ:
        filtered_data = filtered_data[filtered_data['employ'].isin(employ)]
    if gender:
        filtered_data = filtered_data[filtered_data['gender'].isin(gender)]
    
    # Ensure the latitude and longitude columns are correctly named
    filtered_data = filtered_data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
    
    # Map visualization with tooltips
    tooltip = {
        "html": "<b>Sign:</b> {Sign}<br/>"
                "<b>Income:</b> {Income}<br/>"
                "<b>Race:</b> {race}<br/>"
                "<b>Marital Status:</b> {marstat}<br/>"
                "<b>Education:</b> {educ}<br/>"
                "<b>Employment:</b> {employ}<br/>"
                "<b>Gender:</b> {gender}<br/>"
                "<b>Kind of Person:</b> {Kind_of_Person}<br/>"
                "<b>True Colors:</b> {True_Colors}<br/>"
                "<b>Their Reactions:</b> {Their_Reactions}<br/>"
                "<b>How to Connect:</b> {How_to_Connect}<br/>"
                "<b>What they’re into:</b> {What_theyre_into}<br/>"
                "<b>How They Feel:</b> {How_They_Feel}<br/>"
                "<b>How you hook them:</b> {How_you_hook_them_}<br/>",
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
