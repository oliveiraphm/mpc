a = "string"
hash(a)

b = ["list", "of", "strings"]
hash(b)

import_details = [
 ('Chapter_12.ch12_r01', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r02', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r03', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r04', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r05', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r06', ['typing', 'textwrap', 'pathlib']),
 ('Chapter_12.ch12_r07', ['typing', 'Chapter_12.ch12_r06', 'Chapter_12.ch12_r05', 'concurrent']),
 ('Chapter_12.ch12_r08', ['typing', 'argparse', 'pathlib']),
 ('Chapter_12.ch12_r09', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r10', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r11', ['typing', 'pathlib']),
 ('Chapter_12.ch12_r12', ['typing', 'argparse'])
 ]


all_imports = set()

for item, import_list in import_details:
     for name in import_list:
         all_imports.add(name)
all_imports == {'Chapter_12.ch12_r06', 'textwrap', 'Chapter_12.ch12_r05', 'pathlib', 'concurrent', 'argparse', 'typing'}
sorted(all_imports)

names = {name
     for item, import_list in import_details
         for name in import_list}
names ==  {'Chapter_12.ch12_r06', 'Chapter_12.ch12_r05', 'typing', 'concurrent', 'argparse', 'textwrap', 'pathlib'}


set(name
     for item, import_list in import_details
         for name in import_list
)

all_imports = set(name
     for item, import_list in import_details
         for name in import_list
)

all_imports == {'textwrap', 'Chapter_12.ch12_r05', 'Chapter_12.ch12_r06', 'typing', 'pathlib', 'concurrent', 'argparse'}

sorted(all_imports)



import sys
v1 = 7
v2 = 7+sys.hash_info.modulus


hash(v1)
hash(v2)


collection = {1}
collection

item = 3
collection.union({item})

collection


collection = collection | {item}
collection

collection.update({4})
collection