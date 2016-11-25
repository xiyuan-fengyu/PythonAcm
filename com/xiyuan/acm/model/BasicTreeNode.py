import sys


class BasicTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def valToStr(self):
        return str(self.val)

    def toPositionChars(self):
        result = []
        valStr = self.valToStr()
        valStrLen = len(valStr)
        offset = 0
        if self.left is not None or self.right is not None:
            leftChars = None
            rightChars = None
            leftMax = {}
            rightMin = {}

            if self.left is not None:
                leftChars = self.left.toPositionChars()
                leftOffset = len(self.left.valToStr()) + 1
                for item in leftChars:
                    item.x -= leftOffset
                    item.y += 2
                    if item.y in leftMax:
                        leftMax[item.y] = max(item.x, leftMax[item.y])
                    else:
                        leftMax[item.y] = item.x
                if 2 in leftMax:
                    leftChars.append(PositionChar(leftMax[2] + 1, 1, '/'))
                    leftMax[1] = leftMax[2] + 1

            if self.right is not None:
                rightChars = self.right.toPositionChars()
                rightOffset = valStrLen + 1
                for item in rightChars:
                    item.x += rightOffset
                    item.y += 2
                    if item.y in rightMin:
                        rightMin[item.y] = max(item.x, rightMin[item.y])
                    else:
                        rightMin[item.y] = item.x
                if 2 in rightMin:
                    rightChars.append(PositionChar(rightMin[2] - 1, 1, '\\'))
                    rightMin[1] = rightMin[2] - 1

            if leftChars is not None and rightChars is not None:
                isCrossing = True
                while isCrossing:
                    isCrossing = False
                    for y in leftMax:
                        if y in rightMin and leftMax[y] + 2 > rightMin[y] + offset:
                            isCrossing = True
                            break

                    if isCrossing:
                        offset += 1

            if leftChars is not None:
                result[len(result):] = leftChars
            if rightChars is not None:
                result[len(result):] = rightChars

        for i in range(valStrLen):
            result.append(PositionChar(i + int(offset / 2 + 0.5), 0, valStr[i]))

        return result

    def __str__(self, *args, **kwargs):
        chars = self.toPositionChars()
        minX = sys.maxsize
        maxX = -minX
        maxY = -minX
        maxXPerLine = {}
        for item in chars:
            if item.x < minX:
                minX = item.x
            if item.x > maxX:
                maxX = item.x
            if item.y > maxY:
                maxY = item.y

            if item.y in maxXPerLine:
                cur = maxXPerLine.get(item.y)
                if cur < item.x:
                    maxXPerLine[item.y] = item.x
            else:
                maxXPerLine[item.y] = item.x

        xLen = maxX - minX + 1
        offsetX = -minX
        charArr = [['\0' for j in range(xLen + 1)] for i in range(maxY + 1)]
        for y in maxXPerLine:
            x = maxXPerLine[y]
            charArr[y][x + offsetX + 1] = '\n'

        for item in chars:
            charArr[item.y][item.x + offsetX] = item.c

        result = "\n"
        for i in range(maxY + 1):
            for j in range(xLen + 1):
                c = charArr[i][j]
                if c == '\n':
                    result += c
                    break
                elif c == '\0':
                    result += ' '
                else:
                    result += c

        return result


class PositionChar:
    def __init__(self, x, y, c):
        self.c = c
        self.x = x
        self.y = y
