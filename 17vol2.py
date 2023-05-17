def obvod(a, b=0):
    print(b)
    if b != 0:
        print(f"Obvod: {(b+a)*2}")

    else:
        b = a
        print(f"Obvod: {4*a}")


def obsah(a, b=0):
    if b != 0:
        print(f"Obsah: {b * a}")

    else:
        print(f"Obvod: {a * a}")


def faktorial(a):
    faktorial = 1
    faktorialString = ""
    for i in range(a):
        faktorialString += f" {i+1} *"
        faktorial = faktorial*(i+1)
    faktorialString = f"{faktorialString[1:-1]} = {faktorial}"

    print(f"Faktorial: {faktorial}")
    print(f"Faktorial: {faktorialString}")


def secist(slovnik):
    soucet = 0.0
    for key, value in slovnik.items():
        if isinstance(key, int):
            soucet += float(key)

        if isinstance(key, float):
            soucet += key

        if isinstance(value, bool):
            pass
        else:
            if isinstance(value, int):
                soucet += float(value)

            if isinstance(value, float):
                soucet += value
            print(value)

    print(soucet)


secist({1: 3, "a": 1.0, 2: 1, "b": False})

