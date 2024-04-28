import os

def remove_prefix(folder_path):
    if not os.path.isdir(folder_path):
        print("O caminho fornecido não é uma pasta.")
        return
    
    for filename in os.listdir(folder_path):
        if filename.startswith("[SPOTIFY-DOWNLOADER.COM]"):
            old_filepath = os.path.join(folder_path, filename)
            new_filename = filename.replace("[SPOTIFY-DOWNLOADER.COM]", "")
            new_filepath = os.path.join(folder_path, new_filename)
            
            os.rename(old_filepath, new_filepath)
            print(f"Renomeado: {filename} -> {new_filename}")

folder_path = "/caminho/da/sua/pasta"

remove_prefix(folder_path)
