
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Isabela Karoline  
**Turma:** Rio Negrinho — Tarde  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Escola — Sistema de Cadastro e Notas  
**Código analisado:** `codigo/app.py`  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Isabela, você desenvolveu uma primeira versão de um sistema escolar que permite cadastrar estudantes, adicionar notas e consultar médias e situações acadêmicas. Seu projeto demonstra compreensão de conceitos fundamentais da programação em Python.

Pontos positivos identificados:

- Organizou as principais operações em funções: `cadastrar_aluno()`, `adicionar_nota()` e `listar_alunos()`.
- Utilizou **listas e dicionários** para armazenar nome, idade, turma e notas dos estudantes.
- Implementou **tratamento de erros com `try/except ValueError`** ao solicitar idade e notas.
- Validou as notas para aceitar somente valores entre 0 e 10.
- Utilizou `sum()` e `len()` para calcular a média aritmética.
- Criou uma regra para exibir a situação do estudante a partir da média.
- Implementou um menu com opções de cadastro, listagem, lançamento de notas e encerramento.

## O que precisa ser corrigido

### 1. Validar completamente o cadastro

A idade passa por conversão para inteiro, mas o programa ainda aceita valores negativos ou zero. O nome e a turma também podem ser cadastrados vazios.

**Como melhorar:** verificar se o nome e a turma foram preenchidos e se a idade está em uma faixa adequada. Quando a entrada for inválida, informar o problema e solicitar a correção.

### 2. Evitar cadastros duplicados

Atualmente, o sistema permite cadastrar repetidamente estudantes com o mesmo nome e turma, sem alertar o usuário.

**Como melhorar:** verificar se o estudante já existe antes de adicioná-lo à lista. Para projetos maiores, considere utilizar um identificador único para cada estudante.

### 3. Melhorar a organização das chamadas de limpeza da tela

O programa utiliza `os.system("cls")` em diferentes pontos e também fora das funções. Esse comando é específico do Windows e sua repetição dificulta a manutenção.

**Como melhorar:** criar uma função `limpar_tela()` que escolha o comando conforme o sistema operacional. Chamar essa função somente nos momentos necessários.

## Oportunidades de melhoria

### 4. Separar o cálculo da média da listagem

O cálculo da média e da situação do estudante está dentro de `listar_alunos()`.

**Como melhorar:** criar uma função como `calcular_media(notas)` e outra para determinar a situação. Isso permitirá reutilizar as mesmas regras em futuras consultas e relatórios.

### 5. Melhorar a busca de estudantes

Atualmente, o lançamento de notas exige que o nome e a turma correspondam exatamente aos valores cadastrados. Pequenas diferenças de digitação podem impedir a localização.

**Como melhorar:** padronizar as entradas e considerar a utilização de um código de matrícula. Isso também ajudará a diferenciar estudantes com nomes iguais.

### 6. Documentar melhor as funções

O código contém alguns comentários, mas não apresenta descrições suficientes sobre as responsabilidades das funções e as regras do sistema.

**Como melhorar:** adicionar docstrings curtas explicando o cadastro, a busca, o lançamento de notas e o cálculo das médias. Atualizar o README com instruções específicas do projeto.

### 7. Melhorar a apresentação das consultas

As funções de consulta não possuem uma pausa padronizada ao final, o que pode prejudicar a leitura dependendo de como o terminal é utilizado.

**Como melhorar:** estabelecer um padrão de exibição e retorno ao menu, permitindo que o usuário termine a leitura antes de continuar.

## Testes recomendados

1. Cadastrar estudantes com dados válidos.
2. Tentar cadastrar nome vazio, turma vazia e idade negativa.
3. Tentar cadastrar duas vezes o mesmo estudante.
4. Lançar uma nota válida e conferir a média.
5. Digitar letras e notas fora do intervalo de 0 a 10.
6. Consultar um estudante ainda sem notas.
7. Verificar o comportamento quando não houver estudantes cadastrados.

## Prioridades para a próxima versão

1. **Validar nome, idade e turma.**
2. **Impedir cadastros duplicados.**
3. **Separar o cálculo da média em uma função reutilizável.**
4. **Padronizar a limpeza da tela e a navegação.**
5. **Documentar as regras e registrar testes.**

## Mensagem final

Isabela, seu trabalho demonstra que você consegue aplicar **funções, listas, dicionários, condições, repetições e tratamento de erros** para construir uma solução relacionada ao ambiente escolar.

Você já possui uma base importante para continuar evoluindo o sistema. Concentre-se agora em fortalecer as validações e organizar as regras em funções reutilizáveis. **Continue praticando e testando diferentes situações: cada melhoria ajudará você a desenvolver programas mais confiáveis e fáceis de compreender.**
