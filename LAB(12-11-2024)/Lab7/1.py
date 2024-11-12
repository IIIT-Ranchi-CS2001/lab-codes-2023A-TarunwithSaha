# Show party wise seat share for following results of the Assembly Elections 2023 in
# Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached ( show the percentage seat share on each wedge )
# Two pie charts as subplots on the same figure object
# As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
# Madhya Pradesh
# BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)
# Rajasthan
# INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)
import matplotlib.pyplot as plt

# Data for Madhya Pradesh
parties_mp = ['BJP', 'INC', 'BSP', 'Others']
seats_mp = [163, 66, 0, 1]

# Data for Rajasthan
parties_rj = ['INC', 'BJP', 'BSP', 'Others']
seats_rj = [69, 115, 2, 13]

# Calculate percentages for pie charts
total_seats_mp = sum(seats_mp)
total_seats_rj = sum(seats_rj)
percentages_mp = [seat / total_seats_mp * 100 for seat in seats_mp]
percentages_rj = [seat / total_seats_rj * 100 for seat in seats_rj]

# Colors for the charts
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8']

# --- Step 1: Pie Charts in Subplots ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Madhya Pradesh pie chart
explode_mp = [0.1 if seat == max(seats_mp) else 0 for seat in seats_mp]  # Detach the party with highest seats
ax1.pie(seats_mp, labels=parties_mp, autopct='%1.1f%%', startangle=90, explode=explode_mp, colors=colors)
ax1.set_title("Madhya Pradesh Assembly Elections 2023")

# Rajasthan pie chart
explode_rj = [0.1 if seat == max(seats_rj) else 0 for seat in seats_rj]  # Detach the party with highest seats
ax2.pie(seats_rj, labels=parties_rj, autopct='%1.1f%%', startangle=90, explode=explode_rj, colors=colors)
ax2.set_title("Rajasthan Assembly Elections 2023")

plt.tight_layout()
plt.show()

# --- Step 2: Bar Chart for Both States ---
fig, ax = plt.subplots(figsize=(10, 6))

# Bar positions for the two states
bar_width = 0.35
x_pos = range(len(parties_mp))  # Positions for Madhya Pradesh

# Bar plots
bars_mp = ax.bar(x_pos, seats_mp, width=bar_width, label='Madhya Pradesh', color=colors, alpha=0.7)
bars_rj = ax.bar([p + bar_width for p in x_pos], seats_rj, width=bar_width, label='Rajasthan', color=colors, alpha=0.4)

# Adding labels and title
ax.set_xlabel("Party")
ax.set_ylabel("Seats Won")
ax.set_title("Assembly Election Results 2023: Madhya Pradesh and Rajasthan")
ax.set_xticks([p + bar_width / 2 for p in x_pos])
ax.set_xticklabels(parties_mp)
ax.legend()

# Display the bar chart
plt.show()
