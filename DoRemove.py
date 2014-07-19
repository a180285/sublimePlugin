import sublime, sublime_plugin

class RemoveDuplicateEmptyLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    lines = self.view.lines( sublime.Region(0, self.view.size()) )
    lines.reverse()
    empty_line = True
    last_id = self.view.size()
    for r in lines:
      if r.a == r.b and empty_line:
        self.view.erase(edit, sublime.Region(r.a, last_id))
      empty_line = (r.a == r.b)
      last_id = r.a

class MyRemoveEmptyLineEv(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    # if need_remove(view.file_name()):
      view.run_command( 'remove_duplicate_empty_line' )

def need_remove(file_name):
  exts = ['.java', '.xml', '.py', 'BUILD']
  for ext in exts:
    if file_name.endswith(ext):
      return True
  return False

# >>> view.run_command( 'remove_duplicate_empty_line' )
