def split_and_join(line):
    words = line.split()
    join_words = '-'.join(words)
    return join_words
   

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)