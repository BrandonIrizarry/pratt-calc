import cmd
from typing import final, override

from pratt_calc.main import evaluate


@final
class Repl(cmd.Cmd):
    intro = "Welcome to the Pratt Calc REPL. Type 'exit' to exit."
    prompt = "(calc) "

    @override
    def default(self, line: str):
        """Read, evaluate and print the provided expression."""

        print(evaluate(line))

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


if __name__ == "__main__":
    Repl().cmdloop()
