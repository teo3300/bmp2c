
/*
 * Image:        font_test_4bpp
 * Size:         320
 * Width:        80
 * Height:       8
 *
 * Palette size: 2
 */

#ifndef FONT_TEST_4BPP_H
#define FONT_TEST_4BPP_H

#define	font_test_4bpp_size 320	// Byte-expressed image size
#define	font_test_4bpp_length 80	// Array length
#define	font_test_4bpp_width 80	// Image Width
#define	font_test_4bpp_height 8	// Image Height
#define	font_test_4bpp_palette_size 4	// Bye-expressed Palette Size
#define	font_test_4bpp_palette_length 1	// Palette array length

extern const unsigned int font_test_4bpp_palette[font_test_4bpp_palette_length];
extern const unsigned int font_test_4bpp_data[font_test_4bpp_length];

#endif//FONT_TEST_4BPP_H