print("🚀 recommender.py started")

import pandas as pd
import random

# Load dataset
df = pd.read_csv(r"C:\Users\Dell\Desktop\Moodify\data\songs.csv")
print("Dataset loaded:", len(df))


# Map detected emotions to dataset moods
emotion_to_mood = {
    "happy": ["happy", "energetic"],
    "sad": ["sad", "emotional"],
    "neutral": ["calm", "romantic"],
    "angry": ["energetic"],
    "surprise": ["happy"]
}

def recommend_song(detected_emotion):
    moods = emotion_to_mood.get(detected_emotion, ["calm"])

    filtered_songs = df[df["primary_mood"].isin(moods)]

    if filtered_songs.empty:
        return None

    song = filtered_songs.sample(1).iloc[0]

    return {
        "song_name": song["song_name"],
        "artist": song["artist"],
        "mood": song["primary_mood"],
        "spotify_query": song["spotify_query"]
    }


# TESTING
if __name__ == "__main__":
    test_emotion = "happy"
    recommendation = recommend_song(test_emotion)

    if recommendation:
        print("🎵 Recommended Song:")
        print(recommendation)
    else:
        print("No song found")
