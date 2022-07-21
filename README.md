# Password Manager with Python (CLI)

![](https://blog.1password.com/articles/are-password-managers-safe/header.svg)

### What is this? *¿Qué es esto?*

This app is a password manager made in Python, it is a project that is made so that many people can contribute to it, right now there is a functional version, which will be explained below, it has the main features that a password manager should have, it is a little "insecure" because I made it to be easy to use at first, later functions will be added that will not change the core of the program, however they will make it more secure. It is a Command Line Interface, but in the future we plan to make it a web application so it can be accessed from anywhere with a friendly UI.

*Esta app es un administrador de contraseñas hechos en Python, es un proyecto que está hecho para que muchas personas puedan contribuir a el, ahora mismo hay una versión funcional, la que será explicada a continuación, tiene las características principales que un gestor de contraseñas debería tener, es un poco "inseguro" porque lo hice para que fuera fácil de utilizar en un primer momento, después se le agregarán funciones que no cambiarán el core del programa, sin embargo harán que sea más seguro. Es un Command Line Interface, pero en un futuro se tiene planeado hacerlo una aplicación web para que pueda ser accesada desde cualquier parte con un UI amigable.*

### Requirements *Requerimentos*

 - Python 3.9
 - Packages specified in ```requirements.txt```

### Instructions *Instrucciones*

You can run the program in different ways, but following good practices, first create a virtual environment with the native Python ```venv``` module.

*Puedes correr el programa de diferentes formas, pero siguiendo las buenas prácticas, primero crea un ambiente virtual con el módulo ```venv``` nativo de Python.*

```bash
user@penguin:~/password-manager$ python3 -m venv env
user@penguin:~/password-manager$ source env/bin/activate
```

```bash
user@penguin:~/password-manager$ python3 -m pip install -r requirements.txt
```

Now run the ```main.py``` file .

*Ahora solo corre el archivo ```main.py```.*

```bash
user@penguin:~/password-manager$ python3 main.py
```

Follow the instructions and you are ready to start using the program correctly.

*Sigue las instrucciones y listo, puedes empezar a usar el programa correctamente.*

### Screenshots

![](https://i.imgur.com/3cvGDA3.png)

![](https://i.imgur.com/qNT43hf.png)
