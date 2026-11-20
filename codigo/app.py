import json
import math
import os
import unicodedata
from datetime import datetime
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

MEDIA_MINIMA = 6.0
ARQUIVO = "alunos.json"
alunos = []

def normalizar(texto):
    """Padroniza texto para comparar ignorando caixa, acentos e espaços."""
    if not texto:
        return ""
    texto = " ".join(str(texto).split())
    sem_acentos = "".join(
        caractere
        for caractere in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(caractere)
    )
    return sem_acentos.casefold()

def carregar_dados():
    global alunos
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                alunos = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            alunos = []

def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    # Renderiza automaticamente o arquivo index.html dentro da pasta templates
    return render_template("index.html")

@app.route("/api/alunos", methods=["GET"])
def listar_alunos():
    carregar_dados()
    return jsonify(alunos)

@app.route("/api/alunos", methods=["POST"])
def cadastrar_aluno():
    carregar_dados()
    dados = request.json
    nome = dados.get("nome", "").strip()
    idade = dados.get("idade")
    turma = dados.get("turma", "").strip()

    if not nome or not turma or idade is None:
        return jsonify({"erro": "Preencha todos os campos obrigatórios."}), 400

    nome_chave = normalizar(nome)
    turma_chave = normalizar(turma)
    for a in alunos:
        if normalizar(a["nome"]) == nome_chave and normalizar(a["turma"]) == turma_chave:
            return jsonify({"erro": "Já existe um aluno com esse nome nessa turma."}), 400

    novo_aluno = {
        "nome": nome,
        "idade": int(idade),
        "turma": turma,
        "notas": [],
        "frequencia": {}
    }
    alunos.append(novo_aluno)
    salvar_dados()
    return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "aluno": novo_aluno})

if __name__ == "__main__":
    carregar_dados()
app.run(host="0.0.0.0", port=5000, debug=False)
