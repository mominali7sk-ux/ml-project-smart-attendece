import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white;">Created with ❤️ by</p>
        <span style="font-weight:bold; font-size:1rem; color:#FBBF24;">SRM AP</span>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:black;">Created with ❤️ by</p>
        <span style="font-weight:bold; font-size:1rem; color:#2563EB;">SRM AP</span>
        </div>
    """, unsafe_allow_html=True)
