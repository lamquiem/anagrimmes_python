#!/usr/bin/env python3
import argparse
import bz2
import xml.etree.ElementTree as ET

def generate_articles_list(dump_file, list_output):
    with bz2.open(dump_file, "rb") as f, open(list_output, "w", encoding="utf-8") as out:
        for event, elem in ET.iterparse(f, events=("end",)):
            if elem.tag == "title":
                out.write(elem.text + "\n")
            elem.clear()

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Extrait la liste des articles")
    p.add_argument("dump")
    p.add_argument("liste_sortie")
    args = p.parse_args()
    generate_articles_list(args.dump, args.liste_sortie)
