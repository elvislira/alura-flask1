from models.usuario import Usuario


class ListaUsuarios:
    def __init__(self) -> None:
        self._usuario1 = Usuario('Ana Cristina', 'ac', 'ac123')
        self._usuario2 = Usuario('Renata da Silva', 'rs', 'rs123')
        self._usuario3 = Usuario('Fernando Lima', 'fl', 'fl123')
        
    @property
    def get_usuarios(self) -> dict:
        return {
            self._usuario1.nickname: self._usuario1,
            self._usuario2.nickname: self._usuario2,
            self._usuario3.nickname: self._usuario3
        }