def garland(phrase):
    for i in range(1, len(phrase)):
        if phrase[:i] == phrase[-i:]:
            return i
    return 0

print("Programmer: ", garland("programmer"))
print("Ceramic: ", garland("ceramic"))
print("Onion: ", garland("onion"))
print("Alftalft: ", garland("alftalft"))
