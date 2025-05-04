import os
import cv2
import numpy as np

def preprocess_images(input_dir, output_dir, target_size=(224, 224)):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)

            if img is None:
                print(f"⚠ Gagal memuat gambar: {img_path}")
                continue

            img = cv2.resize(img, target_size)
            img = img.astype('float32') / 255.0  # normalisasi

            # Ganti semua ekstensi ke .npy
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_dir, base_name + '.npy')
            np.save(output_path, img)

    print(f"✅ Preprocessing selesai. File .npy disimpan di: {output_dir}")