survey_result = [
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","C++","JavaScript"],
    ["Python","JavaScript","C++","Java"],
    ["Python","JavaScript","C#"],
]

each_part_set = [set(lang) for lang in (survey_result)]
# print(each_part_set) 
all_language = set.union(*each_part_set)



choose_by_all = set.intersection(*each_part_set)

only_one = set()
only_two = set()

for lang in all_language:
    count = sum(lang in part for part in each_part_set)
    if count == 1 :
        only_one.add(lang)
    elif count == 2:
        only_two.add(lang)

same_lang = []
for lang_choice in survey_result:
    rest_tu = []
    for part in survey_result:
        # print(lang_choice, part)
        if survey_result.index(lang_choice) == survey_result.index(part):
            continue
        elif set(lang_choice) == set(part):
            rest_tu.append(survey_result.index(lang_choice))
            rest_tu.append(survey_result.index(part))

            rest_tu.sort()
            if rest_tu in same_lang:
                continue
            else:
                same_lang.append(rest_tu)
print(same_lang)


print(f"Languages chosen by all participants: {choose_by_all}")
print(f"Number of unique language: {len(all_language)}")
print(f"Languages chosen by one participants: {only_one}")
print(f"Languages chosen by two participants: {only_two}")