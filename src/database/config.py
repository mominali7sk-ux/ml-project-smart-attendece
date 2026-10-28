import streamlit as st
from supabase import Client, create_client
from urllib.parse import urlsplit, urlunsplit

supabase_url = st.secrets.get("SUPABASE_URL") or st.secrets.get("SUPABSE_URL")
supabase_key = st.secrets.get("SUPABASE_KEY")

if not supabase_url:
    raise KeyError("Set SUPABASE_URL in .streamlit/secrets.toml.")
if not supabase_key:
    raise KeyError("Set SUPABASE_KEY in .streamlit/secrets.toml.")

parsed_url = urlsplit(supabase_url.strip())
if (
    parsed_url.scheme != "https"
    or not parsed_url.hostname
    or not parsed_url.hostname.endswith(".supabase.co")
    or parsed_url.username
    or parsed_url.password
    or parsed_url.query
    or parsed_url.fragment
):
    raise ValueError(
        "SUPABASE_URL must be the HTTPS root URL of your Supabase project."
    )

supabase_url = urlunsplit(
    (parsed_url.scheme, parsed_url.netloc, "", "", "")
)
supabase: Client = create_client(supabase_url, supabase_key)