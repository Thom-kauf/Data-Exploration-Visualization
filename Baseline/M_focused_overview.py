labels = ['What Matters', 'Mobility', 'Mentation']

#hardcoded positions and dimensions to make it look nice
bar_width = 0.2
fig, ax = plt.subplots(figsize=(11, 6))
x = [0.39, 0.6, 0.81,
     1.19, 1.40,
     1.79, 2.0, 2.21, 2.42, 2.63]


# for each position, plot the thresholded score
for i in range(0, len(x)):
    
    if colors[i] == 'gray':
        bar = ax.bar(x[i],
            adjusted_baseline_totals[i], 
            width=bar_width, 
            label=associated_ms[i],
            color=colors[i],
            alpha=0.2)[0]
        

        plt.text(x[i], bar.get_height() - 0.55, 'Missing',  # "+ 0.5" for a little offset above the bar
                ha='center', va='bottom', color='black')


    else:
        ax.bar(x[i],
            adjusted_baseline_totals[i], 
            width=bar_width, 
            label=associated_ms[i],
            color=colors[i])
    

plt.title('Baseline Display', fontsize='xx-large')

plt.xticks([0.6, 1.3, 2.21], labels)
plt.tick_params(axis='x', labelsize=15, length=0)
plt.tick_params(axis='y', which='both', left=False, labelleft=False)

plt.savefig(SAVE_DIRECTORY + "baseline_overview.png", bbox_inches='tight')
plt.show()