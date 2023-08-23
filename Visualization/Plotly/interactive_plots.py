#!/usr/bin/env python
import plotly.express as px
import numpy as np

def create_scatter_plot():
    x = np.random.rand(100)
    y = np.random.rand(100)
    
    fig = px.scatter(x=x, y=y, title='Interactive Scatter Plot')
    fig.update_xaxes(title_text='X Axis')
    fig.update_yaxes(title_text='Y Axis')
    fig.show()

def main():
    print("Creating an interactive scatter plot")
    create_scatter_plot()

if __name__ == "__main__":
    main()
