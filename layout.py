import streamlit as st
from streamlit_option_menu import option_menu

def onboarding_screen():
    st.title("Welcome to the App!")
    
    # Section 1
    with st.expander("This section allows you to filter the data you want to see, think of it as your way to build a story"):
        st.markdown("""
        - **Field 1:** Ask your questions.
        - **Field 2:** See scenarios.
        """)
    
    # Section 2
    with st.expander("This section shows your data visualization"):
        st.markdown("""
        - **Chart 1:** Displays your data on a map.
        """)
    
    # Section 3
    with st.expander("Use these buttons to navigate"):
        st.markdown("""
        - **Home Button:** Go back to the home screen.
        - **Settings Button:** Adjust your preferences.
        """)

def render_layout(page_function):
    # Check if onboarding is needed
    if st.session_state.get('onboarding_done') != True:
        onboarding_screen()
        if st.button("Finish Onboarding"):
            st.session_state.onboarding_done = True
            st.experimental_rerun()
        return

    # Importing here to avoid circular dependencies
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
                "justify-content": "center"  # Centers the menu items within the container
            },
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {
                "font-size": "18px", 
                "text-align": "center", 
                "margin": "0px", 
                "--hover-color": "#ff0000",
                "color": "black",
                "padding": "15px 30px",  # Increased padding for wider appearance
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
