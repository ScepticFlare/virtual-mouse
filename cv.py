import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False

screen_w, screen_h = pyautogui.size()
prev_x, prev_y = screen_w // 2, screen_h // 2

smoothening = 4
movement_gain_x = 0.6
movement_gain_y = 1.0

is_clicked = False

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def finger_logic(lm, hand_label):
    fingers = [0, 0, 0, 0, 0]

    if hand_label == "Right":
        fingers[0] = 1 if lm[4].x < lm[3].x else 0
    else:
        fingers[0] = 1 if lm[3].x < lm[4].x else 0

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for i in range(4):
        fingers[i + 1] = 1 if lm[tips[i]].y < lm[pips[i]].y else 0

    return fingers


while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark
        hand_label = result.multi_handedness[0].classification[0].label

        fingers = finger_logic(lm, hand_label)
        print(fingers)

        if fingers == [0, 1, 0, 0, 0]:
            raw_x = (1 - lm[8].x) * screen_w
            raw_y = lm[8].y * screen_h

            target_x = prev_x + (raw_x - prev_x) * movement_gain_x
            target_y = prev_y + (raw_y - prev_y) * movement_gain_y

            curr_x = prev_x + (target_x - prev_x) / smoothening
            curr_y = prev_y + (target_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

        if fingers == [0, 1, 1, 0, 0]:
            if not is_clicked:
                print("CLICK")
                pyautogui.click()
                is_clicked = True
        else:
            is_clicked = False

        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
