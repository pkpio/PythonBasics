# -*- coding: utf-8 -*-
"""
Created on Thu Aug 08 15:41:50 2013

@author: Praveen Kumar
"""

import re
from IPython import embed

with open("./a.cir", "r") as cirF :
    #txt = cirF.read()
    #print txt

    for line in cirF :
        print line
        regex = re.compile("(?P<type>(r|v|i))(\w+)\s+\w+", re.IGNORECASE)
        m = re.search(regex, line)        
        if m :
            print m.group(0)
        else :
            print "bad luck bro !"