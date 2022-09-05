
import numpy as np
import matplotlib.pyplot as plt

class Putter_togetherer:
    def __init__(self,input_1,input_2, delta_pop1, delta_pop2, total_specie1,total_specie2, max_1,max_2,type_specie1, type_specie2, biggest_dpop, most_threatened, bigger_area,input_y1,input_y2,density_1,density_2,locreg_1,locsubreg_1,locreg_2,locsubreg_2):
        '''This function creates objects for the class so they can be used by other functions inside this class. This function is automatically run each time the class is called. This function is what accepts all the arguements when the class is called.'''
        self.delta_pop1 = delta_pop1                    #assign self.delta_pop1 to delta_pop1
        self.delta_pop2 = delta_pop2                    #assign self.delta_pop2 to delta_pop2
        self.total_specie1 = total_specie1              #assign self.total_specie1 to total_specie1
        self.total_specie2 = total_specie2              #assign self.total_specie2 to total_specie2
        self.max_1 = max_1                              #assign self.max_1 to max_1
        self.max_2 = max_2                              #assign self.max_2 to max_2
        self.type_specie1 = type_specie1                #assign self.type_specie1 to type_specie1
        self.type_specie2 = type_specie2                #assign self.type_specie2 to type_specie2
        self.input_1 = input_1                          #assign self.input_1 to input_1
        self.input_2 = input_2                          #assign self.input_2 to input_2
        self.biggest_dpop = biggest_dpop                #assign self.biggest_dpop to biggest_dpop
        self.most_threatened = most_threatened          #assign self.most_threatened to most threatened
        self.bigger_area = bigger_area                  #assign self.bigger_area to bigger_area
        self.input_y1 = input_y1                        #assign self.input_y1 to input_y1
        self.input_y2 = input_y2                        #assign self.input_y2 to input_y2
        self.density_1 = density_1                      #assign self.density_1 to density_1
        self.density_2 = density_2                      #assign self.density_2 to density_2
        self.locreg_1 = locreg_1                        #assign self.locreg_1 to locreg_1
        self.locsubreg_1 = locsubreg_1                  #assign self.locsubreg_1 to locsubreg_1
        self.locreg_2 = locreg_2                        #assign self.locreg_2 to locreg_2
        self.locsubreg_2 = locsubreg_2                  #assign self.locsubreg_2 to locsubreg_2

    def printer(self):
        '''This frunction is the instance method in the class and is used to print out everything in the terminal. This function is called from the main function and has access to all the objects 
        of the class as it has "self" as an arguement'''
        print(f'\nCountry:{self.input_1}    Region: {self.locreg_1}    Sub-Region: {self.locsubreg_1}')         #Prints the country name and location for the first country
        print(f'Change in population between {self.input_y1} and {self.input_y2}: {self.delta_pop1}')           #Prints the change in population between the two inputted years
        print(f'The change in density of this country was {self.density_1:.2f} people / sq km')                 #Prints the change in density of the first country between the two inputted years
        print(f'Total number of endangered species: {self.total_specie1}')                                      #Prints the total number of threatened species for the first country
        print(f'Type of species most threatened: {self.type_specie1}')                                          #Prints the type of specie thats most threatened for the first country
        print(f'Number of the type of species most threatened: {self.max_1}')                                   #Prints the number of the type most threatened
        print(f'\nCountry: {self.input_2}   Region: {self.locreg_2}    Sub-Region: {self.locsubreg_2}')         #print country, Region, and sub-Region for the second country
        print(f'Change in population between {self.input_y1} and {self.input_y2}: {self.delta_pop2}')           #print change in population between two years for the second country
        print(f'The change in density of this country was {self.density_2:.2f} people / sq km')                 #print change in density of of the second country between the two inputted years
        print(f'Total number of endangered species: {self.total_specie2}')                                      #Prints the total number of threatened species for the second country
        print(f'Type of species most threatened: {self.type_specie2}')                                          #Prints the type of specie thats most threatened for the second country
        print(f'Number of the type of species most threatened: {self.max_2}')                                   #Prints the type of specie thats most threatened for the second country
        print(f'\nCountry with the biggest change in population: {self.biggest_dpop}')                          #print country with biggest change in population
        print(f'Country with the most threatened species: {self.most_threatened}')                              #print country with most threatened species
        print(f'The larger country is: {self.bigger_area}')                                                     #print the name of the country with the larger area

