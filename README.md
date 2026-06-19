# NIS2 Scope Checker

A step-by-step tool to determine whether your organisation is an **Essential Entity**, **Important Entity**, or out of scope under the EU **NIS2 Directive (2022/2555)**.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nis2-scope-checker.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What it does

- Walks through a structured 6-step quiz covering Member State, sector (Annex I / Annex II), subsector, and size thresholds
- Checks for **automatic in-scope triggers** (Art. 2(2)) that apply regardless of size — qualified TSPs, DNS providers, TLD registries, sole providers, CER-designated critical entities, central government bodies
- Produces an **on-screen verdict** with applicable article citations and obligations
- Generates a **downloadable Markdown scoping report**

## Scope covered

**Annex I — High Criticality Sectors**
Energy · Transport · Banking · Financial Market Infrastructures · Health · Drinking Water · Waste Water · Digital Infrastructure · ICT Service Management (B2B) · Public Administration · Space

**Annex II — Other Critical Sectors**
Postal & Courier · Waste Management · Chemicals · Food · Manufacturing · Digital Providers · Research

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploying to Streamlit Cloud

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account and select this repo
4. Set **Main file path** to `app.py`
5. Deploy — free hosting, no server required

## Disclaimer

This tool provides **indicative scoping guidance only** and does not constitute legal advice. For a definitive determination, consult your national competent authority (NCA) or qualified legal counsel. NIS2 was required to be transposed by Member States by 17 October 2024 — national transpositions may extend or modify the baseline scope set out in the Directive.

## References

- [NIS2 Directive (EU) 2022/2555 — EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022L2555)
- [ENISA NIS2 Guidance](https://www.enisa.europa.eu/topics/cybersecurity-policy/nis-directive-new)
- [NIS2 Transposition Tracker — ENISA](https://www.enisa.europa.eu/topics/cybersecurity-policy/nis-directive-new/nis2-transposition)

## License

MIT — free to use, fork, and build on.

## Author

Built by [Don Kerr](https://github.com/donalkerr) — founder of [RUN Audit](https://runaudit.ai), IT audit and GRC practitioner, New York attorney.
Contributions and issue reports welcome.
