"""Public tests for Lab 13. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab13 as lab  # noqa: E402

def test_conditional_probability():
    joint = {(True, True): 0.2, (True, False): 0.2, (False, True): 0.2, (False, False): 0.4}
    assert abs(lab.conditional_probability(joint, True, True) - 0.5) < 1e-9

def test_question_has_four_options():
    assert len(lab.make_question(0)["options"]) == 4
