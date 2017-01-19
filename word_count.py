"""统计文件包含多少个单词"""

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("the file " + filename + " is not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has " + str(num_words) + " words.")
