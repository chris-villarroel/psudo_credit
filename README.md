# Probar

```bash
curl -X POST -H "Content-Type: application/json" -d '{"Debt_Burden":0.5, "Employment_Years":5, "Income":60000, "Loan_Amount":200000, "Age":30}' http://127.0.0.1:5000/predict_post
```

```bash
curl "http://127.0.0.1:5000/predict_get?Debt_Burden=0.5&Employment_Years=5&Income=60000&Loan_Amount=200000&Age=30"
```

# Configuracion

```bash
source venv/bin/activate
pip freeze > requirements.txt
```

```bash
docker build -t psudo_credit .
docker run --rm -p 5000:5000 psudo_credit
```

```bash
docker login --username=pajar0p
docker tag psudo_credit pajar0p/psudo_credit:v3
docker push pajar0p/psudo_credit:v3
docker logout
docker run --rm -p 5005:5000 pajar0p/psudo_credit:v3
```

* Ir a digitalocean
* Seleccionar 4 USD mensual
* Por clave para facilitar las cosas xTNC@dM5r#qcQy
* hostname : encoders
* Crear en Encoders
* Se demora 1 minutos
* Ingresar por ssh al servir
* Installar 
* Configurar el networking




```bash
ssh root@146.190.151.189
```

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce
sudo systemctl enable docker
sudo systemctl start docker
sudo docker --version
sudo usermod -aG docker $USER
```


```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

```bash
mkdir psudo_credit
cd psudo_credit
mkdir nginxconf
mkdir main
mkdir certbot
mkdir certbot/webrootauth
```

```bash
cd /home/chris/Documents/Analytics/psudo_credit
scp _config/docker-compose.yaml root@146.190.151.189:/root/psudo_credit/main/
scp _config/nginx.conf root@146.190.151.189:/root/psudo_credit/nginxconf/
scp _config/nginx.conf2 root@146.190.151.189:/root/psudo_credit/nginxconf/

```


```bash
cd /root/psudo_credit/main
docker-compose up -d nginx_psudo_credit psudo_credit
docker-compose run --rm certbot_psudo_credit
docker-compose exec nginx_psudo_credit nginx -s reload
rm /root/psudo_credit/nginxconf/nginx.conf
mv /root/psudo_credit/nginxconf/nginx.conf2 /root/psudo_credit/nginxconf/nginx.conf
docker-compose exec nginx_psudo_credit nginx -s reload
```

docker-compose up -d --force-recreate nginx_psudo_credit psudo_credit


```bash
curl -X POST -H "Content-Type: application/json" -d '{"Debt_Burden":0.5, "Employment_Years":5, "Income":60000, "Loan_Amount":200000, "Age":30}' https://aidriven.cl/predict_post
```

```bash
curl "https://aidriven.cl/predict_get?Debt_Burden=0.5&Employment_Years=5&Income=60000&Loan_Amount=200000&Age=30"
```
