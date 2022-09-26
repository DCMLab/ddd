import os


def singleStaff(measures=2, voices=2):
    krn = """\
**kern
*clefG2
*^
1c	1g
=	=
1c	1g
=||	=||
*v	*v
!!!RDF**kern: N = no stem
*-
"""
    return krn


def grandStaff():
    krn = """\
**kern	**kern
*part1	*part1
*staff2	*staff1
*striaNone	*
*clefF4	*clefG2
*k[]	*k[]
*M4/4	*M4/4
=1	=1
*^	*^
1G	2C\	1cc	4f\
.	.	.	4g\
.	2E\	.	4f\
.	.	.	4e\
*v	*v	*	*
*	*v	*v
=2	=2
1D 1F	1d
==	==
*-	*-
!!!system-decoration: {(s1,s2)}
!!!RDF**kern: > = above
!!!RDF**kern: < = below
"""


if __name__ == "__main__":
    images = "allimages"
    for f in os.listdir(images):
        krnf = f.replace(".jpg", ".krn_")
        path = os.path.join(images, krnf)
        with open(path, "w") as fd:
            fd.write(singleStaff())
