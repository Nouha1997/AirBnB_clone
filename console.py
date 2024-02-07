#!/usr/bin/python3
"""The command Line Interepter."""

from models import *
import json
import cmd
import re 


class HBNBCommand(cmd.Cmd):
    """Class that define airBnb clone clone public class instances ."""

    prompt = "(hbnb)"

    def do_EOF(self, line ):
        """Function handle end of file character (Ctrl+D)."""

        print()
        return(True)

    def do_quit(self, line):
        """Function that exist the shell in interactive mode."""

        return(True)

    def emptyline(self):
        """Function that does nothing on ENTER."""


        pass 

    def do_create(self, line):
        """Function that creates new instance of BaseModel."""

        if line == "" or line is None:
            print("**class name missing**")

        elif line not in storage.classes():
            print("**class does not exist**")

        else:
            instance = storage.classes()[line]
            instance.save()
            print(instance.id)


            def do_show(self, line):
                """Function that prints the string representation of an instance."""

                if line == "" or line is None:
                    print("***class name missing**")


                else:

                    words = line.split(' ' )
                    if words[0] not in storage.classes():
                        print("** class does not exist**")

                    elif len(words) < 2:
                        print("** instance id missing **"

                                else:
                                patt = "{}.{}".format(words[0], words[1])
                                if patt not in storage.all():
                                print("** no instance found **")

                                else:
                                print(storage.all()[patt])


                                def do_destroy(self, line):
                                """Function that deletes an instance based on class name and id."""


                                if line == "" or line is None:
                                print("** class name missing **")

                                else:
                                words = line.split(' ')
                                if words[0] not in storage.classes():
                                print("** class does not exist **")


                                elif len(words) < 2:
                                print("** instance id missing **")

                                else:
                                patt = "{}.{}".format(words[0], words[1])
                                if patt not in storage.all():
                                print("** no instance found **")
                                else:
                                del storage.all()[patt]
                                storage.save()


                                def do_all(self, line):
                                """Function that prints all string representation of an instance."""


                                if line != "":
                                words = line.split(' ')
                                if words[0] not in storage.classes():
                                print("** class does not exist **")

                                else:

