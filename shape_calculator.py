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
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        outp = ''
        adding = ('*' * self.width) + '\n'
        for _ in range(self.height):
            outp += adding
        return outp

    def get_amount_inside(self, obj):
        if obj.width > self.width or obj.height > self.height:
            return 0
        else:
            return int(self.get_area() / obj.get_area())

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.height})'
