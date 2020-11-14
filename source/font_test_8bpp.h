
/*
 * Image:        font_test_8bpp
 * Size:         640
 * Width:        80
 * Height:       8
 *
 * Palette size: 2
 */

#ifndef FONT_TEST_8BPP_H
#define FONT_TEST_8BPP_H

#define	font_test_8bpp_size 640	// Byte-expressed image size
#define	font_test_8bpp_length 160	// Array length
#define	font_test_8bpp_width 80	// Image Width
#define	font_test_8bpp_height 8	// Image Height
#define	font_test_8bpp_palette_size 4	// Bye-expressed Palette Size
#define	font_test_8bpp_palette_length 1	// Palette array length

extern const unsigned int font_test_8bpp_palette[font_test_8bpp_palette_length];
extern const unsigned int font_test_8bpp_data[font_test_8bpp_length];

#endif//FONT_TEST_8BPP_H