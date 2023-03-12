# -*- coding: utf8 -*-

class Note():


    def __init__(self,id, name, body,creat_data, creat_tme):
        self.id = id
        self.name = name
        self.body = body
        self.creat_data = creat_data
        self.creat_time = creat_tme


    def __str__(self):
        return "{};{};{};{};{};\n".format(self.id,self.name, self.body, self.creat_data,self.creat_time)







