# Your task in this Kata is to emulate text justification in monospace font. You will be given a
# single-lined text and the expected justification width. The longest word will never be greater than this width.
#
# Here are the rules:
#
# Use spaces to fill in the gaps between words.
# Each line should contain as many words as possible.
# Use '\n' to separate lines.
# Gap between words can't differ by more than one space.
# Lines should end with a word not a space.
# '\n' is not included in the length of a line.
# Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# Last line should not be justified, use only one space between words.
# Last line should not contain '\n'
# Strings with one word do not need gaps ('somelongword\n').

def justify(text, width):
    new_text = ''
    while len(text) > width:
        if text[width] == ' ':
            new_text += text[:width].rstrip() + '\n'
            text = text[width:].lstrip()
        elif text[width-1] == ' ':
            str_i = text[:width-1].rstrip()
            str_i = str_i.replace(" ", "  ", 1)
            new_text += str_i + '\n'
            text = text[width:].lstrip()
        else:
            str_i = text[:width - text[width-1::-1].index(" ")].rstrip()
            spaces = str_i.count(' ')
            if spaces != 0:
                # m = len(str_i)
                j = ((width - len(str_i)) // spaces)
                k = ((width - len(str_i)) % spaces)
                str_i = str_i.replace(" ", " "*(j+1))
                str_i = str_i.replace(" " * (j+1), " " * (j+2), k)
            new_text += str_i +'\n'
            text = text[width - text[width-1::-1].index(" "):].lstrip()
    new_text += text
    return new_text


text = 'От консультации получила именно то, чего ожидала - помощь в выборе направлений развития. \
Перед консультацией выслали подробный опросник и несколько тестов. На встрече Екатерина помогла \
определится с направлениями развития, подсказала, как можно скорректировать резюме под это направление. \
После консультации я прошла несколько бесплатных курсов и интенсивов, чтобы окончательно определится, \
и в ноябре я начинаю обучаться своей новой профессии.'
print(justify(text, 75))
# print(text[:30 - text[30-1::-1].index(" ")])
# t='1234 567 890'
# print(t)
# print(t[::-1])
# print(t[4::-1])
# print(t[5::-1])
# print(t[:4:-1])
