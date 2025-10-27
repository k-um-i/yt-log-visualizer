import streamlit as st

def sidebar_filters(df):
    """Render sidebar filters and update session state. Returns filtered DataFrame."""
    st.sidebar.header("Filters")

    # --- Initialize defaults ---
    if "date_range" not in st.session_state:
        st.session_state["date_range"] = [
            df["Log Date"].min().date(),
            df["Log Date"].max().date(),
        ]
    if "selected_channel" not in st.session_state:
        st.session_state["selected_channel"] = "All Channels"
    if "selected_type" not in st.session_state:
        st.session_state["selected_type"] = "All"

    # --- Date range filter ---
    date_range = st.sidebar.date_input(
        "Date range",
        value=st.session_state["date_range"],
    )
    st.session_state["date_range"] = date_range

    # --- Channel filter ---
    all_channels = sorted(df["Channel"].dropna().unique())
    selected_channel = st.sidebar.selectbox(
        "Filter by channel (optional)",
        options=["All Channels"] + all_channels,
        index=(["All Channels"] + all_channels).index(st.session_state["selected_channel"])
        if st.session_state["selected_channel"] in ["All Channels"] + all_channels
        else 0,
    )
    st.session_state["selected_channel"] = selected_channel

    # --- Type filter ---
    type_options = ["All", "Video", "Livestream"]
    selected_type = st.sidebar.radio(
        "Content type",
        type_options,
        index=type_options.index(st.session_state["selected_type"]),
    )
    st.session_state["selected_type"] = selected_type

    # --- Apply filters ---
    min_date, max_date = st.session_state["date_range"]
    mask = (df["Log Date"].dt.date >= min_date) & (df["Log Date"].dt.date <= max_date)
    df_filtered = df[mask]

    if selected_channel != "All Channels":
        df_filtered = df_filtered[df_filtered["Channel"] == selected_channel]
    if selected_type != "All":
        df_filtered = df_filtered[df_filtered["Type"] == selected_type]

    # Store globally for all pages
    st.session_state["df_filtered"] = df_filtered

    return df_filtered

