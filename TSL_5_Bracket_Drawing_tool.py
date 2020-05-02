from random import randrange

def ro24():
    top_bucket = [
        "Reynor", "Lambo",              # From EU qualifiers
        "Solar", "Trap", "KR3 #1",      # From KR qualifiers
        "Elazer", "NA2 #1", "NA3 #1"    # From NA qualifiers
    ]
    bottom_bucket = [
        "uThermal", "MaNa",             # From EU qualifiers
        "soO", "PartinG", "KR3 #2",     # From KR qualifiers
        "PtitDrogo", "NA2 #2", "NA3 #2" # From NA qualifiers
    ]
    counter = 0

    if len(top_bucket) == 8 and len(bottom_bucket) == 8:
        print("======== Round of 24 ========")
        while top_bucket:
            top_seed = top_bucket.pop(randrange(len(top_bucket)))
            bottom_seed = bottom_bucket.pop(randrange(len(bottom_bucket)))
            counter += 1
            print(f"Match {counter}: {top_seed} vs. {bottom_seed}")

def ro16():
    ro16_players = [
        "Serral", "ShoWTimE", "INnoVation", "Zest", # Invited players
        "HeRoMaRinE",                               # From EU qualifier
        "Clem",                                     # From NA qualifier
        "Trap", "Cure"                              # From KR qualifiers
    ]
    counter = 0

    if len(ro16_players) == 8:
        print("======== Round of 16 ========")
        while ro16_players:
            player = ro16_players.pop(randrange((len(ro16_players))))
            counter += 1
            print(f"Match {counter}: {player} vs. TBD")

ro24()
ro16()
