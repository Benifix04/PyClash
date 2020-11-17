from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive

packets = {
    10101: Login,
    10108: KeepAlive
}
