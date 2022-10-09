# Bot Twitter
 Bot de Twitter criado para dar "RTs" em alguma palavra específica, nesse caso "couve"

## Bibliotecas necessárias
dotenv, tweepy
> pip install dotenv tweepy

## Como configurar as variáveis de ambiente
### Criar uma conta de Developer no portal do Twitter
> [Portal de desenvolvedor do Twitter](https://developer.twitter.com/en/portal/ "Twitter Developer Portal")

Clicar em Create Project na Dashboard
![Create Project](https://user-images.githubusercontent.com/93171892/194770277-851313ed-aada-40ae-8709-e0470be605af.png)

Preencher a descrição do projeto e selecionar o Use Case como "Making a Bot", depois selecionar App Environment como Development.
Logo após, já com seu aplicativo já selecionado, clique em set up, na aba "User authentication settings".
Selecionar a opção "Read and write and Direct message" ou "Read and write" em App Permissions, e "Web App, Automated App or Bot" em Type of App.

Em App Info colocar o campo "Callback URI / Redirect URL" como "https://localhost/" e o campo "Website URL" como qualquer website fictício, já que nosso bot não terá nenhum.

Depois disso voltar no aplicativo na Dashboard e clicar em regenerate na API Key and Secret, Bearer Token, Access Token and Secret e guardar esses valores em um arquivo .env, como mostrado na foto abaixo.
![Arquivo .env](https://user-images.githubusercontent.com/93171892/194770289-2ed7aed9-1d11-4bec-8c6c-9356c3a05db7.png)

## Trocando a palavra chave de pesquisa, e os parâmetros
Trocar argumento da função tweepy.StreamRule() para a Query de pesquisa.
> [Como montar a sua Query de pesquisa!](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query)

## Como deixar o bot rodando na nuvem?
Eu utilizo o serviço Heroku pra hospedar o bot 24/7 gratuitamente (necessário colocar um cartão de crédito no site para conseguir uptime de 31 dias no mês, caso contrário o bot ficará offline a partir do dia ~26)
> [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
