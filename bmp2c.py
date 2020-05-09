import os
from   os import system
import sys
from commands import command

from extractor   import loadData
from interpreter import mapColor, imgFlip, translatePalette, warning
from writer      import writeInfo, writeData

def main_process(path, name, bpp):
    imageObj = open(path + name, 'rb').read()
    name = name.split('.')[0]
    data = loadData(imageObj)
  # data_offset, img_size, img_width, img_height
    palette, index_map, about = mapColor(imageObj, data, bpp)
    warning(about, name)
    index_map = imgFlip(index_map, data)
    palette = translatePalette(palette)

    writeInfo(open('./source/' + name + '.h', 'w+'), name, data, bpp, len(palette))
    writeData(open('./source/' + name + '.c', 'w+'), name, data, bpp, palette, index_map)

def getSys():
    import platform
    return platform.system().lower()
sysOS = getSys()

def mkdir(path):
    dr = command[sysOS]['mkdir'] + ' ' + path
    os.system(dr)
    print('"'+ path +'" directory created')

def cls():
    os.system(command[sysOS]['cls'])

if( not os.path.isdir('./source')):
    mkdir('source')
if( not os.path.isdir('./img')):
    mkdir('img')
cwd = 'img' + command[sysOS]['sep']
if( not os.path.isdir(cwd + '8bpp')):
    mkdir(cwd + '8bpp')
if( not os.path.isdir(cwd + '4bpp')):
    mkdir(cwd + '4bpp')

fold8 = os.listdir(cwd + '8bpp')
fold4 = os.listdir(cwd + '4bpp')

i = 0
l = len(fold8)
if fold8:
    print('\nConverting 8bpp images')
    for file in fold8:
        print("Converting image {:5d} of {:5d}: {}".format(i+1, l, file))
        main_process('./img/8bpp/', fold8[i], 8)
        i=i+1

i = 0
l = len(fold4)
if fold4:
    print('\nConverting 4bpp images')
    for file in fold4:
        print("Converting image {:5d} of {:5d}: {}".format(i+1, l, file))
        main_process('./img/4bpp/', fold4[i], 4)
        i=i+1
print('\n')
