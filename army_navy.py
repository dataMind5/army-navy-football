import pandas as pd
import streamlit as st
from plotly import graph_objects as go

st.title("Army vs. Navy Game")

# Use an interactive slider to get user input

year = st.slider(
    "Year Played",
    min_value=1890,
    max_value=2023,
    value=2023,
    help="Use this to see which team is ahead in the Army vs. Navy matchup",
)

df = pd.read_csv('Army_Navy_Football_Wins.csv')

# get data for selected year from slider

df_year = df[df['Year'] == year]

if df_year.empty:
    # year does not exist because game was not played
    navy_wins = [0]
    army_wins = [0]
    
else:
    # year exists and game was played
    navy_wins = df_year['Navy_Total_Wins']
    army_wins = df_year['Army_Total_Wins']

fig = go.Figure()
fig.add_trace(go.Bar(x=navy_wins, y=['Navy'],
                     marker_color='#515891',
                       orientation='h'
                ))
fig.add_trace(go.Bar(x=army_wins, y=['Army'],
                marker_color='#c1c4c9',
                       orientation='h'
                ))

fig.update_layout(
    height=300,
    showlegend=False,
    yaxis_tickfont_size=14,
    xaxis_range=[0,65],
    xaxis=dict(
        title='Total Wins',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group',
    bargroupgap=0.1
)

st.plotly_chart(fig, key='wins_bar_graph')

option = st.selectbox(
    "Choose a venue",
    df['Location'].unique()
)

# get data for selected venue

df_venue = df[df['Location'] == option]

if 'Navy' in df_venue['Winner'].values:
    navy_wins_venue = [df_venue['Winner'].value_counts()['Navy']]
else:
    navy_wins_venue = [0]

if 'Army' in df_venue['Winner'].values:
    army_wins_venue = [df_venue['Winner'].value_counts()['Army']]
else:
    army_wins_venue = [0]

fig2 = go.Figure()
fig2.add_trace(go.Bar(x=navy_wins_venue, y=['Navy'],
                     marker_color='#515891',
                       orientation='h'
                ))
fig2.add_trace(go.Bar(x=army_wins_venue, y=['Army'],
                marker_color='#c1c4c9',
                       orientation='h'
                ))

fig2.update_layout(
    height=300,
    showlegend=False,
    yaxis_tickfont_size=14,
    xaxis_range=[0,65],
    xaxis=dict(
        title='Total Wins',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group',
    bargroupgap=0.1
)

st.plotly_chart(fig2, key='venue_bar_graph')