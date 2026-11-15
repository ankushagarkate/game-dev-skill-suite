---
name: game-math-and-geometry
description: Solve 3D game math, coordinate space transforms, vector/matrix/quaternion rotations, geometric intersection tests, and triangle mesh topology problems. Use when implementing physics, camera rigs, raycasts, procedural geometry, or graphics math.
---

# 3D Game Math & Geometry

Use consistent coordinate conventions, numerically stable orientation representations, and exact geometric intersection tests.

## 1. Coordinate Spaces & Conventions

Always verify handedness and vector convention before writing transform code:

- **Handedness**:
  - **Left-handed** (e.g., DirectX): `+X` right, `+Y` up, `+Z` forward.
  - **Right-handed** (e.g., OpenGL, Panda3D `+Z` up): verify whether `+Y` or `+Z` is up.
- **Matrix Multiplication Order**:
  - **Row vectors** (`v' = v * M`): transforms compose left-to-right (`v * M_scale * M_rot * M_trans`).
  - **Column vectors** (`v' = M * v`): transforms compose right-to-left (`M_trans * M_rot * M_scale * v`).
- **Standard Space Chain**: Object Space -> World Space -> Camera (View) Space -> Clip Space -> Screen Space.

## 2. Vectors & Matrices

- **Dot Product** (`a · b = |a||b|cos θ`): Use for facing checks (`> 0` same hemisphere), projection (`proj_b(a) = (a·b̂)b̂`), and plane distances.
- **Cross Product** (`a × b`): Produces a perpendicular vector with magnitude `|a||b|sin θ` (handedness determines direction). Use for surface normals and orthonormal basis construction.
- **Homogeneous Coordinates (`4×4` / `4×3`)**: Represent affine transforms (linear rotation/scale + translation) cleanly.
- **Matrix Creep**: Repeatedly multiplying rotation matrices introduces floating-point drift. Periodically re-orthogonalize using **Gram-Schmidt orthogonalization** or store orientation as a unit quaternion.

## 3. 3D Orientation: Matrices vs. Euler vs. Quaternions

| Representation | Best Use Case | Key Pitfall |
| :--- | :--- | :--- |
| **Rotation Matrix** | GPU shaders, transforming many vertices | 9 floats; matrix creep over time |
| **Euler Angles** (Heading-Pitch-Bank) | Inspector UI, human-readable angles | **Gimbal lock** at `±90°` pitch; bad interpolation |
| **Quaternion** (`[w, (x, y, z)]`) | Smooth interpolation (`slerp`/`squad`), physics state | Must stay unit-length (`normalize()`) |

- Canonical Euler ranges: Heading `[-180°, 180°]`, Pitch `[-90°, 90°]`, Bank `[-180°, 180°]`.
- For shortest-path quaternion `slerp(q0, q1, t)`, negate `q1` if `dot(q0, q1) < 0`.

## 4. Geometric Primitives & Intersection Tests

- **Ray**: `p(t) = p0 + t * d` (`t >= 0`).
- **Plane**: `p · n = d` (where `n` is unit normal). Signed distance from point `q` to plane is `q · n - d`.
- **AABB (`AABB3`)**: Fast broad-phase bounds; update via transformed extents rather than transforming 8 corners naively when possible.
- **Barycentric Coordinates `(u, v, w)`**: `u + v + w = 1`; point is inside triangle iff `u, v, w >= 0`. Essential for ray-triangle intersection and attribute interpolation.
- **Dynamic vs. Static Tests**: Prefer swept/dynamic intersection tests (e.g., moving sphere vs. plane, ray vs. AABB slab method) for fast projectiles to prevent tunneling.

## 5. Triangle Meshes

- Use **indexed triangle lists** to share vertices and exploit GPU post-transform vertex caches.
- **Weld vertices** only where positions, normals, and UVs match; **detach faces** across hard edges or UV seams.

## References

- [3D Math Formulas & Intersection Cheatsheet](references/3d-math-cheatsheet.md)
