import string
import csv

def readbook(filename, clean=True):
    """
    Reads a textfile into a single string.
    Standardizes punctuation to help with sentence splitting.
    """
    try:
        with open(filename, 'r') as myfile:
            # Replace line breaks and tabs with spaces
            data = myfile.read().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    except FileNotFoundError:
        return ""
    
    #AI prompt used: Please remove the headers and footers from the alice.txt file
    # Remove Project Gutenberg headers and footers
    prolog = data.find("*** START")
    if prolog > -1:
        data = data[prolog:]
    epilog = data.find('End of the Project Gutenberg EBook')
    if epilog > -1:
        data = data[:epilog]
    epilog2 = data.find('*** END')
    if epilog2 > -1:
        data = data[:epilog2]

    if clean:
        printable = set(string.printable)
        data = ''.join(filter(lambda x: x in printable, data))
        # Replace common punctuation with space
        data = data.replace(';', ' ').replace(',', ' ').replace(':', ' ')
        # Replace sentence terminators with dot for consistent splitting
        data = data.replace('?', '.').replace('!', '.').replace(':', '.')
        # Replace other characters and lowercase the text
        data = data.replace('-', ' ').replace('"', ' ').replace("'", " ").lower()
        
    return data

input_filename = 'Alice.txt'
# Create an output filename based on the input
output_filename = input_filename.replace('.txt', '_stats.csv')

text = readbook(input_filename)

if not text:
    print(f"Error: Could not read {input_filename}")
else:
    # Split text by '.' to get sentences
    sentences = text.split('.')
    # Remove empty strings
    sentences = [s.strip() for s in sentences if s.strip()]

    total_words_in_sentences = 0
    total_chars_in_words = 0
    total_words_count = 0
    
    # List for word length frequency
    word_len_counts = [0] * 21
    
    # Dictionary for word frequency
    word_freq_dict = {}

    for sentence in sentences:
        words = sentence.split()
        total_words_in_sentences += len(words)
        
        for word in words:
            total_words_count += 1
            length = len(word)
            total_chars_in_words += length
            
            # Count word lengths (cap at 20)
            if length <= 20:
                word_len_counts[length] += 1
            
            # 2. Count specific word occurrences for the dictionary
            if word in word_freq_dict:
                word_freq_dict[word] += 1
            else:
                word_freq_dict[word] = 1

    # Calculations
    avg_sentence_len = total_words_in_sentences / len(sentences) if len(sentences) > 0 else 0
    avg_word_len = total_chars_in_words / total_words_count if total_words_count > 0 else 0

    # Sort dictionary to find top 100
    sorted_words = sorted(word_freq_dict.items(), key=lambda item: item[1], reverse=True)


    #Ai prompt used: "Please take the program attached and instead of printing the stats on terminal, print on a seperate csv file"
    # Write CSV File
    print(f"Calculating statistics for {input_filename}...")
    
    try:
        with open(output_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            
            # Section 1: General Averages
            writer.writerow(['--- General Statistics ---'])
            writer.writerow(['Metric', 'Value'])
            writer.writerow(['Average Sentence Length (words)', f"{avg_sentence_len:.2f}"])
            writer.writerow(['Average Word Length (chars)', f"{avg_word_len:.2f}"])
            writer.writerow([]) # Blank row for separation

            # Section 2: Word Length Counts
            writer.writerow(['--- Word Length Counts ---'])
            writer.writerow(['Word Length', 'Count'])
            for i in range(1, 21):
                writer.writerow([f"Length {i}", word_len_counts[i]])
            writer.writerow([]) # Blank row for separation

            # Section 3: Top 100 Common Words
            writer.writerow(['--- Top 100 Most Common Words ---'])
            writer.writerow(['Rank', 'Word', 'Frequency'])
            
            for i in range(min(100, len(sorted_words))):
                word, count = sorted_words[i]
                writer.writerow([i + 1, word, count])
        
        print(f"Success! Statistics have been written to '{output_filename}'.")

    except IOError:
        print(f"Error: Could not write to file {output_filename}")