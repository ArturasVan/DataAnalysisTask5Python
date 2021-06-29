import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',delimiter=',',float_precision='legacy')
  

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    

    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.scatter(x,y)
   
    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    x1 = list(range(1880, 2051))
    y1 = []

    for year in x1:
      y1.append(intercept + slope * year)
    plt.plot(x1, y1, 'r', label = 'Best Fit Line 1')

    # Create second line of best fit
    x2 = df[df['Year'] >= 2000] ['Year']
    y2 = df[df['Year'] >= 2000] ['CSIRO Adjusted Sea Level']
    
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)

    x3 = list(range(2000, 2051))
    y3 =[]
    for year in x3:
        y3.append(intercept2 + slope2 * year)

 
    
    
    plt.plot(x3, y3, 'r', label = 'Best Fit Line 2')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()