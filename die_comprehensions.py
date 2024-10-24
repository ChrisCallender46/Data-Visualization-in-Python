import plotly.express as px
from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = [die.roll() for roll_num in range(1000)]

# Analyze the results
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

print(frequencies)

# Visualize the results
title = "Results of Rolling One D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=range(1, die.num_sides + 1), y=frequencies, title=title, labels=labels)
fig.show()