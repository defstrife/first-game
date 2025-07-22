levels = {
    1 : {
        "spikes": [(500, 500), (200, 500), (325, 200)],
        "coins": [(100, 250), (600, 105), (625, 450)],
        "barrels":[(300, 400), (400, 400, 'heart')],
        "enemies":[(300, 300)],
        "finishzoneX":325,
        "finishzoneY":450,
        "playerstartX": 100,
        "playerstartY": 100,
        "sublevels": {
            "up" : 3,
            "down" : 4
        }
    },
    2: {
        "spikes": [(100, 200), (400, 500)],
        "coins": [(500, 300), (200, 150), (700, 450)],
        "barrels": [(200, 400), (500, 450, "coin")],
        "enemies": [(200, 200), (400, 400)],
        "finishzoneX": 600,
        "finishzoneY": 450,
        "playerstartX": 700,
        "playerstartY": 100,
        "sublevels": {
            "left" : 5
        }
    },
    3 : {
        "spikes": [(250, 300), (400, 300)],
        "coins": [(100, 100), (700, 100), (275, 350)],
        "barrels":[(100, 674), (700, 400, 'heart')],
        "enemies":[(300, 200)],
        "playerstartX": 400,
        "playerstartY": 550,
        "sublevels": {
            "down": 1,
        }
    },
    4: {
        "spikes": [(100, 300), (700, 400)],
        "coins": [(400, 300), (100, 100), (700, 200)],
        "barrels": [(200, 400), (500, 450, "coin")],
        "enemies": [(200, 500), (400, 300)],
        "playerstartX": 400,
        "playerstartY": 50,
        "sublevels": {
            "up": 1,
        }
    },
    5 : {
        "spikes": [(200, 500), (500, 300)],
        "coins": [(300, 450), (500, 100)],
        "barrels": [(200, 400)],
        "enemies": [(200, 725), (400, 100)],
        "playerstartX": 50,
        "playerstartY": 300,
        "sublevels": {
            "right": 2,
        }
    }
}