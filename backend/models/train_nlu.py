# backend/models/train_nlu.py

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import json

# Sample intents data
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "goodbye", "farewell"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "add_event": ["add event", "schedule meeting", "set up a meeting", "create calendar event"],
    "send_email": ["send email", "compose email", "email someone"]
}

# Label encoding
labels = list(intents.keys())
training_sentences = [sentence for intent in intents for sentence in intents[intent]]
training_labels = [labels.index(intent) for intent in intents for _ in intents[intent]]

# Tokenizer and padding
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(training_sentences)
sequences = tokenizer.texts_to_sequences(training_sentences)
max_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

# Convert labels to numpy array
training_labels = np.array(training_labels)

# Model definition
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 16, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(len(labels), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training
model.fit(padded_sequences, training_labels, epochs=500)

# Save the model
model.save('models/nlu_model.h5')

# Save the tokenizer
tokenizer_json = tokenizer.to_json()
with open('models/tokenizer.json', 'w') as f:
    f.write(tokenizer_json)

print("Model and tokenizer saved successfully!")
