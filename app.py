import gradio as gr
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the saved model (Assuming 'model.h5' is a Keras model saved in .h5 format)
roberta_tokenizer = AutoTokenizer.from_pretrained('roberta-base')
roberta_model = TFAutoModelForSequenceClassification.from_pretrained('roberta-base')

# If you saved the Vader model separately, load it directly
sia = SentimentIntensityAnalyzer()

# Function to process the user input and return sentiment
def get_sentiment(text):
    # VADER sentiment analysis
    vader_result = sia.polarity_scores(text)
    vader_result_rename = {f"vader_{key}": value for key, value in vader_result.items()}
    
    # RoBERTa sentiment analysis
    encoded_text = roberta_tokenizer(text, return_tensors='tf')
    output = roberta_model(encoded_text)

    # Ensure logits have the expected shape and are not empty
    logits = output.logits.numpy()
    if logits.shape[0] > 0:  # Ensure there is at least one entry in the batch
        scores = tf.nn.softmax(logits[0])  # Apply softmax to get probabilities
    else:
        raise ValueError("Model output logits are empty or invalid.")
    
    # Check the number of classes in logits (e.g., 2 for binary classification or 3 for multi-class)
    num_classes = logits.shape[-1]  # Get the number of output classes
    if num_classes == 3:
        roberta_result = {
            'roberta_neg': scores[0],
            'roberta_neu': scores[1],
            'roberta_pos': scores[2]
        }
    elif num_classes == 2:
        roberta_result = {
            'roberta_neg': scores[0],
            'roberta_pos': scores[1]
        }
    else:
        raise ValueError(f"Unexpected number of classes in logits: {num_classes}")

    # Combine results from VADER and RoBERTa
    combined_result = {**vader_result_rename, **roberta_result}
    
    return combined_result

# Gradio Interface
iface = gr.Interface(fn=get_sentiment, inputs="text", outputs="json")
iface.launch()