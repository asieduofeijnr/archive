import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
    page_title="MSDS_NBA_GROUP_34",
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

file_path = "NBA_Stats_71_Years_Updated.xlsx"


@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_excel(file_path)


nba_data = get_data()
nba_data["3-Pt FG Attempts"] = nba_data["3-Pt FG Attempts"].fillna(0)
nba_data["3-Pt FG Made"] = nba_data["3-Pt FG Made"].fillna(0)

threepointscolumns = [
    "Year",
    "Season Start Year",
    "Season Type",
    "Player",
    "Team",
    "Games Played",
    "3-Pt FG Attempts",
    "3-Pt FG Made",
]

threepointsdf = nba_data[threepointscolumns]
threepointsdf = threepointsdf.reset_index()
threepointsdf = threepointsdf.drop("index", axis=1)


##STREAMLIT DATA###
st.title("THREE POINTER 🐐")
st.title("NBA Group 34")

data = "https://photos.onedrive.com/share/7653AB837B3500E3!231679?cid=7653AB837B3500E3&resId=7653AB837B3500E3!231679&authkey=!AID9RXUD5x2Ruf0&ithint=video&e=xdZBHB"

st.video(data, format="video/mp4")

col_period_1, col_season_1 = st.columns(2)


# for years filter

with col_period_1:
    years = st.selectbox(
        "Select Period",
        ("All Years", "1951 - 1970", "1971 - 1990", "1991 - 2011", "2012 - 2022"),
    )

# for season filter
with col_season_1:
    season = st.selectbox(
        "Select Season", ("All Seasons", "Regular Season", "Playoffs")
    )

if years == "1951 - 1970":
    threepointsdf = threepointsdf.loc[
        (threepointsdf["Season Start Year"] > 1950)
        & (threepointsdf["Season Start Year"] < 1971)
    ]

if years == "1971 - 1990":
    threepointsdf = threepointsdf.loc[
        (threepointsdf["Season Start Year"] > 1970)
        & (threepointsdf["Season Start Year"] < 1991)
    ]

if years == "1991 - 2011":
    threepointsdf = threepointsdf.loc[
        (threepointsdf["Season Start Year"] > 1990)
        & (threepointsdf["Season Start Year"] < 2012)
    ]

if years == "2012 - 2022":
    threepointsdf = threepointsdf.loc[
        (threepointsdf["Season Start Year"] > 2011)
        & (threepointsdf["Season Start Year"] < 2023)
    ]

if season == "Regular Season":
    threepointsdf = threepointsdf.loc[threepointsdf["Season Type"] == season]

if season == "Playoffs":
    threepointsdf = threepointsdf.loc[threepointsdf["Season Type"] == season]


three_for_graph = threepointsdf.groupby("Season Start Year").sum()

who_shot_three = threepointsdf.groupby("Player").sum()
who_shot_three = who_shot_three.sort_values("3-Pt FG Made", ascending=False)
best_players_who_shot_three = who_shot_three[:10]
best_players_who_shot_three = best_players_who_shot_three.drop(
    axis=1, columns="Season Start Year"
)

best_players = best_players_who_shot_three.index

threepointsdf = threepointsdf[threepointsdf["Player"].isin(best_players)]
# Stream lit kpis at top of page


kpi0, kpi1, kpi2, kpi3 = st.columns(4)


players_images = {
    "Stephen Curry": "https://www.basketball-reference.com/req/202106291/images/headshots/curryst01.jpg",
    "Ray Allen": "https://www.basketball-reference.com/req/202106291/images/headshots/allenra02.jpg",
    "James Harden": "https://www.basketball-reference.com/req/202106291/images/headshots/hardeja01.jpg",
    "Klay Thompson": "https://www.basketball-reference.com/req/202106291/images/headshots/thompkl01.jpg",
    "LeBron James": "https://www.basketball-reference.com/req/202106291/images/headshots/jamesle01.jpg",
    "Bill Russell": "https://www.basketball-reference.com/req/202106291/images/headshots/russebi01.jpg",
    "Hal Greer": "https://www.basketball-reference.com/req/202106291/images/headshots/greerha01.jpg",
    "Bob Cousy": "https://www.basketball-reference.com/req/202106291/images/headshots/cousybo01.jpg",
    "Dolph Schayes": "https://www.basketball-reference.com/req/202106291/images/headshots/schaydo01.jpg",
    "Danny Ainge": "https://www.basketball-reference.com/req/202106291/images/headshots/aingeda01.jpg",
    "Michael Adams": "https://www.basketball-reference.com/req/202106291/images/headshots/adamsmi01.jpg",
    "Larry Bird": "https://www.basketball-reference.com/req/202106291/images/headshots/birdla01.jpg",
    "Dale Ellis": "https://www.basketball-reference.com/req/202106291/images/headshots/ellisda01.jpg",
    "Michael Cooper": "https://www.basketball-reference.com/req/202106291/images/headshots/richami01.jpg",
    "Byron Scott": "https://www.basketball-reference.com/req/202106291/images/headshots/scottby01.jpg",
    "Reggie Miller": "https://www.basketball-reference.com/req/202106291/images/headshots/millere01.jpg",
    "Kobe Bryant": "https://www.basketball-reference.com/req/202106291/images/headshots/bryanko01.jpg",
    "Jason Kidd": "https://www.basketball-reference.com/req/202106291/images/headshots/kiddja01.jpg",
    "Damian Lillard": "https://www.basketball-reference.com/req/202106291/images/headshots/lillada01.jpg",
    "Adrian Smith": "https://www.basketball-reference.com/req/202106291/images/headshots/smithad01.jpg",
    "Larry Staverman": "https://www.basketball-reference.com/req/202106291/images/headshots/steella01.jpg",
    "Larry Jones": "https://www.basketball-reference.com/req/202106291/images/headshots/jonesla01.jpg",
    "Johnny Kerr": "https://www.basketball-reference.com/req/202106291/images/headshots/kerrre01.jpg",
    "Johnny Payak": "https://www.basketball-reference.com/req/202106291/images/headshots/mikange01.jpg",
}

