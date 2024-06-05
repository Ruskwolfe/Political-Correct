import tkinter as tk
from tkinter import scrolledtext
import Levenshtein as lev

# Define your bad words and alternatives here
bad_words_dict = {
"neger" : "person av afrikansk opprinnelse",
"kryple" : "person med funksjonshemming",
"homo" : "homofil person",
"sigøyner" : "romani person",
"eskimo" : "person fra Arktis",
"transvestitt" : "transperson",
"mongoloid" : "person med Downs syndrom",
"psykopat" : "person med antisosial personlighetsforstyrrelse",
"idiot" : "person med kognitive begrensninger",
"debil" : "person med kognitive begrensninger",
"tulling" : "person med psykisk helseutfordring",
"galning" : "person med psykisk helseutfordring",
"feit" : "overvektig person eller person med stor kroppsbygning",
"dverg" : "kortvokst person",
"jomfru" : "person som ikke har hatt sex",
"hore" : "sexarbeider",
"illegal innvandrer" : "udokumentert innvandrer eller person uten oppholdstillatelse",
"gymlærer" : "kroppsøvingslærer",
"husmor" : "hjemmearbeidende eller person som styrer husholdningen",
"fargeblind" : "person med fargevisjonsutfordringer",
"døvstum" : "person som er døv",
"blind" : "uvitende om eller ikke oppmerksom på"
    # Add more words as needed
}

# Threshold for Levenshtein distance to consider a word similar enough to a bad word
levenshtein_threshold = 2

def scan_document_and_suggest():
    document_text = text_input.get("1.0", tk.END)
    words = document_text.split()
    bad_words_count = {}
    total_bad_words = 0

    for word in words:
        for bad_word in bad_words_dict.keys():
            if lev.distance(word.lower(), bad_word) <= levenshtein_threshold:
                bad_words_count[bad_word] = bad_words_count.get(bad_word, 0) + 1
                total_bad_words += 1
                break

    suggestions_text.delete('1.0', tk.END)  # Clear previous suggestions
    for bad_word, count in bad_words_count.items():
        suggestions_text.insert(tk.END, f'"{bad_word}" (suggested alternative: "{bad_words_dict[bad_word]}") was found {count} times.\n')
    suggestions_text.insert(tk.END, f"Total 'bad' words found: {total_bad_words}\n")

# GUI setup remains the same
window = tk.Tk()
window.title("Document Scan for Bad Words")
text_input = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, width=50)
text_input.pack(pady=10)
scan_button = tk.Button(window, text="Scan Document", command=scan_document_and_suggest)
scan_button.pack(pady=5)
suggestions_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, width=50)
suggestions_text.pack(pady=10)
window.mainloop()
