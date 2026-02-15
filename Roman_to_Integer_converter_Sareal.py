# Ülesanne 1 - Roman to Integer

s = input("Sisesta palun Rooma number: ")

# 1. Lubatud sümbolid ja nende väärtused
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

allowed_subtractions = ["IV", "IX", "XL", "XC", "CD", "CM"]

# 2. Kontroll: ainult lubatud tähed
for letter in s:
    if letter not in values:
        print("Viga: Sisesta palun kehtiv Rooma number.")
        exit()

result = 0
i = 0
repeat_count = 1  # loendab sama sümboli kordusi

while i < len(s):

    # Kontroll korduste jaoks
    if i > 0 and s[i] == s[i - 1]:
        repeat_count += 1

        # I, X, C, M võivad olla max 3 korda järjest
        if s[i] in ["I", "X", "C", "M"] and repeat_count > 3:
            print("Viga: Liiga palju järjestikuseid korduvaid numbreid.")
            exit()

        # V, L, D ei tohi korduda
        if s[i] in ["V", "L", "D"]:
            print("Viga: V, L ja D ei tohi korduda.")
            exit()
    else:
        repeat_count = 1

    # Lahutamise kontroll
    if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
        pair = s[i] + s[i + 1]

        if pair not in allowed_subtractions:
            print("Viga: Kehtetu lahutamistehte kombinatsioon.")
            exit()

        result += values[s[i + 1]] - values[s[i]]
        i += 2
    else:
        result += values[s[i]]
        i += 1

print("Teie tulemus on:", result)


