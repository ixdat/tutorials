

lines = []
with open("../../data/01/iridium_butterfly_CVA.mpt", "r", encoding="ISO-8859-1") as f:
    i = 0
    for line in f:
        if i < 200 or i % 20 == 0:
            lines.append(line)
        i += 1

with open("../../data/01/iridium_butterfly_short_CVA.mpt", "w") as f:
    f.writelines(lines)