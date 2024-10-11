# hash_racker

A simple hash cracker written in Python. This tool allows you to crack various hash types using a wordlist and the specified hash algorithm.

## Features

- Supports multiple hashing algorithms: MD5, SHA1, SHA224, SHA256, SHA512, and SHA384.
- Easy to use command-line interface.
- Customizable wordlist for hashing.

## Requirements

- Python 3.x
- `argparse` (included in Python standard library)

## Installation

1. Clone this repository to your local machine:

   git clone https://github.com/Erasmo-Dev/hash_cracker.git
   cd hash-cracker

    Ensure you have Python 3.x installed.

Usage

To run the hash cracker, use the following command:

python3 hash_cracking.py <path_to_wordlist> <hash_value> -alg <algorithm>

Example

python3 hash_cracking.py wordlist.txt 5f4dcc3b5aa765d61d8327deb882cf99 -alg MD5

Arguments

    wordlist: The path to your wordlist file.
    hash: The hash value you want to crack.
    -alg: The hash algorithm to use. Choose from MD5, SHA1, SHA224, SHA256, SHA512, SHA384.
