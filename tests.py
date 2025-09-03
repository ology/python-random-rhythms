import sys
sys.path.append('./src')

from random_rhythms.random_rhythms import Rhythm

rr = Rhythm()
motif = rr.motif()
assert isinstance(motif, list), "motif is not a list"

rr = Rhythm(
    durations=[1],
)
motif = rr.motif()
assert isinstance(motif, list), "motif is not a list"