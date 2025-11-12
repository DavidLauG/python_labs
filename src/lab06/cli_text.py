import argparse
from pathlib import Path
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import *
from lab04.io_txt_csv import read_text

def main():
    parser=argparse.ArgumentParser(description="CLI-utilitary lab06")
    subparser=parser.add_subparsers(dest="command")

    cat_parser=subparser.add_parser("cat", help="Display file contents")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Line Numbers")

    stats_parser=subparser.add_parser("stats", help="Word frequencies")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args=parser.parse_args()
    try:
        if args.command=="cat" or args.command=="stats":
            file=Path(args.input)
        if args.command=="cat":
            """Executes the cat command"""
            with file.open('r', newline='', encoding='utf-8') as txt_file:
                count = 1
                for line in txt_file:
                    s = line.rstrip()
                    if args.n:
                        s = f'{count}: {s}'
                        count += 1
                    print(s)
        elif args.command=="stats":
            """Executes the stats command"""
            text=read_text(file) ##Funcão para ler o ficheiro pretendido
            if not text:
                print(f"File {file} is empty")
            else:
                texto_norma=normalize(text)
                tok=tokenize(texto_norma)
                contar=count_freq(tok)
                top=top_n(contar, args.top)
                print(f"Top-{args.top}:")
                for word, count in top:
                    print(f"{word}:{count}")
        else:
            parser.print_help()
    except FileNotFoundError:
        print(f"Error: File {file} not found")
if __name__=="__main__":
    main()