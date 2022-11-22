albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metalica", 1984),
          ]
print(len(albums))

for album, artist, year in albums:
    print(f"Album: {album}, Artist: {artist}, Year: {year}")

