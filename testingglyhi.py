"""import win32com.client, os
oShell = win32com.client.Dispatch("Wscript.Shell")
print(oShell.SpecialFolders("MyDocuments"))

print(os.path.join(oShell.SpecialFolders("MyDocuments"), 'ten.txt'))"""

import helpers as gf
import re
from math import modf

text = """1. Définir les objectifs du projet :
    Il est important de définir les objectifs du projet, tels que la création d'un nouveau site web, la refonte d'un site existant, l'ajout de nouvelles fonctionnalités, etc.
    1. Définir les objectifs du projet :
    Il est important de définir les objectifs du projet, tels que la création d'un nouveau site web, la refonte d'un site existant, l'ajout de nouvelles fonctionnalités, etc.

    2. Identifier les parties prenantes :
    Il est important de déterminer les parties prenantes du projet, telles que les clients, les utilisateurs finaux, les développeurs, les designers, etc.

2. Identifier les parties prenantes :
    Il est important de déterminer les parties prenantes du projet, telles que les clients, les utilisateurs finaux, les développeurs, les designers, etc.
    1. Définir les objectifs du projet :
    Il est important de définir les objectifs du projet, tels que la création d'un nouveau site web, la refonte d'un site existant, l'ajout de nouvelles fonctionnalités, etc.
    • ferre
    • ferre
    • ferre
    - ctttg
    - ctttg
    - ctttg

    2. Identifier les parties prenantes :
    Il est important de déterminer les parties prenantes du projet, telles que les clients, les utilisateurs finaux, les développeurs, les designers, etc.

3. Élaborer un budget :
    Il est important d'élaborer un budget pour le projet, en prenant en compte les coûts de développement, de conception, d'hébergement et de maintenance.

4. Élaborer un calendrier :
    Il est important d'établir un calendrier réaliste pour le projet, en prenant en compte les délais de développement, de conception et de test."""

text_treated = gf.treat_text(text)
"""
text_treated_2 = {}
list_index = []
actual_higher_level = 0
#print(text_treated)
for _paragraph in text_treated:
    
    left_delimiter = re.findall(r'\d{1,3}\. ', _paragraph)
    left_delimiter_2 = re.findall(r' \d{1,3}\. ', _paragraph)
    left_delimiter_int = int(re.findall(r'\d', left_delimiter[0])[0])
    left_delimiter_int_2 = int(re.findall(r'\d', left_delimiter_2[0])[0]) if len(left_delimiter_2) != 0 else 0
    actual_higher_level = left_delimiter_int if left_delimiter_int_2 == 0 else actual_higher_level
    list_index.append( actual_higher_level if left_delimiter_int_2 == 0 else gf.concatNumbersToFloat(actual_higher_level, left_delimiter_int_2)  )
    
actual_higher_level = 0
list_index_2 = list_index
for i in range(len(list_index)) :
    if i == 0 :
        actual_higher_level = list_index[i]
        continue
    else :
        if list_index[i] == actual_higher_level :
            list_index[i] = gf.concatNumbersToFloat(actual_higher_level, list_index[i])
        elif actual_higher_level == list_index[i]-1 :
            if modf(list_index[i-1])[0] != 0 and modf(list_index[i-1])[0] == list_index[i]-1 :
                if i < len(list_index)-2 :
                    if list_index[i] == list_index[i+1] :
                        list_index[i] == gf.concatNumbersToFloat(actual_higher_level, list_index[i])
                else :
                    """
"""index_in_list = 0
for _paragraph in text_treated:
    
    left_delimiter = re.findall(r'\d{1,3}\. ', _paragraph)
    left_delimiter_int = int(re.findall(r'\d', left_delimiter[0])[0])
    right_delimiter = re.findall( r':\n([\s\S]*)' ,_paragraph)
    
    pattern_string = ( re.escape(left_delimiter[0]) if len(left_delimiter) != 0 else '' ) + "(.*:)" #+ ( re.escape(right_delimiter[0]) if len(right_delimiter) != 0 else '' )
    pattern = re.compile(pattern_string)
    title = pattern.findall(_paragraph)[0]
    
    splitted_paragraph = right_delimiter[0].splitlines(True)
    paragraph_treated = {}
    actual_paragraph_position = 0
    for i in range(len(splitted_paragraph)) :
        point_character = re.findall(r'^\s*•', splitted_paragraph[i])
        hyphen_character = re.findall(r'^\s*-', splitted_paragraph[i])
        if len(point_character) != 0 :
            if i > 0 and len(re.findall(r'^\s*•', splitted_paragraph[i-1])) != 0 :
                paragraph_treated[actual_paragraph_position]["content"].append(splitted_paragraph[i][1:])
            else :
                actual_paragraph_position += 1 if i!=0 else 0
                paragraph_treated[actual_paragraph_position] = {
                    "type" : "point",
                    "content" : [splitted_paragraph[i][1:]]
                }
        elif len(hyphen_character) != 0 :
            if i > 0 and len(re.findall(r'^\s*-', splitted_paragraph[i-1])) != 0 :
                paragraph_treated[actual_paragraph_position]["content"].append(splitted_paragraph[i][1:])
            else :
                actual_paragraph_position += 1 if i!=0 else 0
                paragraph_treated[actual_paragraph_position] = {
                    "type" : "hyphen",
                    "content" : [splitted_paragraph[i][1:]]
                }
        else :
            actual_paragraph_position += 1 if i!=0 else 0
            paragraph_treated[actual_paragraph_position] = {
                "type" : "normal",
                "content" : splitted_paragraph[i]
            }
    
    text_treated_2[list_index[index_in_list]] = {
        "title" : title,
        "content" : paragraph_treated
    }
    index_in_list += 1
    if actual_higher_level == left_delimiter_int - 1 :
        if previous_level == left_delimiter_int - 1 :
            text_treated_2[left_delimiter_int] = {
                "title" : title,
                "content" : right_delimiter
            }
            actual_higher_level = left_delimiter_int
            previous_level_level = left_delimiter_int
        else :
            
            text_treated_2[left_delimiter_int] = {
                "title" : title,
                "content" : right_delimiter
            }"""

with open("console.txt", "a") as f :
    f.write("\n")
    f.write(str(text_treated))

print(text_treated)