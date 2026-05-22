PLAPACEHPOLDER = "[name]"



with open("Day 24/Snake+Project+Code+from+Day+21/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open("Day 24/Snake+Project+Code+from+Day+21/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents) 

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLAPACEHPOLDER, stripped_name)
        new_letter = letter_contents.replace(PLAPACEHPOLDER, stripped_name)
        with open(f"Day 24/Snake+Project+Code+from+Day+21/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  