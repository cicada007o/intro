import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sinplot(n=10):
  x=np.linspace(0,14,100)
  for i in range(1,n+1):
    plt.plot(x,np.sin(x+i*0.5)*(n+10-i))

sns.set()
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth":5})

sinplot()
plt.title('seaborn plots w aesthetic fns')
plt.show()
