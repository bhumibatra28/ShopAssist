import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = pd.read_csv('data/data.csv')

# Clean data
data['text'] = data['title'] + ' ' + data['breadcrumbs']
data['text'] = data['text'].fillna('')

# Create vectorizer
vectorizer = CountVectorizer()
vectorizer.fit(data['text'])

# Get top similar products
def get_top_similar_products(query, num_recommendations=1):
    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, vectorizer.transform(data['text'])).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-num_recommendations-1:-1]
    return data.iloc[related_docs_indices].applymap(lambda x: float(x) if isinstance(x, float) else x)
