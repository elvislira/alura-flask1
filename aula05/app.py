from flask import Flask, render_template, request, redirect, session, flash
from models.jogo import Jogo


lista_jogos = []

tetris = Jogo('Tetris', 'Puzzle', 'Atari')
god_of_war = Jogo('God of War', 'Rack n Slash', 'PS2')
mortal_combat = Jogo('Mortal Combat', 'Luta', 'PS2')
    
lista_jogos.append(tetris)
lista_jogos.append(god_of_war)
lista_jogos.append(mortal_combat)

app = Flask(__name__)
app.secret_key = 'chavesecreta'


@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo = 'Todos os Jogos',
        jogos = lista_jogos
    )

@app.route('/novo')
def novo():
    return render_template(
        'novo.html',
        titulo = 'Novo jogo'
    )

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)

    lista_jogos.append(jogo)

    return redirect('/')

@app.route('/login')
def login():
    return render_template(
        'login.html',
        titulo = 'Faça seu login'
    )

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'minhasenha' == request.form['senha']:
        usuario = request.form['usuario']
        session['usuario_logado'] = usuario
        flash(f'{usuario} está logado.', category='success')
        
        return redirect('/')
    else:
        flash('Usuário ou senha inválida. Tente novamente.', category='danger')
        
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso.', category='success')
    
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)