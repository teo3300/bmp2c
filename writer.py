import text

def hx(data):
    return '{:08x}'.format(data)

def joint(index_map, ii, bpp):
    if bpp == 8:
        ratio = 1
    elif bpp == 4:
        ratio = 2
    value = 0
    for i in range(0, 2<<ratio):
        value = value + (index_map[ii+i]<<(i*bpp))
    return value

def writeInfo(file, name, data, bpp, pal_len):
    img_size   = data[1]
    img_width  = data[2]
    img_height = data[3]

    if bpp == 8:
        ratio = 1
    elif bpp == 4:
        ratio = 2

    file.write(text.info.format(name, img_size>>ratio, img_width, img_height, pal_len))
    file.write('#ifndef '+ name.upper() + '_H\n')
    file.write('#define '+ name.upper() + '_H\n\n')
    file.write(text.define.format(name, 'size',           img_size>>ratio,     '// Byte-expressed image size'))
    file.write(text.define.format(name, 'length',         img_size>>(ratio+2), '// Array length'             ))
    file.write(text.define.format(name, 'width',          img_width,           '// Image Width'              ))
    file.write(text.define.format(name, 'height',         img_height,          '// Image Height'             ))
    file.write(text.define.format(name, 'palette_size',   pal_len<<1,          '// Palette Size'             ))
    file.write(text.define.format(name, 'palette_length', pal_len>>1,          '// Palette Size'             ))
    file.write(text.ar_def.format(name, 'palette',        name + '_palette_length'                           ))
    file.write(text.ar_def.format(name, 'data',           name + '_length'                                   ))
    file.write('\n\n#endif//'+ name.upper() + '_H')

def writeData(file, name, data, bpp, palette, index_map):
    img_size   = data[1]
    img_width  = data[2]
    img_height = data[3]
    pal_len = len(palette)

    if bpp == 8:
        ratio = 1
    elif bpp == 4:
        ratio = 2

    file.write('#include "'+ name + '.h"')
    file.write(text.info.format(name, img_size>>ratio, img_width, img_height, pal_len))

    file.write(text.arr_open.format(name, 'palette', name+'_palette_length'))
    for ii in range(0, pal_len, 2):
        if not (ii % 16):
            file.write('\n\t')
        file.write('0x'+hx(palette[ii]+(palette[ii+1]<<16)))
        if not (ii == pal_len-2):
            file.write(', ')
    file.write('\n};\n')
    file.write(text.arr_open.format(name, 'data, ', img_size>>(ratio+2)))
    for ii in range(0, img_size>>(ratio), 2<<ratio):
        if not (ii % (16<<ratio)):
            file.write('\n\t')
        file.write('0x'+hx(joint(index_map, ii, bpp)))
        if not (ii == ((img_size>>ratio) - 2<<ratio)):
            file.write(', ')
    file.write('\n};\n')
