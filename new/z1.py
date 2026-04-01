s = "String123"

print(s[::-1])

s_reversed = ""
for i in range(len(s)):
    s_reversed += s[len(s)-i-1]
print(s_reversed)

string_words = "one two three"
string_words_reversed = ""
for i in string_words.split(" ")[::-1]:
    print(i, end = " ")
    if string_words_reversed != "":
        string_words_reversed += " "
    string_words_reversed += i
print()
print(string_words_reversed)

def sumchet(m):
    return sum(i for i in m if i & 1 == 0)
print(sumchet([1,2,3,4,5,6]))