
# Sentienta - Dummy ML Model Deployment Demo

This is a minimal FastAPI app with a dummy ML model.  
It is containerized using Docker and tested through GitHub Actions.

## Run locally
docker build -t sentienta .
docker run -p 8080:8080 sentienta

## Test API
curl http://127.0.0.1:8080/
curl -H "Content-Type: application/json" -d '{"data": {"msg": "hello"}}' http://127.0.0.1:8080/predict

