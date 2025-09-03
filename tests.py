import sys
sys.path.append('./src')

from random_rhythms.random_rhythms import Rhythm

r = Rhythm()
motif = r.motif()
assert isinstance(motif, list), "motif is not a list"

r = Rhythm(
    measure_size=1,
    durations=[1],
)
assert r.weights == [1], "weights not correct"
motif = r.motif()
assert motif == [1], "motif not correct"