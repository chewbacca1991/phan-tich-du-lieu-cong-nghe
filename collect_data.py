import requests

class DataCollector:
    def __init__(self, source_urls):
        self.source_urls = source_urls

    def fetch_data(self):
        data = []
        for url in self.source_urls:
            response = requests.get(url)
            if response.status_code == 200:
                data.append(response.json())
            else:
                print(f'Failed to retrieve data from {url}')
        return data

if __name__ == '__main__':
    urls = ['http://example.com/news1', 'http://example.com/news2']
    collector = DataCollector(urls)
    data = collector.fetch_data()
    print(data)