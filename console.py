#!/usr/bin/python3

"""
<<<<<<< HEAD
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
=======
The entry point for the command intepreter
"""

import models
import cmd
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    an interpreter class inheriting from cmd
    """
    prompt = '(hbnb) '
    classes_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]
    int_attrs = ["number_rooms", "number_bathrooms", "max_guest",
                 "price_by_night"]
    float_attrs = ["latitude", "longitude"]

    def do_EOF(self, line):
        """Quits the console when Ctrl D entered
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """overrides parent empty line method
        """
        return False

    def do_create(self, args):
        """
        Creates a new instance of a specified class and prints
        instance's unique id
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

        except:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        prints the string repr of an instance based
        on class name and id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()

        for key, value in all_objs.items():
            if key == obj_key:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """
        deletes an instance of a class based on class name and id
        saves changes to json file
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()

        for key, value in all_objs.items():
            if key == obj_key:
                del all_objs[key]
                storage.__objects = all_objs
                storage.save()
                return

        print("** no instance found **")

    def do_all(self, line):
        """
        prints, as a list of strings, the string repr of all instances
        in storage, or all instances of a certain class, if provided
        """
        objs_list = []
        storage = FileStorage()
        all_objs = storage.all()
        check = False

        if not line:
            for key, value in all_objs.items():
                objs_list.append(str(value))

            print(objs_list)
            return
        else:
            args = line.split()

            for key, value in all_objs.items():
                test_obj_type = key.split(".")
                if test_obj_type[0] == args[0]:
                    objs_list.append(str(value))
                    check = True

            if check:
                print(objs_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        updates or adds an attribute to an instance of a class
        instance is identified by class name and id
        only one attribute and value can be updated per call
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        instance_found = False

        for key, value in all_objs.items():
            if key == obj_key:
                instance_found = value

        if not instance_found:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        if args[2] in HBNBCommand.int_attrs:
            setattr(instance_found, args[2], int(args[3]))
        elif args[2] in HBNBCommand.float_attrs:
            setattr(instance_found, args[2], float(args[3]))
        else:
            setattr(instance_found, args[2], args[3])

        instance_found.save()

    def do_count(self, line):
        """
        counts the numbers of stored instances of a class
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        storage = FileStorage()
        stored_objs = storage.all()
        count = 0

        for key in stored_objs:
            key = key.split('.')
            if key[0] == args[0]:
                count += 1

        print(count)

    def precmd(self, line):
        """
        overrides parent precmd method to handle alt syntax
        """
        if not line:
            return line

        args = line.split()

        if args[0] in ['EOF', 'quit', 'create', 'all', 'show',
                       'destroy', 'help', 'update', 'count']:
            return line

        args = args[0].split(".")
        class_name = args[0]

        if class_name not in HBNBCommand.classes_list:
            return line

        if len(args) > 1:
            args = args[1].split('(')
            command = args[0]
            obj_id = args[1].split('"')
            new_line = command + " " + class_name + " "
            if len(obj_id) > 1:
                new_line += obj_id[1]

        return new_line
>>>>>>> b088020ddb633384f63e0fe9c208d7eaa672ecce


if __name__ == '__main__':
    HBNBCommand().cmdloop()
