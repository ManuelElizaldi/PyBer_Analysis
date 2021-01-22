#%%
import pandas as pd
import numpy.random as rnd
import matplotlib.pyplot as plt
# %%
mean = 0
standrad_dev = 1
sample_size = 1000
# %%
normal_sample = rnd.normal(mean,standrad_dev,sample_size)
# %%
# ndarray = series
normal_sample[0:10]
# %%
normal_df = pd.DataFrame(normal_sample)
# %%
normal_df.plot()
# %%
normal_df.hist()
# %%
number_of_trails = 100
prob_suc = 0.67
binomial_sample = rnd.binomial(number_of_trails,0.67,sample_size)
# %%
binomial_df = pd.DataFrame(binomial_sample)
# %%
binomial_df.hist()
# %%
log_normal_df = pd.DataFrame(rnd.lognormal(mean,standrad_dev,sample_size))
# %%
log_normal_df.plot()
# %%
log_normal_df.hist()
# %%
from stats_module import StatsSampler
# %%
