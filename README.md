# NetSieveX.io — Backend API

Flask REST API for NetSieveX.io, an AI-powered IoT network intrusion 
detection system. Provides ML-based attack classification with SHAP 
explainability, deployed on Azure App Service.

## Related Repositories

- **Frontend:** [WebSait](https://github.com/ingenriquecardosoalfonso/WebSait)
- **ML Models:** [Classify-CyberThreat](https://github.com/barbaraalfaro17/Classify-CyberThreat)

## Tech Stack

- Python 3.11
- Flask + Flasgger (Swagger UI)
- scikit-learn
- SHAP
- SQLAlchemy
- Docker
- Azure App Service

## Project Structure
├── app.py              # App entry point
├── config.py           # Configuration
├── routes/             # API route definitions
├── services/           # Business logic (ML inference, SHAP)
├── repositories/       # Database access layer
├── dtos/               # Data Transfer Objects
├── predictive/         # Trained .pkl models and data
├── utils/              # Helper functions
├── Dockerfile
└── requirements.txt

## Getting Started

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

API docs available at `http://localhost:5000/apidocs/`

## Key Endpoint
POST /api/ml/analyze
Accepts a JSON payload with 31 network flow features and returns:
- Predicted attack class
- Confidence score
- Class probabilities
- SHAP feature importance (top 5 features)
- Risk level (LOW / MEDIUM / HIGH / CRITICAL)

## ML Models

Three pre-trained models are loaded at startup:

| Model | Accuracy |
|---|---|
| Random Forest | 99.37% |
| Decision Tree | 99.19% |
| KNN | 98.91% |

Trained on the RT-IoT2022 dataset (UCI Machine Learning Repository).

## Team

- Ludwig Cardoso
- Barbara Alfaro
- Nehal Gadhavi

SAIT — Integrated Artificial Intelligence Post-Diploma Certificate, 2026
