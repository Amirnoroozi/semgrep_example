import re
redos = r"^(a+)+$"
regex = r"^[0-9]+$"
data = "foo"
# ruleid: regex_dos
pattern = re.compile(redos)
pattern.search(data)
# ok: regex_dos
pattern = re.compile(regex)
pattern.match(data)
pattern.fullmatch(data)
pattern.split(data)
pattern.findall(data)
pattern.escape(redos)
pattern.purge()
