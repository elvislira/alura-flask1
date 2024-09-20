from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.jogo import Jogo
from models.lista_usuarios import ListaUsuarios


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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    
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

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    
    return render_template(
        'login.html',
        titulo = 'Faça seu login',
        proxima=proxima
    )

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuarios = ListaUsuarios().get_usuarios
    nickname = request.form['usuario']
    senha = request.form['senha']
    
    if nickname in usuarios:
        if usuarios[nickname].senha == senha:
            session['usuario_logado'] = nickname
            flash(f'{usuarios[nickname].nome} está logado.', category='success')
            
            proxima_pagina = request.form['proxima']

            return redirect(proxima_pagina)
    else:
        flash('Usuário ou senha inválida. Tente novamente.', category='danger')
        
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso.', category='success')
    
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)