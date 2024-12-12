""" String Methods & Built-In Functions """


# len() returns the Length of the String.
str1="Hello World"
print(len(str1))


# title() method return the string with first letter of every word in string uppercase and rest in lowercase.
str2="hello WORLD"
print(str2.title())

a=str2.title()
print(a)


# lower() method return the string with all uppercase converted to lowercase.
str3="HELLO WORLD"
a=str3.lower()
print(a)


# upper() method return the string with all lowercase converted to uppercase.
str4="hello world"
a=str4.upper()
print(a)


# count() method in Python is used to count the occurrences of a specified value in a string or a list.
str5="Hello World! Hello Hello"

a=str5.count("Hello",12,25)
print(a)

a=str5.count("Hello")
print(a)


# find() method in Python is used to locate the first occurrence of a specified substring within a string. It returns the index of the first occurrence or -1 if the substring is not found.
print(str5.find("Hello",10,20))
print(str5.find("Hello",15,25))
print(str5.find("Hello"))
print(str5.find("Hee"))


# index() method same as find() but raises error if substring not present.
print(str5.index("Hello"))
'print(str5.index("Hee"))' # Raise Error


# endswith() method in Python is used to check if a string ends with a specified substring. It returns True if the string ends with the given substring and False otherwise.
print(str1.endswith("World"))
print(str1.endswith("d"))
print(str1.endswith("lo"))


# startswith() method in Python checks whether a string starts with a specified substring. It returns True if the string begins with the specified substring, and False otherwise.
print(str1.startswith("He"))
print(str1.startswith("Hee"))


# isalnum() method in Python checks if a string contains only alphanumeric characters (letters and digits) and is not empty. It returns True if all characters in the string are alphanumeric, and False otherwise.
str6="HelloWorld"
print(str6.isalnum())

str7="HelloWorld2"
print(str7.isalnum())

str8="2123"
print(str8.isalnum())

str9="HelloWorld!!!"
print(str9.isalnum())


# islower() method in Python is used to check if all the characters in a string are lowercase. It returns True if all alphabetic characters in the string are lowercase, and False otherwise.
print(str4.islower())

stry="hello 1234"
print(stry.islower())

strz="hello ??"
print(strz.islower())

strw="1234"
print(strw.islower())

strx="Hello World"
print(strx.islower())


# isupper() method in Python is used to check if all the alphabetic characters in a string are uppercase. It returns True if all alphabetic characters are uppercase, and False otherwise.
stra="HELLO WORLD!"
print(stra.isupper())

strb="HELLO 1234"
print(strb.isupper())

print(strw.isupper())

print(strx.isupper())


# isspace() method in Python is used to check if all characters in a string are whitespace characters. It returns True if the string contains only whitespace characters (spaces, tabs, newlines, etc.) and is not empty; otherwise, it returns False.
strc="  \n \t \r"
print(strc.isspace())
strd="Hello \n \t"
print(strd.isspace())


# istitle() method in Python checks if a string is in title case. A string is considered in title case if the first character of each word is capitalized, and all other characters in each word are lowercase.
print(str1.istitle())
print(str2.istitle())


# lstrip() method in Python is used to remove leading whitespace characters (or characters specified by the user) from the left side of a string. It does not affect the string’s content on the right side.
stre="     Hello World!"
print(stre.lstrip())

strf="     Hello World!   g"
print(strf.lstrip())


# rstrip() method in Python is used to remove trailing whitespace characters (or characters specified by the user) from the right side of a string. It does not affect the string’s content on the left side.
str1="     Hello World!       "
print(str1.lstrip())


# strip() method in Python is used to remove leading and trailing whitespace characters (or characters specified by the user) from both ends of a string. It does not affect the characters in the middle of the string.
str1="     Hello World!        "
print(str1.lstrip())


# replace() method in Python is used to replace a specified substring with another substring in a string. It can be used to modify parts of a string without altering the original string itself, as replace() returns a new string with the replacements.
strg="Hello World!"
a=strg.replace("!","")
print(a)


# join() method in Python is used to concatenate the elements of an iterable (like a list, tuple, or string) into a single string, with a specified separator placed between each element. This method is commonly used for joining elements of a sequence into a string.
str12="HelloWorld"
ax="-"
print(ax.join(str12))


# partition() method in Python is used to split a string into three parts based on the first occurrence of a specified separator. It divides the string into a tuple of three elements: the part before the separator, the separator itself, and the part after the separator.
strj="India is a Great Country."
ay=strj.partition("is")
print(ay)


strj="India is a Great Country."
ay=strj.partition("are")
print(ay)


# split() method in Python is used to split a string into a list of substrings based on a specified delimiter (separator). It is one of the most commonly used methods for breaking down a string into smaller parts.
a=strj.split()
print(a)

a=strj.split("a")
print(a)
