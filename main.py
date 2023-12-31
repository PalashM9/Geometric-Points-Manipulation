from random import random
import math
import numpy as np


#####################################################################################################################################################


class Points():
    minimum_distance = 0.0

    def generate_random_points(size_of_set, radius):
        horizontal_range = 0
        vertical_range = 0
        random_points = []
        for index in range(size_of_set):
            set = 2 * math.pi * random()
            set_value = radius * random()
            random_points.append(
                (horizontal_range + set_value * math.cos(set), vertical_range + set_value * math.sin(set)))
        return random_points

    # Distance formulae for calculating distance between two points
    def dist(horizontal_point, vertical_point):
        return math.sqrt(
            ((vertical_point[1] - horizontal_point[1]) ** 2) + ((vertical_point[0] - horizontal_point[0]) ** 2))

    # Function to set minimum distance for an iteration inside points class
    def set_minimum_dist(delta_distance):
        Points.minimum_distance = delta_distance

    def merge_sort_closest(points_set, length):
        min_dist = float("inf")
        horizontal_point = 0
        vertical_point = 0
        for index in range(length):
            for sub_index in range(index + 1, length):
                current_dist = Points.dist(points_set[index], points_set[sub_index])
                if current_dist < min_dist:
                    min_dist = current_dist
                    horizontal_point = points_set[index]
                    vertical_point = points_set[sub_index]
        return horizontal_point, vertical_point, min_dist


#####################################################################################################################################################

#####################################################################################################################################################



def divide_and_conquer(X, Y):
    # Extracting the size of the set_point set
    set_size = len(X)

    # Minimizing recursion for small sets
    if set_size <= 4:
        return Points.merge_sort_closest(X, set_size)
    else:
       
        mid_axis_line = X[set_size // 2]

     
        horizontal_left_split = X[:set_size // 2]

        
        horizontal_right_split = X[set_size // 2:]

        
        vertical_left_split = []
        vertical_right_split = []

        
        for set_point in Y:
            vertical_left_split.append(set_point) if (
                        set_point[0] <= mid_axis_line[0]) else vertical_right_split.append(set_point)

        (point_one_left, point_two_left, min_distance_left_part_axis) = divide_and_conquer(horizontal_left_split,
                                                                                           vertical_left_split)

       (point_one_right, point_two_right, min_distance_right_part_axis) = divide_and_conquer(horizontal_right_split,
                                                                                              vertical_right_split)

        (horizontal_point, vertical_point, current_minimum_distance) = (
        point_one_left, point_two_left, min_distance_left_part_axis) if (
                    min_distance_left_part_axis < min_distance_right_part_axis) else (
        point_one_right, point_two_right, min_distance_right_part_axis)
        generated_set = [set_point for set_point in Y if
                         mid_axis_line[0] - current_minimum_distance < set_point[0] < mid_axis_line[
                             0] + current_minimum_distance]
        for index_generated_set in range(len(generated_set)):
            for sub_index_generated_set in range(index_generated_set + 1,
                                                 min(index_generated_set + 7, len(generated_set))):
                left_generated_set_point = generated_set[index_generated_set]
                right_generated_set_point = generated_set[sub_index_generated_set]
                current_generated_distance = Points.dist(left_generated_set_point, right_generated_set_point)
                if current_generated_distance < current_minimum_distance:
                    (horizontal_point, vertical_point, current_minimum_distance) = (
                    generated_set[index_generated_set], generated_set[sub_index_generated_set],
                    current_generated_distance)
        Points.set_minimum_dist(current_minimum_distance)
        return horizontal_point, vertical_point


#####################################################################################################################################################

#####################################################################################################################################################

def merge_and_sort(input_array, p, length):
    if p < length:

        # Calculating mid-set of the input array for further process
        # n1 = q-p+2 ; n2 = r-q+1
        mid = len(input_array) // 2

        left = input_array[:mid]
        right = input_array[mid:]

        
        q = math.floor((p + length) / 2)

        # Recursive call on each half & subdividing the input
        
        merge_and_sort(left, p, q)
        
        merge_and_sort(right, q + 1, length)

        # Performing iterations for two sides 
        left_index = 0
        right_index = 0

        # Performing iteration for entire list
        index = 0

        while left_index < len(left) and right_index < len(right):
            
            if left[left_index] <= right[right_index]:
                
                input_array[index] = left[left_index]
                
                left_index += 1
            else:
                
                input_array[index] = right[right_index]
                
                right_index += 1
            # Move to the next slot
            index += 1

        # combining the result of the recursive calls
        while left_index < len(left):
            input_array[index] = left[left_index]
            left_index += 1
            index += 1

        while right_index < len(right):
            input_array[index] = right[right_index]
            right_index += 1
            index += 1

    return input_array


#####################################################################################################################################################

#####################################################################################################################################################
def perform_tasks(points):
    length_of_points = len(points)
    # Performing merge and sort as per the task 3 on X set of points
    sorted_X = merge_and_sort(points, 1, length_of_points)
    sorted_Y = sorted(points, key=lambda set_point: points[1])
    return divide_and_conquer(sorted_X, sorted_Y)


if __name__ == "__main__":
    set_of_points = [[2, 4], [12, 31], [42, 51], [3, 1], [11, 10], [13, 14]]
    print('Input Points -> ', set_of_points)
    perform_tasks(set_of_points)
    print('The Minimum Distance between the points ->', Points.minimum_distance)

    print(' ')
    print('#### Trying with random points ###')
    # Trying with random points
    set_random_points = Points.generate_random_points(5, 0.1)
    print('Input Random Points -> ', set_random_points)
    perform_tasks(set_random_points)
    print('The Minimum Distance between the random points ->', Points.minimum_distance)
