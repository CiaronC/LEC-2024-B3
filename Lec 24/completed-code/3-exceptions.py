## Exceptions and Input Output

def main():
    
    try:
        
        filename = input('Enter GPA data file (gpa[1-4].txt): ')
        
        fileOpenedSuccessfully = False
        infile = open(filename) # May raise IO error
        fileOpenedSuccessfully = True
        
        print("Data file opened successfully.")
        
        gpa = loadGPAs(infile)
        
        print("GPA:")
        print(gpa)
        
    except IOError as error:
        print("File error:" + str(error))
    except ValueError as error:
        print("Value error: " + str(error))
    except RuntimeError as error:
        print("Runtime error: " + str(error))
    except Exception as error:
        print("Unknown Error: " + str(error))
    finally:
        if fileOpenedSuccessfully:
            infile.close()
            print("Data file closed successfully")
    
    print("Program ended.")


def loadGPAs(file):
    gpaValues = []
    line = file.readline()
    while line != "":
        val = float(line) # May raise a ValueError if the line is not numeric
        
        if not 0 <= val <= 4:
            raise RuntimeError("GPA is outside the valid range  0 and 4: " + val)
            
        gpaValues.append(val)
        
        line = file.readline()
    
    return gpaValues


main()

           
        
        
        
            

