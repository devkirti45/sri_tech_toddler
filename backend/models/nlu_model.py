import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import numpy as np
import json

# Load the trained model and tokenizer
model = tf.keras.models.load_model('models/nlu_model.h5')

# Load the tokenizer
with open('models/tokenizer.json', 'r', encoding='utf-8') as f:
    tokenizer_json = f.read()

# Directly pass the JSON string to tokenizer_from_json
tokenizer = tokenizer_from_json(tokenizer_json)

max_length = 20  # Must match the training max_length

# Labels for intents
labels = ['greeting', 'goodbye', 'thanks', 'add_event', 'send_email']

def classify_intent(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_length, padding='post')
    prediction = model.predict(padded)
    intent_idx = np.argmax(prediction)
    intent = labels[intent_idx]

    # Extract skill name and parameters based on intent
    if intent == 'add_event':
        skill_name = 'calendar'
        params = {
            'event_name': 'Meeting with team',  # Placeholder, should extract from text
            'start_time': '2024-09-05T10:00:00',  # Placeholder
            'duration': 1
        }
    elif intent == 'send_email':
        skill_name = 'email'
        params = {
            'to_email': 'recipient@example.com',  # Placeholder
            'subject': 'Hello',
            'message': 'This is a test email.'
        }
    else:
        skill_name = None
        params = {}
    
    return intent, skill_name, params






