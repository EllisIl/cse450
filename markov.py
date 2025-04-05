import random
import sys
from collections import defaultdict

def build_markov_chain(text, n=2):
    """Builds a Markov chain from the given text with n-grams."""
    markov_chain = defaultdict(list)
    words = text.split()
    
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        markov_chain[key].append(next_word)
    
    return markov_chain

def generate_text(chain, length=50, n=2):
    """Generates text using the Markov chain."""
    if not chain:
        return "No data in Markov Chain"
    
    key = random.choice(list(chain.keys()))
    generated_words = list(key)
    
    for _ in range(length - n):
        if key not in chain:
            key = random.choice(list(chain.keys()))  # Restart with a new key if stuck
        next_word = random.choice(chain[key])
        generated_words.append(next_word)
        key = tuple(generated_words[-n:])
    
    return ' '.join(generated_words)

def main(filename, length=50, n=2):
    """Reads an input file, builds a Markov chain, and generates text."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().replace('\n', ' ')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    
    chain = build_markov_chain(text, n)
    generated_text = generate_text(chain, length, n)
    print(generated_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markov.py <filename> [length] [n-gram]")
    else:
        filename = sys.argv[1]
        length = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 2
        main(filename, length, n)