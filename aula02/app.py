from flask import Flask, render_template
from models.jogo import Jogo


app = Flask(__name__)

@app.route('/aula02')
def aula02():
    tetris = Jogo('Tetris', 'Puzzle', 'Atari')
    god_of_war = Jogo('God of War', 'Rack n Slash', 'PS2')
    mortal_combat = Jogo('Mortal Combat', 'Luta', 'PS2')
    
    lista_jogos = [tetris, god_of_war, mortal_combat]
    
    return render_template(
        'index.html', 
        titulo='Meus Jogos',
        jogos = lista_jogos
    )

app.run()