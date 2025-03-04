# 🎯 OpenCV + MediaPipe 即時人臉特徵點偵測

本專案使用 **MediaPipe Face Mesh** 和 **OpenCV** 來即時偵測 **468 個人臉特徵點**，並標記在影像上。

## 📌 特色

✅ **即時偵測** 人臉特徵點
✅ **使用 MediaPipe Face Mesh** 進行高效能人臉分析
✅ **可視化特徵點**（畫出每個 Landmark 點）
✅ **可擴充**（可加上嘴巴變形、眼睛放大等特效）

---

## 🛠️ 安裝環境

請確保你的電腦已安裝 **Python 3.x**，然後執行以下指令來安裝必要的套件：

```bash
pip install opencv-python mediapipe
```

---

## 🚀 如何運行程式？

1. **下載程式碼**

   ```bash
   git clone https://github.com/your-username/face-landmark-detection.git
   cd face-landmark-detection
   ```
2. **執行程式**

   ```bash
   python face_mesh.py
   ```
3. **開啟攝影機**，看到即時偵測的影像，綠色點標示人臉特徵點。

---

## 📜 程式碼解釋

### **🔹 1. 讀取攝影機影像**

```python
cap = cv2.VideoCapture(0)
```

- `0` 代表 **內建攝影機**，若有外接攝影機可改為 `1` 或 `2`。

---

### **🔹 2. 轉換影像格式**

```python
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
```

- **OpenCV 預設是 BGR**，但 **MediaPipe 需要 RGB**，所以要先轉換格式。

---

### **🔹 3. 使用 MediaPipe 進行人臉偵測**

```python
results = face_mesh.process(rgb_frame)
```

- `face_mesh.process(rgb_frame)` 會回傳 **偵測到的 468 個臉部特徵點**。

---

### **🔹 4. 繪製人臉特徵點**

```python
for idx, landmark in enumerate(face_landmarks.landmark):
    x, y = int(landmark.x * w), int(landmark.y * h)
    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
```

- `landmark.x` 和 `landmark.y` 會回傳 **0~1 的歸一化座標**，所以要乘上 **影像寬度、高度** 才能轉換為實際像素座標。
- `cv2.circle()` 在偵測到的點上畫 **綠色圓點**。

---

### **🔹 5. 顯示影像**

```python
cv2.imshow("Face Mesh Detection", frame)
```

- 透過 `cv2.imshow()` **顯示即時影像**，畫面中會標記人臉特徵點。

---

## 📌 可能應用場景

✔ **VTuber 角色動畫製作**（可用 Landmark 來控制 3D 模型）
✔ **臉部表情分析**（分析臉部變化，例如微笑、皺眉）
✔ **即時特效**（可加上「大眼特效」、「嘴巴縮小」等搞笑濾鏡）
✔ **人臉識別前處理**（用 Landmark 提取關鍵特徵，進行比對）

---

## 📜 **完整程式碼**

```python
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

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape
            for idx, landmark in enumerate(face_landmarks.landmark):
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow("Face Mesh Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```


🌟 **如果覺得不錯，請幫忙按顆星⭐！**
