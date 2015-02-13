#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import *

def connection(usuario, contrasena):
	conexion = Connection()
	db = conexion.webelbadegiacomi
	colection = db.usuarios
	entrada = {"usuario" : usuario, "contrasena" : contrasena}
	colection.insert(entrada)
	