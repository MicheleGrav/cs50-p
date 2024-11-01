from fpdf import FPDF

class Shirtificate(FPDF):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.add_page()
        self.create_shirtificate()

    def create_shirtificate(self):
        self.set_font("Helvetica", "B", 36)
        self.set_text_color(0, 0, 0)
        self.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", align="C")

        self.image("shirtificate.png", x=25, y=80, w=160)

        self.set_font("Helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.text(x=75, y=150, text=f"{self.name} took CS50")


name = input("Name: ")
pdf = Shirtificate(name)
pdf.output("shirtificate.pdf")
