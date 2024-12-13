import os
import shutil
from generate_page import *

base_path = os.path.dirname(os.path.dirname(__file__))

def main():
    if "public" in os.listdir(base_path):
        shutil.rmtree(os.path.join(base_path, 'public'))
    os.mkdir(os.path.join(base_path, 'public'))
    static_path = os.path.join(base_path, 'static')
    dest_path = os.path.join(base_path, 'public')
    copy_file(static_path, dest_path)
    generate_page('./content/index.md', './template.html', './public/index.html')
        

def copy_file(source_path, dest_path):
    files = os.listdir(source_path)
    for file in files:
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_path)
        else:
            os.mkdir(os.path.join(dest_path, f'{file}'))
            copy_file(file_path, os.path.join(dest_path, f'{file}'))
    
main()