import streamlit as st
import requests

api_key = '52f43d37fe00777d42451a8440cd9df1'

def get_candidates(song):
  url = f"http://ws.audioscrobbler.com/2.0/?method=track.search&track={song}&api_key={api_key}&format=json"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    candidates = []
    for track in data["results"]["trackmatches"]["track"]:
      name = track["name"]
      artist = track["artist"]
      candidates.append(f"{name} by {artist}")
    return candidates
  else:
    return ["Something went wrong"]

def get_similar_songs(choice):
  song, artist = choice.split(" by ")
  url = f"http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={artist}&track={song}&api_key={api_key}&format=json"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    similar_songs = []
    for track in data["similartracks"]["track"][:10]:
      name = track["name"]
      artist = track["artist"]["name"]
      similar_songs.append(f"{name} by {artist}")
    return similar_songs
  else:
    return ["Something went wrong"]

st.title("My app")

song = st.text_input("Enter a song title")

if song:
  candidates = get_candidates(song)
  choice = st.selectbox("Choose a song", candidates)
  if choice:
    similar_songs = get_similar_songs(choice)
    st.write("Similar songs:")
    st.write(similar_songs)
