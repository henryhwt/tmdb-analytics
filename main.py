import streamlit as st
import requests
import pandas as pd

from tmdbapi import create_df, Person_Details, get_person_id

def get_df(id): 
    df, df_external_ids, df_movie_credits = create_df(id)
    Person = Person_Details(
        name = df.iloc[0]["name"], 
        biography = df.iloc[0]["biography"], 
        gender = df.iloc[0]["gender"], 
        birthday = df.iloc[0]["birthday"], 
        deathday = df.iloc[0]["deathday"], 
        birthplace = df.iloc[0]["place_of_birth"],
        known = df.iloc[0]["known_for_department"],
        imdb_id = df.iloc[0]["imdb_id"],
        popularity = df.iloc[0]["popularity"],
        profile_path = df.iloc[0]["profile_path"],
        facebook = df_external_ids.iloc[0]["facebook_id"],
        instagram = df_external_ids.iloc[0]["instagram_id"],
        )
    print(df)
    return df, df_external_ids, df_movie_credits, Person

df, df_external_ids, df_movie_credits, Person = get_df(224513)

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    return data

st.title("Title here")
st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")

st.divider()

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(Person.image)

with col2:
    st.header(Person.name)
    st.metric(label="Popularity", value=Person.popularity)
    st.write(f"**Gender**: {Person.gender}")
    st.write(f"**Birthday**: {Person.birthday}")
    st.write(f"**Age**: {Person.age}")
    if Person.deathday == None:
        pass
    else:
        st.write(f"**Died**: {Person.deathday}")
    st.write(f"**Place of Birth**: {Person.birthplace}")
    st.write(f"**Known For**: {Person.known}")
    st.link_button("IMDB", Person.imdb)
    st.link_button("Instagram", Person.instagram)
    if Person.facebook == None:
        pass
    else:
        st.link_button("Facebook", Person.facebook)


st.subheader("Biography")
st.markdown(Person.biography)

tab1, tab2 = st.tabs(["Financials", "Movie Credits"])

tab2.subheader("Movie Credits")
tab2.markdown("tab 2")

tab1.subheader("Financials")
tab1.markdown("tab 1 ")
tab1.dataframe(df)  

# selectbox = None
with st.sidebar:
    # selectbox = st.selectbox(
    #     label= "Placeholder for the other text input widget",
    #     placeholder="This is a placeholder",
    #     if selectbox == None:
    #         options=get_person_id("ana"),
    #     else:
    #         options=get_person_id(selectbox),
    #     # on_change=,
    # )
    # get_df(selectbox)
    text_input = st.text_input(
        label = "Enter some text 👇",
        placeholder="ana de armas",
    )
    if text_input:
        df_search = get_person_id(text_input)
        get_df(df_search.iloc[0]["id"])

        print(text_input)

