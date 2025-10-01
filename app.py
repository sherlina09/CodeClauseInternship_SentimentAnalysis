import tkinter as tk
from textblob import TextBlob

def analyze():
    text = entry.get("1.0", tk.END).strip()
    if text:
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0.1:
            result.set("Positive 😀")
            result_label.config(fg="green")
        elif sentiment < -0.1:
            result.set("Negative 😞")
            result_label.config(fg="red")
        else:
            result.set("Neutral 😐")
            result_label.config(fg="blue")
    else:
        result.set("Please enter text!")
        result_label.config(fg="red")

# UI setup
root = tk.Tk()
root.title("Sentiment Analysis Tool")
root.geometry("400x250")

tk.Label(root, text="Enter text to analyze:", font=("Arial", 12), bg="white").pack(pady=5)
entry = tk.Text(root, height=5, width=40)
entry.pack(pady=10)

result = tk.StringVar()
tk.Button(root, text="Analyze Sentiment", fg="black",bg="orange", command=analyze).pack()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
