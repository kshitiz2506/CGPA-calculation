class student:
    marks=[]
    grades=[]
    gdict=[]
    gradeob=[]

    ns=int(input()) #number of students
    _nm=int(input()) #number of marks
    _ng=int(input()) #number of grades
    i=0
    def info(self):
        for i in range(self._ng):
                     self.fgl=input()       #grade letter i.e. S
                     self.fgp=int(input())       #grade point i.e. 10 for S, 9 for A
                     self.gdict.append(self.fgp)
        for i in range(self.ns):
                self._regn=input()       #student's roll no.
        for i in range(self._nm):
                self.sm=int(input())       #student's marks
                self.marks.append(self.sm)
        for i in range(self._nm):
                self.sg=int(input())     # grades per class
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
    
    '''the input format that I want  is 
    number of s
    number of marks
    number of grades
    grade letter
    grade points...Nth times
    roll code..nth times
    marks..Nth times for N students i.e. if 3 students and 5 marks per student then total 15 input
    grades per class, nth times(number of marks) for n students'''
    
    


    
