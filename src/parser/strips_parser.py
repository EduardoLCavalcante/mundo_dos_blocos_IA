from src.domain.predicate_map import PredicateMap
from src.domain.state import State
from src.domain.action import Action

class StripsParser:
    def __init__(self):
        self.map = PredicateMap()

    def parse_predicates(self, text):
        predicates = []
        for p in text.split(";"):
            p = p.strip()
            if not p:
                continue

            if p.startswith("~"):
                # STRIPS clássico: predicados negados não entram no estado
                continue
            else:
                predicates.append(self.map.get(p))

        return predicates

    def parse_problem(self, content):
        """
        Analisa o arquivo e identifica os estados inicial e final[cite: 36, 37].
        """
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        
        # Tenta encontrar as linhas por prefixo ou pela posição (assumindo as últimas linhas)
        init_line = next((l for l in lines if l.startswith("INIT:")), None)
        goal_line = next((l for l in lines if l.startswith("GOAL:")), None)

        # Fallback: Se não houver rótulos, o PDF sugere que o estado inicial 
        # e final aparecem sequencialmente 
        if init_line is None or goal_line is None:
            # Assume que a penúltima é INIT e a última é GOAL conforme exemplo do PDF 
            init_line = lines[-2]
            goal_line = lines[-1]

        # Limpa os rótulos se existirem para processar apenas os predicados
        init_raw = init_line.replace("INIT:", "").strip()
        goal_raw = goal_line.replace("GOAL:", "").strip()

        init_preds = self.parse_predicates(init_raw)
        goal_preds = self.parse_predicates(goal_raw)

        # O estado inicial contém as proposições verdadeiras 
        # O estado final contém o que queremos como verdadeiro 
        return State(init_preds), set(goal_preds)

    def parse_actions(self, action_defs):
        """
        Cria as ações com pré-condições e pós-condições[cite: 34, 35].
        """
        actions = []
        for name, pre, add, delete in action_defs:
            
            actions.append(Action(name, pre, add, delete))
        return actions