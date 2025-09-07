import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot(self):
        indices = np.arange(len(self.data))
        plt.bar(indices, self.data)
        plt.xticks(indices, [f'Item {i + 1}' for i in range(len(self.data))])  # Changed to start from 1
        plt.xlabel('Data Points')  # Changed xlabel for clarity
        plt.ylabel('Values')  # Changed ylabel for clarity
        plt.title('Data Visualization of Technology Metrics')  # Updated title for clarity
        plt.show()

if __name__ == '__main__':
    data = [10, 20, 15, 25]
    visualizer = DataVisualizer(data)
    visualizer.plot()