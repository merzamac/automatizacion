from automatizacion.sender_message import Sender
from automatizacion.helpers import which_comand
from automatizacion.constants import allgps
import pandas as pd



def test_send():

    Sender.google(".data/lp.csv")
                

    