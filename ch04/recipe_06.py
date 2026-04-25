week = 13
day = 2
hour = 7
minute = 53
second = 19

t_s = (((week*7+day)*24+hour)*60+minute)*60+second
t_s
8063599

t_s = 8063599
fields = []
for base in 60, 60, 24, 7:
    t_s, f = divmod(t_s, base)
    fields.append(f)
fields.append(t_s)
fields
[19, 53, 7, 2, 13]


fields_copy1 = fields.copy()
fields_copy1.reverse()
fields_copy1

fields_copy2 = fields[::-1]
fields_copy2

fields_copy3 = list(reversed(fields))
fields_copy3
