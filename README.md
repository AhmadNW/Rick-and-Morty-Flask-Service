# Rick and Morty Flask Service

This service queries the Rick and Morty API and returns all characters that:
- Species: Human
- Status: Alive
- Origin: Earth

The data is returned as JSON and also written to a CSV file.

---

## Build Docker Image

```bash
docker build -t flask-rickmorty .
