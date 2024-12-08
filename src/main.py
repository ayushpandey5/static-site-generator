import os
import shutil

base_path = '.'
def main():
    if os.path.exists(os.path.join(base_path, 'public')):
        shutil.rmtree(os.path.join(base_path, 'public'))
    os.mkdir(os.path.join(base_path, 'public'))
    copy_files(os.path.join(base_path, 'static'), os.path.join(base_path, 'public'))
        

def copy_files(source_path, dest_path):
    items = os.listdir(source_path)
    for item in items:
        if os.path.isfile(os.path.join(source_path, item)):
            shutil.copy(os.path.join(source_path, item), dest_path)
        else:
            dest_dir = os.path.join(dest_path, item)
            os.mkdir(dest_dir)
            copy_files(os.path.join(source_path, item), dest_dir)
        print(f"Copied {item} to {dest_path}")
main()