kpi0.image(
    "https://cdn.freebiesupply.com/images/large/2x/nba-logo-transparent.png",
    width=101,
)
kpi0.metric(
    label="NAME:",
    value="POINTS:",
    delta="GAMES PLAYED:",
)

kpi1.image(
    players_images[best_players[0]],
    width=150,
)
kpi1.metric(
    label=best_players[0],
    value=int(best_players_who_shot_three["3-Pt FG Made"][0]),
    delta=int(best_players_who_shot_three["Games Played"][0]),
)

kpi2.image(
    players_images[best_players[1]],
    width=150,
)
kpi2.metric(
    label=best_players[1],
    value=int(best_players_who_shot_three["3-Pt FG Made"][1]),
    delta=int(best_players_who_shot_three["Games Played"][1]),
)

kpi3.image(
    players_images[best_players[2]],
    width=150,
)
kpi3.metric(
    label=best_players[2],
    value=int(best_players_who_shot_three["3-Pt FG Made"][2]),
    delta=int(best_players_who_shot_three["Games Played"][2]),
)


x = three_for_graph.index
a = three_for_graph["Games Played"]
b = three_for_graph["3-Pt FG Attempts"]
c = three_for_graph["3-Pt FG Made"]

# Create traces for 3points attempts and 3 points made
fig = go.Figure(layout={"width": 850})
fig.add_trace(go.Bar(x=x, y=a, name="Games Played"))
fig.add_trace(
    go.Scatter(
        x=x, y=b, mode="markers+lines", name="3 PTS Attempt", visible="legendonly"
    )
)
fig.add_trace(
    go.Scatter(
        x=x,
        y=c,
        mode="markers+lines",
        name="3 PTS Made",
        visible="legendonly",
    )
)


# Create traces for best 3 points players


games_played = best_players_who_shot_three["Games Played"]
pts_attempts = best_players_who_shot_three["3-Pt FG Attempts"]
pts_made = best_players_who_shot_three["3-Pt FG Made"]


fig2 = go.Figure(layout={"width": 850})
fig2.add_trace(
    go.Bar(
        x=best_players,
        y=games_played,
        text=games_played,
        name="Games Played",
    )
)
fig2.add_trace(
    go.Scatter(
        x=best_players,
        y=pts_attempts,
        mode="markers+lines+text",
        text=pts_attempts,
        textposition="top center",
        name="3 PTS Attempt",
        visible="legendonly",
    )
)
fig2.add_trace(
    go.Scatter(
        x=best_players,
        y=pts_made,
        mode="markers+lines+text",
        text=pts_made,
        textposition="top center",
        name="3 PTS Made",
        visible="legendonly",
    )
)


fig3 = px.scatter(
    threepointsdf,
    x="Season Start Year",
    y="3-Pt FG Made",
    color="Player",
    size="3-Pt FG Attempts",
    hover_data="Season Type",
    width=850,
)

fig3.update_traces(visible="legendonly")

tab1, tab2, tab3 = st.tabs(
    ["GAMES OVER THE YEARS", "PLAYERS OVER THE YEARS", "BEST 3 POINTER"]
)
with tab1:
    st.plotly_chart(
        fig,
        theme="streamlit",
    )
with tab2:
    st.plotly_chart(fig2, theme="streamlit")
with tab3:
    st.plotly_chart(fig3, theme="streamlit")


st.dataframe(best_players_who_shot_three)

st.subheader("ERICS PRESENTATION")

st.markdown(
    """
- 4229-6296 Missing Values for multiple columns
- Strong positive correlation between “Points Scored” and : “FG Attempts”, “Minutes Played” and “Turnovers”
- Mean and STD of “FG %” : 43.06% & 12.29%
- Mean and STD of “3-Pt FG %” : 21.27% & 19.64%
- “Points Scored” mean ~ 413 ; 90th percentile = 1134 points
"""
)

st.image("Eric/eric1.png")

st.subheader("Some text here")

img_col1, img_col2 = st.columns(2)
img_col1.image("Eric/eric2.png")
img_col2.image("Eric/eric3.png")

st.subheader("Some text here")


st.subheader("HAMZA PRESENTATION")

st.subheader("Some text here")

st.image("Hamza/hamza.png")

st.subheader("Some text here")

st.image("Hamza/hamza2.png")

st.subheader("Some text here")


st.subheader("CONCLUSION AND BUSINESS FINDINGS")
