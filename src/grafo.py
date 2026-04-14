grafo_kanto = {
    "Pallet": [("Viridian", 1)],    
     
    "Viridian": [("Pallet", 1), ("Viridian Forest", 4), ("Victory Road", 7)],

    "Viridian Forest": [("Viridian", 4), ("Diglett's Cave A", 4)],

    "Diglett's Cave A": [("Viridian Forest", 4), ("Pewter", 2), ("Diglett's Cave B", 5)],

    "Diglett's Cave B": [("Diglett's Cave A", 5), ("Lavender", 6), ("Vermilion", 2), ("Fuchsia", 3)],

    "Pewter": [("Diglett's Cave A", 2), ("Mt. Moon", 4)],

    "Mt. Moon": [("Pewter", 4), ("Cerulean", 4) ],

    "Cerulean": [("Mt. Moon", 4), ("Rock Tunnel", 5), ("Saffron", 2)],

    "Rock Tunnel": [("Cerulean", 5), ("Lavender", 4), ("Power Plant", 3)],

    "Power Plant": [("Rock Tunnel", 3)],

    "Lavender": [("Rock Tunnel", 4), ("Saffron", 2), ("Diglett's Cave B", 6), ("Fuchsia", 5)],

    "Vermilion": [("Saffron", 2), ("Diglett's Cave B", 2), ("Fuchsia", 3)],

    "Saffron": [("Cerulean", 2), ("Lavender", 2), ("Vermilion", 2), ("Celadon", 2)],

    "Celadon": [("Saffron", 2), ("Fuchsia", 3)],

    "Fuchsia": [("Lavender", 5), ("Diglett's Cave B", 3), ("Celadon", 3), ("Seafoam Islands", 5)],

    "Seafoam Islands": [("Fuchsia", 5), ("Cinnabar Island", 5)],

    "Cinnabar Island": [("Seafoam Islands", 5), ("Pallet", 6)],

    "Victory Road": [("Viridian", 7), ("Indigo Plateau", 3)],

    "Indigo Plateau": [("Victory Road", 3)]

}