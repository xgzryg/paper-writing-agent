"""Build a normalized JSON index from 2025IF.xlsx for fast lookup.

This script is part of the journal-if-lookup skill and lives at the skill
root. It reads only <skill>/data/2025IF.xlsx.

Output: <skill>/data/journals_index.json
"""
import json
import os
import re
import sys
from collections import defaultdict
import openpyxl

# Resolve paths relative to this script's location so the script is
# location-independent.
SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SKILL_DIR, 'data')
os.makedirs(OUT_DIR, exist_ok=True)

CANDIDATE_SRCS = [os.path.join(SKILL_DIR, 'data', '2025IF.xlsx')]


def find_source():
    for p in CANDIDATE_SRCS:
        if os.path.exists(p):
            return p
    raise FileNotFoundError(
        'Could not find 2025IF.xlsx. Tried:\n  ' + '\n  '.join(CANDIDATE_SRCS)
    )


def normalize_text(s):
    if s is None:
        return ''
    s = str(s).upper()
    s = re.sub(r'[^A-Z0-9 ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def normalize_issn(s):
    if s is None:
        return ''
    return re.sub(r'[^0-9X]', '', str(s)).upper()


def acronym_of(name_norm):
    """Build acronym from a normalized uppercase journal name.

    Rules: take first letter of each word; for hyphenated compounds, take first
    letter of each segment; ignore tiny words ('J', 'OF', 'THE', 'AND', 'AN',
    'A', 'IN', 'ON', 'FOR', 'TO', '&') from the start? We keep them so that
    'JAMA' (Journal of the American Medical Association) still works.
    """
    # normalized name uses single spaces
    words = name_norm.split()
    # Split hyphenated words further
    parts = []
    for w in words:
        for sub in w.split('-'):
            if sub:
                parts.append(sub)
    acr = ''.join(p[0] for p in parts if p)
    return acr


def main():
    src = find_source()
    print(f'Loading workbook: {src}')
    wb = openpyxl.load_workbook(src, data_only=True)
    ws = wb['Journals']
    headers = [c.value for c in ws[1]]

    journals = []
    acronym_index = defaultdict(list)  # acronym -> [journal_idx, ...]
    issn_index = {}  # issn -> journal_idx
    eissn_index = {}
    name_norm_index = {}  # normalized name -> journal_idx (first hit only; we keep all but use first)
    abbr_norm_index = {}

    for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True)):
        if not row or not row[1]:
            continue
        d = dict(zip(headers, row))
        # Build a compact record — keep fields that are useful for display
        rec = {
            'rank': d.get('Rank'),
            'name': d.get('Journal name'),
            'abbr': d.get('Abbreviated journal'),
            'publisher': d.get('Publisher'),
            'issn': d.get('ISSN'),
            'eissn': d.get('eISSN'),
            'categories': d.get('Categories'),  # may be 'Multiple' or a single string
            'editions': d.get('Editions'),
            'jcr_year': d.get('JCR year'),
            'jif': d.get('2025 JIF'),
            'jif_5y': d.get('5-year JIF'),
            'jif_no_self': d.get('JIF without self cites'),
            'jif_quartile': d.get('JIF quartile'),
            'jif_percentile': d.get('JIF percentile'),
            'jif_rank': d.get('JIF rank'),
            'jci': d.get('JCI'),
            'jci_quartile': d.get('JCI quartile'),
            'jci_percentile': d.get('JCI percentile'),
            'jci_rank': d.get('JCI rank'),
            'total_citations': d.get('Total citations'),
            'total_articles': d.get('Total articles'),
            'citable_items': d.get('Citable items'),
            'pct_oa_gold': d.get('% OA gold'),
            'immediacy_index': d.get('Immediacy index'),
            'eigenfactor': d.get('Eigenfactor'),
            'norm_eigenfactor': d.get('Normalized eigenfactor'),
            'article_influence_score': d.get('Article influence score'),
            'ais_quartile': d.get('AIS quartile'),
            'ais_rank': d.get('AIS rank'),
            'cited_half_life': d.get('Cited half-life'),
            'citing_half_life': d.get('Citing half-life'),
            'category_quartiles_json': d.get('Category quartiles JSON'),
            # internal lookups
            '_name_norm': normalize_text(d.get('Journal name')),
            '_abbr_norm': normalize_text(d.get('Abbreviated journal')),
        }
        idx = len(journals)
        journals.append(rec)

        # Index by acronym
        acr = acronym_of(rec['_name_norm'])
        if acr:
            acronym_index[acr].append(idx)
        # Also index by any all-caps token in the name (length >= 3) — this
        # covers cases like 'JAMA' in 'JAMA-JOURNAL OF THE AMERICAN MEDICAL
        # ASSOCIATION', which a strict first-letter acronym would miss.
        for token in rec['_name_norm'].split():
            tok = re.sub(r'[^A-Z0-9]', '', token)
            if len(tok) >= 3 and tok.isalpha() and tok.isupper() and re.match(r'^[A-Z]+$', tok):
                acronym_index.setdefault(tok, []).append(idx)

        # Index by ISSN
        issn_n = normalize_issn(d.get('ISSN'))
        eissn_n = normalize_issn(d.get('eISSN'))
        if issn_n and issn_n not in issn_index:
            issn_index[issn_n] = idx
        if eissn_n and eissn_n not in eissn_index:
            eissn_index[eissn_n] = idx

        # Index by normalized name (first hit wins)
        nn = rec['_name_norm']
        if nn and nn not in name_norm_index:
            name_norm_index[nn] = idx
        an = rec['_abbr_norm']
        if an and an not in abbr_norm_index:
            abbr_norm_index[an] = idx

    print(f'Indexed {len(journals)} journals')
    print(f'Unique acronyms: {len(acronym_index)}')
    print(f'Unique ISSNs: {len(issn_index)} + {len(eissn_index)} eISSN')

    out = {
        'meta': {
            'source': 'JCR 2025 release',
            'rows': len(journals),
            'note': 'Index built from 2025IF.xlsx. Do not edit by hand.',
        },
        'journals': journals,
        'index': {
            'acronym': acronym_index,
            'issn': issn_index,
            'eissn': eissn_index,
            'name_norm': name_norm_index,
            'abbr_norm': abbr_norm_index,
        },
    }
    out_path = os.path.join(OUT_DIR, 'journals_index.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
    size_mb = os.path.getsize(out_path) / 1024 / 1024
    print(f'Wrote {out_path} ({size_mb:.1f} MB)')


if __name__ == '__main__':
    main()
