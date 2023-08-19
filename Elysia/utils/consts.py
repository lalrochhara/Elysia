# Famhawite-Infosys-License-Identifier: MIT
# Copyright (c) 2019 - 2023 Famhawite Infosys

from typing import Iterable

from pyrogram.enums import ChatMemberStatus, ChatType

GROUP_TYPES: Iterable[ChatType] = (ChatType.GROUP, ChatType.SUPERGROUP)

ADMIN_STATUSES: Iterable[ChatMemberStatus] = (
    ChatMemberStatus.OWNER,
    ChatMemberStatus.ADMINISTRATOR,
)
