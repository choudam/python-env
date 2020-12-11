# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:49:59 2020

@author: srinic
"""

import lmdb

#key1="1".encode('ascii')
#value1="test updated".encode('ascii')
env=lmdb.open("data", map_size=50000000)

"""
with env.begin(write=True) as txn:
    for id in range(100000):
        k1='{:01}'.format(id).encode('ascii')
        v1=' add somemore put more data on this sample record for id {0}'.format(id).encode('ascii')       
        txn.put(k1,v1)
        
#    x=txn.get(key1)
#    print(x)


with env.begin(write=False) as txn:

    for id in np.random.randint(1, 10000000,5000):
        k1='{:01}'.format(id).encode('ascii')
        x=txn.get(k1)
        print("{0} = {1}", id, x)

    print(txn.stat())
"""

with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        print(key, value)
        
        
env.close() 