import streamlit as st
import pandas as pd
from new_parser import load_youtube_log
from analytics import (
    compute_summary,
    plot_watch_time_by_date,
    plot_time_by_type,
    plot_top_channels,
)
from filters import sidebar_filters

st.set_page_config(page_title="YouTube Log Visualizer", layout="wide")
st.title("YouTube Listening Time Visualizer")

# --- Upload / Load data ---
if "df" not in st.session_state:
    uploaded_file = st.file_uploader("Upload your YouTube log CSV", type=["csv"])

    if uploaded_file:
        df = load_youtube_log(uploaded_file)
        st.session_state["df"] = df
        st.session_state["filename"] = uploaded_file.name
    else:
        st.info("Upload a CSV file to begin.")
        st.stop()
else:
    df = st.session_state["df"]
    st.caption(f"Using file: **{st.session_state["filename"]}**")

if st.button("Upload a different file"):
    for key in ["df", "filename", "df_filtered", "date_range", "selected_channel", "selected_type"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# --- Sidebar Filters ---
df_filtered = sidebar_filters(df)

# --- Dashboard Content ---
total_minutes, total_videos, avg_minutes = compute_summary(df_filtered)
st.metric("Total Minutes Watched", f"{total_minutes:.0f}")
st.metric("Unique Videos", total_videos)
st.metric("Average Minutes per Session", f"{avg_minutes:.2f}")

# Charts
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(
        plot_watch_time_by_date(df_filtered),
        config={ "responsive": True, "displayModeBar": False }
    )
with col2:
    st.plotly_chart(
        plot_time_by_type(df_filtered),
        config={ "responsive": True, "displayModeBar": False }
    )

st.plotly_chart(
    plot_top_channels(df_filtered),
    config={ "responsive": True, "displayModeBar": False }
)

with st.expander("View Raw Data"):
    st.dataframe(df_filtered)
