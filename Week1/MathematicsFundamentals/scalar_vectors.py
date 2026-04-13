# scalars and vectors
import numpy as np
#########################################################################
# # creating a vector
# u = np.array([5, 12])
# scalar = 3
# # scaling the vector with static number
# scaled_u = scalar * u
#########################################################################
# # ascertaining the magnitude of the vector
# magnitude_u = np.linalg.norm(u)

# print(u)
# print(scalar)
# print(scaled_u)
# print(magnitude_u)
#########################################################################
# # trying variations
# a = np.array((1,2,3,4,5,6), dtype = int)
# print(a)
# a = np.array({"1": 6, "2":5}, dtype = bool)
# print(a)

#########################################################################
# creating a matrix 
users = np.array([
    [45, 162, 67],
    [25, 180, 68],
    [70, 150, 73]
])

# print(users.shape)

# print(users[2, :])
# print(np.reshape(users, [6, 2]))

#########################################################################
# learning dot product, core mathematics used in a lot of concepts in
# data science and Neural Nets to find alignment and similarities between 2 vectors
# a = np.array([3, -2])

# b = np.array([1, 4])

# a_b = (sum(a[i]* b[i] for i in range(len(a))))
# print(a_b)

# dot = np.dot(a, b)
# print(dot)

#########################################################################
# transposing a matrix
# no inplace changes
# users_t = users.T
# data = np.array([
#     [45, 162, 67],
#     [25, 180, 68],
#     [70, 150, 73], 
#     [35, 190, 76]
# ])

# # prints transposed data matrix without inplace updates
# print(np.transpose(data))
# print("Transposed users matrix: \n", users_t)

#########################################################################
# # matrix multiplicaton allowing you to perform dot product on multiple vectors together
# # transpose used here for matching the sequence of both the vectors for multiplication
# # eg. V @ W.T
# query = np.array([
#     [21],
#     [3],
#     [56],
# ])

# mat_mul = data @ query
# print(mat_mul)

# product = np.matmul(data, query)
# print(product)

#########################################################################
# identity and inverse matrices
# identity = np.identity(3, dtype= int)
# eye = np.eye(3, dtype= int)
# print(eye)
# print(identity)
# print(identity.shape)

# i_users = np.linalg.inv(users)
# print(i_users)

# print(np.round(users @ i_users))
# print(users @ i_users)

#########################################################################
one = np.ones((2))
# print(one)

# an array with radom numbers 
random = np.random.rand(3,2) # a 3d array with 3x3x3
# print(random)
# det = np.linalg.det(random)
# print(det)

# # evenly spaced number array with n samples given as the 3rd argument.
# linspace = np.linspace(2, 10, 15) # start, end, no. of expected values
# print(np.round(linspace))
# print(linspace)

# # evenly spaced number array given n as the step value
# array1 = np.arange(2,10,2)
# array2 = np.arange(2,10,3)
# array3 = np.arange(2,10,8)
# print(array1)
# print(array2)
# print(array3)


# X = np.array([
#     [4,2],
#     [2,1]
# ])

# print(np.linalg.det(X))
# # numpy.linalg.LinAlgError: Singular matrix
# # print(np.linalg.inv(X))

#########################################################################
print(random)
print(random.reshape((1, -5)))   # specifying unknown dimension in the 2nd value of the argument tuple 
random.resize(2, 4)     # resizes the array in-place irrespective of the number of elements.
print(random)
#########################################################################

