import streamlit as st
from modules.data_loader import load_data
import pydeck as pdk

def sample_data(data, fraction=0.5):
    """Sample a cross-section of the data"""
    return data.sample(frac=fraction, random_state=1)

def app():
    st.title("Business ExploR")
    st.write("**Note:** This represents only a portion of the available data. For full access, contact [darnel.m@distinctlymktg.com](mailto:darnel.m@distinctlymktg.com).")
    
    # Load and sample data
    data = load_data('data/business_explor_data.parquet')
    data_sampled = sample_data(data, fraction=0.5)
    
    # Sidebar for filtering data
    st.sidebar.header("Filter Options")
    
    kind_of_person = st.sidebar.multiselect("Kind of Person", data_sampled['kind_of_person'].dropna().unique(), help="Filter by Kind of Person")
    true_colors = st.sidebar.multiselect("True Colors", data_sampled['true_colors'].dropna().unique(), help="Filter by True Colors")
    their_reactions = st.sidebar.multiselect("Their Reactions", data_sampled['their_reactions'].dropna().unique(), help="Filter by Their Reactions")
    how_to_connect = st.sidebar.multiselect("How to Connect", data_sampled['how_to_connect'].dropna().unique(), help="Filter by How to Connect")
    what_theyre_into = st.sidebar.multiselect("What they’re into", data_sampled['what_theyre_into'].dropna().unique(), help="Filter by What they’re into")
    how_they_feel = st.sidebar.multiselect("How They Feel", data_sampled['how_they_feel'].dropna().unique(), help="Filter by How They Feel")
    make_them_loyal = st.sidebar.multiselect("Make Them Loyal", data_sampled['make_them_loyal'].dropna().unique(), help="Filter by Make Them Loyal")
    
    business_types = st.sidebar.multiselect("Select Business Type", data_sampled['business_type'].dropna().unique())
    
    filtered_data = data_sampled.copy()
    
    # Applying filters
    if business_types:
        filtered_data = filtered_data[filtered_data['business_type'].isin(business_types)]
    if kind_of_person:
        filtered_data = filtered_data[filtered_data['kind_of_person'].isin(kind_of_person)]
    if true_colors:
        filtered_data = filtered_data[filtered_data['true_colors'].isin(true_colors)]
    if their_reactions:
        filtered_data = filtered_data[filtered_data['their_reactions'].isin(their_reactions)]
    if how_to_connect:
        filtered_data = filtered_data[filtered_data['how_to_connect'].isin(how_to_connect)]
    if what_theyre_into:
        filtered_data = filtered_data[filtered_data['what_theyre_into'].isin(what_theyre_into)]
    if how_they_feel:
        filtered_data = filtered_data[filtered_data['how_they_feel'].isin(how_they_feel)]
    if make_them_loyal:
        filtered_data = filtered_data[filtered_data['make_them_loyal'].isin(make_them_loyal)]
    
    # Ensure proper naming for map display
    filtered_data = filtered_data.rename(columns={'latitude': 'lat', 'longitude': 'lon'})
    
    # Map visualization with pydeck
    tooltip = {
        "html": "<b>Business Name:</b> {business_name}<br/>"
                "<b>City:</b> {city}<br/>"
                "<b>State:</b> {state}<br/>"
                "<b>Kind of Person:</b> {kind_of_person}<br/>"
                "<b>True Colors:</b> {true_colors}<br/>"
                "<b>Their Reactions:</b> {their_reactions}<br/>"
                "<b>How to Connect:</b> {how_to_connect}<br/>"
                "<b>What they’re into:</b> {what_theyre_into}<br/>"
                "<b>How They Feel:</b> {how_they_feel}<br/>"
                "<b>Make Them Loyal:</b> {make_them_loyal}<br/>",
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
    from layout import render_layout
    render_layout(app)
