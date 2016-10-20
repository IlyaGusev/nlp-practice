from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from utils.preprocess import text_to_wordlist, stem_sentence, get_sentence_tags


def bow(train_texts, test_texts, language='en', stem=False, tokenizer=text_to_wordlist, preprocessor=None,
        use_tfidf=False, max_features=None, bow_ngrams=(1,2)):
    print("BOW building...")

    if stem:
        print(" Stemming...")
        for i in range(len(train_texts)):
            train_texts[i] = stem_sentence(train_texts[i], language)
        for i in range(len(test_texts)):
            test_texts[i] = stem_sentence(test_texts[i], language)

    if use_tfidf:
        vectorizer = TfidfVectorizer(analyzer='word', ngram_range=bow_ngrams, tokenizer=tokenizer,
                                     preprocessor=preprocessor, max_features=max_features)
    else:
        vectorizer = CountVectorizer(analyzer='word', ngram_range=bow_ngrams, tokenizer=tokenizer,
                                     preprocessor=preprocessor, max_features=max_features)

    print(" Building BOW from texts...")
    data = train_texts+test_texts
    data = vectorizer.fit_transform(data)
    train_data = data[:len(train_texts)]
    test_data = data[len(train_texts):]
    return train_data, test_data