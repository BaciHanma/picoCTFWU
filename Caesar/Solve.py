import string


key = string.ascii_letters

def show_result(ciphertext):
    for i in range(1,26):
        result = ''
        for l in ciphertext:
            result += key[(key.index(l) + i) % len(key)]
        print(result)

print(show_result('ynkooejcpdanqxeykjrbdofgkq'))