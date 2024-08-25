
# Walmart Product Recommendation System

This project implements a product recommendation system for Walmart customers using the Alternating Least Squares (ALS) model from the `implicit` library. The system provides personalized product recommendations based on historical purchase data.

## Features

- **Advanced Recommendations**: Utilizes ALS, a collaborative filtering technique to generate precise and personalized product recommendations.
- **FastAPI Backend**: A lightweight backend API built with FastAPI to handle recommendation requests.
- **Efficient Computation**: Uses sparse matrices to efficiently handle large-scale user-item interaction data.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/walmart-recommendation-system.git
   cd walmart-recommendation-system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your Data**:
   - Ensure you have a CSV file named `walmart.csv` in the root directory of the project with the appropriate schema.

2. **Run the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```
   - This will start the server on `http://localhost:8000`.

3. **Access the API**:
   - You can test the API endpoint by navigating to `http://localhost:8000/docs` in your web browser and using the interactive Swagger UI.

### Example Request

To get product recommendations for a user, send a GET request to the `/recommend/` endpoint with a `user_id` query parameter:

```bash
curl -X 'GET'   'http://localhost:8000/recommend/?user_id=12345'   -H 'accept: application/json'
```

### Requirements

- **Python Libraries**:
  - `fastapi`
  - `pandas`
  - `scipy`
  - `implicit`

To install all required libraries, ensure you have the `requirements.txt` file with the following contents:

```txt
fastapi
pandas
scipy
implicit
uvicorn
```

### License

This project is licensed under the MIT License - see the LICENSE file for details.
