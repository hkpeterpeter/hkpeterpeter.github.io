lines = """\
content = "He is always willing to teach even I am very stupid. And he is very devoted into his work that he is always approachable even on Sundays. He is also able to reply queries efficiently."
course = "COMP104 (former COMP2011)"
section = "T1A"
semester = "Fall 09/10"
report = "COMP104_T1A_Fall0910.pdf"
"""

print("{")
for line in lines.split("\n"):
    tokens = line.split("=")
    if len(tokens) > 1:
        token_key = tokens[0].strip() 
        if len(tokens) == 3:
            token_value = (tokens[1] + "=" + tokens[2]).strip()
        else:
            token_value = tokens[1].strip()
        #print(token_key, token_value) 
        result = "".join(['"', token_key, '"', " : ", token_value, ","])
        print(result)
print("},")