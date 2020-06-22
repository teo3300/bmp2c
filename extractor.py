def slot(mem, pos, size):
    '''Read byte chunks (little endian)'''
    value = 0
    for i in range(pos+size-1, pos-1, -1):
        value = (value<<8) + mem[i]
    return value
    # Read <size> elements (bytes) from list as single value

def loadData(mem):
    if not slot(mem, 0, 2) == 19778:
        print('ERROR: unknown file format')
        exit()
    bpp = slot(mem,28,2)
    if (not bpp == 16):
        print('ERROR: bitdepth must be 16bpp, found', bpp +'bpp')
        exit()
    img_offset = slot(mem,10,4)
    img_width  = slot(mem,18,4)
    img_height = slot(mem,22,4)
    img_size   = slot(mem,34,4)
    return (img_offset, img_size, img_width, img_height)
    # Return image info
