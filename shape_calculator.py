class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        outp = 2 * self.width + 2 * self.height
        return outp

    def get_diagonal(self):
        outp = (self.width ** 2 + self.height ** 2) ** 0.5
        return outp

    def get_picture(self):
        outp = ''
        adding = ('*' * self.width) + '\n'
        for i in range(self.height):
            outp += adding
        return outp

    def get_amount_inside(self, obj):
        if obj.width > self.width or obj.height > self.height:
            return 0
        else:
            return self.get_area() / obj.get_area


class Square:
    pass
