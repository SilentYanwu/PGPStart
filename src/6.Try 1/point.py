# point.py
# Point类 - 表示二维空间中的一个点

class Point(object):
    def __init__(self, x, y):
        self.__x = x  # 私有x坐标
        self.__y = y  # 私有y坐标

    # property修饰器的用处:不改变接口，直接修改数据。
    # X属性 - 使用property装饰器实现getter和setter
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    # Y属性 - 使用property装饰器实现getter和setter
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        # 返回点的字符串表示，格式为 {X:值,Y:值}
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"