import os
png_filenames = []
for file in os.listdir("./images"):
    if file.endswith(".png"):
        png_filenames.append(os.path.join("images", file))