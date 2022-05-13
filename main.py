import json

books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Josue', 'Judges', 'Ruth', '1 Kings', '2-Samuel', '1 Kings', '2 Kings', '3 Kings', '4 Kings', '1 Paralipomenon', '2 Paralipomenon', '1 Esdras', '2 Esdras', 'Nehemiah', 'Tobias', 'Judith', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Canticles', 'Ecclesiasticus', 'Wisdom', 'Sirach', 'Isaias', 'Jeremias', 'Lamentations', 'Baruch', 'Ezechiel', 'Daniel', 'Osee', 'Joel', 'Amos', 'Abdias', 'Jonas', 'Micheas', 'Nahum', 'Habacuc', 'Sophonias', 'Aggeus', 'Zacharias', 'Malachias', '1 Machabees', '2 Machabees', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Apocalypse']

bibledic = {

}

chapter_num_list = [0, 50, 90, 117, 152, 186, 208, 225, 227, 258, 281, 303, 328, 355, 391, 401, 412, 426, 437, 450, 469, 620, 648, 660, 668, 687, 735, 801, 852, 857, 863, 907, 921, 932, 935, 942, 943, 947, 953, 956, 959, 962, 964, 975, 979, 995, 1009, 1037, 1053, 1077, 1097, 1125, 1141, 1156, 1169, 1175, 1181, 1185, 1189, 1194, 1197, 1203, 1207, 1210, 1211, 1224, 1229, 1234, 1237, 1242, 1243, 1244, 1245, 1264, 0]

def has_numbers(inputString):
    list = []
    number_bool = False
    for i, char in enumerate(inputString):
        if not char.isdigit():
            list.append(char)
        elif char.isdigit() and ":" not in inputString[:3]:
            number_bool = True 

    newstring = ''.join(list).lstrip(' ')    
    return newstring, number_bool
            

with open("dr_bible.txt", 'r') as f:
    bible = f.read()
    chapters = bible.split("____________________")

count = 0
for k in range(len(chapter_num_list) - 1):

    for j, ch in enumerate(chapters[chapter_num_list[k]:chapter_num_list[k+1]]): #1229 chapters
        verse_num = 1
        for i, line in enumerate(ch.split("\n")):
            for b in books:
                if b == line:
                    current_book = b
                    bibledic[current_book] = {}

            if "CHAPTER" in line or "PSALM" in line:
                bibledic[current_book][str(j + 1)] = {}

            elif has_numbers(line)[1] and str(j + 1)in bibledic[current_book]:
                bibledic[current_book][str(j + 1)][str(verse_num)] = has_numbers(line)[0]
                verse_num += 1



with open('full_bible.json', 'w') as f:
    json.dump(bibledic, f, indent=True)



    


