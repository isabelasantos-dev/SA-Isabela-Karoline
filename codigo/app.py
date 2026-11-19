# os imports traz ferramentas prontas

import json # serve pra salvar os alunos num arquivo e não perder quando fechar
import math # serve pra ver se o número é válido
import os # os para limpar a tela
import unicodedata # serve pra ignorar acento
from datetime import datetime # datetime serve pra validar a data

# define a medida mínima pra aprovar o aluno.
MEDIA_MINIMA = 6.0
ARQUIVO = "alunos.json" # arquivo onde os alunos ficam salvos
alunos = [] # lista onde todos os alunos ficam guardados

def normalizar(texto):
    """Padroniza texto para comparar ignorando caixa, acentos e espaços."""
    texto = " ".join(texto.split())
    sem_acentos = "".join(
        caractere
        for caractere in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(caractere)
    )
    return sem_acentos.casefold()

def limpar_tela():
    """Limpa a tela usando o comando adequado ao sistema operacional."""
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)

def pausar():
    """Espera ENTER antes de voltar ao menu."""
    try:
        input("\nPressione ENTER para voltar ao menu...")
    except (EOFError, KeyboardInterrupt):
        pass

def salvar_dados():
    """Salva todos os alunos no arquivo alunos.json."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=2)

def carregar_dados():
    """Carrega os alunos salvos. Se não houver arquivo, começa vazio."""
    global alunos
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                alunos = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            alunos = []

def ler_texto(pergunta, maximo):
    """Lê um texto obrigatório e verifica seu tamanho."""
    while True:
        valor = " ".join(input(pergunta).split())

        if not valor:
            print("Este campo não pode ficar vazio.")
        elif len(valor) > maximo:
            print(f"Use no máximo {maximo} caracteres.")
        else:
            return valor

def ler_nome():
    """Lê e valida o nome do aluno."""
    while True:
        nome = ler_texto("Nome: ", 100)

        if any(letra.isalpha() for letra in nome):
            return nome

        print("O nome precisa conter pelo menos uma letra.")

def ler_idade():
    """Lê uma idade inteira entre 6 e 17 anos."""
    while True:
        entrada = input("Idade (6 a 17 anos): ").strip()

        try:
            idade = int(entrada)
        except ValueError:
            print("Digite uma idade inteira, sem letras ou casas decimais.")
            continue

        if 6 <= idade <= 17:
            return idade

        print("A idade precisa estar entre 6 e 17 anos.")

def ler_nota():
    """Lê uma nota entre 0 e 10 e aceita vírgula decimal."""
    while True:
        entrada = input("Nota (0 a 10): ").strip().replace(",", ".")

        try:
            nota = float(entrada)
        except ValueError:
            print("Digite um número válido, por exemplo 7,5.")
            continue

        if math.isfinite(nota) and 0 <= nota <= 10:
            return nota

        print("A nota precisa ser um número entre 0 e 10.")

def ler_data():
    """Lê uma data real no formato AAAA-MM-DD."""
    while True:
        entrada = input(
            "Data da aula (AAAA-MM-DD, por exemplo 2026-11-18): "
        ).strip()

        try:
            data_lida = datetime.strptime(entrada, "%Y-%m-%d").date()

            if data_lida.isoformat() == entrada:
                return entrada
        except ValueError:
            pass

        print("Data inválida. Use o formato AAAA-MM-DD.")

def buscar_aluno_por_nome_turma(nome, turma):
    """Busca aluno por nome e turma, ignorando caixa, acentos e espaços."""
    nome_chave = normalizar(nome)
    turma_chave = normalizar(turma)

    for aluno in alunos:
        if (
            normalizar(aluno["nome"]) == nome_chave
            and normalizar(aluno["turma"]) == turma_chave
        ):
            return aluno

    return None

def escolher_aluno():
    """Pede nome e turma e retorna o aluno encontrado ou None."""
    nome = ler_texto("Nome do aluno: ", 100)
    turma = ler_texto("Turma do aluno: ", 50)
    aluno = buscar_aluno_por_nome_turma(nome, turma)

    if aluno is None:
        print("Aluno não encontrado nessa turma.")

    return aluno

def cadastrar_aluno():
    """Cadastra um aluno e impede nomes iguais na mesma turma."""
    print("\n--- CADASTRAR ALUNO ---")

    nome = ler_nome()
    idade = ler_idade()
    turma = ler_texto("Turma: ", 50)

    if buscar_aluno_por_nome_turma(nome, turma) is not None:
        print("Já existe um aluno com esse nome nessa turma.")
        return

    aluno = {
        "nome": nome,
        "idade": idade,
        "turma": turma,
        "notas": [],
        "frequencia": {},
    }

    alunos.append(aluno)
    salvar_dados()
    print("Aluno cadastrado com sucesso.")

def calcular_media(notas):
    """Calcula a média das notas; retorna None se ainda não houver notas."""
    if not notas:
        return None

    return sum(notas) / len(notas)

def determinar_situacao(media):
    """Determina a situação escolar a partir da média."""
    if media is None:
        return "Sem notas"
    if media >= MEDIA_MINIMA:
        return "Aprovado(a)"
    return "Abaixo da média mínima"

def adicionar_nota():
    """Registra uma nota e mostra a média atual do aluno."""
    print("\n--- ADICIONAR NOTA ---")
    aluno = escolher_aluno()
    if aluno is None:
        return

    descricao = ler_texto(
        "Disciplina/avaliação (ex.: Matemática - prova 1): ",
        80,
    )
    nota = ler_nota()

    aluno["notas"].append({
        "descricao": descricao,
        "valor": nota,
    })
    salvar_dados()

    notas = [item["valor"] for item in aluno["notas"]]
    media = calcular_media(notas)

    print(f"Nota registrada. Média atual: {media:.2f}.")
    print(f"Situação: {determinar_situacao(media)}.")

def registrar_frequencia():
    """Registra presença ou falta e mostra a frequência atual."""
    print("\n--- REGISTRAR FREQUÊNCIA ---")
    aluno = escolher_aluno()
    if aluno is None:
        return

    data_aula = ler_data()

    if data_aula in aluno["frequencia"]:
        print("Já existe uma chamada para esse aluno nessa data.")
        return

    while True:
        situacao = input(
            "Situação (P = presente, F = falta): "
        ).strip().upper()

        if situacao in ("P", "F"):
            break

        print("Escolha P para presente ou F para falta.")

    aluno["frequencia"][data_aula] = situacao
    salvar_dados()
    mostrar_frequencia(aluno)

def mostrar_frequencia(aluno):
    """Calcula e exibe o percentual de presença do aluno."""
    chamadas = aluno["frequencia"]

    if not chamadas:
        print("Ainda não há aulas registradas para este aluno.")
        return

    total = len(chamadas)
    presentes = sum(
        1 for situacao in chamadas.values() if situacao == "P"
    )
    percentual = presentes / total * 100

    print(
        f"Frequência: {presentes}/{total} aulas "
        f"= {percentual:.1f}%."
    )

def mostrar_resumo_aluno(aluno):
    """Exibe os dados, a média, a situação e a frequência do aluno."""
    notas = [item["valor"] for item in aluno["notas"]]
    media = calcular_media(notas)
    situacao = determinar_situacao(media)

    if media is None:
        media_texto = "Sem notas"
    else:
        media_texto = f"{media:.2f}"

    chamadas = aluno["frequencia"]

    if not chamadas:
        frequencia_texto = "Sem chamadas"
    else:
        total = len(chamadas)
        presentes = sum(
            1 for item in chamadas.values() if item == "P"
        )
        percentual = presentes / total * 100
        frequencia_texto = f"{presentes}/{total} aulas ({percentual:.1f}%)"

    print(
        f"- {aluno['nome']} | {aluno['idade']} anos "
        f"| Turma: {aluno['turma']}"
    )
    print(f"  Média: {media_texto} | Situação: {situacao}")
    print(f"  Frequência: {frequencia_texto}")

def consultar_alunos():
    """Consulta todos os alunos ou filtra a lista por turma."""
    print("\n--- CONSULTAR ALUNOS ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("1 - Pesquisar uma turma")
    print("2 - Listar todos os alunos")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        turma = ler_texto("Digite a turma: ", 50)
        resultado = [
            aluno for aluno in alunos
            if normalizar(aluno["turma"]) == normalizar(turma)
        ]

        if not resultado:
            print("Não há alunos cadastrados nessa turma.")
            return

        print(f"\nAlunos da turma {resultado[0]['turma']}:")
        for aluno in resultado:
            mostrar_resumo_aluno(aluno)

    elif opcao == "2":
        alunos_ordenados = sorted(
            alunos,
            key=lambda aluno: (
                normalizar(aluno["turma"]),
                normalizar(aluno["nome"]),
            ),
        )

        for aluno in alunos_ordenados:
            mostrar_resumo_aluno(aluno)

    else:
        print("Opção inválida.")

def editar_nota():
    """Edita ou remove uma nota já lançada de um aluno."""
    print("\n--- EDITAR / REMOVER NOTA ---")
    aluno = escolher_aluno()
    if aluno is None:
        return

    if not aluno["notas"]:
        print("Este aluno ainda não tem notas.")
        return

    print("\nNotas do aluno:")
    for i, item in enumerate(aluno["notas"], start=1):
        print(f"{i} - {item['descricao']} : {item['valor']}")

    try:
        indice = int(input("\nQual nota quer alterar? Digite o número: ")) - 1
    except ValueError:
        print("Digite apenas o número da nota.")
        return

    if indice < 0 or indice >= len(aluno["notas"]):
        print("Número inválido.")
        return

    print("1 - Corrigir valor da nota")
    print("2 - Remover essa nota")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        nova_nota = ler_nota()
        aluno["notas"][indice]["valor"] = nova_nota
        print("Nota corrigida com sucesso!")
    elif opcao == "2":
        removida = aluno["notas"].pop(indice)
        print(f"Nota '{removida['descricao']}' removida.")
    else:
        print("Opção inválida.")
        return

    salvar_dados()

def remover_aluno():
    """Remove um aluno do sistema após confirmação."""
    print("\n--- REMOVER ALUNO ---")
    aluno = escolher_aluno()
    if aluno is None:
        return

    confirmacao = input(
        f"Tem certeza que quer remover {aluno['nome']}? (S/N): "
    ).strip().upper()

    if confirmacao == "S":
        alunos.remove(aluno)
        salvar_dados()
        print("Aluno removido com sucesso!")
    else:
        print("Remoção cancelada.")

def menu():
    """Apresenta as opções principais e executa a escolhida."""
    carregar_dados()
    acoes = {
        "1": cadastrar_aluno,
        "2": adicionar_nota,
        "3": registrar_frequencia,
        "4": consultar_alunos,
        "5": editar_nota,
        "6": remover_aluno,
    }

    while True:
        limpar_tela()
        print("==== SISTEMA ESCOLAR ====")
        print("1 - Cadastrar aluno")
        print("2 - Adicionar nota e ver média")
        print("3 - Registrar presença/falta")
        print("4 - Consultar alunos")
        print("5 - Editar / remover nota")
        print("6 - Remover aluno")
        print("0 - Sair")

        try:
            opcao = input("Escolha: ").strip()
        except KeyboardInterrupt:
            print("\nPrograma encerrado.")
            break
        except EOFError:
            print("\nEntrada encerrada. Até mais!")
            break

        if opcao == "0":
            salvar_dados()
            print("Dados salvos. Até mais!")
            break

        acao = acoes.get(opcao)

        if acao is None:
            print("Opção inválida. Escolha um número do menu.")
            pausar()
            continue

        try:
            acao()
        except KeyboardInterrupt:
            print("\nOperação interrompida.")
        except EOFError:
            print("\nEntrada encerrada.")
            break

        pausar()

if __name__ == "__main__":
    menu()