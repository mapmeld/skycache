import web
import view, config
from view import render

urls = (
  '/', 'index'
)

class index:
  def GET(self):
    return render.base('hello world')

  def POST(self):
    form = web.input(tiles={})
    filedir = '~/skycache/static'
    if 'tiles' in form:
      filepath = form.tiles.filename.replace('\\','/')
      filename = filepath.split('/')[-1]
      fout = open(filedir + '/' + filename, 'w')
      fout.write(form.tiles.file.read())
      fout.close()
    raise web.seeother('/')

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.internalerror = web.debugerror
  app.run()
