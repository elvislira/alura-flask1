class Jogo:
    def __init__(self, nome: str, categoria: str, console: str) -> None:
        self._nome = nome
        self._categoria = categoria
        self._console = console

    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def console(self):
        return self._console