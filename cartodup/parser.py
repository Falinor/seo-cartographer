def parse(path: str) -> str:
    with open(path) as f:
        for line in f:
            yield line
