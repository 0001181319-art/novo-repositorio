from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco agora é feita pelo Flask (não usamos mais sqlite3 direto)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca_jogos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy (ORM)
db = SQLAlchemy(app)

# Criamos uma CLASSE que representa a tabela (antes era SQL manual)
class Jogo(db.Model):
    __tablename__ = 'jogos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    plataforma = db.Column(db.String(50), nullable=False)

    # Método auxiliar para converter objeto em JSON
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "preco": self.preco,
            "plataforma": self.plataforma
        }


# Criamos o banco automaticamente usando ORM
@app.before_first_request
def criar_banco():
    db.create_all()


#  GET (todos ou por id)
@app.route('/jogos', methods=['GET'])
@app.route('/jogos/<int:id>', methods=['GET'])
def gerenciar_jogos(id=None):

    # Usando ORM ao invés de SELECT SQL
    if id:
        jogo = Jogo.query.get(id)
        if jogo:
            return jsonify(jogo.to_dict()), 200
        return jsonify({"erro": "Jogo não encontrado"}), 404

    jogos = Jogo.query.all()
    return jsonify([j.to_dict() for j in jogos]), 200


@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()

    # Criando objeto ao invés de INSERT SQL
    novo_jogo = Jogo(
        nome=dados.get('nome'),
        genero=dados.get('genero'),
        preco=dados.get('preco'),
        plataforma=dados.get('plataforma')
    )

    db.session.add(novo_jogo)
    db.session.commit()

    return jsonify({"mensagem": "Jogo adicionado com sucesso!"}), 201


@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    # Atualização direta do objeto (sem SQL)
    jogo.nome = dados.get('nome')
    jogo.genero = dados.get('genero')
    jogo.preco = dados.get('preco')
    jogo.plataforma = dados.get('plataforma')

    db.session.commit()

    return jsonify({"mensagem": "Jogo atualizado com sucesso!"}), 200


@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):

    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    db.session.delete(jogo)
    db.session.commit()

    return jsonify({"mensagem": f"Jogo '{jogo.nome}' removido!"}), 200


if __name__ == '__main__':
    app.run(debug=True)