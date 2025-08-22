#!/usr/bin/env python3
import argparse
import os
import csv
import json
from wikitextprocessor import Wtp
from wiktextract import parse_wiktionary
from wiktextract.wxr_context import WiktextractContext
from wiktextract.config import WiktionaryConfig
 
def extract_tables(dump_file, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    pron_path = os.path.join(out_dir, "prononciations.csv")
    with open(pron_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["mot", "pron"])

        def word_cb(data):
            # Ne conserver que les mots français
            if data.get("lang_code") == "fr":
                mot = data.get("word")
                for sound in data.get("sounds", []):
                    ipa = sound.get("ipa")
                    if ipa:
                        writer.writerow([mot, ipa])

        # 1) Création du contexte d’extraction (Wtp + config)
        # On capture uniquement le français et les prononciations
        config = WiktionaryConfig(
            ump_file_lang_code="fr",
            capture_language_codes=["fr"],
            capture_pronunciation=True,
            capture_translations=False
        )  # :contentReference[oaicite:0]{index=0}
        ctx = WiktextractContext(Wtp(), config)

        # 2) parse_wiktionary appelle word_cb(data) pour chaque entrée
        class OutWrapper:
            def __init__(self, cb):
                self.cb = cb
            def write(self, line):
                self.cb(json.loads(line))

        # parse_wiktionary(ctx, dump_path, num_processes, phase1_only,
        #                  namespace_ids, out_f, human_readable=False, ...)
        parse_wiktionary(
            ctx,
            dump_file,
            num_processes=1,
            phase1_only=False,
            namespace_ids={0},
            out_f=OutWrapper(word_cb)
        )  # :contentReference[oaicite:1]{index=1}

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Extrait les prononciations (CSV) depuis un dump Wiktionnaire"
    )
    p.add_argument("dump", help="Chemin vers frwiktionary-…xml.bz2")
    p.add_argument("repertoire_sortie", help="Dossier où écrire le CSV")
    args = p.parse_args()
    extract_tables(args.dump, args.repertoire_sortie)
