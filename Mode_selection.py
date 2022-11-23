import Pair_num_color as Pairnum_color
from Colour_classes import MAJOR_COLORS,MINOR_COLORS
class Mode:
    def color_pair_to_string(self,major_color, minor_color):
        return f'{major_color} {minor_color}'
    def verfication(self):
        for major_color in MAJOR_COLORS:
            for minor_color in MINOR_COLORS:
                color_names = self.color_pair_to_string(major_color, minor_color)
                color_number = Pairnum_color.get_pair_number_from_color(major_color, minor_color)
                print(f'{color_names} {color_number}')
