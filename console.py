#!/usr/bin/python3

import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel

dictionary = {"Amenity": Amenity,
              "BaseModel": BaseModel,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Print Anything"""
        pass

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_quit(self, args):
        """Quit"""
        return True

    def do_create(self, arg):
        """Create a new instance"""
        my_args = arg.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        try:
            new_ins = eval(my_args[0])()
            new_ins.save()
            print(new_ins.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of
        an instance based on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        my_dict = storage.all()
        for key, value in my_dict.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    print(value)
                    return
        for k in dictionary.keys():
            if my_args[0] == k:
                print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        my_dict = storage.all()
        for key, value in my_dict.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    all_objects = storage.all()
                    all_objects.pop(key)
                    storage.save()
                    return
        for k in dictionary.keys():
            if my_args[0] == k:
                print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name"""
        my_arg = arg.split()
        my_list = []
        my_dict = storage.all()
        if len(arg) == 0:
            for key, value in my_dict.items():
                my_list.append(str(value))
            print(my_list)
        else:
            for key, value in my_dict.items():
                if my_arg[0] == value.__class__.__name__:
                    my_list.append(str(value))
            if len(my_list) == 0:
                print("** class doesn't exist **")
            else:
                print(my_list)
    def do_update(self, args):

        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        my_dict = storage.all()
        for key, value in my_dict.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    if len(my_args) == 2:
                        print("** attribute name missing **")
                        return
                    if len(my_args) == 3:
                        print("** value missing **")
                        return
                    all_objects = storage.all()
                    setattr(all_objects[key], my_args[2], my_args[3])
                    storage.save()
                    return
        for k in dictionary.keys():
            if my_args[0] == k:
                print("** no instance found **")
                return
        print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
