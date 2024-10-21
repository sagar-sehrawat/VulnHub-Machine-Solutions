#!/usr/bin/env python3

import itertools


base_password = "P4SsW0rD"

possible_digits = itertools.product("0123456789", repeat=4)

for digits in possible_digits:
    full_password = base_password + ''.join(digits)
    print(full_password)
