import docx  #работа с документом
import pandas  #таблица
import matplotlib.pyplot as plt  #график

#чтение текста из файла
document = docx.Document('lion.docx')
content = ''
for p in document.paragraphs:
    content += p.text
#очистка текста от знаков
symbols_to_remove = ['°', '=', '!', '?', '…', '\uf00f', '―', '[', ':', ')', '.', '/', '–', '\t', '’', '\xa0', '№', '_', '*', '—', '(', '»', ',', '«', '\n', ';', '-', ']', "'"]
for s in symbols_to_remove:
    content = content.replace(s, ' ')

#подсчёт слов
words = content.split()
total = len(words)
word_counts = {}
for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

#расчёт процентов
stats = []
for w, count in word_counts.items():
    percent = round(count / total * 100, 2)
    stats.append([w, count, percent])

#создание таблицы
df = pandas.DataFrame(stats, columns=['Слово', 'Частота встречи, раз', 'Частота встречи в %'])
df.to_excel('counter_words.xlsx', index=False)

#подсчёт символов
char_counts = {}
for ch in content:
    char_counts[ch] = char_counts.get(ch, 0) + 1

#подготовка к графику
sorted_chars = sorted(char_counts.items())
labels, values = zip(*sorted_chars)

plt.figure(figsize=(12, 6))
plt.bar(labels, values, color='cornflowerblue', edgecolor='black')
plt.title('встречаемость букв в тексте')
plt.xlabel('буквы')
plt.ylabel('кол-во')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
