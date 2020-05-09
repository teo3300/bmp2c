def mapColor(mem, data, bpp):
    palette = [0]
    index_map = []
    data_offset = data[0]
    img_size = data[1]
    lost = 0
    evened = 0

    from extractor import slot
    for wStart in range(data_offset, data_offset+img_size, 2):
        colorID = slot(mem, wStart, 2)
        if (colorID & 32768):
            if not (colorID in palette[1:]):
                if (len(palette) < (1<<bpp)):
                    palette.append(colorID)
            try:
                index_map.append(palette.index(colorID))
            except:
                index_map.append(0)
                lost = lost + 1
        else:
            index_map.append(0)
    if len(palette) % 2:
        palette.append(0)
        evened = 1
    return (palette, index_map, (lost, evened))

def imgFlip(index_map, data):
    reversed = []
    w = data[2]
    h = data[3]

    for scan_line in range(h-1, -1, -1):
        reversed.extend(index_map[scan_line*w:scan_line*w+w])
    return reversed

def translatePalette(old_palette):
    new_palette = []
    for colorID in old_palette:
        red = (colorID>>10)&31
        green = (colorID>>5)&31
        blue = (colorID&31)
        new_color = ((blue<<5)+green<<5)+red
        new_palette.append(new_color)
    return new_palette

def warning(stat, name):
    if stat[0]:
        print('WARNING:', name, stat[0], 'color/s lost due to palette size exceeded')
    if stat[1]:
        print('Palette size evened\n')
