# This product is released under version 3 of the UK Open Government Licence, see here for details: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

__This is a test of options for sharing resources for countries implementing ICD-11. It will definitely go away in a few days, and its content only works on my machine for now, so you really don't want to use it!__

# Instructions for use

This repository has 2 sections:

## Data
Individual files that are combined to create a dictionary. You can use these files individually by importing them into an Access (or other) database, editing them as you need. Or you can use the Python script to build a dictionary for you (currently only in Access)...

## Src
Python code to build a dictionary in Access using all the supplied files.
- This is destructive - it deletes most of the data in your dictionary before importing the files, so be careful!
- All the files supplied need to be available, otherwise you'll have an incomplete dictionary
- The target database must be closed before running, otherwise bad things happen
- Run using python build.py <name and location of database>

# Caveats:
- This ICD-11 English dictionary is developed by ONS based of cause of deaths occurred in England and Wales.
- It is shared free of charge to aid Iris testing and ICD-11 development work in other English-speaking countries
- It's an ongoing work, the dictionary will be updated as and when deemed necessary by ONS, which does not commit to updating it at regular intervals.
- ONS will not offer support to other countries in terms of responding to queries, adding ad hoc entries, amending codes to suit a specific country need, etc.
- If you find a code or standardisation that you believe is universally wrong, please log an issue (note: process TBD).
- As you are free to copy, adapt and re-distribute this product, you should consider forking this repository and customising it to suit your needs.
