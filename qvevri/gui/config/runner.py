from qvevri.config import QvevriConfig
from qvevri.gui.dialogs import Dialog
from qvevri.gui.config.common import GameDialogCommon
from qvevri.gui.config import DIALOG_WIDTH, DIALOG_HEIGHT


class RunnerConfigDialog(Dialog, GameDialogCommon):
    """Runner config edit dialog."""

    def __init__(self, runner, parent=None):
        self.runner_name = runner.__class__.__name__
        super().__init__("Configure %s" % runner.human_name, parent=parent)

        self.game = None
        self.saved = False
        self.qvevri_config = QvevriConfig(runner_slug=self.runner_name)

        self.set_default_size(DIALOG_WIDTH, DIALOG_HEIGHT)

        self.build_notebook()
        self.build_tabs("runner")
        self.build_action_area(self.on_save)
        self.show_all()

    def on_save(self, wigdet, data=None):
        self.qvevri_config.save()
        self.destroy()
