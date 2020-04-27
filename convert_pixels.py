import os
from PIL import Image
from shutil import copy, copytree

root = '/home/chai/Downloads/Cupertino-KDE/'
copy_root = '/home/chai/Downloads/Cupertino-KDE_copy/'
for next_dir in os.listdir(root):
    if not os.path.isdir(root + next_dir):
        copy(root + next_dir, copy_root + next_dir)
    else:
        next_dir += '/'
        dirs = os.listdir(root + next_dir)
        os.makedirs(copy_root + next_dir)
        for each_dir in dirs:
            if each_dir.isdigit():
                os.makedirs(copy_root + next_dir + each_dir)
                width = int(each_dir)
                height = int(each_dir)
                each_dir += '/'
                for img in os.listdir(root + next_dir + each_dir):
                    try:
                        pic = Image.open(root + next_dir + each_dir + img)
                        if pic.size[0] != width and pic.size[1] != height:
                            newpic = pic.resize((width, height), Image.ANTIALIAS)
                            newpic.save(copy_root + next_dir + each_dir + img)
                        else:
                            # print(img, 'is normal.')
                            copy(root + next_dir + each_dir + img, copy_root + next_dir + each_dir + img)
                    except:
                        print(img, 'is not png.')
                        copy(root + next_dir + each_dir + img, copy_root + next_dir + each_dir + img)
            else:
                try:
                    copytree(root + next_dir + each_dir, copy_root + next_dir + each_dir)
                except:
                    print(root + next_dir + each_dir)