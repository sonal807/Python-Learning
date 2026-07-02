#Store following word meanings in python dictionary:
# table: "a peice of furniture", "list of facts and figures"
# cat: "a small animal"
meaning = {
    "table": ["a peice of furniture", "list of facts and figures"],
    "cat": "a small animal"
}
print(meaning)
print(meaning.keys())
print(meaning.values())
print(meaning.items())
print(meaning.get("table"))
meaning.update({"dog": "a domestic animal"})
print(meaning)