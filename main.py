from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web

# database 
import sqlite3 as sqlite

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('hello hasime')
# does this return ""hello hasime"" when it recieves a get request

def verifyDatabase():
	conn = sqlite.connect("got.db") # conn - connection?
	c = conn.cursor() # c just a throwaway variable name
	
	try:
		c.execute("SELECT * from got")
		print "Game of Thrones table already exists"
	except:
		print "Creating table \'got\'"
		c.execute('CREATE TABLE got (\
				character text,\
				house text,\
				quote text )')
		
		print "Successfully created table \'got\'"
	conn.commit()
	conn.close()

class GotQuoter(tornado.web.RequestHandler):
	def get(self, id):
		response = {
			'id': int(id),
			'name': 'Crazy quotes',
			'release_date': date.today().isoformat()
			}
		self.write(response)

	def post(self):
		self.write("POST - Welcome to GOT Quoter")


class Application(tornado.web.Application):
	def __init__(self):
		# constructor function i.e. first run
		handlers = [
			(r"/?", MainHandler), 
			#at the url / main handler is called
			(r"/api/quotes/?", GotQuoter),
			(r"/api/quotes/[0-9]+/?", GotQuoter),
			]
		
		tornado.web.Application.__init__(self, handlers)
	
def main():
	# verify the database and it's fields
	verifyDatabase()
	
	app = Application()
	app.listen(80)
	IOLoop.instance().start()

if __name__ == '__main__':
	main()