def finder_funct(index_1,index_2,index_y1,index_y2, pop_data, specie_data,country_data):
    '''
    A function that requires data in order to work, it is called in the main function. This function is meant to calculate the growth in population for both countries, total endangered species for both countries 
    , the type of species most endangered for both countries, and the changes in density for both countries. The funtcion then returns all these calculated values back to where it was called from.
    '''
    pop_growth1 = int(pop_data[index_1,index_y2]) - int(pop_data[index_1,index_y1])                                                             #Calculates the population growth for the first country between the two given years
    pop_growth2 = int(pop_data[index_2,index_y2]) - int(pop_data[index_2,index_y1])                                                             #Calculates the population growth for the second country between the two given years
    total_specie1 =int(specie_data[index_1,1]) + int(specie_data[index_1,2]) + int(specie_data[index_1,3]) + int(specie_data[index_1,4])        #Calculates the total number of threatened species for the first country
    total_specie2 =int(specie_data[index_2,1]) + int(specie_data[index_2,2]) + int(specie_data[index_2,3]) + int(specie_data[index_2,4])        #Calculates the total number of threatened species for the second country
    maxer_1 = np.array([int(specie_data[index_1,1]), int(specie_data[index_1,2]), int(specie_data[index_1,3]), int(specie_data[index_1,4])])    #Creates an array with the threatened specie data at the row of the first inputted country
    max_1 = np.max(maxer_1)                                                                                                                     #finds the highest value in the array created above and stores the value in a variable
    maxer_2 = np.array([int(specie_data[index_2,1]), int(specie_data[index_2,2]), int(specie_data[index_2,3]), int(specie_data[index_2,4])])      #Creates an array with the threatened specie data at the row of the second inputted country
    max_2 = np.max(maxer_2)                                                                                                                     #finds the highest value in the array created above and stores the value in a variable
    list_max1 = [123 ,int(specie_data[index_1,1]), int(specie_data[index_1,2]), int(specie_data[index_1,3]), int(specie_data[index_1,4])]       #Creates a list fo the data in the row of the first inputted country
    list_max2 = [123 , int(specie_data[index_2,1]), int(specie_data[index_2,2]), int(specie_data[index_2,3]), int(specie_data[index_2,4])]      #Creates a list fo the data in the row of the second inputted country
    index_specie1 = list_max1.index(max_1)                                                                                                      #Find the index of where the max value is in the list created above and store it in variable
    specie_type1 = specie_data[0,index_specie1]                                                                                                 #Gets the name of the specie thats most threatened and stores it
    index_specie2 = list_max2.index(max_2)                                                                                                      #Finds the index of the max value for the second country in the list created above
    specie_type2 = specie_data[0,index_specie2]                                                                                                 #Finds the specie name thats most threatened for the second country and stores it in a variable
    density_1 = pop_growth1 / int(country_data[index_1,3])                                                                                      #Finds the change in density for the first country between the two inputted years
    density_2 = pop_growth2 / int(country_data[index_2,3])                                                                                      #Finds the change in density of the second country between the two inputted years
    return(pop_growth1,pop_growth2,total_specie1,total_specie2,max_1,max_2,specie_type1,specie_type2,density_1,density_2)                       #Returns things calculated in the function back to where the function was called

