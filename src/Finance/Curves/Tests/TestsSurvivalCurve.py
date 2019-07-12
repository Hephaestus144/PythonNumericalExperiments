from src.Finance.Curves.SurvivalCurve import SurvivalCurve

import numpy as np
import unittest

class SurvivalCurve_Tests(unittest.TestCase):
    # driftless test
    # pfe type test
    # stats tests
    def test_get_default_probability(self):
        tenors = np.array([0, 0.25, 0.5])
        default_probabilities = np.array([0, 0.1, 0.2])
        survival_curve = SurvivalCurve(tenors, default_probabilities, 0.4)
        expected_survival_probabilities = np.array([0, 0.05, 0.1, 0.15, 0.2])
        print(survival_curve.get_probabilities_of_default([0, 0.125, 0.25, 0.375, 0.5]))
        np.testing.assert_array_almost_equal(
            survival_curve.get_probabilities_of_default([0, 0.125, 0.25, 0.375, 0.5]),
            expected_survival_probabilities, 2)