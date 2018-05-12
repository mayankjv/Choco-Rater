# Choco-Rater
This project analyses chocolate bars and also assigns a rating to an unknown chocolate bar.

Firstly, the data is collected using the web crawler module written in node.js
There are some reports that are to be created:

1. Top 10 sources and strains to produce chocolate bars (per type).
2. Top ingredients present in chocolate bar for 4 and 5 rating per type.
3. Text graph on which words describe the best bars and worst bars for a certain type (excluding common English words)
4. Which attributes are important for the rating to be high?

The Python scripts are written in order to prepare data for the above drill downs. The data so prepared is then imported into Tableau Desktop and is used to create interactive visualizations.

The Python script "chocolate.py" uses a python script to predict the rating of a chocolate that is not already known to the system. It uses Random Forest Regressor to do so.
