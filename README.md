🧠 Planejamento em Inteligência Artificial – Mundo dos Blocos (STRIPS)

Este projeto implementa um planejador automático para o problema clássico do Mundo dos Blocos, utilizando o formalismo STRIPS e diferentes algoritmos de busca em Inteligência Artificial.
O objetivo é encontrar uma sequência de ações que transforme um estado inicial em um estado final desejado, respeitando as restrições do domínio.

🎯 Objetivo do Projeto

Modelar o problema do Mundo dos Blocos utilizando STRIPS

Implementar e comparar algoritmos clássicos de busca

Avaliar desempenho em termos de tempo, número de nós e uso de memória

Produzir um relatório experimental conforme exigido no enunciado acadêmico

📦 Estrutura do Projeto
blocks-world-planning-IA/
│
├── main.py                     # Ponto de entrada do sistema
├── README.md                   # Documentação do projeto
│
├── instances/                  # Arquivos de instância (STRIPS)
│
├── src/
│   ├── domain/
│   │   ├── state.py             # Representação do estado
│   │   ├── action.py            # Ações STRIPS
│   │   ├── node.py              # Nó da busca
│   │   └── predicate_map.py     # Mapeamento de predicados
│   │
│   ├── planner/
│   │   └── planner.py           # Seleção e execução dos algoritmos
│   │
│   ├── search/
│   │   ├── bfs.py               # Busca em Largura (BFS)
│   │   ├── dls.py               # Busca em Profundidade Limitada (DLS)
│   │   ├── ids.py               # Busca em Profundidade Iterativa (IDS)
│   │   ├── astar.py             # Busca A*
│   │   └── bidirectional.py     # Busca Bidirecional (bônus)
│   │
│   ├── heuristics/
│   │   └── blocks_heuristic.py  # Heurística do A*
│   │
│   └── utils/
│       └── performance.py       # Coleta de métricas

🧩 Modelagem do Problema

Cada estado é representado como um conjunto de predicados verdadeiros

As ações seguem o formalismo STRIPS:

Pré-condições

Lista de adição

Lista de remoção

O estado objetivo é definido como um conjunto parcial de predicados que devem ser satisfeitos

🔎 Algoritmos Implementados
✔ Busca em Largura (BFS)

Busca não informada

Garante solução ótima

Alto consumo de memória

✔ Busca em Profundidade Limitada (DLS)

Utilizada como base para o IDS

Controla ciclos por limite de profundidade

✔ Busca em Profundidade Iterativa (IDS)

Combina completude do BFS com menor uso de memória

Executa DLS com limites crescentes

✔ Busca A*

Busca informada por heurística

Utiliza função de avaliação f(n) = g(n) + h(n)

Mantém optimalidade com heurística admissível

✔ Busca Bidirecional (Bônus)

Implementação limitada

Justificada teoricamente devido às restrições do STRIPS

🧠 Heurística Utilizada (A*)

Foi utilizada uma heurística baseada na contagem de predicados do estado objetivo ainda não satisfeitos no estado atual.

Características:

✔ Admissível

✔ Simples

✔ Reduz significativamente o espaço de busca em relação ao BFS

📊 Métricas Coletadas

Durante a execução, o sistema coleta automaticamente:

Tempo total de execução

Número de nós expandidos

Número de nós explorados

Uso de memória atual e pico

Essas métricas são utilizadas para a análise comparativa entre os algoritmos.

▶️ Como Executar
Requisitos

Python 3.9+

Execução
python main.py --instance=4-0 --algorithm=BFS

Algoritmos disponíveis

BFS

IDS

ASTAR

BIDIR

📄 Saída Esperada
============================================================
                     Execution summary
============================================================
Algorithm         : BFS
Instance          : 4-0
Time elapsed      : 0.009520 s
Expanded nodes    : 269
Explored nodes    : 122
Total memory cost : 5.72 KB
Memory usage      : current=22.74 KB; peak=90.75 KB
------------------------------------------------------------
Solution (6 steps):
   1. pick-up_b
   2. stack_b_a
   3. pick-up_c
   4. stack_c_b
   5. pick-up_d
   6. stack_d_c
============================================================

📚 Considerações Finais

Este projeto demonstra a aplicação prática de algoritmos clássicos de busca no contexto de planejamento em Inteligência Artificial. A utilização do formalismo STRIPS e a instrumentação de métricas permitiram uma análise clara das vantagens e limitações de cada abordagem.

👨‍🎓 Contexto Acadêmico

Projeto desenvolvido como atividade avaliativa da disciplina de Inteligência Artificial, com foco em:

Planejamento automático

Algoritmos de busca

Análise experimental