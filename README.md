# Displacement Cipher Suite - Encryption & Decryption Tool

## 📌 Project Overview

This is a **cryptography tool** I developed at age 17 for my high school computer science project. It implements multiple cipher-breaking algorithms to decrypt messages encrypted with a simple displacement cipher (Caesar cipher variant), along with encryption capabilities.

**⚠️ Note:** This was my early programming work - the code may contain unconventional practices, but it fully demonstrates the core cryptographic concepts I was learning at the time.

---

## 🔐 What It Does

The application provides both **encryption** and **decryption** functionality through a Tkinter GUI. It supports three different decryption methods that automatically crack displacement ciphers without needing to know the shift key:

### Decryption Methods

| Method | Description |
|--------|-------------|
| **Dictionary Method** | Uses a 100k word frequency dictionary from Wiktionary to find the shift that produces the most valid English words |
| **Letter Frequency Method** | Analyzes character frequency distribution (English letter frequency: 'E' is most common) to determine the shift |
| **Sequence Method** | A custom sequence-based encryption/decryption where the shift changes with each character position |

### Encryption Methods

| Method | Description |
|--------|-------------|
| **Standard Displacement** | Traditional Caesar cipher (shift K positions, mod 26) |
| **Sequence Encryption** | Position-dependent shifting (shift = position index, loops 1-26) |

---

## 🚀 How to Run

### Prerequisites
- Python 3.x
- Required libraries: `tkinter`, `chardet`, `matplotlib`

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/displacement-cipher-suite.git
cd displacement-cipher-suite

# Install dependencies (if needed)
pip install chardet matplotlib
```

### Run the Application

```bash
python mainUI.py
```

The GUI will launch with two main tabs:
- **Encryptor** - Upload text files and encrypt them
- **Decryptor** - Upload ciphertext and automatically crack the encryption

---

## 🧠 How It Works

### 1. Dictionary Method
- Converts ciphertext to ASCII values
- Tests all 26 possible shifts
- For each shift, splits text into potential words and checks against a preloaded dictionary
- Selects the shift that yields the highest percentage of recognized words

### 2. Letter Frequency Method
- Counts character frequencies in the ciphertext
- In English, 'E' is the most common letter (approximately 12.7%)
- Finds the shift that would make the most frequent ciphertext character map to 'E'

### 3. Sequence Method (M2O / M2P)
- Special encryption where shift = position index (1-26, looping)
- M2O: incremental shift (increasing with each character)
- M2P: decremental shift (decreasing with each character)

---

## 📊 Features

- ✅ Upload text files (auto-detects encoding with `chardet`)
- ✅ Real-time preview of encrypted/decrypted text
- ✅ K-value adjustment slider for manual override
- ✅ Matplotlib charts showing frequency distributions
- ✅ Save results to original file or new location
- ✅ Bilingual comments (Chinese/English) in source code

---

## 🔧 Technical Details

- **GUI Framework:** Tkinter
- **Encoding Detection:** chardet library
- **Data Visualization:** matplotlib
- **Dictionary Source:** Wiktionary Frequency Lists (http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)
- **Algorithm Complexity:** O(n) for dictionary method, O(26n) for full search

---

## 🧪 Test Cases

The repository includes test files:
- `TEST CASE 00` - Full text of "Harry Potter and the Sorcerer's Stone" (Chapter 1-17) - excellent for frequency analysis testing
- `TEST CASE 01` - Short examples including "HELLO WORLD" and "KILLER QUEEN"
- `try try.txt` - Simple "TRY THIS" test

---

## 📝 Notes from the Developer

This project was created when I was 17 years old as a high school assignment. Looking back, I can see many areas for improvement:
- The code could be more modular and follow better practices
- Error handling is minimal
- Some functions are overly complex
- Chinese/English mixed comments

However, the algorithms work correctly, and the project taught me valuable lessons about:
- Cryptanalysis fundamentals
- GUI development with Tkinter
- File I/O and encoding handling
- Data visualization for debugging

**I'm keeping this repository as-is to document my learning journey.** Feel free to explore, learn from it, or laugh at my 17-year-old coding style!

---

## 📄 License

This project is for educational purposes. Feel free to use it as a reference for learning cryptography concepts.

---

## 🙏 Acknowledgments

- Wiktionary for the frequency word list
- My high school teacher who assigned this project
- Stack Overflow (where I learned 90% of my debugging skills at 17)

---

*Built with 🐍 Python and teenage determination.*
