# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 16:00:02 2017

@author: KingDash
"""

from difflib import SequenceMatcher
m = SequenceMatcher(None, "NEW YORK METS", "NEW YORK MEATS")
x=m.ratio()
print(x)
