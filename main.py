from collect_data import DataCollector
from analyze_data import DataAnalyzer
from visualize_data import DataVisualizer

if __name__ == '__main__':
    # Bước 1: Thu thập dữ liệu
    urls = ['http://example.com/news1', 'http://example.com/news2']
    collector = DataCollector(urls)
    data = collector.fetch_data()

    # Bước 2: Phân tích dữ liệu
    analyzer = DataAnalyzer(data)
    labels = analyzer.analyze()

    # Bước 3: Trực quan hóa dữ liệu
    visualizer = DataVisualizer(labels)
    visualizer.plot()