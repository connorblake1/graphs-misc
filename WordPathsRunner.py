from WordPathKeeperFile import WordPathKeeper

wpk = WordPathKeeper()
wpk.load_words()
wpk.build_edges()
print (f"{len(wpk.vertices)} nodes, {len(wpk.edges)} edges.")

# Alternately, use this method once to build the edges and save them to a file.
# I'll let you research saving files, yourself.... It's fairly similar to opening a file.
# Then load the file in the future. wpk.load_edges()

num_letters = len(wpk.vertices[0])

while True:
    while True:
        word1 = input(f"Enter the first {num_letters}-letter word: ")
        if len(word1) != num_letters:
            print(f"{word1} has the wrong number of letters.")
        else:
            break # a good answer - stop asking for #1

    while True:
        word2 = input(f"Enter the second {num_letters}-letter word: ")

        if len(word2) != num_letters:
            print(f"{word2} has the wrong number of letters.")
        elif word1 == word2:
            print("That was the same word.")
        else:
            break # a good answer - stop asking for #2

    print(f"Searching for path from \"{word1}\" to \"{word2}.\"")
    path = wpk.find_path(word1, word2)
    for i in range(len(wpk.vertices)):
        if wpk.vertices[i] == word1:
            w1 = i
        elif wpk.vertices[i] == word2:
            w2 = i
    if path is None:
        print (f"No path found from \"{word1}\" to \"{word2}.\"")
    elif len(path) == 0:
        print ("You have returned an empty list.")
    elif path[0] != w1:
        print (f"ERROR: The first word in the path did not match word 1.\n{path}")
    elif path[-1] != w2:
        print (f"ERROR: The last word in the path did not match word 2.\n{path}")
    else:
        #Success!
        print (f"Path has {len(path)-1} steps:")
        for word in path:
            print(wpk.vertices[word])


