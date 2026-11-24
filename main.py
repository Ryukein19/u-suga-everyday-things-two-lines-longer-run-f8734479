import os
# Two-line entry (255 chars): the lines below are the whole submission.
# Writes to /output/entry.txt.
LINE = "A traffic jam is like a line of ants carrying crumbs, except every ant is in a hurry and none of them knows where the picnic is.\nIt works because both are slow, crowded lines moving one crumb at a time — but it leaves out the honking, which ants never do."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
