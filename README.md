# 📩 Spam Message Classifier (Naive Bayes)

A lightweight and easy-to-understand project that classifies text messages as **SPAM** or **HAM (not spam)** using Python and the **Naive Bayes** algorithm.  
Built for learning purposes, this project shows how simple text classification can be done using real message data.

---

## 🚀 What it does
- Reads a dataset (`s.csv`) containing messages and their labels (`ham` or `spam`)
- Transforms the text into numerical vectors using **CountVectorizer** (Bag of Words)
- Trains a **Multinomial Naive Bayes** model from scikit-learn
- Evaluates its accuracy
- Lets you test your own messages interactively in the console

---

## 📂 Dataset format
Your CSV file should have two columns:

| Column | Description |
|--------|--------------|
| `v1` | Label (`ham` or `spam`) |
| `v2` | Message text |

### Example (`s.csv`)
```csv
v1,v2
ham,Hey are we still meeting today?
spam,WIN a free iPhone by clicking this link!
ham,I'll call you when I get home.
spam,Congratulations! You have won $1000 cash. Claim now!
```

---

## ⚙️ Installation

Make sure you have **Python 3.x** installed.

1. Clone this repository or download the project files  
2. Open a terminal in the project folder  
3. Install the required libraries:
   ```bash
   pip install pandas scikit-learn
   ```

---

## ▶️ How to Run

Run the Python script:

```bash
python spam_classifier.py
```

If your dataset has a different name, update this line in the code:
```python
file = pd.read_csv("s.csv", encoding="latin-1")[['v1', 'v2']]
```

---

## 💬 Example interaction

```
Accuracy: 0.85000
Write a message (if not please write 'exit'): Hey, how are you?
Your message is: HAM
```

```
Write a message (if not please write 'exit'): Win money now! Click here!
Your message is: SPAM
```

---

## 🧠 Technologies used
- 🐍 **Python 3**
- 📦 **pandas** – for reading and processing CSV data
- 🔢 **scikit-learn** – for training and evaluating the Naive Bayes model  
  - `train_test_split`
  - `CountVectorizer`
  - `MultinomialNB`
  - `accuracy_score`

---

## 👨‍💻 About this project

This mini-project was created by **Rares Fagadeanu (@raresstefan14)**  
as a way to explore how **machine learning models** can classify text using simple NLP (Natural Language Processing) techniques.  

It’s a great starting point for anyone learning:
- how to prepare text data for ML,
- how Naive Bayes works,
- and how to test models interactively.

---

## 💡 Notes
- Works best with English text messages.
- Encoding is set to `"latin-1"` to prevent Unicode errors.
- You can expand the dataset to improve accuracy.

---

⭐ **If you find this useful, give it a star on GitHub!**  
Created with ❤️ by [raresstefan14](https://github.com/raresstefan14)
