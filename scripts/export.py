from anki.storage import Collection
from os import mkdir, getcwd
from os.path import isdir, isfile
from anki.collection import DeckIdLimit
from hashlib import sha256

class MyCol(Collection):
    def __init__(self, path):
        Collection.__init__(self, path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()



with MyCol("/home/redclem/.local/share/Anki2/Utilisateur 1/collection.anki2") as col:

    hashes_c = {}
    
    for noteid in col.find_notes(""):
        note = col.get_note(noteid)
        if len(note.cards()) == 0: continue
        did = note.cards()[0].current_deck_id()
        dname = col.decks.name(did)

        if dname not in hashes_c.keys():
            hashes_c[dname] = sha256()

        for f in note.fields:
            hashes_c[dname].update(f.encode())

    hashes_i = {}
    if isfile("hashes.txt"):
        with open("hashes.txt", "r") as file:
            data = file.read()

        for tok in data.split(";"):
            if tok == "": continue
            spl = tok.split("|")
            hashes_i[spl[0]] = spl[1]
    
    decks_n_i = col.decks.all_names_and_ids()

    def exists_or_create(path):
        if not isdir(path):
            mkdir(path)

    for deck in decks_n_i:
        did = deck.id
        dname = deck.name

        tokens = dname.split("::")
        filename = tokens.pop()

        path = getcwd()
        exists_or_create(path)

        for i in tokens:
            path += '/'
            path += i
            exists_or_create(path)

        path += '/' + filename + ".apkg"

        lim = DeckIdLimit(did)

        if dname in hashes_i.keys() and hashes_i[dname] == hashes_c[dname].hexdigest():
            print("Skipping {}".format(filename))
        elif dname in hashes_c.keys():
            print("Exporting {}".format(filename))
            #col.export_anki_package(out_path=path, limit=lim, with_scheduling=False, with_media=False, legacy_support=False)


    with open("hashes.txt", "w") as f:
        for k,v in hashes_c.items():
            f.write(str(k) + '|' + v.hexdigest() + ';')
