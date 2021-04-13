def prod_css_line_percent(county_id, party, percent):
    f_str = "#c{c_id} {{fill:rgba({r_val}, 0, {b_val}, {a_val});}}"
    red = 0
    blue = 0
    green = 0
    alpha = 0.0
    if party == "GOP":
        red = 255
    elif party == "DEM":
        blue = 255
    alpha = (percent*0.8)+20
    return f_str.format(c_id=county_id, r_val=red, b_val = blue, a_val=alpha)
print(prod_css_line_percent("01001","GOP", 73.61363732498625))