# Bottle song
ZERO_TEXT = "no more"
# Loop 0-99
for beers_drank in range(0, 100, 1):
    # Print: verse of bottle song with correct Number
    beers = 100 - beers_drank - 1

    # Line 2
    if(beers_drank != 0):
        print(f"Take one down, pass it around, {beers or ZERO_TEXT} bottles of beer on the wall.")

    # Line 1
    print(f"{beers or ZERO_TEXT.capitalize()} bottles of beer on the wall, {beers or ZERO_TEXT} bottles of beer...")

    # On final loop print: ending verse
    if(beers == 0):
        print(f"Go to the store and buy some more, 99 bottles of beer on the wall")
