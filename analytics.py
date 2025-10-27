import pandas as pd
import plotly.express as px

def compute_summary(df: pd.DataFrame):
    total_minutes = df["Amount Logged"].sum()
    total_videos = df["Video ID"].nunique()
    avg_minutes = df["Amount Logged"].mean()
    return total_minutes, total_videos, avg_minutes

def plot_watch_time_by_date(df: pd.DataFrame):
    df_date = df.groupby(df["Log Date"].dt.date)["Amount Logged"].sum().reset_index()
    fig = px.line(df_date, x="Log Date", y="Amount Logged", title="Watch Time Over Time")
    return fig

def plot_top_videos(df: pd.DataFrame, n=10):
    top_videos = (
        df.groupby(["Video ID", "Title"])["Amount Logged"]
        .sum()
        .reset_index()
        .sort_values("Amount Logged", ascending=False)
        .head(n)
    )
    fig = px.bar(
        top_videos,
        x="Title",
        y="Amount Logged",
        title=f"Top {n} Videos",
        hover_data=["Video ID"],
    )
    return fig

def plot_top_channels(df: pd.DataFrame, n=10):
    top_channels = (
        df.groupby("Channel")["Amount Logged"]
        .sum()
        .reset_index()
        .sort_values("Amount Logged", ascending=False)
        .head(n)
    )
    fig = px.bar(
        top_channels,
        x="Channel",
        y="Amount Logged",
        title=f"Top {n} Channels"
    )
    return fig

def plot_time_by_type(df):
    type_stats = df.groupby("Type")["Amount Logged"].sum().reset_index()
    fig = px.pie(
        type_stats,
        names="Type",
        values="Amount Logged",
        title="Time Spent: Videos vs Livestreams",
        hole=0.4,
    )
    return fig
