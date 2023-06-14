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

Pokusy:

1. Pokus
Převedl jsem si obrázek do černobíle podoby, abych ověřil, zda-li vůbec můžu celou mřížku poskladat tak, 
aby každý pár očí měl na přilehlé stěne pusu (ten černobilý obrázek jsem udělal proto, protože mě mátla ta barva). 
Lze vytvořit takovou mřížku (ve skutečnosti jich lze vytvořit hned několik). Postup jak vytvořit mřížku aby všechny 
stěny čverečku měly takové přílehlé stěny, že vždycky obrázek na stěně bude mít jiný obrázek na stěně přilehlé by 
vypadal tak, že si zvolíme první čvereček, který je v levem horním rohu jako defaultní (ať je tam zobrazení jakékoliv). 
V dalším kroku se budeme držet pravidla, že na protější straně nemůže být ten stejný vzor, takže můžeme na protější stranu
zobrazit druhý typ obrázku. Když se budeme držet dalšího pravidla, které jsme si zadali, tak určitě musí na přilehlé stějne 
platit to, že tam bude opačný pbrázek než, který je na stěne čverečku, ve kterém se nacházíme my. Tento jednoduchý algoritmus
nám pomůže v prvních třech vrchních čverečcích a prvních levých vyplnít čverečcích vyplnit prostřední smajlíky. Dále jsem si 
všiml, že pokud si zvolíme v levém horním rohu pořadí například [["top", "mouth"], ["right", "mouth"], ["bottom", "eyes"], ["left", "eyes"]],
tak v dolním pravém rohu bude je vždy zrcadlově přetočený -> [["top", "eyes"], ["right", "eyes"], ["bottom", "mouth"], ["left", "mouth"]] a
když tohle víme, tak ho tam můžeme tedy zrcadlově vložit a vyplnit polsední trojci pravých čtverečků a spodní trojci dolních čverečků podle algoritmu
který jsem vytvořil na začatků, protože opět znamé pravý dolní čtvereček a můžeme se držet jednoduchých dvou pravidel (když si vybereme nějakou 
stranu čverečku, tak obrázek na této straně bude jiný, než obrázek na prostější straně čverečku a vždycky když budeme mít dva čverečky vedle sebe, 
tak jejich přilehle strany budou mít opačné obrázky aby tvořili smajlíka). V tuto chvíli máme vyřešené prostředky v pro vnější čverečky mřížky/čverečku.
Proto, abychom vyplnili celý čvereček jsem empiricky vytvořil algoritmus, který říká, že ty nejvíc vnější hrany na každé straně musí mít vždy dva stejné
obrázky a jeden rozdílný -> Kždy například vezmu první stři levé čverečky ne levé straně mřížky, tak všechny levé stěný by měly ve finále dát trojici, 
kde budou například kombinace "mouth", "mouth", "eyes" nebo "mouth", "eyes", "mouth", nebo "eyes", "mouth", "mouth" nebo
"eyes", "eyes", "mouth", nebo "eyes", "mouth", "eyes", nebo "mouth", "eyes", "eyes". No a s tím, co jsme dělali v minulých krocích by jsme měli být schopní
doplnit vzor, který do trojice zbývá a pak znovu pokračovat s naším úplně prvním algoritmem.



"""