from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_maneger = LoginManager()
db.init_app(app)
login_maneger.init_app(app)

# view login
login_maneger.login_view = 'login'
# Session <- conexão ativa


@login_maneger.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso"})

    return jsonify({"message": "Credencias inválidas"}), 400


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"Message": "Logout realizado com sucesso"})


@app.route('/user', methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get('username')
    passoword = data.get('password')

    if username and passoword:
        user = User(username=username, password=passoword)
        db.session.add(user)
        db.session.commit()
        return jsonify({"Message": "Usuário cadastrado com sucesso"})

    return jsonify({"Message": "Dados inválidas"}), 400


@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_users(id_user):
    user = User.query.get(id_user)

    if user:
        return jsonify({"username": user.username})

    return jsonify({"Message": "Usuário não encontrado"}), 404


@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_users(id_user):
    data = request.json
    user = User.query.get(id_user)

    if user and data.get('password'):
        user.password = data.get('password')
        db.session.commit()

        return jsonify({"Message": f"Usuário {id_user} atualizado com sucesso"})

    return jsonify({"Message": "Usuário não encontrado"}), 404


@app.route('/user/<int:id_user>', methods=['DELETE'])
@login_required
def delete_users(id_user):
    user = User.query.get(id_user)

    if id_user == current_user.id:
        return jsonify({"Message": "Deleção não permitida"}), 403

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"Message": f"Usuário{id_user} deletado com sucesso"})

    return jsonify({"Message": "Usuário não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
