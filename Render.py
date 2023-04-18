import numpy as np
from mayavi import mlab
from scipy.spatial.transform import Rotation as R

class Render:
    def __init__(self, filename):
        self.vertices = [] # vertices represent points in 3D space
        self.normals = [] # normals represent the normal vectors of the surfaces where the points are located
        self.faces = [] # faces mean a patch composed of vertices

        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('Vertex'):
                    vertex_data = line.split()
                    x, y, z = float(vertex_data[2]), float(vertex_data[3]), float(vertex_data[4])
                    self.vertices.append([x, y, z])
                    nx, ny, nz = float(vertex_data[5][9:]), float(vertex_data[6]), float(vertex_data[7][:-2])
                    self.normals.append([nx, ny, nz])
                elif line.startswith('Face'):
                    face_data = line.split()
                    v1, v2, v3 = int(face_data[2]) - 1, int(face_data[3]) - 1, int(face_data[4]) - 1
                    self.faces.append([v1, v2, v3])

        # list to NumPy array
        self.vertices = np.array(self.vertices)
        self.normals = np.array(self.normals)
        self.faces = np.array(self.faces)
        

    def visualize(self, joycon):
        # Create a triangular mesh object and add it to the scene
        mesh = mlab.triangular_mesh(self.vertices[:, 0], self.vertices[:, 1], self.vertices[:, 2], self.faces)
        mesh.mlab_source.dataset.point_data.normals = self.normals
        mesh.mlab_source.update()


        # Add a plane at the bottom of the bunny in the XZ plane
        xmin, xmax, ymin, ymax, zmin, zmax = self.vertices[:, 0].min(), self.vertices[:, 0].max(), \
                                              self.vertices[:, 1].min(), self.vertices[:, 1].max(), \
                                              self.vertices[:, 2].min(), self.vertices[:, 2].max()
        x = np.linspace(xmin, 0.3, 10)
        z = np.linspace(zmin, 0.3, 10)
        xx, zz = np.meshgrid(x, z)
        yy = np.zeros_like(xx)
        yy.fill(ymin)
        mlab.mesh(xx, yy, zz, representation='wireframe', color=(0, 0, 0))

        @mlab.animate(delay=10)
        def anim():
            scale_factor = 1.0

            while True:
                # Rotate
                # Convert rotation angle to rotation matrix
                rotation_matrix = 30*R.from_euler('xyz', joycon.rotation).as_matrix()
                # Apply the rotation matrix to the orientation property of the 3D object
                mesh.actor.actor.orientation = tuple(rotation_matrix.flatten()[:3]) #Euler angles from -180-180
                
                for event_type, status in joycon.events():
                    
                    # Zoom in and out
                    if event_type == 'right_sr' and status == 1:
                        scale_factor *= 0.8
                        mesh.actor.actor.scale = (scale_factor, scale_factor, scale_factor)
                    if event_type == 'right_sl' and status == 1:
                        scale_factor /= 0.8
                        mesh.actor.actor.scale = (scale_factor, scale_factor, scale_factor)
                    
                    # Move along x-axis
                    if event_type == 'a' and status == 1:
                        old_pos = mesh.actor.actor.position
                        mesh.actor.actor.position = (old_pos[0]+0.01, old_pos[1], old_pos[2])
                    if event_type == 'y' and status == 1:
                        old_pos = mesh.actor.actor.position
                        mesh.actor.actor.position = (old_pos[0]-0.01, old_pos[1], old_pos[2])
                    # Move along z-axis
                    if event_type == 'b' and status == 1:
                        old_pos = mesh.actor.actor.position
                        mesh.actor.actor.position = (old_pos[0], old_pos[1], old_pos[2]+0.01)
                    if event_type == 'x' and status == 1:
                        old_pos = mesh.actor.actor.position
                        mesh.actor.actor.position = (old_pos[0], old_pos[1], old_pos[2]-0.01)
                    # Move along y-axis
                    if event_type == 'zr' and status == 1:
                        old_pos = mesh.actor.actor.position
                        mesh.actor.actor.position = (old_pos[0], old_pos[1]+0.01, old_pos[2])
                    if event_type == 'r' and status == 1:
                        old_pos = mesh.actor.actor.position
                        mesh.actor.actor.position = (old_pos[0], old_pos[1]-0.01, old_pos[2])
                
                yield

        anim()
        mlab.show()