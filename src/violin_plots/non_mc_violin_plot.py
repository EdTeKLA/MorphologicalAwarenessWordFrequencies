import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.patches import ConnectionPatch
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def format_reference(reference):
    if reference == "Wolter & Pike (2015)":
        return "Wolter\n& Pike\n(2015)"
    elif reference == "McCutchen & Logan (2011)":
        return "McCutchen\n& Logan\n(2011)"
    elif reference == "Ku & Anderson (2003)":
        return "Ku &\nAnderson\n(2003)"
    elif reference == "Kieffer & Lesaux (2008)":
        return "Kieffer &\nLesaux\n(2008)"
    elif reference == "Kruk & Bergman (2013)":
        return "Kruk &\nBergman\n(2013)"
    return reference.replace("et al.", "ETAL").replace("et al", "ETAL").replace(" ", "\n").replace("ETAL", "et al.")


class _Custom_ViolinPlotter(sb.categorical._ViolinPlotter):
    def __init__(self, *args, **kwargs):
        super(_Custom_ViolinPlotter, self).__init__(*args, **kwargs)
        self.gray = '#333333'
        self.linewidth = 0.9


sb.categorical._ViolinPlotter = _Custom_ViolinPlotter
color = sb.color_palette("hls", 23)[5]
freq_column = "Average Frequency per 1000 Words"
y_limit = 0.5
fontsize = 8


counts_df = pd.read_csv("../../output/all/non_mc_counts.csv", header=0, sep=',')

targets_df = counts_df.loc[counts_df.Type == "Target"].copy()

targets_df[freq_column] = targets_df[freq_column].clip(
    lower=targets_df[freq_column].quantile(0), upper=targets_df[freq_column].quantile(0.95))

reference_order = list(targets_df.groupby(by=["Reference"])[freq_column].median().sort_values().index)

i = [2, 5, 14]
panel_one_references = reference_order[:i[0]]
panel_two_references = reference_order[i[0]:i[1]]
panel_three_references = reference_order[i[1]:i[2]]
panel_four_references = reference_order[i[2]:]

panel_one_df = targets_df.loc[targets_df.Reference.isin(panel_one_references)]
panel_two_df = targets_df.loc[targets_df.Reference.isin(panel_two_references)]
panel_three_df = targets_df.loc[targets_df.Reference.isin(panel_three_references)]
panel_four_df = targets_df.loc[targets_df.Reference.isin(panel_four_references)]



fig = plt.figure(figsize=(8.3, 10))

fig.text(0.06, 0.5, 'Frequency per 1000 Words', va='center', rotation='vertical', fontsize=12)
gs = fig.add_gridspec(3, i[1])
ax1 = fig.add_subplot(gs[0, :2])
plt.xticks(rotation=0, fontsize=fontsize)
plt.yticks(fontsize=fontsize)

axins1 = inset_axes(ax1, width='70%', height='65%', loc='center left', bbox_to_anchor=(0.2, 0.05, 1, 1),
                    bbox_transform=ax1.transAxes)
plt.xticks(rotation=0, fontsize=fontsize - 1)
plt.yticks(fontsize=fontsize - 1)
sb.violinplot(data=panel_one_df,
              x="Reference",
              y=freq_column,
              color=color,
              order=panel_one_references,
              ax=axins1)
axins1.set_xlim(-0.5, 1.5)
axins1.set_ylim(0, 0.012)
axins1.set(ylabel=None)
axins1.set(xlabel=None)
# remove x ticks from inset
plt.tick_params(
    axis='x',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False)
plt.yticks((0, 0.004, 0.008, 0.012))


con1 = ConnectionPatch(xyA=(0, 0), coordsA=ax1.transData,
                       xyB=(0, 0), coordsB=axins1.transData,
                       arrowstyle='->', zorder=1)
con2 = ConnectionPatch(xyA=(1, 0), coordsA=ax1.transData,
                       xyB=(1, 0), coordsB=axins1.transData,
                       arrowstyle='->', zorder=1)


sb.violinplot(data=panel_one_df,
              x="Reference",
              y=freq_column,
              color=color,
              order=panel_one_references,
              ax=ax1)
ax1.set_ylim([0, y_limit])

fig.add_artist(con1)
fig.add_artist(con2)
panel_one_labels = [format_reference(reference) for reference in panel_one_references]
ax1.set_xticklabels(panel_one_labels)
ax1.set(ylabel=None)
ax1.set(xlabel=None)
ax1.spines[['right']].set_visible(False)

ax2 = fig.add_subplot(gs[0, 2:])
plt.xticks(rotation=0, fontsize=fontsize)
plt.yticks(fontsize=fontsize)
sb.violinplot(data=panel_two_df,
              x="Reference",
              y=freq_column,
              color=color,
              order=panel_two_references)

ax2.set_ylim([0, y_limit])
panel_two_labels = [format_reference(reference) for reference in panel_two_references]
ax2.set_xticklabels(panel_two_labels)
plt.yticks(visible=False)
ax2.set(ylabel=None)
ax2.set(xlabel=None)
ax2.spines[['left']].set_visible(False)
ax2.tick_params(
    axis='y',
    which='both',
    left=False,
    right=False,
    labelleft=False)

ax3 = fig.add_subplot(gs[1, :])
plt.xticks(rotation=0, fontsize=fontsize)
plt.yticks(fontsize=fontsize)
sb.violinplot(data=panel_three_df,
              x="Reference",
              y=freq_column,
              color=color,
              order=panel_three_references)

ax3.set_ylim([0, y_limit])
panel_three_labels = [format_reference(reference) for reference in panel_three_references]
ax3.set_xticklabels(panel_three_labels)
ax3.set(ylabel=None)
ax3.set(xlabel=None)

ax4 = fig.add_subplot(gs[2, :])
plt.xticks(rotation=0, fontsize=fontsize)
plt.yticks(fontsize=fontsize)

sb.violinplot(data=panel_four_df,
              x="Reference",
              y=freq_column,
              color=color,
              order=panel_four_references)
ax4.set_ylim([0, y_limit])
panel_four_labels = [format_reference(reference) for reference in panel_four_references]
ax4.set_xticklabels(panel_four_labels)
ax4.set(ylabel=None)
ax4.set(xlabel=None)

fig.subplots_adjust(hspace=0.27)
fig.subplots_adjust(wspace=0.01)

plt.savefig("../../output/violin_plots/non_MC_violin_plot.png", dpi=300, bbox_inches="tight")
