import streamlit as st
import projectinfo
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id="7b99b7d189b24f27a32aaea94ee8f927", client_secret="0f4e075ae55842e6a2f22f41dbf39d2a")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager) 


#About Me
def intro_section():
    st.header("Do you use Spotify...")
    st.image(projectinfo.headerImage, width = 600)
    st.write(projectinfo.about_section)
    st.write("---")
intro_section()

#NEW Spotify username lookup (Uses Spotipy API)
def spotify_lookup(username):
    try:
        user = sp.user(username)
        return user
    except:
        return None

#NEW - Spotify username input (button and text input, error handling)
def user_input():
    st.header("Here you can check Spotify profile information!!")
    st.subheader("Input a full spotify username and the site will return some info!")
    username = st.text_input('Enter your username:')

    if st.button("Get Profile"):
        if username:
            profile = spotify_lookup(username)
            if profile:
                st.subheader("User Profile:")
                st.write(f"Display Name: {profile['display_name']}")
                st.write(f"Followers: {profile['followers']['total']}")
                st.image(profile['images'][0]['url'], caption="Profile Image", width=600)
            else:
                st.error("User not found. Please enter a valid Spotify username.")
    st.write("---")

user_input()

#NEW Requests reccomended artists from Spotipy API
def reccomendations(artist):
    try:
        recs = sp.artist_related_artists(artist)
        return recs
    except:
        return None

#NEW - Gets an input from a user of a URL for an artist and displays reccomendations for similar artists - Uses API, button, text input, and error handling
def get_reccomendations():
    st.header("Who likes reccomendations...")
    st.subheader("Here you can input the link to your favorite artist and get reccomendations for more artists like them!")

    artist = st.text_input('Enter the URL to your favorite artist:')

    if st.button("Get Reccomendations"):
        if artist:
            reccomendedartists = reccomendations(artist)
            if reccomendedartists:
                st.subheader("Artists")
                for artist in reccomendedartists['artists']:
                    st.write(f"Artist Name: {artist['name']}")
                    artist_link = f"<a href={artist['external_urls']['spotify']}>Click Here!</a>"
                    st.write("Artist Link:")
                    st.markdown(artist_link, unsafe_allow_html=True)
                    st.image(artist['images'][0]['url'], caption="Artist Image", width=600)
            else:
                st.error("User not found. Please enter a valid Spotify username.")
    st.write("---")

get_reccomendations()

#Displays end info for the site creator and an image
def ending_section():
    st.subheader(f"**I hope you enjoyed using this website!**")
    st.write(f"*{projectinfo.about_creator}*")
    st.image(projectinfo.atl_image, width=600)
ending_section()




 