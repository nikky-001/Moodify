import cv2
import webbrowser
from deepface import DeepFace
from music_recommender import recommend_song

cap = cv2.VideoCapture(0)

frame_count = 0
dominant_emotion = None

print("Camera started. Press 'q' to capture emotion.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Detect emotion every 5 frames
    if frame_count % 5 == 0:
        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )
            dominant_emotion = result[0]['dominant_emotion']
        except:
            pass

    # Show emotion on screen
    if dominant_emotion:
        cv2.putText(
            frame,
            f"Emotion: {dominant_emotion}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Moodify - Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ================== RECOMMEND SONG ==================

if dominant_emotion:
    recommendation = recommend_song(dominant_emotion)

    if recommendation:
        print("\nRecommended Song:")
        print(f"Song   : {recommendation['song_name']}")
        print(f"Artist : {recommendation['artist']}")
        print(f"Mood   : {recommendation['mood']}")

        print("Opening Spotify...")
        webbrowser.open(recommendation["spotify_link"])
    else:
        print("No song found for this emotion.")
else:
    print("Emotion not detected properly.")


