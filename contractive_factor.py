
import numpy as np
import math
import matplotlib.pyplot as plt
# Contraction - power method
# P
# $
# P = W G
# $
### the G operator is :

# $ 
# I_n - \gamma A^T A
# $

########################################    POWER METHOD FOR SPECTRAL NORM   ####################
########################################                                    ######################


######################################################################################
######################################################################################
#------------------              POWER METHOD              ----------------------------

#we will plot the gain in norm of each step, the euclidean distance between the two vectors, and the dot product
#for each step
#the graph has to be very crips and presentable and self explanatory
def plot_power_method(norm_gain_list, euclidean_distance_list, dot_product_list, save=False):
    # Plot the norm gain data
    plt.scatter(range(len(norm_gain_list)), norm_gain_list, color='red', label='norm gain')
    plt.plot(range(len(norm_gain_list)), norm_gain_list, color='salmon', linewidth=1.5)

    # Plot the euclidean distance data
    plt.scatter(range(len(euclidean_distance_list)), euclidean_distance_list, color='blue', label='euclidean distance')
    plt.plot(range(len(euclidean_distance_list)), euclidean_distance_list, color='lightblue', linewidth=1.5)

    # Plot the dot product data
    plt.scatter(range(len(dot_product_list)), dot_product_list, color='green', label='cosine similarity')
    plt.plot(range(len(dot_product_list)), dot_product_list, color='lightgreen', linewidth=1.5)

    # Label the x-axis
    plt.xlabel('iteration')

    # Add a legend to the plot
    plt.legend(loc='center right')

    # Label the last iteration on the x-axis
    plt.annotate(str(len(norm_gain_list)-1), xy=(len(norm_gain_list)-1, 0), xycoords='data',
                xytext=(0,-30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=-0.2"),
                ha='center', va='bottom', fontsize=10, color='r',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3)
                )
    plt.gca().tick_params(axis='x', which='major', pad=15)

    # Increase tick frequency for y axis intervals were more values are present
    # plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    
    # Plot the y-axis values for all 3 metrics at the last iteration
    last_iter = len(norm_gain_list) - 1
    y_ticks = [norm_gain_list[last_iter], euclidean_distance_list[last_iter], dot_product_list[last_iter]]
    x_ticks = [last_iter] * len(y_ticks)
    # #print only 3 decimal places
    plt.annotate(str(round(norm_gain_list[last_iter], 3)), xy=(last_iter, norm_gain_list[last_iter]), xycoords='data',
                xytext=(0, -15), textcoords='offset points',
                ha='center', va='bottom', fontsize=10, color='salmon',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3)
                )
    plt.annotate(str(round(dot_product_list[last_iter], 3)), xy=(last_iter, dot_product_list[last_iter]), xycoords='data',
                xytext=(0, -45), textcoords='offset points',  
                ha='center', va='bottom', fontsize=10, color='lightgreen',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3)
                )
    #for euclidean distance print the value above the point with distance 10 and left of the point with distance 5
    #only print 3 decimal places
    plt.annotate(str(round(euclidean_distance_list[last_iter], 3)), xy=(last_iter, euclidean_distance_list[last_iter]), xycoords='data',
                xytext=(-5, 10), textcoords='offset points',
                ha='center', va='bottom', fontsize=10, color='lightblue',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3)
                )
    #  

    # Show the plot
    plt.show()
    # #if save is true, save the plot
    # if save:
    #     plt.savefig('/home/lisa/bhartendu/kernal_convergence/power_method_plot.png', dpi=300, bbox_inches='tight')
def power_method_for_images(f, f_adjoint, input_image, args_dict, max_iterations=1000, \
                            norm_tolerance=1e-8, dot_tolerance=1e-12, plot= True, verbose = True):
    
    m, n = input_image.shape
    #create 3 lists to store the gain in norm, euclidean distance, and dot product
    norm_gain_list = []
    euclidean_distance_list = []
    dot_product_list = []
    #initialize variables
    i = 0
    euclidean_distance = 1e+5
    cos_distance = -1
    #create a random image
    v = np.random.rand(m, n)
    #x to double
    v = x.astype(np.float64)
    v /= np.linalg.norm(v, 'fro')

    #create another random image
    u = np.random.rand(m, n)
    #u to double
    u = u.astype(np.float64)
    u /= np.linalg.norm(u, 'fro')
    
    for i in range(max_iterations):
        u = f(v, **args_dict)
        #the norm of u is the gain in this step
        u_norm = np.linalg.norm(u, 'fro')
        u_new = u / u_norm 

        #update v
        v = f_adjoint(u_new, **args_dict)
        #the norm of v is the gain in this step
        v_norm = np.linalg.norm(v, 'fro')
        v_new = v / v_norm

        #sigma is dot product of u_new and f(v_new, **args_dict)
        sigma = np.dot(u_new.flatten(), f(v_new, **args_dict).flatten())
        
        euclidean_distance = np.linalg.norm(u_new - u, 'fro')
        cos_distance = np.sum(np.multiply(u_new,u))

        #append the gain in norm to the list
        norm_gain_list.append(sigma)
        #append the euclidean distance to the list
        euclidean_distance_list.append(euclidean_distance)
        #append the dot product to the list
        dot_product_list.append(cos_distance)
        # if euclidean_distance < norm_tolerance:
        #use math.isclose to get close to zero with norm_tolerance
        if math.isclose(euclidean_distance, 0, abs_tol=norm_tolerance):
            #print the return reason
            #that the norm of the difference between x_new and x is less than tolerance
            # print('Converged at iteration', i, 'because the norm of the difference between x_new and x is less than tolerance')
            #print converged as the norm of the difference between x_new and x is less than tolerance
            if verbose:
                print('Converged because the norm of the difference between x_new and x is less than tolerance')
            break
        #as both x_new and x are unit norm images, we can check if the cosine of the angle between them is
        #  less than tolerance, and the dot product of the two vectors is the cosine of the angle between them
        #just to stop we can check if the dot product is less than more than 1-tolerance
        #first take sum and then take sum, to get the dot product of two matrices
        # if np.sum(np.multiply(x_new,x)) >= 1-dot_tolerance:
        #we will test if the dot product close to 1, then we will stop
        #use the tolerance as dot_tolerance, and function for checking close
        
        if math.isclose(cos_distance, 1, abs_tol=dot_tolerance, rel_tol=dot_tolerance):
            #print the return reason
            #that the dot product is greater than 1-tolerance
            if verbose:
                print('Converged because the dot product is greater than 1-tolerance')
            break
        u = u_new
        v = v_new
    #print iterations at which the power method is stopped
    #if i==max_iterations:, we print not converged

    if verbose:
        if i==max_iterations:
            print('Not converged')

        print('iteration', i)
        #print euclidean distance
        print('Euclidean distance', euclidean_distance)
        #also print the dot product of x_new and x
        print('cosine similarity', cos_distance)

    #PLOTTING
    if plot:
        #plot the dictionary
        plot_power_method(norm_gain_list, euclidean_distance_list, dot_product_list)
    # return np.linalg.norm(y, 'fro')
    return sigma


