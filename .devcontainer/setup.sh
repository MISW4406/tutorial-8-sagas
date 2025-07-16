#!/bin/bash

echo "[*] Installing Python dependencies..."
pip install -r requirements.txt
pip install -r sidecar-requirements.txt
pip install -r ui-requirements.txt
pip install -r cliente-requirements.txt

echo "[*] Building Docker images..."
docker build . -f aeroalpes.Dockerfile -t aeroalpes/flask
docker build . -f adaptador.Dockerfile -t aeroalpes/adaptador
docker build . -f notificacion.Dockerfile -t aeroalpes/notificacion
docker build . -f ui.Dockerfile -t aeroalpes/ui
docker build . -f cliente.Dockerfile -t aeroalpes/cliente
docker build . -f gds.Dockerfile -t aeroalpes/gds
docker build . -f pagos.Dockerfile -t aeroalpes/pagos

echo "[*] Pulling docker-compose dependencies..."
docker-compose pull

echo "[✓] Dev container setup completed successfully."