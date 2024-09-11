import Augmentor
import os

# Definisikan path dataset
dataset_path = 'D:\DATA\Latihan\Programming\Python\\augmentasi\\blackspot'

# Inisialisasi pipeline Augmentor
pipeline = Augmentor.Pipeline(dataset_path, output_directory=dataset_path)


# MEKANISME PERTAMA - 693/kelas (3465 TOTAL)
pipeline.rotate_random_90(probability=1)
pipeline.random_distortion(probability=1, grid_width=10, grid_height=10, magnitude=12)
pipeline.random_brightness(probability=1, min_factor=0.5, max_factor=1.5)
pipeline.zoom_random(probability=1, percentage_area=0.9)


# Untuk pake mekanisme kedua, comment dulu code mekanisme pertama
# MEKANISME KEDUA - 693/kelas (3465 TOTAL)
# pipeline.flip_random(probability=1)
# pipeline.shear(probability=1, max_shear_left=10, max_shear_right=10)
# pipeline.random_contrast(probability=1, min_factor=0.8, max_factor=1.5)
# pipeline.skew(probability=1)

# Jumlah gambar augmetnasi yang dihasilkan per 1 gambar asli
num_of_augmented_images = 10

# Eksekusi augmentasi untuk semua gambar dalam folder
for image_path in os.listdir(dataset_path):
    if image_path.endswith(('.jpg')):
        image_full_path = os.path.join(dataset_path, image_path)
        pipeline.image_input = image_full_path
        pipeline.sample(num_of_augmented_images)
print("Augmentation completed.")

