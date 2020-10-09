import numpy as np

np_arr = np.array((10,22,3,40,5))
print(np_arr)
print(np.__version__)
print(type(np_arr))
np_arr.sort()
print(np_arr)

np_zero = np.array(20)
print(np_zero)

np_two = np.array([[1,2,3],[4,5,6]])
print(np_two)

np_three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]] )
print(np_three,' ',np_three.ndim,' ',np_three.nbytes)

np_five = np.array([1,2,3,4,5],ndmin=5)
print(np_five,' ',np_five.ndim)

print(np_two[0,-1])
print(np_three[1,1,2])
print(np_arr[::-1])
print(np_two[1,::-1])
print(np_two[0:2,1])
print(np_two[0:2,1:2])


#copy and view
np_arr1 = np.array([1,2,3,4,5,6,7])


np_vew = np_arr1.view()
print(np_vew)
np_vew[0]=22
print(np_vew," ",np_arr1," ",np_vew.base)

np_cpy = np_arr1.copy()
np_cpy[0] = 11
print(np_arr1,' ',np_cpy,' ',np_cpy.base)

#shape of array
print(np_five.shape)

#reshapping arrays
#converting 1D array into 2D array
np_one_d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
np_two_d = np_one_d.reshape(3,4)
print(np_two_d)

#converting 1D to 3D
np_three_d = np_one_d.reshape(3,2,-1)
print(np_three_d)

#flattening arrays converting multidimwntional arrays into 1D array
new_arr = np_two_d.reshape(-1)
print(new_arr,' ')


#iterating through array
#using nditer
for i in np.nditer(np_three_d[0:3,::1]):
    print(i)
#using ndenumerate
for x,i in np.ndenumerate(np_three_d):
    print(x,i)


#array joins

#using concatenate
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2),axis=0)
print(arr)

arr11 = np.array([[1, 2], [3, 4]])
arr22 = np.array([[5, 6], [7, 8]])
arr12 = np.concatenate((arr11,arr22),axis=1)
print(arr12)

#using stack
arr21 = np.stack((arr1,arr2))
print(arr21)

arr21 = np.hstack((arr1,arr2))
print(arr21)

arr21 = np.vstack((arr1,arr2))
print(arr21)

arr21 = np.dstack((arr1,arr2))
print(arr21)

#splitting arrays
a1 = np.array([1,2,3,4,5,6])
asp1 = np.split(a1,3 )
print(asp1)
asp2 = np.array_split(a1,4)
print(asp2)

#searching
#using where()
x = np.where(new_arr%2==0)
print(x)

#using searchsorted
y = np.searchsorted(new_arr,8)
print(y)

y = np.searchsorted(new_arr,8,side='right')
print(y)

z = np.searchsorted(new_arr,[1,2,3])
print(z)

#sorting
print(np.sort(new_arr))

#filtering arrays
arr_filt = np.array([1,2,3,4,5,6,7,8,9,10])
filt_arr = []
for i in arr_filt:
    if i%2 == 0:
        filt_arr.append(True)
    else:
        filt_arr.append(False)
print(filt_arr)

newarr = arr_filt[filt_arr]
print(newarr)

arr4 = (arr_filt%2==0)
newar = arr_filt[arr4]
print(newar)




