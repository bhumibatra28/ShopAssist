import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from joblib import load, dump
import nltk

# Downloading contents of NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Load data
data = pd.read_json('data/data.json')

# Extract feature text from feature column
feature_text = []
for features in data['features']:
    feature_list = []
    for feature in features:
        for key, value in feature.items():
            feature_list.append(value)
    feature_text.append(' '.join(feature_list))

# Clean data

data['text'] = data['title'] + ' ' + data['breadcrumbs'] + ' ' + data['price'] + \
    ' ' + data['brand'] + ' ' + \
    data['product_details'] + pd.Series(feature_text)
data['text'] = data['text'].fillna('')
data['text'] = data['text'].apply(lambda x: ' '.join(
    [word.lower() for word in word_tokenize(x) if word.isalpha()]))
stop_words = set(stopwords.words('english'))
data['text'] = data['text'].apply(lambda x: ' '.join(
    [word for word in word_tokenize(x) if not word in stop_words]))

# Create vectorizer
vectorizer = TfidfVectorizer().fit(data['text'])

'''
print('dump startedf for v2')
dump(vectorizer,'recommenderV2.joblib')
print('dump completed for v2')
'''

vectorizer = load('mlModels/recommenderV2.joblib')

def getTopSimilarProducts(query, num_recommendations=5):
    query = ' '.join([word.lower()
                     for word in word_tokenize(query) if word.isalpha()])
    query = ' '.join([word for word in word_tokenize(
        query) if not word in stop_words])
    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(
        query_vector, vectorizer.transform(data['text'])).flatten()
    related_docs_indices = cosine_similarities.argsort()[
        :-num_recommendations-1:-1]
    return data.iloc[related_docs_indices].applymap(lambda x: float(x) if isinstance(x, float) else x)
