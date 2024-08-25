from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Load Walmart data
data = pd.read_csv('walmart.csv')  # Replace with your actual file path

user_item_matrix = data.pivot_table(index='User_ID', columns='Product_ID', values='Purchase', fill_value=0)

sparse_user_item = csr_matrix(user_item_matrix.values)

# Train ALS model
model = AlternatingLeastSquares(factors=20, regularization=0.1, iterations=50)
model.fit(sparse_user_item)

user_ids = list(user_item_matrix.index)
user_id_to_index = {user_id: index for index, user_id in enumerate(user_ids)}


product_ids = list(user_item_matrix.columns)
product_id_to_index = {product_id: index for index, product_id in enumerate(product_ids)}

def get_user_recommendations(user_id: int, num_recommendations: int = 10):
    if user_id not in user_id_to_index:
        return []

    user_index = user_id_to_index[user_id]

    recommended_indices, _ = model.recommend(user_index, sparse_user_item[user_index], N=num_recommendations)

    recommended_product_ids = [product_ids[index] for index in recommended_indices]

    return recommended_product_ids

@app.get("/recommend/")
def recommend_products(user_id: int = Query(None, description="ID of the user to get recommendations for")):
    if user_id is None:
        return {"recommended_products": []}

    recommended_products = get_user_recommendations(user_id)
    return {"recommended_products": recommended_products}
