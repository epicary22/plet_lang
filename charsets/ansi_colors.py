# End
END = "\x1b[0m"

# Light
RED = "\x1b[38;2;255;0;0m" 
YEL = "\x1b[38;2;255;255;0m" 
GRE = "\x1b[38;2;0;255;0m" 
CYA = "\x1b[38;2;0;255;255m" 
BLU = "\x1b[38;2;0;0;255m" 
MAG = "\x1b[38;2;255;0;255m" 
WHI = "\x1b[38;2;255;255;255m" 
BLA = "\x1b[38;2;0;0;0m" 

# Dark
DRED = "\x1b[38;2;80;0;0m" 
DYEL = "\x1b[38;2;80;80;0m" 
DGRE = "\x1b[38;2;0;80;0m" 
DCYA = "\x1b[38;2;0;80;80m" 
DBLU = "\x1b[38;2;0;0;80m" 
DMAG = "\x1b[38;2;80;0;80m" 
DWHI = "\x1b[38;2;80;80;80m" 
DBLA = "\x1b[38;2;0;0;0m" 

ANSI_COLORS = {
    "0000": DBLA,
    "0001": DBLU,
    "0010": DGRE,
    "0011": DCYA,
    "0100": DRED,
    "0101": DMAG,
    "0110": DYEL,
    "0111": DWHI,
    "1000": BLA,
    "1001": BLU,
    "1010": GRE,
    "1011": CYA,
    "1100": RED,
    "1101": MAG,
    "1110": YEL,
    "1111": WHI,
    "END": END
}