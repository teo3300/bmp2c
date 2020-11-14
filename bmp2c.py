import os
from   os import system
import sys

from extractor   import loadData
from interpreter import mapColor, imgFlip, translatePalette, warning, imgSplit
from writer      import writeInfo, writeData
# dependencies

def main_process(sourceFile, destFold, bitDepth, splitSize):
    fileName = sourceFile.split('/')[-1].split('.')[0]

    imageObj = open(sourceFile, 'rb').read()                            # raw bmp
    meta = loadData(imageObj)                                           # image metadata
    # ^ tuple: data_offset, img_size, img_width, img_height
    palette, index_map, about = mapColor(imageObj, meta, bitDepth)      # palette indexing
    warning(about, fileName)                                            # warn about conversion errors
    index_map = imgFlip(index_map, meta)                                # GBA uses a different indexing order than bmp
    if splitSize > 0:                                                   # splitSize > 0 -> split
        index_map = imgSplit(index_map, meta, splitSize)                # manage bitmap as an <splitSize>*N image
    palette = translatePalette(palette)                                 # convert RGB to BGR

    fullName = fileName + '_' + str(bitDepth) + 'bpp'                   # used afterwards to name files, macro and variables
    writeInfo(open(destFold + '/' + fullName + '.h', 'w+'), fullName, meta, bitDepth, len(palette))
    writeData(open(destFold + '/' + fullName + '.c', 'w+'), fullName, meta, bitDepth, palette, index_map)

def main():
    if len(sys.argv)<4:
        print("Error: too fiew arguments\n\tbmp2c source_file dest_folder [split_size]\n")
        return 1
        # impossible to operate

    SOURCE   = sys.argv[1]
    if not os.path.isfile(SOURCE):
        return 1

    DESTFOLD = sys.argv[2]
    if not os.path.isdir(DESTFOLD):
        return 1

    BITDEPTH = int(sys.argv[3])

    SPLIT = 0

    if len(sys.argv) > 4:
        SPLIT = int(sys.argv[4])
        if not SPLIT > 0:
            SPLIT = 0
    else:
        SPLIT = 8
    # check splitsize
    main_process(SOURCE, DESTFOLD, BITDEPTH, SPLIT)

if __name__ == '__main__':
    main()
