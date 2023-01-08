# loteria

## 📁 Acesso ao projeto

**É possível baixar ou acessar o código fonte do projeto no [Link](https://github.com/AlanNegalho/loteria.git) ou clone o repositório**
```python
git clone https://github.com/AlanNegalho/loteria.git
```

## 🛠️ Abrir e rodar o projeto

Após acessar o código fonte do projeto faça o download através do git clone ou no formato zip. Podemos agora iniciamos a instalação da aplicação em nossa máquina. Lembrando que utilizaremos o ambiente virtual para criação do projeto.

## Upgrade necessários

Acesse a pasta diretoria da aplicação
```python
cd loteria
```
Atualizar o sistema caso esteja no Linux

```python
sudo apt update 
```


```python
sudo apt -y upgrade
```

Instalar o pip3


```python
sudo apt install python3-pip
```

Instalar ferramentas adicionais


```python
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

Instalando o env e virtualenv


```python
sudo apt install -y python3-venv
```


```python
sudo apt install python3-virtualenv
```
Instalando no Windows

```python
pip install virtualenv
```
Instalando no MacOS

```python
sudo pip uninstall virtualenv

sudo -H pip install virtualenv
```

## Criando o ambiente virtual
Criando seu ambiente virtual. Vamos chamá-lo venv

No Linux
```python
python3 -m venv venv
```

Criando o seu ambiente virtual no Windows 

```python
python -m venv venv
```

Criando seu ambiente virtual no MacOS

```python
virtualenv -p python3 <desired-path>


virtualenv -p python3 env

```

Ative o ambiente virtual 

No Windows
```python
venv\Scripts\activate.bat
```
No linux
```python
. venv/bin/activate
```
Para desativar o ambiente virtual, na pasta


```python
deactivate 
```

```python
quit()
```

## Bibliotecas utilizadas no desenvolvimento da aplicação
- Django==4.1.4

1.   https://pypi.org/project/Django/

Instale todas as bibliotecas acima através do requirements.txt arquivo localizado na pasta da aplicação.

```python
pip install -r requirements.txt
```
Realize  as migrations e o migrate:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
Após realizar as migrações, crie um super usuário pra realizar acesso ao admin do Django. Adicione o nome do usuário logo após o comando.
```python
python manage.py createsuperuser
```
Inicie o servidor:
```python
python manage.py runserver
```
Acesse o link da aplicação:
```python
http://127.0.0.1:8000/
```


⌨️ com ❤️ por [Alan Negalho](https://github.com/AlanNegalho) 😊
