🧠 Planejamento em Inteligência Artificial – Mundo dos Blocos (STRIPS)

Este projeto implementa um planejador automático para o problema clássico do Mundo dos Blocos, utilizando o formalismo STRIPS e diferentes algoritmos de busca em Inteligência Artificial.
O objetivo é encontrar uma sequência de ações que transforme um estado inicial em um estado final desejado, respeitando as restrições do domínio.

🎯 Objetivo do Projeto

Modelar o problema do Mundo dos Blocos utilizando STRIPS

Implementar e comparar algoritmos clássicos de busca

Avaliar desempenho em termos de tempo, número de nós e uso de memória

Produzir um relatório experimental conforme exigido no enunciado acadêmico

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

## 📄 Saída Esperada

Ao executar o algoritmo A* na instância 4-0, o sistema apresentará o seguinte relatório técnico:

```text
>>> RELATÓRIO DE PLANEJAMENTO: ASTAR <<<
--------------------------------------------------
Problema            : 4-0
Ações Carregadas    : 12
Duração             : 0.0045 segundos
Estados Visitados   : 42
Fronteira (Explored): 18
Memória de Pico     : 112.40 KB
--------------------------------------------------
SUCESSO: Plano encontrado com 6 movimentos
SEQÜÊNCIA DE OPERAÇÕES:
  pick-up_b -> stack_b_a -> pick-up_c -> stack_c_b -> pick-up_d -> stack_d_c
--------------------------------------------------
============================================================
```

📚 Considerações Finais

Este projeto demonstra a aplicação prática de algoritmos clássicos de busca no contexto de planejamento em Inteligência Artificial. A utilização do formalismo STRIPS e a instrumentação de métricas permitiram uma análise clara das vantagens e limitações de cada abordagem.

👨‍🎓 Contexto Acadêmico

Projeto desenvolvido como atividade avaliativa da disciplina de Inteligência Artificial, com foco em:

Planejamento automático

Algoritmos de busca

Análise experimental
