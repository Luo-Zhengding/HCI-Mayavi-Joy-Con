# HCI-Mayavi-Joy-Con
The interaction interface is mainly based on the Mayavi platform and the Nintendo Switch Joy-Con controller.
This is a course assignment of CE6121 in Nanyang Technological University (NTU).
The author is Zhengding Luo, a PhD student in NTU.

For this assignment, an interface for visualizing three-dimensional (3D) models is developed via the Mayavi platform. The interface is an interactive tool for displaying 3D models based on triangle meshes. Instead of using traditional input devices like a mouse or keyboard, the Nintendo Joy-Con Controller is exploited to rotate, translate, and zoom the 3D model.

<img width="778" alt="2(1)" src="https://user-images.githubusercontent.com/95018034/232702595-15af0a76-f8a7-4455-9c9a-9fba62896a72.PNG">
<img width="678" alt="2(2)" src="https://user-images.githubusercontent.com/95018034/232702616-14b777ac-ab2a-46fe-ae07-a8ebeef3955b.PNG">

Programming language: Python

Joy-Con code reference:
https://github.com/tocoteron/joycon-python

The interaction is based on the gyroscope and Button events of the Joy-Con controller.

• Rotation: The 3D model can be rotated along the x, y, and z axes by changing the orientation property of the 3D model using the rotation matrix, which is obtained from the Joy-Con's orientation data.

• Scaling: We can zoom in and out by changing the scale of the object using the Joy-Con's buttons 'right_sr' and 'right_sl', respectively.

• Translation: We can move the Bunny model along the x, y, and z axes by using the Joy-Con's 'A', 'Y', 'B', 'Z', 'ZR' and 'R' buttons.
