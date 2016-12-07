import sublime
import sublime_plugin

import sys, os
from datetime import datetime as dt

class UndoColumnLineCommand(sublime_plugin.TextCommand):

  def log(self, msg):
    class_name = type(self).__name__.replace("Command", "")

    if 'win' in sys.platform:
      dir_path = os.path.join(os.getenv('APPDATA'), r"Sublime Text 3\Packages")
      log_path = os.path.join(dir_path, class_name, "log.txt")
    else:
      # TODO mac/linux
      log_path = os.path.join(class_name, "_log.txt")

    str_d = dt.now().strftime('%y%m%d %H:%M:%S')

    with open(log_path, "a") as f:
      f.write(str_d + " : " + str(msg) + "\n")

  def run(self, edit):
    # self.log("test111")
    sel = self.view.sel()
    if len(self.view.sel()) != 1:
      sel.subtract(sel[-1])
