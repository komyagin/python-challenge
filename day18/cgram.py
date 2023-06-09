import colorgram

rgb_colors = []
colors = colorgram.extract('img.png', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)


color_list = [(249, 248, 244), (251, 245, 249), (242, 250, 246), (237, 244, 250), (218, 0, 81), (240, 225, 0), (206, 164, 1), (234, 223, 102), (1, 193, 224), (218, 73, 5), (11, 193, 115), (17, 108, 176), (16, 30, 176), (10, 25, 69), (224, 160, 106), (117, 176, 216), (224, 2, 0), (219, 131, 176), (233, 58, 141), (239, 162, 199), (225, 16, 163), (3, 51, 26), (18, 143, 66), (119, 223, 237), (119, 192, 166), (58, 10, 24), (140, 220, 203), (72, 17, 3), (4, 101, 49), (120, 88, 214)]
