dictA = {'liuke':'nan','liuyiping':'nv'}
print dictA
dictB = dict([['jiyangyang','nv'],['liuxinqing','nv']])
dictMerged2=dict(dictA, **dictB)
print dictMerged2