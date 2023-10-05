import streamlit as st
import pandas

st.set_page_config(page_title=None,
                   page_icon=None,
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items=None)

colL, colR = st.columns([1.0, 5.0])

with colL:
    st.write("Home")
    st.write("About")

with colR:
    st.image("images/Hamburger_icon.svg.png", width=50 )
    st.button(label="Menu", help="Menu Principal", )
    #st.menu_items(['Item 1', 'Item 2', 'Item 3'], expanded=True, floating=True, emphasized_items=[0])
    st.title("The Best Company")
    content = """
    Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
    Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, 
    cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una 
    galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. 
    No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos 
    electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con 
    la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más 
    recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye 
    versiones de Lorem Ipsum.
    """
    st.write(content)

    st.header("Our Team")

    df = pandas.read_csv("data.csv", sep=",")

    col1, col2, col3 = st.columns(3)

    with col1:
        for index, row in df[:4].iterrows():
            fn = row["first name"].title()
            ln = row["last name"].title()
            role = row["role"]
            img = row["image"]
            st.subheader(fn+" "+ln)
            st.write(role)
            st.image(f"images/{img}")

    with col2:
        for index, row in df[4:8].iterrows():
            fn = row["first name"].title()
            ln = row["last name"].title()
            role = row["role"]
            img = row["image"]
            st.subheader(fn+" "+ln)
            st.write(role)
            st.image(f"images/{img}")

    with col3:
        for index, row in df[8:].iterrows():
            fn = row["first name"].title()
            ln = row["last name"].title()
            role = row["role"]
            img = row["image"]
            st.subheader(fn+" "+ln)
            st.write(role)
            st.image(f"images/{img}")