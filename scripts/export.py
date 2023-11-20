from anki.storage import Collection
from os import mkdir, getcwd
from os.path import isdir, isfile, expanduser
from anki.collection import DeckIdLimit
from hashlib import sha256
from sys import argv

dry_run = False

avoid_exporting = ["Card Types", "Advanced English Vocabulary"]

if "-d" in argv or "--dry-run" in argv:
    dry_run = True


class MyCol(Collection):
    def __init__(self, path):
        Collection.__init__(self, path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def main():
    with MyCol(expanduser("~/.local/share/Anki2/Redclem/collection.anki2")) as col:

        hashes_c = {}
        modified = {}

        for noteid in col.find_notes(""):
            note = col.get_note(noteid)
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
                if len(spl) >= 2:
                    hashes_i[spl[0]] = spl[1]

        decks_n_i = col.decks.all_names_and_ids()

        def exists_or_create(pth):
            if not isdir(pth):
                mkdir(pth)

        for deck in decks_n_i:
            did = deck.id
            dname = deck.name

            if dname == "Default":
                continue

            if not (dname in hashes_i.keys() and
                    hashes_i[dname] == hashes_c[dname].hexdigest()) and dname in hashes_c.keys():
                modified[did] = True
                cdid = did
                for parent in col.decks.parents(cdid):
                    cdid = parent["id"]
                    modified[cdid] = True

        for deck in decks_n_i:
            did = deck.id
            dname = deck.name

            tokens = dname.split("::")
            filename = tokens.pop()
            
            if filename in avoid_exporting:
            	print("Avoiding marked deck {}".format(filename))
            	continue

            path = getcwd()
            exists_or_create(path)

            for i in tokens:
                path += '/'
                path += i
                exists_or_create(path)

            path += '/' + filename + ".csv"

            lim = DeckIdLimit(did)

            if did in modified.keys():
                print("Exporting {}".format(filename))
                if not dry_run:
                    col.export_note_csv(out_path=path, limit=lim, with_html=False, with_tags=False, with_deck=True, with_notetype=True, with_guid=False)
            else:
                print("Skipping {}".format(filename))

        if not dry_run:
            with open("hashes.txt", "w") as f:
                for k, v in hashes_c.items():
                    f.write(str(k) + '|' + v.hexdigest() + ';')


main()
