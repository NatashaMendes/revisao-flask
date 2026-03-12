from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/revisao')
def revisao():
    return '''
<h1> ???? </h1>
<p> !!!! </p>
<p style=" color: red;">Kwei?</p>
'''
@app.route('/revisao/<nome>/<int:idade>')
def parametros(nome, idade):
    ano_nascimento = 2026 - idade
    return f'Você {nome}, tem {idade} anos, porque nasceu em {ano_nascimento}. Ta fazendo hora extra na terra fdp?'





# ultima coisa
if __name__ == '__main__':
    app.run(debug=True)