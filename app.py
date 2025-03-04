import cv2
import mediapipe as mp

# 初始化 MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# 開啟攝影機
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # **步驟 1：轉換 BGR -> RGB（MediaPipe 需要 RGB）**
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # **步驟 2：偵測臉部特徵點**
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape
            for idx, landmark in enumerate(face_landmarks.landmark):
                x, y = int(landmark.x * w), int(landmark.y * h)

                # **標記特徵點**
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                # **顯示 Landmark 編號**
                # cv2.putText(frame, str(idx), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 
                #             0.3, (255, 0, 0), 1, cv2.LINE_AA)

    # **顯示影像**
    cv2.imshow("Face Mesh with Landmark IDs", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
