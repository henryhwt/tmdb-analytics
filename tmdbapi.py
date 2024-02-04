import requests
import pandas as pd
from datetime import datetime, date

import os
from dotenv import dotenv_values,load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
    }

base_URL = "https://api.themoviedb.org/3/"



def get_person_id(query):
    endpoint_URL = f"{base_URL}search/person?query={query}"
    response = requests.get(endpoint_URL, headers=headers)
    json_response = response.json()
    df = pd.json_normalize(json_response["results"])
    return df[["name","id","profile_path","popularity"]]

# df = get_person_id("ana")

# print(df)






def get_response(id):
    endpoint_URL = f"{base_URL}person/{id}?append_to_response=external_ids,movie_credits"
    response = requests.get(endpoint_URL, headers=headers)
    json_response = response.json()
    external_ids = json_response["external_ids"]
    movie_credits = json_response["movie_credits"]["cast"]
    return json_response, external_ids, movie_credits



def create_df(id):
    data, external_ids, movie_credits = get_response(id)
    df = pd.json_normalize(data)
    df_external_ids = pd.json_normalize(external_ids)
    df_movie_credits = pd.json_normalize(movie_credits)
    return df, df_external_ids, df_movie_credits

class Person_Details:

    base_image_URL = "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/"

    base_imdb_URL = "https://www.imdb.com/name/"

    def gender_convert(self, gendercode):
        if gendercode == 3:
            gender = "Non-binary"
        elif gendercode == 1:
            gender = "Female"
        elif gendercode == 2:
            gender = "Male"
        else:
            gender = "Not Specified"
        return gender
    
    def age_format(self, birthdayUSA):
        birthdayUK = datetime.strptime(birthdayUSA, '%Y-%m-%d').strftime('%d-%m-%Y')
        return birthdayUK

    def calculate_age(self, strbirthday):
        birthday = datetime.strptime(strbirthday, '%d-%m-%Y')
        today = datetime.today()
        age = today.year - birthday.year  - ((today.month, today.day) < (birthday.month, birthday.day))
        return age
    
    def facebook_url(self,fb_id):
        if fb_id == None:
            return None
        else:
            return f"https://www.facebook.com/{fb_id}"
    
    def instagram_url(self,insta_id):
        if insta_id == None:
            return None
        else:
            return f"https://www.instagram.com/{insta_id}"

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.biography = kwargs["biography"]
        self.birthday = self.age_format(kwargs["birthday"])
        self.deathday = kwargs["deathday"]
        self.birthplace = kwargs["birthplace"]
        self.known = kwargs["known"]
        self.imdb = str(self.base_imdb_URL + kwargs["imdb_id"])
        self.popularity = kwargs["popularity"]
        self.image = self.base_image_URL + kwargs["profile_path"]
        self.gender = self.gender_convert(kwargs["gender"])
        self.age = self.calculate_age(self.birthday)
        self.facebook = self.facebook_url(kwargs["facebook"])
        self.instagram = self.instagram_url(kwargs["instagram"])
        # self.tiktok =
        # self.wiki = 
        # self.twitter =

# external_ids.facebook_id
# external_ids.instagram_id
# external_ids.tiktok_id
# external_ids.twitter_id
        # external_ids.wikidata_id
