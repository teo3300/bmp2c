
/*
 * Image:        test_4bpp
 * Size:         19200
 * Width:        240
 * Height:       160
 *
 * Palette size: 16
 */

#ifndef TEST_4BPP_H
#define TEST_4BPP_H

#define	test_4bpp_size 19200	// Byte-expressed image size
#define	test_4bpp_length 4800	// Array length
#define	test_4bpp_width 240	// Image Width
#define	test_4bpp_height 160	// Image Height
#define	test_4bpp_palette_size 32	// Palette Size
#define	test_4bpp_palette_length 8	// Palette Size

extern const unsigned int test_4bpp_palette[test_4bpp_palette_length];
extern const unsigned int test_4bpp_data[test_4bpp_length];

#endif//TEST_4BPP_H