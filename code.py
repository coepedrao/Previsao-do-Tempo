# O site OpenWeather foi usado na criação do código
import requests

# Key é gerada pelo site, ela varia de usuário para usuário
API_KEY = 'a99628d987b79253d47a5adfafac6138'
cidade = 'alegrete'
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'
# Url alterada no final, para que API mande as informações do tempo em PT-BR

requisição = requests.get(link)
requisição_dic = requisição.json()
descricao = requisição_dic['weather'][0] ['description']
temperatura = requisição_dic['main']['temp'] - 273.15
print(descricao, f'{temperatura} C')

