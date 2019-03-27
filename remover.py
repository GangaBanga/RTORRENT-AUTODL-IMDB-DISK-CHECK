# -*- coding: utf-8 -*-

import sys, os
from remotecall import xmlrpc

t_hash = sys.argv[1]
t_path = sys.argv[2]

files = xmlrpc('f.multicall', (t_hash, '', 'f.frozen_path='))
t_hash = tuple([t_hash])
xmlrpc('d.tracker_announce', t_hash)
xmlrpc('d.erase', t_hash)

if len(files) <= 1:
        os.remove(files[0][0])
else:
        [os.remove(file[0]) for file in files]

        try:
                os.rmdir(t_path)
        except:

                for root, directories, files in os.walk(t_path, topdown=False):

                        try:
                                os.rmdir(root)
                        except:
                                pass
