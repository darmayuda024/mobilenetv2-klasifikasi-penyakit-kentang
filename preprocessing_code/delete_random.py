import os
import random

def delete_random_images(dataset_path, num_of_image_delete=27):
    try:
        # Mendapatkan daftar file gambar dalam folder
        images = [img for img in os.listdir(dataset_path) if img.lower().endswith(('.jpg'))]

         # Menentukan jumlah gambar yang akan dihapus
        num_of_image_delete = min(num_of_image_delete, len(images))

        # Memilih gambar secara acak untuk dihapus
        sample_image_delete = random.sample(images, num_of_image_delete)

        # Menghapus gambar yang telah dipilih
        for img in sample_image_delete:
            path_file = os.path.join(dataset_path, img)
            os.remove(path_file)
            print(f"Image {img} already delete.")

        print(f"\nTotal {num_of_image_delete} image already delete from {dataset_path}.")

    except Exception as e:
        print(f"Error : {e}")

# lokasi path dataset
dataset_path = 'D:\DATA\dataset_kentang\dataset_augmented_2\soft_rot'
delete_random_images(dataset_path)
