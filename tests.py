import sys
sys.path.append('./src')

from random_rhythms.random_rhythms import Rhythm

r = Rhythm()
motif = r.motif()
assert isinstance(motif, list), "motif is not a list"

r = Rhythm(
    durations=[4],
)
assert r.weights == [1], "weights not correct"
motif = r.motif()
assert motif == [4], "motif not correct"

r = Rhythm(
    durations=[1],
)
motif = r.motif()
assert motif == [1,1,1,1], "motif not correct"

r = Rhythm(
    durations=[2/3],
)
motif = r.motif()
assert motif == [2/3 for x in range(6)], "motif not correct"

r = Rhythm(
    measure_size=8,
    durations=[4],
)
motif = r.motif()
assert motif == [4,4], "motif not correct"

r = Rhythm(
    measure_size=100,
    durations=[50],
)
motif = r.motif()
assert motif == [50,50], "motif not correct"

r = Rhythm(
    durations=[1,2],
    weights=[0,1],
)
motif = r.motif()
assert motif == [2,2], "motif not correct"

r = Rhythm(
    durations=[3],
)
motif = r.motif()
assert motif == [3,1], "motif not correct"