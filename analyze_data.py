import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(self.data)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X)
        return kmeans.labels_

if __name__ == '__main__':
    data = ['Dữ liệu công nghệ 1', 'Dữ liệu công nghệ 2']
    analyzer = DataAnalyzer(data)
    labels = analyzer.analyze()
    print(labels)