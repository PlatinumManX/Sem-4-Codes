def create(filename):
    with open(filename, "w") as file:
        print("Enter the content for the file (Type 'STOP' on a new line to finish):")
        while True:
            line=input()
            if line.upper()=="STOP":
                break
            file.write(line+"\n")
    print("File {} created successfully\n".format(filename))

def count(filename):
    with open(filename, "r") as file:
        content=file.readlines()
        num_lines=len(content)
        num_words=sum(len(line.split()) for line in content)
        num_chars=sum(len(line.rstrip("\n")) for line in content)
    print("File {} Details:-".format(filename))
    print("Lines: {}".format(num_lines))
    print("Words: {}".format(num_words))
    print("Characters: {}\n".format(num_chars))
    return content

def copy_and_read(source, destination):
    with open(destination, "w") as new_file:
        content=count(source)
        new_file.writelines(content)
    print("Content copied to {}".format(destination))
    with open(destination, "r") as new_file:
        print(new_file.read().strip())

source_file="original.txt"
new_file="copy.txt"
create(source_file)
copy_and_read(source_file, new_file)
