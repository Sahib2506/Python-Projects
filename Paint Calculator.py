print("Welcome to Paint Calculator")

Height = int(input("Height of wall: "))
Width = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
  area = height * width
  required = round(area/cover)
  print(f"You will need {required} cans to paint the wall")

paint_calc(height=Height, width=Width, cover=coverage)

