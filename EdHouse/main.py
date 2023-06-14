colors = ["red", "green", "blue", "yellow"]

grid = [
    [
        [
            {"top":  ["mouth", "red"]},
            {"right":  ["mouth", "yellow"]},
            {"bottom":  ["eyes", "red"]},
            {"left":  ["eyes", "green"]},
        ],
        [
            {"top":  ["eyes", "blue"]},
            {"right":  ["eyes", "yellow"]},
            {"bottom":  ["mouth", "blue"]},
            {"left":  ["mouth", "green"]},
        ],
        [
            {"top":  ["eyes", "red"]},
            {"right":  ["eyes", "yellow"]},
            {"bottom":  ["mouth", "blue"]},
            {"left":  ["mouth", "yellow"]},
        ],
    ],
    [
        [
            {"top":  ["mouth", "red"]},
            {"right":  ["eyes", "blue"]},
            {"bottom":  ["eyes", "green"]},
            {"left":  ["mouth", "red"]},
        ],
        [
            {"top":  ["eyes", "blue"]},
            {"right":  ["eyes", "green"]},
            {"bottom":  ["mouth", "red"]},
            {"left":  ["mouth", "yellow"]},
        ],
        [
            {"top":  ["mouth", "blue"]},
            {"right":  ["mouth", "yellow"]},
            {"bottom":  ["eyes", "red"]},
            {"left":  ["eyes", "green"]},
        ],
    ],
    [
        [
            {"top":  ["mouth", "blue"]},
            {"right":  ["mouth", "green"]},
            {"bottom":  ["eyes", "yellow"]},
            {"left":  ["eyes", "blue"]},
        ],
        [
            {"top":  ["eyes", "blue"]},
            {"right":  ["mouth", "red"]},
            {"bottom":  ["mouth", "blue"]},
            {"left":  ["eyes", "yellow"]},
        ],
        [
            {"top":  ["eyes", "yellow"]},
            {"right":  ["mouth", "red"]},
            {"bottom":  ["mouth", "green"]},
            {"left":  ["eyes", "green"]},
        ],
    ]
]

"""
Poznatky:
    
+ Vždy jsou v každém čverečku dva páry očí a dvě pusy.
+ Vždy jsou pusy vedle sebe a páry očí vedle sebe -> nikdy se nestane, že by pusa byla naproti puse a páry oči byly naproti sobě.
+ Červených polovin = 9
+ Modrých polovin = 10
+ Zelených polovin = 8
+ Žlutých polovin = 9
+ Zatím nevím, zdali-li se má řešit otáčením jednotlivých čverečků aby na sebe obličeje pasovaly jak barvou, tak i jako tváří nebo pohybem jednotlivých čverečů či kombinací obou.
"""