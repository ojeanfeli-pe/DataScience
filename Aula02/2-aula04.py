from matplotlib import *
from pylab import *
from numpy import *
from scipy import *
from scipy import stats
#create a (discreet) random variable with poissionian distribuion
X = stats.poisson(3.5) #photon distribuion for a coherent state with n=3,5 photons

n = arange(0,15)
fig, axes = subplots(3,1, sharex=True)
#plot the probability mass function (PMF)
axes[0].step(n, X.pmf(n))
#plot the commulative distribution function (CDF)
axes[1].step(n, X.cdf(n))
#plot histogram of 1000 random realization of the stochastic variable x
axes[2].hist(X.rvs(size=1000))
plt.savefig("Grafico1.jpg", format="jpg", dpi=300)
show()

#create a (continous) random variable with normal distribution
Y = stats.norm()
x = linspace(-5,5,100)
fig, axes = subplots(3,1,sharex=True)
# Plot the probability distribution function (PDF)
axes[0].plot(x,Y.pdf(x))
#plot the commulative distributin function (CDF)
axes[1].plot(x,Y.cdf(x))
# Plot histogram of 1000 random realizations of the stochastic variable Y
axes[2].hist(Y.rvs(size=1000), bins=50)
plt.savefig("Grafico2.jpg", format="jpg", dpi=300)
show()

X.mean(), X.std(), X.var() # poission distribution
Y.mean(), Y.std(), Y.var() # normal distribution

t_statistic, p_value = stats.ttest_ind(X.rvs(size=1000), X.rvs(size=1000))
print('t_statistic =', t_statistic)
print('p-value =', p_value)