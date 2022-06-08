import json

books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Josue', 'Judges', 'Ruth', '1 Kings', '2-Samuel', '1 Kings', '2 Kings', '3 Kings', '4 Kings', '1 Paralipomenon', '2 Paralipomenon', '1 Esdras', '2 Esdras', 'Nehemiah', 'Tobias', 'Judith', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Canticles', 'Ecclesiasticus', 'Wisdom', 'Sirach', 'Isaias', 'Jeremias', 'Lamentations', 'Baruch', 'Ezechiel', 'Daniel', 'Osee', 'Joel', 'Amos', 'Abdias', 'Jonas', 'Micheas', 'Nahum', 'Habacuc', 'Sophonias', 'Aggeus', 'Zacharias', 'Malachias', '1 Machabees', '2 Machabees', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Apocalypse']

bibledic = {

}


chapter_num_list = [0, 50, 90, 117, 152, 186, 208, 225, 227, 258, 282, 304, 329, 356, 392, 402, 413, 427, 438, 451, 493, 645, 673, 685, 693, 712, 760, 826, 877, 882, 888, 932, 946, 957, 960, 967, 968, 972, 978, 981, 984, 987, 989, 1000, 1004, 1020, 1034, 1062, 1078, 1102, 1123, 1151, 1167, 1182, 1195, 1201, 1207, 1211, 1215, 1220, 1223, 1229, 1233, 1236, 1237, 1250, 1255, 1260, 1263, 1268, 1269, 1270, 1271, 1292, 0]


# An updated chapter list based on new lines added to psalms and other books (Psalms starts at 494)
chapter_num_list2 = [0, 50, 90, 117, 152, 186, 208, 225, 227, 258, 282, 304, 329, 356, 392, 402, 413, 427, 438, 451, 493, 645, 673, 685, 693, 712, 760, 826, 877, 882, 888, 932, 946, 957, 960, 967, 968, 972, 978, 981, 984, 
987, 989, 1000, 1004, 1020, 1034, 1062, 1078, 1102, 1123, 1151, 1167, 1182, 1195, 1201, 1207, 1211, 1215, 1220, 1223, 1229, 1233, 1236, 1237, 1250, 1255, 1260, 1263, 1268, 1269, 1270, 1271, 1291, 0] 



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
for k in range(len(chapter_num_list2) - 1):
    for j, ch in enumerate(chapters[chapter_num_list2[k]:chapter_num_list2[k+1]]): #1229 chapters
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


with open(f'books/EntireBible-DR.json', 'w') as f:
    json.dump(bibledic, f, indent=True)



    


