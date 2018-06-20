# coding: utf8

import os
import sys

# We then load the all namespaces so that if it's imported in any way, it's
# still available
CURDIR = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(CURDIR, 'src')

sys.path.append(SRCDIR)

from pypnnomenclature.admin import * # noqa