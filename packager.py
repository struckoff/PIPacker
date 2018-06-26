import callable_pip as pip
import shutil
import os

def download_package(name, paent_dir):
    pip.main('download', '-d', f'{paent_dir}{os.sep}{name}', name)
    return f'{paent_dir}{os.sep}{name}'

def pack(name, source_path):
    return shutil.make_archive(name, 'zip', root_dir=source_path)

if __name__ == '__main__':
    name = 'pip-save'
    path = download_package(name, 'packages')
    p = pack(name, path)
    print(p)