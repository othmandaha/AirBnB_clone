#!/usr/bin/python3
"""The HBbB Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
