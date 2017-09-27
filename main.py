from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('hello hasime')
# does this return ""hello hasime"" when it recieves a get request

class Application(tornado.web.Application):
	def __init__(self):
		# constructor function i.e. first run
		handlers = [
			(r"/?", MainHandler)
			#at the url / main handler is called
			]
		
		tornado.web.Application.__init__(self, handlers)
	
def main():
	app = Application()
	app.listen(80)
	IOLoop.instance().start()

if __name__ == '__main__':
	main()

