from collections import defaultdict

""" {1: ["j", "s"],
     2: ["p", "x"],} """

mydict = defaultdict(list)
mydict[1].append("j")
mydict[1].append("s")

mydict[2].append("p")
mydict[2].append("x")