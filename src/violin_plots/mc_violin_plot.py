import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def format_reference(reference):
    return reference.replace("et al.", "ETAL").replace(" ", "\n").replace("ETAL", "et al.")


class _Custom_ViolinPlotter(sb.categorical._ViolinPlotter):

    def __init__(self, *args, **kwargs):
        super(_Custom_ViolinPlotter, self).__init__(*args, **kwargs)
        self.gray = '#333333'
        self.linewidth = 0.9


sb.categorical._ViolinPlotter = _Custom_ViolinPlotter

colors = sb.color_palette("hls", 23)[5], sb.color_palette("hls", 23)[15]

reference_order = ["James et al. (2021)", "Nagy et al. (2003)", "Nagy et al. (2006)", "Roth (2007)", "Singson et al. (2000)"]
hue_order = ["Target", "Foil"]
freq_column = "Average Frequency per 1000 Words"

counts_df = pd.read_csv("../../output/all/mc_counts.csv", header=0, sep=',')

reference_labels = [format_reference(reference) for reference in reference_order]

counts_df = counts_df.loc[counts_df.Type != "Potential Answer"].copy()  # we want only targets and foils
# clip frequencies above the 95th percentile, do nothing to low frequencies
counts_df[freq_column] = counts_df[freq_column].clip(
    lower=counts_df[freq_column].quantile(0), upper=counts_df[freq_column].quantile(0.95))


fig, ax = plt.subplots()
plt.rc('axes', titlesize=18)
sb.violinplot(data=counts_df,
              x="Reference",
              y=freq_column,
              hue="Type",
              hue_order=hue_order,
              order=reference_order,
              split=True,
              palette=colors)

plt.xticks(rotation=0, fontsize=12)
plt.yticks((0, 0.02, 0.04, 0.06, 0.08, 0.10), fontsize=12)

ax.set_ylim([0, 0.1])

ax.legend(handles=ax.legend_.legendHandles, labels=hue_order)
plt.legend(frameon=False, fontsize=12)

plt.ylabel('Frequency per 1000 Words', fontsize=14)
plt.xlabel(None, fontsize=14)
ax.set_xticklabels(reference_labels)

plt.savefig("../../output/violin_plots/mc_violin_plot.png", bbox_inches="tight", dpi=300)
