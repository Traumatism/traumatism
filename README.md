```py
"""
This app requires Python 3.8+
due to warlus operator usage.
"""


class Truth(object):
    """ Object for the truth """
    
    def __init__(self) -> None:
        pass

    @property
    def location(self) -> str:
        """ Get the truth location.

        Returns:
            str: The truth location.
        """

        a = 0xC2A8B98

        return "".join(
            chr(0x7574726F686520 >> (((a := a >> 3) & 7) << 3) & 0xFF)
            for _ in range(0x9)
        )


if __name__ == "__main__":
    app = App()

    print("The truth is %s." % app.truth_location)

```

Inspired from https://gist.github.com/rexim/326dceb0b3c9e524b827724f90501ee3
