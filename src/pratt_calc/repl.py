import cmd
from typing import final, override

from pratt_calc.evaluator import Evaluator


@final
class Repl(cmd.Cmd):
    intro = """Welcome to the Pratt Calc REPL.

Use Ctrl+D (or the 'exit' command) to exit.

Type 'help' or '?' to list all commands."""

    prompt = "(calc) "

    def __init__(self, ev: Evaluator):
        super().__init__()

        self.ev = ev

    @override
    def default(self, line: str):
        """Read, evaluate and print the provided expression."""

        print(self.ev.evaluate(line))

    @override
    def precmd(self, line: str):
        """Intercept EOF before it mangles the application."""

        if line == "EOF":
            return "exit"

        return line

    def do_exit(self, _):
        """Exit the REPL."""

        print()
        return True
