START = "start"
END = "end"


def is_small_cave(cave: str):
    return cave.islower()


def rec_dfs(graph: dict[str, list[str]], visited: list[str], current: str) -> list[list[str]]:
    if is_small_cave(current) and current in visited:
        return []

    new_visited = visited + [current]
    if current == END:
        return [new_visited]

    all_paths = []
    for neighbour in graph[current]:
        if neighbour == START:
            continue
        all_paths += rec_dfs(graph, new_visited, neighbour)

    return all_paths


def rec_dfs2(graph: dict[str, list[str]], visited: list[str], current: str) -> list[list[str]]:
    new_visited = visited + [current]
    if current == END:
        return [new_visited]

    if current == START and START in visited:
        return []

    visited_small_caves = [c for c in visited if is_small_cave(c)]
    already_visited_twice = len(set(visited_small_caves)) < len(visited_small_caves)

    if is_small_cave(current) and current in visited and already_visited_twice:
        return []

    all_paths = []
    for neighbour in graph[current]:
        if neighbour == START:
            continue
        all_paths += rec_dfs2(graph, new_visited, neighbour)

    return all_paths


def part1():
    graph = load_graph()

    all_paths = rec_dfs(graph, [], "start")
    return len(all_paths)


def part2():
    graph = load_graph()

    all_paths = rec_dfs2(graph, [], "start")
    return len(all_paths)


def load_graph():
    with open("input12.txt") as file:
        parts = [line.strip().split('-') for line in file.readlines()]
        graph = {}
        for p in parts:
            f = p[0]
            s = p[1]
            if f in graph.keys():
                graph[f].append(s)
            else:
                graph[f] = [s]

            if s in graph.keys():
                graph[s].append(f)
            else:
                graph[s] = [f]
    return graph


print(part1())
print(part2())
