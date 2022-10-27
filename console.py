#!/usr/bin/python3
"""
Function speccify a Console the entry point of the command interpreter
"""
import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Define the class HBNB as interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit Success
        """
        return True

    def emptyline(self):
        """When recive an empty line do nothing.
        """
        pass

    def do_create(self, line):
        """Create a new instance from base model
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            split_line = shlex.split(line)
            _instance = eval(split_line[0])()
            _instance.save()
            print(_instance.id)

        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """Representation of an instance based on the class name and id
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print("** class name missing **")
            return
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(split_line) < 2:
            print("** instance id missing **")
            return
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return

        tmp_key = split_line[0] + "." + split_line[1]
        if tmp_key in storage.all().keys():
            print(storage.all()[tmp_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Method to Deletes an instance based on the class name and id.
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print("** class name missing **")
            return
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(split_line) < 2:
            print("** instance id missing **")
            return

        tmp_key = split_line[0] + "." + split_line[1]
        if tmp_key in storage.all().keys():
            del(storage.all()[tmp_key])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Method to print all elements of storage as a list of string
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print([str(v) for v in storage.all().values()])
            return
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in storage.all().items()
              if split_line[0] in k])

    def do_update(self, line):
        """Method to Updates an instance based on the class name
        and id by adding or updating attribute
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print("** class name missing **")
            return False
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return False
        if len(split_line) < 2:
            print("** instance id missing **")
            return False
        elif split_line[0] + "." + split_line[1] not in storage.all().keys():
            print("** no instance found **")
            return False
        elif len(split_line) < 3:
            print("** attribute name missing **")
            return False
        elif len(split_line) < 4:
            print("** value missing **")
            return False
        else:
            if split_line[3][0] == "\"":
                split_line[3] = split_line[3][1:-1]
            tmp_key = split_line[0] + "." + split_line[1]
            setattr(storage.all()[tmp_key], split_line[2], split_line[3])
            storage.all()[tmp_key].save()

    def default(self, line):
        """Method to  to retrieve all instances of a class by using
        """
        line_tmp = line.replace("(", ".").replace(")", ".").replace('"', "")\
            .replace(",", "").split(".")
        arguments = line_tmp[0] + " " + line_tmp[2]
        if len(line_tmp) > 1:
            if line_tmp[1] == "all":
                self.do_all(line_tmp[0])
            elif line_tmp[1] == "count":
                self.do_count(line_tmp[0])
            elif line_tmp[1] == "show":
                self.do_show(arguments)
            elif line_tmp[1] == "destroy":
                self.do_destroy(arguments)
            elif line_tmp[1] == "update":
                self.do_update(arguments)
                if "{" in line_tmp[2]:
                    print("Holi")
                else:
                    self.do_update(arguments)
                
                """
                arguments = command[1].split()
                id_ = arguments[0].replace(",", "").replace("\"", "")
                if "{" in arguments[2]:  # Work with dictionary
                    for i in arguments:
                        if id_ in i:
                            continue
                        if ":" in i:
                            key_ = i.replace("{", "").replace("'", "").replace(
                                ":", "").replace("\"", "")
                            print("Key:", key_)
                        else:
                            i = i.replace("\"", "").replace(",", "").replace(
                                "}", "")
                            value_ = i.replace("\"", "").replace(",", "")\
                                .replace("'", "")
                            print("Value:", value_)
                            # Update object with key and value
                            if self.do_update(
                                args[0] + " " + id_ + " " + key_ + " " + value_
                            ) is False:
                                return
                else:  # Work without dictionary
                    args_to_update = str(arguments).replace("\"", "").replace(
                        ",", "").replace("[", "").replace("]", "").replace(
                            "\'", "")
                    self.do_update(args[0] + " " + args_to_update)"""
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, line):
        """Method to print the number of instance inside the storage file json
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print(len([str(v) for v in storage.all().values()]))
            return
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return
        print(len([str(v) for k, v in storage.all().items()
              if split_line[0] in k]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
