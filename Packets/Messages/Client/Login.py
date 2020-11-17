from random import choice
from string import ascii_uppercase
import time

from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData

from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers

class Login(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
    	pass

    def process(self):
        LoginOk(self.client, self.player).send()
        OwnHomeData(self.client, self.player).send()