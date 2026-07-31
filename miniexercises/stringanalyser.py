s=input("\nenter the string:\n")
s=s.lower()
total_char=len(s)
words=len(s.split())

vowels=0
consonents=0
digits=0
space=0
special=0

for i in s:
    if i in "a,e,i,o,u":
        vowels+=1
    elif i.isalpha():
        consonents+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        space+=1
    elif not i.isalnum() and not i.isspace():
        special+=1

rev=s[::-1]
pallindrome=True
state=" "

if rev==s:
    pallindrome=True
else:
    pallindrome=False

if pallindrome:
    state="YES"
else:
    state="No"

print("characters: ",total_char)
print("Words: ",words)
print("Vowels: ",vowels)
print("consonents: ",consonents)
print("digits: ",digits)
print("space: ",space)
print("special charcters: ",special)
print("Reversed: ",rev)
print("pallindrome: ",state)