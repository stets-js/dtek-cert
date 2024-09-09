# CertificateBot
Create GoITeens certificates
Працює з aiogram=2.23

# Підключіться до Droplet через SSH:
ssh root@your_droplet_ip

# Налаштування середовища
Оновіть систему:
sudo apt update && sudo apt upgrade -y

# Встановіть Python 3.11 (якщо не встановлений):
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev

# Встановіть pip для Python 3.11:
curl https://bootstrap.pypa.io/get-pip.py | python3.11

# Створіть віртуальне середовище та активуйте його:
python3.11 -m venv myenv
source myenv/bin/activate