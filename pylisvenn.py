#!/usr/bin/python

__author__ = "Nilesh Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "nilesh.iiita@gmail.com"
__status__ = "Production"

import argparse
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

'''
sudo pip install matplotlib-venn
python Python.py -f1 FILE1.csv -f2 FILE2.csv -C1 1 -a1 0 -b2 2 
'''

parser = argparse.ArgumentParser(add_help=False,description='Intersection of tow csv files (Lists).')
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,help='Help section')
parser.add_argument('-V','--Version', action='version', version='1.0.0(beta)')
parser.add_argument('-f1','--file1', help='First file', required=False)
parser.add_argument('-f2','--file2', help='Second file', required=False)
#parser.add_argument('-m','--mode', default=1, help='"c" for common, "u" for uniq', required=False)
parser.add_argument('-d','--delimator', help='Delimator [c for "," t for "{tab},s for "{space}",m for ";"]', required=False)
parser.add_argument('-C1','--col1', type=int, help='an integer in the range 1..Last column', default=1 , required=False)
parser.add_argument('-C2','--col2', type=int, help='an integer in the range 1..Last column', default=1 , required=False)
parser.add_argument('-a1','--ignoreF1', type=int, help='Number of character ignore form first',default=0, required=False)
parser.add_argument('-a2','--ignoreF2', type=int, help='Number of character ignore form first',default=0, required=False)
parser.add_argument('-b1','--ignoreL1', type=int, help='Number of character ignore form last',default=0, required=False)
parser.add_argument('-b2','--ignoreL2', type=int, help='Number of character ignore form last',default=0, required=False)
parser.add_argument('-H1','--Header1', type=int, help='Consider first row as header',default=1, required=False)
parser.add_argument('-H2','--Header2', type=int, help='Consider first row as header',default=1, required=False)
#parser.add_argument('-h','--help', help='Help section', required=False)
args = vars(parser.parse_args())

########################################################################
try:args['delimator']
except:args['delimator'] == '\t'

fhu1 =  open('_'.join(args['file1'].split('.')[:-1]+['uniq.csv']),'w')
fhu2 =  open('_'.join(args['file2'].split('.')[:-1]+['uniq.csv']),'w')


File1 = [i.split(args['delimator']) for i in open(args['file1']).read().splitlines()]
File2 = [i.split(args['delimator']) for i in open(args['file2']).read().splitlines()]
if args['Header1']:print >>fhu1,'\t'.join(File1.pop(0))
if args['Header2']:print >>fhu2,'\t'.join(File2.pop(0))
#if args['Header2']:File2.pop(0)


#data1 = [i[args['col1']-1][args['ignoreF1']:].lower() for i in File1]
if args['ignoreL1'] <= 0:
    data1 = [i[args['col1']-1][args['ignoreF1']:].lower() for i in File1]
else:
    data1 = [i[args['col1']-1][args['ignoreF1']:(args['ignoreL1'])*-1].lower() for i in File1]



if args['ignoreL2'] <= 0:
    data2 = [i[args['col2']-1][args['ignoreF2']:].lower() for i in File2]
else:
    data2 = [i[args['col2']-1][args['ignoreF2']:(args['ignoreL2'])*-1].lower() for i in File2]


both = []
both_c = 0

data1_c = len(data1)
data2_c = len(data2)

#if args['mode'] == 1:
#if args['mode'] == 1 or args['mode'] == 'c':
both = data1+data2
both = list(set(both))
#print len(both),len(data1),len(data2)
both = [i for i in both if i in data1 and i in data2]
both_c = len(both)

#print both_c,data1_c,data2_c

uniq1 = []
uniq2 = []
uniq1_c = 0
uniq2_c = 0

#if args['mode'] == 'u':
uniq1 = [i for i in list(set(data1)) if i in data1 and i not in data2]
uniq1_c = len(uniq1)
uniq2 = [i for i in list(set(data2)) if i in data2 and i not in data1]
uniq2_c = len(uniq2)

#print uniq1,uniq1_c,uniq2_c
#print both

venn2(subsets = (uniq1_c ,uniq2_c,both_c ), set_labels = ('Group A', 'Group B'))
#plt.show()
plt.savefig('Venn_diagram.png', bbox_inches='tight')

#fhu1 =  open('_'.join(args['file1'].split('.')[:-1]+['uniq.csv']),'w')
#fhu2 =  open('_'.join(args['file2'].split('.')[:-1]+['uniq.csv']),'w')
fhu3 =  open('common.csv','w')

for i in File1:
    if i[args['col1']-1][args['ignoreF1']:].lower() in uniq1:print >>fhu1, '\t'.join(i)
    if i[args['col1']-1][args['ignoreF1']:(args['ignoreL1'])*-1].lower() in uniq1:print >>fhu1, '\t'.join(i)

for i in File2:
    if i[args['col2']-1][args['ignoreF2']:].lower() in uniq2:print >>fhu2, '\t'.join(i)
    if i[args['col2']-1][args['ignoreF2']:(args['ignoreL2'])*-1].lower() in uniq2:print >>fhu2, '\t'.join(i)

for i in both:
    print >>fhu3,i
