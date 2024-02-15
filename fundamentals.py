import numpy as np

#Initialise one dimentional array
oneD = np.array([1,2,3,4,5])
print('one dimetional array')
print(oneD,'\n')

#Initialise one dimentional array with zero's
zeroOneD = np.zeros(5,int)
print('initialise one dimetional array with zeros')
print(zeroOneD)

#Initialise one dimentional array with zero's
onesOneD = np.ones(5,int)
print('initialise one dimetional array with ones')
print(onesOneD)

#Initialise one dimentional empty array with n
emptyOneD = np.empty(5,int)
print('initialise one dimetional empty array with n')
print(emptyOneD)

#Initialise one dimentional array with arrange of n
arrangeOneD = np.arange(5)
print('initialise one dimetional array with arrange of n')
print(arrangeOneD)

#Initialise one dimentional array with arrange of n with step 
arrangeStepOneD = np.arange(0,10,2)
print('initialise one dimetional array with arrange of n with step ')
print(arrangeStepOneD)

#Initialise one dimentional array by arranging elements linearly 
linspaceStepOneD = np.linspace(0,10,5,dtype=int)
print('initialise one dimetional array by arranging elements linearly ')
print(linspaceStepOneD)


#Initialise two dimentional array
twoD = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print('two dimetional array')
print(twoD,'\n')

#Initialise n dimentional array
nD = np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
print('n dimetional array')
print(nD,'\n')
