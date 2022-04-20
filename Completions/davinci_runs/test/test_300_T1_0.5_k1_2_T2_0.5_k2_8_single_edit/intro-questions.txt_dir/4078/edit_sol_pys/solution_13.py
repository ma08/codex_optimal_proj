import os
import shutil

if os.path.exists('.git'):
    shutil.rmtree('.git')

if os.path.exists('README.md'):
    os.remove('README.md')

if os.path.exists('file'):
    os.remove('file')

if os.path.exists('setup.py'):
    os.remove('setup.py')
