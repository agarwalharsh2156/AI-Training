import os

file_path = r".\sample_file.txt"
if os.path.exists(file_path):
    print(True)
else:
    print(False)


with open(file_path, "a") as f:
    print(f.writable())
    
    f.writelines("""Hi, my name is Harsh.\nI am from Maharashtra.""")