#we will define power method in scaled inner product space
#there is a matrix D which is a diagonal matrix with diagonal entries as the scaling factors
#so we will use the eigen values of the matrix D^(1/2) P^T P D^(-1/2)
#this is the matrix whose eigen values we will use to find the spectral norm in scaled inner product space

def power_method_for_images_scaled_inner_product( f, f_adjoint, D, D_matrix, input_image, args_dict, max_iterations=1000, \
                            norm_tolerance=1e-8, dot_tolerance=1e-12, plot= True, verbose = True):
    
    m, n = input_image.shape
    #create 3 lists to store the gain in norm, euclidean distance, and dot product
    norm_gain_list = []
    euclidean_distance_list = []
    dot_product_list = []
    #initialize variables
    i = 0
    euclidean_distance = 1e+5
    cos_distance = -1

    #create a random image
    x = np.random.rand(m, n)
    #x to double
    x = x.astype(np.float64)
    x /= np.linalg.norm(x, 'fro')

    for i in range(max_iterations):
        y = D(input_image=f_adjoint( f(D(input_image=x, D_matrix=D_matrix, D_power=-1/2), **args_dict) , **args_dict),\
              D_matrix=D_matrix, D_power=1/2)
        #the norm of y is the gain in this step
        y_norm = np.linalg.norm(y, 'fro')
        x_new = y / y_norm 
        
        euclidean_distance = np.linalg.norm(x_new - x, 'fro')
        cos_distance = np.sum(np.multiply(x_new,x))

        #append the gain in norm to the list
        norm_gain_list.append(y_norm)
        #append the euclidean distance to the list
        euclidean_distance_list.append(euclidean_distance)
        #append the dot product to the list
        dot_product_list.append(cos_distance)
        # if euclidean_distance < norm_tolerance:
        #use math.isclose to get close to zero with norm_tolerance
        if math.isclose(euclidean_distance, 0, abs_tol=norm_tolerance):
            #print the return reason
            #that the norm of the difference between x_new and x is less than tolerance
            # print('Converged at iteration', i, 'because the norm of the difference between x_new and x is less than tolerance')
            #print converged as the norm of the difference between x_new and x is less than tolerance
            if verbose:
                print('Converged because the norm of the difference between x_new and x is less than tolerance')
            break
        #as both x_new and x are unit norm images, we can check if the cosine of the angle between them is
        #  less than tolerance, and the dot product of the two vectors is the cosine of the angle between them
        #just to stop we can check if the dot product is less than more than 1-tolerance
        #first take sum and then take sum, to get the dot product of two matrices
        # if np.sum(np.multiply(x_new,x)) >= 1-dot_tolerance:
        #we will test if the dot product close to 1, then we will stop
        #use the tolerance as dot_tolerance, and function for checking close
        
        if math.isclose(cos_distance, 1, abs_tol=dot_tolerance, rel_tol=dot_tolerance):
            #print the return reason
            #that the dot product is greater than 1-tolerance
            if verbose:
                print('Converged because the dot product is greater than 1-tolerance')
            break
        x = x_new
    #print iterations at which the power method is stopped
    #if i==max_iterations:, we print not converged

    if verbose:
        if i==max_iterations:
            print('Not converged')

        print('iteration', i)
        #print euclidean distance
        print('Euclidean distance', euclidean_distance)
        #also print the dot product of x_new and x
        print('cosine similarity', cos_distance)

    #PLOTTING
    if plot:
        #plot the dictionary
        plot_power_method(norm_gain_list, euclidean_distance_list, dot_product_list)
    # return np.linalg.norm(y, 'fro')
    return np.linalg.norm(y, 'fro')


######################################################################################
######################################################################################
#------------------              POWER METHOD ENDS         ----------------------------