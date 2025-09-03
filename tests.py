import sys
sys.path.append('./src')

from random_rhythms.random_rhythms import Rhythm

rr = Rhythm(
    measure_size=4,
    durations=[1/4, 1/2, 1/3, 1, 3/2, 2],
    weights=[1, 1, 1, 1, 1, 1],
    groups={1/3: 3},
    smallest=1/128
)

motif = rr.motif()
assert isinstance(motif, list), "motif is not a list"

motif = rr.motif()
assert isinstance(motif, list), "motif is not a list"