import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

frame_count = 0
last_emotion = "Detecting..."

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Emotion Detection every 5 frames
    if frame_count % 5 == 0:
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            last_emotion = result[0]['dominant_emotion']
        except:
            pass

    # Display Emotion
    cv2.putText(frame,
                f"Emotion: {last_emotion}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Moodify - Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
