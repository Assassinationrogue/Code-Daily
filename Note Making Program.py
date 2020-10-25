import os

FileInput = str(input("Please enter file name: ") + ".TXT")  # will always return a text file


Check = os.path.exists(FileInput)

if Check:  # to check if file exist in the current directory or not.

    print(
        f'What you want to do?\na). Read file\nb). Delete the file and start over\nc). Append the file\nd). Replace a '
        f'single line')
    OptionSelected = str(input(""))
    if OptionSelected == "a":  # to read the file.
        FileReading = open(FileInput, "r")

        print(FileReading.read())
        FileReading.close()

    elif OptionSelected == "b":  # to delete a file
        os.remove(FileInput)
        FileWriting = open(FileInput, "w")  # will open a new file with the file name
        no_of_lines = 1
        lines = ""

        for i in range(no_of_lines):
            lines += input() + "\n"
        FileWriting.write(lines)
        FileWriting.close()

    elif OptionSelected == "c":
        FileAppend = open(FileInput, "a")  # will open a new file with the file name
        no_of_lines = 1
        lines = ""

        for i in range(no_of_lines):
            lines += input() + "\n"
        FileAppend.write(lines)
        FileAppend.close()

    elif OptionSelected == "d":
        FileReading = open(FileInput, "r")

        print(FileReading.read())
        FileReading.close()

        userInputOfLineNumber = int(input("Please, enter the line number you want to replace: "))
        with open(FileInput, "r") as LineIndexing:

            lineIndexNumber = LineIndexing.readlines()[userInputOfLineNumber - 1]  # to get a proper index of a line

        ReadFile = open(FileInput, "r")

        with ReadFile as inputFile:  # 'with' statements Opens a file do some processing and closes the file

            FileData = inputFile.read()

            NewText = input("Enter the new text to replace with: ")
            ReadFile = open(FileInput, "r")

            FileData = FileData.replace(lineIndexNumber, NewText)
        with open(FileInput, "w") as file:
            file.write(FileData)



else:

    # to write in the file if file exists.
    FileWrite = open(FileInput, "w")  # will open a new file with the file name

    no_of_lines = 1
    lines = ""

    for i in range(no_of_lines):
        lines += input() + "\n"
    FileWrite.write(lines)
    FileWrite.write("\n")
    FileWrite.close()
