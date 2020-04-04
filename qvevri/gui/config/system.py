from qvevri.config import QvevriConfig
from qvevri.gui.dialogs import Dialog
from qvevri.gui.config.common import GameDialogCommon
from qvevri.gui.config import DIALOG_WIDTH, DIALOG_HEIGHT


class SystemConfigDialog(Dialog, GameDialogCommon):
    def __init__(self, parent=None):
        super().__init__("System preferences", parent=parent)

        self.game = None
        self.runner_name = None
        self.qvevri_config = QvevriConfig()

        self.set_default_size(DIALOG_WIDTH, DIALOG_HEIGHT)

        self.build_notebook()
        self.build_tabs("system")
        self.build_action_area(self.on_save)
        self.show_all()

    def on_save(self, _widget):
        self.qvevri_config.save()
        self.destroy()
