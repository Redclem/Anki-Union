# A lancer dans la console de debug Anki (Ctrl + :)

math_fun = ["sin", "cos", "tan", "arcsin", "arctan", "arccos", "sh", "ch", "th", "ln"]

for mod in mw.col.models.all_names_and_ids():
    for nid in mw.col.models.nids(mod.id):
        note = mw.col.get_note(nid)

        for i in range(len(note.fields)):

            text = note.fields[i]

            for fun in math_fun:
                lim = 0
                idx = text.find(fun, lim)
                while idx != -1:
                    if idx > 0 and text[idx-1] != '\\' and text[idx - 6:idx] != "\\text{" and (not text[idx-1].isalnum()):
                        text = text[:idx] + "\\text{" + fun + "}" + text[idx+len(fun):]
                    lim = idx + 8 + len(fun)
                    idx = text.find(fun, lim)

            note.fields[i] = text
        note.flush()
