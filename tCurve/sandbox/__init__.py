

def test(x):
    return x

highB = 20
lowB = 0

delta = 0.00001
oldResult = 0
newResult = delta
slices = 4
step = (highB-lowB)/slices

while (abs(newResult-oldResult)/newResult) > delta:
        oldResult = newResult
        step = (highB - lowB) / slices
        newResult = 0
        for i in range(0, slices - 2, 2):
            newResult += test(lowB + i*step) + 4 * test(lowB + (i+1)*step)    \
             + test(lowB + (i+2)*step)
        newResult *= (step/3)
        slices *= 2
        
print(newResult)
        
