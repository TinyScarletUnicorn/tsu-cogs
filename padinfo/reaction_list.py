from typing import List, Optional, TYPE_CHECKING

from padinfo.core.padinfo_settings import settings
from padinfo.menu.id import IdMenuEmoji, IdMenuPanes
from padinfo.view.evos import EvosViewState
from padinfo.view.materials import MaterialsViewState
from padinfo.view.pantheon import PantheonViewState

if TYPE_CHECKING:
    from dbcog.models.monster_model import MonsterModel


async def get_id_menu_initial_reaction_list(ctx, dbcog, monster: "MonsterModel",
                                            full_reaction_list: List[Optional[str]] = None, force_evoscroll=False):
    # hide some panes if we're in evo scroll mode
    if not full_reaction_list:
        full_reaction_list = IdMenuPanes.emoji_names()
    if not force_evoscroll and not settings.checkEvoID(ctx.author.id):
        return full_reaction_list
    alt_versions, gem_versions = await EvosViewState.do_query(dbcog, monster)
    if alt_versions is None and gem_versions is None:
        full_reaction_list.remove(IdMenuEmoji.left)
        full_reaction_list.remove(IdMenuEmoji.right)
        full_reaction_list.remove(IdMenuEmoji.evos)
    pantheon_list, _, _ = await PantheonViewState.do_query(dbcog, monster)
    if pantheon_list is None:
        full_reaction_list.remove(IdMenuEmoji.pantheon)
    mats, usedin, gemid, _, skillups, _, _, _ = await MaterialsViewState.do_query(dbcog, monster)
    if mats is None and usedin is None and gemid is None and skillups is None:
        full_reaction_list.remove(IdMenuEmoji.mats)
    return full_reaction_list
