# 2D Rotational Matrix

In two-dimensional space, a rotation matrix is a 2x2 matrix that represents a transformation from a local frame to a global frame


> The standard rotation matrix has the following form:

![Alt Text](https://wikimedia.org/api/rest_v1/media/math/render/svg/f634dcca650647858444511d84cb6e228f9682eb)

> Thus, the new coordinates (x′, y′) of a point (x, y) after rotation are

![Alt Text](https://wikimedia.org/api/rest_v1/media/math/render/svg/cdf8017414ac9ea8dbdbaa644c4439cad105f244)

Where:
- `(x', y')`: The coordinates of the global points.
- `(x, y)`: The original coordinates of local points.
- `cos(theta)` and `sin(theta)` are the cosine and sine of the angle `theta`.