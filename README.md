# Sentiment Analysis Application

This project provides a sentiment analysis application that utilizes both VADER (Valence Aware Dictionary and sEntiment Reasoner) and RoBERTa (a robust transformer model) for analyzing the sentiment of text input. The application uses Gradio to create a user-friendly interface and is capable of combining results from both VADER and RoBERTa for enhanced sentiment analysis.

## Features

- **VADER Sentiment Analysis**: Based on a lexicon and rules, VADER performs sentiment analysis primarily for social media text, evaluating positive, negative, and neutral sentiment.
  
- **RoBERTa Sentiment Analysis**: RoBERTa is a transformer-based model pre-trained for sequence classification tasks. It classifies text into multiple sentiment categories (e.g., negative, neutral, positive).

- **Gradio Interface**: Provides a simple web interface for users to input text and get sentiment results in real time.

## Technologies Used

- **Python**: The backend is developed in Python 3.11, with various libraries and frameworks.
- **TensorFlow**: For deep learning models such as RoBERTa.
- **Transformers**: For loading the pre-trained RoBERTa model.
- **NLTK**: For performing VADER sentiment analysis.
- **Gradio**: For creating the interactive user interface.

## Installation

### Prerequisites

- Python 3.11 or higher
- A virtual environment (recommended)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd sentiment-analysis
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scripts\activate      # For Windows
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not provided, you can manually install the necessary libraries:
   ```bash
   pip install gradio tensorflow transformers nltk
   ```

5. Download the pre-trained models:
   - RoBERTa and VADER models will be automatically downloaded the first time you run the application.

## Usage

To start the sentiment analysis application, run the following command:

```bash
python app.py
```

This will start a local server and open the application in your browser.

### Input and Output

- **Input**: Type any text (e.g., a sentence or paragraph) into the input field.
- **Output**: The application will return a JSON object with sentiment scores from both VADER and RoBERTa models. The output will include sentiment scores such as:

  - VADER Sentiment: 
    - Positive sentiment score
    - Neutral sentiment score
    - Negative sentiment score
  - RoBERTa Sentiment: 
    - Scores for `roberta_neg`, `roberta_neu`, `roberta_pos` (or similar values, depending on the number of classes).

### Example Output

For an input such as:  
> "I absolutely love this product! It's amazing."

You will get an output similar to:

```json
{
  "vader_neg": 0.0,
  "vader_neu": 0.2,
  "vader_pos": 0.8,
  "roberta_neg": 0.01,
  "roberta_neu": 0.15,
  "roberta_pos": 0.84
}
```

## Contributing

We welcome contributions! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## Result of Execution

Below is an example of the execution result after running the application with a sample input:

### Sample Input:
> "I love working on this project! It's a great opportunity."

### Execution Output:

```json
{
  "vader_neg": 0.0,
  "vader_neu": 0.1,
  "vader_pos": 0.9,
  "roberta_neg": 0.02,
  "roberta_neu": 0.1,
  "roberta_pos": 0.88
}
```

### Explanation:
- **VADER Sentiment**:
  - Positive sentiment score (`vader_pos`): 0.9
  - Neutral sentiment score (`vader_neu`): 0.1
  - Negative sentiment score (`vader_neg`): 0.0

- **RoBERTa Sentiment**:
  - Negative sentiment score (`roberta_neg`): 0.02
  - Neutral sentiment score (`roberta_neu`): 0.1
  - Positive sentiment score (`roberta_pos`): 0.88
### App Result execution
![Screenshot 2024-11-27 150019](https://github.com/user-attachments/assets/9c36ab03-b3d2-40ae-8beb-530871f58dd2)

Here the feebback was positive and the app showes a hight score for the positive rate and 0 for the negative one

This shows that both models independently analyze the text and produce sentiment scores, which are then combined for a comprehensive result.

