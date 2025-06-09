import streamlit as st

st.write("Record thinking process")


main_page = st.Page("./main_page.py", title="Main Page", icon="")
it_page = st.Page("./it_page.py", title="information theory", icon="")
ft_page = st.Page("./ft_page.py", title="fourier transform", icon="")

# Set up navigation
pg = st.navigation([main_page, it_page, ft_page])

# Run the selected page
pg.run()


