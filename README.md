# The Social Network
[![es](https://img.shields.io/badge/lang-es-red.svg)](/README-ES.md)

This repository holds a two-part homework assignment from the subject _Estructuras de Datos y Algoritmos_ (Data Structures and Algorithms) of Computer Science at the University of Valladolid. The main purpose was to find out how efficient data structures could heavily improve performance.

Its design is based on a _social network_, in the sense that there are multiple users, with multiple (bidirectional) connections with each other. The objective of this program is to identify _grumos_, which are groups of users connected (directly, or via another user) with each other. The following image shows 15 users forming 4 _grumos_:

![Grumos](/readme-files/grumos1.jpg "Grumos")

The social network tries to keep users as connected as possible with the rest of the platform. In other words, we are looking to have as many users as possible on the same _grumo_.
With this in mind, the program takes in a percentage marking how many users you want to be on the largest _grumo_, and calculates the least amount of connections needed to make it.

The picture below shows the example of the previous image when the percentage is fixed at 85%. The 3 biggest _grumos_ are joined, making the largest _grumo_ hold 87% of the users.

![Grumos 2](/readme-files/grumos2.jpg "Grumos 2")

Some input files representing networks are located at the folder [testfiles](testfiles/).
After its execution, the needed connections are printed via standard output and also written to a text file called `extra.txt`. For completeness and testing purposes, this file can be provided when running the program to verify the conditions are met (no new connections are needed).

Remember the purpose of the assignment was to learn about data structures, algorithms and their efficency. That is why at several points the program prints how much time each part has taken to compute.

There are tow implementations of this program:
1. The first version was made using typical tools in programming: lists/arrays and associated methods (`sort`, `append`, `in`...). It is held on a single [file](original_unoptimized.py). Although able to carry out the job, the efficency was pretty bad. Trying to process the biggest networks would take too much time.

2. The second version applies knowledge of the subject to improve the program and reduce the time needed to process the network. The way of achieving this was using a [_disjoint-set_](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) to represent the network and its users. After this and some other modifications, trying to process the biggest networks (2000000 connections) was possible. To run this version use the file [optimized.py](optimized.py). The rest of the files contain code to represent _grumos_ and users.

Part of this assignment was learning to become a better programmer, and that is why two different ways of commenting code are used. Both code and comments are written in Spanish.