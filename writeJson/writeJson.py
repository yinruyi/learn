import json

d = [{"a": 1, "c": 3, "b": 3},{"a":2}]
with open("G:\\dev\\learn\\writeJson\\test.json", "w") as f:
	json.dump(d, f)
with open("G:\\dev\\learn\\writeJson\\test.json", "r") as f:
	d1 = json.load(f)

print d1
print type(d1)