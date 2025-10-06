from termcolor import colored

def build_dictionary(n):
    """
    Builds a dictionary where each language's words map to their translations in other languages.
    """
    # Dictionary structure to hold translations for each language
    translation_dict = {
        "persian": {},
        "english": {},
        "french": {},
        "german": {}
    }
    
    print(colored("\nEnter each dictionary entry in the format: <persian> <english> <french> <german>","magenta"))
    for _ in range(n):
        # Read each line of the dictionary input and split into original and translations
        persian, english, french, german = input().strip().split()
        
        # Map translations for each language
        translation_dict["persian"][persian] = {"english": english, "french": french, "german": german}
        translation_dict["english"][english] = {"persian": persian, "french": french, "german": german}
        translation_dict["french"][french.replace(" ", "")] = {"persian": persian, "english": english, "german": german}
        translation_dict["german"][german] = {"persian": persian, "english": english, "french": french}

    return translation_dict

def translate_sentence(sentence, translation_dict, from_lang, to_lang):
    """
    Translates a sentence from `from_lang` to `to_lang`.
    If a word is not in the dictionary, it remains unchanged.
    """
    # Translate each word or keep it as is if not found
    return " ".join(translation_dict.get(from_lang, {}).get(word, {}).get(to_lang, word) for word in sentence)

def main():
    # Choose the input and target languages
    print("Available languages: Persian, English, French, German")
    from_lang = input("Enter the language of the sentence (Persian/English/French/German): ").strip().lower()
    to_lang = input("Enter the language you want to translate to (Persian/English/French/German): ").strip().lower()

    # Validate chosen languages
    if from_lang not in ["persian", "english", "french", "german"] or to_lang not in ["persian", "english", "french", "german"]:
        print("Invalid language selection. Please choose from Persian, English, French, or German.")
        return
    if from_lang == to_lang:
        print("Source and target languages cannot be the same.")
        return

    # Read the number of dictionary entries
    n = int(input("Enter the number of words in the dictionary: ").strip())
    # Build the dictionary from input data
    translation_dict = build_dictionary(n)

    # Read the sentence to be translated and split it into words
    sentence = input("\nEnter the sentence to be translated: ").strip().split()
    
    # Translate and print the translated sentence
    translated_sentence = translate_sentence(sentence, translation_dict, from_lang, to_lang)
    print("\nTranslated Sentence:", translated_sentence)

# Run the main function
if __name__ == "__main__":
    main()




# def build_dictionary(n):
#     """
#     Builds a dictionary where each translation (English, French, German) points to the original word.
#     """
#     translation_dict = {}
#     print("\nEnter each dictionary entry in the format: <original> <english> <french> <german>")
#     for _ in range(n):
#         # Read each line of the dictionary input and split into original and translations
#         original, english, french, german = input().strip().split()
#         # Add translations for each language to point back to the original word
#         translation_dict[english] = original
#         translation_dict[french.replace(" ", "")] = original
#         translation_dict[german] = original
#     return translation_dict

# def translate_sentence(sentence, translation_dict):
#     """
#     Translates a sentence based on the provided translation dictionary.
#     If a word is not in the dictionary, it remains unchanged.
#     """
#     # Translate each word or keep it as is if not found
#     return " ".join(translation_dict.get(word, word) for word in sentence)

# def main():
#     # Read the number of dictionary entries
#     n = int(input("Enter the number of words in the dictionary: ").strip())
#     # Build the dictionary from input data
#     translation_dict = build_dictionary(n)
#     # Read the sentence to be translated and split it into words
#     sentence = input("\nEnter the sentence to be translated: ").strip().split()
#     # Translate and print the translated sentence
#     translated_sentence = translate_sentence(sentence, translation_dict)
#     print("\nTranslated Sentence:", translated_sentence)

# # Run the main function
# if __name__ == "__main__":
#     main()





# # Read number of words in the dictionary
# n = int(input().strip())

# # Initialize dictionary for translations
# dictionary = {}

# # Read the translations
# for _ in range(n):
#     words = input().strip().split()
#     original, english, french, german = words
#     dictionary[english] = original
#     dictionary[french.replace(" ", "")] = original
#     dictionary[german] = original

# # Read the sentence that needs to be translated
# sentence = input().strip().split()

# # Translate each word in the sentence
# translated_sentence = []
# for word in sentence:
#     translated_word = dictionary.get(word, word)  # Use the original word if not in dictionary
#     translated_sentence.append(translated_word)

# # Print the translated sentence
# print(" ".join(translated_sentence))

