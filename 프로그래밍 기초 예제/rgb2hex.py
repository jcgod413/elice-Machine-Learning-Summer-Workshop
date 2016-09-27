def main():
    r = input() # First line
    g = input() # Second line
    b = input() # Third line

    # change r, g, b into integer...
    r = int(r)
    g = int(g)
    b = int(b)

    print(rgb2hex(r, g, b))


def rgb2hex(r, g, b):
    r = "%02X" % r
    g = "%02X" % g
    b = "%02X" % b
    hex_color = "#" + r + g + b

    return hex_color

if __name__ == "__main__":
    main()
