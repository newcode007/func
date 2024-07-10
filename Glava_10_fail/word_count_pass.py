def count_words(filename):
    """Подсчёт приблизительного количества  строк в файле."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Подсчёт приблизительного количества слов в файле.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['Alice_in_Wonderland.txt', 'sdfghsfg.txt','programming.txt', 'learning_python.py']
for filename in filenames:
    count_words(filename)



