import pypyodbc


class DBManager:


	def __init__(self):

		try:
			self.conn = pypyodbc.connect("DRIVER={MySQL ODBC 3.51 Driver};SERVER=localhost;DATABASE=renewalsystem;USER=root;OPTION=3;")
			self.cursor = self.conn.cursor()
			self.success = True
		except:
			self.success = False
	


	def executeQuery(self, query):
		self.data = self.cursor.execute(query)
		self.data = self.data.fetchall()
		return self.data

	def executeNonQuery(self, query):
		self.cursor.execute(query)
		self.conn.commit()


	def closeConnection(self):
		self.conn.close()


if __name__ == "__main__":
	db = DBManager()
	print (db.success)
	data = db.executeQuery("select * from clients")
	print (data)