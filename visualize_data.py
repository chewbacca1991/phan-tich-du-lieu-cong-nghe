import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot(self):
        x = np.arange(len(self.data))
        plt.bar(x, self.data)
        plt.xticks(x, [f'Item {i}' for i in range(len(self.data))])
        plt.xlabel('Data')
        plt.ylabel('Value')
        plt.title('Technology Data Chart')
        plt.show()

if __name__ == '__main__':
    data = [10, 20, 15, 25]
    visualizer = DataVisualizer(data)
    visualizer.plot()