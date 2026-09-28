from flask import Flask, render_template

# Criamos nossa aplicação Flask
app = Flask(__name__)


# Criamos a rota da página inicial
@app.route("/")
def inicio():

    nome = "João"

    alunos = [
        {"id": 1, "nome": "João", "idade": 20},
        {"id": 2, "nome": "Maria", "idade": 22},
        {"id": 3, "nome": "Pedro", "idade": 25}
    ]

    return render_template(
        "index.html",
        nome=nome,
        alunos=alunos
    )


# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)