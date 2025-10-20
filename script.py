import os
import shutil

def declutter(path):
    extension_map = {
        'Images' : ('jpg','jpeg','heic','png',),
        'Videos' : ('mp4',),
        'Audio' : ('aac','mp3',),
        'Compressed' : ('zip','rar','tar'),
        'Code' :   ('py','php','html','xml','js','sh','cpp','c'),
        'Documents' : ('pdf','txt','csv','docx','doc','xls','xlsx'),
    }  # Press F9 to toggle the breakpoint.

if __name__ == '__main__':
    path = input('Enter path: ')
    if os.path.isabs(path) and os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(os.path.join(path, file)):
                print(os.path.join(path, file))
        print('Path exists')
    else:
        print('Path doesn\'t exist')
    declutter(path)