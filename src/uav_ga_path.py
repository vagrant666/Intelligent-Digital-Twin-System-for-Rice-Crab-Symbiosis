import numpy as np
from config.global_config import UAV_POP, UAV_GEN

class UAVPathPlanner:
    def __init__(self):
        self.points = self.gen_farm_points()
        self.n = len(self.points)

    def gen_farm_points(self):
        x = np.linspace(0,100,10)
        y = np.linspace(0,80,8)
        xx, yy = np.meshgrid(x,y)
        return np.vstack([xx.ravel(), yy.ravel()]).T

    def calc_dist(self, path):
        d = 0.0
        for i in range(len(path)-1):
            p1 = self.points[path[i]]
            p2 = self.points[path[i+1]]
            d += np.linalg.norm(p1-p2)
        return d

    def init_pop(self):
        pop = []
        for _ in range(UAV_POP):
            pop.append(np.random.permutation(self.n))
        return np.array(pop)

    def crossover(self, p1, p2):
        start, end = sorted(np.random.choice(self.n, 2, replace=False))
        child = np.zeros_like(p1)
        child[start:end] = p1[start:end]
        ptr = 0
        for gene in p2:
            if gene not in child[start:end]:
                while start <= ptr < end:
                    ptr += 1
                child[ptr] = gene
                ptr += 1
        return child

    def mutate(self, path):
        if np.random.rand() < 0.2:
            i, j = np.random.choice(self.n, 2, replace=False)
            path[i], path[j] = path[j], path[i]
        return path

    def gen_best_route(self):
        pop = self.init_pop()
        best_path = None
        best_d = float("inf")
        for _ in range(UAV_GEN):
            fit = [1/(self.calc_dist(p)+1e-6) for p in pop]
            best_idx = np.argmax(fit)
            cur_d = self.calc_dist(pop[best_idx])
            if cur_d < best_d:
                best_d = cur_d
                best_path = pop[best_idx].copy()
            new_pop = []
            while len(new_pop) < UAV_POP:
                idx1, idx2 = np.random.choice(UAV_POP, 2, replace=False)
                child1 = self.crossover(pop[idx1], pop[idx2])
                child2 = self.crossover(pop[idx2], pop[idx1])
                new_pop.append(self.mutate(child1))
                new_pop.append(self.mutate(child2))
            pop = np.array(new_pop[:UAV_POP])
        best_route = self.points[best_path]
        return best_route, best_d
