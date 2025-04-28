import numpy as np
import tensorflow as tf
from PIL import Image
import os

# Load model saat pertama kali
model_path = os.path.join('src', 'storage', 'models',
                          'hand_recognition_model.h5')
model = tf.keras.models.load_model(model_path)

# Mapping ID hasil prediksi ke student_id
# Note: Ini dummy, nanti idealnya mapping ini di database
student_mapping = {
    0: 1,  # id student 1
    1: 2,  # id student 2
    # dst
}


def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224))  # menyesuaikan ukuran input model
    img_array = np.array(img) / 255.0  # normalisasi
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension
    return img_array


def predict_hand_owner(image_path):
    img_array = preprocess_image(image_path)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])

    student_id = student_mapping.get(predicted_class, None)
    confidence = float(np.max(predictions[0]))

    return student_id, confidence
