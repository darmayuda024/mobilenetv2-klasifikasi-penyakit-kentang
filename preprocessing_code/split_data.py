import os
import shutil
from sklearn.model_selection import train_test_split

# Path ke folder dataset awal
original_dataset_path = 'D:\DATA\Tugas\KULIAH\SEMANGAT TA\FINAL SKRIPSI\kumpul\penomoran\super final ultimate\code clean\dataset_kentang\dataset-mean\dataset_augmented'

# Path ke folder baru yang akan dibuat
new_dataset_path = 'D:\DATA\Tugas\KULIAH\SEMANGAT TA\FINAL SKRIPSI\kumpul\penomoran\super final ultimate\code clean\dataset_kentang\dataset-mean\split\dataset_augmented'

# Tentukan nama folder untuk train, validation, dan test
train_folder = 'train'
validation_folder = 'validation'
test_folder = 'test'

# Tentukan path untuk folder train, validation, dan test
train_path = os.path.join(new_dataset_path, train_folder)
validation_path = os.path.join(new_dataset_path, validation_folder)
test_path = os.path.join(new_dataset_path, test_folder)

# Buat folder baru jika belum ada
os.makedirs(train_path, exist_ok=True)
os.makedirs(validation_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# List kategori kelas (class directories) dari folder awal
class_directories = os.listdir(original_dataset_path)

# Loop melalui setiap kategori kelas
for class_directory in class_directories:
    class_path = os.path.join(original_dataset_path, class_directory)
    images = os.listdir(class_path)

    # Bagi data menjadi train, validation, dan test
    train_images, temp_images = train_test_split(images, train_size=0.7, random_state=42)
    validation_images, test_images = train_test_split(temp_images, test_size=0.333, random_state=42)

    # Buat folder untuk setiap kelas di dalam folder train, validation, dan test
    train_class_path = os.path.join(train_path, class_directory)
    validation_class_path = os.path.join(validation_path, class_directory)
    test_class_path = os.path.join(test_path, class_directory)

    os.makedirs(train_class_path, exist_ok=True)
    os.makedirs(validation_class_path, exist_ok=True)
    os.makedirs(test_class_path, exist_ok=True)

    # Pindahkan gambar ke dalam folder masing-masing
    for image in train_images:
        source_path = os.path.join(class_path, image)
        destination_path = os.path.join(train_class_path, image)
        shutil.copy(source_path, destination_path)

    for image in validation_images:
        source_path = os.path.join(class_path, image)
        destination_path = os.path.join(validation_class_path, image)
        shutil.copy(source_path, destination_path)

    for image in test_images:
        source_path = os.path.join(class_path, image)
        destination_path = os.path.join(test_class_path, image)
        shutil.copy(source_path, destination_path)

print("The folder structure has been changed.")
