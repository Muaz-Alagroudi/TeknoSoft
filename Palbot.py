
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class Palbot:
    def __init__(self):
        self.rules = []
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def add_rule(self, pattern, response):
        self.rules.append((pattern, response))

    def preprocess_input(self, user_input):
        # Tokenize the input
        tokens = word_tokenize(user_input)
        # Convert to lowercase
        tokens = [token.lower() for token in tokens]
        # Remove stop words and non-alphabetic tokens
        filtered_tokens = [token for token in tokens if token.isalpha()]
        # lemmantize the tokens
        lemmed_tokens = [self.lemmatizer.lemmatize(token, pos='v') for token in filtered_tokens]
        return ' '.join(lemmed_tokens)

    def get_response(self, user_input):
        processed_input = self.preprocess_input(user_input.lower())
        print('processed : ', processed_input)
        for pattern, response in self.rules:
            if pattern.search(processed_input):
                return response
        return "I'm sorry, I don't understand that."

