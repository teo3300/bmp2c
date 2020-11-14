import text

def hx(data):
    '''allign hex values'''
    return '{:08x}'.format(data)

def joint(index_map, ii, bpp):
    '''combine 4 or 8 index_map values together depending on bpp'''
    # This allows to create a 32bit array, instead of 16bit array,
    # which is slower to compute or 8bit array which can't be copied
    # on VRAM due to GBA limitations
    if bpp == 8:
        ratio = 1   # 4
    elif bpp == 4:
        ratio = 2   # 8
    value = 0
    for i in range(2<<ratio):
        value = value + (index_map[ii+i]<<(i*bpp))
    return value

def writeInfo(file, fullName, data, bpp, pal_len):
    '''Write infos about the data and palette array in an header file'''
    img_size   = data[1]
    img_width  = data[2]
    img_height = data[3]

    if bpp == 8:
        ratio = 1
    elif bpp == 4:
        ratio = 2
    # Use bitshift instead of multiplications and divisions

    file.write(text.info.format(fullName, img_size>>ratio, img_width, img_height, pal_len))
    # Commented infos
    file.write('#ifndef '+ fullName.upper() + '_H\n')
    file.write('#define '+ (fullName).upper() + '_H\n\n')
    # Definition to prevent include-conflicts
    file.write(text.define.format(fullName, 'size',           img_size>>ratio,     '// Byte-expressed image size' ))
    # User fot memcpy
    file.write(text.define.format(fullName, 'length',         img_size>>(ratio+2), '// Array length'              ))
    file.write(text.define.format(fullName, 'width',          img_width,           '// Image Width'               ))
    file.write(text.define.format(fullName, 'height',         img_height,          '// Image Height'              ))
    file.write(text.define.format(fullName, 'palette_size',   pal_len<<1,          '// Bye-expressed Palette Size'))
    file.write(text.define.format(fullName, 'palette_length', pal_len>>1,          '// Palette array length'      ))
    # Metadata definitions
    file.write(text.ar_def.format(fullName, 'palette',        fullName + '_palette_length'                        ))
    file.write(text.ar_def.format(fullName, 'data',           fullName + '_length'                                ))
    # Arrays declaration (exploits previous definitions for size declaration)
    file.write('\n\n#endif//'+ (fullName).upper() + '_H')

def writeData(file, fullName, data, bpp, palette, index_map):
        img_size   = data[1]
        img_width  = data[2]
        img_height = data[3]
        pal_len = len(palette)

        if bpp == 8:
            ratio = 1
        elif bpp == 4:
            ratio = 2

        file.write('#include "'+ fullName + '.h"')
        file.write(text.info.format(fullName, img_size>>ratio, img_width, img_height, pal_len))
        # Commented infos
        file.write(text.arr_open.format(fullName, 'palette', fullName+'_palette_length'))
        # Define array content (exploits previous definitions for size declaration)
        for ii in range(0, pal_len, 2):
            if not (ii % 16):
                file.write('\n\t')
            file.write('0x'+hx(palette[ii]+(palette[ii+1]<<16)))
            if not (ii == pal_len-2):
                file.write(', ')
        file.write('\n};\n')
        # Palette array is always double-16bit
        file.write(text.arr_open.format(fullName, 'data', img_size>>(ratio+2)))
        for ii in range(0, len(index_map), ratio<<2):
            if not (ii % (8<<ratio)):
                file.write('\n\t')
            file.write('0x'+hx(joint(index_map, ii, bpp)))
            if (ii < len(index_map) - (ratio<<2)):
                file.write(', ')
        file.write('\n};\n')
