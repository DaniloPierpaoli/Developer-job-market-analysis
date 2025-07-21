import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("survey-data_cleaned.csv", keep_default_na= False)

# Sidebar filters
st.sidebar.header("Filter Respondents")
countries = df['Country'].unique()
age_groups = df['Age'].unique()

selected_country = st.sidebar.selectbox("Select Country", sorted(countries))
selected_ages = st.sidebar.multiselect("Select Age Group(s)", sorted(age_groups), default=sorted(age_groups))

# Filter dataset
filtered_df = df[(df['Country'] == selected_country) & (df['Age'].isin(selected_ages))]

# Helper to split, clean, and count tech frequencies
def process_tech_column(df,column_name):
    df = df[df[column_name] != "None"]
    series = df[column_name].apply(lambda x: [item.strip() for item in x.split(';')])
    exploded = pd.Series([item for sublist in series for item in sublist])
    return exploded.value_counts()

st.title(" Tech Preferences Explorer")
st.markdown("Filter by country and age range to see how preferences shift in technology categories.")

# ---------- Programming Languages (bar plot) ----------
st.subheader(" Programming Languages")
worked = process_tech_column(filtered_df,"LanguageHaveWorkedWith")
want = process_tech_column(filtered_df,"LanguageWantToWorkWith")
admired = process_tech_column(filtered_df,"LanguageAdmired")

lang_df = pd.concat([worked, want, admired], axis=1).astype(int)
lang_df.columns = ["Worked With", "Want To Work With", "Admired"]
lang_df = lang_df.head(10)

fig_lang = px.bar(lang_df, x=lang_df.index, y=lang_df.columns,
                  title="Top 10 Programming Languages",
                  labels={"value": "Number of Respondents", "index": "Language"},
                  barmode='group', height=500)
st.plotly_chart(fig_lang)

# ---------- Databases (pie chart) ----------
st.subheader(" Databases")
db_worked = process_tech_column(filtered_df,"DatabaseHaveWorkedWith").head(10)
db_want = process_tech_column(filtered_df,"DatabaseWantToWorkWith").head(10)
db_admired = process_tech_column(filtered_df,"DatabaseAdmired").head(10)
db_df = pd.DataFrame({"Worked With": db_worked, "Want To Work With": db_want,"Admired": db_admired}).fillna(0).astype(int)

col1, col2 = st.columns(2)
with col1:
    
    st.plotly_chart(px.pie(db_df, values='Worked With', names=db_df.index, title="Databases Worked With"))

with col2:
    
    st.plotly_chart(px.pie(db_df, values='Want To Work With', names=db_df.index, title="Databases Desired"))


    
st.plotly_chart(px.pie(db_df, values='Admired', names=db_df.index, title="Databases Admired"))

# ---------- Platforms (horizontal bar chart) ----------
st.subheader(" Cloud Platforms")
plat_worked = process_tech_column(filtered_df,"PlatformHaveWorkedWith")
plat_want = process_tech_column(filtered_df,"PlatformWantToWorkWith")
plat_admired = process_tech_column(filtered_df,"PlatformAdmired")

plat_df = pd.concat([plat_worked, plat_want, plat_admired], axis=1).astype(int).head(10)
plat_df.columns = ["Worked With", "Want To Work With", "Admired"]

fig_platform = px.bar(plat_df, y=plat_df.index, x=plat_df.columns,
                      title="Top 10 Cloud Platforms",
                      orientation='h',
                      labels={"value": "Number of Respondents", "index": "Platform"},
                      barmode='stack', height=500)
st.plotly_chart(fig_platform)

# ---------- Web Frameworks (grouped bar chart) ----------
st.subheader("🕸️ Web Frameworks")
web_worked = process_tech_column(filtered_df,"WebframeHaveWorkedWith")
web_want = process_tech_column(filtered_df,"WebframeWantToWorkWith")
web_admired = process_tech_column(filtered_df,"WebframeAdmired")

web_df = pd.concat([web_worked, web_want, web_admired], axis=1).fillna(0).astype(int).head(10)
web_df.columns = ["Worked With", "Want To Work With", "Admired"]

fig_web = px.bar(web_df, x=web_df.index, y=web_df.columns,
                 title="Top 10 Web Frameworks",
                 labels={"value": "Number of Respondents", "index": "Framework"},
                 barmode='group', height=500)
st.plotly_chart(fig_web)

st.markdown("---")
