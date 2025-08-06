survey_result = [
    ["Python","JavaScript","C++",],
    ["Python","JavaScript","C#",],
    ["Python","Java"],
    ["Python","C++","JavaScript",],
    ["Python","JavaScript","C++","Java"],
]

each_part_set = [set(lang) for lang in (survey_result)]
# print(each_part_set) 
all_language = set.union(*each_part_set)

choose_by_all = set.intersection(*each_part_set)
print(f"Languages chosen by all participants: {choose_by_all}")



print(f"Number of unique language: {len(all_language)}")
choose_by_one = set.difference_update(*each_part_set)
# choose_by_one = all_language.symmetric_difference
print(f"Languages chosen by one participants: {choose_by_one}")