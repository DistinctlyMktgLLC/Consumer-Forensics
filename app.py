import streamlit as st
from layout import render_layout

def main():
    render_layout(lambda: st.write("Select a page from the menu above."))

if __name__ == "__main__":
    main()
