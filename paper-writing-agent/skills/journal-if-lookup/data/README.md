# Journal data

No journal metrics database is included in the public package. Keep your own permitted spreadsheet and index in your project, then pass their paths explicitly.

Build: `python build_index.py --data-file "<project>/journals.xlsx" --output "<project>/journals_index.json"`

Query: `python query.py "journal name" --data-file "<project>/journals_index.json"`

The query tool does not search old installations or load a default dataset. Without a supplied index it returns `data_unavailable`; it does not report zero matches or perform online verification itself. See the skill instructions for online verification through your agent host.
