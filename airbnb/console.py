#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to quit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        new_instance = BaseModel()
        with open(FileStorage.__file_path, mode="w") as f:
            f = new_instance.save()
        print(self.id)

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
