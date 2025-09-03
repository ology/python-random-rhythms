import sys
sys.path.append('./src')

from random_rhythms.random_rhythms import Rhythm

rr = Rhythm()
motif = rr.motif()
assert isinstance(motif, list), "motif is not a list"

rr = Rhythm(
    measure_size=1,
    durations=[1],
)
assert rr.weights == [1]
motif = rr.motif()
assert motif == [1]