import os, web
import view, config
from view import render

urls = (
  '/', 'index',
  '/uploaded/(.*)', 'uploaded'
)

class index:
  def GET(self):
    return render.base('hello world')

  def POST(self):
    form = web.input(tiles={})
    filedir = '/root/skycache/tiles'
    if 'tiles' in form:
      filepath = form.tiles.filename.replace('\\','/')
      filename = filepath.split('/')[-1]
      fout = open(filedir + '/' + filename, 'w')
      fout.write(form.tiles.file.read())
      fout.close()
      arg = str(len(os.listdir('static')) + 2)
      os.system('mb-util ' + filedir + '/' + filename + ' /root/skycache/static/tile' + arg)
      raise web.seeother('/uploaded/tile' + arg)
    else:
      raise web.seeother('/')

class uploaded:
  def GET(self, tilevar):
    return render.uploaded(web.websafe(tilevar))

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.internalerror = web.debugerror
  app.run()
