#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET
from wiktextract import WiktionaryConfig, WiktionaryExtractor

def create_xml(dump_file, xml_output):
    cfg = WiktionaryConfig()
    ext = WiktionaryExtractor(cfg)
    root = ET.Element("dictionnaire")
    for entry in ext.extract(dump_file):
        e = ET.SubElement(root, "entry", mot=entry.word)
        for pron in entry.pronunciations or []:
            ET.SubElement(e, "pron", valeur=pron)
    tree = ET.ElementTree(root)
    tree.write(xml_output, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Génère un XML ‘dico’ depuis un dump")
    p.add_argument("dump")
    p.add_argument("xml_sortie")
    args = p.parse_args()
    create_xml(args.dump, args.xml_sortie)