def grapher_er(index_1,index_2,index_y1,index_y2,pop_data,input_1,input_2,total_specie1,total_specie2,country_data,locsubreg_1,locsubreg_2):    #creates a function that requires info
    '''
    This function is accepts all the neccessary variables to plot all the graphs, it also contains some code fro some calculations
    which are then used to graph as well. This function is called by the main function which is where it also recieves all the 
    info from  
    
    '''
    lister_1 = []                                                           #Creates an empty list for values to be appended into
    lister_2 = []                                                           #Creates another empty list for values to be appended into
    x_axis = []                                                             #Creates a third empty list for values to be appended into
    for i in range(index_y1, (index_y2+1)):                                 #Creates a for loop for the range of of years between the 2 years inputted by user    
        lister_1.append(pop_data[index_1,i])                                #appends the population of the first country at a certain year in the empty list named lister_1
        lister_2.append(pop_data[index_2,i])                                #appeneds the population of the second country at certain years in the empty list named lister_2
    for i in range(index_y1-1,(index_y2)):                                  #creates another for loop that runs for only the years between the two inputted years from the user, it gets the indexes of the years of those years
        i = int(int(i) + 2000)                                              #adds 2000 to the index of the years between the two inputted years
        x_axis.append(i)                                                    #Appends those years into the empty list labbeled x_axis
    reg_countries1=[]                                                       #Creates another empty list
    h = 0                                                                   #Sets variable used to iterate through data in the file to zero
    for p in country_data[:,2]:                                             #A for loop that runs through all the rows of the file named country_data at the third column
        if p == locsubreg_1:                                                #If the certain place p in the file matches the name of the sub-region of the first inputted country then run the code indented beneath
            reg_countries1.append(int(country_data[h,3]))                   #Append whatever is in the fourth colum of the file at this certain row where the sub-region is the same as the sub-region of the first country
        h+=1                                                                # If the requirements for the if statement are not matched, add 1 to the variable h
    subreg_area1 = sum(reg_countries1)                                      #Adds all the values stored in the list name reg_countries1 to get total area of the sub-region
    percentage_area1 = ((int(country_data[index_1,3]))/(subreg_area1))*100  #Calculates what percentage of the area of the sub-region is accounted for by the first inputted country
    sizes_1 = np.array([percentage_area1,int(100-percentage_area1)])        #Stores the numbers for the percentage makup of the sub-region area in an array
    country_names1= (input_1, 'Other Countries')                            #Stores the first inputted country name and a string literal to represent the other countries in the piechart
    explode = (0.2,0)                                                       # A variiable used in the piechart to change the charts experience
    
    reg_countries2 = []                                                     #Creates another empty list
    v = 0                                                                   #Sets the variable v that is used to iterate through data in the file to zero
    for p in country_data[:,2]:                                             #If the certain place p in the file matches the name of the sub-region of the second inputted country then run the code indented beneath
        if p == locsubreg_2:                                                #If the certain place p in the file matches the name of the sub-region of the second inputted country then run the code indented beneath
            reg_countries2.append(int(country_data[v,3]))                   #Append whatever is in the fourth colum of the file at this certain row where the sub-region is the same as the sub-region of the second country
        v+=1                                                                # If the requirements for the if statement are not matched, add 1 to the variable v
    subreg_area2 = sum(reg_countries2)                                      #Adds all the values stored in the list name reg_countries2 to get total area of the sub-region
    percentage_area2 = ((int(country_data[index_2,3]))/(subreg_area2))*100  #Calculates what percentage of the area of the sub-region is accounted for by the second inputted country
    sizes_2 = np.array([percentage_area2,int(100-percentage_area2)])        #Stores the percents of the makeup of the sub-region for the second inputted country
    country_names2 = (input_2, 'Other Countries')                           #Stores the second inputted country name and a string literal to represent the other countries in the piechart


    plt.figure(1)                                                                               #Creates window for the first graph
    plt.bar((input_1),(total_specie1), color = 'blue', label = f'{input_1} Data', width = 0.7)  #Plots the first bar in the bar graph with the colour blue and sets the width and gives the bar a label 
    plt.bar((input_2),(total_specie2), color = 'red', label = f'{input_2} Data', width = 0.7)   #Plots the second bar in the bar graph and gives it the colour red and sets the width and gives it a label
    plt.legend()                                                                                #Creates a legend for the graph, labels are used for the legend
    plt.title('Total Endangered speices for 2 countries')                                       #Gives the graph a title
    plt.xlabel('Countries')                                                                     #Graph title for the x axis
    plt.ylabel('Total number of Endangered Speices')                                            #Gives graph titles for y axis

    plt.figure(2)                                                                               #Creates a second window for the line graph
    plt.subplot(2,1,1)                                                                          #Creates a subplot for the graphs
    plt.title('Population Trajectory')                                                          #A title for the subplots
    plt.plot((x_axis),(lister_1),'r--', label = f'{input_1} Population Trajectory')             #Plots the first subplot
    plt.legend(shadow = True)                                                                   #Creates a leged for the subplot
    plt.ylabel('Population')                                                                    #A title for the y-axis
    plt.subplot(2,1,2)                                                                          #Creates a second subplot
    plt.plot(x_axis,lister_2,'b--', label = f'{input_2} Population Trajectory')                 #Plots the line for the second subplot
    plt.ylabel('Population')                                                                    #Gives the y-axis a label
    plt.xlabel('Year')                                                                          #Gives subplot a title for the x-axis
    plt.legend(shadow = True)                                                                   # A legend for the second subplot

    plt.figure(3)                                                                               #Creates a third window for the third graph
    plt.subplot(1,2,1)                                                                          #Creates subplots in the window
    plt.pie(sizes_1, labels= country_names1, autopct='%1.1f%%', explode=explode , shadow=True)  #Creates a piechart with the first country's data
    plt.suptitle('Area occupied by the selected countries in their sub-region', fontsize = 15)  #A title for bothe subplots
    plt.legend(title = f'Distribution of area of {locsubreg_1}')                                #A title for the legend
    
    plt.subplot(1,2,2)                                                                          #Creates a second subplot
    plt.pie(sizes_2, labels= country_names2,autopct='%1.1f%%', explode=explode,shadow=True)     #Plots the second graph in the wondow
    plt.legend(title = f'Distribution of area of {locsubreg_2}')                                #Gives the second graphs legend a title
    plt.show()                                                                                  #Shows all the graphs
