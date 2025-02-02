import numpy as np
from compas.geometry import Polyhedron
from compas.datastructures import Mesh
from compas_cgal._cgal import subdivision
from compas_view2.app import App

shape = Polyhedron.from_platonicsolid(20)
mesh = Mesh.from_shape(shape)

V, F = mesh.to_vertices_and_faces()
V, F = subdivision.subd_catmullclark(np.asarray(V, dtype=np.float64), F, 2)

shape = Polyhedron(V, F)

viewer = App()
viewer.add(shape)
viewer.show()
