import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Button class
class Button:
    def __init__(self, pos, text, size=[60, 60]):
        self.pos = pos
        self.size = size
        self.text = text

    def draw(self, img):
        x, y = self.pos
        w, h = self.size
        cv2.rectangle(img, self.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.rectangle(img, self.pos, (x + w, y + h), (50, 50, 50), 3)
        cv2.putText(img, self.text, (x + 20, y + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    def is_over(self, x, y):
        bx, by = self.pos
        bw, bh = self.size
        return bx < x < bx + bw and by < y < by + bh

# Create calculator buttons
button_list = []
keys = [['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+']]

for i in range(4):
    for j in range(4):
        button_list.append(Button([100 * j + 50, 100 * i + 50], keys[i][j]))

# Initialize webcam
cap = cv2.VideoCapture(0)
equation = ""

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Pinch detection: thumb tip (4) and index tip (8)
            x1, y1 = lm_list[4]
            x2, y2 = lm_list[8]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)

            distance = np.hypot(x2 - x1, y2 - y1)

            if distance < 40:
                for button in button_list:
                    if button.is_over(cx, cy):
                        cv2.rectangle(img, button.pos,
                                      (button.pos[0] + button.size[0], button.pos[1] + button.size[1]),
                                      (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (button.pos[0] + 20, button.pos[1] + 40),
                                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

                        if button.text == '=':
                            try:
                                equation = str(eval(equation))
                            except:
                                equation = "Error"
                        else:
                            equation += button.text

                        cv2.waitKey(300)  # Debounce delay

    # Draw buttons
    for button in button_list:
        button.draw(img)

    # Display the current equation/result
    cv2.rectangle(img, (50, 450), (450, 520), (255, 255, 255), cv2.FILLED)
    cv2.rectangle(img, (50, 450), (450, 520), (50, 50, 50), 3)
    cv2.putText(img, equation, (60, 500),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("Gesture Controlled Calculator", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
