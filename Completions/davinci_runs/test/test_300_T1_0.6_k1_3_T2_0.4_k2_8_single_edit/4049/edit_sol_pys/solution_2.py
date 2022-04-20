import os


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def create_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def create_project_dir(project_name):
    create_dir(project_name)


def create_queue_file(project_name, base_url, domain):
    queue = project_name + '/queue.txt'
    create_file(queue, base_url)


def create_crawled_file(project_name, domain):
    crawled = project_name + '/crawled.txt'
    create_file(crawled, '')


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
