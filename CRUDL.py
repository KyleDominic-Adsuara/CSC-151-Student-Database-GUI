import csv
import os
import tkinter as tk

class Student_Database():
	"""docstring for Student_Database"""
	def __init__(self,root):
		self.root = root
		self.root.title('student database')
		self.root.geometry('1000x700')

		self.frame = tk.Frame(self.root, width = 560, height = 660,relief = 'sunken', bg = 'white')
		self.frame.place(x=230, y=40)

		self.mainlabel = tk.Label(self.root, text = 'SIMPLE STUDENT DATABASE',height = 3)
		self.mainlabel.place(x=50, y = 10)

		self.name = ''
		self.yearlv = ''
		self.idNum = ''
		self.course = ''

		self.namelabel = tk.Label(self.root, text='full name :')
		self.namelabel.place(x = 0, y = 50)
		self.nameEntry = tk.Entry(self.root)
		self.nameEntry.place(x = 90, y = 50)

		self.idlabel = tk.Label(self.root, text='ID number:')
		self.idlabel.place(x = 0, y = 70)
		self.idEntry = tk.Entry(self.root)
		self.idEntry.place(x = 90, y = 70)

		self.courselabel = tk.Label(self.root, text='Course: ')
		self.courselabel.place(x = 0, y = 90)
		self.courseEntry = tk.Entry(self.root)
		self.courseEntry.place(x = 90, y = 90)

		self.yearlabel = tk.Label(self.root, text='Check year level: ')
		self.yearlabel.place(x = 0, y = 110)
		self.p = tk.StringVar()

		self.yr1 = tk.Radiobutton(self.root, text='1st year', variable = self.p, value = '1st year student')
		self.yr1.place(x = 0, y = 130)
		self.yr2 = tk.Radiobutton(self.root, text='2nd year', variable = self.p, value = '2nd year student')
		self.yr2.place(x = 0, y = 150)
		self.yr3 = tk.Radiobutton(self.root, text='3rd year', variable = self.p, value = '3rd year student')
		self.yr3.place(x = 0, y = 170)
		self.yr4 = tk.Radiobutton(self.root, text='4th year', variable = self.p, value = '4th year student')
		self.yr4.place(x = 0, y = 190)
		self.yr5 = tk.Radiobutton(self.root, text='5th+ year', variable = self.p, value = '5th+ year student')
		self.yr5.place(x = 0, y = 210)

		self.savebutton = tk.Button(self.root, text='Save new profile',height = 2, width=15,bg = 'green', command = self.getProfile)
		self.savebutton.place(x = 20, y = 230)

		self.displaybutton = tk.Button(self.root, text = 'Display List',height = 2, width=15,bg = 'yellow', command = self.displayList)
		self.displaybutton.place(x = 20, y = 270)

		self.clearlistbutton = tk.Button(self.root, text = 'Clear List',height = 2, width=15,bg = 'yellow', command = self.clearList)
		self.clearlistbutton.place(x = 20, y = 310)

		self.deletelabel = tk.Label(self.root, text='Enter Id to delete profile:')
		self.deletelabel.place(x = 20, y = 350)
		self.delete_entry = tk.Entry(self.root)
		self.delete_entry.place(x =20, y = 370)

		self.deleteprofbutton = tk.Button(self.root,text = 'Delete', height = 2, width = 15, bg = 'red', fg = 'white', command = self.deletion)
		self.deleteprofbutton.place(x = 25, y = 390)

		self.cnamelabel = tk.Label(self.root,text="New name: ")
		self.cnamelabel.place(x=800, y= 50)
		self.cname_entry = tk.Entry(self.root)
		self.cname_entry.place(x=870, y=50)

		self.idchange1label = tk.Label(self.root,text="Enter ID: ")
		self.idchange1label.place(x=800, y=70)
		self.idchange1entry = tk.Entry(self.root)
		self.idchange1entry.place(x=870, y =70)

		self.changenamebutton = tk.Button(self.root,text='enter ID to change name', height =2, width = 20, bg= 'blue', fg ='white', command = self.editName)
		self.changenamebutton.place(x = 835, y =90)

		self.cidlabel = tk.Label(self.root,text = "New ID: ")
		self.cidlabel.place(x=800,y=150)
		self.cidentry = tk.Entry(self.root)
		self.cidentry.place(x=870,y=150)

		self.idchange2label = tk.Label(self.root,text="Enter ID: ")
		self.idchange2label.place(x=800,y=170)
		self.idchange2entry = tk.Entry(self.root)
		self.idchange2entry.place(x=870, y =170)

		self.changeIDbutton = tk.Button(self.root,text='enter old ID to change ID', height =2, width = 20, bg= 'blue', fg ='white', command = self.editID)
		self.changeIDbutton.place(x = 835, y =190)

		self.c_courselabel  = tk.Label(self.root,text = "New Course: ")
		self.c_courselabel.place(x=800,y=250)
		self.c_courseentry = tk.Entry(self.root)
		self.c_courseentry.place(x=870,y=250)

		self.idchange3label = tk.Label(self.root,text="Enter ID: ")
		self.idchange3label.place(x=800,y=270)
		self.idchange3entry = tk.Entry(self.root)
		self.idchange3entry.place(x=870, y =270)

		self.changecoursebutton = tk.Button(self.root,text='enter ID to change Course', height =2, width = 20, bg= 'blue', fg ='white', command = self.editCourse)
		self.changecoursebutton.place(x = 835, y =290)

		self.idchange4label = tk.Label(self.root,text="Enter ID: ")
		self.idchange4label.place(x=800,y=350)
		self.idchange4entry = tk.Entry(self.root)
		self.idchange4entry.place(x=870, y =350)
		self.newyearlevellabel = tk.Label(self.root, text='check new year level')
		self.newyearlevellabel.place(x=800, y =370)
		self.j = tk.StringVar()

		self.nyr1 = tk.Radiobutton(self.root, text='1st year', variable = self.j, value = '1st year student')
		self.nyr1.place(x = 835, y = 390)
		self.nyr2 = tk.Radiobutton(self.root, text='2nd year', variable = self.j, value = '2nd year student')
		self.nyr2.place(x = 835, y = 410)
		self.nyr3 = tk.Radiobutton(self.root, text='3rd year', variable = self.j, value = '3rd year student')
		self.nyr3.place(x = 835, y = 430)
		self.nyr4 = tk.Radiobutton(self.root, text='4th year', variable = self.j, value = '4th year student')
		self.nyr4.place(x = 835, y = 450)
		self.nyr5 = tk.Radiobutton(self.root, text='5th+ year', variable = self.j, value = '5th+ year student')
		self.nyr5.place(x = 835, y = 470)

		self.changeyearbutton = tk.Button(self.root,text='enter ID to change YearLV', height =2, width = 20, bg= 'blue', fg ='white', command = self.editYearlevel)
		self.changeyearbutton.place(x = 835, y =490)

	def getProfile(self):
		self.name = self.nameEntry.get()
		self.idNum = self.idEntry.get()
		self.course = self.courseEntry.get()
		self.yearlv = self.p.get()
		self.saveProfile()
		self.radioB_Reset()
		self.entryReset()
		self.reset()

	def deletion(self):
		num = self.delete_entry.get()
		self.delete_entry.delete(0,'end')
		self.deleteProfile(num)
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful", bg = 'white')
		self.savelabel.place(x = 280, y = 0)

	def displayProfile(self):
		print('Student name: ', self.name)
		print('ID number: ', self.idNum)
		print('Course and year level: ', self.course,' ' ,self.yearlv)

	def reset(self):
		self.name = ''
		self.idNum = ''
		self.yearlv = ''
		self.course = ''

	def entryReset(self):
		self.nameEntry.delete(0,'end')
		self.idEntry.delete(0,'end')
		self.courseEntry.delete(0,'end')

	def radioB_Reset(self):
		self.yr1.deselect()
		self.yr2.deselect()
		self.yr3.deselect()
		self.yr4.deselect()
		self.yr5.deselect()

	def editName(self):
		newname = self.cname_entry.get()
		validId = self.idchange1entry.get()
		self.cname_entry.delete(0,'end')
		self.idchange1entry.delete(0,'end')
		self.nameEdit(validId,newname)
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful", bg ='white')
		self.savelabel.place(x = 280, y = 0)

	def editID(self):
		newID = self.cidentry.get()
		oldID = self.idchange2entry.get()
		self.idEdit(oldID,newID)
		self.cidentry.delete(0,'end')
		self.idchange2entry.delete(0,'end')
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful", bg ='white')
		self.savelabel.place(x = 280, y = 0)

	def editCourse(self):
		newCourse = self.c_courseentry.get()
		validId = self.idchange3entry.get()
		self.courseEdit(validId,newCourse)
		self.c_courseentry.delete(0,'end')
		self.idchange3entry.delete(0,'end')
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful", bg ='white')
		self.savelabel.place(x = 280, y = 0)

	def editYearlevel(self):
		newYear = self.j.get()
		validId = self.idchange4entry.get()
		self.yearlevelEdit(validId,newYear)
		self.nyr1.deselect()
		self.nyr2.deselect()
		self.nyr3.deselect()
		self.nyr4.deselect()
		self.nyr5.deselect()
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful", bg ='white')
		self.savelabel.place(x = 280, y = 0)


	def displayList(self):
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful")
		self.savelabel.place(x = 280, y = 0)
		with open('student_database.csv','r') as csv_reader:
			multistring =[]
			reader = csv.DictReader(csv_reader)
			for row in reader:
				string = "Name: %s |ID Number: %s |Course and Year Level: %s %s \n" %(row['Name'],row['IDnumber'],row['YearLevel'],row['Course'])
				self.listLabel = tk.Label(self.frame,text = string, bg = 'white')
				self.listLabel.pack()

	def saveProfile(self):
		with open('student_database.csv', 'a', newline = '') as csv_writer:
			writer = csv.writer(csv_writer)
			writer.writerow([self.name,self.idNum,self.yearlv,self.course])
		self.clearList()
		self.savelabel = tk.Label(self.frame, text= "operation succesful", bg ='white')
		self.savelabel.place(x = 280, y = 0)

	def displayAll(self):
		with open('student_database.csv','r') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				print(row)

	def clearList(self):
		self.frame.destroy()
		self.frame = tk.Frame(self.root, width = 560, height = 660,relief = 'sunken', bg = 'white')
		self.frame.place(x=230, y=40)

	def deleteProfile(self,Id):
		rows = list()
		with open('student_database.csv', 'r') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				rows.append(row)
				for field in row:
					if field == Id:
						rows.remove(row)
		with open('student_database.csv','w') as csv_writer:
			writer = csv.writer(csv_writer)
			writer.writerows(rows)

	def nameEdit(self,Id,newname):
		rows = list()
		with open('student_database.csv', 'r') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				rows.append(row)
				for field in row:
					if row[1] == Id:
						row[0] = newname
		with open('student_database.csv','w') as csv_writer:
			writer = csv.writer(csv_writer)
			writer.writerows(rows)

	def idEdit(self,Idold,Idnew):
		rows = list()
		with open('student_database.csv','r') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				rows.append(row)
				for field in row:
					if row[1] == Idold:
						row[1] = Idnew
		with open('student_database.csv', 'w') as csv_writer:
			writer = csv.writer(csv_writer)
			writer.writerows(rows)

	def courseEdit(self,ID,newCourse):
		rows = list()
		with open('student_database.csv', 'r') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				rows.append(row)
				for field in row:
					if row[1] == ID:
						row[3] = newCourse
		with open('student_database.csv', 'w') as csv_writer:
			writer = csv.writer(csv_writer)
			writer.writerows(rows)

	def yearlevelEdit(self,ID,newYearlv):
		rows = list()
		with open('student_database.csv', 'r') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				rows.append(row)
				for field in row:
					if row[1] == ID:
						row[2] = newYearlv
		with open('student_database.csv', 'w') as csv_writer:
			writer = csv.writer(csv_writer)
			writer.writerows(rows)


def main():
	window = tk.Tk()
	app = Student_Database(window)
	window.mainloop()

if __name__ == '__main__':
	main()
