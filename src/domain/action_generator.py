from src.domain.action import Action


def extract_blocks(predicate_map):
    """
    Extrai os blocos a partir de predicados como:
    on_a_b, clear_c, ontable_d
    """
    blocks = set()

    for pred in predicate_map._map.keys():
        parts = pred.split("_")
        if parts[0] in ("on",):
            blocks.add(parts[1])
            blocks.add(parts[2])
        elif parts[0] in ("clear", "ontable", "holding"):
            blocks.add(parts[1])

    return sorted(blocks)


def generate_actions(predicate_map):
    blocks = extract_blocks(predicate_map)
    actions = []

    def on(x, y): return predicate_map.get(f"on_{x}_{y}")
    def clear(x): return predicate_map.get(f"clear_{x}")
    def ontable(x): return predicate_map.get(f"ontable_{x}")
    def holding(x): return predicate_map.get(f"holding_{x}")
    handempty = predicate_map.get("handempty")

    # -------------------
    # pick-up(x)
    # -------------------
    for x in blocks:
        actions.append(
            Action(
                name=f"pick-up_{x}",
                preconditions=[
                    ontable(x),
                    clear(x),
                    handempty
                ],
                add_effects=[
                    holding(x)
                ],
                del_effects=[
                    ontable(x),
                    clear(x),
                    handempty
                ]
            )
        )

    # -------------------
    # put-down(x)
    # -------------------
    for x in blocks:
        actions.append(
            Action(
                name=f"put-down_{x}",
                preconditions=[
                    holding(x)
                ],
                add_effects=[
                    ontable(x),
                    clear(x),
                    handempty
                ],
                del_effects=[
                    holding(x)
                ]
            )
        )

    # -------------------
    # stack(x, y)
    # -------------------
    for x in blocks:
        for y in blocks:
            if x != y:
                actions.append(
                    Action(
                        name=f"stack_{x}_{y}",
                        preconditions=[
                            holding(x),
                            clear(y)
                        ],
                        add_effects=[
                            on(x, y),
                            clear(x),
                            handempty
                        ],
                        del_effects=[
                            holding(x),
                            clear(y)
                        ]
                    )
                )

    # -------------------
    # unstack(x, y)
    # -------------------
    for x in blocks:
        for y in blocks:
            if x != y:
                actions.append(
                    Action(
                        name=f"unstack_{x}_{y}",
                        preconditions=[
                            on(x, y),
                            clear(x),
                            handempty
                        ],
                        add_effects=[
                            holding(x),
                            clear(y)
                        ],
                        del_effects=[
                            on(x, y),
                            clear(x),
                            handempty
                        ]
                    )
                )

    return actions
