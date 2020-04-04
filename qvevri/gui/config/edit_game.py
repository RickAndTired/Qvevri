from qvevri.gui.dialogs import Dialog
from qvevri.gui.config.common import GameDialogCommon
from qvevri.gui.config import DIALOG_WIDTH, DIALOG_HEIGHT


class EditGameConfigDialog(Dialog, GameDialogCommon):
    """Game config edit dialog."""

    def __init__(self, parent, game):
        super().__init__("Configure %s" % game.name, parent=parent)
        self.game = game
        self.qvevri_config = game.config
        self.slug = game.slug
        self.runner_name = game.runner_name

        self.set_default_size(DIALOG_WIDTH, DIALOG_HEIGHT)

        self.build_notebook()
        self.build_tabs("game")
        self.build_action_area(self.on_save)
        self.connect("delete-event", self.on_cancel_clicked)
        self.show_all()
