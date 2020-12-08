#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CorSaiR is a control and status register (CSR) map generator for FPGA/ASIC projects.
It generates HDL code, documentation and other artifacts from CSR map description file.
"""

from .__version__ import __version__

from . import config
from . import regmap
from . import readers
from . import writers
