import random

class NormalDistributionSimulator:
    def __init__(self, seed, mean, standard_deviation):
        self._random = random.Random(seed)
        self._mean = mean
        self._standard_deviation = abs(standard_deviation)
        self._step_size_factor = self._standard_deviation / 10
        self._value = self._mean - self._random.random()
        self._factors = [-1, 1]

    def next_value(self):
        value_change = self._random.random() * self._step_size_factor
        factor = self._factors[self._decide_factor()]
        self._value += value_change * factor
        return self._value
    
    def _decide_factor(self):
        distance = abs(self._value - self._mean)
        continue_direction = 1 if self._value > self._mean else 0
        change_direction = 0 if self._value > self._mean else 1
        chance = (self._standard_deviation / 2) - (distance / 50)
        random_value = self._random.random() * self._standard_deviation
        return continue_direction if random_value < chance else change_direction