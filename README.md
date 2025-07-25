# 📊 FastAPI + Prometheus Metrics Demo
Este projeto demonstra como expor métricas de uma API FastAPI para o Prometheus e visualizá-las com Grafana.

## 🚀 Rotas da API

- `/ping` – retorna "pong"
- `/slow` – simula uma resposta lenta aleatória (para gerar métricas interessantes)
- `/metrics` – endpoint de métricas para o Prometheus

 ## 🧪 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [prometheus-fastapi-instrumentator](https://github.com/trallard/prometheus-fastapi-instrumentator)

## ▶️ Como rodar

#### 1. Criar ambiente virtual usando o python
```bash
python3.9 -m venv venv
```
#### 2. Ative o ambiente virtual
- Linux
```bash
source venv/bin/activate
```
- Windows
```bash
venv\Scripts\activate
```

#### 3. Clone o repositório fora da pasta venv
```bash
git clone https://github.com/seu-usuario/fastapi-prometheus-grafana-demo.git
```
#### 4. Acesse a pasta do projeto
```bash
cd fastapi-prometheus-grafana-demo
```
#### 5. instale as dependências
```bash
pip install -r requirements.txt
```
#### 6. Crie e mude para a branch Develop
```bash
git checkout -b develop
```
#### 7. Rodar a API
```bash
uvicorn app.main:app --reload
```
