import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, max_hands=1, detection_confidence=0.8):
        self.hands = mp.solutions.hands.Hands(max_num_hands=max_hands,
                                               min_detection_confidence=detection_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        return self.results

    def draw_hands(self, frame):
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    def get_landmark_points(self, frame_shape):
        if not self.results.multi_hand_landmarks:
            return None

        lm = self.results.multi_hand_landmarks[0].landmark
        w, h = frame_shape[1], frame_shape[0]
        return [(int(lm[i].x * w), int(lm[i].y * h)) for i in range(21)]