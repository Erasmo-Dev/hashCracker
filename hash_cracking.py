import hashlib
import argparse

def crack_hash(hash, wordlist, algorithm):
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            if algorithm == 'MD5' and hashlib.md5(word.encode()).hexdigest() == hash:
                print(f"Hash cracked! The word is: {word}")
                return
            elif algorithm == 'SHA1' and hashlib.sha1(word.encode()).hexdigest() == hash:
                print(f"Hash cracked! The word is: {word}")
                return
            elif algorithm == 'SHA224' and hashlib.sha224(word.encode()).hexdigest() == hash:
                print(f"Hash cracked! The word is: {word}")
                return
            elif algorithm == 'SHA512' and hashlib.sha512(word.encode()).hexdigest() == hash:
                print(f"Hash cracked! The word is: {word}")
                return
            elif algorithm == 'SHA384' and hashlib.sha384(word.encode()).hexdigest() == hash:
                print(f"Hash cracked! The word is: {word}")  
                return
        print("No match found in the wordlist.")


def main():
    
    parser = argparse.ArgumentParser(description="Simple Hash Cracker")

    # Path to your wordlist
    parser.add_argument('wordlist', type=str, help="The path to your wordlist.")

    # The hash
    parser.add_argument('hash', type=str, help="The hash to be find.")
   
    # Algorithm choices
    parser.add_argument('-alg',  required=True, choices=['MD5', 'SHA1', 'SHA224', 'SHA256', 'SHA512', 'SHA384'], help="Chose the hash algorithm to use 'MD5', 'SHA1', 'SHA224', 'SHA256', 'SHA512', 'SHA384' Exemple: python3 hash_cracking.py wordlist.txt 5f4dcc3b5aa765d61d8327deb882cf99 -alg MD5")
    
    args = parser.parse_args()

    # Call the hash cracking function
    crack_hash(args.hash, args.wordlist, args.alg)
    

if __name__ == "__main__":
    main()