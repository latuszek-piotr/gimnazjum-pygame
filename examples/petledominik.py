zdanie = "Nie lubie chodzic do szkoly"
print zdanie
obrot_petli = 0
for litera in zdanie:
    obrot_petli = obrot_petli + 1
    print "%s: litera = %s" % (obrot_petli, litera * obrot_petli)
