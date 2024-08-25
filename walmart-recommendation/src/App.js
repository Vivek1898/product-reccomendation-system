import React, { useState } from "react";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [userId, setUserId] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/recommend/`, {
        params: { user_id: userId },
      });
      setRecommendations(response.data.recommended_products);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="card">
        <div className="card-body">
          <h1 className="card-title">Walmart Product Recommendation System</h1>
          <div className="mb-3">
            <input
              type="text"
              className="form-control"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              placeholder="Enter User ID"
            />
          </div>
          <button className="btn btn-primary mb-3" onClick={fetchRecommendations}>
            Get Recommendations
          </button>
          <h2>Recommended Products:</h2>
          {recommendations.length > 0 ? (
            <ul className="list-group">
              {recommendations.map((product, index) => (
                <li key={index} className="list-group-item">
                  Product ID: {product}
                </li>
              ))}
            </ul>
          ) : (
            <p>No recommendations available.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
