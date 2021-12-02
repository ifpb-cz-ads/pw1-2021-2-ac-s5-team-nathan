from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/questao1', methods=['POST'])
def verificador_multa():
    km = request.form['km']
    km = int(km)
    if km > 80:
        km_acima = km - 80
        valor_cobrado = km_acima * 5
        return '<h1>Será cobrado uma multa de %d R$</h1>' % (valor_cobrado)
    else:
        return '<h1>Não será cobrado multa</h1>'


@app.route('/questao2', methods=['POST'])
def maior_menor_numero():
    numero1 = request.form['numero1']
    numero1 = int(numero1)
    numero2 = request.form['numero2']
    numero2 = int(numero2)
    numero3 = request.form['numero3']
    numero3 = int(numero3)
    min_numero = 0
    max_numero = 0
    if numero1 >= numero2 and numero1 >= numero3:
        max_numero = numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        max_numero = numero2
    else:
        max_numero = numero3
    if numero1 <= numero2 and numero1 <= numero3:
        min_numero = numero1
    elif numero2 <= numero1 and numero2 <= numero3:
        min_numero = numero2
    else:
        min_numero = numero3
    return '<h1>O maior numero é igual a %d e o menor é igual a %d </h1>' % (max_numero, min_numero)


@app.route('/questao4', methods=['POST'])
def calcular_preco():
    distancia = request.form['km']
    distancia = int(distancia)
    if distancia <= 200:
        valor_cobrado = distancia * 0.50
    else:
        valor_cobrado = distancia * 0.45
    return '<h1>O valor cobrado sera de %.2f R$</h1>' % (valor_cobrado)


@app.route('/questao5', methods=['POST'])
def calculardora():
    numero1 = request.form['numero1']
    numero1 = float(numero1)
    numero2 = request.form['numero2']
    numero2 = float(numero2)
    simbolo = request.form['simbolo']
    if simbolo == '+':
        valor_total = numero1 + numero2
        return '<h1>O valor da soma é igual a %.2f</h1>' % (valor_total)
    elif simbolo == '-':
        valor_total = numero1 - numero2
        return '<h1>O valor da subtração é igual a %.2f</h1>' % (valor_total)
    elif simbolo == '*':
        valor_total = numero1 * numero2
        return '<h1>O valor da multiplicação é igual a %.2f</h1>' % (valor_total)
    else:
        valor_total = numero1 / numero2
        return '<h1>O valor da divisão é igual a %.2f</h1>' % (valor_total)


@app.route('/questao6', methods=['POST'])
def casa():
    valor_casa = request.form['casa']
    valor_casa = float(valor_casa)
    salario = request.form['salario']
    salario = float(salario)
    prestacoes = request.form['prestacoes']
    prestacoes = int(prestacoes)
    valor_prestacoes = valor_casa / prestacoes
    if valor_prestacoes <= (salario * 0.3):
        return '<h1>Parabens a compra foi efetuada com sucesso e o valor das prestações sera de %.2f</h1>' % (
            valor_prestacoes)
    else:
        return '<h1>Erro o valor do salario tem que ser igual ou maior a 30% das prestaçoes</h1>'


@app.route('/questao7', methods=['POST'])
def conta_energia():
    kWh = request.form['KWH']
    kWh = float(kWh)
    simbolo = request.form['simbolo']
    simbolo = str(simbolo)
    if (simbolo == 'R') or (simbolo == 'r'):
        if kWh > 500:
            valor_total = kWh * 0.65
            return '<h1>O valor da sua conta de energia residencial é igual a %.2f</h1>' % (valor_total)
        else:
            valor_total = kWh * 0.40
            return '<h1>O valor da sua conta de energia residencial é igual a %.2f</h1>' % (valor_total)
    elif (simbolo == 'C') or (simbolo == 'c'):
        if kWh > 1000:
            valor_total = kWh * 0.60
            return '<h1>O valor da sua conta de energia do seu comercio é igual a %.2f</h1>' % (valor_total)
        else:
            valor_total = kWh * 0.55
            return '<h1>O valor da sua conta de energia do seu comercio é igual a %.2f</h1>' % (valor_total)
    elif (simbolo == 'I') or (simbolo == 'i'):
        if kWh > 5000:
            valor_total = kWh * 0.60
            return '<h1>O valor da sua conta de energia da sua industria é igual a %.2f</h1>' % (valor_total)
        else:
            valor_total = kWh * 0.55
            return '<h1>O valor da sua conta de energia da sua industria é igual a %.2f</h1>' % (valor_total)