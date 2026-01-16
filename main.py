import argparse
from src.domain.action_generator import generate_actions

from src.parser.file_manager import read_file
from src.parser.strips_parser import StripsParser
from src.planner.planner import Planner
from src.metrics.performance import Performance

def format_kb(value):
    return f"{value / 1024:.2f} KB"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--algorithm", required=True)

    args = parser.parse_args()

    instance = args.instance
    algorithm = args.algorithm

    content = read_file(f"assets/problems/blocks-{instance}.strips")

    strips = StripsParser()
    initial_state, goal = strips.parse_problem(content)

    # Ações STRIPS do mundo dos blocos
    actions = generate_actions(strips.map)
    print("ACTIONS:", len(actions))

    planner = Planner(initial_state, goal, actions)



    with Performance() as perf:
        plan = planner.solve(algorithm, perf)

    
    print(f"\n>>> RELATÓRIO DE PLANEJAMENTO: {algorithm.upper()} <<<")
    print("-" * 50)
    
    # Informações da Instância e Métricas
    stats = [
        ("Problema", instance),
        ("Ações Carregadas", len(actions)),
        ("Duração", f"{perf.elapsed:.4f} segundos"),
        ("Estados Visitados", perf.expanded),
        ("Fronteira (Explored)", perf.explored),
        ("Memória de Pico", format_kb(perf.peak_memory))
    ]

    for label, value in stats:
        print(f"{label:<20}: {value}")

    print("-" * 50)

    if plan:
        print(f"SUCESSO: Plano encontrado com {len(plan)} movimentos")
        print("SEQÜÊNCIA DE OPERAÇÕES:")
        # Exibe os passos em uma linha ou formato numerado diferente
        passos = " -> ".join([step for step in plan])
        print(f"  {passos}")
    else:
        print("FALHA: Não foi possível encontrar um caminho até o objetivo.")

    print("-" * 50)

if __name__ == "__main__":
    main()