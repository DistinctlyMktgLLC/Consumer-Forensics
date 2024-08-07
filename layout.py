import streamlit as st
from streamlit_option_menu import option_menu
from Pages import home, people_findr, neighborhood_viewr, business_explor

# Define the menu items and corresponding pages
menu_items = ["Home", "People", "Neighborhood", "Business"]
menu_icons = ['house', 'person-bounding-box', 'search-heart', 'buildings']
menu_pages = {
    "Home": home.show_home,
    "People": people_findr.app,
    "Neighborhood": neighborhood_viewr.app,
    "Business": business_explor.app
}

def render_layout(page_function):
    # Horizontal menu with custom styling for even spacing and color changes
    selected = option_menu(
        menu_title=None,
        options=menu_items,
        icons=menu_icons,
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#FFFFFF",
                "width": "100%",  # Ensures the menu spans the entire width of the page
                "display": "flex",
                "justify-content": "space-around"  # Evenly distributes the items
            },
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {
                "font-size": "18px", 
                "text-align": "center", 
                "margin": "0px", 
                "--hover-color": "#ff0000",
                "color": "black",
                "padding": "15px 20px",  # Adjusted padding
                "flex-grow": "1",
                "white-space": "nowrap",  # Prevents text wrapping
                "display": "flex",
                "align-items": "center",
                "justify-content": "center"
            },
            "nav-link-selected": {"background-color": "#ff0000", "color": "white"},
        }
    )

    # Display the selected page
    page_function = menu_pages[selected]
    page_function()

if __name__ == "__main__":
    render_layout(lambda: st.write("Select a page from the menu above."))
