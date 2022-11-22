flowers = ["Daffodil", "Evening Primrose", "Hydragea", "Iris", "Lavender", "Sunflower", "Tiger Lily"]

for flower in flowers:
    print(flower)
print()

separator = " -*- "
output = separator.join(flowers)
print(output)

print(", ".join(flowers))