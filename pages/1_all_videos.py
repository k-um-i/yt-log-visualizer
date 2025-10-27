import streamlit as st
import pandas as pd
from filters import sidebar_filters

st.set_page_config(page_title="All Videos", layout="wide")
st.title("Complete Video List")

# --- Load data ---
if "df" not in st.session_state:
    st.warning("Please upload your CSV on the main page first.")
    st.stop()

df = sidebar_filters(st.session_state["df"]).copy()

# --- Video list ---
# Create a clickable YouTube link
df["Link"] = df["Video ID"].apply(
    lambda vid: f"https://www.youtube.com/watch?v={vid}" if pd.notna(vid) else None
)

df_grouped = (
    df.groupby(["Title", "Channel", "Type", "Duration", "Link"], dropna=False)["Amount Logged"]
    .sum()
    .reset_index()
)
df_grouped.rename(columns={"Amount Logged": "Minutes Watched"}, inplace=True)

# Reorder columns for clarity
columns = ["Title", "Channel", "Type", "Minutes Watched", "Duration", "Link"]
df_display = df_grouped[columns].drop_duplicates(subset=["Link"])

# Add a search box
search_query = st.text_input("Search by title or channel", "")
if search_query:
    mask = (
        df_display["Title"].str.contains(search_query, case=False, na=False)
        | df_display["Channel"].str.contains(search_query, case=False, na=False)
    )
    df_display = df_display[mask]

# Show as interactive table
st.dataframe(
    df_display,
    width = "stretch",
    hide_index=True,
    column_config={
        "Link": st.column_config.LinkColumn("YouTube Link"),
        "Duration": st.column_config.NumberColumn("Duration (min)", format="%.1f"),
    },
)

