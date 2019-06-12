
from __future__ import annotations

from typing import List
from typing import Type

from component.name import Name
from component.role import Role

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat

class CmdComp:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_COMP, self._on_cmd_COMP)

    @LogCat.log_func
    def _on_cmd_comp(
        self, e: Event, entity: str = '', args: List[str] = []
    ) -> None:
        if not args:
            text=f'Comp：？'
        else:    
            text = f'Comp：{" ".join(args)}'

        Channel.to_role(entity, Message.TEXT, text)

# cmd_echo.py
