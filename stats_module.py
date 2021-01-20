#%%
import pandas as pd
import numpy.random as rnd
import matplotlib.pyplot as plt
# %%
class StatsSampler:

    def __init__(
        self, mean = 0,
        stnd = 1,
        sample_size=1000
        ):
        self.mean = mean
        self.stnd = stnd
        self.sample_size = sample_size
        self.number_of_trails = number_of_trails

    def normal_sample(self):
        normal_sample = rnd.normal(self.mean, self.stnd, self.sample_size)
        normal_df = pd.DataFrame(normal_sample)
        normal_df.hist()
        return normal_df

    def binomial_sample(self):
        binomial_sample = rnd.binomial(number_of_trails,0.67,sample_size)
        normal_df = pd.DataFrame(normal_sample)
        normal_df.hist()
        return binomial_df

    def lognormal_sample(self):
        lognormal_sample = rnd.lognormal(self.mean, self.stnd, self.sample_size)
        lognormal_df = pd.DataFrame(lognormal_sample)
        lognormal_df.hist()
        return lognormal_df

# %%
