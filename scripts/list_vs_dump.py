#!/usr/bin/env python3
import argparse

def list_vs_dump(list_file, dump_list_file, output):
    with open(list_file, encoding="utf-8") as f1, open(dump_list_file, encoding="utf-8") as f2:
        s1 = set(line.strip() for line in f1)
        s2 = set(line.strip() for line in f2)
    missing = s1 - s2
    with open(output, "w", encoding="utf-8") as out:
        for m in sorted(missing):
            out.write(m + "\n")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Compare une liste vs un dump")
    p.add_argument("liste")
    p.add_argument("dump_liste")
    p.add_argument("sortie")
    args = p.parse_args()
    list_vs_dump(args.liste, args.dump_liste, args.sortie)
