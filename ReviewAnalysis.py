# Task 1 Keyword Highlighter

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())
    print(review)

# Task 2 Sentiment Tally

def count_positive_negative_words(review, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for word in positive_words:
        if word in review:
            positive_count += 1

    for word in negative_words:
        if word in review:
            negative_count += 1
            
    return positive_count, negative_count

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for idx, review in enumerate(reviews):
    positive_count, negative_count = count_positive_negative_words(review, positive_words, negative_words)
    print(f"Review {idx+1}: Positive words: {positive_count}, Negative words: {negative_count}")

# Task 3 Summary Review
def create_summary(review):
    words = review.split()
    summary = ""
    char_count = 0

    for word in words:
        if char_count + len(word) <= 30:
            summary += word + " "
            char_count += len(word) + 1
        else:
            break

    # Remove the extra space at the end and add "…" if the summary is shorter than the review
    summary = summary.rstrip()
    if len(summary) < len(review):
        summary += "…"

    return summary

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for idx, review in enumerate(reviews):
    summary = create_summary(review)
    print(f"Review {idx+1} Summary: {summary}")
