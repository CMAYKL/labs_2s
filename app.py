class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length
        
    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length

    
    def area(self):
        if self.type == "квадрат":
            return self.length ** 2
        elif self.type == "прямокутник":
            assert self.width is not None, "Ширина має бути вказана для прямокутника"
            return self.length * self.width
        elif self.type == "трикутник":
            return 0.5 * self.length * self.length  # Спрощено для рівнобедреного трикутника

    def perimeter(self):
        if self.type == "квадрат":
            return 4 * self.length
        elif self.type == "прямокутник":
            assert self.width is not None, "Ширина має бути вказана для прямокутника"
            return 2 * (self.length + self.width)
        elif self.type == "трикутник":
            return 3 * self.length  # Спрощено для рівностороннього трикутника
        

    def test_app_triangle():
        """Test if we create triangle figure.
        """
        fig = "трикутник"
        triangle = Figure(fig, 4)
        assert triangle.type == fig, f"Фігура має бути {fig}"

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3