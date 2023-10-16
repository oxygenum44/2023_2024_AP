import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 8, 16)
y1 = 4 + x*x
y2 = 1 + 2*x

# plot
fig, ax = plt.subplots()
fig.patch.set_facecolor('xkcd:light gray')

ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, (y1 + y2)/2, linewidth=2, label="f(x)")
plt.legend(loc=6, fontsize=20)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 24), yticks=np.arange(1, 24, 3))

ax.tick_params(axis="y",direction="in", pad=5, width=5)
ax.tick_params(axis="x",direction="in", pad=5, width=5)
ax.set_facecolor("#EDE8BA")
plt.title("Important chart with fontsize 24", fontsize=24)
ax.set_xlabel("This is xlabel with math symbol "+r'$\alpha > \beta \sum_{i=0}^\infty x_i$'+"\n")
ax.set_ylabel("This is ylabel")

ax.text(5.2, 6, 'boxed oblique text\nin position 5.2, 6', style='oblique',
        bbox={'facecolor': 'red', 'alpha': 0.7, 'pad': 10})

plt.grid(linestyle="--", color="red")
plt.subplots_adjust(bottom=0.15)
plt.show()


# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
x2 = 4 + np.random.normal(0, 2, 24)
y2 = 4 + np.random.normal(0, 2, len(x))
# size and color:
sizes = np.random.uniform(45, 180, len(x))
colors = np.random.uniform(45, 180, len(x))

# plot
fig, ax = plt.subplots(2)

ax[1].scatter(x, y, s=sizes, c=colors)

ax[1].set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

ax[0].scatter(x2, y2, s=sizes, c=colors)

ax[0].set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

ax[0].tick_params(labelbottom=False, labeltop=True, labelleft=True, labelright=True,
                     bottom=False, top=True, left=True, right=True)
ax[1].tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=True,
                     bottom=True, top=False, left=True, right=True)

ax[0].set_aspect('equal', adjustable='box')
ax[1].set_aspect('equal', adjustable='box')

plt.show()
