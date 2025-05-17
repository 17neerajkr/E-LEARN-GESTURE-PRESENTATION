from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np

# Parameters
width, height = 1280, 720
gestureThreshold = 300
folderPath = "presentation"

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=1)

# Variables
delay = 30
buttonPressed = False
counter = 0
imgNumber = 0
annotations = [[]]
annotationNumber = -1
annotationStart = False
hs, ws = 120, 213  # webcam overlay size
pauseMode = False
colorIndex = 0
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
currentColor = colors[colorIndex]

# Load presentation slides
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)
    imgCurrent = cv2.resize(imgCurrent, (width, height))

    # Detect hands
    hands, img = detectorHand.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    if hands and not buttonPressed and not pauseMode:
        hand = hands[0]
        cx, cy = hand["center"]
        lmList = hand["lmList"]
        fingers = detectorHand.fingersUp(hand)

        # Calculate index finger position
        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))
        indexFinger = xVal, yVal

        # --- Slide Navigation ---
        if cy <= gestureThreshold:
            if fingers == [1, 0, 0, 0, 0]:  # Left
                if imgNumber > 0:
                    imgNumber -= 1
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    buttonPressed = True
            elif fingers == [0, 0, 0, 0, 1]:  # Right
                if imgNumber < len(pathImages) - 1:
                    imgNumber += 1
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    buttonPressed = True

        # --- Clear Annotations ---
        elif fingers == [0, 0, 0, 0, 0]:
            annotations = [[]]
            annotationNumber = -1
            annotationStart = False

        # --- Laser Pointer ---
        elif fingers == [0, 1, 0, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 20, (0, 0, 255), cv2.FILLED)

        # --- Pause Mode ---
        elif fingers == [1, 1, 1, 1, 1]:
            pauseMode = True

        # --- Toggle Drawing Color ---
        elif fingers == [0, 0, 1, 1, 0]:
            colorIndex = (colorIndex + 1) % len(colors)
            currentColor = colors[colorIndex]
            buttonPressed = True

        # --- Zoom Gesture (thumb & index) ---
        elif fingers[0] == 1 and fingers[1] == 1 and sum(fingers) == 2:
            length, _, _ = detectorHand.findDistance(lmList[4], lmList[8], img)
            if length < 30:
                cv2.putText(imgCurrent, "Zoom In", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
            elif length > 200:
                cv2.putText(imgCurrent, "Zoom Out", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

        # --- Start Drawing ---
        elif fingers == [0, 1, 0, 0, 0]:
            if not annotationStart:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            annotations[annotationNumber].append(indexFinger)
            cv2.circle(imgCurrent, indexFinger, 12, currentColor, cv2.FILLED)

        # --- Undo Drawing ---
        elif fingers == [0, 1, 1, 1, 0]:
            if annotations:
                annotations.pop(-1)
                annotationNumber -= 1
                buttonPressed = True

        else:
            annotationStart = False

    elif pauseMode and hands:
        # Exit pause mode when all fingers down
        if detectorHand.fingersUp(hands[0]) == [0, 0, 0, 0, 0]:
            pauseMode = False
            buttonPressed = True

    if buttonPressed:
        counter += 1
        if counter > delay:
            buttonPressed = False
            counter = 0

    # Draw annotations
    for i, annotation in enumerate(annotations):
        for j in range(1, len(annotation)):
            cv2.line(imgCurrent, annotation[j - 1], annotation[j], currentColor, 12)

    # Overlay webcam
    imgSmall = cv2.resize(img, (ws, hs))
    imgCurrent[0:hs, width - ws:width] = imgSmall

    # Display
    cv2.imshow("Slides", imgCurrent)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break
