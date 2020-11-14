info = '''
/*
 * Image:        {}
 * Size:         {}
 * Width:        {}
 * Height:       {}
 *
 * Palette size: {}
 */

'''
define  = '#define\t{}_{} {}\t{}\n'
ar_def = '\nextern const unsigned int {}_{}[{}];'
arr_open = '\nconst unsigned int {}_{}[{}] __attribute__((allign(4))) = \n{{'
