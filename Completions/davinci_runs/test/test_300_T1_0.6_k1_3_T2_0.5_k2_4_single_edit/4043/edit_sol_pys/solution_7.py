import os
import sys

def read(path):
    with open(path, 'r') as f:
        return f.read()

def create(path, content):
    with open(path, 'w') as f:
        f.write(content)

def append(path, content):
    with open(path, 'a') as f:
        f.write(content)

def delete(path):
    os.remove(path)

def copy(src, dst):
    with open(src, 'r') as f:
        with open(dst, 'w') as g:
            g.write(f.read())

def move(src, dst):
    copy(src, dst)
    delete(src)

def exists(path):
    return os.path.exists(path)

def is_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def get_size(path):
    return os.path.getsize(path)

def get_parent(path):
    return os.path.dirname(path)

def get_name(path):
    return os.path.basename(path)

def get_ext(path):
    return os.path.splitext(path)[1]

def get_last_modified(path):
    return os.path.getmtime(path)

def get_last_accessed(path):
    return os.path.getatime(path)

def get_created(path):
    return os.path.getctime(path)

def get_all_files(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_all_dirs(path):
    return [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def get_all_files_recursive(path):
    files = []
    for root, subdirs, f in os.walk(path):
        for file in f:
            files.append(os.path.join(root, file))
    return files

def get_all_dirs_recursive(path):
    dirs = []
    for root, subdirs, f in os.walk(path):
        for dir in subdirs:
            dirs.append(os.path.join(root, dir))
    return dirs

def get_all_files_and_dirs(path):
    return os.listdir(path)

def get_all_files_and_dirs_recursive(path):
    files = []
    for root, subdirs, f in os.walk(path):
        for dir in subdirs:
            files.append(os.path.join(root, dir))
        for file in f:
            files.append(os.path.join(root, file))
    return files

def create_dir(path):
    os.mkdir(path)

def create_dirs(path):
    os.makedirs(path)

def create_temp_file(content):
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        return f.name

def create_temp_dir():
    import tempfile
    return tempfile.mkdtemp()

def get_temp_dir():
    return os.getenv('TEMP')

def get_current_dir():
    return os.getcwd()

def get_current_file():
    return os.path.realpath(sys.argv[0])

def get_user():
    return os.getenv('USERNAME')

def get_home_dir():
    return os.getenv('HOME')

def get_desktop_dir():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def get_documents_dir():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')

def get_downloads_dir():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

def get_pictures_dir():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')

def get_music_dir():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music')

def get_videos_dir():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
