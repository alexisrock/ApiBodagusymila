@echo off
cd C:\Users\invitador\Documents\pruebaApi
uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile=C:\Users\invitador\Documents\CertificadoSSl\key.pem --ssl-certfile=C:\Users\invitador\Documents\CertificadoSSl\cert.pem
