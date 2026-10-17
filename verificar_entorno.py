import sys, numpy, pandas, matplotlib, seaborn, sklearn, statsmodels

print("Python", sys.version.split()[0])
for lib in (numpy, pandas, matplotlib, seaborn, sklearn, statsmodels):
    print(f"{lib.__name__:12} {lib.__version__}")
    