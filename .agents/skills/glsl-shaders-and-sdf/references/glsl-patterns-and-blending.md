# GLSL Patterns, SDFs & Blend Modes

## Essential Snippets

### 2D Rotation Matrix
```glsl
mat2 rotate2d(float angle) {
    return mat2(cos(angle), -sin(angle),
                sin(angle),  cos(angle));
}
```

### 2D Box SDF
```glsl
float sdBox(vec2 p, vec2 b) {
    vec2 d = abs(p) - b;
    return length(max(d, 0.0)) + min(max(d.x, d.y), 0.0);
}
```

### Smooth Anti-Aliased SDF Fill
```glsl
float aa = fwidth(d); // or 1.5 / u_resolution.y
float mask = 1.0 - smoothstep(-aa, aa, d);
```

### Deterministic 2D Hash & Value Noise
```glsl
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

float noise(vec2 st) {
    vec2 i = floor(st);
    vec2 f = fract(st);
    vec2 u = f * f * (3.0 - 2.0 * f);
    return mix(mix(random(i + vec2(0.0, 0.0)), random(i + vec2(1.0, 0.0)), u.x),
               mix(random(i + vec2(0.0, 1.0)), random(i + vec2(1.0, 1.0)), u.x), u.y);
}
```

### Fractal Brownian Motion (fBM)
```glsl
float fbm(vec2 st) {
    float value = 0.0;
    float amp = 0.5;
    for (int i = 0; i < 5; i++) {
        value += amp * noise(st);
        st *= 2.0;
        amp *= 0.5;
    }
    return value;
}
```

### Common Blend Modes
- **Multiply**: `base * blend`
- **Screen**: `1.0 - (1.0 - base) * (1.0 - blend)`
- **Overlay**: `mix(2.0 * base * blend, 1.0 - 2.0 * (1.0 - base) * (1.0 - blend), step(0.5, base))`
