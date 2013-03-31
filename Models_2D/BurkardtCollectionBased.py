from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2013 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)

import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them


import pyeq2.Model_2D_BaseClass


BurkhardtCollectionWebReference_1 = 'http://people.sc.fsu.edu/~jburkardt/m_src/prob/prob.html'



class arcsin_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Arcsin CDF Based"
    _HTML = 'y = a * asin( (bx+c) / d) / pi'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp =  a * numpy.arcsin( (b*x_in+c) / d) / numpy.pi
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * asin( (b * x_in + c) / d) / 3.14159265358979323846;\n"
        return s



class arcsin_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Arcsin PDF Based"
    _HTML = 'y = a / ( pi * sqrt( b<sup>2</sup> - x<sup>2</sup>))'
    __leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = BurkhardtCollectionWebReference_1
    
    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a / ( numpy.pi * numpy.power(b*b - x_in*x_in, 0.5))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp =  a / (3.14159265358979323846 * pow(b*b - x_in*x_in, 0.5));\n"
        return s


    
class bradford_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Bradford CDF Based"
    _HTML = 'ln(1.0+c*(x-a)/(b-a)) / ln(c+1.0)'
    __leftSideHTML = 'y'
    _coefficientDesignators = ['a','b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = BurkhardtCollectionWebReference_1
    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = numpy.log(1.0+c*(x_in-a)/(b-a)) / numpy.log(c+1.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = log(1.0+c*(x_in-a)/(b-a)) / log(c+1.0);\n"
        return s



class bradford_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Bradford PDF Based"
    _HTML = 'y = c / (( c * (x-a) + b-a) * ln(c + 1.0))'
    __leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = BurkhardtCollectionWebReference_1
    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = c / (( c * (x_in-a) + b-a) * numpy.log(c + 1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = c / (( c * (x_in-a) + b-a) * log(c + 1.0));\n"
        return s



    
    
    
undefinedString = ''
undefinedBoolean = False
undefinedList = []
    
    
    
    

class burr_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Burr CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = burr_cdf ( x, a, b, c, d )
  if ( x <= a )
    cdf = 0.0;
  else
    cdf = 1.0 / ( 1.0 + ( b / ( x - a ) )^c  )^d;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class burr_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Burr PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = burr_pdf ( x, a, b, c, d )
  if ( x <= a )
    pdf = 0.0;
  else
    y = ( x - a ) / b;
    pdf = ( c * d / b ) * y^( - c - 1.0 ) * ( 1.0 + y^( -c ) )^( - d - 1.0 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class cardioid_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Cardioid CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = cardioid_cdf ( x, a, b )
  if ( x <= a - pi )
    cdf = 0.0;
  elseif ( x < a + pi )
    cdf = ( pi + x - a + 2.0 * b * sin ( x - a ) ) / ( 2.0 * pi );
  else
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class cardioid_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Cardioid PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = cardioid_pdf ( x, a, b )
  pdf = ( 1.0 + 2.0 * b * cos ( x - a ) ) / ( 2.0 * pi );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class cauchy_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Cauchy CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = cauchy_cdf ( x, a, b )
  y = ( x - a ) / b;
  cdf = 0.5 + atan ( y ) / pi;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class cauchy_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Cauchy PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = cauchy_pdf ( x, a, b )
  y = ( x - a ) / b;
  pdf = 1.0 / ( pi * b * ( 1.0 + y * y ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class circular_normal_01_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Circular Normal 01 PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = circular_normal_01_pdf ( x, pdf )
  pdf = exp ( - 0.5 * ( x(1)^2 + x(2)^2 ) ) / ( 2.0 * pi );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class circular_normal_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Circular Normal PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = circular_normal_pdf ( x, a, b )
  d = ( ( x(1) - a(1) ).^2 + ( x(2) - a(2) ).^2 ) / b^2;
  pdf = exp ( - 0.5 * d ) / ( 2.0D+00 * b^2 * pi );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class cosine_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Cosine CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = cosine_cdf ( x, a, b )
  if ( x <= a - pi * b )
    cdf = 0.0;
  elseif ( x <= a + pi * b )
    y = ( x - a ) / b;
    cdf = 0.5 + ( y + sin ( y ) ) / ( 2.0 * pi );
  elseif ( a + pi * b < x )
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class cosine_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Cosine PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = cosine_pdf ( x, a, b )
  if ( x < a - pi * b )
    pdf = 0.0;
  elseif ( x <= a + pi * b )
    y = ( x - a ) / b;
    pdf = 1.0 / ( 2.0 * pi * b ) * cos ( y );
  elseif ( a + pi * b < x )
    pdf = 0.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class dipole_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Dipole CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = dipole_cdf ( x, a, b )
  cdf = 0.5 + ( 1.0 / pi ) * atan ( x ) + b * b * ( x * cos ( 2.0 * a ) ...
    - sin ( 2.0 * a ) ) / ( pi * ( 1.0 + x * x ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class dipole_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Dipole PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = dipole_pdf ( x, a, b )
  pdf = 1.0 / ( pi * ( 1.0 + x * x ) ) ...
    + b * b * ( ( 1.0 - x * x ) * cos ( 2.0 * a ) ...
    + 2.0 * x * sin ( 2.0 * x ) ) / ( pi * ( 1.0 + x * x ) * ( 1.0 + x * x ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class exponential_01_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Exponential 01 CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = exponential_01_cdf ( x )
  if ( x <= 0.0 )
    cdf = 0.0;
  else
    cdf = 1.0 - exp ( - x );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class exponential_01_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Exponential 01 PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = exponential_01_pdf ( x )
  if ( x < 0.0 )
    pdf = 0.0;
  else
    pdf = exp ( - x );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class exponential_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Exponential PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = exponential_pdf ( x, a, b )
  if ( x < a )
    pdf = 0.0;
  else
    pdf = ( 1.0 / b ) * exp ( ( a - x ) / b );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class extreme_values_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Extreme Values CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = extreme_values_cdf ( x, a, b )
  y = ( x - a ) / b;
  cdf = exp ( - exp ( - y ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class extreme_values_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Extreme Values PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = extreme_values_pdf ( x, a, b )
  pdf = ( 1.0 / b ) * exp ( ( a - x ) / b - exp ( ( a - x ) / b ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class fisk_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Fisk CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = fisk_cdf ( x, a, b, c )
  if ( x <= a )
    cdf = 0.0;
  else
    cdf = 1.0 / ( 1.0 + ( b / ( x - a ) )^c );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class fisk_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Fisk PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = fisk_pdf ( x, a, b, c )
  if ( x <= a )
    pdf = 0.0;
  else
    y = ( x - a ) / b;
    pdf = ( c / b ) * y^( c - 1.0 ) / ( 1.0 + y^c )^2;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class folded_normal_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Folded Normal PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = folded_normal_pdf ( x, a, b )
  if ( x < 0.0 )
    pdf = 0.0;
  else
    pdf = sqrt ( 2.0 / pi ) * ( 1.0 / b ) * cosh ( a * x / ( b * b ) ) ...
      * exp ( -0.5 * ( x * x + a * a ) / ( b * b ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class frechet_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Frechet CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = frechet_cdf ( x, alpha )
  if ( alpha <= 0.0 )
    fprintf ( 1, '\n' );
    fprintf ( 1, 'FRECHET_CDF - Fatal error!\n' );
    fprintf ( 1, '  ALPHA <= 0.0.\n' );
    error ( 'FRECHET_CDF - Fatal error!' );
  if ( x <= 0.0 )
    cdf = 0.0;
  else
    cdf = exp ( - 1.0 / x^alpha );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class frechet_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Frechet PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = frechet_pdf ( x, alpha )
  if ( alpha <= 0.0 )
    fprintf ( 1, '\n' );
    fprintf ( 1, 'FRECHET_PDF - Fatal error%\n' );
    fprintf ( 1, '  ALPHA <= 0.0.\n' );
    error ( 'FRECHET_PDF - Fatal error%' );
  pdf = alpha * exp ( - 1.0 / x^alpha ) / x^( alpha + 1.0 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class genlogistic_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Genlogistic CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = genlogistic_cdf ( x, a, b, c )
  y = ( x - a ) / b;
  cdf = 1.0 / ( 1.0 + exp ( - y ) )^c;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class genlogistic_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Genlogistic PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = genlogistic_pdf ( x, a, b, c )
  y = ( x - a ) / b;
  pdf = ( c / b ) * exp ( - y ) / ( 1.0 + exp ( - y ) )^( c + 1.0 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class gompertz_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gompertz CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = gompertz_cdf ( x, a, b )
  if ( x <= 0.0 )
    cdf = 0.0;
  else
    cdf = 1.0 - exp ( - b * ( a^x - 1.0 ) / log ( a ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class gompertz_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gompertz PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = gompertz_pdf ( x, a, b )
  if ( x < 0.0 )
    pdf = 0.0;
  elseif ( 1.0 < a )
    pdf = exp ( log ( b ) + x * log ( a ) - ( b / log ( a ) ) * ( a^x - 1.0 ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class gumbel_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gumbel CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = gumbel_cdf ( x )
  cdf = exp ( - exp ( - x ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class gumbel_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gumbel PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = gumbel_pdf ( x )
  pdf = exp ( - x - exp ( - x ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class half_normal_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Half Normal PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = half_normal_pdf ( x, a, b )
  if ( x <= a )
    pdf = 0.0;
  else
    y = ( x - a ) / b;
    pdf = sqrt ( 2.0 / pi ) * ( 1.0 / b ) * exp ( - 0.5 * y * y );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class inverse_gaussian_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Inverse_gaussian PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = inverse_gaussian_pdf ( x, a, b )
  if ( x <= 0.0 )
    pdf = 0.0;
  else
    pdf = sqrt ( b / ( 2.0 * pi * x^3 ) ) * ...
      exp ( - b * ( x - a )^2 / ( 2.0 * a^2 * x ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class laplace_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Laplace CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = laplace_cdf ( x, a, b )
  y = ( x - a ) / b;
  if ( x <= a )
    cdf = 0.5 * exp ( y );
  else
    cdf = 1.0 - 0.5 * exp ( - y );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class laplace_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Laplace PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = laplace_pdf ( x, a, b )
  pdf = exp ( - abs ( x - a ) / b ) / ( 2.0 * b );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class levy_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Levy PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = levy_pdf ( x, a, b )
  if ( b <= 0.0 )
    fprintf ( 1, '\n' );
    fprintf ( 1, '  LEVY_PDF - Fatal error!\n' );
    fprintf ( 1, '  Input parameter B <= 0.0\n' );
    error ( 'LEVY_PDF - Fatal error!' );
  if ( x < a )
    pdf = 0.0;
  else
    pdf = sqrt ( b / ( 2.0 * pi ) ) ...
        * exp ( - b / ( 2.0 * ( x - a ) ) ) ...
        / sqrt ( ( x - a )^3 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class log_normal_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log Normal PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = log_normal_pdf ( x, a, b )
  if ( x <= 0.0 )
    pdf = 0.0;
  else
    pdf = exp ( -0.5 * ( ( log ( x ) - a ) / b )^2 ) ...
      / ( b * x * sqrt ( 2.0 * pi ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class log_uniform_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log_uniform CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = log_uniform_cdf ( x, a, b )
  if ( x <= a )
    cdf = 0.0;
  elseif ( x < b )
    cdf = ( log ( x ) - log ( a ) ) / ( log ( b ) - log ( a ) );
  else
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class log_uniform_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log_uniform PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = log_uniform_pdf ( x, a, b )
  if ( x < a )
    pdf = 0.0;
  elseif ( x <= b )
    pdf = 1.0 / ( x * ( log ( b ) - log ( a ) ) );
  else
    pdf = 0.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class logistic_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Logistic CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = logistic_cdf ( x, a, b )
  cdf = 1.0 / ( 1.0 + exp ( ( a - x ) / b ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class logistic_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Logistic PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = logistic_pdf ( x, a, b )
  temp = exp ( ( a - x ) / b );
  pdf = temp / ( b * ( 1.0D+00 + temp )^2 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class lorentz_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentz CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = lorentz_cdf ( x )
  cdf = 0.5 + atan ( x ) / pi;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class lorentz_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentz PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = lorentz_pdf ( x )
  pdf = 1.0 / ( pi * ( 1.0 + x * x ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class normal_01_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Normal 01 PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = normal_01_pdf ( x )
  pdf = exp ( -0.5 * x * x ) / sqrt ( 2.0 * pi );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class normal_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Normal PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = normal_pdf ( x, a, b )
  pdf = exp ( - 0.5 * ( ( x - a ) / b ).^2 )  / sqrt ( 2.0 * pi * b^2 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class pareto_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Pareto CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = pareto_cdf ( x, a, b )
  if ( x < a )
    cdf = 0.0;
  else
    cdf = 1.0 - ( a / x )^b;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class pareto_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Pareto PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = pareto_pdf ( x, a, b )
  if ( x < a )
    pdf = 0.0;
  else
    pdf = b * a^b / x^( b + 1.0 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class power_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Power CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = power_cdf ( x, a, b )
  if ( x <= 0.0 )
    cdf = 0.0;
  elseif ( x <= b )
    cdf = ( x / b )^a;
  else
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class power_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Power PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = power_pdf ( x, a, b )
  if ( x < 0.0 | b < x )
    pdf = 0.0;
  else
    pdf = ( a / b ) * ( x / b )^( a - 1.0 );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class rayleigh_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Rayleigh CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = rayleigh_cdf ( x, a )
  if ( x < 0.0 )
    cdf = 0.0;
  else
    cdf = 1.0 - exp ( - x * x / ( 2.0 * a * a ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class rayleigh_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Rayleigh PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = rayleigh_pdf ( x, a )
  if ( x < 0.0 )
    pdf = 0.0;
  else
    pdf = ( x / ( a * a ) ) * exp ( - x * x / ( 2.0 * a * a ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class reciprocal_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Reciprocal CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = reciprocal_cdf ( x, a, b )
  if ( x <= 0.0 )
    cdf = 0.0;
  elseif ( 0.0 < x )
    cdf = log ( a / x ) / log ( a / b );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class reciprocal_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Reciprocal PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = reciprocal_pdf ( x, a, b )
  if ( x <= 0.0 )
    pdf = 0.0;
  elseif ( 0.0 < x )
    pdf = 1.0 / ( x * log ( b / a ) );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class sech_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sech CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = sech_cdf ( x, a, b )
  y = ( x - a ) / b;
  cdf = 2.0 * atan ( exp ( y ) ) / pi;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class semicircular_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Semicircular CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = semicircular_cdf ( x, a, b )
  if ( x <= a - b )
    cdf = 0.0;
  elseif ( x <= a + b )
    y = ( x - a ) / b;
    cdf = 0.5 + ( y * sqrt ( 1.0 - y * y ) + asin ( y ) ) / pi;
  elseif ( a + b < x )
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class semicircular_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Semicircular PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = semicircular_pdf ( x, a, b )
  if ( x < a - b )
    pdf = 0.0;
  elseif ( x <= a + b )
    y = ( x - a ) / b;
    pdf = 2.0 / ( b * pi ) * sqrt ( 1.0 - y * y );
  elseif ( a + b < x )
    pdf = 0.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class triangle_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Triangle CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = triangle_cdf ( x, a, b, c )
  if ( x <= a )
    cdf = 0.0;
  elseif ( x <= b )
    if ( a == b )
      cdf = 0.0;
    else
      cdf = ( x - a ) * ( x - a ) / ( b - a ) / ( c - a );
  elseif ( x <= c )
    cdf = ( b - a ) / ( c - a ) + ( 2.0 * c - b - x ) * ( x - b ) / ( c - b ) / ( c - a );
  else
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class triangle_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Triangle PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = triangle_pdf ( x, a, b, c )
  if ( x <= a )
    pdf = 0.0;
  elseif ( x <= b )
    if ( a == b )
      pdf = 0.0;
    else
      pdf = 2.0 * ( x - a ) / ( b - a ) / ( c - a );
  elseif ( x <= c )
    if ( b == c )
      pdf = 0.0;
    else
      pdf = 2.0 * ( c - x ) / ( c - b ) / ( c - a );
  else
    pdf = 0.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class triangular_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Triangular CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = triangular_cdf ( x, a, b )
  if ( x <= a )
    cdf = 0.0;
  elseif ( x <= 0.5 * ( a + b ) )
    cdf = 2.0 * ( x * x - 2.0 * a * x + a * a ) / ( b - a )^2;
  elseif ( x <= b )
    cdf = 0.5 + ( -2.0 * x * x + 4.0 * b * x + 0.5 * a * a ...
      - a * b - 1.5 * b * b ) / ( b - a )^2;
  else
    cdf = 1.0;
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class uniform_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Uniform CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = uniform_cdf ( x, a, b )
  if ( x < a )
    cdf = 0.0;
  elseif ( b < x )
    cdf = 1.0;
  else
    cdf = ( x - a ) / ( b - a );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class weibull_cdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull CDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function cdf = weibull_cdf ( x, a, b, c )
  if ( x < a )
    cdf = 0.0;
  else
    y = ( x - a ) / b;
    cdf = 1.0 - 1.0 / exp ( y^c );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class weibull_pdf(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull PDF Based"
    _HTML = undefinedString
    __leftSideHTML = 'y'
    _coefficientDesignators = undefinedList
    _canLinearSolverBeUsedForSSQABS = undefinedBoolean
    
    webReferenceURL = BurkhardtCollectionWebReference_1

    '''
function pdf = weibull_pdf ( x, a, b, c )
  if ( x < a )
    pdf = 0.0;
  else
    y = ( x - a ) / b;
    pdf = ( c / b ) * y^( c - 1.0 )  / exp ( y^c );
'''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = undefinedBoolean
    autoGenerateOffsetForm = undefinedBoolean
    autoGenerateReciprocalForm = undefinedBoolean
    autoGenerateInverseForms = undefinedBoolean
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = undefinedBoolean
    independentData1CannotContainPositiveFlag = undefinedBoolean
    independentData1CannotContainNegativeFlag = undefinedBoolean
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        undefined
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        undefined
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        undefined
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s


