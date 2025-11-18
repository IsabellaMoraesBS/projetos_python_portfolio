import requests

url = "https://api.github.com/users/IsabellaMoraesBS"
response = requests.get(url)
dados = response.json()

print("Nome:", dados.get("name"))
print("Repositórios públicos:", dados.get("public_repos"))
print("Seguidores:", dados.get("followers"))
