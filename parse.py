import random


def hashtagParser(hashList):
    hashSplit = hashList.split('#')
    i = 0
    while i < len(hashSplit):
        if hashSplit[i] == '':
            del hashSplit[i]
        else:
            hashSplit[i] = hashSplit[i].strip()
            i += 1
    return hashSplit

hashList = "#airforce1 #airforce1mid #stuusy  #stussyairforce1mid #신발스타그램 #나이키 #스투시 #스투시포스 #스투시에어포스 #스투시에어포스1포실 #나이키스투시 #에어포스1 #에어포스1미드 #나투시 #stussynike #nikestussy #nikestyleclub #airforce1 #airforce1mid #sneakerhead #sneakerheads #airforce #kickstagram #thekickscafe #snkerskickcheck #snkrs"
insta_tag= hashtagParser(hashList)
print(insta_tag)

shuffle_tag = random.sample(insta_tag,len(insta_tag))
print(insta_tag)


