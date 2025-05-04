from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

print("import berhasil")
import os

# --- Konfigurasi awal ---
# Nama mahasiswa (bisa kamu ambil dari database saat registrasi)
nim = '22040123'
nama = 'Budi Santoso'
folder_nama = f"{nim} - {nama}"

# Lokasi file telapak kiri dan kanan
gambar_kiri = f'gambar_mahasiswa/{nim}_kiri.jpg'
gambar_kanan = f'gambar_mahasiswa/{nim}_kanan.jpg'

# Folder output hasil augmentasi
output_dir = os.path.join('augment', folder_nama)
os.makedirs(output_dir, exist_ok=True)

# Inisialisasi ImageDataGenerator
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

def augment_image(image_path, prefix, save_dir, jumlah_aug=11):
    img = load_img(image_path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir=save_dir,
                              save_prefix=prefix,
                              save_format='jpeg'):
        i += 1
        if i >= jumlah_aug:
            break

# Proses augmentasi untuk kiri dan kanan
augment_image(gambar_kiri, prefix=f'{nim}_kiri_aug', save_dir=output_dir)
augment_image(gambar_kanan, prefix=f'{nim}_kanan_aug', save_dir=output_dir)

print(f"✅ Augmentasi selesai. 22 file disimpan di folder: {output_dir}")