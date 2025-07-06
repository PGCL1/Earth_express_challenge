import streamlit as st

# defining the logo for all pages
LOGO_URL_LARGE = "images/celonis_large_logo.png"
LOGO_URL_SMALL = "images/celonis_small_logo.png"

st.logo(
    LOGO_URL_LARGE,
    icon_image=LOGO_URL_SMALL,
)


# setting page to fullscreen
st.set_page_config(layout="wide")

# defining login flow
if not st.user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")

# defining pagination for main application
pages = {
    "Main Navigation": [
        st.Page("dashboard/department_emissions.py", title="Stats"),
        st.Page("travel_calculation/travel_cockpit.py", title="Travel Cockpit"),
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
