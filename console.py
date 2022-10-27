#!/usr/bin/python3
"""Defines the HBnB console."""
from ast import Not
import cmd
from optparse import Values
import string
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        exit()

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates an instance"""
        if my_args == "" or my_args is None:
            print("** class name missing **")
        elif my_args not in storage.Classes():
            print("** class doesn't exist **")
        else:
            arg = storage.Classes()[my_args]()
            arg.save()
            print(arg.id)

    def do_show(self, my_args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if my_args == "" or my_args is None:
            print("** class name missing **")
        else:
            wd = my_args.split(' ')
            if wd[0] not in storage.Classes():
                print("** class doesn't exist **")
            elif len(wd) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(wd[0], wd[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, my_args):
        """Deletes an instance based on the class name and id"""
        if my_args == "" or my_args is None:
            print("** class name missing **")
        else:
            wd = my_args.split(' ')
            if wd[0] not in storage.Classes():
                print("** class doesn't exist **")
            elif len(wd) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(wd[0], wd[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, my_args):
        """Prints all string representation of all instances
        based or not on the class name"""
        if my_args != "":
            wd = my_args.split(' ')
            if wd[0] not in storage.Classes():
                print("** class doesn't exist **")
            else:
                lis = [str(obj) for key, obj in storage.all().items()
                       if type(obj).__name__ == wd[0]]
                print(lis)
        else:
            lis = [str(obj) for key, obj in storage.all().items()]
            print(lis)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        if len(line) == 0:
            print("** class name missing **")
            return

        my_args = line.split()
        if my_args[0] not in storage.Classes():
            print("** class doesn't exist **")
            return

        if len(my_args) < 2:
            print("** instance id missing **")
            return

        var = my_args[0] + "." + my_args[1]
        instance = FileStorage()
        all_objs = storage.all()
        id_val = False

        for key, values in all_objs.items():
            if key == var:
                id_val = values

        if not id_val:
            print("** no instance found **")
            return
        if len(my_args) < 3:
            print("** attribute name missing **")
            return
        if len(my_args) < 4:
            print("** value missing **")
            return
        setattr(id_val, my_args[2], my_args[3])
        id_val.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
