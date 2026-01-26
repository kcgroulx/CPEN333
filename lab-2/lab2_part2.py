#Lab 2 (part 1)
#student name: Kyle Groulx
#student number: 95104774

from __future__ import annotations  #helps with type hints
from tkinter import *
#do not import any more modules

class ComplexNumber:
    """ 
        this class implements the complex number type 
        two data fields: 
            real and imag (imaginary)
        Operation: 
            add, subtract, multiply and divide
            toString
    """
    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag
    
    def add(self, secondComplex: ComplexNumber) -> ComplexNumber:
        """
           adds 'this' complex to secondComplex
           returns the result as a complex number (type ComplexNumber)
        """
        real = self.real + secondComplex.real
        imag = self.imag + secondComplex.imag
        num = ComplexNumber(real=real, imag=imag)
        return num
    
    def subtract(self, secondComplex: ComplexNumber) -> ComplexNumber:
        """
           subtracts secondComplex from 'this' complex to 
           returns the result as a complex number (type complex)
        """
        real = self.real - secondComplex.real
        imag = self.imag - secondComplex.imag
        num = ComplexNumber(real=real, imag=imag)
        return num

    def multiply(self, secondComplex: ComplexNumber) -> ComplexNumber:
        """
           multiplies 'this' complex to secondComplex
           returns the result as a complex number (type ComplexNumber)
        """ 
        real = (self.real * secondComplex.real) - (self.imag * secondComplex.imag)
        imag = (self.real * secondComplex.imag) + (self.imag * secondComplex.real)
        return ComplexNumber(real=real, imag=imag)


    def divide(self, secondComplex: ComplexNumber) -> ComplexNumber:
        """
           divides 'this' complex by secondComplex
           returns the result as a complex number (type ComplexNumber)
        """ 
        denominator = (secondComplex.real ** 2) + (secondComplex.imag ** 2)
        real = ((self.real * secondComplex.real) + (self.imag * secondComplex.imag)) / denominator
        imag = ((self.imag * secondComplex.real) - (self.real * secondComplex.imag)) / denominator
        return ComplexNumber(real=real, imag=imag)

    def toString(self) -> str:
        """             
            returns a string representation of 'this' complex number
            the general output format is: {real} + {imag} i

            Special Cases:
                - Both real and imag are 0: Return 0
                - real is 0: Only show imag
                - imag is 0: Only show real
                - imag is 1/-1: Don't show coefficient infront of i
        """

        if self.real == 0 and self.imag == 0:
            return "0"

        parts = []
        if self.real != 0:
            parts.append(f"{self.real}")

        if self.imag != 0:
            imag_abs = abs(self.imag)
            imag_str = "i" if imag_abs == 1 else f"{imag_abs} i"
            if parts:
                sign = " + " if self.imag > 0 else " - "
                parts.append(f"{sign}{imag_str}")
            else:
                sign = "-" if self.imag < 0 else ""
                parts.append(f"{sign}{imag_str}")

        return "".join(parts)

class GUI:
    """ 
        this class implements the GUI for our program
        use as is.
        The add, subtract, multiply and divide methods invoke the corresponding
        methods from the ComplexNumber class to calculate the result to display.
    """
    def __init__(self):
        """ 
            The initializer creates the main window, label and entry widgets,
            and starts the GUI mainloop.
        """
        window = Tk()
        window.title("Complex Numbers")
        window.geometry("190x180")
       
        # Labels and entries for the first complex number
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)

        Label(frame1, text = "Complex 1:").pack(side = LEFT)
        self.complex1Real = StringVar()
        Entry(frame1, width = 4, textvariable = self.complex1Real, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "+").pack(side = LEFT)
        self.complex1Imag = StringVar()
        Entry(frame1, width = 4, textvariable = self.complex1Imag, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "i").pack(side = LEFT)
        
        # Labels and entries for the second complex number
        frame2 = Frame(window)
        frame2.grid(row = 3, column = 1, pady = 10)
        Label(frame2, text = "Complex 2:").pack(side = LEFT)
        self.complex2Real = StringVar()
        Entry(frame2, width = 4, textvariable = self.complex2Real, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "+").pack(side = LEFT)
        self.complex2Imag = StringVar()
        Entry(frame2, width = 4, textvariable = self.complex2Imag, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "i").pack(side = LEFT)
        
        # Labels and entries for the result complex number
        # an entry widget is used as the output here
        frame3 = Frame(window)
        frame3.grid(row = 4, column = 1, pady = 10)
        Label(frame3, text = "Result:     ").pack(side = LEFT)
        self.result = StringVar()
        Entry(frame3, width = 10, textvariable = self.result, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)

        # Buttons for add, subtract, multiply and divide
        frame4 = Frame(window) # Create and add a frame to window
        frame4.grid(row = 5, column = 1, pady = 5, sticky = E)
        Button(frame4, text = "Add", command = self.add).pack(
            side = LEFT)
        Button(frame4, text = "Subtract", 
               command = self.subtract).pack(side = LEFT)
        Button(frame4, text = "Multiply", 
               command = self.multiply).pack(side = LEFT)
        Button(frame4, text = "Divide", 
               command = self.divide).pack(side = LEFT)
               
        mainloop()
        
    def add(self): 
        (complex1, complex2) = self.getBothComplex()
        result = complex1.add(complex2)
        self.result.set(result.toString())
    
    def subtract(self):
        (complex1, complex2) = self.getBothComplex()
        if complex1 != None and complex2 != None:
            result = complex1.subtract(complex2)
            self.result.set(result.toString())
    
    def multiply(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.multiply(complex2)
        self.result.set(result.toString())
    
    def divide(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.divide(complex2)
        self.result.set(result.toString())

    def getBothComplex(self):
        """ Helper method used by add, subtract, multiply and divide methods """
        def get_entry(entry: StringVar) -> float:
            text = entry.get().strip()
            return 0 if text == "" else eval(text)

        try:
            real1 = get_entry(self.complex1Real)
            imag1 = get_entry(self.complex1Imag)
            complex1 = ComplexNumber(real1, imag1)

            real2 = get_entry(self.complex2Real)
            imag2 = get_entry(self.complex2Imag)
            complex2 = ComplexNumber(real2, imag2)
            return (complex1, complex2)
        except:
            return (ComplexNumber(0, 0), ComplexNumber(0, 0))

if __name__ == "__main__": GUI()
