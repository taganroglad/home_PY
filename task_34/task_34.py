def count_vowels(word):
    vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
    return sum(1 for char in word if char in vowels)


def check_rhythm(poem):
    lines = poem.split()
    syllable_count = None

    for line in lines:
        words = line.split('-')
        line_syllables = [count_vowels(word) for word in words]

        if syllable_count is None:
            syllable_count = line_syllables
        else:
            if syllable_count != line_syllables:
                return "Пам парам"

    return "Парам пам-пам"


poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
