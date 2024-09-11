import os

def rename_images(dataset_path):
    # Mendapatkan daftar gambar dalam folder
    images = os.listdir(dataset_path)

    # Mendapatkan daftar file gambar dalam folder
    total_images = len([img for img in images if img.lower().endswith(('.jpg'))])

    # Inisialisasi counter untuk nama gambar
    count = 1

    # Iterasi melalui setiap gambar dalam folder
    for img in images:
        if img.lower().endswith(('.jpg')):
            # Membuat path lama dan baru untuk gambar
            old_path = os.path.join(dataset_path, img)
            new_name = f"{count}.jpg"
            new_path = os.path.join(dataset_path, new_name)

            # Mengganti nama img
            os.rename(old_path, new_path)

            # Menambahkan counter
            count += 1

    print(f"Successfully renamed {count-1} an image in a folder.")

dataset_path = 'D:\DATA\dataset_kentang\dataset_augmented_2\blackspot_bruising'
rename_images(dataset_path)
