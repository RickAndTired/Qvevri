from qvevri.config import QvevriConfig
from qvevri.gui.dialogs import Dialog
from qvevri.gui.config.common import GameDialogCommon
from qvevri.gui.config import DIALOG_WIDTH, DIALOG_HEIGHT


class AddGameDialog(Dialog, GameDialogCommon):
    """Add game dialog class."""

    def __init__(self, parent, game=None, runner=None):
        super().__init__("Add a new game", parent=parent)
        self.game = game
        self.saved = False

        self.set_default_size(DIALOG_WIDTH, DIALOG_HEIGHT)
        if game:
            self.runner_name = game.runner_name
            self.slug = game.slug
        else:
            self.runner_name = runner
            self.slug = None

        self.qvevri_config = QvevriConfig(
            runner_slug=self.runner_name,
            level="game",
        )
        self.build_notebook()
        self.build_tabs("game")
        self.build_action_area(self.on_save)
        self.name_entry.grab_focus()
        self.connect("delete-event", self.on_cancel_clicked)
        self.show_all()
