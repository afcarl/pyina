#!/usr/bin/env python

from pyina.launchers import Mpi

#XXX:: can fail with NameError: global name 'func' is not defined
#XXX:: can fail with RuntimeError: maximum recursion depth exceeded
#from mystic.models.poly import chebyshev8cost as func

def host(coeffs):
    from mystic.models.poly import chebyshev8cost as func
    return "Chebyshev%s = %s" % (coeffs, func(coeffs))

params = [(i,0,-2*i,0,4*i,0,-2*i,0,i) for i in range(10)]
pool = Mpi()

print "Evaluate the 8th order Chebyshev polynomial..."
print "Using 'dill' for 10 combinations over 4 nodes"
pool.nodes = 4
res1 = pool.map(host, params)
print pool
print '\n'.join(res1)
print ''

print "Using 'dill.source' for 10 combinations over 4 nodes"
pool.source = True
res2 = pool.map(host, params)
print pool
print '\n'.join(res2)

# end of file
