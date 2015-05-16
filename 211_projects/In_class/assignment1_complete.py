class MyError(Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)

class Hospital:
        def __init__(self,patient_no):
                self.patient_no = patient_no
                """Hospital has 4 wards and each ward has 3 beds,
                so patient 3 should be in first ward(location: A 3), patient 4 should be in the second ward(location: B 4)
                """

                if self.patient_no >= 0 and self.patient_no <= 9:
                    print("allowed")
                else : 
                    #print("card should not be between 0 and 51")
                    raise MyError("invalid id, a valid id should range between 0 and 9")

        def __repr__(self):
                """ this function translates the location of the patient to a 2-letter string
                like : A1, A2 etc
                tips: if and elif statements are cumbersome, use dictionary
                """
                #grade = {'\u2660','\u2661','\u2662','\u2663'} #suits
                wards = {
                        1: 'A', # key is the self.patient_no
                        2: 'B',
                        3: 'C',
                        4: 'D'
                        } [self.patient_no]
        
                beds = {
                        'A': '1',  # key is the ward
                        'B':'2',
                        'C':'3',
                        'D':'4'
                       } [wards]
                #beds = { 'A': '1', 'B':'2', 'C':'3','D':'4'}
                location = []
                return wards+ ' ' + beds

        def __lt__(self,other):
                """
		the less than operator '<' is called when sort() function is used upon
		a list containing Hospital objects, define this function helps avoid unexpected
		exceptions.
	        """
                return self.patient_no <other.patient_no
      
                
        def floor(self):
                """ this returns the floor at which the patient would be staying
                    similar to the rank function for Cards project
                """
                if self.patient_no == 1 or self.patient_no == 3:
                        self.floor = 2
                elif self.patient_no == 2 or self.patient_no == 4:
                        self.floor = 3
                return self.floor
        
        def rating(self):
                """ Given by the employees of the hospital for each floor
                """
                if self.patient_no == 1 or self.patient_no == 3:
                        self.rating = 3
                elif self.patient_no == 2 or self.patient_no == 4:
                        self.rating = 4
                        
                return self.rating
        


class Area(Hospital):

        def __init__(self,patient_no):
                super().__init__(patient_no)
                self.patient_no = patient_no

        def rating(self):
                """ overrides the rating function given in the base class
                this rating is given by tha Area incharge on the basis of patient feedback etc
                This might vary from the earlier rating
                """

                if self.patient_no == 1 or self.patient_no == 3:
                        self.rating = 4
                elif self.patient_no == 2 or self.patient_no == 4:
                        self.rating = 5

                return self.rating

class Code(list):
        """ the class that inherits the Python class "list"
        similar to Deck class in Cards
        Append 0,1,2,3,4 to self
        """
        
        def __init__(self):
                for i in range(0,4):
                        self.append(Hospital)
                                    
        
def main():
    hospital = Hospital(4)
    location = repr(hospital)
    print("Location of the patient (ward and bed): ",location)
    f = hospital.floor()
    print("The floor for the patient is : ",f)
    r = hospital.rating()
    print("The employees's rating is : --> ", r)
    area = Area(4)
    rtng = area.rating()
    print("Area incharge's rating : --> ", rtng)
    code = Code()
    print("Illustration of the extended class of python 'list' ,Length --> ", len(code))
    

if __name__ == "__main__":
    main()
        








    
