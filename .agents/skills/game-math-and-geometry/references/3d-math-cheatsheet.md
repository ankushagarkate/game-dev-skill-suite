# 3D Math Formulas & Intersection Cheatsheet

## Vector Operations

- **Normalize**: `v_hat = v / ||v||` (guard against `||v|| < eps`).
- **Reflect vector `v` across unit normal `n`**: `r = v - 2 * (v · n) * n`.
- **Project `a` onto unit vector `u`**: `a_parallel = (a · u) * u`, `a_perp = a - a_parallel`.

## Quaternions

- **Axis-angle `(n_hat, theta)` to Quaternion**:
  - `w = cos(theta / 2)`
  - `(x, y, z) = n_hat * sin(theta / 2)`
- **Inverse of unit quaternion**: Conjugate `q* = [w, -v]`.
- **Rotate vector `p` by unit quaternion `q`**: `p' = q * [0, p] * q*`.
- **SLERP (`q0` to `q1` at `t in [0, 1]`)**:
  1. `cos_omega = dot(q0, q1)`
  2. If `cos_omega < 0`: `q1 = -q1`, `cos_omega = -cos_omega`
  3. If `cos_omega > 0.9995`: use normalized lerp (`nlerp`) to avoid division by zero.
  4. Else: `omega = acos(cos_omega)`, `k0 = sin((1 - t) * omega) / sin(omega)`, `k1 = sin(t * omega) / sin(omega)`.

## Fast Intersection Tests

### Ray vs. Plane (`p(t) = o + t*d`, `p · n = dist`)
- `denom = dot(d, n)`
- If `|denom| < eps`, ray is parallel.
- `t = (dist - dot(o, n)) / denom`; hit if `t >= 0`.

### Ray vs. AABB (Slab Method)
For each axis `i in {x, y, z}`:
- `t0 = (min[i] - o[i]) / d[i]`, `t1 = (max[i] - o[i]) / d[i]`
- Swap `t0, t1` if `d[i] < 0`
- `t_min = max(t_min, t0)`, `t_max = min(t_max, t1)`
- Intersects iff `t_max >= max(t_min, 0)`.

### Sphere vs. Sphere
- Centers `c1, c2`, radii `r1, r2`.
- Intersects iff `dot(c2 - c1, c2 - c1) <= (r1 + r2)^2`.

### Point in Triangle (Barycentric)
Given triangle `A, B, C` and coplanar point `P`:
- `v0 = B - A`, `v1 = C - A`, `v2 = P - A`
- Solve 2x2 system via dot products (`d00, d01, d11, d20, d21`) for `(v, w)` and `u = 1 - v - w`.
- Inside iff `u >= 0 and v >= 0 and w >= 0`.
