from tsutils.menu.closable_embed_base import ClosableEmbedMenuBase

from crowddata.mixins.adpem.view.show_stats import ShowStatsView


class ClosableEmbedMenu(ClosableEmbedMenuBase):
    view_types = {
        ShowStatsView.VIEW_TYPE: ShowStatsView
    }
