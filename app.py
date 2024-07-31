import streamlit as st
from streamlit_option_menu import option_menu

# Import your page functions
from Pages import home, people_findr, neighborhood_viewr, business_explor

# Define the menu items and corresponding pages
menu_items = ["Home", "People FindR", "Neighborhood ViewR", "Business ExploR"]
menu_icons = ['house', 'person-bounding-box', 'search-heart', 'buildings']
menu_pages = {
    "Home": home.show_home,
    "People FindR": people_findr.app,
    "Neighborhood ViewR": neighborhood_viewr.app,
    "Business ExploR": business_explor.app
}

def main():
    # Horizontal menu with custom styling for even spacing and color changes
    selected = option_menu(
        menu_title=None,
        options=menu_items,
        icons=menu_icons,
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#FFFFFF"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {
                "font-size": "18px", 
                "text-align": "center", 
                "margin": "0px", 
                "--hover-color": "#ff0000",
                "color": "black",
                "padding": "10px",
                "flex-grow": "1"
            },
            "nav-link-selected": {"background-color": "#ff0000", "color": "white"},
        }
    )

    # Display the selected page
    menu_pages[selected]()

if __name__ == "__main__":
    main()
