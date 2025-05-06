filename = "dev/docs/tests.md"

heading = """<h1 align="center" style="font-weight: bold">
    Tests
</h1>\n\n"""

with open(filename, "r+", encoding="utf-8") as f:
    original = f.read()
    f.seek(0)
    f.write(heading + original)