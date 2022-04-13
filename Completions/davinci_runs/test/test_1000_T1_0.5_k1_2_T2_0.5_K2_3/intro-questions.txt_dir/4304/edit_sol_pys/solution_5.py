import os

#print(os.getcwd())

#os.chdir(r'C:\Users\sagar\Desktop\Python\file')

#print(os.getcwd())

#os.chdir(r'C:\Users\sagar\Desktop\Python')

#print(os.getcwd())

#print(os.listdir())

#os.mkdir('new')

#os.makedirs('new/new2/new3')

#os.rmdir('new')

#os.removedirs('new/new2/new3')

#print(os.listdir())

#print(os.stat('file.py'))

#print(os.stat('file.py').st_ctime)

#from datetime import datetime

#mod_time = os.stat('file.py').st_mtime

#print(datetime.fromtimestamp(mod_time))

#print(os.listdir())

#for dirpath, dirnames, filenames in os.walk('C:\\Users\\sagar\\Desktop\\Python'):
#    print('Current Path:', dirpath)
#    print('Directories:', dirnames)
#    print('Files:', filenames)
#    print()

#print(os.environ.get('PATH'))

#file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

#print(file_path)

#print(os.path.basename('/tmp/test.txt'))

#print(os.path.dirname('/tmp/test.txt'))

#print(os.path.split('/tmp/test.txt'))

#print(os.path.exists('/tmp/test.txt'))

#print(os.path.isfile('/tmp/test.txt'))

#print(os.path.isdir('/tmp/test.txt'))

#print(os.path.splitext('/tmp/test.txt'))

#print(dir(os.path))

#print(os.listdir())

#for f in os.listdir():
#    f_name, f_ext = os.path.splitext(f)
#    f_title, f_number = f_name.split('-')
#    f_title = f_title.strip()
#    f_number = f_number.strip()[1:].zfill(2)
#    print('{}-{}{}'.format(f_number, f_title, f_ext))

#from PIL import Image

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#print(img.size)
#print(img.format)
#img.show()

#new_img = img.resize((300, 300))
#new_img.save('resized.jpg')

#new_img.show()

#print(img.size)
#print(img.format)
#print(img.mode)

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#img.rotate(90).save('rotated_pikachu.jpg')

#img.show()

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#img = img.convert('L')

#img.show()

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#new_img = img.resize((150, 150))

#new_img.save('pikachu_thumbnail.jpg')

#img.show()

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#img.thumbnail((150, 150))

#img.save('pikachu_thumbnail.jpg')

#img.show()

#import glob

#for img in glob.glob('*.jpg'):
#    print(img)

#from PIL import Image

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#img.save('pikachu.png')

#img.show()

#from PIL import Image

#img = Image.open(r'C:\Users\sagar\Desktop\Python\file\Pokedex\pikachu.jpg')

#img.show()

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for file in os.listdir('.'):
#    if file.endswith('.jpg'):
#        img = Image.open(file)
#        clean_name = os.path.splitext(file)[0]
#        img.save(f'{clean_name}.png')
#        print('all done')

#from PIL import Image
#import os

#for
