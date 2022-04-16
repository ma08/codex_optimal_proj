import os
import sys
import re
import json

def get_file_list(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            file_list.append(os.path.join(root, f))
    return file_list

def get_file_content(file_path):
    with open(file_path, 'rb') as f:
        content = f.read().decode('utf-8', 'ignore')
        return content

def get_file_name(file_path):
    return file_path.split('/')[-1]

def get_file_suffix(file_path):
    return file_path.split('.')[-1]

def get_file_size(file_path):
    return os.path.getsize(file_path)

def get_file_abspath(file_path):
    return os.path.abspath(file_path)

def get_file_abspath_list(file_path_list):
    abspath_list = []
    for file_path in file_path_list:
        abspath_list.append(os.path.abspath(file_path))
    return abspath_list

def get_file_absdir(file_path):
    return os.path.dirname(os.path.abspath(file_path))

def get_file_type(file_path):
    cmd = 'file ' + file_path
    return os.popen(cmd).read().strip()

def get_file_md5(file_path):
    cmd = 'md5sum ' + file_path
    return os.popen(cmd).read().strip().split(' ')[0]

def get_file_sha1(file_path):
    cmd = 'sha1sum ' + file_path
    return os.popen(cmd).read().strip().split(' ')[0]

def get_file_sha256(file_path):
    cmd = 'sha256sum ' + file_path
    return os.popen(cmd).read().strip().split(' ')[0]

def get_file_sha512(file_path):
    cmd = 'sha512sum ' + file_path
    return os.popen(cmd).read().strip().split(' ')[0]

def get_file_sha(file_path):
    file_sha = {
        'md5': get_file_md5(file_path),
        'sha1': get_file_sha1(file_path),
        'sha256': get_file_sha256(file_path),
        'sha512': get_file_sha512(file_path)
    }
    return file_sha

def get_file_magic(file_path):
    cmd = 'file -b ' + file_path
    return os.popen(cmd).read().strip()

def get_file_info(file_path):
    file_info = {}
    file_info['name'] = get_file_name(file_path)
    file_info['suffix'] = get_file_suffix(file_path)
    file_info['size'] = get_file_size(file_path)
    file_info['abspath'] = get_file_abspath(file_path)
    file_info['absdir'] = get_file_absdir(file_path)
    file_info['type'] = get_file_type(file_path)
    file_info['magic'] = get_file_magic(file_path)
    file_info['md5'] = get_file_md5(file_path)
    file_info['sha1'] = get_file_sha1(file_path)
    file_info['sha256'] = get_file_sha256(file_path)
    file_info['sha512'] = get_file_sha512(file_path)
    file_info['sha'] = get_file_sha(file_path)
    return file_info

def get_file_info_list(file_path_list):
    file_info_list = []
    for file_path in file_path_list:
        file_info_list.append(get_file_info(file_path))
    return file_info_list

def get_file_info_list_by_dir(dir_path):
    file_path_list = get_file_list(dir_path)
    return get_file_info_list(file_path_list)

def get_file_info_list_by_dir_json(dir_path):
    return json.dumps(get_file_info_list_by_dir(dir_path))

def get_file_info_list_by_dir_json_file(dir_path, file_path):
    with open(file_path, 'w') as f:
        f.write(get_file_info_list_by_dir_json(dir_path))

def get_file_info_list_by_dir_json_file_gzip(dir_path, file_path):
    cmd = 'python file.py ' + dir_path + ' | gzip > ' + file_path
    os.system(cmd)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        dir_path = sys.argv[1]
        file_path = sys.argv[2]
        get_file_info_list_by_dir_json_file_gzip(dir_path, file_path)
    else:
        print('Usage: python file.py DIR_PATH FILE_PATH')
