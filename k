'''Write add_marks(subject, mark, record=None) that returns a dictionary without the trap.

add_marks("Python", 45)  -> {'Python': 45}
add_marks("SQL", 40)     -> {'SQL': 40}'''


def add_marks(subject, mark , record = None ):
    if record is None:
        record = {}
    record[subject] = mark
    return record

print(add_marks("Python" , 45))
print(add_marks("SQL",40))