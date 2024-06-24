# task 1 
all_reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

all_descriptors = ["good", "excellent", "bad", "Poor", "average"]

#loop to find and capitalize  the listed words 
for review_index in range(len(all_reviews)):
    review = all_reviews[review_index]
    for descriptor in all_descriptors: 
        review = review.replace(descriptor, descriptor.upper())
    all_reviews[review_index] = review 

# print the new reviews 
print(all_reviews)

# task 2 
# review and lists of postive  of words and define the lglobal variables  
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

all_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

positive_counter = 0
negative_counter = 0

# Function for counting positive and negative words
def count_word(review, word_list):
    count = 0
    for word in word_list:
        if word in review:
            count += 1
    return count

# Use function to count positive and negative words in reviews
for review in all_reviews:
    positive_counter += count_word(review, positive_words)
    negative_counter += count_word(review, negative_words)

# Print results
print("Number of positive words:", positive_counter)
print("Number of negative words:", negative_counter)

# task 3
# list reviews and global variables  
all_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
edited_reviews = []

# function to shorten and edit a review 
def edited_review(review):
    short_review = review[:30]+"..."
    return short_review 

# pass individual reviews through editing function  and print results
for review in all_reviews:
    edited_reviews.append(edited_review(review))

print(edited_reviews)

