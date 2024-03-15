# def steps_to_convert(string):
#     rezalt = 0
#     rezalt1 = 0
#     for x in string:
#         if x.count(x.lower()) == 1:
#             rezalt += 1
#         elif x.count(x.upper()) == 1:
#             rezalt1 += 1
#     if rezalt1 < rezalt:
#         return rezalt1
#     else:
#         return rezalt
#
# print(steps_to_convert("abC"))
# print(steps_to_convert("abCBA"))
# print(steps_to_convert("aba"))
# print(steps_to_convert("abaCCC"))

# 1-masala
# def double_char(string):
#     i = 0
#     while i < len(string):
#         x = string[i]
#         q = x * 2
#         print(q)
#         i += 1
#
# double_char("String")
# double_char("Hello World!")

# 2-masala
# def index_of_caps(letter):
#     i = 0
#     while i < len(letter):
#         x = letter[i]
#         if x.isupper() is True:
#             print(x)
#             q = letter.index(x)
#             print(q)
#         i += 1
#
# index_of_caps("eDaBiT")
# index_of_caps("eQuINoX")

# 3-masala
# def filter_list(num):
#     i = 0
#     while i < len(num):
#         x = num[i]
#         if type(x) == int:
#             print(x)
#         i += 1
#
#
# filter_list([1, 2, 3, "a", "b", 4])
# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"])

# 4-masala
# def alphabet_soup(alphabet):
#     a = sorted(alphabet)
#     print(a)
#
# alphabet_soup("hello")
# alphabet_soup("edabit")
# alphabet_soup("hacker")
# alphabet_soup("geek")
# alphabet_soup("javascript")

# 5-masala
# def is_isogram(string):
#     a = ""
#     i = 0
#     while i < len(string):
#         x = string[i]
#
#         i += 1
#
# is_isogram("Algorism")

# 6-masala
# def convert_to_decimal(numstr):
#     lst = []
#     i = 0
#     while i < len(numstr):
#         x = numstr[i]
#         rep = x.replace("%" , " ")
#         a = int(rep)
#         w = a/100
#         r = lst.append(w)
#         print(lst)
#         i += 1
#
#
# convert_to_decimal(["1%", "2%", "3%"])

# 7-masala
# def count_palindromes(polindrom):
#     lst = []
#     i = 0
#     while i < len(polindrom):
#         x = polindrom[i]
#         a = str(x)
#         if a == a[::-1]:
#             lst.append(a)
#         i += 1
#     print(len(lst))
#
# count_palindromes(list(range(878 , 898 + 1)))

# 8-masala
# def greet_people(name):
#     i = 0
#     while i < len(name):
#         x = name[i]
#         a = "Salom "
#         y = a + x
#         print(y)
#         i += 1
# greet_people(["Joe"])
# greet_people(["Angela", "Joe"])
# greet_people(["Frank", "Angela", "Joe"])\

# 9-masala
# def remove_vowels(vowel):
#     a = "aouie"
#     i = 0
#     while i < len(vowel):
#         x = vowel[i]
#         i += 1
#         if x in a:
#             # print(x)
#             w = vowel.replace(x ,"")
#     print(w)
#
# remove_vowels("I have never seen a thin person drinking Diet Coke.")
# remove_vowels("We're gonna build a wall!")







# 10-masala
# def integer_boolean(falstru):
#     i = 0
#     while i < len(falstru):
#         x = falstru[i]
#         # print(x)
#         i += 1
# integer_boolean("10")