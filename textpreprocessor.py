import re
import inflect
p = inflect.engine()
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    # text = re.sub(r'\d+', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Convert numbers to words
    words = text.split()
    processed_words = []
    for word in words:
        if word.isdigit():
            processed_words.append(p.number_to_words(word))
        else:
            processed_words.append(word)
    
    return ' '.join(processed_words)

main_text = "Hello World! This is a test. The number 123 should be converted to words."
processed_text = preprocess_text(main_text)
print(processed_text)