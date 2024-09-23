def file_name(file_name: str) -> str:
    with open(f"data/{file_name}", encoding="utf-8") as file:
        # file.read()
        format_text = []
        for line in file.readlines():
            if line.isalpha():
                format_text.append(line)
            else:
                new_word = ""
                for lin in line:
                    if lin.isalpha():
                        new_word += lin
                if len(new_word) > 0:
                    format_text.append(new_word)
        print(format_text)
        # return format_text
    with open("data/{format_file_name.txt}", "w", encoding="utf-8") as new_file:
        new_file.write("\n".join(format_text))
sdavcsdv