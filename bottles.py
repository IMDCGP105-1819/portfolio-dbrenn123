MAX_BEERS = 99
ZERO_TEXT = "no more"

for beers_drank in range(0, MAX_BEERS + 1, 1):
    beers = MAX_BEERS - beers_drank # Number of bottles on wall

    # Return text with correct plurality.
    def bottle_text(beers = beers):
        return f"bottle{'s' * (beers != 1)}"

    # If beers are drank, print number now remaining.
    if(beers_drank != 0):
        print(f"Take {'one' if beers else 'it'} down, pass it around, {beers or ZERO_TEXT} {bottle_text()} of beer on the wall.")

    # Print current number of beers remaining on wall.
    print(f"{beers or ZERO_TEXT.capitalize()} {bottle_text()} of beer on the wall, {beers or ZERO_TEXT} {bottle_text()} of beer...")

    # When beers have ran out, restock.
    if(beers == 0):
        print(f"Go to the store and buy some more, {MAX_BEERS} {bottle_text(MAX_BEERS)} of beer on the wall.")
