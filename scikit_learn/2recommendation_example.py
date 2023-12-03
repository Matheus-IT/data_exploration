import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample data (replace this with your actual data)
data = {
    "user_id": [1, 1, 2, 2, 3],
    "food_item": ["Pizza", "Burger", "Sushi", "Salad", "Pizza"],
}
df = pd.DataFrame(data)

# Convert food items into item profiles using TF-IDF
tfidf = TfidfVectorizer(stop_words="english")
item_profiles = tfidf.fit_transform(df["food_item"])

# Calculate similarity between items
cosine_sim = linear_kernel(item_profiles, item_profiles)


# Function to recommend items for a given user
def recommend_items(user_id, df, cosine_sim):
    user_orders = df[df["user_id"] == user_id]["food_item"].unique()
    recommended_items = []

    for item in user_orders:
        idx = df[df["food_item"] == item].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]  # Get top 5 similar items

        similar_items = [i for i, _ in sim_scores]
        recommended_items.extend(df.iloc[similar_items]["food_item"].unique())

    return list(set(recommended_items))


# Example usage: Recommend items for user with ID 1
user_id = 1
recommendations = recommend_items(user_id, df, cosine_sim)
print(f"Recommended items for user {user_id}: {recommendations}")
