import sys
sys.path.append('./src')

from random_rhythms.random_rhythms import Rhythm

rr = Rhythm()
assert rr.time_signature == '4/4'
assert rr.measure_size == 4
assert rr.durations == [ 1/4, 1/2, 1/3, 1, 3/2, 2 ]
assert rr.weights == [ 1, 1, 1, 1, 1, 1 ]
assert rr.groups == { 1/3: 3 }
assert rr.smallest == 1/128

motif = rr.motif()
assert isinstance(motif, list), "motif is not a list"