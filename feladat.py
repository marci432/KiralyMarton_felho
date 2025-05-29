#egy függvényt hoz létre az első sor
def keszit_diagram_sort(nap_szama, homerseklet):
#elmenti a homersekletet a csillagok szama valtozoba
    csillagok_szama = int(homerseklet)
#annyi csillagot generál amennyi a hőmérséklet
    csillagok = '*' * csillagok_szama
#a nap számát a csillagokat es a homersekletet egy stringbe illeszti
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor

#másik függvény létrehozása
def rajzolj_diagram(homersekletek):
#kiírja a diagrammot
    print("Napi átlaghőmérséklet diagram (°C)")
#kiír egy vonalat ami 40 kötőjelből áll
    print("-" * 40)
#a for ciklus minden napon végigmegy
    for i in range(len(homersekletek)):
        nap = i + 1  # Napok számozása 1-től indul
        sor = keszit_diagram_sort(nap, homersekletek[i])
        print(sor)

#listába teszi az átlaghőmérsékleteket
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]
#visszatzér a függvény
rajzolj_diagram(napi_atlaghomersekletek)


