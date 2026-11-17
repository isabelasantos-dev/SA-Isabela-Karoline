import os
os.system("cls")

# SISTEMA DE ESCOLA 
alunos = []

def cadastrar_aluno():
    os.system("cls")
    nome = input("Nome do aluno: ").strip().capitalize()
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Digite apenas números inteiros para a idade.")

    turma = input("Turma (ex: 1°1): ").strip()

    alunos.append({"nome": nome, "idade": idade, "turma": turma, "notas": []})
    print("Aluno cadastrado com sucesso!")
    input("\nPressione ENTER para voltar ao menu...")
    os.system("cls")


def adicionar_nota():
    os.system("cls")
    if len(alunos) == 0:
        print("Cadastre algum aluno primeiro.")
        return
    
    nome_buscar = input("Digite o nome do aluno: ").strip().capitalize()
    turma_buscar = input("Digite a turma do aluno (ex: 1°1): ").strip()
    
    encontrado = False

    for aluno in alunos:
        # Procura se o nome e a turma coincidem exatamente
        if aluno["nome"] == nome_buscar and aluno["turma"] == turma_buscar:
            try:
                nota =float(input(f"Digite a nota (0 a 10) para {aluno['nome']}: "))
                
                if 0 <= nota <= 10:
                    aluno["notas"].append(nota)
                    print(f"Nota {nota} adicionada com sucesso para {aluno['nome']}!")
                else:
                    print("A nota deve ser um valor entre 0 e 10.")
            except ValueError:
                print("Digite apenas números válidos para a nota.")
                
            encontrado = True
            break
    
     
    if not encontrado:
        print("Aluno não encontrado com esse nome nessa turma.")
os.system("cls")

def listar_alunos():
    os.system("cls")
    print("\n--- ALUNOS ---")
    if len(alunos) == 0: 
        print("Nenhum aluno cadastrado ainda.")
    else:
        for i, a in enumerate(alunos):
            print(f"\n[{i+1}] Nome: {a['nome']} | Idade: {a['idade']} anos | Turma: {a['turma']}")
            print(f"    Notas: {a['notas'] if a['notas'] else 'Sem notas'}")
            
            # Se houver notas, calcula a média automaticamente na listagem
            if a['notas']:
                media = sum(a['notas']) / len(a['notas'])
                status = "Aprovado(a)" if media >= 6.0 else "Reprovado(a)"
                print(f"    Média: {media:.2f} ({status})")
os.system("cls")

# MENU PRINCIPAL
while True:
    print("\n==== SISTEMA DE ESCOLA ====")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Adicionar nota do aluno")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        adicionar_nota()
    elif opcao == "0":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida!")
