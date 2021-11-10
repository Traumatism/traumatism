"""
Inspired from https://github.com/willmcgugan/willmcgugan/


"""

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.box import ROUNDED

console = Console(
    record=True,
    width=200
)

title = "Hello world"

title_bis = "Contact me 📩"

text = """
Im a young developer, I am a young 15 year old developer who mainly does Python and sometimes Golang and Rust. I am also passionate about computers, h4ck1ng and electronics.
"""[1:]

text_bis = """
- GitHub: [link=https://github.com/traumatism]You are here! 📍[/]
- Twitter: [link=https://t.me/toastakerman]@toastakerman[/]
- Telegram: [link=https://t.me/toastakerman]@toastakerman[/]
- Discord: toast#3108
- Mail: [link=mailto:cpastoast@protonmail.com]cpastoast@protonmail.com
"""[1:-1]

CONSOLE_HTML_FORMAT = """<p align="center"><img src="assets/gif.gif"></p><pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""

console.print(Columns((
    Panel.fit(
        text,
        box=ROUNDED,
        title=title,
        title_align="center",
        width=60
    ),
    Panel.fit(
        text_bis,
        box=ROUNDED,
        title=title_bis,
        title_align="center",
        width=60
    )
)))

console.save_html(
    "README.md", 
    inline_styles=True, 
    code_format=CONSOLE_HTML_FORMAT
)