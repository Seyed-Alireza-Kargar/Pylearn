import pysynth as ps
notes = [("c", 4), ("c", 4), ("g", 4), ("g", 4),
         ("a", 4), ("a", 4), ("g", 2),
         ("f", 4), ("f", 4), ("e", 4), ("e", 4),
         ("d", 4), ("d", 4), ("c", 2),
         ("g", 4), ("g", 4), ("f", 4), ("f", 4),
         ("e", 4), ("e", 4), ("d", 2),
         ("g", 4), ("g", 4), ("f", 4), ("f", 4),
         ("e", 4), ("e", 4), ("d", 2),
         ("c", 4), ("c", 4), ("g", 4), ("g", 4),
         ("a", 4), ("a", 4), ("g", 2),
         ("f", 4), ("f", 4), ("e", 4), ("e", 4),
         ("d", 4), ("d", 4), ("c", 2)]

ps.make_wav(notes, fn = "test.wav")