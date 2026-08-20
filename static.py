class Chai:
    def clean(text):
        return [items.strip() for items in text.split(",")]
raw = "water  , ginger, milk   ,  honey"
cleaned = Chai.clean(raw)
print(cleaned)