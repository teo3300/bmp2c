
/*
 * Image:        test_8bpp
 * Size:         38400
 * Width:        240
 * Height:       160
 *
 * Palette size: 16
 */

#ifndef TEST_8BPP_H
#define TEST_8BPP_H

#define	test_8bpp_size 38400	// Byte-expressed image size
#define	test_8bpp_length 9600	// Array length
#define	test_8bpp_width 240	// Image Width
#define	test_8bpp_height 160	// Image Height
#define	test_8bpp_palette_size 32	// Palette Size
#define	test_8bpp_palette_length 8	// Palette Size

extern const unsigned int test_8bpp_palette[test_8bpp_palette_length];
extern const unsigned int test_8bpp_data[test_8bpp_length];

#endif//TEST_8BPP_H