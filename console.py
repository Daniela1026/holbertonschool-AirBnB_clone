#!/usr/bin/python3

"""
The entry point of the command interpreter
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
    An interpreter class inheriting from cmd
    """
    model_tags = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Quit the console when Ctrl D entered
        """
        return True

    def emptyline(self):
        """
        Overrides parent empty line method
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of a specified class and prints
        instance's unique id
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
        Prints the string repr of an instance based
        on class name and id
        """
        line_arg = args.split()
        m_name, m_id = line_arg

        if not args:
            print("** class name missing **")
            return
        if m_name not in self.model_tags:
            print("** class doesn't exist **")
            return
        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        base_id = storage.all().get(f"{m_name}.{m_id}")
        if not base_id:
            print("** no instance found **")
            return

        print(base_id)

    def do_destroy(self, args):
        """
        deletes an instance of a class based on class name and id
        saves changes to json file
        """
        line_arg = args.split()
        m_name, m_id = line_arg

        if not args:
            print("** class name missing **")
            return
        if m_name not in self.model_tags:
            print("** class doesn't exist **")
            return
        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        base_id = storage.all().get(f"{m_name}.{m_id}")
        if not base_id:
            print("** no instance found **")
            return

        del storage.all()[f"{line_arg[0]}.{m_id}"]
        storage.save()

    def do_all(self, name):
        """
        prints, as a list of strings, the string repr of all instances
        in storage, or all instances of a certain class, if provided
        """
        storage_ = storage.all()
        if name:
            if name not in self.model_tags:
                print("** class doesn't exist **")
                return

        print([str(value) for key, value in storage_.items()])

    def do_update(self, args):
        """
        updates or adds an attribute to an instance of a class
        instance is identified by class name and id
        only one attribute and value can be updated per call
        """
        line_arg = args.split()
        m_name, m_id, name_attr, value_attr = line_arg
        if not args:
            print("** class name missing **")
            return

        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        if len(line_arg) == 2:
            print("** attribute name missing **")
            return

        if len(line_arg) == 3:
            print("** value missing **")
            return

        if m_name not in self.model_tags:
            print("** class doesn't exist **")
            return

        base = storage.all().get(f"{m_name}.{m_id}")
        if not base:
            print("** no instance found **")
            return

        setattr(storage.all()[f"{line_arg[0]}.{m_id}"],
                name_attr, value_attr.strip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
