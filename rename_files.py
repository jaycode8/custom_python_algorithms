import os

def rename_files(path):
    files = os.listdir(path)
    for i,file_name in enumerate(files):
        f_name, f_ext = os.path.splitext(file_name)
        new_file_name = f'zero_{str(i+1).zfill(3)}{f_ext}'
        curent_name = os.path.join(path,file_name)
        new_name = os.path.join(path, new_file_name)

        os.rename(curent_name, new_name)
        

path = '#provide the directory containing the files'
rename_files(path)