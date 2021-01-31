# python-test-prometheus-client

Este teste tem como objetivo testar integração de aplicações python com Prometheus usando prometheus _ cliente e armazenar um configuração para VSCode, afim de reutilizar futuramente.

Para configuara o projeto inicial no VSCode, após definir o diretório e a estrutura do projeto, foi instalado as extenções Code Runner e Python(Mycrosoft).

Para criar o ambiente virtual foi utilizado o seguinte comando:

```
$python 3 -m venv venv
```

Para ativar será preciso usar/executar o arquivo de ativação venv/bin/activate (ou um dos equivalentes para shells diferentes). a ativação pode ser feita usando um dos seguintes comandos:

```
$#ponto espaço e comando
$. venv/bin/activate
$#ou 
$source /Users/elsonsilva/Workspace/Python/PrometheusMonitoring/venv/bin/activate
```

As configurações em .vscode/settings.json ativam a execução do projeto em virtualenv, habilita testes e outros.