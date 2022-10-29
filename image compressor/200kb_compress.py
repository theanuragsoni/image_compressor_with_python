
import os
from tkinter import messagebox
import tinify

# tinify_key = ["LTPjzX2VJF0QPTJJNw0xhHLvbVpSQhkTasdjklf", "v3LpvsWlN7th7L0nFYFqH9vFPBhj1J3p"]
tinify_key = ["LTPjzX2VJF0QPTJJNw0xhHLvbVpSQhkT", "v3LpvsWlN7th7L0nFYFqH9vFPBhj1J3p"]
tinify_key_number = 0
tinify.key = tinify_key[tinify_key_number]

for image in os.listdir():
    if ".jpeg" in image or ".jpg" in image or ".png" in image or ".gif" in image:
        print(f"Compressing {image}")
        def compress_to_200_width(image):
            source = tinify.from_file(image)
            resized = source.resize(
                method="scale",
                width=600,
                # width=200,
            )
            resized.to_file("comp-" + image)
            # print(f"{image} compressed successfully")
            # print(f"Images compressed this month: {tinify.compression_count}, in key {tinify.key}")

        try:
            compress_to_200_width(image)
        except tinify.AccountError:
            tinify.key = tinify_key[tinify_key_number + 1]
            compress_to_200_width(image)

messagebox.showinfo("", "Image(s) compressd successfully.")
