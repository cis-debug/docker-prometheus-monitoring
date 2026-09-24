# 📊 Docker Prometheus Monitoring

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker\&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Multi--Container-2496ED?logo=docker\&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus\&logoColor=white)

## 📌 Description

Projet de **monitoring d'une application Flask avec Prometheus**, entièrement exécuté avec Docker Compose.

L'application expose une API Flask ainsi qu'un endpoint `/metrics`. Prometheus récupère automatiquement ces métriques afin de suivre l'activité de l'application.

Ce projet permet de découvrir les bases de l'**observabilité** et du **monitoring applicatif**.

---

## 🎯 Objectifs

Cette mission permet de pratiquer :

* 📊 Monitoring
* 🐍 Python / Flask
* 🐳 Docker
* 🧩 Docker Compose
* 📈 Prometheus
* 📡 Collecte de métriques
* 🔎 Vérification de l'état d'un service

---

## 🏗️ Architecture

```text
                 🌍 Client
                    │
                    ▼
            ┌───────────────┐
            │   Flask API   │
            │     :5000     │
            └───────┬───────┘
                    │
                    │ /metrics
                    ▼
            ┌───────────────┐
            │  Prometheus   │
            │     :9090     │
            └───────────────┘
```

Prometheus interroge régulièrement l'API Flask afin de récupérer les métriques exposées par `/metrics`.

---

## 📁 Structure du projet

```text
docker-prometheus-monitoring/
│
├── app/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── prometheus/
│   └── prometheus.yml
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 🌐 API Flask

L'application expose plusieurs endpoints :

| Méthode | Endpoint   | Fonction                              |
| ------- | ---------- | ------------------------------------- |
| `GET`   | `/`        | Vérifier que l'application fonctionne |
| `GET`   | `/health`  | Vérifier l'état de santé              |
| `GET`   | `/info`    | Afficher les informations du projet   |
| `GET`   | `/metrics` | Exposer les métriques Prometheus      |

### Tester l'application

```bash
curl http://localhost:5000/
```

```bash
curl http://localhost:5000/health
```

```bash
curl http://localhost:5000/info
```

---

## 📊 Endpoint `/metrics`

L'endpoint :

```text
/metrics
```

permet à Prometheus de récupérer les données de monitoring.

Pour l'afficher :

```bash
curl http://localhost:5000/metrics
```

Une métrique importante du projet est :

```text
app_requests_total
```

Elle permet de compter le nombre de requêtes reçues par l'application.

Exemple :

```text
app_requests_total 5.0
```

Le compteur augmente lorsque de nouvelles requêtes sont envoyées à l'API.

---

## 🐳 Docker Compose

Le projet utilise deux services :

```text
app
prometheus
```

### Flask

* Python 3.12
* Flask
* port `5000`

### Prometheus

* Prometheus
* port `9090`

Les deux conteneurs communiquent via le réseau Docker Compose.

---

## ⚙️ Configuration Prometheus

La configuration se trouve dans :

```text
prometheus/prometheus.yml
```

Prometheus interroge l'application toutes les **5 secondes** :

```yaml
global:
  scrape_interval: 5s
```

La cible configurée est :

```yaml
targets:
  - "app:5000"
```

Le nom `app` correspond au service Flask défini dans `docker-compose.yml`.

---

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/cis-debug/docker-prometheus-monitoring.git
cd docker-prometheus-monitoring
```

### 2. Construire les images

```bash
docker compose build
```

### 3. Démarrer les services

```bash
docker compose up -d
```

### 4. Vérifier les conteneurs

```bash
docker compose ps
```

Les deux services doivent être en fonctionnement :

```text
monitoring-app
prometheus
```

---

## 📈 Accéder à Prometheus

Ouvrir dans le navigateur :

```text
http://localhost:9090
```

Dans l'interface Prometheus, rechercher :

```text
app_requests_total
```

Puis exécuter la requête.

---

## 🟢 Vérifier la cible

Dans Prometheus :

```text
Status → Target health
```

La cible :

```text
flask-api
```

doit apparaître avec l'état :

```text
UP
```

Cela signifie que Prometheus récupère correctement les métriques de l'application Flask.

---

## 🧪 Tester les métriques

Effectuer plusieurs requêtes :

```bash
curl http://localhost:5000/
```

```bash
curl http://localhost:5000/health
```

```bash
curl http://localhost:5000/info
```

Puis rechercher dans Prometheus :

```text
app_requests_total
```

La valeur du compteur doit augmenter.

---

## 🔧 Commandes utiles

### Voir les conteneurs

```bash
docker compose ps
```

### Voir les logs Flask

```bash
docker compose logs app
```

### Voir les logs Prometheus

```bash
docker compose logs prometheus
```

### Voir toutes les métriques

```bash
curl http://localhost:5000/metrics
```

### Arrêter les services

```bash
docker compose down
```

### Reconstruire les conteneurs

```bash
docker compose up -d --build
```

---

## 🛠️ Technologies utilisées

* 🐍 Python 3.12
* 🌐 Flask
* 📊 Prometheus
* 🐳 Docker
* 🧩 Docker Compose
* 🐧 Linux / WSL
* 🔧 Git / GitHub

---

## 🔐 Bonnes pratiques

Dans un environnement réel, le monitoring pourrait être amélioré avec :

* authentification de l'accès à Prometheus
* stockage persistant des métriques
* limitation des métriques exposées
* alertes automatiques
* dashboards Grafana
* monitoring de plusieurs applications
* surveillance des ressources Docker

---

## 🚀 Améliorations possibles

Ce projet peut évoluer vers une architecture de monitoring plus complète :

```text
Flask
  │
  ▼
Prometheus
  │
  ▼
Grafana
  │
  ├── CPU
  ├── Mémoire
  ├── Requêtes HTTP
  ├── Erreurs
  └── Temps de réponse
```

Les prochaines améliorations possibles sont notamment :

* ajouter **Grafana**
* créer un dashboard personnalisé
* ajouter des alertes Prometheus
* surveiller les conteneurs Docker
* ajouter des métriques CPU et mémoire
* intégrer le monitoring dans une pipeline CI/CD

---

## 👩‍💻 Auteur

**Cisse Ndeye**

GitHub :
https://github.com/cis-debug
