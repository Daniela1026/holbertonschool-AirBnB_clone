#!/usr/bin/python3
"""
Defines the HBnB console.
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBnB command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        EOF signal to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when receiving an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Creates an instance
        """
        if not args:
          print("** class name missing **")
        return
        if args not in self.model_tags:
            print("** class doesn't exist **")
            return

        if args == "BaseModel":
            base = BaseModel()
        if args == "User":
            base = User()
        if args == "State":
            base = State()
        if args == "City":
            base = City()
        if args == "Place":
            base = Place()
        if args == "Amenity":
            base = Amenity()
        if args == "Review":
            base = Review()

        base.save()
        print(base.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        line_arg = args.split()
        nam_name, nam_id = line_arg

        if not args:
            print("** class name missing **")
            return

        if len(line_arg) == 1:
            print("** class doesn't exist **")
            return
        
        if nam_name not in self.model_tags:
            print("** instance id missing **")
            return

        base_id = storage.all().get(f"{nam_name}.{nam_id}")
        if nor base_id:
            print("** no instance found **")
            return

        print(base_id)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return

        if len(line_arg) ==1:
            print("** class doesnt exist **")
            return

        base_id = storage.all().get(f"{nam_name}.{nam.id}")
        if not base_id:
            print("** no instance found **")
            return

    del storage.all()[f"{line_arg[0]}.{nam_id}"]
    storage.save()

    def do_all(self, my_args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if name:
            if name not in self.model_tags:
                print("** class doesn't exist **")
                return
        print([str(value) for key, value in storage_.items()])

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        my_args = line.split()
        nam_name, nam_id, name_attr, value_attr = line_arg
        if not args:
            print("** class name missing **")
            return

        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        if len(line_arg) == 2:
            print("** attribute name missing **")
            return

        base = storage.all().get(f"{nam_name}.{nam_id}")
        if not base:
            print("** no instance found **")
            return
        setattr(storage.all()[f"{line_arg[0]}.{nam_id}"),
                name_attr, value_attr.strip('"'))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
