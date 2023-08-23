#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def create_line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Simple Line Plot')
    plt.legend()
    plt.grid(True)
    plt.savefig('line_plot.png')
    plt.show()

def main():
    print("Creating a basic line plot")
    create_line_plot()
    print("Plot saved as line_plot.png")

if __name__ == "__main__":
    main()

