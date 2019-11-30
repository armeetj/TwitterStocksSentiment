from textblob import TextBlob

print("enter string: ")
s = TextBlob(input())

print(s.sentiment)