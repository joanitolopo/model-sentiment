from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
from string import punctuation

def predict(tweet, process_tweet, model):
    
    # prosses word
    word_l = process_tweet(tweet)
    
    result = model.predict([tweet])
    
    if result == [1]:
        print(f"Kalimat '{tweet}' adalah positif")
    elif result == [0]:
        print(f"Kalimat '{tweet}' adalah negatif")
        
        
def process_tweet(tweet):
    
    # kumpulan stemming
    factory_stem = StemmerFactory()
    stemmer = factory_stem.create_stemmer()

    # kumpulan stopwords
    factory_stopwords = StopWordRemoverFactory()
    stopword = factory_stopwords.get_stop_words() + stopwords.words('indonesian')
  
    # menghapus kata-kata yang tidak penting seperti @, #
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    
    # tokenizer word
    tweet_tokens = word_tokenize(tweet)
    
    # membersihkan word
    tweets_clean = [stemmer.stem(word) for word in tweet_tokens if (word not in stopword and word not in punctuation)]

    return ' '.join(tweets_clean)