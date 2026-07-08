import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.termination import get_termination
from pymoo.optimize import minimize
from config.global_config import NSGA_POP, NSGA_GEN, CRAB_STOCKING_DENSITY_RANGE, RICE_YIELD_RANGE

class RiceCrabMOP(ElementwiseProblem):
    def __init__(self):
        super().__init__(n_var=3, n_obj=4, xl=[RICE_YIELD_RANGE[0], CRAB_STOCKING_DENSITY_RANGE[0],20], xu=[RICE_YIELD_RANGE[1], CRAB_STOCKING_DENSITY_RANGE[1],80])
    def _evaluate(self, x, out, *args, **kwargs):
        rice_d, crab_d, fert = x
        rice_y = rice_d * (1 - 0.001 * crab_d * 0.1)
        crab_y = crab_d * (1 - 0.002 * fert * 0.05)
        cost = rice_d * 120 + crab_d * 80 + fert * 50
        risk = 0.01 * crab_d + 0.02 * fert
        out["F"] = [-rice_y, -crab_y, cost]

class RiceCrabNSGA2:
    def run_optimization(self):
        prob = RiceCrabMOP()
        algo = NSGA2(pop_size=NSGA_POP, n_offsprings=100, crossover=SBX(0.9,15), mutation=PM(20), eliminate_duplicates=True)
        term = get_termination("n_gen", NSGA_GEN)
        res = minimize(prob, algo, term, seed=42, verbose=False)
        return res.F
