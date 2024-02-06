import streamlit as st
import requests
import pandas as pd

from tmdbapi import run, Person_Details, get_person_id



# def get_df(id): 
    # df, df_external_ids, df_movie_credits = create_df(id)
    # Person = Person_Details(
    #     name = df.iloc[0]["name"], 
    #     biography = df.iloc[0]["biography"], 
    #     gender = df.iloc[0]["gender"], 
    #     birthday = df.iloc[0]["birthday"], 
    #     deathday = df.iloc[0]["deathday"], 
    #     birthplace = df.iloc[0]["place_of_birth"],
    #     known = df.iloc[0]["known_for_department"],
    #     imdb_id = df.iloc[0]["imdb_id"],
    #     popularity = df.iloc[0]["popularity"],
    #     profile_path = df.iloc[0]["profile_path"],
    #     facebook = df_external_ids.iloc[0]["facebook_id"],
    #     instagram = df_external_ids.iloc[0]["instagram_id"],
    #     )
    # print(df)
    # return Person
    # return df, df_external_ids, df_movie_credits, Person

# df, df_external_ids, df_movie_credits, Person = get_df(224513)

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    return data

st.title("Title here")
st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")

st.divider()

text_input = None

with st.sidebar:
    text_input = st.text_input(
        label = "Enter some text 👇",
        placeholder="",
    )
    if text_input:
        df, df_external,df_movie_credits = run(text_input)

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/" + df.iloc[0]["profile_path"])

with col2:
    st.header(df.iloc[0]["name"])
    st.metric(label="Popularity", value= df.iloc[0]["popularity"])
    # st.write(f"**Gender**: {Person.gender}")
    # st.write(f"**Birthday**: {Person.birthday}")
    # st.write(f"**Age**: {Person.age}")
    # if Person.deathday == None:
    #     pass
    # else:
    #     st.write(f"**Died**: {Person.deathday}")
    st.write("**Place of Birth**: " + df.iloc[0]["place_of_birth"])
    st.write("**Known For**: " + df.iloc[0]["known_for_department"])
    st.link_button("IMDB", ("https://www.imdb.com/name/")+df.iloc[0]["imdb_id"])
    # st.link_button("Instagram", Person.instagram)
    # if Person.facebook == None:
    #     pass
    # else:
    #     st.link_button("Facebook", Person.facebook)



st.subheader("Biography")
if df is not df.empty:
    st.markdown(df.iloc[0]["biography"])
else:
    pass

tab1, tab2 = st.tabs(["Financials", "Movie Credits"])

tab2.subheader("Movie Credits")
tab2.markdown("tab 2")

tab1.subheader("Financials")
tab1.markdown("tab 1 ")
# tab1.dataframe(df)  



   

print(df.columns)
# print(df.iloc[0]["biography"])

