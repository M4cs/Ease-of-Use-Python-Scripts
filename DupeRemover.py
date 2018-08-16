class header:
    banner = """
    DupeRemover by Macs


    Version: 1.0
    Description: Remove duplicate combinations from your Combo lists.
    Works with 1 line, 1 combo format lists.

    Instructions:

    1. Start the program by entering a lowercase y when prompted.
    2. Input file name of Combolist (don't include .txt)
    3. Input the name of a file you'd like to output your new list to.*
    *you can use the same file as your combolist but it will overwrite.

    More Info:
    If you have issues feel free to contact me on Discord: @macs#0420!
    """

print header.banner

try:
    userinput = raw_input("Please read the instructions before starting. Would you like to start the program? [y]/[n] ")
    if str("y") in userinput:
        try:
            combolist = raw_input("\nName of Combolist: ") + ".txt"
            print "\nReading Combolist..."
            combolistp = open(combolist,"r").readlines()

        except IOError,KeyError:
            print "\n[*] Something went wrong.. did you put the right file name in? [*]"
            exit()
    if str("y") not in userinput:
        print "\nUser cancelled running the program. If this was a mistake please make sure you \nuse a lowercase n."
        exit()
except IndexError:
    pass

lines = len(str(combolistp))

try:
    for i in range(0,lines):
        parsedcombo = combolistp[i].strip("\r\n")

except IndexError:
    pass

print "\n[*] Loaded Combos: " + str(len(combolistp))

try:
    outputfile = raw_input("\nName of File to Output: ") + ".txt"
    print "\nRemoving Duplicates.."
    lines_seen = set()
    outfile = open(outputfile,"w")
    for line in open(combolist,"r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    print "[*] Number of Combos Remaining After Duplication Removal: " + str(len(lines_seen))
except NameError:
    print "Invalid Syntax"

print "\n\nDuplication Removal Completed. Happy Cracking :)"
