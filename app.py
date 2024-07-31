import streamlit as st
from streamlit_option_menu import option_menu

# Import your page functions
from Pages import home, people_findr, neighborhood_viewr, business_explor

def main():
    # Sidebar menu for selecting pages
    selected = option_menu(
        "Main Menu", 
        ["Home", "People FindR", "Neighborhood ViewR", "Business ExploR"], 
        icons=['house', 'person-bounding-box', 'search-heart', 'buildings'], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal"
    )

    # Display the selected page
    if selected == "Home":
        home.show_home()
    elif selected == "People FindR":
        people_findr.app()
    elif selected == "Neighborhood ViewR":
        neighborhood_viewr.app()
    elif selected == "Business ExploR":
        business_explor.app()

if __name__ == "__main__":
    main()
