def to_bytes(size: str) -> int:
    """ """
    num, unit = size.split()
    match unit:
        case 'KiB':
            s = 2 ** 10
        case 'MiB':
            s = 2 ** 20
        case 'GiB':
            s = 2 ** 30
        case 'TiB':
            s = 2 ** 40
        case _:
            raise ValueError(f"Unexpected input: {size}")
    return int(s * float(num))
