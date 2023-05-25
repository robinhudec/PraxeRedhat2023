def obvod(a, b=0):
    if a == 0 or a < 0 or b < 0:
        raise Exception
    if b != 0:
        return (b+a)*2

    else:
        return 4*a


def obsah(a, b=0):
    if a == 0 or a < 0 or b < 0:
        raise Exception
    if b != 0:
        return b * a

    else:
        return a * a


def faktorial(a):
    if a < 0 or type(a) == "str":
        raise Exception
    faktorial = 1
    faktorialString = ""
    for i in range(a):
        faktorialString += f" {i+1} *"
        faktorial = faktorial*(i+1)
    faktorialString = f"{faktorialString[1:-1]} = {faktorial}"

    return faktorial


def secist(slovnik):
    soucet = 0.0
    for key, value in slovnik.items():
        if isinstance(key, int):
            soucet += float(key)

        if isinstance(key, float):
            soucet += key

        if isinstance(value, int):
            soucet += float(value)

        if isinstance(value, float):
            soucet += value

    return soucet



