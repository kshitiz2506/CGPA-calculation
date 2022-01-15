class student:
    marks=[]
    grades=[]
    gdict=[]
    gradeob=[]

    ns=int(input())
    _nm=int(input())
    _ng=int(input())
    i=0
    def info(self):
        for i in range(self._ng):
                     self.fgl=input()
                     self.fgp=int(input())
                     self.gdict.append(self.fgp)
        for i in range(self.ns):
                self._regn=input()
        for i in range(self._nm):
                self.sm=int(input())
                self.marks.append(self.sm)
        for i in range(self._nm):
                self.sg=int(input())
                self.grades.append(self.sg)
    def cgpa(self):
        self.count=0
        for i in self.marks:
                if i >=90:
                    self.grade1=self.gdict[0]
                elif 80<=i<90:
                    self.grade1=self.gdict[1]
                elif 70<=i<80:
                    self.grade1=self.gdict[2]
                elif 60<=i<70:
                    self.grade1=self.gdict[3]
                elif 55<=i<60:
                    self.grade1=self.gdict[4]
                elif 50<=i<55:
                    self.grade1=self.gdict[5]
                elif i<50:
                     self.grade1=self.gdict[6]
                student.gradeob.append(self.grade1)
                
                i+=1
        print(self.gradeob)
        print(self.marks)
        print(self.grades)
        self.total= (self.grades[0]*self.gradeob[0]+self.grades[1]*self.gradeob[1]+self.grades[2]*self.gradeob[2]+self.grades[3]*self.gradeob[3]+self.grades[4]*self.gradeob[4])/(self.grades[0]+self.grades[1]+self.grades[2]+self.grades[3]+self.grades[4])
        print(self._regn)
        print(self.total)
for i in range(student.ns):   
    def main():
        s= student()
        s.info()
        s.cgpa()
    
if __name__=="__main__":
    main()


    
