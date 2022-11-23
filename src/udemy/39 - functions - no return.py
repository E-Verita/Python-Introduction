def banner_text(text: str = "", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.

   :param text: The string to print.
       An asterisk (*) will result in a row of asterisks.
       The default will print a blank line, with a ** border at
       the left and right edges.
   :param screen_width: The overall width to print within
       (including the 4 spaces for the ** either side).
   :raises ValueError: if the supplied string is too long to fit.
   """
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger than specified width {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Eyes at night never see the day", 70)
banner_text("Because it's not in my nature", 70)
banner_text("Golden wings rise from the plane", 70)
banner_text("They burn above the red earth", 70)
banner_text(screen_width=60)
banner_text("Scale these walls in front of me", 70)
banner_text("Have you ever stopped to wonder...", 70)
banner_text("*")
