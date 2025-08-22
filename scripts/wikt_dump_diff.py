#!/usr/bin/env python3
import argparse
import bz2
import xml.etree.ElementTree as ET

def iter_titles(dump_path):
    with bz2.open(dump_path, "rb") as f:
        for event, elem in ET.iterparse(f, events=("end",)):
            if elem.tag == "title":
                yield elem.text
            elem.clear()

def diff_dumps(old_dump, new_dump, output):
    old = set(iter_titles(old_dump))
    new = set(iter_titles(new_dump))
    with open(output, "w", encoding="utf-8") as out:
        out.write("=== Ajoutés ===\n")
        for t in sorted(new - old):
            out.write(f"{t}\n")
        out.write("\n=== Supprimés ===\n")
        for t in sorted(old - new):
            out.write(f"{t}\n")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Diff entre deux dumps Wiktionnaire")
    p.add_argument("ancien")
    p.add_argument("nouveau")
    p.add_argument("sortie")
    args = p.parse_args()
    diff_dumps(args.ancien, args.nouveau, args.sortie)
