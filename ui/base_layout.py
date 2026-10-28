
import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
        .stApp {
            background: #5865F2 !important;
        }
        .stApp div[data-testid="stColumn"] {
        background-color:#E0E3FF !important;
        padding:1.5rem!important;
        border-radius: 5rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background: #E0E3FF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap');

        /* Hide Streamlit toolbar */
        # #MainMenu,
        # footer,
        # header {
        #     visibility: hidden;
        # }

        # /* Page spacing */
        # .block-container {
        #     padding-top: 1.5rem !important;
        # }

        /* H1 heading */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        /* H2 heading */
        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
        }

        /* Text fonts */
        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Button styling */
        button[kind="primary"],
        button[kind="secondary"],
        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        /* Button hover effect */
        button[kind="primary"]:hover,
        button[kind="secondary"]:hover,
        button[kind="tertiary"]:hover {
            transform: scale(1.05);
        }
        button:hover{
        transform: scale(1.05);
           }
        </style>
        """,
        unsafe_allow_html=True
    )
