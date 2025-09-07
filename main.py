from collect_data import DataCollector
from analyze_data import DataAnalyzer
from visualize_data import DataVisualizer
import logging


if __name__ == '__main__':
    # Step 1: Collect Data
    urls = ['http://example.com/news1', 'http://example.com/news2']
    data_collector = DataCollector(urls)
    try:
        collected_data = data_collector.fetch_data()
    except Exception as e:
        logging.error(f'Error collecting data: {e}')
        exit(1)

    # Step 2: Analyze Data
    data_analyzer = DataAnalyzer(collected_data)
    try:
        labels = data_analyzer.analyze()
    except Exception as e:
        logging.error(f'Error analyzing data: {e}')
        exit(1)

    # Step 3: Visualize Data
    data_visualizer = DataVisualizer(labels)
    data_visualizer.plot()