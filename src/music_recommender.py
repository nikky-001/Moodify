import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Dell\Desktop\Moodify\data\songs.csv")


def generate_spotify_link(song_name, artist):
    query = f"{song_name} {artist}".replace(" ", "%20")
    return f"https://open.spotify.com/search/{query}"

def recommend_song(emotion):
    emotion = emotion.lower()

    filtered = df[df["primary_mood"].str.lower() == emotion]

    if filtered.empty:
        return None

    song = filtered.sample(1).iloc[0]

    spotify_link = generate_spotify_link(song["song_name"], song["artist"])

    return {
        "song_name": song["song_name"],
        "artist": song["artist"],
        "mood": song["primary_mood"],
        "spotify_link": spotify_link 
    }




