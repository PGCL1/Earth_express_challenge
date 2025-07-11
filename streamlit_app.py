import streamlit as st

# setting page to fullscreen
st.set_page_config(layout="wide")


# defining the logo for all pages
LOGO_URL_LARGE = "images/celonis_large_logo.png"
LOGO_URL_SMALL = "images/celonis_small_logo.png"

st.logo(
    LOGO_URL_LARGE,
    icon_image=LOGO_URL_SMALL,
)


# defining login flow
if not st.user.is_logged_in:
    # User is not logged in, show login screen
    st.header("This app is private.")
    st.subheader("Please log in.")

    # Using st.button with on_click=st.login will trigger the login process
    if st.button("Log in with Google"):
        st.login()
else:
    # User logged in, showing main application
    # st.write(st.user) see what are st.user attributes
    print(st.user)
    col1, col2 = st.columns([8,1])
    with col2:
        if st.user.picture:
            st.image(st.user.picture)
        st.button("Log out", on_click=st.logout)

    # defining pagination for main application
    pages = {
        "Main Navigation": [
            st.Page("dashboard/department_emissions.py", title="Stats"),
            st.Page("travel_calculation/travel_cockpit.py", title="Travel Cockpit"),
        ]
    }

    pg = st.navigation(pages, position="top")
    pg.run()

