def directionToString(self):
    switcher = {
        0: "rechts",
        1: "links",
        2: "runter",
        3: "hoch"
    }
    return(switcher.get(self, "Invalid direction"))