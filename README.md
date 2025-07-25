# 📊 FastAPI + Prometheus Metrics Demo
This project demonstrates how to expose metrics from a FastAPI API to Prometheus and visualize them using Grafana.

## 🚀 List of API Routes

- `/ping` – return "pong"
- `/slow` – Simulates a random slow response (to generate interesting metrics)
- `/metrics` – An endpoint that exposes metrics for Prometheus
- `/proxy-computers` - Returns a simulated Trend Micro computers log representing a cyber attack

 ## 🧪 Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [prometheus-fastapi-instrumentator](https://github.com/trallard/prometheus-fastapi-instrumentator)

## ▶️ Running the project

#### 1. Create a virtual environment using Python
```bash
python3.9 -m venv venv
```
#### 2. Activate the virtual environment
```bash
source venv/bin/activate
```
- Windows
```bash
venv\Scripts\activate
```

#### 3. Clone the repository outside the venv folder
```bash
git clone https://github.com/seu-usuario/fastapi-prometheus-grafana-demo.git
```
#### 4. Navigate to the project folder

```bash
cd fastapi-prometheus-grafana-demo
```
#### 5. Install the dependencies
```bash
pip install -r requirements.txt
```
#### 6. Create and switch to the develop branch
```bash
git checkout -b develop
```
#### 7. Run the API
```bash
uvicorn app.main:app --reload
```
### 🧠 Grafana

#### 1. Install Docker if you haven't already.

#### 2. In a separate terminal, run Docker:
```bash
    docker-compose up
```
#### 3. Access Grafana

 - Login: `admin`
 - Password: `admin`

#### 4. Add a Data Source:
- Click on `Add data source`
- Select "Prometheus"
- In the URL field, enter:
``` bash
     http://prometheus:9090
```
- Click "Save & Test"

#### 5. Create a Dashboard

- In the left menu, go to `Dashboards` > `New` > `New dashboard`
- Click `Add visualization`
- Select `Prometheus` as the data source
- Save Dashboard