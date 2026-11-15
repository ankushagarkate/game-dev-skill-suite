# DDA Raycasting, ECS & Allocator Internals

## Digital Differential Analyzer (DDA) Grid Raycaster
```cpp
// 2D grid raycasting (Wolfenstein 3D style)
struct RaycastResult {
    int mapX, mapY;
    int side; // 0 for X-wall, 1 for Y-wall
    float perpWallDist;
};

RaycastResult castRay(float posX, float posY, float rayDirX, float rayDirY, const int map[MAP_H][MAP_W]) {
    int mapX = int(posX);
    int mapY = int(posY);

    float deltaDistX = (rayDirX == 0) ? 1e30f : std::abs(1.0f / rayDirX);
    float deltaDistY = (rayDirY == 0) ? 1e30f : std::abs(1.0f / rayDirY);

    int stepX = (rayDirX < 0) ? -1 : 1;
    int stepY = (rayDirY < 0) ? -1 : 1;

    float sideDistX = (rayDirX < 0) ? (posX - mapX) * deltaDistX : (mapX + 1.0f - posX) * deltaDistX;
    float sideDistY = (rayDirY < 0) ? (posY - mapY) * deltaDistY : (mapY + 1.0f - posY) * deltaDistY;

    bool hit = false;
    int side = 0;
    while (!hit) {
        if (sideDistX < sideDistY) {
            sideDistX += deltaDistX;
            mapX += stepX;
            side = 0;
        } else {
            sideDistY += deltaDistY;
            mapY += stepY;
            side = 1;
        }
        if (map[mapY][mapX] > 0) hit = true;
    }

    // Perpendicular distance avoids fisheye distortion
    float perpWallDist = (side == 0) ? (sideDistX - deltaDistX) : (sideDistY - deltaDistY);
    return { mapX, mapY, side, perpWallDist };
}
```

## Linear Linear/Stack Allocator Pattern
```cpp
class LinearAllocator {
    uint8_t* buffer;
    size_t capacity;
    size_t offset;
public:
    LinearAllocator(size_t size) : capacity(size), offset(0) {
        buffer = new uint8_t[size];
    }
    ~LinearAllocator() { delete[] buffer; }

    void* allocate(size_t size, size_t alignment = 16) {
        size_t current = (size_t)(buffer + offset);
        size_t padding = (alignment - (current % alignment)) % alignment;
        if (offset + padding + size > capacity) return nullptr; // Out of memory
        offset += padding;
        void* ptr = buffer + offset;
        offset += size;
        return ptr;
    }

    void reset() { offset = 0; } // Instant O(1) frame teardown
};
```
