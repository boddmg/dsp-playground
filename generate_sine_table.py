import numpy as np
import jinja2

MAX_LENGTH = 1000
MAX_VALUE = 4095

h_template = \
'''#ifndef __SIN_TABLE_H_
#define __SIN_TABLE_H_

#define SIN_TABLE_MAX_LENGTH [[MAX_LENGTH]]
#define SIN_TABLE_MAX_INDEX (SIN_TABLE_MAX_LENGTH - 1)

#include <stdint.h>
extern const uint16_t SIN_TABLE[SIN_TABLE_MAX_LENGTH];

#endif
'''

c_template = \
'''#include "sin_table.h"
const uint16_t SIN_TABLE[SIN_TABLE_MAX_LENGTH] = {[[DATA]]};
'''

def main():
    sin_table = range(MAX_LENGTH)
    sin_table = np.array(sin_table) * 1.0 / MAX_LENGTH * 2 * np.pi
    sin_table = np.sin(sin_table)
    sin_table = sin_table / 2.0 * MAX_VALUE  + MAX_VALUE / 2
    sin_table = sin_table.astype(np.uint32)
    print(sin_table)
    sin_table_string = ''
    for i in sin_table:
        sin_table_string += str(i)
        sin_table_string += ', '
    sin_table_string = sin_table_string[:-2]

    c_file = c_template.replace('[[DATA]]', sin_table_string)
    h_file = h_template.replace('[[MAX_LENGTH]]', str(MAX_LENGTH))
    open("sin_table.c", 'w').write(c_file)
    open("sin_table.h", 'w').write(h_file)

if __name__ == '__main__':
    main()