def main():                                                                                     #The main function, accepts no arguements.
    '''
    This is the main function that accepts no arguements and will run the entire code once called.
    The data files area all imported in this function and it is also where all the inputs are asked for from the user.
    The purpose of this code is to find the exact row for where the entered countries info is. The country indexes are then used to retrieve info from
    other files as well since they will all have the same index. This function also gets the indexes of the inputed years which are used to get the all the population data.
    The indexes were used to get alot of information from the files such as the total endangered species, the location of the ocuntry and many more things.
    '''                                                                               
    pop_data = np.genfromtxt('Population_Data.csv', delimiter = ',', encoding=None, dtype=None)     #Imports the file containing population data and creates an array from it the stores it in a variable
    specie_data = np.genfromtxt('Threatened_Species.csv', delimiter=',', encoding=None, dtype=None) #Imports the file containing threatened species data and creates an array from it the stores it in a variable
    country_data = np.genfromtxt('Country_Data.csv', delimiter=',', encoding=None, dtype=None)      #Imports the file containing country data and creates an array from it the stores it in a variable
    
    x= True                                                            #Sets variable x to True to run the while loop beneath
    while x ==True:                                                    #A while loop that keeps running until the variable x becomes false
        input_1 = input('Please enter the name of the country:')       #Asks user for the input of the first country
        length = len(pop_data)                                         #Stores the length of the data in the file pop_data in a variable
        index_1 = 0                                                    #initially sets the index to zero
        check = 0                                                      #sets the variable check to zero 
        for b in range(length):                                        #A for loop that goes through the length of the pop_data file
            if input_1 == (pop_data[b,0]):                             #if this statement was true then the code indented underneath will run
                index_1 = b                                            #If the input matches the data at a certain spot in the pop_data then the code indented underneath will run
                x = False                                              #Sets varaiable x to false
                check = 1                                              #Sets variable check to 1
                break                                                  #Breaks the for loop
        if check == 0:                                                 #If the variable check is 0 then run the code indented underneath
            print('Invalid input, try Again')                          #Tells user that there input is wrong
    
    q = True                                                           #assign q as True
    while q ==True:                                                    #while q is equal to True
        input_2 = input('Please enter the name of the second country:')#assign input_2 to input second country
        length = len(pop_data)                                         #assign length to length of pop_data
        index_2 = 0                                                    #assign index_2 to 0
        p = 0                                                          #assign p to 0
        check = 0                                                      #assign check to 0
        for p in range(length):                                        #for loop of for p in range(length)
            if input_2 == (pop_data[p,0]):                             #if input_2 is in the pop_data file in any row at the third column, execute the code indented underneath
                index_2 = p                                            #assign index_2 to p
                q = False                                              #assign q to False
                check = 1                                              # assign check to 1
                break                                                  #Breaks the loop
        if check == 0:                                                 #if check is equal to 0
            print('Invalid input, try Again')                          #print Invalid input, try Again

    y = True                                                           #assign y as True
    while y== True:                                                    #while y is equal to True
        input_y1= input('Please enter the first year between 2000 and 2020:') #assign input_y1 as input first year
        width = len(pop_data[0,:])                                     #assign width to the length of all the pop_data file 
        index_y1 = 0                                                   #assign index_y1 to 0
        i = 0                                                          #assign i to 0
        check = 0                                                      #assign check to 0
        for i in range(width):                                         #for i in range of width
            if input_y1 in (pop_data[0,i]):                            #if input_y1 in pop_data in the first row at any of the columns execute the code underneath
                if len(input_y1)==4:                                   #if length of input_y1 is equal to 4 execute the code indented underneath
                    index_y1 = i                                       #assign index_y1 to i
                    check = 1                                          #assign check to 1
                    y = False                                          #assign y to False
                    break                                              #Break the loop
        if check == 0:                                                 #if check is equal to 0
            print('Please enter a year for which the data is available')#print Please enter a year for which data is available
                
    y_1 = True                                                          #assign y1 to True
    while y_1 == True:                                                  #while y1 is equal to True
        input_y2= input('Please enter the later second year:')          #assign input_y2 to second year
        width = len(pop_data[0,:])                                      #assign width to length of the first row in the pop_data file
        index_y2 = 0                                                    #assign index_y2 to 0
        i_1 = 0                                                         #assign i_1 to 0
        check = 0                                                       #assign check to 0
        for i_1 in range(width):                                        #for i_1 in range of width
            if input_y2 in (pop_data[0,i_1]):                           #if input_y2 in pop_data at the firsst row in any column execute the indented code underneath
                if len(input_y2)==4:                                    #if length of input_y2 is equal to 4
                    index_y2 = i_1                                      #assign index_y2 to i_1
                    check = 1                                           #assign check to 1
                    y_1 = False                                         #assign y1 to False
                    break                                               #Breaks the loop
        if check == 0:                                                  #if check is equal to 0
                print('Please enter a year for which the data is available') #print Please enter a year for which data is available
                
    change_pop1 , change_pop2, total_specie1, total_specie2, max1, max2, specie_type1,specie_type2,density_1,density_2 = finder_funct(index_1,index_2,index_y1,index_y2, pop_data, specie_data, country_data) #call finder function and send it info
    bigger_dpop = max(change_pop1,change_pop2)                          #bigger_dpop is max of (change_pop1 and change_pop2)
    if bigger_dpop == change_pop1:                                      #if bigger_dpop is equal to change_pop1
        biggest_dpop = input_1                                          #biggest_dpop is input_1
    elif bigger_dpop == change_pop2:                                    #else if bigger_dpop is equal to change_pop2
        biggest_dpop = input_2                                          #biggest_dpop is input_2
    if total_specie1 > total_specie2:                                   #if total_specie1 is greater than total_speice2
        most_threatened = input_1                                       #most_threatened is input_1
    if total_specie2 > total_specie1:                                   #if total_specie2 is greater than total_specie1
        most_threatened = input_2                                       #most_threatened is input_2
    if (int(country_data[index_1,3]) > (int(country_data[index_2,3]))): #if the area of the first inputted country is greateer than the second inputted country execute code indented underneath
        bigger_area = input_1                                           #bigger_area is input_1
    elif (int(country_data[index_2,3])) > (int(country_data[index_1,3])):       #if the area of the second inputted country is greateer than the first inputted country execute code indented underneath
        bigger_area = input_2                                                   #bigger_area is equal to input_2
    locreg_1,locsubreg_1 = country_data[index_1,1], country_data[index_1,2]     #assign locreg_1,locsubreg_1 to country_data[index_1,1], country_data[index_1,2]
    locreg_2,locsubreg_2 = country_data[index_2,1], country_data[index_2,2]     #assign locreg_2,locsubreg_2 to country_data[index_2,1], country_data[index_2,2]
    caller_class = Putter_togetherer(input_1,input_2,change_pop1 , change_pop2,total_specie1, total_specie2, max1, max2,specie_type1, specie_type2,biggest_dpop, most_threatened,bigger_area,input_y1, input_y2,density_1,density_2,locreg_1,locsubreg_1,locreg_2,locsubreg_2) #assign caller_class to call the Putter_togetherer class of given parameter
    caller_class.printer()                                                      #calls the printer function inside the class function
    grapher_er(index_1,index_2, index_y1,index_y2,pop_data,input_1,input_2,total_specie1,total_specie2,country_data, locsubreg_1,locsubreg_2)   #call grapher_er function of given parameter
if __name__ == '__main__':                                                      #makes sure only the desired piece of code is running
    main()                                                                      #Calls the main function

    
    

    



    
    


