import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

news = input("Enter news: ")

vec = vectorizer.transform([news])
result = model.predict(vec)

print("Result:", result[0])