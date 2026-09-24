"""
Flask + Prometheus metrics (Mission 16 - étape 1)

Objectif:
- Exposer une API Flask simple
- Exposer /metrics pour Prometheus

Métriques:
- Counter: nombre total de requêtes HTTP sur /
"""

from flask import Flask, Response, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Counter = compteur qui ne fait que monter (ex: nombre de requêtes)
HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["endpoint"]
)

@app.get("/")
def index():
    # On incrémente le compteur à chaque appel de /
    HTTP_REQUESTS_TOTAL.labels(endpoint="/").inc()
    return jsonify(message="Hello from Flask app with Prometheus metrics")

@app.get("/metrics")
def metrics():
    """
    Endpoint standard pour Prometheus.
    generate_latest() retourne toutes les métriques au format texte attendu.
    """
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    # Important: écouter sur 0.0.0.0 pour Docker (on s'y prépare)
    app.run(host="0.0.0.0", port=5000)
