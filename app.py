import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1 {
    color: #00BFFF;
}

h2, h3 {
    color: white;
}

[data-testid="stMetricValue"] {
    color: #00FF7F;
}

[data-testid="stSidebar"] {
    background-color: #262730;
}
</style>
""", unsafe_allow_html=True)






df=pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")


st.sidebar.header("Filters")

selected_platform = st.sidebar.selectbox(
    "Select Platform",
    ["All", "Netflix", "Hulu", "Prime Video", "Disney+"]
)


filtered_df = df.copy()

if selected_platform != "All":
    filtered_df = filtered_df[
        filtered_df[selected_platform] == 1
    ]




st.markdown(
    """
    <h1 style='text-align:center;'>
    🎬 OTT Platform Content Analytics Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Netflix | Prime Video | Hulu | Disney+</h4>",
    unsafe_allow_html=True
)


st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Analysis",
    [
        "Overview",
        "Platform Analysis",
        "Genre Analysis",
        "Country Analysis",
        "Language Analysis",
        "IMDb Analysis",
        "Correlation Analysis",
        "Business Insights",
        "About Project"
    ]
)

if page == "Overview":
    st.divider()

    st.header("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(" 🎬 Total Titles", len(filtered_df))
    col2.metric(" ⭐ Average IMDb", round(filtered_df['IMDb'].mean(),2))
    col3.metric(" 🌍 Countries", filtered_df['Country'].nunique())
    col4.metric(" 🗣 Languages", filtered_df['Language'].nunique())

    st.subheader("Dataset Preview")
    st.dataframe(filtered_df.head())

elif page == "Platform Analysis":
    st.divider()

    st.header("OTT Platform Analysis")

    platform_count = filtered_df[
        ['Netflix', 'Hulu', 'Prime Video', 'Disney+']
    ].sum()

    st.bar_chart(platform_count)

elif page == "Genre Analysis":
    st.divider()

    st.header("🎭 Genre Analysis")

    genre_count = (
        filtered_df['Genres']
        .dropna()
        .str.split(',')
        .explode()
        .value_counts()
    )

    st.bar_chart(genre_count.head(10))

    st.subheader("Top 10 Genres")

    st.dataframe(genre_count.head(10))



elif page == "Country Analysis":
    st.divider()
    st.header("🌍 Country Analysis")

    country_count = (
        filtered_df['Country']
        .dropna()
        .str.split(',')
        .explode()
        .value_counts()
    )

    st.bar_chart(country_count.head(10))

    st.subheader("Top 10 Countries")

    st.dataframe(country_count.head(10))


elif page == "Language Analysis":
    st.divider()
    st.header("🌐 Language Analysis")

    language_count = (
        filtered_df['Language']
        .dropna()
        .str.split(',')
        .explode()
        .value_counts()
    )

    st.bar_chart(language_count.head(10))

    st.subheader("Top 10 Languages")

    st.dataframe(language_count.head(10))



elif page == "IMDb Analysis":
    st.divider()

    st.header("⭐ IMDb Analysis")

    st.metric(
        "Average IMDb Rating",
        round(filtered_df['IMDb'].mean(), 2)
    )

    st.subheader("Top 10 Highest Rated Titles")

    top_movies = (
        filtered_df[['Title', 'IMDb']]
        .dropna()
        .sort_values('IMDb', ascending=False)
        .head(10)
    )

    st.dataframe(top_movies)

    st.subheader("IMDb Distribution")

    st.bar_chart(
        filtered_df['IMDb']
        .dropna()
        .value_counts()
        .sort_index()
    )

elif page == "Correlation Analysis":
    st.divider()

    st.header("📈 Correlation Analysis")

    corr_df = filtered_df[['IMDb', 'Runtime', 'Year']]

    correlation = corr_df.corr(numeric_only=True)

    st.subheader("Correlation Matrix")

    st.dataframe(correlation)

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="Blues",
        ax=ax
    )

    st.pyplot(fig)

elif page == "Business Insights":
    st.divider()

    st.header("💡 Business Insights")

    st.success("Prime Video has the largest content library among OTT platforms.")

    st.success("Drama is the most popular genre across OTT platforms.")

    st.success("United States contributes the highest number of titles.")

    st.success("English is the dominant language in OTT content.")

    st.success("IMDb ratings show very weak correlation with Runtime and Release Year.")





elif page == "About Project":
    st.divider()

    st.header("📋 About Project")

    st.write("""
    Problem Statement:
    
    OTT platforms host thousands of movies and TV shows, making it difficult
    to understand content trends, platform dominance, genre popularity,
    language distribution, and audience ratings.

    Objectives:
    
    • Compare content libraries across OTT platforms
    • Identify popular genres
    • Analyze country and language distribution
    • Study IMDb ratings
    • Generate business insights

    Tools Used:
    
    • Python
    • Pandas
    • Streamlit
    • Matplotlib
    • Seaborn
    """)

st.markdown("---")

st.caption(
    "© 2026 Jangiti Vamshi | OTT Platform Content Analytics Dashboard | Built with Streamlit"
)


st.sidebar.markdown("---")

st.sidebar.subheader("👨‍💻 About the Developer")

st.sidebar.write("**Jangiti Vamshi**")
st.sidebar.write("Data Analyst | Python | SQL | Power BI")

st.sidebar.markdown("📧 Email: jangitivamshi7@gmail.com")

st.sidebar.markdown(
    "[🔗 LinkedIn](https://www.linkedin.com/in/jangiti-vamshi-4447273a1?)"
)

st.sidebar.markdown(
    "[💻 GitHub](https://github.com/dashboard)"
)



st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
        url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
        background-size: cover;
        background-position: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)











